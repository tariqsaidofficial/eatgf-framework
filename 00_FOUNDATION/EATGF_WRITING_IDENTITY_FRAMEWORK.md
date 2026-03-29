# EATGF Writing Identity Framework

## Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field          | Value                                       |
| -------------- | ------------------------------------------- |
| Document Type  | Framework                                   |
| Version        | 1.0                                         |
| Classification | Internal                                    |
| Effective Date | 2026-02-14                                  |
| Authority      | Enterprise Architecture & Governance Office |
| MCM Reference  | EATGF-EDM-GOV-01                            |

---

## 1. Purpose

This document establishes the distinctive writing identity for all Enterprise AI-Aligned Technical Governance Framework (EATGF) documentation. It defines the institutional tone, approved terminology, prohibited phrasing, and signature sentence patterns that constitute the EATGF voice. Compliance with this framework ensures that governance content is consistent, authoritative, and free from ambiguity across all 8 framework layers and 44+ documents.

## 2. Scope

This framework applies to:

- All documents within the EATGF authority repository
- All portal-specific content (homepage, blog, supplementary guides)
- Pull request descriptions and commit messages
- Any public-facing communication that represents the EATGF

This framework does not apply to:

- Code comments in configuration files (TypeScript, CSS, JSON)
- Git log messages from automated tools
- Third-party standard documents referenced by the framework

## 3. Definitions

| Term                | Definition                                                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Writing Identity    | The consistent voice, tone, and linguistic conventions that distinguish EATGF documentation from other governance frameworks |
| Institutional Tone  | Writing that represents the framework authority rather than an individual author                                             |
| Signature Pattern   | A reusable sentence structure that maintains consistency across documents                                                    |
| Prohibited Phrasing | Language constructions that violate EATGF tone standards and shall not appear in framework documents                         |

## 4. Responsibilities

| Role                | Responsibility                                                                         |
| ------------------- | -------------------------------------------------------------------------------------- |
| Document Author     | Applies this writing identity when creating or modifying any EATGF document            |
| Governance Reviewer | Validates writing identity compliance during pull request review                       |
| Framework Owner     | Approves amendments to the governance language dictionary and prohibited phrasing list |

---

## 5. Tone Specification

Every EATGF document shall embody the following 6 mandatory tone attributes:

### 5.1 Institutional

Write as the framework authority, not as an individual contributor. The EATGF speaks as an institution.

| Correct                                         | Incorrect                                         |
| ----------------------------------------------- | ------------------------------------------------- |
| "This framework establishes..."                 | "I have created..."                               |
| "The EATGF mandates..."                         | "We believe that..."                              |
| "This policy applies to..."                     | "Our policy is..."                                |
| "Access control requirements are defined in..." | "We define our access control requirements in..." |

### 5.2 Authoritative

Use declarative, definitive statements. The EATGF does not suggest — it defines, mandates, and establishes.

| Correct                                    | Incorrect                                       |
| ------------------------------------------ | ----------------------------------------------- |
| "This control mandates..."                 | "You should consider..."                        |
| "Organizations shall implement..."         | "It would be a good idea to..."                 |
| "Compliance is required."                  | "Compliance is recommended."                    |
| "This requirement applies to all systems." | "This requirement might apply to some systems." |

### 5.3 Precise

Quantify wherever possible. Avoid vague qualifiers and prefer specific counts, dates, and references.

| Correct                           | Incorrect                              |
| --------------------------------- | -------------------------------------- |
| "35 controls across 7 domains"    | "Many controls across several domains" |
| "ISO/IEC 27001:2022 Clause 6.1.2" | "The relevant ISO clause"              |
| "Review every 12 months"          | "Review regularly"                     |
| "3 governance editions"           | "Multiple editions"                    |

### 5.4 Structured

Organize content using numbered sections, consistent heading hierarchy, and predictable document templates. Avoid freestyle prose.

| Correct                               | Incorrect                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------- |
| Numbered H2 sections: `## 1. Purpose` | Unnumbered sections: `## Purpose` (permitted only in reference documents) |
| Tabular data for comparisons          | Paragraph-form comparisons                                                |
| Bulleted lists for requirements       | Run-on sentences listing requirements                                     |

### 5.5 Neutral

Present governance requirements without advocacy, persuasion, or comparative claims against other frameworks.

| Correct                                                                     | Incorrect                                                                 |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| "This framework defines governance standards for AI-aligned organizations." | "This framework is the most comprehensive governance solution available." |
| "The EATGF provides 35 controls."                                           | "The EATGF provides industry-leading coverage."                           |
| "ISO 42001 alignment is implemented through AIMS."                          | "Our ISO 42001 alignment sets us apart from competitors."                 |

### 5.6 No Exaggeration

Prohibit superlatives, promotional modifiers, and claims that cannot be independently verified.

| Prohibited                                  | Rationale                                                 |
| ------------------------------------------- | --------------------------------------------------------- |
| "Best-in-class"                             | Unverifiable comparative claim                            |
| "World-leading"                             | Unsubstantiated superlative                               |
| "Cutting-edge"                              | Marketing modifier                                        |
| "Revolutionary"                             | Promotional exaggeration                                  |
| "Comprehensive and unmatched"               | Unverifiable absolute claim                               |
| "Enterprise-grade" (as marketing adjective) | Vague qualifier — use specific edition references instead |

---

## 6. Governance Language Dictionary

The following terms are the approved vocabulary for governance concepts within the EATGF. Document authors shall use these terms exclusively and avoid the listed alternatives.

### 6.1 Core Governance Terms

| Approved Term      | Definition                                                                                                         | Prohibited Alternatives                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **Control**        | A governance directive defined in the MCM that mandates specific organizational behavior, measurement, or evidence | Rule, guideline, best practice, recommendation, tip                            |
| **Mandate**        | A requirement that is binding and non-optional within the stated scope                                             | Suggest, recommend, advise, encourage                                          |
| **Framework**      | A structured, layered governance architecture with defined boundaries and traceability                             | Toolkit, solution, platform, product, offering                                 |
| **Authority**      | The governance body or role with decision-making power over a specific domain                                      | Admin, owner (in governance context), manager                                  |
| **Baseline**       | A declared, immutable state of the framework at a specific version                                                 | Starting point, minimum, floor, foundation (as version concept)                |
| **Deviation**      | A formally documented departure from a stated policy or control requirement                                        | Exception, workaround, bypass, exemption                                       |
| **Evidence**       | A governance artifact that demonstrates control implementation or compliance                                       | Proof, documentation (generic), record (generic)                               |
| **Applicability**  | The determination of whether a control applies to a specific organizational context                                | Relevance, pertinence, suitability                                             |
| **Escalation**     | The formal process of elevating a governance matter to a higher authority                                          | Reporting up, raising, flagging, alerting                                      |
| **Non-compliance** | A state in which an organizational practice does not meet a stated control requirement                             | Violation, breach (reserve for security), failure, gap (in compliance context) |

### 6.2 Document Structure Terms

| Approved Term       | Definition                                                                              | Prohibited Alternatives                                                           |
| ------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Section**         | A numbered division of a document at H2 or H3 level                                     | Part, chapter, module, block                                                      |
| **Document Type**   | The classification of a document (Policy, Manual, Procedure, Framework, Record, Report) | File type, template, artifact (generic)                                           |
| **Cross-reference** | A directed link from one document to a specific section of another                      | Link, pointer, redirect, see also (informal)                                      |
| **Supersede**       | To replace a previous version or document with a newer authoritative version            | Override, overwrite, replace (informal), update (as verb for version replacement) |

### 6.3 Control Architecture Terms

| Approved Term         | Definition                                                                              | Prohibited Alternatives                    |
| --------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Control Objective** | The measurable outcome that a control is designed to achieve                            | Goal, target, aim, control purpose         |
| **Control Domain**    | A thematic grouping of related controls within the MCM (e.g., Security, AI, API, Risk)  | Category (in MCM context), area, topic     |
| **Control Owner**     | The role accountable for implementing and maintaining a specific control                | Responsible party, assignee, control admin |
| **Evidence Type**     | The classification of evidence artifacts (Policy, Configuration, Log, Attestation)      | Proof type, document category              |
| **Framework Mapping** | The formal correspondence between an EATGF control and an external standard requirement | Alignment, correspondence, coverage        |
| **Maturity Level**    | A defined stage of governance capability (Level 1–5)                                    | Stage, phase, tier, grade                  |

### 6.4 Audit Terms

| Approved Term         | Definition                                                                          | Prohibited Alternatives                         |
| --------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Finding**           | An auditor's assessment of a control's compliance state                             | Issue, problem, bug, concern                    |
| **Nonconformity**     | A finding that a control requirement is not met (Major or Minor)                    | Failure, violation, deficiency, gap             |
| **Observation**       | A finding that indicates an area for improvement without constituting nonconformity | Note, comment, suggestion, feedback             |
| **Corrective Action** | A documented response to a nonconformity that addresses the root cause              | Fix, remediation (in audit context), resolution |

### 6.5 Version Governance Terms

| Approved Term         | Definition                                                                       | Prohibited Alternatives             |
| --------------------- | -------------------------------------------------------------------------------- | ----------------------------------- |
| **Deprecation**       | The formal marking of a document as superseded, with a defined transition period | Retirement, sunsetting, end-of-life |
| **Archival**          | The permanent transfer of a deprecated document to a read-only historical state  | Deletion, removal, decommissioning  |
| **Version Increment** | A change to the semantic version identifier (Major, Minor, Patch)                | Version bump, update, revision      |
| **Freeze**            | A governance-mandated state preventing changes to a tagged version               | Lock, seal, finalize                |

---

## 7. Prohibited Phrasing List

### 7.1 First-Person Constructions

| Prohibited            | Correction                                            | Rationale                                            |
| --------------------- | ----------------------------------------------------- | ---------------------------------------------------- |
| "We believe..."       | "This framework establishes..."                       | First-person violates institutional tone             |
| "Our framework..."    | "The EATGF..."                                        | Possessive first-person implies individual ownership |
| "We identify..."      | "Risks are identified through..."                     | Use passive or institutional third-person            |
| "We recommend..."     | "This policy mandates..." or "Organizations shall..." | First-person + hedging                               |
| "Our approach..."     | "The EATGF approach..."                               | Possessive first-person                              |
| "We have designed..." | "This framework is designed to..."                    | First-person + past tense narrative                  |

### 7.2 Marketing and Promotional Language

| Prohibited                                        | Correction                                                                                                    | Rationale                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| "Best-in-class"                                   | Remove or replace with specific metric                                                                        | Unverifiable marketing claim  |
| "Cutting-edge"                                    | "Current" or "aligned with [standard version]"                                                                | Vague promotional modifier    |
| "Done! "                                        | "Complete."                                                                                                   | Casual celebration marker     |
| "Out of the box"                                  | "In the default configuration"                                                                                | Informal idiom                |
| "Professional governance standards that scale..." | "This framework defines governance standards for organizations at three maturity levels."                     | Tagline/marketing phrasing    |
| "Buildable. Testable. Audit-Defensible."          | Remove — document title and purpose section convey this                                                       | Marketing tagline             |
| "Data is a strategic asset"                       | "Data governance ensures classification, protection, and lifecycle management of organizational data assets." | Strategic marketing assertion |

### 7.3 Casual and Informal Language

| Prohibited                                    | Correction                                                                     | Rationale                              |
| --------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------- |
| "Nobody reads"                                | Remove or rephrase: "Policy documents shall be concise and actionable."        | Informal, dismissive                   |
| "Avoid lengthy 50-page policies nobody reads" | "Policy documents shall not exceed the scope required for governance clarity." | Casual directive with informal example |
| "Easy to use"                                 | "Structured for implementation efficiency"                                     | Marketing simplification               |
| "You should..."                               | "Organizations shall..." or use imperative                                     | Second-person informal directive       |
| "Just do X"                                   | "Execute X per [procedure reference]."                                         | Casual imperative                      |
| "Basically..."                                | Remove                                                                         | Filler word                            |
| "In a nutshell..."                            | "In summary:"                                                                  | Informal idiom                         |

### 7.4 Hedging and Weak Modifiers

| Prohibited               | Correction                                                     | Rationale             |
| ------------------------ | -------------------------------------------------------------- | --------------------- |
| "Might want to..."       | "Shall..." or "Organizations are required to..."               | Non-committal         |
| "Could potentially..."   | "May, subject to [condition]..."                               | Excessive hedging     |
| "It's a good idea to..." | "This control requires..."                                     | Subjective evaluation |
| "Probably..."            | State definitively or quantify probability with risk framework | Vague uncertainty     |
| "Various"                | Enumerate the items or provide a count                         | Imprecise             |
| "Some"                   | Specify quantity or scope                                      | Imprecise             |
| "Several"                | Provide a count                                                | Imprecise             |

### 7.5 Decorative Elements

| Prohibited                         | Context                                        | Rationale                                     |
| ---------------------------------- | ---------------------------------------------- | --------------------------------------------- |
| Emoji in H1/H2/H3 headings         | All non-archived documents                     | Violates heading hierarchy discipline         |
| Exclamation marks                  | Formal documents (policies, controls, manuals) | Inappropriate emphasis for governance content |
| Badges (shields.io or similar)     | Framework documents                            | Marketing presentation element                |
| ASCII art or decorative separators | All documents                                  | Non-standard formatting                       |

---

## 8. Signature Sentence Patterns

The following patterns shall be used as templates when constructing governance statements. Document authors shall adapt these patterns to their specific context while preserving the structural intent.

### 8.1 Document Opening Patterns

| Pattern                                                                  | Usage                                        |
| ------------------------------------------------------------------------ | -------------------------------------------- |
| "This document establishes [scope] for [domain] within the EATGF."       | Primary opening for all document types       |
| "This [document type] defines the [subject] applicable to [scope]."      | Alternative opening specifying document type |
| "This document supersedes [previous version/document] effective [date]." | Opening for replacement documents            |

**Examples:**

- "This document establishes the Git repository governance policy for the EATGF."
- "This policy defines the version increment model applicable to all framework content."
- "This document supersedes the Governance Charter v1 effective 2026-02-14."

### 8.2 Control Statement Patterns

| Pattern                                                                                  | Usage                                           |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------- |
| "This control mandates [requirement] as defined in MCM reference [EATGF-XXX-YYY-NNN]."   | Stating a control requirement with traceability |
| "Control [ID] requires [measurable outcome] with evidence provided via [evidence type]." | Specifying control objective and evidence       |
| "[Domain] controls are governed by [authority] per MCM Section [reference]."             | Establishing domain authority                   |

**Examples:**

- "This control mandates role-based access control for all governance artifacts as defined in MCM reference EATGF-DSS-SEC-01."
- "Control EATGF-AI-RISK-01 requires documented bias assessment with evidence provided via attestation record."
- "API security controls are governed by the API Governance Framework per MCM Section 5."

### 8.3 Deviation and Enforcement Patterns

| Pattern                                                                                                  | Usage                     |
| -------------------------------------------------------------------------------------------------------- | ------------------------- |
| "Deviation from this [policy/control/requirement] requires written approval from [authority]."           | Standard deviation clause |
| "Non-compliance with this [policy/control] shall be escalated to [authority] per [procedure reference]." | Enforcement escalation    |
| "Unauthorized modification of [artifact] constitutes a policy violation subject to [consequence]."       | Violation consequence     |

**Examples:**

- "Deviation from this access control policy requires written approval from the Chief Information Security Officer."
- "Non-compliance with the version tagging convention shall be escalated to the Framework Owner per the Git Governance Policy Section 13."
- "Unauthorized modification of a frozen baseline constitutes a policy violation subject to formal incident documentation."

### 8.4 Scope and Boundary Patterns

| Pattern                                                                                          | Usage                        |
| ------------------------------------------------------------------------------------------------ | ---------------------------- |
| "This [document type] applies to [scope]. Items outside this scope are governed by [reference]." | Defining boundaries          |
| "The scope of this [policy/control] encompasses [inclusion] and excludes [exclusion]."           | Inclusion/exclusion boundary |
| "This document does not govern [out-of-scope item], which is addressed in [reference]."          | Explicit exclusion           |

**Examples:**

- "This policy applies to all contributors with write access to the authority repository. Items outside this scope are governed by the organization's general IT policy."
- "The scope of this control encompasses all AI model deployments and excludes internal research experiments."
- "This document does not govern portal application dependencies, which are addressed in the portal maintainer's operational procedures."

### 8.5 Cross-Reference Patterns

| Pattern                                                                                    | Usage                     |
| ------------------------------------------------------------------------------------------ | ------------------------- |
| "This requirement aligns with [ISO standard] Clause [X.Y] and maps to COBIT [process ID]." | External standard mapping |
| "Refer to [document name] Section [N] for [specific guidance]."                            | Internal cross-reference  |
| "As established in [document name], [restated requirement]."                               | Inherited requirement     |

**Examples:**

- "This requirement aligns with ISO/IEC 27001:2022 Clause 6.1.2 and maps to COBIT 2019 APO12."
- "Refer to the Version Governance Policy Section 7 for control modification impact scoring criteria."
- "As established in the Baseline Declaration, tagged versions are permanently immutable."

### 8.6 Version and Status Patterns

| Pattern                                                                                | Usage               |
| -------------------------------------------------------------------------------------- | ------------------- |
| "This document is effective as of [date] and supersedes all prior versions."           | Version effectivity |
| "This [document/version] is classified as [DRAFT / APPROVED / DEPRECATED / ARCHIVED]." | Status declaration  |
| "Changes to this document require [approval process] per [policy reference]."          | Change authority    |

**Examples:**

- "This document is effective as of 2026-02-14 and supersedes all prior versions."
- "This document is classified as APPROVED."
- "Changes to this document require Framework Owner approval per the Git Governance Policy Section 7.2."

---

## 9. Remediation Queue — Current Writing Identity Violations

The following violations were identified during the documentation style audit and require correction per this framework:

| Document                                       | Violation                         | Current Text                                  | Required Correction                                                                                           |
| ---------------------------------------------- | --------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| RISK_FRAMEWORK.md                              | First-person plural (Section 7.1) | "how **we** identify"                         | "how risks are identified"                                                                                    |
| GOVERNANCE_FRAMEWORK_README.md                 | Marketing tone (throughout)       | Badges, , FAQ format, tagline         | Full rewrite: remove badges, emoji, FAQ format, marketing tagline; apply EATGF header and institutional tone  |
| GOVERNANCE_BY_TEAM_SIZE.md                     | Casual language                   | "Avoid lengthy 50-page policies nobody reads" | "Policy documents shall not exceed the scope required for governance clarity."                                |
| EVIDENCE_REGISTER_EXCEL_BUILD_SPECIFICATION.md | Marketing tagline                 | "Buildable. Testable. Audit-Defensible."      | Remove tagline; purpose is conveyed by Section 1                                                              |
| 03_DATA_GOVERNANCE_POLICY.md                   | Strategic marketing               | "Data is a strategic asset"                   | "Data governance ensures classification, protection, and lifecycle management of organizational data assets." |
| GOVERNANCE_FRAMEWORK_README.md                 | Placeholder email                 | `governance@enterprise.com`                   | `[designated-contact]@[organization-domain]`                                                                  |
| FRAMEWORK_MAPPINGS.md                          | Placeholder email                 | `governance@enterprise.com`                   | `[designated-contact]@[organization-domain]`                                                                  |
| 01_GOVERNANCE_CHARTER.md                       | Placeholder email                 | `governance@enterprise.com`                   | `[designated-contact]@[organization-domain]`                                                                  |
| 02_INFORMATION_SECURITY_POLICY.md              | Placeholder email                 | `security@enterprise.com`                     | `[designated-contact]@[organization-domain]`                                                                  |
| 03_DATA_GOVERNANCE_POLICY.md                   | Placeholder email                 | `data-governance@enterprise.com`              | `[designated-contact]@[organization-domain]`                                                                  |

---

## 10. Governance Enforcement Rules

1. All documents merged into the EATGF authority repository shall comply with the tone specification in Section 5.
2. Pull requests containing prohibited phrasing (Section 7) shall be returned for correction prior to approval.
3. The governance language dictionary (Section 6) is the authoritative terminology source. Prohibited alternatives shall not appear in new or updated documents.
4. Signature sentence patterns (Section 8) are recommended templates. While exact wording may be adapted, the structural intent (declarative, institutional, precise) shall be preserved.
5. Writing identity violations identified in the remediation queue (Section 9) shall be corrected as part of the scheduled document update cycle.
6. Amendments to the governance language dictionary require Framework Owner approval and shall be documented in the Version & Status Block.

---

**Document Control**

| Version | Date       | Author                                      | Change Description                 |
| ------- | ---------- | ------------------------------------------- | ---------------------------------- |
| 1.0     | 2026-02-14 | Enterprise Architecture & Governance Office | Initial writing identity framework |

**Authority Sign-Off**

| Role                     | Name | Date | Signature |
| ------------------------ | ---- | ---- | --------- |
| Framework Owner          |      |      |           |
| Chief Governance Officer |      |      |           |
