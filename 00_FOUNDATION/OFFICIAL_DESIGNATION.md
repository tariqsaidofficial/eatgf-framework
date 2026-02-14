# Official Designation

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**

Official Framework Identity & Naming Convention

---

## Official Framework Name

**Full Legal Name:**
```
Enterprise AI-Aligned Technical Governance Framework (EATGF)
```

**Official Abbreviation:**
```
EATGF
```

**Effective Date:**
```
February 13, 2026
```

---

## Naming Convention (Mandatory)

### Correct Usage

✅ **DO USE:**
- Enterprise AI-Aligned Technical Governance Framework (EATGF)
- EATGF
- EATGF v1.0
- EATGF v1.1
- EATGF Phase 2
- EATGF Phase 3 (pending Phase 2 transition)

### Incorrect Usage

❌ **DO NOT USE:**
- enterprise-governance-framework
- governance framework
- AI governance framework
- technical governance
- control governance
- EGF
- AGF
- TGF
- governance-docs
- Any informal abbreviation not EATGF

---

## Official Repositories

### Primary Authority Repository

**Repository Name:** eatgf-framework  
**GitHub URL:** https://github.com/tariqsaidofficial/eatgf-framework.git  
**Purpose:** Single source of authority for all MCM, ISMS, AIMS, Audit, and Evidence specifications  
**Access:** Public (for reference implementations)  
**Authority:** Tariq Said Official

**Contents:**
- Master Control Matrix (MCM) – 35 controls
- ISMS Manual (ISO 27001:2022)
- AIMS Manual (ISO 42001:2023)
- Internal Audit Procedure (ISO 19011:2018)
- Evidence Register Specification
- Evidence Integrity & Repository Controls
- Phase 2 Stabilization Plan
- Week 1 Execution Plan
- Cross-Framework Mappings

### Documentation Portal Repository

**Repository Name:** governance-docs-site  
**GitHub URL:** https://github.com/tariqsaidofficial/governance-docs-site.git  
**Purpose:** Public-facing documentation with Docusaurus rendering  
**Access:** Public  
**Authority:** Tariq Said Official

**Contents:**
- Governance architecture overview
- Quick-start guides
- Policy templates
- Implementation roadmaps
- Best practices
- Case studies

---

## Version Control & Tagging

### v1.0 Foundation Baseline

**Tag Name:** `EATGF-v1.0-Foundation`  
**Git Command:**
```bash
git tag -a EATGF-v1.0-Foundation -m "EATGF v1.0 - Phase 2 Architecture Freeze (MCM + ISMS + AIMS + Audit + Evidence)"
git push origin EATGF-v1.0-Foundation
```

**Contents:**
- Master Control Matrix (35 controls, 7 domains)
- ISMS Manual (ISO 27001:2022, all clauses)
- AIMS Manual (ISO 42001:2023, all clauses)
- Internal Audit Procedure (ISO 19011:2018)
- Evidence Register Specification (20 columns)
- Evidence Integrity Policy (SHA256 hashing + repository controls)
- Phase 2 Stabilization Plan (6-week operational cycle)
- Week 1 Execution Plan (developer-ready specifications)

**Freeze Rationale:**
- Architecture is complete and operationally validated
- No structural changes to MCM, ISMS, or AIMS
- All governance layers defined
- Audit framework ready
- Evidence register specification final

### Post-v1.0 Versioning

**v1.1 and Beyond:**
- Any modification to v1.0 Foundation → increment to v1.1
- Create new tag: `EATGF-v1.1-[Description]`
- All v1.1+ changes logged in CHANGELOG.md
- Minor versions (1.x) = no structural changes
- Major versions (2.x, 3.x) = architectural changes requiring Phase 3+ decisions

**Version Progression:**
```
EATGF-v1.0-Foundation (Feb 13, 2026) ← Current
   ↓
EATGF-v1.1-... (If Week 1-6 refinements needed)
   ↓
EATGF-v2.0-Edition-Deployment (Phase 3, pending Phase 2 success)
   ↓
EATGF-v2.1-Startup-Tuning, EATGF-v2.2-SaaS-Tuning, EATGF-v2.3-Enterprise-Tuning
   ↓
EATGF-v3.0-... (Future major releases)
```

---

## Document Naming Standards

### Framework Documents (Root Level)

**Format:** `PHASE_[N]_[DESCRIPTOR].md`

Examples:
- ✅ PHASE_2_COMPLETION_SUMMARY.md
- ✅ PHASE_2_STABILIZATION_PLAN.md
- ✅ PHASE_2_WEEK_1_GO_APPROVAL.md
- ✅ WEEK_1_EXECUTION_PLAN.md
- ✅ WEEK_1_STATUS.md

**Incorrect:**
- ❌ governance-phase-2.md
- ❌ phase2_summary.md
- ❌ P2_Summary.md

### Governance Subdirectory Documents

**Format:** `[SUBJECT]_[TYPE]_[VERSION].md` or `[SUBJECT].md`

Examples:
- ✅ EVIDENCE_REGISTER_MASTER.md
- ✅ EVIDENCE_REGISTER_IMPLEMENTATION_GUIDE.md
- ✅ EVIDENCE_REGISTER_EXCEL_BUILD_SPECIFICATION.md
- ✅ EVIDENCE_INTEGRITY_AND_REPOSITORY_CONTROL_POLICY.md

### Management System Documents

**Format:** [SYSTEM]_MANUAL_[VERSION].md`

Examples:
- ✅ ISMS_MANUAL_v1.0.md
- ✅ AIMS_MANUAL_v1.0.md

### Control Documents

**Format:** `MASTER_CONTROL_MATRIX.md`

Standard:
- ✅ MASTER_CONTROL_MATRIX.md

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

✅ Framework Name: Enterprise AI-Aligned Technical Governance Framework (EATGF)  
✅ Official Repositories: eatgf-framework + governance-docs-site  
✅ v1.0 Foundation Tag: EATGF-v1.0-Foundation (created Feb 13, 2026)  
✅ Naming Enforcement: Effective immediately  
✅ Version Progression: v1.0 → v1.1 (if needed) → v2.0 (Phase 3)

**Authority:** Tariq Said Official  
**Date:** February 13, 2026

---

**🎯 From this moment forward, the framework is officially known as EATGF.**

**Any modification to EATGF v1.0-Foundation (frozen) will automatically increment to v1.1.**

**Phase 3 authorization requires Phase 2 completion (March 31, 2026 gate).**
