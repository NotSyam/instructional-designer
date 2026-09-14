# L&D Project Recipes & Skill Combinations (COMBINATIONS.md)

> **Inspiration**: Grounded in Trina Rimmer's *Skill Combinations for Common ID Projects* (*id-skills-for-claude*, 2024).  
> **Purpose**: Tested multi-step recipes showing how to combine slash commands, templates, and methodologies for common enterprise L&D challenges.

---

## Recipe 1: The High-Stakes Compliance Overhaul
*Your client requested a generic 1-hour compliance course. You want to transform it into an engaging, behavior-changing intervention.*

1. **Step 1: Performance Gate Check** (`/critique` or Gate 0):
   * Run Mager's test to separate statutory knowledge gaps from organizational culture/process issues.
   * *Output*: Consultative memo reframing the course around high-stakes decision points.
2. **Step 2: Master Architecture** (`/idd`):
   * Assemble M-IDA Layer 1 (ADDIE/Seels & Glasgow) + Layer 2 (Action Mapping) + Layer 3 (Young CBM).
3. **Step 3: Branching Decision Dilemmas** (`/scenario`):
   * Create 3 realistic gray-zone scenarios with natural consequences.
4. **Step 4: Character Casting** (`/character`):
   * Generate character spec sheets with 5 emotional poses for realistic employee avatars.
5. **Step 5: Storyboard & QA** (`/storyboard` ➔ `/qa`):
   * Produce 5-column production blueprint and run 4-tier QA verification before LMS deployment.

---

## Recipe 2: The Complex Technical Troubleshooting Simulation
*Engineering or IT teams need to diagnose critical machine/software failures under operational stress.*

1. **Step 1: Theory Diagnostic** (`/theory-match`):
   * Pair **van Merriënboer's 4C/ID** with **Sweller's Cognitive Load Theory**.
2. **Step 2: Subskills Analysis & Content Chunking** (Cennamo & Kalk):
   * Break the diagnostic workflow into *Whole Tasks*, *Supportive Info*, and *Part-Task Practice*.
3. **Step 3: Creative Treatment** (`/treatment`):
   * Draft 2-column chunk-to-media table mapping terminal telemetry to interactive simulations.
4. **Step 4: Storyboard Production** (`/storyboard`):
   * Detail simulated terminal interfaces, error codes, and step-by-step diagnostic paths.
5. **Step 5: Assessment & GIFT Export** (`/assessment`):
   * Generate scenario-based test bank and export to Moodle XML / Canvas GIFT via `scripts/quiz_to_gift.py`.

---

## Recipe 3: The Rapid Turnaround Microlearning Sprint
*Tight deadline (<2 weeks), limited budget, deskless or shift workers needing quick on-the-job support.*

1. **Step 1: Scaling Model** (Tessmer & Wedman Layers-of-Necessity Layer 1 MVP):
   * Strip all extraneous nice-to-know information; focus strictly on 1 atomic behavior.
2. **Step 2: Microlearning Module Generation** (`/microlearning`):
   * 4-part architecture: Hook (30s), Concept (60s), Practice (60s), Takeaway (30s).
3. **Step 3: Job Aid Cheat Sheet**:
   * Produce a 1-page downloadable decision table or laminated checklist.
4. **Step 4: Spaced Retrieval Booster**:
   * Schedule 1-minute recall prompts for Day 3, Day 7, and Day 21 post-launch.

---

## Recipe 4: The Facilitator-Led Workshop (ILT / VILT)
*Designing a live leadership, sales, or team-building session for instructors to deliver.*

1. **Step 1: Course Plan & Syllabus** (`/course-plan`):
   * Map modules, seat times, Dale's Cone active learning exercises, and Bloom's verbs.
2. **Step 2: Facilitator Guide Production** (`/facilitator-guide`):
   * 3-column timeline script with verbatim dialogue and minute-by-minute pacing (Mode B / Ready Tomorrow Morning).
3. **Step 3: Participant Workbook** (`/workbook`):
   * Action sheets, case studies, and breakout group reflection exercises.
4. **Step 4: Presentation Slide Deck**:
   * Convert outline to Marp Markdown presentation slides via `scripts/outline_to_slides.py`.

---

## Recipe 5: Pre-Flight Adversarial Pedagogy Audit
*You have a completed course draft or vendor submission and need to find every weakness before executive review.*

1. **Step 1: Adversarial Critique** (`/critique` with `stance: adversarial`):
   * Stress-test against 5 lenses: Rigor, Cognitive Demand, Access, Assessment Alignment, Feedback Depth.
2. **Step 2: Identify Smallest Testable Experiment**:
   * Formulate the single micro-intervention with the highest pedagogical ROI.
3. **Step 3: QA Bug Tracking** (`/qa`):
   * Log critical blockers, instructional misalignments, and accessibility issues.
