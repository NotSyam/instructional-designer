# Multi-Lens Instructional Design Critique & Adversarial Audit

> **Foundation**: Grounded in the evidence-backed critique architecture by Fastcat (*instructional-design-critic*, 2024) and formative peer review standards (Cennamo & Kalk, 2019).  
> **Purpose**: Provide a rigorous, evidence-based quality control mechanism that separates personal taste from structural design risk, exposes hidden assumptions, and prescribes the smallest testable alternative.

---

## 1. The Multi-Lens Critique Architecture

Never critique an instructional design based on personal aesthetic preference or gut feeling. Every finding must be grounded in an identifiable **instructional mechanism** and **learner consequence**.

### 1.1 The 5 Specialized Critique Lenses

| Critique Lens | Core Question | Evidence / Risk Tested |
|---|---|---|
| **1. Rigor & Cognitive Demand** | *Does the activity match the promised Bloom's level, or is it low-level recall masquerading as application?* | Sweller's Cognitive Load Theory, Expertise Reversal Effect, shallow multiple-choice items. |
| **2. Alignment & Construct Validity** | *Does the assessment truly measure the real-world performance outcome, or is it testing a proxy test-taking skill?* | Construct underrepresentation, construct-irrelevant difficulty, teaching-to-the-test distortions. |
| **3. Access & Inclusivity (UDL/WCAG)** | *Can every learner perceive, operate, and comprehend the experience regardless of physical or cultural background?* | WCAG 2.2 AA standards, UDL 3 pillars (Engagement, Representation, Action & Expression), reading level. |
| **4. Feedback & Decision Architecture** | *Does the feedback explain the causal mechanism and natural consequences, or merely announce Right/Wrong?* | Knowledge of correct response vs. elaborate explanatory feedback; plausible distractors vs. obvious giveaways. |
| **5. Transfer & Real-World Utility** | *Will this competence survive outside the training environment and bridge the knowing-doing gap?* | Far transfer, procedural automaticity, job aid scaffolding, environmental friction. |

---

## 2. Critique Stances (How to Frame the Review)

When running a critique (via `/critique` or `/audit`), select the stance matching the project's current phase:

1. **Supportive Stance** (Ideal for early ideation / Define Phase):  
   * Highlights existing strengths and suggests natural extensions.
   * Focuses on building momentum and protecting designer confidence while flagging 1–2 key risks.
2. **Balanced Stance** (Default / Design Phase):  
   * Weighs trade-offs equitably: identifies what works, what carries risk, and the design compromises made (e.g. speed vs. depth).
   * Delivers an objective assessment of both sides.
3. **Adversarial / Devil's Advocate Stance** (Mandatory before High-Stakes Launch / Demonstrate Phase):  
   * Rigorously pressure-tests the design as a skeptical auditor, unmotivated learner, or cynical executive.
   * Actively seeks failure points: *"Where will learners disengage? Where will the LMS break? Where will the SME claim they were misquoted?"*

---

## 3. The "Smallest Testable Alternative" Protocol

A poor critique tells the designer: *"Scrap everything and rewrite from scratch."* This causes defensiveness and project paralysis.  
An expert critique identifies the **Single Smallest Testable Experiment** that yields the highest instructional payoff:

```
┌─────────────────────────────────────────────────────────────────────────┐
│              THE SMALLEST TESTABLE EXPERIMENT TEMPLATE                  │
├─────────────────────────────────────────────────────────────────────────┤
│ 1. Current Risk:                                                        │
│    [e.g. 20-minute lecture on compliance rules produces zero retention] │
│ 2. Smallest Alternative:                                                │
│    [Replace 5 minutes of slides with 1 realistic dilemma card where     │
│     learners choose between 2 legally gray vendor gifts]                │
│ 3. Expected Signal / Metric:                                            │
│    [Compare quality and nuance of learner rationale on posttest,        │
│     not seat time or completion percentage]                             │
│ 4. Review Question for SME / Client:                                    │
│    ["Has anyone on the team ever accepted a vendor invitation like this │
│     in real life? What was the gray area?"]                             │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Standard Critique Output Format

When invoking a design critique, produce the evaluation in this structured format:

```markdown
### 🔎 Instructional Design Critique Report

* **Design Summary**: [1–2 sentence objective description of what is being proposed]
* **Design Promise vs. Reality**: [What the design claims to achieve vs. what cognitive architecture predicts]
* **Selected Lens & Stance**: [e.g. Lens: Rigor & Cognitive Demand | Stance: Adversarial]

#### 1. Core Strengths (What Works)
* [Strength 1 grounded in learning science mechanism]

#### 2. Material Risks & Hidden Assumptions
* **Risk 1**: [Description of failure mode]
  * *Hidden Assumption*: [What the designer implicitly assumed about the learner]
  * *Learner Consequence*: [How the learner will actually experience or fail this]
  * *Evidence Base*: [Sweller / Mayer / Mager / Cennamo citation]

#### 3. Trade-Off Analysis
* [Explicit acknowledgment of constraints: budget, timeline, authoring tool limits]

#### 4. The Smallest Testable Experiment
* **The Intervention**: [Specific 5-minute tweak or component replacement]
* **Measurement Signal**: [Observable metric of success]
* **Key SME Review Question**: [Targeted question to ask the subject matter expert]
```
