# Baseline Declaration v1.0

| Field | Value |
|-------|-------|
| Document Type | Authority & Governance Baseline |
| Version | 1.0 |
| Classification | Controlled |
| Effective Date | 2026-02-13 |
| Authority | Framework Authority - Tariq Said Official |
| EATGF Layer | 00_FOUNDATION |

---

## Purpose

This document establishes the official baseline declaration for the Enterprise AI-Aligned Technical Governance Framework (EATGF) v1.0-Foundation. It formalizes the freeze of the framework naming, versioning, and governance architecture, establishing an immutable reference point for organizational adoption and audit defensibility.

## Architectural Position

This specification operates within **00_FOUNDATION** of EATGF as the definitive governance baseline and version anchor.

- **Upstream requirement:** Depends on Official Designation (framework naming authority)
- **Downstream enforcement:** All implementation and version management must comply
- **Cross-layer reference:** Referenced by all 01-07 layers for baseline immutability assurance

## Governance Principles

1. **Baseline Immutability** – v1.0-Foundation remains frozen; no retroactive changes permitted
2. **Version Traceability** – All modifications increment to v1.1 or v2.0 with formal authorization
3. **Audit Defensibility** – Baseline provides reliable reference point for governance audits and compliance assessment
4. **Progressive Governance** – Clear version progression path (v1.0 → v1.1 → v2.0) aligned with EATGF phases
5. **Documentation Continuity** – Baseline declaration anchors all subsequent framework evolution

## Technical Implementation

### Official Framework Identity

### Official Framework Identity

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
**Status:** BASELINE FROZEN – Naming, versioning, and governance architecture locked

Deprecated Names (No Longer Valid):
- enterprise-governance-framework (old folder name, archived)
- governance framework (informal, discontinued)
- AI governance framework (too narrow, avoided)
- control governance (too narrow, avoided)
- Any abbreviation other than EATGF (EGF, AGF, etc. invalid)

### Repository Authority and Status

**Primary Authority Repository – eatgf-framework**

Repository: eatgf-framework  
Owner: tariqsaidofficial  
URL: https://github.com/tariqsaidofficial/eatgf-framework.git  
Access: Public  
Purpose: Single source of truth for all governance specifications  
Status: Frozen as v1.0-Foundation baseline

**Documentation Portal Repository – governance-docs-site**

Repository: governance-docs-site  
Owner: tariqsaidofficial  
URL: https://github.com/tariqsaidofficial/governance-docs-site.git  
Access: Public  
Purpose: Public-facing documentation portal (Docusaurus)  
Status: Aligned with v1.0-Foundation baseline

Both repositories are confirmed as official and will remain synchronized with v1.0-Foundation baseline.

### v1.0-Foundation Baseline Contents

**Baseline Designation:** EATGF-v1.0-Foundation  
**Release Date:** February 13, 2026  
**Status:** FROZEN – No changes to v1.0-Foundation allowed

Git Tag Command:
```bash
git tag -a EATGF-v1.0-Foundation \
  -m "EATGF v1.0 - Phase 2 Architecture Freeze (MCM + ISMS + AIMS + Audit + Evidence)"
git push origin EATGF-v1.0-Foundation
```

Framework Contents Included in v1.0-Foundation:

Governance Foundation:
- Master Control Matrix (35 controls, 7 COBIT domains)
- Official Designation and Framework Identity
- Governance Framework Philosophy and Architecture

Management Systems (ISO-aligned):
- ISMS Manual (ISO 27001:2022, complete clauses 4-10)
- AIMS Manual (ISO 42001:2023, complete clauses 4-10)
- Statement of Applicability template

Control Architecture:
- Control Objectives and effectiveness criteria
- Cross-Framework Mappings (COBIT, ISO, NIST, OWASP alignment)
- Risk Framework and assessment methodology

Governance Models:
- Maturity Assessment Framework (capability levels)
- Performance Model and KPI definitions
- Governance by Team Size (Startup to Enterprise editions)

Policy Architecture:
- Governance Charter (formal v2.0)
- Information Security Policy
- Data Governance Policy

Domain Frameworks:
- AI Governance Framework (ISO 42001:2023-aligned)
- API Governance Framework (OWASP-aligned)

Audit and Assurance:
- Internal Audit Procedure (ISO 19011:2018-aligned)
- Audit methodology, qualifications, scheduling

Evidence and Integrity:
- Evidence Register specification (20 columns, complete formulas)
- Evidence Integrity and Repository Control Policy (SHA256 hashing, access controls)

### Baseline Immutability Constraints

No structural changes to v1.0-Foundation are permitted:
- No modifications to v1.0 MCM, ISMS, or AIMS architecture
- No retroactive amendments to v1.0 content
- No version rolling back or retagging

Forward-looking version increments only (v1.1, v2.0) apply changes.

Rationale: Baseline immutability ensures v1.0-Foundation remains a reliable reference point for organizations adopting EATGF and provides an audit-defensible governance anchor.

### Version Progression and Criteria

Version Progression Path:
```
EATGF-v1.0-Foundation (Feb 13, 2026) ← CURRENT BASELINE
    ↓
EATGF-v1.1-[Description] (IF refinements needed during operational phase)
    ↓
EATGF-v2.0-Edition-Deployment (IF Phase 2 passes compliance gates & Phase 3 authorized)
    ↓
EATGF-v2.1-Startup, v2.2-SaaS, v2.3-Enterprise (Edition-specific variants)
```

Version Decision Matrix:

| Change Type | Version Increment | Allowed on v1.0 | Action |
|-------------|-------------------|-----------------|--------|
| Structural changes (new domains, MCM expansion) | Major (v2.0+) | No | Requires new baseline tag |
| Control clarifications, policy updates | Minor (v1.1, v1.2) | No | Create new v1.x tag if needed |
| Documentation improvements, examples | Patch (v1.0.1) | No | v1.0-Foundation immutable |
| Operational tuning per edition | Edition (v2.1, v2.2, v2.3) | No | Post-Phase 3 only |

When Refinements Are Required During the Operational Phase:

Scenario 1 – Minor Clarifications Needed (Weeks 1-6):
1. Document change request with business justification
2. Create new tag: EATGF-v1.1-[Description] (e.g., EATGF-v1.1-Week-2-Refinements)
3. Update CHANGELOG.md with version history
4. Maintain v1.0-Foundation as baseline reference
5. Update documentation portal to reference v1.1

Scenario 2 – Major Changes Needed (Post-Phase 2):
1. Architectural review required (internal governance review)
2. Cross-standard impact assessment (ISO/COBIT/NIST alignment check)
3. Formal approval gates before v2.0 baseline
4. Only authorized post-March 31 Phase 2 gate completion
5. v2.0 replaces v1.0 as production baseline

## Control Mapping

### ISO 27001:2022 Alignment
- **Clause 4.4** – Determining the scope of the information security management system
- **Clause 5.1** – Management commitment and organizational policies
- **Clause 5.2** – Information security policies and procedures
- **Clause 6.2** – Risk assessment and treatment

### NIST SSDF v1.1 Alignment
- **PO1.1** – Establish or reuse a secure development policy
- **PO2.1** – Document and communicate security and privacy requirements
- **PO3.1** – Use a consistent set of tools and methods
- **PO3.2** – Document, implement, and enforce versioning policy

### COBIT 2019 Alignment
- **EDM01** – Evaluate, Direct and Monitor the Establishment of Governance
- **APO01** – Manage the IT Management Framework
- **APO03** – Manage Enterprise Architecture
- **DSS06** – Manage IT Assets

## Developer Checklist

Before implementation or version management:

- [ ] Framework designation matches official v1.0-Foundation baseline
- [ ] Version tag created: EATGF-v1.0-Foundation (February 13, 2026)
- [ ] All organizational communications reference EATGF v1.0-Foundation
- [ ] Baseline contents documented and confirmed complete
- [ ] v1.0 immutability constraints understood and established
- [ ] Post-v1.0 versioning rules documented for future modifications
- [ ] Version progression path clear (v1.0 → v1.1 → v2.0)
- [ ] Framework repository confirmed as definitive source of truth

## Governance Implications

### Organizational Adoption

Organizations adopting EATGF must:
- Reference v1.0-Foundation baseline in all implementation documentation
- Maintain immutability of v1.0 baseline in their deployment
- Follow version progression rules for any customizations or extensions
- Maintain audit trail of version changes and modifications

### Change Authority and Control

Framework Authority: Tariq Said Official  
GitHub Organization: tariqsaidofficial

Change authority varies by modification scope:

Phase 2 Current (v1.0-Foundation):
- Governance Lead – Approves clarification-only updates
- CISO – Approves integrity-related policy changes
- Chief Audit Officer – Approves audit procedure clarifications

Phase 2 Transition to v1.1 (if needed):
- Same as Phase 2, with additional CHANGELOG.md logging requirement

Phase 3 Authorization (v2.0+):
- Framework Council – Strategic decisions on major versions
- Edition-specific steering committees – Edition customization

### Effective Dates and Gates

Official Effective Date: February 13, 2026  
Production Implementation Date: February 16, 2026 (Week 1 operational cycle begins)  
Next Governance Gate: March 31, 2026 (Post-Phase 2 evaluation; Phase 3 authorization decision)

## Official References

- **NIST Special Publication 800-53 Rev. 5** – Security and Privacy Controls for Information Systems and Organizations (2020)
- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
- **ISO/IEC 42001:2023** – Artificial Intelligence Management Systems (2023)
- **COBIT 2019** – Governance of Enterprise Information Technology (ISACA, 2019)
- **ISO/IEC 19011:2018** – Guidelines for Auditing Management Systems (2018)
