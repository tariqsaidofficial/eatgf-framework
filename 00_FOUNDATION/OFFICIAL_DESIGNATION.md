# Official Designation

| Field | Value |
|-------|-------|
| Document Type | Authority Framework |
| Version | 1.0 |
| Classification | Controlled |
| Effective Date | 2026-02-13 |
| Authority | Framework Authority - Tariq Said Official |
| EATGF Layer | 00_FOUNDATION |

---

## Purpose

This document establishes the official legal designation, naming conventions, version control standards, and repository authority for the Enterprise AI-Aligned Technical Governance Framework (EATGF). It serves as the authoritative reference for all naming, versioning, and repository management decisions.

## Architectural Position

This specification operates within **00_FOUNDATION** of EATGF as the definitive authority on framework identity and naming.

- **Upstream requirement:** None (foundational)
- **Downstream enforcement:** All documents, repositories, and communications must comply
- **Cross-layer reference:** Referenced by all 01-07 layers for naming enforcement

## Governance Principles

1. **Single Authoritative Name** – One official framework designation: Enterprise AI-Aligned Technical Governance Framework (EATGF)
2. **Immutable Identity** – Official names and abbreviations do not change; new versions increment systematically
3. **Repository Authority** – Two official repositories serve distinct governance functions; no alternative sources exist
4. **Version Traceability** – All versions tagged, frozen, and documented with clear progression paths
5. **Naming Consistency** – All governance documents follow standardized naming conventions without exception

## Technical Implementation

### Official Framework Designation

**Full Legal Name:**
```
Enterprise AI-Aligned Technical Governance Framework (EATGF)
```

**Official Abbreviation:**
```
EATGF
```

**Designation Authority:** Tariq Said Official  
**Effective Date:** February 13, 2026

### Correct Usage in Documentation

Do use:
- Enterprise AI-Aligned Technical Governance Framework (EATGF)
- EATGF
- EATGF v1.0
- EATGF v1.1
- EATGF Phase 2
- EATGF Phase 3 (pending Phase 2 transition)

Do not use:
- enterprise-governance-framework
- governance framework
- AI governance framework
- technical governance
- control governance
- EGF, AGF, TGF (invalid abbreviations)
- governance-docs (repository nickname only)
- Any informal abbreviation other than EATGF

### Repository Authority and Purpose

**Primary Authority Repository – eatgf-framework**

Repository: eatgf-framework  
Owner: tariqsaidofficial  
URL: https://github.com/tariqsaidofficial/eatgf-framework.git  
Access Level: Public  
Purpose: Single source of truth for all MCM, ISMS, AIMS, audit, and evidence specifications

Contents:
- Master Control Matrix (MCM) – 35 controls across 7 domains
- ISMS Manual (ISO 27001:2022 implementation)
- AIMS Manual (ISO 42001:2023 implementation)
- Internal Audit Procedure (ISO 19011:2018)
- Evidence Register Specification with master control definitions
- Evidence Integrity and Repository Control Policy
- Phase 2 and Phase 3 execution planning artifacts

**Documentation Portal Repository – governance-docs-site**

Repository: governance-docs-site  
Owner: tariqsaidofficial  
URL: https://github.com/tariqsaidofficial/governance-docs-site.git  
Access Level: Public  
Purpose: Public-facing documentation portal with Docusaurus rendering

Contents:
- Governance architecture overview and navigation
- Quick-start implementation guides
- Policy and procedure templates
- Framework roadmaps and evolution decisions
- Best practices and reference implementations
- Case studies and deployment examples

### Version Control and Tagging

**v1.0 Foundation Baseline**

Tag Name: `EATGF-v1.0-Foundation`  
Release Date: February 13, 2026  
Status: FROZEN

Contents:
- Master Control Matrix (35 controls, 7 domains)
- ISMS Manual (ISO 27001:2022, clauses 4-10)
- AIMS Manual (ISO 42001:2023, clauses 4-10)
- Internal Audit Procedure (ISO 19011:2018)
- Evidence Register Specification (20 columns)
- Evidence Integrity Policy (SHA256 hashing)
- Phase 2 Stabilization Plan (6-week cycle)

Freeze Rationale:
- Architecture complete and operationally validated
- No structural changes permitted to MCM, ISMS, or AIMS
- All governance layers defined and documented
- Audit framework operational
- Evidence register specification finalized

**Post-v1.0 Versioning Strategy**

Version Progression: v1.0 → v1.1 (if Week 1-6 refinements) → v2.0 (Phase 3 authorization)

Minor versions (1.x):
- No structural changes to MCM, ISMS, or AIMS
- Clarifications, examples, and procedural updates only
- Change tag: `EATGF-v1.1-[Description]`

Major versions (2.x, 3.x):
- Architectural changes requiring strategic authorization
- Edition-specific variations (Startup, SaaS, Enterprise)
- Change tag: `EATGF-v2.0-[Edition]-[Description]`

All changes logged in CHANGELOG.md with authorization dates.

### Document Naming Standards

**Framework Documents:**
- Format: `PHASE_[N]_[DESCRIPTOR].md`
- Examples: PHASE_2_COMPLETION_SUMMARY.md, WEEK_1_EXECUTION_PLAN.md

**Governance Subdirectory Documents:**
- Format: `[SUBJECT]_[TYPE]_[VERSION].md` or `[SUBJECT].md`
- Examples: EVIDENCE_REGISTER_MASTER.md, EVIDENCE_INTEGRITY_AND_REPOSITORY_CONTROL_POLICY.md

**Management System Documents:**
- Format: `[SYSTEM]_MANUAL_[VERSION].md`
- Examples: ISMS_MANUAL_v1.0.md, AIMS_MANUAL_v1.0.md

**Control Authority Documents:**
- Standard: MASTER_CONTROL_MATRIX.md

**Filename Rules:**
- Use SCREAMING_SNAKE_CASE exclusively
- No spaces, hyphens, or mixed case
- No special characters except underscores

### Header Usage in All Documents

Every governance document must reference the framework officially:

```markdown
**Enterprise AI-Aligned Technical Governance Framework (EATGF)**

[Document Title]
```

In body text:
- "The EATGF Master Control Matrix (MCM) defines..."
- "Per EATGF ISMS Manual v1.0, the control requires..."
- "EATGF evidence integrity policy mandates..."

Do not use:
- "The governance framework..."
- "Our control system..."
- Informal framework references

## Control Mapping

### ISO 27001:2022 Alignment
- **Clause 5.2** – Information security policies and procedures
- **Clause 5.3** – Organization of information security roles
- **Clause 6.2** – Risk assessment and treatment
- **Clause 7.2** – Competence

### NIST SSDF v1.1 Alignment
- **PO1.1** – Establish or reuse a secure development policy
- **PO2.1** – Document and communicate security requirements
- **PO3.1** – Use a consistent set of tools
- **PO3.2** – Document, implement, and enforce a versioning policy

### COBIT 2019 Alignment
- **EDM01** – Evaluate, Direct and Monitor the Establishment and Maintenance of Governance
- **APO01** – Manage the IT Management Framework
- **APO03** – Manage Enterprise Architecture
- **DSS06** – Manage IT Assets

## Developer Checklist

Before publication or repository updates:

- [ ] Framework referenced as "EATGF" (never "EGF", "AGF", or "governance framework")
- [ ] Official repositories identified: eatgf-framework and governance-docs-site
- [ ] Version tag matches current baseline: EATGF-v1.0-Foundation
- [ ] Document filename uses SCREAMING_SNAKE_CASE
- [ ] No alternative naming conventions used in document
- [ ] All hyperlinks point to official repositories
- [ ] Repository URLs use tariqsaidofficial/eatgf-framework format
- [ ] Version progression documented if making modifications to v1.0

## Governance Implications

### Organizational Impact

All enterprise communication, documentation, and stakeholder references must use the official EATGF designation. This includes:

- Board-level governance communications
- Audit and compliance reporting
- External regulatory submissions
- Procurement and vendor communications
- Internal policy and procedure documents

### Authority and Change Control

**Framework Authority:** Tariq Said Official  
**GitHub Organization:** tariqsaidofficial

Change authority varies by phase:

Phase 2 (Current):
- Governance Lead – Approves stabilization updates
- CISO – Approves integrity-related changes
- Chief Audit Officer – Approves audit procedure modifications

Phase 3 and Beyond:
- Framework Council – Strategic decisions on major versions
- Edition-specific steering committees – Edition customization

### Version Management Responsibility

The Framework Authority maintains authoritative naming and versioning. All modifications to v1.0-Foundation automatically increment to v1.1. Major architectural changes require Phase 3 authorization (pending Phase 2 completion by March 31, 2026).

## Official References

- **NIST Special Publication 800-53 Rev. 5** – Security and Privacy Controls for Information Systems and Organizations (2020)
- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
- **ISO/IEC 42001:2023** – Artificial Intelligence Management Systems (2023)
- **COBIT 2019** – Governance of Enterprise Information Technology (ISACA, 2019)
- **CommonMark Specification 0.30** – Markdown Format Standard (2023)
```

---

## Document Naming Standards

### Framework Documents (Root Level)

**Format:** `PHASE_[N]_[DESCRIPTOR].md`

Examples:
-  PHASE_2_COMPLETION_SUMMARY.md
-  PHASE_2_STABILIZATION_PLAN.md
-  PHASE_2_WEEK_1_GO_APPROVAL.md
-  WEEK_1_EXECUTION_PLAN.md
-  WEEK_1_STATUS.md

**Incorrect:**
-  governance-phase-2.md
-  phase2_summary.md
-  P2_Summary.md

### Governance Subdirectory Documents

**Format:** `[SUBJECT]_[TYPE]_[VERSION].md` or `[SUBJECT].md`

Examples:
-  EVIDENCE_REGISTER_MASTER.md
-  EVIDENCE_REGISTER_IMPLEMENTATION_GUIDE.md
-  EVIDENCE_REGISTER_EXCEL_BUILD_SPECIFICATION.md
-  EVIDENCE_INTEGRITY_AND_REPOSITORY_CONTROL_POLICY.md

### Management System Documents

**Format:** [SYSTEM]_MANUAL_[VERSION].md`

Examples:
-  ISMS_MANUAL_v1.0.md
-  AIMS_MANUAL_v1.0.md

### Control Documents

**Format:** `MASTER_CONTROL_MATRIX.md`

Standard:
-  MASTER_CONTROL_MATRIX.md

---

## Official References in Documents

### Header Usage (All Documents Starting)

**MANDATORY FORMAT:**
```markdown
**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
[Document Title]
```

Example:
```markdown
**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
Phase 2 Completion Summary
```

### Body Text Usage

**Recommended Patterns:**
- "The EATGF Master Control Matrix (MCM)..."
- "EATGF evidence integrity controls..."
- "Per EATGF ISMS Manual v1.0..."
- "EATGF Phase 2 architecture..."

**Avoid:**
- "The governance framework..."
- "Our control framework..."
- "The ISO governance system..."

### Hyperlinks

**Internal Links (Within eatgf-framework repo):**
```markdown
[EVIDENCE_REGISTER_MASTER.md](governance/EVIDENCE_REGISTER_MASTER.md)
[MASTER_CONTROL_MATRIX.md](controls/MASTER_CONTROL_MATRIX.md)
```

**External References:**
```markdown
EATGF Reference: https://github.com/tariqsaidofficial/eatgf-framework
Documentation: https://github.com/tariqsaidofficial/governance-docs-site
```

---

## Authority & Governance

**Framework Authority:** Tariq Said Official  
**GitHub Organization:** tariqsaidofficial  
**Official Repositories:** eatgf-framework, governance-docs-site  

**Change Authority (v1.0 Foundation Phase):**
- Governance Lead: Approves Phase 2 stabilization updates
- CISO: Approves integrity-related changes
- Chief Audit Officer: Approves audit procedure modifications

**Change Authority (v2.0+ Phases):**
- Framework Council (to be established)
- Edition-specific steering committees

---

## Phase 2 Current Status

**Phase:** 2 – Management System Layer Establishment  
**Status:** Execution Mode (Week 1: Feb 16-20, 2026)  
**Current Version:** EATGF-v1.0-Foundation (frozen)  
**Next Potential Version:** EATGF-v1.1 (if Week 1-6 refinements needed)  
**Decision Frozen Until:** March 31, 2026 (Phase 2 completion gate)

---

## Enforcement

**Effective Immediately:** All documents created after February 13, 2026, must use:
- Full name: Enterprise AI-Aligned Technical Governance Framework (EATGF)
- Abbreviation: EATGF (not EGF, AGF, or other)
- Repository references: eatgf-framework (not enterprise-governance-framework)
- Version tags: EATGF-vX.X-[Description]

**Retroactive Standards (Recommended but Not Mandatory):**
- Legacy documents may retain original naming but should reference EATGF officially
- When editing legacy documents, apply new naming standards

---

## Document History

| Date | Version | Status | Notes |
|------|---------|--------|-------|
| Feb 13, 2026 | v1.0 | Foundation Freeze | Official naming convention established |
| Feb 16–20, 2026 | v1.0 | Week 1 Execution | Operational validation cycle begins |
| Mar 31, 2026 | v1.0 or v1.1? | Phase 2 Gate | Decision on v1.1 refinements vs. Phase 3 transition |

---

## Sign-Off

**This document officially designates:**

 Framework Name: Enterprise AI-Aligned Technical Governance Framework (EATGF)  
 Official Repositories: eatgf-framework + governance-docs-site  
 v1.0 Foundation Tag: EATGF-v1.0-Foundation (created Feb 13, 2026)  
 Naming Enforcement: Effective immediately  
 Version Progression: v1.0 → v1.1 (if needed) → v2.0 (Phase 3)

**Authority:** Tariq Said Official  
**Date:** February 13, 2026

---

** From this moment forward, the framework is officially known as EATGF.**

**Any modification to EATGF v1.0-Foundation (frozen) will automatically increment to v1.1.**

**Phase 3 authorization requires Phase 2 completion (March 31, 2026 gate).**
