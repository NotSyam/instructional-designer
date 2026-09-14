# E-Learning Quality Assurance (QA) & Bug Tracker

> **Source Methodology**: Trina Rimmer (*id-skills-for-claude*, 2024), *Quality Assurance Testing for E-Learning*  
> **Purpose**: Systematic 4-tier pre-delivery verification to catch functional breakdowns, instructional misalignment, editorial typos, and accessibility barriers before client/learner release.

---

## 1. The 4 Testing Tiers Overview

1. **Tier 1: Functional QA**: Triggers, branching logic, score passing to LMS (SCORM/xAPI), bookmarking, audio controls, device responsiveness.
2. **Tier 2: Instructional QA**: Alignment with objectives, feedback accuracy, scenario consequence realism, question validity, cognitive load balance.
3. **Tier 3: Editorial QA**: Grammar, consistent capitalization, glossary terms, voiceover timing vs. OST, nomenclature standards.
4. **Tier 4: Accessibility QA (WCAG 2.2 AA)**: Color contrast (4.5:1 minimum), keyboard tab order, screen reader descriptions (alt-text), closed caption synchronization.

---

## 2. Bug Tracking & Remediation Log

| Bug ID | Screen / Asset ID | QA Tier | Severity | Description of Issue & Steps to Reproduce | Expected Behavior | Assigned To | Status | Verification & Sign-Off |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|
| **BUG-01** | `SC-08` | Functional | **Critical** | Selecting Option B triggers infinite loading spinner; course cannot progress. | Option B displays feedback layer SC-08B and reveals Next button. | Developer | Fixed | Verified by ID (2026-09-14) |
| **BUG-02** | `SC-04` | Instructional | **Major** | Feedback states ground beef can sit at room temp for 6 hours (contradicts USDA rule). | Feedback must state maximum 2 hours (or 1 hour above 90°F). | SME / Writer | Open | Pending SME re-check |
| **BUG-03** | `SC-12` | Editorial | **Minor** | Typo in header: "Prosedure" instead of "Procedure". | Correct spelling to "Procedure". | Copyeditor | Fixed | Verified |
| **BUG-04** | `SC-01` | Accessibility | **Major** | Video player lacks toggleable Closed Captions (CC) button. | CC button present; `cc_sc01.vtt` captions display correctly on toggle. | Media Dev | Open | In Progress |

### Severity Classifications:
* **Critical (Blocker)**: Crash, infinite loop, blocked navigation, data loss, LMS score not recording. (Course CANNOT ship).
* **Major**: Factual error in content, misaligned answer key, missing required media asset, failed WCAG color contrast.
* **Minor**: Inconsistent font size, minor layout misalignment, non-critical audio clip clipping.
* **Cosmetic**: Minor spacing imperfection, subtle color tint difference.

---

## 3. Pre-Delivery Sign-Off Checklist
- [ ] **100% Critical & Major Bugs Resolved**: Zero open blockers.
- [ ] **LMS Communication Verified**: Tested in SCORM Cloud or target LMS (Completion, Success, Score, Time tracked).
- [ ] **Multi-Device Smoke Test**: Tested on Desktop (Chrome, Edge, Safari) and Mobile/Tablet viewport.
- [ ] **Audio/Script Match**: Voiceover narration matches final signed-off script 100%.
- [ ] **Client Final Authorization**: Project Manager and Client Liaison signatures recorded.
