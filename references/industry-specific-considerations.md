# Industry-Specific Instructional Design Considerations & Regulatory Nuances

> **Source Methodology**: Trina Rimmer (*id-skills-for-claude*, 2024), *Industry-Specific Design Considerations*  
> **Purpose**: Provide instructional designers with domain-specific regulatory constraints, terminology pitfalls, and LLM failure modes across 5 major enterprise verticals.

---

## 1. Healthcare & Clinical Practice

* **Core Mandate**: Patient safety, clinical judgment, evidence-based guidelines, and regulatory compliance (HIPAA, JCAHO, FDA).
* **High-Risk LLM Failure Modes**:
  * Hallucinating clinical dosages or omitting critical contraindications.
  * Over-simplifying diagnostic complexity into superficial multiple-choice items.
  * Assuming nurse practitioners or physicians have hours of desk time (they are shift workers on their feet).
* **Design Heuristics**:
  * Prioritize microlearning bites (3–5 min) accessible via mobile or workstation COW (computer on wheels).
  * Use branching clinical case vignettes with subtle early warning signs (e.g. sepsis progression).
  * Require 100% formal sign-off from a credentialed Medical Director / Clinical SME before any pilot testing.

---

## 2. Financial Services, Banking, & Fintech

* **Core Mandate**: Fiduciary duty, risk mitigation, fraud detection, and strict statutory compliance (SEC, FINRA, AML/BSA, SOX, GDPR).
* **High-Risk LLM Failure Modes**:
  * Using generic ethical platitudes rather than specific statutory triggers (e.g. confusion between "royalty" vs. "commission", or vague definitions of "insider trading").
  * Presenting clear-cut good vs. evil scenarios rather than realistic pressure-filled gray zones (e.g., meeting quarterly sales quotas vs. suitability rules).
* **Design Heuristics**:
  * Emphasize realistic dilemma cards where client interests collide with short-term revenue incentives.
  * Frame compliance not as a punitive audit chore, but as safeguarding client trust and corporate license to operate.
  * Maintain strict audit trails and immutable SCORM/xAPI record-keeping for legal defensibility.

---

## 3. Manufacturing, Energy, & Industrial Safety (K3 / OSHA)

* **Core Mandate**: Life-safety, physical hazard containment, zero-tolerance OSHA compliance, and equipment operational integrity (Lockout/Tagout - LOTO, PPE, Hazmat).
* **High-Risk LLM Failure Modes**:
  * Substituting physical motor practice with passive video watching.
  * Omitting critical physical verification steps (e.g., verifying zero energy state before servicing machinery).
  * Tone that sounds academic or disconnected from shop-floor culture.
* **Design Heuristics**:
  * Design training as a blended hybrid: digital visual procedures + mandatory supervised hands-on physical verification check.
  * Use high-contrast visual diagrams and animations showing internal mechanical hazards (e.g., pinch points, electrical arc flash).
  * Provide laminated, ruggedized physical Job Aids and QR-code-accessible troubleshooting wizards at the machine terminal.

---

## 4. Government & Public Sector (ASN / Civil Service)

* **Core Mandate**: Public trust, statutory accountability, transparency, anti-corruption, and the Plain Writing Act.
* **High-Risk LLM Failure Modes**:
  * Writing dense, bureaucratic legal jargon that alienates junior civil servants.
  * Creating generic corporate scenarios that ignore civil service employment protections and public sector hierarchy.
* **Design Heuristics**:
  * Adhere strictly to Plain Language standards (8th-grade reading level, active voice, short sentences).
  * Incorporate realistic scenarios on public procurement ethics, conflict of interest disclosures, and citizen data handling.
  * Ensure 100% WCAG 2.2 AA accessibility compliance as legally mandated for public sector software.

---

## 5. Higher Education & Academic Learning

* **Core Mandate**: Deep conceptual transfer, critical thinking, academic rigor, peer collaboration, and metacognition.
* **High-Risk LLM Failure Modes**:
  * Treating university students like corporate employees (focusing solely on quick workplace procedures rather than conceptual depth).
  * Writing exams that test rote memorization of definitions rather than synthesizing divergent arguments.
* **Design Heuristics**:
  * Apply Understanding by Design (UbD): Essential Questions and authentic assessments (GRASPS).
  * Design peer review clinics and seminar discussions using Zahorik's Invention or Extension sequencing models.
