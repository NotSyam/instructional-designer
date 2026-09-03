# 🎓 Instructional Designer AI Agent Skill (v3.2.0)

[![Agent Skills Standard](https://img.shields.io/badge/Agent_Skills_Standard-v2.0-blue.svg)](https://github.com/GarethManning/education-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.2.0-green.svg)](CHANGELOG.md)
[![Tests](https://img.shields.io/badge/Tests-Passing_6/6-brightgreen.svg)](tests/test_scripts.py)
[![Compatible](https://img.shields.io/badge/Harnesses-Claude_|_Codex_|_Hermes_|_Antigravity-purple.svg)](SKILL.md)

An evidence-grounded **AI Agent Skill for Instructional Designers, L&D Consultants, and Curriculum Architects**.

Converts ambiguous training requests into **turnkey, measurable, and cognitively sound learning deliverables**—grounded in the dual foundations of:
1. **AECT Canonical Taxonomy**: *Survey of Instructional Design Models (6th Edition)* by Tonia A. Dousay & Robert Maribe Branch (Brill / AECT, 2022).
2. **Real-World Collaborative Spiral**: *Real World Instructional Design: An Iterative Approach to Designing Learning Experiences (2nd Edition)* by Katherine Cennamo & Debby Kalk (Routledge, 2019).

---

## ⚡ Production-Oriented Slash Commands (Quick Triggers)

Practitioners can trigger specific, turnkey deliverables instantly using these production slash commands:

| Command | Output Deliverable | Focus & Execution Standard |
|---|---|---|
| `/storyboard` | **E-Learning & Video Storyboard** | Screen-by-screen script with On-Screen Text (OST), Voiceover Script (VO), Visual UI Layout, Branching/Interaction Logic, and Developer Notes. Ready for Articulate/Rise/Video production. |
| `/treatment` | **Instructional Strategy Treatment** | 2-column creative prototype linking content chunks with treatment ideas (*what learners see, hear, and do*) before full storyboarding (Cennamo & Kalk, 2019). |
| `/idd` | **Master Instructional Design Document** | Architectural blueprint featuring M-IDA framework scoring, learner personas, curriculum matrix, Kirkpatrick L1–L4 evaluation, contextual WBS, and RACI governance. |
| `/course-plan` | **Curriculum Blueprint & Syllabus** | Module-by-module curriculum matrix mapping Bloom's objectives, seat time, Dale's Cone activities, and assessments. |
| `/facilitator-guide` | **Complete Facilitator / Trainer Guide** | 3-column timeline script with verbatim facilitator dialogue, minute-by-minute pacing, and transition cues (**Mode B / Ready Tomorrow Morning**). |
| `/workbook` | **Participant Workbook & Job Aids** | Learner-facing exercise sheets, authentic case studies, reflection worksheets, and job aids. |
| `/scenario` | **Branching Decision Simulation** | Interactive decision tree with realistic choices, immediate natural consequence feedback layers, and score tracking. |
| `/assessment` | **Assessment Bank & Evaluation Rubrics** | Criterion-referenced quiz questions (GIFT/Moodle XML ready) or 4-tier analytic evaluation rubrics. |
| `/microlearning` | **Microlearning Bite / Job Aid (3–5 Min)** | High-impact 4-part micro-nugget (Hook, Concept, Application, Retention Check) with spaced booster schedule. |
| `/theory-match` | **Dynamic Theory & Model Diagnostics** | Automated analysis evaluating project needs against M-IDA layers and 75+ learning theories from the knowledge base. |

---

## 🌟 Key Capabilities & Industry-Ready Standards

### 1. Open Modular ID Architecture (M-IDA)
Instead of forcing learning projects into rigid, pre-canned hybrid packages, this skill applies the **Open Modular ID Architecture (M-IDA)** grounded in Dousay & Branch (2022) and Cennamo & Kalk (2019).

Projects are assembled dynamically across **4 Functional Layers**:
* **Layer 1: Macro Governance & Lifecycle**: *ADDIE, Cennamo-Kalk Spiral, Agile ID (Scrum), Gentry IPDM, Seels & Glasgow ISD Model 2, Branson IPISD*.
* **Layer 2: Task & Knowledge Architecture**: *Dick, Carey & Carey, Merrill Pebble in the Pond, van Merriënboer 4C/ID, Cathy Moore Action Mapping, Gerlach & Ely, Kemp Model*.
* **Layer 3: Pedagogical & Contextual Strategy**: *Gagné 9 Events, Understanding by Design (UbD), Patricia Young Culture Based Model (CBM), CAST Universal Design for Learning (UDL)*.
* **Layer 4: Constraint Scaling & Evolution**: *Tessmer & Wedman Layers-of-Necessity (Layer 1 MVP -> Layer n)*.

### 2. The Essential Triangle of ID & Collaborative Spiral (Cennamo & Kalk, 2019)
* **Learner at the Center**: Outcomes, Activities, and Assessments form an equilateral triangle with the learner at the core, wrapped by continuous Evaluation.
* **Non-Linear Entry Principle**: Start at any point (Outcomes-first, Assessment-first with field SMEs, or Activity/Content-first with existing assets), ensuring perfect alignment.
* **Zahorik's 4 Instructional Sequences**: Application Model (hierarchical-convergent), Discovery Model (problem-convergent), Extension Model (hierarchical-divergent), and Invention Model (problem-divergent).
* **Progressive Deliverable Refinement**: Design Document -> Content Document -> Treatment -> Storyboard -> Working Prototype -> Revision Table.

### 3. Weighted 5-Dimension Scoring Engine & 20-Point Rule
* **D1 — Stakes & Failure Cost**: Minor error consequence (1) -> Operational impact (3) -> Zero-tolerance / Life-safety / Legal audit (5).
* **D2 — Skill Complexity**: Declarative recall (1) -> Procedural multi-step (3) -> Complex cognitive & heuristics (5).
* **D3 — Timeline & Delivery Pressure**: Loose horizon >12 wks (1) -> Standard 6–12 wks (3) -> Rapid sprint <6 wks (5).
* **D4 — Primary Outcome Goal**: Conceptual transfer (1) -> Specific task execution (3) -> Measurable on-the-job behavior change (5).
* **D5 — Governance & Culture**: Lean startup (1) -> Mid enterprise (3) -> Heavy audit & regulatory sign-off (5).
* **Decision Logic**: Score diff > 20 pts -> Single framework (#1 ranked); Score diff <= 20 pts -> Dynamic M-IDA modular composition (**Confidence: Medium**). User override is always supported.

### 4. Dynamic Theory Selection Engine (Knowledge Base)
Automatically diagnoses and pairs the instructional challenge with the optimal theoretical mechanism from `references/knowledge-base.md`:
* **Complex Cognitive Tasks**: Sweller Cognitive Load Theory & Expertise Reversal Effect.
* **Procedural Mastery**: Merrill's First Principles & Behaviorist Task Chaining.
* **Conceptual Transfer**: Wiggins & McTighe UbD & Ausubel Subsumption.
* **Low Motivation & Drive**: Keller ARCS-E & Deci/Ryan Self-Determination Theory.
* **Long-Term Retention**: Roediger & Karpicke Retrieval Practice & Spaced Testing (3, 7, 21 days).
* **Social & Cohort Dynamics**: Vygotsky ZPD & Wenger Communities of Practice (CoP).
* **Cultural Responsiveness**: Patricia Young Culture Based Model (CBM).

### 5. Industry-Ready Standards (No Hollow Artifacts)
* **Zero Placeholder Jargon**: Complete minute-by-minute facilitator scripts, explicit exercises, and verbatim talking points—no vague *"use Gagné here"* labels.
* **Contextual Scale & Timeline**: Timelines scale to real project duration (no forced 16-week WBS for a 90-minute workshop). Unspecified parameters are marked explicitly as `[ASUMSI: ...]`.
* **Project-Specific Definition of Done (DoD)**: Concrete sign-off criteria specifying when deliverables are ready for production.
* **The "Ready-to-Deploy Tomorrow Morning" Test**: If handed to a facilitator or developer tomorrow morning, they can execute immediately with zero missing information.

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
│   ├── document-production.md               # Toolchain routing & 3-tier fallback protocols
│   ├── idd-and-isd-methodology.md          # M-IDA architecture, 15 canonical models, Cennamo & Kalk spiral
│   ├── isd-quality-and-pm-standards.md      # 48 intake questions & 37-point audit checklist
│   ├── knowledge-base.md                    # 75+ learning theories & dynamic selection matrix
│   └── modern-edtech-and-microlearning.md   # H5P matrix, xAPI schemas, spaced retrieval
├── resources/templates/
│   ├── storyboard-template.md               # Screen-by-screen e-learning & media storyboard
│   ├── treatment-template.md                # 2-column chunk-to-media creative treatment
│   ├── course-blueprint-template.md         # Module-by-module curriculum matrix
│   ├── course-quality-self-check.md         # Hard/Advisory gate audit & Definition of Done
│   ├── facilitator-guide-template.md        # 3-column timeline facilitator script
│   ├── instructional-design-document-template.md  # Master 8-section enterprise IDD
│   ├── isd-project-timeline-and-pm-plan.md  # Contextual WBS, RACI, & 35-point checklist
│   ├── branching-scenario-template.md       # Interactive decision-tree simulation script
│   └── rubric-matrix-template.md            # 4-tier analytic evaluation rubric
├── scripts/
│   ├── outline_to_slides.py                 # Marp slide deck generator
│   └── quiz_to_gift.py                      # Canvas/Moodle GIFT & XML quiz exporter
├── tests/
│   ├── test_scripts.py                      # Unit test suite for automation scripts
│   └── validate_skill.py                    # Skill structure & manifest validator
├── ATTRIBUTION.md                           # Third-party framework attribution & disclaimers
├── CHANGELOG.md                             # Version history & release notes
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
git clone https://github.com/NotSyam/instructional-designer.git ~/.gemini/antigravity/skills/instructional-designer
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
* **Attribution**: Grounded in seminal works from AECT, Tonia A. Dousay & Robert Maribe Branch (*Survey of Instructional Design Models*, 6th Edition, 2022), Katherine Cennamo & Debby Kalk (*Real World Instructional Design*, 2019), Cathy Moore (*Action Mapping*), Walter Dick & Lou Carey, Michael Allen (*SAM*), Jeroen van Merriënboer (*4C/ID*), Grant Wiggins & Jay McTighe (*UbD*), and Patricia Young (*CBM*). See [ATTRIBUTION.md](ATTRIBUTION.md) for detailed fair-use notices.
