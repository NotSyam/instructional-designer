# Instructional Design Document (IDD) & ISD Methodology Reference

> **Version**: 3.2.0 | **Domain**: Curriculum Architecture, L&D Enterprise Documentation, & Project Governance

---

## 1. The L&D Documentation Hierarchy

An **Instructional Design Document (IDD)** serves as the master architectural contract between the Instructional Designer, Stakeholders, SMEs, and Developers before media production or storyboarding begins.

```
+----------------------------------------------------------------------------------------+
|                        HIERARKI DOKUMENTASI INSTRUCTIONAL DESIGN                       |
+----------------------------------------------------------------------------------------+
| 1. Needs Analysis Report   -> Diagnosis: kesenjangan performa, akar masalah, audiens   |
| 2. INSTRUCTIONAL DESIGN    -> ARSITEKTUR MAKRO: Kontrak strategi, model hybrid,       |
|    DOCUMENT (IDD)             LMS, WCAG, kriteria evaluasi, dan RACI sign-off          |
| 3. ISD Project Plan (WBS)  -> MANAJEMEN PROYEK: Timeline 16-minggu, jadwal review SME  |
| 4. Course Blueprint        -> MATRIKS KURIKULUM: Modul, objektif, aktivitas, asesmen   |
| 5. Storyboard / Script     -> DETAIL MIKRO: Teks per layar, instruksi visual, tombol   |
| 6. Facilitator/Learner Doc -> MATERI DELIVERABLE: Panduan fasilitator, buku peserta     |
| 7. Evaluation Report       -> EVALUASI DAMPAK: Analisis data Kirkpatrick L1 - L4       |
+----------------------------------------------------------------------------------------+
```

---

## 2. Weighted Multi-Dimensional Framework Selection Rubric

Real-world training initiatives rarely fit into neat, mutually exclusive boxes. Instead of rigid categorical assignment (e.g., 'compliance -> Dick & Carey'), evaluate projects across **5 weighted dimensions** to determine the optimal primary and complementary model:

| Dimension | Low (1-2 pts) | Moderate (3-4 pts) | High / Critical (5 pts) | Primary Framework Affinity |
|---|---|---|---|---|
| **1. Stakes & Failure Risk** | Low cost of error (orientation, general awareness) | Measurable operational impact (sales, customer service) | Zero-tolerance / Safety-critical (medical, aviation, compliance legal) | High -> Dick & Carey; Mod -> Action Mapping |
| **2. Skill Complexity** | Declarative / basic recall | Procedural & rule-based tasks | Complex cognitive, heuristics, ill-structured problems | High -> 4C/ID or Cognitive Apprenticeship; Mod -> Merrill |
| **3. Timeline & Delivery Cadence** | Long horizon (>16 weeks), fixed waterfall | Standard quarter (8-12 weeks) | Rapid sprint (<6 weeks), agile prototyping needed | High -> SAM; Low -> ADDIE / Dick & Carey |
| **4. Primary Outcome Goal** | Academic / conceptual understanding | Applied task execution | Measurable on-the-job business behavior change | Behavior -> Action Mapping; Concept -> UbD |
| **5. Governance & Culture** | Autonomous startup / product squads | Balanced enterprise matrix | Heavily regulated audit environment / formal accreditation | Regulated -> ADDIE/Dick & Carey; Agile -> SAM |

### Decision Scoring Output Standard:
When selecting or recommending an ID model, the agent should report:
```
Primary Framework: [Selected Model]
Complementary Framework (if Hybrid): [Second Model]
Confidence Level: [High 85%+ / Moderate 65-80%]
Scoring Rationale: [Breakdown of scores across the 5 dimensions]
User Override: [Notice explaining how the user can customize or re-weight the model]
```

---

## 3. Official Hybrid Framework Architectures

Modern instructional design excels when frameworks are combined strategically:

### Pattern 1: Behavioral Agile (Action Mapping + SAM)
* **Best For**: Corporate performance problems requiring fast, iterative e-learning.
* **Architecture**: Use **Cathy Moore's Action Mapping** to anchor the business goal and identify target behaviors -> Use **Michael Allen's SAM** (Savvy Start, Alpha, Beta) to rapidly prototype and test branching scenarios with SMEs.

### Pattern 2: Technical Rigor & Decision Transfer (Dick & Carey + Action Mapping)
* **Best For**: High-stakes compliance, engineering, or clinical safety where foundation must be rigorous but practice must be realistic.
* **Architecture**: Use **Dick & Carey** for hierarchical task analysis, subordinate skills, and criterion-referenced testing -> Use **Action Mapping** to design realistic decision-tree scenarios with delayed consequences.

### Pattern 3: Academic Enterprise (Backward Design / UbD + ADDIE)
* **Best For**: Multi-campus university programs, accreditation-heavy curricula, or enterprise leadership academies.
* **Architecture**: Use **Wiggins & McTighe's UbD** (Enduring Understandings, Essential Questions, GRASPS tasks) for the pedagogical core -> Use **ADDIE** to manage enterprise resource budgeting, pilot delivery, and Kirkpatrick L3-L4 rollout.

### Pattern 4: Complex Cognitive Systems (4C/ID + SAM)
* **Best For**: Software architecture, cyber incident response, complex technical troubleshooting.
* **Architecture**: Use **van Merrienboer's 4C/ID** to structure Whole Tasks, Supportive Information, and Procedural Aids -> Use **SAM** to iterate through functional lab simulations with engineering leads.

---

## 4. Stakeholder Review & Sign-Off Governance

1. **Lock Learning Objectives First**: Any post-signoff change to objectives triggers a formal Scope Change Request.
2. **3-Day SLA on SME Reviews**: Prevent project stalls by establishing an agreed 72-hour turnaround for feedback.
3. **In-Scope vs. Out-of-Scope Transparency**: Explicitly exclude unbudgeted items (custom video shoots, translations, LMS administration).
