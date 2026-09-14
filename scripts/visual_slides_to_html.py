#!/usr/bin/env python3
"""
visual_slides_to_html.py — Convert Markdown Course Outline into Standalone HTML Presentation Deck
Grounded in Richard Mayer's Multimedia Principles and Dual Coding (visual-cognition-slides, 2024).

Usage:
  python visual_slides_to_html.py outline.md -o presentation.html
  python visual_slides_to_html.py examples/sample_outline.md
"""

import sys
import re
import argparse
from pathlib import Path

DEFAULT_HTML_SHELL = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #0f172a;
      --card-bg: #1e293b;
      --card-border: #334155;
      --text: #f8fafc;
      --muted: #94a3b8;
      --accent: #6366f1;
      --accent-light: #818cf8;
      --success: #10b981;
      --font-main: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      width: 100%; height: 100%;
      background: #020617;
      color: var(--text);
      font-family: var(--font-main);
      overflow: hidden;
    }}
    #stage {{
      position: absolute; inset: 0;
      display: flex; align-items: center; justify-content: center;
    }}
    #deck {{
      position: absolute;
      width: 1920px; height: 1080px;
      background: var(--bg);
      transform-origin: top left;
      overflow: hidden;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }}
    .slide {{
      position: absolute; inset: 0;
      padding: 80px 100px;
      display: flex; flex-direction: column;
      justify-content: center;
      opacity: 0; pointer-events: none;
      transition: opacity 0.4s ease, transform 0.4s ease;
      transform: scale(0.98);
    }}
    .slide.active {{
      opacity: 1; pointer-events: auto;
      transform: scale(1);
    }}
    #progress-wrap {{
      position: absolute; bottom: 0; left: 0; right: 0;
      height: 6px; background: rgba(255,255,255,0.1); z-index: 100;
    }}
    #progress-bar {{
      height: 100%; width: 0%;
      background: var(--accent);
      transition: width 0.3s ease;
    }}
    #slide-counter {{
      position: absolute; top: 28px; right: 40px;
      font-size: 16px; font-weight: 600;
      color: var(--muted); z-index: 100;
    }}
    .hero-title {{ font-size: 64px; font-weight: 800; line-height: 1.15; margin-bottom: 24px; }}
    .hero-sub {{ font-size: 28px; color: var(--muted); line-height: 1.4; max-width: 1200px; }}
    .badge {{
      display: inline-block; padding: 8px 18px; border-radius: 9999px;
      font-size: 14px; font-weight: 700; text-transform: uppercase;
      margin-bottom: 24px;
      background: rgba(99, 102, 241, 0.2); color: var(--accent-light);
      border: 1px solid rgba(99, 102, 241, 0.3);
    }}
    .grid-cards {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 32px; width: 100%; margin-top: 36px;
    }}
    .card {{
      background: var(--card-bg); border: 1px solid var(--card-border);
      border-radius: 16px; padding: 36px;
    }}
    .card-title {{ font-size: 22px; font-weight: 700; margin-bottom: 12px; color: #fff; }}
    .card-body {{ font-size: 16px; color: var(--muted); line-height: 1.5; }}
  </style>
</head>
<body>
  <div id="stage">
    <div id="deck">
{slides_html}
      <div id="slide-counter">Slide 1 / {total_slides}</div>
      <div id="progress-wrap"><div id="progress-bar"></div></div>
    </div>
  </div>
  <script>
    const slides = Array.from(document.querySelectorAll('.slide'));
    let currentIdx = 0;
    function scaleDeck() {{
      const deck = document.getElementById('deck');
      const targetW = 1920, targetH = 1080;
      const scale = Math.min(window.innerWidth / targetW, window.innerHeight / targetH);
      const left = (window.innerWidth - targetW * scale) / 2;
      const top = (window.innerHeight - targetH * scale) / 2;
      deck.style.transform = `scale(${{scale}})`;
      deck.style.left = `${{left}}px`;
      deck.style.top = `${{top}}px`;
    }}
    window.addEventListener('resize', scaleDeck);
    window.addEventListener('DOMContentLoaded', scaleDeck);
    function updateDeck() {{
      slides.forEach((s, idx) => {{
        if (idx === currentIdx) s.classList.add('active');
        else s.classList.remove('active');
      }});
      document.getElementById('slide-counter').innerText = `Slide ${{currentIdx + 1}} / ${{slides.length}}`;
      document.getElementById('progress-bar').style.width = `${{((currentIdx + 1) / slides.length) * 100}}%`;
    }}
    function nextSlide() {{ if (currentIdx < slides.length - 1) {{ currentIdx++; updateDeck(); }} }}
    function prevSlide() {{ if (currentIdx > 0) {{ currentIdx--; updateDeck(); }} }}
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') nextSlide();
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
    }});
    updateDeck();
  </script>
</body>
</html>
"""

def parse_markdown_to_slides(md_text: str) -> tuple[str, list[dict]]:
    lines = md_text.splitlines()
    deck_title = "Visual Cognition Presentation"
    raw_slides = []
    current_slide = None

    for line in lines:
        if line.startswith("# "):
            deck_title = line[2:].strip()
            if not raw_slides:
                raw_slides.append({"type": "cover", "title": deck_title, "content": []})
        elif line.startswith("## "):
            if current_slide:
                raw_slides.append(current_slide)
            current_slide = {"type": "content", "title": line[3:].strip(), "content": []}
        elif current_slide is not None:
            if line.strip():
                current_slide["content"].append(line.strip())

    if current_slide:
        raw_slides.append(current_slide)

    return deck_title, raw_slides

def render_html_slides(deck_title: str, slides_data: list[dict]) -> str:
    rendered_slides = []

    for idx, s in enumerate(slides_data):
        active_cls = " active" if idx == 0 else ""
        if s["type"] == "cover":
            sub = s["content"][0] if s["content"] else "Grounded in Dual Coding & Cognitive Science"
            slide_html = f"""      <div class="slide{active_cls}" id="slide-{idx+1}">
        <span class="badge">Visual Cognition</span>
        <h1 class="hero-title">{s["title"]}</h1>
        <p class="hero-sub">{sub}</p>
      </div>"""
        else:
            cards_html = []
            for item in s["content"]:
                clean_item = re.sub(r"^[*-]\s+", "", item)
                clean_item = re.sub(r"^\d+\.\s+", "", clean_item)
                parts = clean_item.split(":", 1)
                if len(parts) == 2:
                    card_t, card_b = parts[0].strip(), parts[1].strip()
                else:
                    card_t, card_b = "Key Concept", clean_item
                cards_html.append(f"""          <div class="card">
            <h3 class="card-title">{card_t}</h3>
            <p class="card-body">{card_b}</p>
          </div>""")

            cards_str = "\n".join(cards_html)
            slide_html = f"""      <div class="slide{active_cls}" id="slide-{idx+1}">
        <span class="badge">Module Section</span>
        <h2 style="font-size: 44px; font-weight: 800; margin-bottom: 24px;">{s["title"]}</h2>
        <div class="grid-cards">
{cards_str}
        </div>
      </div>"""
        rendered_slides.append(slide_html)

    all_slides = "\n\n".join(rendered_slides)
    return DEFAULT_HTML_SHELL.format(
        title=deck_title,
        slides_html=all_slides,
        total_slides=len(rendered_slides)
    )

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown outline to Visual Cognition HTML Slides")
    parser.add_argument("input", help="Path to input Markdown outline")
    parser.add_argument("-o", "--output", help="Path to output HTML file")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} does not exist.")
        sys.exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    title, slides_data = parse_markdown_to_slides(md_text)
    html_out = render_html_slides(title, slides_data)

    output_path = Path(args.output) if args.output else input_path.with_suffix(".html")
    output_path.write_text(html_out, encoding="utf-8")
    print(f"Successfully generated visual HTML presentation: {output_path} ({len(slides_data)} slides)")

if __name__ == "__main__":
    main()
