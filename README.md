# 🎓 Instructional Designer AI Agent Skill (v3.2.0)

[![Agent Skills Standard](https://img.shields.io/badge/Agent_Skills_Standard-v2.0-blue.svg)](https://github.com/GarethManning/education-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.2.0-green.svg)](CHANGELOG.md)
[![Tests](https://img.shields.io/badge/Tests-Passing_6/6-brightgreen.svg)](tests/test_scripts.py)
[![Compatible](https://img.shields.io/badge/Harnesses-Claude_|_Codex_|_Hermes_|_Antigravity-purple.svg)](SKILL.md)

An evidence-grounded **AI Agent Skill for Instructional Designers, L&D Consultants, and Curriculum Architects**.

Converts ambiguous training requests into **turnkey, measurable, and cognitively sound learning deliverables**—grounded in learning sciences, contemporary cognitive research, and real-world corporate L&D standards.

---

## 🌟 Key Capabilities & Industry-Ready Standards

### 1. Weighted Multi-Dimensional Framework Scoring Engine
Instead of rigid categorical assignment, every project is evaluated across **5 weighted dimensions (Scale 1–5)**:
* **D1 — Stakes & Failure Cost**: Minor error consequence (1) -> Operational impact (3) -> Zero-tolerance / Life-safety / Legal audit (5).
* **D2 — Skill Complexity**: Declarative recall (1) -> Procedural multi-step (3) -> Complex cognitive & heuristics (5).
* **D3 — Timeline & Delivery Pressure**: Loose horizon >12 wks (1) -> Standard 6–12 wks (3) -> Rapid sprint <6 wks (5).
* **D4 — Primary Outcome Goal**: Conceptual transfer (1) -> Specific task execution (3) -> Measurable on-the-job behavior change (5).
* **D5 — Governance & Culture**: Lean startup (1) -> Mid enterprise (3) -> Heavy audit & regulatory sign-off (5).

#### Engine Decision Logic & 20-Point Threshold Rule:
* **Score Difference > 20 Points**: Single framework chosen (#1 ranked), **Confidence: High**.
* **Score Difference <= 20 Points**: Mandatory hybrid recommendation (**Confidence: Medium**), combining macro architecture with specialized micro practice.
* **User Override**: User choices are always respected, with transparent diagnostic trade-off notes.

### 2. Official Hybrid Framework Architectures
* **Pola A — Behavioral Agile (Action Mapping + SAM)**: Behavior-first decision scenarios built via rapid iterative prototyping sprints.
* **Pola B — Technical Rigor & Transfer (Dick & Carey + Action Mapping)**: Rigorous task hierarchy & entry behaviors paired with realistic consequence branching scenarios.
* **Pola C — Academic Enterprise (Backward Design / UbD + ADDIE)**: Deep conceptual understanding (Stage 1–3, GRASPS) wrapped in enterprise budget & rollout governance.
* **Pola D — Complex Systems (4C/ID + SAM)**: Complex cognitive skills broken into whole tasks and delivered through iterative module releases.

### 3. Industry-Ready Standards (No Hollow Artifacts)
* **Zero Placeholder Jargon**: Complete minute-by-minute facilitator scripts, explicit exercises, and verbatim talking points—no vague *"use Gagné here"* labels.
* **Contextual Scale & Timeline**: Timelines scale to real project duration (no forced 16-week WBS for a 90-minute workshop). Unspecified parameters are marked explicitly as `[ASUMSI: ...]`.
* **Project-Specific Definition of Done (DoD)**: Concrete sign-off criteria specifying when deliverables are ready for production.
* **The "Ready-to-Deploy Tomorrow Morning" Test**: If handed to a facilitator or developer tomorrow morning, they can execute immediately with zero missing information.

### 4. Contemporary Learning Sciences in Active Workflow
* **Retrieval Practice & Spaced Testing** (Roediger & Karpicke 2006, Dunlosky 2013): Low-stakes retrieval checks during learning + booster schedules at 3, 7, and 21 days.
* **Advanced Cognitive Load Theory & Expertise Reversal** (Sweller 2011, Kalyuga 2007): Worked examples for novices; faded guidance & problem-solving for experts.
* **Full 3-Pillar Universal Design for Learning** (CAST 2018): Multiple Means of Engagement, Representation, and Action & Expression.
* **Social Learning & Communities of Practice** (Wenger-Trayner 2015): Peer case clinics and cohort reflection channels.

### 5. Verified Automation Scripts & LMS Exporters
* `scripts/quiz_to_gift.py`: Converts Markdown quizzes into Canvas/Moodle **GIFT** and **Moodle XML** formats.
* `scripts/outline_to_slides.py`: Transforms course blueprints into presentation-ready **Marp Markdown** slide decks.
* Automated unit test suite with 6 tests passing cleanly (`tests/test_scripts.py`).

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
│   ├── idd-and-isd-methodology.md          # Weighted scoring, 20-point rule, hybrid patterns, & DoD
│   ├── isd-quality-and-pm-standards.md      # 48 intake questions & 37-point audit checklist
│   ├── knowledge-base.md                    # 75+ learning theories & contemporary research
│   └── modern-edtech-and-microlearning.md   # H5P matrix, xAPI schemas, spaced retrieval
├── resources/templates/
│   ├── branching-scenario-template.md       # Interactive decision-tree simulation script
│   ├── course-blueprint-template.md         # Module-by-module curriculum matrix
│   ├── course-quality-self-check.md         # Hard/Advisory gate audit & Definition of Done
│   ├── facilitator-guide-template.md        # 3-column timeline facilitator script
│   ├── instructional-design-document-template.md  # Master 8-section enterprise IDD
│   ├── isd-project-timeline-and-pm-plan.md  # Contextual WBS, RACI, & 35-point checklist
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
* **Attribution**: Proprietary frameworks referenced in this work (Understanding by Design®, Action Mapping, Dick & Carey Model, SAM, 4C/ID, UDL) are acknowledged in detail in [ATTRIBUTION.md](ATTRIBUTION.md). All templates are transformative educational adaptations.
