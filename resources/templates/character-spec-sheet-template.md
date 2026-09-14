# Character Specification Sheet Template (E-Learning & Scenario Cast)

> **Source Methodology**: Trina Rimmer (*id-skills-for-claude*, 2024), *Character Design for E-Learning*  
> **Purpose**: Establish visual consistency, emotional authenticity, and inclusive representation for scenario characters across multiple screens and AI image generations.

---

## 1. Character Identity & Instructional Profile

* **Character Name**: [e.g. Maya Chen]
* **Role / Job Title**: [e.g. Senior Network Operations Engineer]
* **Tenure / Experience Level**: [e.g. 6 years at the company, highly competent but balancing high ticket volume]
* **Instructional Purpose**: [e.g. Models expert troubleshooting and critical communication under time pressure]
* **Tone & Persona**: [e.g. Pragmatic, focused, approachable, calm during outages]

---

## 2. Visual Style & Aesthetic Grounding

| Dimension | Specification |
|---|---|
| **Visual Style** | **[Flat Vector / Photorealistic / Hand-Drawn / Comic Book / 3D Stylized]** |
| **Reference System** | [e.g., Pablo Stanley Humaaans / Clean Corporate Vector / Studio Portrait / Open Peeps] |
| **Color Palette** | • Primary: `[#Hex]` (Workplace attire)<br>• Secondary: `[#Hex]` (Brand accent)<br>• Background: `[#Hex]` (Neutral office context) |
| **Workplace Attire** | [e.g. Charcoal smart-casual collared shirt, company lanyard, rolled sleeves — authentic to the actual job] |

---

## 3. Physical Attributes & Authentic Diversity

* **Apparent Age**: [e.g. Early 30s]
* **Ethnicity / Cultural Context**: [e.g. East Asian heritage]
* **Hair & Grooming**: [e.g. Shoulder-length dark straight hair tied in a practical low ponytail]
* **Distinctive Features**: [e.g. Wireframe reading glasses, subtle wristwatch]
* **Adaptive / Assistive Devices** (if applicable): [e.g. Ergonomic headset / None]

---

## 4. Emotional States & Pose Matrix (The 5 Core Poses)

To maintain narrative immersion, characters must exhibit distinct emotional reactions aligned with learner decisions:

| State | Scenario Context | Facial Expression & Body Language | On-Screen Asset ID |
|---|---|---|---|
| **1. Neutral / Listening** | Screen load, introducing context, reading system logs. | Direct gaze, relaxed shoulders, neutral mouth, attentive posture. | `char_maya_01_neutral.png` |
| **2. Thoughtful / Deliberating** | Weighing two viable technical solutions or diagnosing telemetry. | Chin resting on hand, slight brow furrow, looking slightly off-camera. | `char_maya_02_thinking.png` |
| **3. Stressed / Conflicted** | High-pressure dilemma, critical system alert, sub-optimal outcome. | Tense shoulders, widened eyes, hand on temple, urgent posture. | `char_maya_03_stressed.png` |
| **4. Relieved / Confident** | Correct decision made, root cause identified, system stabilized. | Warm open smile, relaxed posture, slight nod of approval. | `char_maya_04_success.png` |
| **5. Engaged / Guiding** | Offering a coaching tip, debriefing consequence, explaining rationale. | Leaning forward slightly, one hand gesturing toward content, warm focus. | `char_maya_05_guide.png` |

---

## 5. AI Image Generation & Reference Image Anchor Formula

To ensure Midjourney, DALL-E 3, or Imagen generates consistent facial features across all 5 poses, use the **Anchor Prompt Technique**:

### 5.1 Base Anchor Prompt (Master Image)
```text
[Visual Style]: Flat vector illustration in the style of Humaaans by Pablo Stanley, clean outlines, solid colors.
[Subject]: A 32-year-old East Asian female network engineer named Maya, shoulder-length straight black hair in a low ponytail, wireframe glasses, wearing charcoal button-up work shirt with teal company lanyard.
[Pose]: Frontal bust shot, neutral friendly expression, looking at camera.
[Environment]: Clean isolated solid light gray background (#F3F4F6), corporate SaaS aesthetic, no extra clutter, high resolution --no 3d, realistic shading, gradients, photorealism
```

### 5.2 State Variation Formula (Using Master as Image Reference)
```text
[Reference Image URL / ID] + [Base Subject Description] + [Target Emotional State & Hand Pose] + [Consistent Lighting & Background]
Example (Pose 3 - Stressed):
[Image Anchor] Maya, 32-year-old East Asian female engineer, wireframe glasses, ponytail, charcoal shirt. Showing stressed, concerned expression, hand rubbing temple, looking worried at server alert, solid gray background.
```

---

## 6. Definition of Done (DoD) for Character Assets
- [ ] **Role Realism**: Character clothing, tools, and background match actual job conditions (verified by SME).
- [ ] **Facial Consistency**: Features, hair color, and glasses remain identical across all 5 emotional poses.
- [ ] **Accessibility Compliance**: All character images have descriptive WCAG alt-text indicating emotion and context (e.g., *"Maya looking concerned at system alert"*).
- [ ] **Cast Diversity Balanced**: Cast representation reflects authentic workforce distribution without falling into tokenism.
