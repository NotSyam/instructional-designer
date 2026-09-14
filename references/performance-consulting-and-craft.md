# Performance Consulting, Craft Nuance, & AI Failure Modes Guard

> **Foundation**: Grounded in performance analysis by Robert Mager & Peter Pipe (1997), Cathy Moore (2017), and modern e-learning craft heuristics by Trina Rimmer (*id-skills-for-claude*, 2024).  
> **Purpose**: Equip instructional designers with the judgment to identify non-training problems, navigate stakeholder politics, eliminate cosmetic interactivity, and avoid common AI-generated design failures.

---

## 1. The "When NOT to Design" Protocol (Performance Consulting)

One of the highest-value capabilities of an expert Instructional Designer is knowing **when training is the wrong answer**—and possessing the professional courage and diplomatic language to say so.

### 1.1 The Inherent Bias of AI vs. Human Performance Consulting
> [!WARNING]
> Large Language Models (LLMs) are naturally predisposed to generate content. When handed an ambiguous request like *"Our sales reps need training on data entry"*, a naive AI immediately spits out a 5-module curriculum outline. An expert consultant, however, first investigates whether the CRM software is broken or the incentive structure penalizes logging data.

### 1.2 The "Is-It-Really-A-Training-Problem?" Diagnostic Test (Mager Test)

Before outlining any course, evaluate these 5 diagnostic filters:

1. **The Life-or-Death Test (Mager & Pipe)**:  
   * *"Could the performers execute this task correctly if their lives or jobs depended on it right now?"*  
   * **If YES**: The issue is **NOT a knowledge/skill deficit**. It is a problem of motivation, broken incentives, ambiguous feedback, faulty tools, or unmanageable workload. Training will fail.
2. **The Historical Competence Test**:  
   * *"Did they ever perform this task correctly in the past?"*  
   * **If YES**: What changed? (Did management change? Did software update without documentation? Did team size shrink by 40%?). A change in environment cannot be fixed by training.
3. **The Consequence & Feedback Test**:  
   * *"What happens immediately when someone performs correctly vs. incorrectly?"*  
   * If correct performance takes 3x longer and goes unrewarded, or if incorrect performance has zero visible consequence, the problem is an **accountability and incentive architecture failure**.
4. **The Job Aid vs. Course Test**:  
   * *"Does this task occur frequently with rapid recall needed (e.g. emergency CPR), or is it an infrequent, high-step procedural task (e.g. quarterly tax reconciliation)?"*  
   * Infrequent procedural tasks **MUST NOT be forced into memorization courses**. They require a 1-page Job Aid, checklist, or inline software wizard.
5. **The Capacity & Selection Test**:  
   * *"Do the individuals possess the basic cognitive or physical capacity and tools required for the role?"*

### 1.3 Decision Matrix: Course vs. Alternative Interventions

| Root Cause Identified | Recommended Intervention | Actionable Designer Recommendation |
|---|---|---|
| **Lack of Knowledge / Skill** | **Interactive Training / Simulation** | Build scenario-based practice with immediate feedback. |
| **Infrequent Complex Procedure** | **Job Aid / Quick-Reference Guide** | Create step-by-step checklist, decision tree, or cheat sheet. |
| **Flawed Process / Software UX** | **Process Improvement / UX Fix** | Recommend workflow restructuring or UI simplification. |
| **Misaligned Incentives** | **Management / Reward Redesign** | Deliver consultative memo highlighting contradictory KPIs. |
| **Unclear Standards / Expectations** | **SOP Documentation & Management Coaching** | Draft clear service-level agreements (SLAs) and managerial rubrics. |

### 1.4 How to Deliver the "No-Course" Recommendation Diplomatically
Never tell a stakeholder: *"Your idea is bad and training won't work."*  
Use the consultative reframing protocol:
1. **Acknowledge the Strategic Urgency**: *"I completely share your commitment to eliminating billing errors in Q3."*
2. **Present Empirical Findings**: *"In our root-cause analysis, 92% of operators demonstrated correct protocol knowledge when tested, but the ERP system requires 14 redundant clicks across 3 unintegrated screens."*
3. **Propose the Higher-ROI Solution**: *"If we build a 2-hour training course, the error rate will likely persist because the system friction remains. Instead, by introducing an automated auto-fill script and a 1-page job aid, we can save 200 hours of development time and resolve the errors at the source."*

---

## 2. AI Failure Modes Guard in Instructional Design

When using AI agents in curriculum development, the agent MUST actively enforce guards against these 4 classic AI failure modes:

### 2.1 Failure Mode A: The "Laughably Obvious" Multiple-Choice Distractor
* **The AI Tendency**: Creating 1 clearly correct answer, 2 nonsensical jokes, and 1 morally evil choice. (Learner easily guesses without thinking).
* **The Guard Rule**: All distractors must represent **plausible, authentic misconceptions or common near-miss errors** actually observed in the workplace.
* *Poor*:  
  A. Follow the sanitation protocol  
  B. Ignore all safety rules and laugh  
  C. Eat the contaminated sample  
* *Robust*:  
  A. Rinse tools in lukewarm tap water for 10 seconds *(common trap: assumes water alone removes pathogens)*  
  B. Submerge tools in a 1:10 bleach solution for 15 minutes *(correct)*  
  C. Wipe tools with a dry microfiber cloth before reusing *(near-miss: visually clean but biologically contaminated)*  

### 2.2 Failure Mode B: Cosmetic vs. Meaningful Interactivity
* **The AI Tendency**: Recommending *"Click each of the 4 tabs to read the 4 principles"* (passive text-dump masquerading as active learning).
* **The Guard Rule**: An interaction is only meaningful if it requires **cognitive processing, decision-making, or prediction**.
* *Transformation*: Instead of clicking tabs to reveal definitions, present a realistic client dilemma and require the learner to categorize which principle is being violated.

### 2.3 Failure Mode C: Additive Redundancy in UI Controls
* **The AI Tendency**: Cluttering the interface with explicit instructions on how to use intuitive controls: *"Click the Next button below to advance to the next screen."*
* **The Guard Rule**: UI controls must communicate their own purpose. Reserve on-screen text strictly for instructional prompts and cognitive cues.

### 2.4 Failure Mode D: Preachy / Moralizing Tone in Sensitive Topics
* **The AI Tendency**: Lecturing learners with heavy-handed moral statements in compliance, DEI, ethics, or harassment training.
* **The Guard Rule**: Calibrate tone to **Empathy and Practical Utility**. Present complex, ambiguous ethical gray zones where well-intentioned people make subtle errors. Focus on natural consequences and organizational safety rather than scolding.

---

## 3. Authoring Tool Capabilities & Constraints (Industry Reality)

When designing e-learning architectures, align the design specifications to the target tool's technological reality:

| Tool | Ideal Use Case | Strengths | Constraints / Anti-Patterns |
|---|---|---|---|
| **Articulate Rise 360** | Rapid development, mobile-first responsive delivery, information-dense reference courses, light knowledge checks. | Fast production, modular blocks, pristine typography across mobile/tablet/desktop, zero programming. | Limited custom branching logic, cannot build complex multi-state simulations or custom mathematical variables. |
| **Articulate Storyline 360** | High-fidelity branching scenarios, software simulations, gamified mechanics, custom variables & triggers, complex states. | Pixel-perfect control, custom layers, conditional branching, xAPI trigger statements, custom state tracking. | Slower production time, fixed aspect-ratio scaling (not fluid responsive), requires detailed storyboards. |
| **Custom HTML5 / SCORM Web App** | Tailored web apps, interactive calculators, bespoke sound synthesis (Web Audio API), client-side encryption. | Complete architectural freedom, modern CSS (Tailwind), lightweight asset footprint. | Requires web developer / programming expertise, higher initial build cost. |
