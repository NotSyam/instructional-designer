# Modern EdTech, Microlearning & Learning Analytics Reference

This guide provides practical frameworks for architecting modern digital learning experiences, including microlearning modularity, interactive H5P integration, xAPI telemetry tracking, and AI-assisted learning experiences.

---

## 1. Microlearning Architecture & Spaced Retrieval

Microlearning delivers focused, bite-sized learning units (typically 3–5 minutes) designed for immediate on-the-job application or spaced retention.

### A. The 4-Part Micro-Nugget Anatomy
Every microlearning module should focus on a **single, discrete outcome**:

1. **The Hook (15–30 sec)**: Immediate real-world problem statement, friction point, or surprising metric.
2. **Core Model / Action (1.5–2.5 min)**: Concise demonstration, visual breakdown, or step-by-step procedure (avoid conceptual fluff).
3. **Active Practice / Decision Check (1–1.5 min)**: Single scenario-based question, diagnostic choice, or quick task.
4. **Takeaway & Immediate Action (30 sec)**: 1-sentence synthesis + job-aid download or workflow prompt.

### B. Spaced Retrieval Booster Campaign
To overcome Ebbinghaus's Forgetting Curve, pair microlearning with an automated spaced reinforcement schedule:

| Timeline | Channel | Format | Cognitive Focus |
| :--- | :--- | :--- | :--- |
| **Day +1** | Slack / Teams / Email | 1-question scenario poll | Recall & Immediate Comprehension |
| **Day +3** | LMS / Mobile App | 2-minute worked example | Application & Troubleshooting |
| **Day +7** | Chatbot / Nudge | "What would you do?" dilemma | Critical Decision-making (Evaluate) |
| **Day +21** | Manager 1-on-1 | Observation checklist prompt | Real-world Behavioral Transfer (Level 3) |

---

## 2. Interactive H5P Component Selection Matrix

H5P allows rapid authoring of responsive, interactive HTML5 learning activities without complex coding. Match the activity type to your learning objective:

| H5P Activity Type | Best For | Cognitive Level (Bloom's) | Pedagogical Rationale |
| :--- | :--- | :--- | :--- |
| **Branching Scenario** | High-stakes decision trees, customer service, safety simulations | *Apply, Analyze, Evaluate* | Provides safe environment for trial-and-error with immediate, natural consequences. |
| **Interactive Video** | Software walkthroughs, live demos, lecture-recording enrichment | *Remember, Understand, Apply* | Embeds knowledge checks, bookmarks, and formative quizzes directly at key video timestamps. |
| **Drag the Words / Mark the Words** | Terminology reinforcement, syntax checks, compliance rules | *Remember, Understand* | Active recognition with tactile engagement. |
| **Flashcards / Dialog Cards** | Spaced retrieval practice, language learning, vocabulary drills | *Remember* | Low-friction retrieval practice with self-scoring. |
| **Accordion / Tabbed Content** | Reducing cognitive load in reference material / policy manuals | *Understand* | Hides secondary detail until needed, preventing visual overload. |
| **Documentation Tool** | Guided project drafting, action planning, portfolio generation | *Create* | Step-by-step form wizard that exports a formatted learner action plan or report. |

> ⚠️ **Accessibility caveat**: H5P **Drag the Words**, **Drag the Boxes**, and other drag-and-drop activity types fail keyboard-only navigation (WCAG 2.1 SC 2.1.1). Always provide an accessible alternative format for these activities — e.g., dropdown selection menus or multi-choice lists — as required by the WCAG 2.2 AA checklist in `references/accessible-learning-wcag.md`. Branching Scenario, Interactive Video, Flashcards, Accordion, and Documentation Tool are generally keyboard-accessible when configured correctly.

---

## 3. xAPI (Experience API / Tin Can) Telemetry Mapping

Unlike traditional SCORM (which only tracks *completion*, *time*, and *final score*), **xAPI** captures granular learner interactions across any platform (LMS, mobile apps, simulations, VR, chatbots) using standard **Actor-Verb-Object** statements sent to a **Learning Record Store (LRS)**.

### A. Standard xAPI Verbs & Event Triggers

| Verb URI / Name | Trigger Event | Context / Payload Example |
| :--- | :--- | :--- |
| `http://adlnet.gov/expapi/verbs/launched` | Learner opens module/activity | Module ID, device type, timestamp |
| `http://adlnet.gov/expapi/verbs/interacted` | Learner clicks hotspot, toggles layer, or pauses video | Video timestamp, UI element ID |
| `http://adlnet.gov/expapi/verbs/answered` | Learner submits a quiz or branching choice | Question ID, selected choice, correct answer, response latency |
| `http://adlnet.gov/expapi/verbs/completed` | Learner finishes all required steps in unit | Unit ID, completion percentage |
| `http://adlnet.gov/expapi/verbs/passed` / `failed`| Learner reaches mastery threshold | Score achieved, passing score threshold, duration |

### B. Sample xAPI Statement Payload (Branching Simulation)

```json
{
  "actor": {
    "name": "Alex Johnson",
    "mbox": "mailto:alex.johnson@company.com"
  },
  "verb": {
    "id": "http://adlnet.gov/expapi/verbs/answered",
    "display": { "en-US": "answered" }
  },
  "object": {
    "id": "https://learning.company.com/scenarios/customer-escalation/node-1",
    "definition": {
      "name": { "en-US": "Decision Point 1: Responding to Angry Client" },
      "description": { "en-US": "Learner chose Option A (De-escalation with Empathy)" },
      "type": "http://adlnet.gov/expapi/activities/cmi.interaction",
      "interactionType": "choice"
    }
  },
  "result": {
    "success": true,
    "response": "option_a",
    "score": { "raw": 100, "scaled": 1.0 }
  },
  "context": {
    "contextActivities": {
      "parent": [{ "id": "https://learning.company.com/courses/manager-excellence" }]
    }
  }
}
```

---

## 4. AI-Assisted Learning & Conversational Tutors

When designing AI-powered learning experiences (e.g., automated role-play partners or Socratic tutors), use the following prompt architectures:

### A. Socratic AI Tutor Architecture
* **Persona**: Supportive subject matter mentor.
* **Instructional Guardrail**: **Never give the direct answer**. When a learner asks for help, diagnose their current reasoning, provide a targeted hint or counter-example, and ask a scaffolding question.
* **Scaffolding Levels**: Level 1 (Guiding question) $\to$ Level 2 (Partial hint / analogy) $\to$ Level 3 (Worked example with missing final step).

### B. AI Simulation & Role-Play Bot Persona Prompt Template

```markdown
You are roleplaying as [Stakeholder Persona: e.g., Pat, a frustrated client whose shipment is 4 days late].

**Your Personality & Stance**:
- Skeptical, impatient, but will soften if the learner demonstrates genuine empathy, active listening, and a concrete resolution plan.
- If the learner makes excuses or quotes policy without empathy, increase your frustration level.

**Learner Objective**:
- De-escalate the situation and agree upon an updated delivery timeline without offering unapproved financial concessions.

**Interaction Rules**:
1. Stay in character at all times.
2. Keep responses realistic and conversational (2-4 sentences per turn).
3. Do not break character to explain instructions.
4. When the learner reaches an agreement or critical impasse, end the conversation with `[SCENARIO COMPLETE]` to trigger the debrief.
```
