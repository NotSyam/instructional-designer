# Visual Cognition & Slide Design Guide (Dual Coding & Zero-Bullet-Point Standard)

This reference operationalizes cognitive science principles—primarily **Richard Mayer's Cognitive Theory of Multimedia Learning (CTML)**, **Allan Paivio's Dual Coding Theory**, and **John Sweller's Cognitive Load Theory (CLT)**—specifically for the design of presentation slide decks, visual lectures, and HTML slides (adapted from *visual-cognition-slides*, 2024).

---

## 1. The Core Philosophy: Dual Coding Over Text Dumps

### 1.1 The Golden Rule of Visual Slides
> **Visuals must carry independent semantic weight.** If you remove all the words from the slide, the audience should still comprehend the core conceptual relationship or sequence. Text acts as an **anchor or label**, not as a transcript of the speaker's script.

### 1.2 The Zero-Bullet-Point Law
Bullet points violate the **Redundancy Principle** and cause the **Split-Attention Effect**:
* When a slide displays a bulleted paragraph while the speaker talks, the learner's phonological loop in working memory is overloaded (trying to read and listen to competing verbal streams simultaneously).
* **Mandatory Rule**: Never generate a raw bulleted list (`- item 1`, `- item 2`, `- item 3`) on presentation slides. Every collection of ideas must be transformed into a **spatial visual structure** (Cards, Flows, Comparison Columns, Matrices, or Analogies).

---

## 2. Richard Mayer's 12 Multimedia Principles for Slide Decks

| Principle | Meaning in Cognitive Science | Operational Rule in Slide Design |
|---|---|---|
| **1. Coherence** | People learn better when extraneous material is excluded. | Strip away decorative clip-art, meaningless corporate stock photos, and animated transition fluff. |
| **2. Signaling** | Highlighting essential material guides attention. | Use visual accents (contrast color, subtle glow, zoom scale) to highlight the focal concept; mute background elements. |
| **3. Redundancy** | On-screen text identical to spoken narration impairs learning. | Slides should show visuals + keywords/labels; never put the full verbatim voiceover text on screen. |
| **4. Spatial Contiguity** | Words and corresponding visuals must be placed near each other. | Place labels and arrows **inside** the diagram or directly adjacent to the component, never in an isolated legend box. |
| **5. Temporal Contiguity** | Corresponding narration and graphics should occur simultaneously. | Reveal visual elements and annotations in sync with the spoken explanation using step reveals (`[data-step]`). |
| **6. Segmenting** | Pacing controlled by learner improves assimilation. | Break complex multi-part concepts across sequential slides or controlled step clicks rather than 1 crowded slide. |
| **7. Pre-training** | Learning is deeper when key names and concepts are known in advance. | Include a clear conceptual hook or definition unpacking slide before diving into complex operational steps. |
| **8. Modality** | Graphics + spoken narration > Graphics + printed text blocks. | Keep slide text minimal (keywords only) when a presenter is speaking. Reserve text-heavy formats for standalone reference decks. |
| **9. Multimedia** | Words + pictures > Words alone. | Always pair abstract concepts with concrete visual representations (graphs, diagrams, spatial layouts). |
| **10. Personalization** | Conversational style fosters deeper engagement than formal tone. | Use direct, active, second-person voice (*"You examine the client's telemetry"*, not *"The participant will observe..."*). |
| **11. Voice** | Human, friendly voice enhances cognitive processing. | Voiceover script and slide captions must feel authentic, clear, and empathetic. |
| **12. Image** | Static photo of the speaker's talking head does not improve learning. | Maximize screen real estate for the conceptual graphic rather than a large speaker video frame. |

---

## 3. The 8 Narrative Structures (Slide Deck Architectures)

Select the narrative structure matching the project's communicative goal:

| Structure | Best For | Core Narrative Logic | Hook Formula (Slide 1) |
|---|---|---|---|
| **1. Contrastive** | Correcting common misconceptions | "You thought X → Actually Y" | *"You thought [X], but the data reveals [Y]"* |
| **2. Problem-Solution** | Teaching a new concept/framework | Why → Because → Therefore | *"Why does [Problem X] keep happening? The answer is counterintuitive"* |
| **3. Progressive Unpacking** | Deepening a multi-layered complex topic | Surface → Root Cause → Strategic Implication | *"Behind [Symptom X] lies a much larger systemic force"* |
| **4. Identity & Empowerment** | Leadership, change management, motivation | You have this challenge → Here is your leverage | *"You are better positioned to solve [X] than you think"* |
| **5. Story / Case Study** | Incident review, real-world narrative | Context → Conflict → Climax → Epiphany | *"On October 14th, a simple typo took down 40% of the network"* |
| **6. Modular Framework** | Teaching a structured methodology | N components → How each works → Synergy | *"Deconstructing [Complex System]: Only 3 moving parts"* |
| **7. A vs. B Comparison** | Technology selection, paradigm shifts | Structural side-by-side evaluation | *"[Approach A] vs [Approach B]: Which one actually scales?"* |
| **8. Chronological Timeline** | Historical evolution, roadmaps, future trends | Past → Present → Future trajectory | *"10 years ago, nobody predicted [X] would become standard"* |

---

## 4. Visual Translation for the 6 Knowledge Types

When translating training material into slides, identify the knowledge category and apply the corresponding spatial pattern:

### 4.1 Conceptual Knowledge ("What is X?")
* **Spatial Patterns**:
  * **Analogical Mapping**: Familiar real-world object on the left, new technical concept on the right, connecting arrows mapping isomorphic functions (e.g., *API = Restaurant Waiter*).
  * **Definition Unpacking**: Target term in large display font, with 2–3 core operational attributes highlighted as distinct badge cards.
  * **Positive vs. Negative Examples**: Side-by-side card comparison contrasting what falls inside the definition vs. near-miss edge cases.
* **Anti-Pattern**: Pasting a dictionary or Wikipedia definition without concrete visual anchors.

### 4.2 Procedural Knowledge ("How to execute X?")
* **Spatial Patterns**:
  * **Horizontal/Vertical Step Progression**: Numbered node sequence (`1 → 2 → 3`) with previous steps remaining visually subdued and the active step highlighted.
  * **Decision Tree / Branching Flow**: Decision diamond (`Condition?`) splitting into green (Success Path) and red/amber (Remediation Path).
  * **Mistake → Correction Pair**: Showing the authentic workplace mistake first (crossed out with red tag), followed by the validated standard procedure.
* **Anti-Pattern**: Putting 7 numbered text paragraphs on a single slide without spatial flow indicators.

### 4.3 Narrative & Case Study Knowledge
* **Spatial Patterns**:
  * **Scene Layout**: Authentic workplace background photo/illustration with speech callouts representing dialogue.
  * **Emotional Arc Curve**: Line graph charting tension/risk vs. timeline across the critical decision points of the case.
  * **"Turning Point" Freeze Frame**: Full-bleed slide with a high-contrast headline capturing the pivotal crisis moment.

### 4.4 Relational & Structural Knowledge ("How does X connect to Y?")
* **Spatial Patterns**:
  * **2×2 Matrix**: Two orthogonal axes defining 4 operational quadrants with distinct strategic implications.
  * **Venn Diagram**: Overlapping geometric zones visually representing synergies, intersections, or distinct jurisdictions.
  * **Causal Domino Chain**: Stepwise progression showing how an action at Node A triggers cascading consequences at Nodes B and C.

### 4.5 Metacognitive Knowledge ("How to think through X?")
* **Spatial Patterns**:
  * **Mental Model Contrast**: Old mental model (linear, brittle) on the left vs. New mental model (iterative, resilient) on the right.
  * **Visible Thinking Process**: Thought bubble callouts depicting internal diagnostic questions an expert asks themselves.
  * **Interactive Prediction Slide**: Presenting a scenario and prompting learners to commit to a prediction before revealing the outcome.

### 4.6 Quantitative & Data Knowledge ("Magnitude, Proportion & Trends")
* **Spatial Patterns**:
  * **Benchmark Scaled Comparison**: Converting an astronomical or micro number into a visceral physical equivalent (*"Equivalent to 1 drop of water in an Olympic swimming pool"*).
  * **Proportion Area Grid**: 100-cell waffle chart or pie segment visually proving ratios rather than raw percentages.
  * **Dynamic Trendline**: Simplified curve with clear peak, valley, and inflection callouts.

---

## 5. The 8 Visual Layout Alternatives to Bullet Points

Whenever tempted to write a bulleted list, substitute one of these 8 standard visual containers:

1. **Split-Column Comparison**: 2 contrasting cards (50/50 split) comparing *Before vs After*, *Problem vs Solution*, or *Traditional vs Modern*.
2. **3-Card Horizontal Grid**: 3 balanced cards (33% each) displaying *Key Pillars*, *Operational Phases*, or *Primary Benefits*.
3. **Linear Step Flow**: Numbered cards connected by directional chevron arrows (`Step 01` → `Step 02` → `Step 03`).
4. **2×2 Quadrant Matrix**: 4 distinct quadrants categorizing items by High/Low Impact vs High/Low Effort.
5. **Hero Callout Stat**: Massive display number (`84%`, `3.5×`, `$1.2M`) with a 1-sentence explanatory insight below.
6. **Timeline Milestone Spine**: A central horizontal or vertical axis connecting timestamped event cards.
7. **Hub & Spoke / Central Core**: Central core concept encircled by 3–5 radial satellite nodes.
8. **Dilemma Choice Architecture**: Two competing options with their immediate trade-offs detailed in side-by-side decision cards.

---

## 6. Slide Aspect Ratios & Technical Specs

| Aspect Ratio | Canvas Resolution | Target Use Case | Typography Multiplier |
|---|---|---|---|
| **16:9 Standard** | 1920×1080 px | Projectors, Zoom/Meet VILT, Video recording, Widescreen LMS | 1.0× (Baseline) |
| **16:9 Web Lightweight** | 1280×720 px | Lightweight web embeds, email sharing, mobile landscape | 0.75× |
| **9:16 Vertical Mobile** | 1080×1920 px | Smartphone microlearning, Reels/TikTok, WhatsApp sharing | 1.2× (Larger text, stacked layout) |
| **4:5 Tablet / Social** | 1080×1350 px | Social learning feeds, iPad vertical, carousel posts | 1.1× |
| **1:1 Square** | 1080×1080 px | Instagram carousel slides, square LMS widgets | 1.0× |

### 6.1 Viewport Scaling Engine (Pure JS)
HTML slides should implement responsive letterboxing so they display identically on all screens without layout breakage:
```javascript
function scaleDeck() {
  const deck = document.getElementById('deck');
  const targetW = 1920, targetH = 1080;
  const scale = Math.min(window.innerWidth / targetW, window.innerHeight / targetH);
  const left = (window.innerWidth - targetW * scale) / 2;
  const top = (window.innerHeight - targetH * scale) / 2;
  deck.style.transform = `scale(${scale})`;
  deck.style.left = `${left}px`;
  deck.style.top = `${top}px`;
}
window.addEventListener('resize', scaleDeck);
window.addEventListener('DOMContentLoaded', scaleDeck);
```
