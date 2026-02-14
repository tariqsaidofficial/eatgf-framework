# Enterprise AI-Aligned Technical Governance Framework (EATGF)

## Governance Framework Overview

| Field | Value |
|-------|-------|
| Document Type | Framework Overview |
| Version | 2.0 |
| Classification | Public |
| Effective Date | 2026-02-14 |
| Authority | Enterprise Architecture & Governance Office |
| MCM Reference | EATGF-EDM-GOV-01 |

---

## 1. Purpose

This document provides a navigational overview of the Enterprise AI-Aligned Technical Governance Framework (EATGF). The EATGF is a structured, 8-layer governance architecture containing 35 controls defined in the Master Control Matrix (MCM), aligned with international standards.

## 2. Standards Alignment

The EATGF is aligned with the following standards:

- **COBIT 2019** — Control Objectives for Information and Related Technologies
- **ISO/IEC 27001:2022** — Information Security Management Systems
- **ISO/IEC 38500:2015** — Corporate Governance of Information Technology
- **ISO/IEC 42001:2023** — Artificial Intelligence Management Systems
- **OWASP API Security Top 10 (2023)** — API Security

## 3. Repository Structure

```
eatgf-framework/
├── 00_FOUNDATION/          Layer 0 — Baseline declarations and framework overview
├── 01_MANAGEMENT_SYSTEMS/  Layer 1 — ISMS and AIMS manuals
├── 02_CONTROL_ARCHITECTURE/ Layer 2 — MCM, control objectives, risk framework, mappings
├── 03_GOVERNANCE_MODELS/   Layer 3 — Editions, maturity model, performance model
├── 04_POLICY_LAYER/        Layer 4 — Governance charter, security and data policies
├── 05_DOMAIN_FRAMEWORKS/   Layer 5 — AI governance, API governance
├── 06_AUDIT_AND_ASSURANCE/ Layer 6 — Internal audit procedures
└── 07_REFERENCE_AND_EVOLUTION/ Layer 7 — Roadmaps, decision records, historical artifacts
```

## 4. MCM Control Domains (35 Controls)

| Domain | Controls | Description |
|--------|----------|-------------|
| EDM | 3 | Evaluate, Direct, Monitor — Board-level oversight |
| APO | 4 | Align, Plan, Organize — Architecture, risk, ISMS, AIMS |
| BAI | 3 | Build, Acquire, Implement — Change, configuration, QA |
| DSS | 4 | Deliver, Service, Support — IAM, encryption, vulnerability, incident |
| MEA | 3 | Monitor, Evaluate, Assess — Audit, performance, maturity |
| AI | 2 | AI lifecycle governance and risk management |
| API | 2 | API security and lifecycle management |
| CLD | 4 | Cloud architecture, security, monitoring, resilience |
| DEV | 4 | Secure SDLC, code scanning, supply chain, CI/CD |
| DATA | 3 | DPIA, data retention, data minimization |
| BCP | 3 | Business continuity planning, testing, RTO/RPO |

## 5. Governance Editions

| Edition | Personnel | Setup Time | Governance FTE |
|---------|-----------|------------|----------------|
| Startup | 1-10 | 2 weeks | 1-2 |
| SaaS | 10-50 | 2-3 months | 2-3 |
| Enterprise | 50+ | 4-6 months | 8-12 |

Edition-specific guidance: [GOVERNANCE_BY_TEAM_SIZE.md](../03_GOVERNANCE_MODELS/GOVERNANCE_BY_TEAM_SIZE.md)

## 6. Core Document Navigation

### Foundation and Authority

| Document | Path | Purpose |
|----------|------|---------|
| Baseline Declaration | [BASELINE_DECLARATION_v1.0.md](BASELINE_DECLARATION_v1.0.md) | Framework baseline and version lock |
| Master Control Matrix | [MASTER_CONTROL_MATRIX.md](MASTER_CONTROL_MATRIX.md) | Single source of truth for all 35 controls |
| Official Designation | [OFFICIAL_DESIGNATION.md](OFFICIAL_DESIGNATION.md) | Framework naming and authority |

### Policies

| Document | Path | Purpose |
|----------|------|---------|
| Governance Charter | [01_GOVERNANCE_CHARTER.md](../04_POLICY_LAYER/01_GOVERNANCE_CHARTER.md) | Strategic governance direction |
| Governance Charter (Formal) | [GOVERNANCE_CHARTER_FORMAL_v2.md](../04_POLICY_LAYER/GOVERNANCE_CHARTER_FORMAL_v2.md) | Board-level formal charter |
| Information Security Policy | [02_INFORMATION_SECURITY_POLICY.md](../04_POLICY_LAYER/02_INFORMATION_SECURITY_POLICY.md) | Data protection requirements |
| Data Governance Policy | [03_DATA_GOVERNANCE_POLICY.md](../04_POLICY_LAYER/03_DATA_GOVERNANCE_POLICY.md) | Data management requirements |

### Control Architecture

| Document | Path | Purpose |
|----------|------|---------|
| Control Objectives | [CONTROL_OBJECTIVES.md](../02_CONTROL_ARCHITECTURE/CONTROL_OBJECTIVES.md) | 35 control objectives with evidence requirements |
| Framework Mappings | [FRAMEWORK_MAPPINGS.md](../02_CONTROL_ARCHITECTURE/FRAMEWORK_MAPPINGS.md) | COBIT, ISO, OWASP cross-mappings |
| Risk Framework | [RISK_FRAMEWORK.md](../02_CONTROL_ARCHITECTURE/RISK_FRAMEWORK.md) | Enterprise risk management methodology |

### Domain Frameworks

| Document | Path | Purpose |
|----------|------|---------|
| AI Governance | [AI_GOVERNANCE_FRAMEWORK.md](../05_DOMAIN_FRAMEWORKS/AI_GOVERNANCE_FRAMEWORK.md) | AI/ML system governance |
| API Governance | [API_GOVERNANCE_FRAMEWORK.md](../05_DOMAIN_FRAMEWORKS/API_GOVERNANCE_FRAMEWORK.md) | API security and lifecycle |

### Assessment and Monitoring

| Document | Path | Purpose |
|----------|------|---------|
| Maturity Assessment | [MATURITY_ASSESSMENT.md](../03_GOVERNANCE_MODELS/MATURITY_MODEL/MATURITY_ASSESSMENT.md) | Governance maturity evaluation |
| Performance Model | [PERFORMANCE_MODEL.md](../03_GOVERNANCE_MODELS/PERFORMANCE_MODEL/PERFORMANCE_MODEL.md) | KPI and measurement framework |
| Internal Audit | [INTERNAL_AUDIT_PROCEDURE_v1.0.md](../06_AUDIT_AND_ASSURANCE/INTERNAL_AUDIT_PROCEDURE_v1.0.md) | Audit program and procedures |

## 7. Documentation Portal

The companion Docusaurus portal provides a formatted, navigable version of this framework:

- Repository: [governance-docs-site](https://github.com/tariqsaidofficial/governance-docs-site)

The portal renders this repository as its content source via Git submodule.

## 8. Governance Enforcement Rules

1. The Master Control Matrix is the single source of truth for all control definitions. All documents in this repository derive authority from the MCM.
2. Control IDs use the `EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]` taxonomy exclusively.
3. Framework updates follow the semi-annual review cycle (February and August).
4. All documents must conform to the EATGF Document Template as defined in the Documentation Style Review Report.

---

**Document Control**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-01 | Governance Office | Initial framework overview |
| 2.0 | 2026-02-14 | Enterprise Architecture & Governance Office | Corrected to 35-control MCM taxonomy; removed marketing content; corrected directory structure; standardized ISO 42001 to 2023; removed placeholder content |

**Next Review:** August 2026
