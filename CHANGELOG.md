# Changelog

All notable changes to the instructional-designer AI Agent Skill will be documented in this file.
The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

---

## [3.2.0] - 2026-09-03
### Added
- **Weighted Multi-Dimensional Scoring Engine**: Replaced rigid categorical framework matching with a 5-dimension weighted assessment (Stakes, Complexity, Timeline, Goal Type, Governance).
- **Official Hybrid Framework Architectures**: Formalized 4 standard hybrid patterns (Action Mapping + SAM, Dick & Carey + Action Mapping, UbD + ADDIE, 4C/ID + SAM) with real-world case studies and trade-off analyses.
- **Contemporary Learning Sciences Integration**:
  - Retrieval Practice & Spaced Repetition (Roediger & Karpicke 2006, Dunlosky 2013).
  - Advanced Cognitive Load Theory & Expertise Reversal Effect (Sweller 2011, Kalyuga 2007).
  - Full 3-Pillars Universal Design for Learning (CAST 2018).
  - Social Learning & Communities of Practice (Wenger-Trayner 2015).
- **Script Testing & Quality Suite**:
  - Added requirements.txt for dependencies.
  - Added test fixtures examples/sample_quiz.md and examples/sample_outline.md.
  - Added automated unit test suite tests/test_scripts.py covering GIFT, Moodle XML, and Marp deck generation.
- **Graceful Tool Fallbacks**: 3-tier fallback protocol when external document skills (hermes/*) are unavailable.
- **Third-Party Attribution**: Created ATTRIBUTION.md explicitly crediting proprietary models (UbD, Action Mapping, Dick & Carey, SAM, 4C/ID, CAST).

### Changed
- **YAML Frontmatter Simplification**: Streamlined SKILL.md frontmatter from 140+ lines of nested tables to a clean, flat, high-efficiency Agent Skills Standard v2 format.
- **Structured Quality Self-Check**: Partitioned design verification into strict Hard Gates (Must-Pass) and Advisory Gates with actionable remediation paths.
- **README Tone Refinement**: Replaced unverified marketing superlatives with clear, transparent, and professionally validated capability documentation.

---

## [3.1.0] - 2026-08-29
### Added
- Enterprise-grade 8-section Master Instructional Design Document (IDD) template.
- 16-week ISD Project Management Plan, WBS matrix, RACI matrix, and 35-point ISD Quality Checklist (ATD-aligned).
- Framework-adaptive IDD routing logic in references/idd-and-isd-methodology.md.
- Pressure Test 11: Framework-Adaptive IDD Generation.

---

## [3.0.0] - 2026-08-22
### Added
- Conformance with Agent Skills Standard v2 (input/output typing, evidence strength, chaining metadata).
- Generation-time 7-point self-audit and post-generation Quality Self-Check table.
- Comprehensive suite of 10 Functional Pressure Tests (pressure-tests/).
- Multi-harness compatibility manifests (.codex-plugin/plugin.json, package.json).

---

## [2.1.0] - 2026-08-15
### Added
- Hermes document production skills routing table (references/document-production.md) for DOCX, XLSX, PDF, and PPTX generation.
- WCAG 2.2 AA accessibility checklist and UDL integration matrix.

---

## [2.0.0] - 2026-08-01
### Added
- Core ID frameworks: ADDIE, Bloom's Revised Taxonomy, Merrill's First Principles, Keller's ARCS, Dale's Cone, Gagne's 9 Events, Kirkpatrick 4 Levels, Knowles' Andragogy.
- Dual operating modes: Mode A (ID Consultant) and Mode B (Production / Enterprise Ready).
- Python automation utilities: quiz_to_gift.py and outline_to_slides.py.
- Standardized templates: Course Blueprint, Facilitator Guide, Branching Scenario, Performance Rubric.

---

## [1.0.0] - 2026-07-15
### Added
- Initial release of the foundational Instructional Designer agent prompt and core pedagogy guidelines.
