# Instructional Designer AI Agent Skill (v3.2.0)

[![Agent Skills Standard](https://img.shields.io/badge/Agent_Skills_Standard-v2.0-blue.svg)](https://github.com/GarethManning/education-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.2.0-green.svg)](CHANGELOG.md)
[![Tests](https://img.shields.io/badge/Tests-Passing_6/6-brightgreen.svg)](tests/test_scripts.py)
[![Compatible](https://img.shields.io/badge/Harnesses-Claude_|_Codex_|_Hermes_|_Antigravity-purple.svg)](SKILL.md)

An evidence-grounded **AI Agent Skill for Instructional Designers, L&D Consultants, and Curriculum Architects**.

Helps practitioners transform training requests into **measurable, cognitively sound, and turnkey learning deliverables** - integrating classical instructional systems design (ADDIE, Dick & Carey, Mager) with contemporary learning sciences (retrieval practice, cognitive load theory, and universal design).

---

## Key Capabilities

### 1. Weighted Framework Scoring & Hybrid Architectures
Unlike rigid categorical ID templates, this skill evaluates learning projects across **5 core dimensions**:
- **Stakes & Failure Cost** (Safety-critical vs. business impact vs. foundational)
- **Skill Complexity** (Complex cognitive & heuristics vs. procedural vs. conceptual)
- **Timeline & Delivery Cadence** (Agile/rapid <6 weeks vs. standard 8-16 weeks)
- **Primary Outcome Type** (On-the-job behavior change vs. regulatory compliance vs. academic transfer)
- **Organizational Governance** (Audit/waterfall vs. agile pods vs. higher-ed)

It formally supports **Hybrid Architectures**:
* **Behavioral Agile**: *Cathy Moore Action Mapping* (practice scenarios) + *SAM* (iterative sprint prototyping).
* **Technical Rigor & Decision Transfer**: *Dick & Carey* (task hierarchy & entry behavior tests) + *Action Mapping* (ethical/incident branching dilemmas).
* **Academic Enterprise**: *Backward Design (UbD)* (enduring understandings & GRASPS authentic assessment) + *ADDIE* (macro operational rollout).
* **Complex Systems**: *4C/ID* (whole tasks & supportive information) + *SAM* (phased prototype releases).

### 2. Contemporary Learning Sciences Integration
Directly informs design decisions with modern empirical research:
* **Retrieval Practice & Spaced Testing** (Roediger & Karpicke, 2006; Dunlosky et al., 2013).
* **Advanced Cognitive Load Theory & Expertise Reversal Effect** (Sweller, 2011; Kalyuga, 2007).
* **3-Pillar Universal Design for Learning** (CAST, 2018: Representation, Action & Expression, Engagement).
* **Social Learning & Communities of Practice** (Wenger-Trayner, 2015).

### 3. Enterprise IDD & Project Management
* **Master 8-Section IDD Template**: Covers business gap, audience persona, adaptive pedagogy, Bloom's matrix, module blueprint, Kirkpatrick L1-L4 / Phillips ROI, technical specs, and RACI governance.
* **ATD-Aligned ISD Project Management**: 16-week WBS master schedule, RACI matrix, Change Control protocol, and 35-point ISD Quality Checklist.

### 4. Verified LMS & Slide Automation Utilities
Includes verified, unit-tested Python utilities (zero external dependencies required):
* `scripts/quiz_to_gift.py`: Converts Markdown quizzes into Canvas/Moodle **GIFT** and **Moodle XML** formats.
* `scripts/outline_to_slides.py`: Transforms course outlines into presentation-ready **Marp Markdown** slide decks.
* Verified via unit tests (`tests/test_scripts.py`) with sample fixtures in `examples/`.

### 5. Graceful Tool Fallbacks
When external document skills (`hermes/docx`, `hermes/pptx`, `hermes/xlsx`) are unavailable, the skill automatically degrades gracefully to standalone Python scripts or universal Markdown/CSV formats.

---

## Repository Structure

```
|-- .codex-plugin/
|   `-- plugin.json                          # OpenAI Codex manifest
|-- examples/
|   |-- sample_outline.md                    # Fixture for slide generation
|   `-- sample_quiz.md                       # Fixture for GIFT/XML quiz generation
|-- references/
|   |-- accessible-learning-wcag.md          # WCAG 2.2 AA & UDL compliance checklist
|   |-- document-production.md               # Toolchain routing & 3-tier fallback protocols
|   |-- idd-and-isd-methodology.md          # Weighted scoring, hybrid patterns, & sign-off guide
|   |-- isd-quality-and-pm-standards.md      # 48 intake questions & 37-point audit checklist
|   |-- knowledge-base.md                    # 75+ learning theories & contemporary research
|   `-- modern-edtech-and-microlearning.md   # H5P matrix, xAPI schemas, spaced retrieval
|-- resources/templates/
|   |-- branching-scenario-template.md       # Interactive decision-tree simulation script
|   |-- course-blueprint-template.md         # Module-by-module curriculum matrix
|   |-- course-quality-self-check.md         # Structured Hard & Advisory gate audit table
|   |-- facilitator-guide-template.md        # 3-column timeline facilitator script
|   |-- instructional-design-document-template.md  # Master 8-section enterprise IDD
|   |-- isd-project-timeline-and-pm-plan.md  # 16-week WBS, RACI, & 35-point checklist
|   `-- rubric-matrix-template.md            # 4-tier analytic evaluation rubric
|-- scripts/
|   |-- outline_to_slides.py                 # Marp slide deck generator
|   `-- quiz_to_gift.py                      # Canvas/Moodle GIFT & XML quiz exporter
|-- tests/
|   `-- test_scripts.py                      # Unit test suite for automation scripts
|-- ATTRIBUTION.md                           # Third-party framework attribution & fair-use disclaimers
|-- CHANGELOG.md                             # Version history & release notes
|-- LICENSE                                  # MIT License
|-- package.json                             # SkillHub metadata
|-- README.md                                # Project documentation
|-- requirements.txt                         # Dependency specifications
`-- SKILL.md                                 # Streamlined Agent Skills Standard v2 specification
```

---

## Installation & Multi-Harness Usage

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
Clone into your custom skill directory:
```bash
git clone https://github.com/NotSyam/instructional-designer.git ~/.claude/skills/instructional-designer
```

---

## Testing the Scripts

Run the automated test suite locally:
```bash
python -m unittest tests/test_scripts.py
```

---

## Attribution & License

* **License**: [MIT License](LICENSE)
* **Attribution**: Proprietary frameworks referenced in this work (Understanding by Design, Action Mapping, Dick & Carey Model, SAM, 4C/ID, UDL) are acknowledged in detail in [ATTRIBUTION.md](ATTRIBUTION.md). All templates are transformative educational adaptations.
