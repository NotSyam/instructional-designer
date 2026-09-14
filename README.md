# 🎓 Instructional Designer AI Agent Skill (v3.4.0 Master Suite)

[![Agent Skills Standard](https://img.shields.io/badge/Agent_Skills_Standard-v2.0-blue.svg)](https://github.com/GarethManning/education-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.4.0-green.svg)](CHANGELOG.md)
[![Tests](https://img.shields.io/badge/Tests-Passing_6/6-brightgreen.svg)](tests/test_scripts.py)
[![Compatible](https://img.shields.io/badge/Harnesses-Claude_|_Codex_|_Hermes_|_Antigravity-purple.svg)](SKILL.md)

An evidence-grounded **AI Agent Skill for Instructional Designers, L&D Consultants, Performance Consultants, and Curriculum Architects**.

Converts ambiguous training requests into **turnkey, measurable, and cognitively sound learning deliverables**—grounded in the unified synthesis of four seminal pillars:
1. **AECT Canonical Taxonomy & M-IDA**: *Survey of Instructional Design Models (6th Edition)* by Tonia A. Dousay & Robert Maribe Branch (Brill / AECT, 2022).
2. **Real-World Collaborative Spiral**: *Real World Instructional Design: An Iterative Approach (2nd Edition)* by Katherine Cennamo & Debby Kalk (Routledge, 2019).
3. **Performance Consulting & Craft Heuristics**: *The "When NOT to Design" Protocol & AI Failure Modes Guard* by Trina Rimmer (*id-skills-for-claude*, 2024).
4. **Multi-Lens Adversarial Critique**: *Evidence-Backed Pedagogy Audit & Smallest Testable Experiment* by Fastcat (*instructional-design-critic*, 2024).

---

## ⚡ Production-Oriented Slash Commands (Quick Triggers)

Practitioners can trigger specific, turnkey deliverables instantly using these production slash commands:

| Command | Output Deliverable | Focus & Execution Standard |
|---|---|---|
| `/storyboard` | **E-Learning & Video Storyboard** | Screen-by-screen script with On-Screen Text (OST), Voiceover Script (VO), Visual UI Layout, Branching/Interaction Logic, and Developer Notes. Ready for Articulate/Rise/Video production. |
| `/treatment` | **Instructional Strategy Treatment** | 2-column creative prototype linking content chunks with treatment ideas (*what learners see, hear, and do*) before full storyboarding (Cennamo & Kalk, 2019). |
| `/character` | **Character Spec Sheet & AI Prompts** | Scenario cast specification with 5 emotional poses, visual style guide, and AI image prompts using the Reference Image Anchor technique (Trina Rimmer, 2024). |
| `/qa` | **E-Learning QA & Bug Tracker** | 4-tier pre-delivery verification (Functional, Instructional, Editorial, Accessibility WCAG 2.2 AA) with severity classification and bug tracking log. |
| `/idd` | **Master Instructional Design Document** | Architectural blueprint featuring M-IDA framework scoring, learner personas, curriculum matrix, Kirkpatrick L1–L4 evaluation, contextual WBS, and RACI governance. |
| `/course-plan` | **Curriculum Blueprint & Syllabus** | Module-by-module curriculum matrix mapping Bloom's objectives, seat time, Dale's Cone activities, and assessments. |
| `/facilitator-guide` | **Complete Facilitator / Trainer Guide** | 3-column timeline script with verbatim facilitator dialogue, minute-by-minute pacing, and transition cues (**Mode B / Ready Tomorrow Morning**). |
| `/workbook` | **Participant Workbook & Job Aids** | Learner-facing exercise sheets, authentic case studies, reflection worksheets, and job aids. |
| `/scenario` | **Branching Decision Simulation** | Interactive decision tree with realistic choices, immediate natural consequence feedback layers, and score tracking. |
| `/assessment` | **Assessment Bank & Evaluation Rubrics** | Criterion-referenced quiz questions (GIFT/Moodle XML ready) or 4-tier analytic evaluation rubrics. |
| `/microlearning` | **Microlearning Bite / Job Aid (3–5 Min)** | High-impact 4-part micro-nugget (Hook, Concept, Application, Retention Check) with spaced booster schedule. |
| `/theory-match` | **Dynamic Theory & Model Diagnostics** | Automated analysis evaluating project needs against M-IDA layers and 75+ learning theories from the knowledge base. |
| `/critique` | **Multi-Lens Design Critique & Audit** | Evidence-backed review testing Rigor, Cognitive Demand, Access, Assessment Alignment, and Feedback with Supportive, Balanced, or Adversarial stance. |

---

## 🌟 Key Architectural Pillars & Quality Standards

### 1. Gate 0: Performance Consulting ("When NOT to Design")
* **The Mager Life-or-Death Test**: *"Could the performers execute this task correctly if their lives or jobs depended on it?"*
* If **YES**: The problem is not a knowledge gap—it is a broken tool, flawed process, or misaligned incentive. Do not build a bloated course. Recommend a **Job Aid, Checklist, Workflow Fix, or Management KPI Redesign**.
* If **NO**: Proceed to design systematic instruction.

### 2. AI Failure Modes Guard (Anti-Shallow Quality Control)
* **Plausible Distractors**: Quizzes must never include silly or obvious throwaway choices. Every distractor must reflect authentic workplace misconceptions or common near-miss errors.
* **Meaningful Interactivity**: Zero cosmetic clicks. Interactions must require cognitive decision-making, diagnosis, or prediction.
* **Zero UI Redundancy**: Eliminate condescending button instructions like *"Click the Next button below to continue"*. Controls must communicate their purpose intuitively.
* **Empathy in Sensitive Topics**: Strip preachy, moralizing lectures from compliance and ethics training. Focus on nuanced gray areas and realistic natural consequences.

### 3. Open Modular ID Architecture (M-IDA)
Instead of forcing learning projects into rigid, pre-canned hybrid packages, this skill applies the **Open Modular ID Architecture (M-IDA)** grounded in Dousay & Branch (2022) and Cennamo & Kalk (2019):
* **Layer 1: Macro Governance & Lifecycle**: *ADDIE, Cennamo-Kalk Spiral, Agile ID (Scrum), Gentry IPDM, Seels & Glasgow ISD Model 2, Branson IPISD*.
* **Layer 2: Task & Knowledge Architecture**: *Dick, Carey & Carey, Merrill Pebble in the Pond, van Merriënboer 4C/ID, Cathy Moore Action Mapping, Gerlach & Ely, Kemp Model*.
* **Layer 3: Pedagogical & Contextual Strategy**: *Gagné 9 Events, Understanding by Design (UbD), Patricia Young Culture Based Model (CBM), CAST Universal Design for Learning (UDL)*.
* **Layer 4: Constraint Scaling & Evolution**: *Tessmer & Wedman Layers-of-Necessity (Layer 1 MVP -> Layer n)*.

### 4. Multi-Lens Adversarial Critique Engine (Fastcat)
Run an evidence-backed review using 5 specialized lenses:
* **Rigor & Cognitive Demand**: Cognitive Load Theory, Expertise Reversal Effect.
* **Alignment & Construct Validity**: Does assessment measure authentic capability or proxy test skills?
* **Access & Inclusivity**: UDL 3 Pillars, WCAG 2.2 AA.
* **Feedback Depth**: Natural consequence layers vs. shallow "Right/Wrong" announcements.
* **Transfer**: Far transfer and on-the-job bridging.
* **Review Stances**: *Supportive* (ideation), *Balanced* (design review), *Adversarial* (stress-testing before launch).
* **The Smallest Testable Experiment**: Identifies the single micro-intervention that yields the highest instructional payoff without rewriting everything.

---

## 📂 Repository Structure

```
├── .codex-plugin/
│   └── plugin.json                          # OpenAI Codex manifest
├── examples/
│   ├── sample_outline.md                    # Fixture for slide deck generation
│   └── sample_quiz.md                       # Fixture for GIFT/XML quiz generation
├── references/
│   ├── accessible-learning-wcag.md          # WCAG 2.2 AA & UDL compliance checklist
│   ├── design-critique-and-audit.md         # Multi-lens critique & adversarial audit engine
│   ├── document-production.md               # Toolchain routing & 3-tier fallback protocols
│   ├── idd-and-isd-methodology.md          # M-IDA architecture, 15 canonical models, Cennamo & Kalk spiral
│   ├── industry-specific-considerations.md  # Healthcare, Finance, Manufacturing, Gov, Higher Ed
│   ├── isd-quality-and-pm-standards.md      # 48 intake questions & 37-point audit checklist
│   ├── knowledge-base.md                    # 75+ learning theories & dynamic selection matrix
│   ├── modern-edtech-and-microlearning.md   # H5P matrix, xAPI schemas, spaced retrieval
│   ├── performance-consulting-and-craft.md  # "When NOT to Design", AI failure modes, Storyline/Rise
│   └── system-prompt-plain.txt              # Plain-text mirror for non-file LLM harnesses
├── resources/templates/
│   ├── branching-scenario-template.md       # Interactive decision-tree simulation script
│   ├── character-spec-sheet-template.md     # Cast spec sheet & AI prompt generator
│   ├── course-blueprint-template.md         # Module-by-module curriculum matrix
│   ├── course-quality-self-check.md         # Gate 0 + Hard/Advisory audit & Definition of Done
│   ├── elearning-qa-bug-tracker.md          # 4-tier QA verification & bug tracking log
│   ├── facilitator-guide-template.md        # 3-column timeline facilitator script
│   ├── instructional-design-document-template.md  # Master 8-section enterprise IDD
│   ├── isd-project-timeline-and-pm-plan.md  # Contextual WBS, RACI, & 35-point checklist
│   ├── rubric-matrix-template.md            # 4-tier analytic evaluation rubric
│   ├── storyboard-template.md               # Screen-by-screen e-learning & media storyboard
│   └── treatment-template.md                # 2-column chunk-to-media creative treatment
├── scripts/
│   ├── outline_to_slides.py                 # Marp slide deck generator
│   └── quiz_to_gift.py                      # Canvas/Moodle GIFT & XML quiz exporter
├── tests/
│   ├── test_scripts.py                      # Unit test suite for automation scripts
│   └── validate_skill.py                    # Skill structure & manifest validator
├── ATTRIBUTION.md                           # Comprehensive attribution & fair-use notices
├── CHANGELOG.md                             # Version history & release notes
├── COMBINATIONS.md                          # Multi-skill project recipes & workflows
├── LICENSE                                  # MIT License
├── package.json                             # SkillHub metadata
├── README.md                                # Project documentation
├── requirements.txt                         # Dependency specifications
└── SKILL.md                                 # Streamlined Agent Skills Standard v2 specification
```

---

## 🛠️ Multi-Harness Installation

### 1. Google Antigravity (AGY)
```bash
git clone https://github.com/NotSyam/instructional-designer.git ~/.gemini/config/skills/instructional-designer
```

### 2. Hermes Agent
```bash
hermes skills install NotSyam/instructional-designer
```

### 3. OpenAI Codex
The `.codex-plugin/plugin.json` manifest enables native discovery in Codex environments.

### 4. Claude Code CLI
```bash
git clone https://github.com/NotSyam/instructional-designer.git ~/.claude/skills/instructional-designer
```

---

## 🧪 Local Verification & Tests

Run the automated test suite locally:
```bash
python -m unittest tests/test_scripts.py
python tests/validate_skill.py
```

---

## 📜 Attribution & License

* **License**: [MIT License](LICENSE)
* **Attribution**: Grounded in seminal works from AECT, Tonia A. Dousay & Robert Maribe Branch (*Survey of Instructional Design Models*, 6th Edition, 2022), Katherine Cennamo & Debby Kalk (*Real World Instructional Design*, 2nd Edition, 2019), Trina Rimmer (*id-skills-for-claude*, 2024), Fastcat (*instructional-design-critic*, 2024), Robert Mager & Peter Pipe (1997), Cathy Moore (*Action Mapping*), Walter Dick & Lou Carey, Michael Allen (*SAM*), Jeroen van Merriënboer (*4C/ID*), Grant Wiggins & Jay McTighe (*UbD*), and Patricia Young (*CBM*). See [ATTRIBUTION.md](ATTRIBUTION.md) for full fair-use disclosures.
