# E-Learning & Media Storyboard Template

## [Module / Unit Title]: [Module Name]
> **Project / Course Name**: [Project Name]  
> **Target Delivery Tool**: [Articulate Storyline 360 / Rise / Camtasia / Custom HTML5 / LMS Video]  
> **Estimated Seat Time**: [e.g., 15 minutes]  
> **Target Audience**: [Learner Profile]  
> **Lead Instructional Designer**: [Name] | **SME Reviewer**: [Name]  
> **Version**: [1.0] | **Date**: [YYYY-MM-DD]

---

## 1. Module Overview & Learning Objective Alignment

| Screen Range | Topic / Section | Aligned Bloom's Objective | Interaction Type |
|---|---|---|---|
| **SC-01 - SC-03** | Hook & Contextual Problem | Recall prior challenge | Video / Animated Scenario |
| **SC-04 - SC-07** | Guided Procedure (Worked Example) | Apply step-by-step task | Click-and-Reveal / Tabs |
| **SC-08 - SC-11** | Branching Decision Practice | Evaluate realistic dilemmas | Multi-path Branching Simulation |
| **SC-12 - SC-14** | Summary & Retrieval Check | Analyze retention & transfer | Interactive Knowledge Check |

---

## 2. Screen-by-Screen Storyboard Specifications

### Screen ID: SC-01 (Title & Hook Screen)
* **Screen Title**: Operational Crisis: The Midnight Anomaly
* **Screen Type**: Opening Video / Ambient Animation
* **Navigation**: User must watch opening sequence; Next button enabled upon completion.

| Storyboard Component | Specification & Content |
|---|---|
| **Visual Assets & Layout** | • Split screen layout.<br>• Left: 2D flat illustration of a server dashboard with red flashing alert icons (`alert_server.svg`).<br>• Right: Character illustration of Lead Engineer 'Maya' looking concerned at laptop.<br>• High-contrast corporate palette (Navy #0A192F, Danger Red #E63946). |
| **On-Screen Text (OST)** | **Title**: Incident Response: Resolving Level-1 System Outages<br>**Subtitle**: Module 2: Rapid Fault Isolation<br>*Button*: [Start Mission] |
| **Audio / Voiceover Script (VO)** | *"It's 02:15 AM. The primary payment gateway suddenly drops 40% of incoming transactions. An alert escalates to your terminal. In the next 15 minutes, your diagnostic decisions will determine whether the system recovers or suffers total downtime. Let's begin."* |
| **Developer / Interaction Notes** | • Autoplay voiceover on slide load.<br>• Synchronize flashing alert pulse with VO line: *"drops 40% of incoming transactions"* at 00:04.<br>• Clicking [Start Mission] plays transition sound (`btn_click.mp3`) and jumps to slide SC-02. |
| **Accessibility (WCAG 2.2 AA)** | • Closed captions (CC) file: `cc_sc01.vtt`.<br>• Alt-text for image: *"Illustration of system dashboard displaying urgent red error notifications."*<br>• Full keyboard tab navigation enabled across interactive controls. |

---

### Screen ID: SC-08 (Branching Decision Dilemma)
* **Screen Title**: Critical Decision Point: Diagnosing Memory Saturation
* **Screen Type**: Interactive Branching Simulation (Action Mapping / 4C/ID Part-Task)
* **Branching Rule**: 3 choices with immediate natural consequence feedback layers.

| Storyboard Component | Specification & Content |
|---|---|
| **Visual Assets & Layout** | • Background: Terminal command line interface with simulated live output log.<br>• Top banner: Scenario context prompt box.<br>• Bottom: 3 distinct decision action cards (Cards A, B, C) styled as clickable button blocks. |
| **On-Screen Text (OST)** | **Scenario Prompt**: Server telemetry indicates RAM saturation at 98%. Thread count is spiking.<br>**What is your first diagnostic action?**<br><br>• **Option A**: Trigger an emergency cluster restart immediately.<br>• **Option B**: Run thread-dump analysis (`jstack -l`) and capture heap histogram before taking any action.<br>• **Option C**: Double the cloud container memory quota in Kubernetes without investigating root cause. |
| **Audio / Voiceover Script (VO)** | *"Look at the terminal metrics. RAM is at 98% and climbing. What is your immediate diagnostic step? Select the best option below to proceed."* |
| **Branching & Developer Notes** | • **If Option A selected** -> Jump to Feedback Layer **SC-08A (Sub-optimal)**: Server reboots, but memory leak reoccurs 10 minutes later and transaction logs are lost. Learner loses 10 operational stability points.<br>• **If Option B selected** -> Jump to Feedback Layer **SC-08B (Optimal)**: Thread dump isolates memory leak in connection pool; issue safely neutralized. Learner advances to SC-09.<br>• **If Option C selected** -> Jump to Feedback Layer **SC-08C (Ineffective)**: Memory cost doubles but leak consumes extra RAM in 5 minutes. |
| **Accessibility (WCAG 2.2 AA)** | • Screen reader announces option count: *"Question 1 of 3, 3 options available."*<br>• Focus rectangle visible on selected card (`outline: 3px solid #005fcc`). |

---

## 3. Definition of Done (DoD) for Storyboard Production
- [ ] **SME Technical Review**: All terminal commands, error codes, and technical jargon verified 100% accurate.
- [ ] **Voiceover Word Count**: Audio scripts timed at ~130–150 words per minute.
- [ ] **Asset List Generated**: Graphic design, video clip, and audio SFX asset IDs compiled into production tracker.
- [ ] **Accessibility Completed**: Closed captions written, alt text assigned, keyboard tabbing order tested.
- [ ] **LMS Interaction Verified**: SCORM/xAPI trigger points documented for LMS reporting.
