#!/usr/bin/env python3
"""
outline_to_slides.py - Converts course blueprints and lesson plans into Marp-ready presentation decks.

Features:
- Standard Marp YAML frontmatter (customizable theme, pagination, header/footer)
- Automatic slide segmentation (title, agenda, objectives, content chunking, breakout exercises)
- Speaker notes generation (using <!-- Notes --> comments)
- Clean visual callouts and typography

Usage:
    python outline_to_slides.py --input lesson_plan.md --output presentation.marp.md --theme gaia
"""

import argparse
import re
import sys


def generate_marp_deck(markdown_content, title="Learning Session", theme="default"):
    """Converts markdown syllabus/lesson plan into Marp presentation slides."""
    slides = []
    
    # Frontmatter
    frontmatter = f"""---
marp: true
theme: {theme}
paginate: true
header: "**{title}**"
footer: "Instructional Design Output"
style: |
  section.lead {{
    text-align: center;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    color: white;
  }}
  section.activity {{
    background: #f4f7f6;
    border-left: 10px solid #2a5298;
  }}
  .callout {{
    background: #e8f4fd;
    padding: 12px;
    border-radius: 6px;
    border-left: 4px solid #0284c7;
    margin-top: 10px;
  }}
---
"""
    slides.append(frontmatter.strip())
    
    # Title Slide
    title_match = re.search(r'^#\s+(.*)', markdown_content, re.MULTILINE)
    deck_title = title_match.group(1).strip() if title_match else title
    
    title_slide = f"""<!-- _class: lead -->

# {deck_title}

### Interactive Workshop & Learning Experience

---"""
    slides.append(title_slide)
    
    # Split content by major sections (## or ###)
    sections = re.split(r'\n?(?=^## )', markdown_content, flags=re.MULTILINE)
    
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
            
        lines = sec.splitlines()
        header_match = re.match(r'^##\s+(.*)', lines[0])
        sec_header = header_match.group(1).strip() if header_match else "Overview"
        
        # Don't duplicate overall document title
        if sec_header == deck_title:
            continue
            
        body_lines = lines[1:]
        body_text = "\n".join(body_lines).strip()
        
        # Skip empty preamble chunks (everything before the first '## ' heading)
        if header_match is None and not body_text:
            continue
        
        # Check if section represents an activity / practice
        is_activity = any(kw in sec_header.lower() for kw in ['activity', 'practice', 'role-play', 'scenario', 'exercise', 'breakout'])
        
        slide_class = "<!-- _class: activity -->\n\n" if is_activity else ""
        
        # Extract speaker notes if any (lines starting with 'Say:' or 'Facilitator:')
        # Notes are attached only to the FIRST slide of a section so they are not duplicated.
        regular_lines = []
        notes_lines = []
        
        for line in body_lines:
            if re.match(r'^(?:Say|Facilitator Script|Note|Speaker):\s*(.*)', line.strip(), re.IGNORECASE):
                notes_lines.append(line.strip())
            else:
                regular_lines.append(line)
                
        cleaned_body = "\n".join(regular_lines).strip()
        section_notes_block = ""
        if notes_lines:
            section_notes_block = "\n\n<!--\nSpeaker Notes:\n" + "\n".join(notes_lines) + "\n-->"
        
        # Chunk very long bodies into multiple sub-slides if needed
        sub_blocks = re.split(r'\n(?=###\s+)', cleaned_body)
        first_slide_done = False
        
        if len(sub_blocks) > 1 and not is_activity:
            for sub in sub_blocks:
                sub = sub.strip()
                if not sub:
                    continue
                sub_lines = sub.splitlines()
                # Strip leading markdown hashes before re-adding the target level
                sub_header = re.sub(r'^#+\s*', '', sub_lines[0]).strip()
                sub_body = "\n".join(sub_lines[1:]).strip()
                
                slide_content = f"{slide_class}## {sub_header}\n\n{sub_body}"
                # Attach speaker notes to the FIRST slide of this section only
                if not first_slide_done and section_notes_block:
                    slide_content += section_notes_block
                    first_slide_done = True
                slides.append(slide_content.strip() + "\n\n---")
        else:
            slide_content = f"{slide_class}## {sec_header}\n\n{cleaned_body}"
            if section_notes_block:
                slide_content += section_notes_block
                first_slide_done = True
            slides.append(slide_content.strip() + "\n\n---")
            
    # Closing Action Slide
    closing_slide = """<!-- _class: lead -->

# Action Commitment & Next Steps

* What is 1 action you will apply in the next 48 hours?
* Complete the quick feedback evaluation.

**Thank you for your active participation!**"""
    slides.append(closing_slide)
    
    return "\n\n".join(slides)


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown lesson plans or outlines into Marp presentation slides.")
    parser.add_argument('--input', '-i', help="Input Markdown file. Reads from stdin if omitted.")
    parser.add_argument('--output', '-o', help="Output Marp markdown file. Writes to stdout if omitted.")
    parser.add_argument('--theme', '-t', choices=['default', 'gaia', 'uncover'], default='default', help="Marp theme (default: default).")
    parser.add_argument('--title', help="Presentation header title.")
    
    args = parser.parse_args()
    
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = sys.stdin.read()
        
    pres_title = args.title or "Learning Session"
    deck = generate_marp_deck(content, title=pres_title, theme=args.theme)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(deck)
        print(f"Successfully generated Marp presentation at: {args.output}")
    else:
        print(deck)


if __name__ == '__main__':
    main()
