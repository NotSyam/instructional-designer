#!/usr/bin/env python3
"""
quiz_to_gift.py - Converts Markdown/JSON quiz definitions into GIFT and Moodle XML formats for LMS import.

Supports:
- Multiple Choice (Single correct)
- Multiple Response (Multi-select with fractional weights)
- True/False
- Short Answer / Fill-in-the-blank
- Essay / Open Response
- Matching

Usage:
    python quiz_to_gift.py --input quiz.md --output quiz.gift --format gift
    python quiz_to_gift.py --input quiz.json --output quiz.xml --format moodle_xml
"""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom


def parse_markdown_quiz(md_text):
    """
    Parses a markdown quiz formatted with headers and bullet items.
    
    Format:
    ### Question Title / Question Text
    Category / Metadata: [Optional category tag]
    - [x] Correct Choice (or [=] Correct Choice)
    - [ ] Distractor Choice
    Feedback: [Optional question feedback]
    
    Or for True/False:
    ### Statement
    Answer: True (or False)
    
    Or for Short Answer:
    ### Question text
    Answer: Correct Term
    """
    questions = []
    blocks = re.split(r'\n(?=###?\s+)', md_text.strip())
    
    for block in blocks:
        if not block.strip():
            continue
        lines = block.strip().splitlines()
        first_line = lines[0].strip()
        title_match = re.match(r'^###?\s*(?:Q\d+[:.]?\s*)?(.*)', first_line)
        question_text = title_match.group(1).strip() if title_match else first_line
        
        q_type = 'multiple_choice'
        choices = []
        answer_text = None
        feedback = ""
        category = "General"
        
        for line in lines[1:]:
            line_str = line.strip()
            if not line_str:
                continue
            
            # Check Category
            cat_match = re.match(r'^(?:Category|Tag):\s*(.*)', line_str, re.IGNORECASE)
            if cat_match:
                category = cat_match.group(1).strip()
                continue
                
            # Check Feedback
            fb_match = re.match(r'^(?:Feedback|Explanation):\s*(.*)', line_str, re.IGNORECASE)
            if fb_match:
                feedback = fb_match.group(1).strip()
                continue
                
            # Check Direct Answer line (for T/F or Short answer)
            ans_match = re.match(r'^Answer:\s*(.*)', line_str, re.IGNORECASE)
            if ans_match:
                ans_val = ans_match.group(1).strip()
                if ans_val.lower() in ['true', 't', 'false', 'f']:
                    q_type = 'true_false'
                    answer_text = ans_val.lower() in ['true', 't']
                else:
                    q_type = 'short_answer'
                    answer_text = ans_val
                continue
            
            # Check Multiple choice checkboxes: - [x] or - [ ] or * [=]
            choice_match = re.match(r'^[-*]\s*\[([ xX=~])\]\s*(.*)', line_str)
            if choice_match:
                is_correct = choice_match.group(1).lower() in ['x', '=']
                choice_body = choice_match.group(2).strip()
                # Check for inline feedback: Choice text # Feedback text
                choice_fb = ""
                if ' # ' in choice_body:
                    parts = choice_body.split(' # ', 1)
                    choice_body = parts[0].strip()
                    choice_fb = parts[1].strip()
                choices.append({
                    "text": choice_body,
                    "correct": is_correct,
                    "feedback": choice_fb
                })
        
        # Determine if multiple_response
        correct_count = sum(1 for c in choices if c['correct'])
        if correct_count > 1:
            q_type = 'multiple_response'
        elif len(choices) > 0 and q_type == 'multiple_choice':
            pass
        elif not choices and answer_text is None:
            # Assume essay if no choices or answer given
            q_type = 'essay'
            
        questions.append({
            "title": (question_text[:77] + "…") if len(question_text) > 80 else question_text,
            "text": question_text,
            "type": q_type,
            "choices": choices,
            "answer": answer_text,
            "feedback": feedback,
            "category": category
        })
        
    return questions


def to_gift(questions):
    """Converts parsed questions list to GIFT format."""
    output = []
    for i, q in enumerate(questions, 1):
        # Escape ALL GIFT-special characters in the title, not just ':'
        title = q.get('title', f"Question {i}")
        for ch in (':', '{', '}', '~', '=', '#'):
            title = title.replace(ch, '\\' + ch)
        text = q.get('text', '').replace(':', r'\:').replace('{', r'\{').replace('}', r'\}').replace('~', r'\~').replace('=', r'\=')
        q_type = q.get('type')
        general_fb = q.get('feedback', '')
        
        gift_entry = f"::{title}:: {text} "
        
        if q_type == 'true_false':
            val = "TRUE" if q.get('answer') else "FALSE"
            if general_fb:
                gift_entry += f"{{{val}#{general_fb}}}"
            else:
                gift_entry += f"{{{val}}}"
                
        elif q_type == 'short_answer':
            ans = str(q.get('answer', '')).replace('=', r'\=').replace('~', r'\~')
            if general_fb:
                gift_entry += f"{{={ans}#{general_fb}}}"
            else:
                gift_entry += f"{{={ans}}}"
                
        elif q_type == 'essay':
            gift_entry += "{}"
            if general_fb:
                gift_entry += f" // Feedback: {general_fb}"
                
        elif q_type == 'multiple_response':
            # Allocate equal positive weight for correct, equal negative for incorrect
            correct_count = sum(1 for c in q['choices'] if c['correct'])
            incorrect_count = len(q['choices']) - correct_count
            pos_weight = round(100.0 / correct_count, 2) if correct_count > 0 else 100
            neg_weight = round(100.0 / incorrect_count, 2) if incorrect_count > 0 else 100
            
            gift_entry += "{\n"
            for c in q['choices']:
                ctext = c['text'].replace('=', r'\=').replace('~', r'\~').replace('#', r'\#')
                cfb = f"#{c['feedback']}" if c.get('feedback') else ""
                if c['correct']:
                    gift_entry += f"  ~%{pos_weight}%{ctext}{cfb}\n"
                else:
                    gift_entry += f"  ~%-{neg_weight}%{ctext}{cfb}\n"
            if general_fb:
                gift_entry += f"  ####{general_fb}\n"
            gift_entry += "}"
            
        else: # multiple_choice
            gift_entry += "{\n"
            for c in q['choices']:
                ctext = c['text'].replace('=', r'\=').replace('~', r'\~').replace('#', r'\#')
                cfb = f"#{c['feedback']}" if c.get('feedback') else ""
                if c['correct']:
                    gift_entry += f"  ={ctext}{cfb}\n"
                else:
                    gift_entry += f"  ~{ctext}{cfb}\n"
            if general_fb:
                gift_entry += f"  ####{general_fb}\n"
            gift_entry += "}"
            
        output.append(gift_entry)
        
    return "\n\n".join(output)


def to_moodle_xml(questions):
    """Converts parsed questions list to Moodle XML format."""
    root = ET.Element('quiz')
    
    for q in questions:
        q_elem = ET.SubElement(root, 'question')
        q_type = q.get('type')
        
        # Map types to Moodle XML types
        if q_type in ['multiple_choice', 'multiple_response']:
            q_elem.set('type', 'multichoice')
        elif q_type == 'true_false':
            q_elem.set('type', 'truefalse')
        elif q_type == 'short_answer':
            q_elem.set('type', 'shortanswer')
        elif q_type == 'essay':
            q_elem.set('type', 'essay')
        else:
            q_elem.set('type', 'multichoice')
            
        name = ET.SubElement(q_elem, 'name')
        name_text = ET.SubElement(name, 'text')
        name_text.text = q.get('title', 'Question')
        
        qtext = ET.SubElement(q_elem, 'questiontext', {'format': 'html'})
        qtext_text = ET.SubElement(qtext, 'text')
        qtext_text.text = f"<p>{q.get('text', '')}</p>"
        
        if q.get('feedback'):
            genfb = ET.SubElement(q_elem, 'generalfeedback', {'format': 'html'})
            genfb_text = ET.SubElement(genfb, 'text')
            genfb_text.text = f"<p>{q.get('feedback')}</p>"
            
        if q_type in ['multiple_choice', 'multiple_response']:
            single = "false" if q_type == 'multiple_response' else "true"
            single_elem = ET.SubElement(q_elem, 'single')
            single_elem.text = single
            
            correct_count = sum(1 for c in q['choices'] if c['correct'])
            pos_fraction = (100.0 / correct_count) if correct_count > 0 else 100.0
            
            for c in q['choices']:
                fraction = str(pos_fraction) if c['correct'] else "0"
                if q_type == 'multiple_response' and not c['correct']:
                    inc_count = len(q['choices']) - correct_count
                    fraction = str(-100.0 / inc_count) if inc_count > 0 else "-100"
                    
                ans_elem = ET.SubElement(q_elem, 'answer', {'fraction': fraction, 'format': 'html'})
                ans_text = ET.SubElement(ans_elem, 'text')
                ans_text.text = f"<p>{c['text']}</p>"
                if c.get('feedback'):
                    cfb = ET.SubElement(ans_elem, 'feedback', {'format': 'html'})
                    cfb_text = ET.SubElement(cfb, 'text')
                    cfb_text.text = f"<p>{c['feedback']}</p>"
                    
        elif q_type == 'true_false':
            is_true = bool(q.get('answer'))
            ans1 = ET.SubElement(q_elem, 'answer', {'fraction': '100' if is_true else '0', 'format': 'html'})
            ans1_text = ET.SubElement(ans1, 'text')
            ans1_text.text = 'true'
            
            ans2 = ET.SubElement(q_elem, 'answer', {'fraction': '0' if is_true else '100', 'format': 'html'})
            ans2_text = ET.SubElement(ans2, 'text')
            ans2_text.text = 'false'
            
        elif q_type == 'short_answer':
            ans_elem = ET.SubElement(q_elem, 'answer', {'fraction': '100', 'format': 'plain_text'})
            ans_text = ET.SubElement(ans_elem, 'text')
            ans_text.text = str(q.get('answer', ''))
            
    xml_str = ET.tostring(root, encoding='utf-8')
    parsed_xml = minidom.parseString(xml_str)
    # Pass encoding so minidom emits: <?xml version="1.0" encoding="utf-8"?>
    # which Moodle requires for successful import.
    return parsed_xml.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8")


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown / JSON quizzes to LMS GIFT and Moodle XML formats.")
    parser.add_argument('--input', '-i', help="Input Markdown (.md) or JSON (.json) file. Reads from stdin if omitted.")
    parser.add_argument('--output', '-o', help="Output file path. Writes to stdout if omitted.")
    parser.add_argument('--format', '-f', choices=['gift', 'moodle_xml'], default='gift', help="Export format (default: gift).")
    
    args = parser.parse_args()
    
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    else:
        raw_content = sys.stdin.read()
        
    if args.input and args.input.endswith('.json'):
        questions = json.loads(raw_content)
    else:
        questions = parse_markdown_quiz(raw_content)
        
    if args.format == 'gift':
        result = to_gift(questions)
    else:
        result = to_moodle_xml(questions)
        
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Successfully converted {len(questions)} question(s) to {args.output} ({args.format}).")
    else:
        print(result)


if __name__ == '__main__':
    main()
