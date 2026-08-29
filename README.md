# 🎓 Instructional Designer AI Agent Skill (v3.1.0)

[![Agent Skills Standard](https://img.shields.io/badge/Agent_Skills_Standard-v2.0-blue.svg)](https://github.com/GarethManning/education-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.1.0-green.svg)](https://github.com/NotSyam/instructional-designer/releases)
[![Multi-Harness](https://img.shields.io/badge/Compatible-Claude_|_Codex_|_Hermes_|_Antigravity-purple.svg)](https://github.com/NotSyam/instructional-designer)

An enterprise-grade, evidence-grounded **AI Agent Skill for Instructional Designers, L&D Consultants, and Curriculum Architects**.

Designed to transform ambiguous training needs into **outcome-driven, measurable, and turnkey learning deliverables**—grounded in cognitive science, adult learning principles, and modern EdTech standards.

---

## 🌟 Key Capabilities

* **📐 Framework-Adaptive Instructional Design Documents (IDD)**: Dynamically adapts the structural architecture of the IDD based on the pedagogical model:
  * **ADDIE Classic** (Comprehensive macro enterprise programs)
  * **SAM** (Rapid agile e-learning & iterative prototyping)
  * **Dick & Carey** (High-stakes technical, clinical, and compliance systems)
  * **Cathy Moore Action Mapping** (Performance-first corporate training)
  * **Backward Design / UbD** (Higher ed, K-12, and deep conceptual transfer)
  * **4C/ID Model** (Complex cognitive skills & software architecture)
* **📋 ATD-Aligned Project Management Plan**: 16-week WBS master schedule, RACI matrix, Change Management protocols, and 35-point ISD Quality Checklist.
* **🎭 Dual Operating Modes**:
  * `Mode A (ID Consultant)`: Explains pedagogical rationale, tags Bloom's cognitive levels, and cites frameworks inline.
  * `Mode B (Production / Enterprise Ready)`: Produces clean, turnkey deliverables (facilitator scripts, participant workbooks, scenario cards) with **zero instructional jargon**.
* **⚙️ LMS & Presentation Automation**:
  * `quiz_to_gift.py`: Converts Markdown quizzes into Canvas/Moodle **GIFT** or **Moodle XML** formats.
  * `outline_to_slides.py`: Transforms course outlines into presentation-ready **Marp Markdown** slide decks.
* **♿ Accessibility & Inclusion**: Built-in **WCAG 2.2 Level AA** compliance auditing and Universal Design for Learning (UDL) matrices.

---

## 📂 Repository Structure

```
├── .codex-plugin/
│   └── plugin.json                          # OpenAI Codex plugin manifest
├── references/
│   ├── accessible-learning-wcag.md          # WCAG 2.2 AA & UDL compliance checklist
│   ├── document-production.md               # Hermes document skills toolchain routing
│   ├── idd-and-isd-methodology.md          # Comprehensive IDD methodology & RACI guide
│   ├── isd-quality-and-pm-standards.md      # Standar 48 Qs Intake & 37-Point Audit ATD
│   ├── knowledge-base.md                    # 75+ foundational learning theories & models
│   └── modern-edtech-and-microlearning.md   # H5P matrix, xAPI schemas, spaced retrieval
├── resources/templates/
│   ├── branching-scenario-template.md       # Interactive decision-tree simulation script
│   ├── course-blueprint-template.md         # Module-by-module curriculum matrix
│   ├── course-quality-self-check.md         # Mandatory design quality gate audit table
│   ├── facilitator-guide-template.md        # 3-column timeline facilitator script
│   ├── instructional-design-document-template.md  # Master 8-section enterprise IDD
│   ├── isd-project-timeline-and-pm-plan.md  # 16-week WBS, RACI, & 35-point ISD checklist
│   └── rubric-matrix-template.md            # 4-tier analytic evaluation rubric
├── scripts/
│   ├── outline_to_slides.py                 # Marp slide deck generator
│   └── quiz_to_gift.py                      # Canvas/Moodle GIFT & XML quiz exporter
├── package.json                             # SkillHub package metadata & keywords
├── README.md                                # Project documentation & portfolio guide
└── SKILL.md                                 # Agent Skills Standard v2 specification
```

---

## 🛠️ Multi-Harness Compatibility & Installation

This skill conforms to the open **Agent Skills Standard (v2)** and runs natively across major agent platforms:

### 1. Google Antigravity (AGY)
Clone or copy this repository into your skills directory:
```bash
git clone https://github.com/NotSyam/instructional-designer.git ~/.gemini/antigravity/skills/instructional-designer
```

### 2. Hermes Agent
Add as a skill tap or local directory:
```bash
hermes skills install NotSyam/instructional-designer
```

### 3. OpenAI Codex
The `.codex-plugin/plugin.json` manifest is included for native discovery in Codex environments.

### 4. Claude Code CLI / Claude.ai
Install directly via Claude Code plugin or place in `~/.claude/skills/`.

---

## 🧪 Example Triggers & Prompts

* **Master IDD Creation**:
  > *"Create an enterprise Instructional Design Document (IDD) for a 60-minute compliance training on Anti-Bribery & FCPA. Target audience is 200 regional sales directors. Use Cathy Moore Action Mapping to focus on scenario practice."*
* **Facilitator Guide (Mode B)**:
  > *"Generate a 90-minute client-ready Facilitator Guide for a new manager conflict resolution workshop. Format in Mode B with zero L&D jargon."*
* **Branching Scenario**:
  > *"Design a 3-level branching decision tree simulation for customer service escalation handling."*

---

## 📜 License & Attribution

* **License**: [MIT License](LICENSE)
* **Author**: [NotSyam](https://github.com/NotSyam)
* **Grounding References**: Grounded in seminal works by Bloom (1956/2001), Kirkpatrick (1959–1994), Keller (1987), Knowles (1984), Gagné (1965), Merrill (2002), Sweller (1988), Mayer (2001), Collins et al. (1989), Wiggins & McTighe (2005), and Cathy Moore (2017).
