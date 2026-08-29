# Document Production — Hermes Skills Integration Reference

This reference connects the Instructional Designer skill to five Hermes productivity document skills for producing, reading, and converting training artifacts into standard office file formats. The ID skill designs the content; these skills produce the files.

> **Workflow principle**: Design with ID frameworks first → structure content using templates → export/generate using the appropriate document skill below.

---

## Quick Dispatch — Which Skill to Use?

| User Request | File Type | Use |
|---|---|---|
| Export course blueprint / rubric as a Word doc | `.docx` | `docx` skill (`python-docx`) |
| Generate a fillable evaluation form, certificate, or packaged report | `.pdf` | `pdf` skill (`pypdf`, `reportlab`, `pdfplumber`) |
| Extract text from a training manual or scanned handout | scanned PDF | `ocr-and-documents` skill (`pymupdf` / `marker-pdf`) |
| Build a presentation slide deck from a lesson plan | `.pptx` | `powerpoint` skill (`python-pptx`) |
| Export quiz bank or assessment data as a spreadsheet | `.xlsx` | `xlsx` skill (`openpyxl`) |
| Fill a Word template with learner-specific data | `.docx` `{{tokens}}` | `docx` skill — template mode |
| Merge/split or watermark PDF study guides | `.pdf` | `pdf` skill — page manipulation |

---

## 1. OCR & Document Extraction (`ocr-and-documents`)

**Use when**: A user uploads a scanned training manual, legacy PDF handout, or image-only PDF where text cannot be directly copied.

### Tool Selection Logic

| Scenario | Tool | Notes |
|---|---|---|
| PDF has a URL | Firecrawl via `web_extract` | Always try first: no local deps |
| Text-based PDF, local | pymupdf (~25 MB, instant) | Use `pymupdf4llm.to_markdown()` |
| Scanned / OCR needed, equations, forms, complex layout | marker-pdf (~3–5 GB) | `marker_single file.pdf outdir/` |

### pymupdf — Text-Based PDF

`python
import pymupdf4llm
md_text = pymupdf4llm.to_markdown("course_manual.pdf")
`

### marker-pdf — Scanned / Complex OCR

`ash
pip install marker-pdf
marker_single scanned_handout.pdf output_dir/ --langs English
`

### Handling Extraction Warnings

If `read_file` returns a coverage warning (pages with no text):
- **A few pages**: `pdftoppm -jpeg -r 150 -f N -l N file.pdf /tmp/page` then vision-analyze each image.
- **Many pages**: Use marker-pdf for bulk OCR.

### ID Use Cases

- Digitize legacy printed training guides for redesign.
- Extract competency framework tables from scanned PDFs.
- Digitize printed assessment rubrics for LMS migration.
- Read archived facilitator guides for review and modernization.

---

## 2. PDF Skill (`pdf`)

**Use when**: Creating, reading, manipulating, or securing PDF training artifacts.

### Prerequisites

`ash
pip install pypdf reportlab pdfplumber
pip install pypdfium2  # optional, for page rasterization
`

### ID-Specific Commands

| Training Artifact | Command |
|---|---|
| Generate a packaged course report or certificate | `python scripts/pdf_create.py spec.json -o certificate.pdf` |
| Build a fillable learner evaluation / registration form | `python scripts/pdf_make_form.py formspec.json -o form.pdf` |
| Validate form layout before distributing | `python scripts/pdf_form_layout.py formspec.json --render-overlay preview.png` |
| Extract text from a PDF resource for design review | `python scripts/pdf_read.py resource.pdf --text` |
| Extract tables from a PDF competency matrix | `python scripts/pdf_read.py matrix.pdf --tables --csv-dir output/` |
| Merge separate module PDFs into a course package | `python scripts/pdf_merge.py m1.pdf m2.pdf m3.pdf -o full_course.pdf --bookmarks` |
| Split a large guide into per-module handouts | `python scripts/pdf_split.py guide.pdf --pages 1-15 -o module1.pdf` |
| Watermark draft facilitator guides | `python scripts/pdf_watermark.py guide.pdf --stamp watermark.pdf -o draft_guide.pdf` |
| Stamp "DRAFT" or version on course materials | `python scripts/pdf_stamp.py guide.pdf -o out.pdf --text "DRAFT v1.2" --rotation 45 --opacity 0.3` |
| Export pages as images for SCORM thumbnails | `python scripts/pdf_page_image.py cover.pdf --pages 1 --dpi 150 --out-dir imgs/` |
| Fill a learner-specific certificate template | `python scripts/pdf_fill_form.py cert_template.pdf --fields-json learner_data.json -o cert_john.pdf --flatten` |
| Encrypt sensitive assessment answer keys | `python scripts/pdf_secure.py answers.pdf --encrypt -o answers_enc.pdf --user-password secret` |

### JSON Spec Pattern (Course Report)

`json
{
  "pages": [
    {
      "elements": [
        {"type": "heading", "text": "Course Completion Report", "level": 1},
        {"type": "paragraph", "text": "Learner: {{name}} | Cohort: {{cohort}}"},
        {"type": "table",
         "headers": ["Module", "Score", "Status"],
         "rows": [["Module 1", "92%", "Passed"], ["Module 2", "88%", "Passed"]]}
      ]
    }
  ]
}
`

> **Scope boundary**: If `pdf_read.py --meta` returns `"scanned": true` for a page, stop and route to `ocr-and-documents`. Never pretend to extract text from image-only pages.

---

## 3. Docx Skill (`docx`)

**Use when**: Producing or editing Microsoft Word training artifacts.

### Prerequisites

`ash
pip install python-docx
`

### ID-Specific Commands

| Training Artifact | Command |
|---|---|
| Generate a course blueprint document | `python scripts/docx_create.py blueprint_spec.json blueprint.docx` |
| Generate a facilitator guide | `python scripts/docx_create.py guide_spec.json facilitator_guide.docx` |
| Generate a participant workbook | `python scripts/docx_create.py workbook_spec.json participant_workbook.docx` |
| Fill a branded Word template | `python scripts/docx_template.py org_template.docx values.json filled.docx --strict` |
| Read an existing curriculum document's structure | `python scripts/docx_read.py curriculum.docx --structure` |
| Extract all text from a Word training manual | `python scripts/docx_read.py manual.docx --text` |
| Find/replace outdated terminology | `python scripts/docx_edit.py replace guide.docx --find "old term" --replace "new term" -o updated.docx` |
| Accept tracked changes from an SME review | `python scripts/docx_revisions.py accept-all reviewed.docx -o final.docx` |
| Add a review comment to a draft | `python scripts/docx_comments.py add draft.docx --target "learning objective" --text "Check Bloom level" --author "ID Lead"` |

### Token Template Pattern

Create `org_template.docx` with `{{placeholders}}`:

`
{{course_title}}
{{learning_objectives}}
{{facilitator_notes}}
{{assessment_criteria}}
`

`values.json`:
`json
{
  "course_title": "Conflict Resolution for Team Leads",
  "learning_objectives": "By the end of this session, participants will be able to...",
  "facilitator_notes": "Allow 5 minutes for warm-up activity...",
  "assessment_criteria": "Participants will be assessed via role-play rubric..."
}
`

### JSON Spec Pattern (Facilitator Guide)

`json
{
  "page": {"size": "A4", "margins": {"top": 25, "bottom": 25, "left": 30, "right": 30}},
  "footer_page_numbers": true,
  "styles": {"Heading 1": {"bold": true, "font_size": 16, "color": "#1a3a5c"}},
  "content": [
    {"type": "heading", "text": "Session Overview", "level": 1},
    {"type": "paragraph", "text": "Duration: 90 min | Audience: New Managers"},
    {"type": "table",
     "headers": ["Time", "Activity", "Materials"],
     "rows": [
       ["0:00-0:10", "Hook & Context (Gagne 1-3)", "Slide 1-3"],
       ["0:10-0:30", "Demonstration (Gagne 4-5)", "Slide 4-7"],
       ["0:30-1:10", "Deliberate Practice (Gagne 6-7)", "Scenario Cards"]
     ]}
  ]
}
`

---

## 4. PowerPoint Skill (`powerpoint`)

**Use when**: Building slide decks for ILT/VILT sessions or extracting content from existing decks.

### Prerequisites

`ash
pip install python-pptx
# Optional for PNG rendering: LibreOffice (soffice) + poppler
`

### Integration with `outline_to_slides.py`

The built-in `scripts/outline_to_slides.py` generates **Marp Markdown**. For branded `.pptx` output, use the PowerPoint skill directly:

`ash
# Build branded pptx from JSON spec
python scripts/pptx_create.py deck_spec.json workshop_slides.pptx

# Or: fill an existing branded template
python scripts/pptx_from_template.py org_brand.pptx out.pptx --values slide_values.json
`

### ID-Specific Commands

| Training Artifact | Command |
|---|---|
| Build a workshop slide deck from a lesson plan | `python scripts/pptx_create.py deck_spec.json out.pptx` |
| Fill an on-brand company template | `python scripts/pptx_from_template.py brand.pptx out.pptx --values vals.json` |
| Extract speaker notes from an existing deck | `python scripts/pptx_read.py deck.pptx --notes` |
| Update organisation name across a deck | `python scripts/pptx_edit.py deck.pptx --replace-text "Old Corp" "New Corp"` |
| Reorder slides after agenda change | `python scripts/pptx_edit.py deck.pptx --move-slide 5 2` |
| Export slides as images for SCORM thumbnails | `python scripts/pptx_render.py deck.pptx --outdir ./slide_images/` |

### JSON Deck Spec Pattern (ILT Workshop)

`json
{
  "slide_size": "16:9",
  "slides": [
    {"layout": "title", "title": "Giving Effective Feedback", "subtitle": "Manager Excellence Series"},
    {"layout": "title_content", "title": "Session Objectives",
     "bullets": [
       "Apply the SBI model in feedback conversations",
       "Distinguish specific from vague feedback",
       "Practice with a structured role-play rubric"
     ]},
    {"layout": "title_content", "title": "The SBI Model",
     "bullets": [
       {"text": "Situation — describe the context", "bold": true},
       {"text": "Behavior — describe what you observed", "bold": true},
       {"text": "Impact — describe the effect on the team", "bold": true}
     ]},
    {"layout": "section", "title": "Practice Activity"},
    {"layout": "blank", "footer": "Manager Excellence | Feedback Workshop", "slide_number": true}
  ]
}
`

> **Gagne alignment tip**: Structure slide order to mirror the Nine Events — gain attention (slide 1) → state objectives (slide 2) → recall prior knowledge (slide 3) → present content → provide guidance → signal practice transition.

---

## 5. XLSX Skill (`xlsx`)

**Use when**: Creating spreadsheet-based training management tools, quiz banks, assessment trackers, or data exports.

### Prerequisites

`ash
pip install openpyxl
# Optional for headless recalculation: LibreOffice (soffice)
`

### ID-Specific Commands

| Training Artifact | Command |
|---|---|
| Build a quiz bank / question tracker | `python scripts/xlsx_create.py quiz_bank_spec.json quiz_bank.xlsx` |
| Export learner assessment scores | `python scripts/xlsx_create.py scores_spec.json assessment_results.xlsx` |
| Build a Training Needs Analysis (TNA) matrix | `python scripts/xlsx_create.py tna_spec.json tna_matrix.xlsx` |
| Import CSV assessment data into styled workbook | `python scripts/csv_to_xlsx.py raw_scores.csv workbook.xlsx` |
| Dump existing training data for analysis | `python scripts/xlsx_read.py data.xlsx --json --sheet Results` |
| Update a learner score in a tracker | `python scripts/xlsx_edit.py tracker.xlsx --sheet Results --set "C5=88"` |
| Append a new cohort row | `python scripts/xlsx_edit.py log.xlsx --append '["2026-08-22","Cohort B","15","Completed"]'` |

### JSON Spec Pattern (Assessment Tracker)

`json
{
  "sheets": [
    {
      "name": "Results",
      "freeze_panes": "A2",
      "autofilter": "A1:F1",
      "headers": ["Learner", "Module 1", "Module 2", "Module 3", "Average", "Status"],
      "rows": [
        ["Alex Johnson", 88, 92, 85, "=AVERAGE(B2:D2)", "=IF(E2>=80,\"Pass\",\"Needs Review\")"],
        ["Sam Rivera",   76, 81, 79, "=AVERAGE(B3:D3)", "=IF(E3>=80,\"Pass\",\"Needs Review\")"]
      ],
      "conditional_formatting": [
        {"range": "F2:F100", "rule": "text_contains", "value": "Needs Review", "fill": "#FFE0E0"}
      ]
    }
  ]
}
`

---

## 6. Cross-Skill Workflow Examples

### A. Full Course Package Production

1. **ID Design** (this skill): Course blueprint → facilitator guide → quiz questions → rubric.
2. **Word export**: `docx_create.py` → `facilitator_guide.docx` + `participant_workbook.docx`.
3. **Slides export**: `pptx_create.py` → `workshop_slides.pptx`.
4. **Quiz LMS export**: `quiz_to_gift.py` → `quiz.gift` (Moodle/Canvas import).
5. **Assessment tracker**: `xlsx_create.py` → `assessment_tracker.xlsx`.
6. **Final package PDF**: `pdf_merge.py` → `course_package.pdf` (all handouts combined + bookmarks).

### B. Digitize a Legacy Printed Course

1. **OCR extraction**: marker-pdf → `legacy_course.md` (text + tables).
2. **ID Review** (this skill): Evaluate extracted content against modern ID principles; rewrite objectives using Bloom's; redesign for current audience.
3. **Rebuild deliverables**: Use `docx`, `pptx`, `pdf` skills for new format outputs.

### C. Fill Branded Templates for a Client

1. **ID Design** (this skill, Mode A): Draft all content with framework rationale visible.
2. **Switch to Mode B**: Prepare clean content strings for each template placeholder.
3. **Word**: `docx_template.py org_template.docx values.json output.docx --strict`
4. **PowerPoint**: `pptx_from_template.py brand.pptx out.pptx --values vals.json`
5. **PDF**: `pdf_create.py` for certificates or `pdf_fill_form.py` for evaluation forms.
