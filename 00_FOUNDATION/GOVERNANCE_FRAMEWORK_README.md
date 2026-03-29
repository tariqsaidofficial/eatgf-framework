# Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field | Value |
|-------|-------|
| Document Type | Framework Overview & Navigation Guide |
| Version | 2.0 |
| Classification | Public |
| Effective Date | 2026-02-14 |
| Authority | Enterprise Architecture and Governance Office |
| EATGF Layer | 00_FOUNDATION |
| MCM Reference | EATGF-EDM-GOV-01 |

---

## Purpose

This document provides a comprehensive navigational overview of the Enterprise AI-Aligned Technical Governance Framework (EATGF). It explains the framework's 8-layer architecture, control inventory, documentation structure, governance editions, and standards alignment. This guide serves as the entry point for understanding EATGF's scope, organization, and usage.

## Architectural Position

This specification operates within **00_FOUNDATION** of EATGF as the authoritative framework navigation guide and structural overview.

- **Upstream dependency:** Depends on Official Designation and Baseline Declaration for authority
- **Downstream usage:** Referenced by all 01-07 layers for framework navigation and context
- **Cross-layer reference:** Provides structural overview for all EATGF governance layers

## Governance Principles

1. **Single Control Authority** – The Master Control Matrix (MCM) serves as the sole source of truth for all 35 controls
2. **Layered Architecture** – Eight distinct layers organize governance from foundation through evolution
3. **Standards Alignment** – All controls mapped to COBIT, ISO, NIST, and OWASP frameworks
4. **Edition-Based Scalability** – Single framework adapts to Startup, SaaS, and Enterprise organizations
5. **Audit Defensibility** – Framework structure supports independent assessment and certification

## Technical Implementation

### Framework Architecture Overview

EATGF is organized into eight authoritative layers, each serving distinct governance functions:

**Layer 00 – FOUNDATION**
Authority, naming conventions, and governance baseline
- Official Designation and naming standards
- Master Control Matrix (35 controls, 7 COBIT domains)
- Baseline Declaration and version control
- Governance Framework Philosophy

**Layer 01 – MANAGEMENT SYSTEMS**
ISO-aligned formal management systems
- ISMS Manual (ISO 27001:2022 implementation)
- AIMS Manual (ISO 42001:2023 implementation)
- Statement of Applicability template

**Layer 02 – CONTROL ARCHITECTURE**
Controls, objectives, mappings, and risk framework
- Control Objectives (all 35 controls defined)
- Framework Mappings (COBIT, ISO, NIST, OWASP alignment)
- Risk Framework and assessment methodology

**Layer 03 – GOVERNANCE MODELS**
Capability assessment and performance frameworks
- Maturity Assessment Framework
- Performance Model and KPI definitions
- Governance by Team Size (edition guidance)

**Layer 04 – POLICY LAYER**
Formal governance policies and charters
- Governance Charter (strategic direction)
- Information Security Policy
- Data Governance Policy

**Layer 05 – DOMAIN FRAMEWORKS**
Domain-specific governance extensions
- AI Governance Framework (AI/ML systems)
- API Governance Framework (API security and lifecycle)

**Layer 06 – AUDIT AND ASSURANCE**
Audit methodology and assurance frameworks
- Internal Audit Procedure (ISO 19011:2018-aligned)
- Audit program design and execution

**Layer 07 – REFERENCE AND EVOLUTION**
Historical artifacts, roadmaps, and decision records
- Framework evolution history
- Decision records and design rationale
- Future roadmaps and planning

### Master Control Matrix Organization

The MCM organizes 35 controls across 11 domains:

| Domain | Controls | Description |
|--------|----------|-------------|
| EDM | 3 | Evaluate, Direct, Monitor – Board-level oversight |
| APO | 4 | Align, Plan, Organize – Architecture, risk, ISMS, AIMS |
| BAI | 3 | Build, Acquire, Implement – Change, configuration, QA |
| DSS | 4 | Deliver, Service, Support – IAM, encryption, vulnerability, incident |
| MEA | 3 | Monitor, Evaluate, Assess – Audit, performance, maturity |
| AI | 2 | AI lifecycle governance and risk management |
| API | 2 | API security and lifecycle management |
| CLD | 4 | Cloud architecture, security, monitoring, resilience |
| DEV | 4 | Secure SDLC, code scanning, supply chain, CI/CD |
| DATA | 3 | Data protection, retention, and minimization |
| BCP | 3 | Business continuity planning, testing, RTO/RPO |

### Governance Editions

The framework scales across three governance editions:

| Edition | Organization Size | Setup Time | Governance Effort |
|---------|-------------------|------------|------------------|
| Startup | 1-10 personnel | 2 weeks | 1-2 FTE |
| SaaS | 10-50 personnel | 2-3 months | 2-3 FTE |
| Enterprise | 50+ personnel | 4-6 months | 8-12 FTE |

Edition-specific guidance: See GOVERNANCE_BY_TEAM_SIZE.md in Layer 03 for detailed customization.

### Key Document Index

**Foundation and Authority Documents**

| Document | Path | Purpose |
|----------|------|---------|
| Baseline Declaration | BASELINE_DECLARATION_v1.0.md | Framework baseline and version lock |
| Master Control Matrix | MASTER_CONTROL_MATRIX.md | Single source of truth for 35 controls |
| Official Designation | OFFICIAL_DESIGNATION.md | Framework naming and authority |

**Policies and Governance**

| Document | Path | Purpose |
|----------|------|---------|
| Governance Charter | ../04_POLICY_LAYER/01_GOVERNANCE_CHARTER.md | Strategic governance direction |
| Governance Charter (Formal) | ../04_POLICY_LAYER/GOVERNANCE_CHARTER_FORMAL_v2.md | Board-level formal charter |
| Information Security Policy | ../04_POLICY_LAYER/02_INFORMATION_SECURITY_POLICY.md | Data protection requirements |
| Data Governance Policy | ../04_POLICY_LAYER/03_DATA_GOVERNANCE_POLICY.md | Data management requirements |

**Control Architecture and Mappings**

| Document | Path | Purpose |
|----------|------|---------|
| Control Objectives | ../02_CONTROL_ARCHITECTURE/CONTROL_OBJECTIVES.md | 35 control objectives with evidence requirements |
| Framework Mappings | ../02_CONTROL_ARCHITECTURE/FRAMEWORK_MAPPINGS.md | COBIT, ISO, NIST, OWASP cross-mappings |
| Risk Framework | ../02_CONTROL_ARCHITECTURE/RISK_FRAMEWORK.md | Enterprise risk management methodology |

**Domain-Specific Frameworks**

| Document | Path | Purpose |
|----------|------|---------|
| AI Governance | ../05_DOMAIN_FRAMEWORKS/AI_GOVERNANCE_FRAMEWORK.md | AI/ML system governance |
| API Governance | ../05_DOMAIN_FRAMEWORKS/API_GOVERNANCE_FRAMEWORK.md | API security and lifecycle |

**Assessment and Assurance**

| Document | Path | Purpose |
|----------|------|---------|
| Maturity Assessment | ../03_GOVERNANCE_MODELS/MATURITY_MODEL/MATURITY_ASSESSMENT.md | Governance maturity evaluation |
| Performance Model | ../03_GOVERNANCE_MODELS/PERFORMANCE_MODEL/PERFORMANCE_MODEL.md | KPI and measurement framework |
| Internal Audit | ../06_AUDIT_AND_ASSURANCE/INTERNAL_AUDIT_PROCEDURE_v1.0.md | Audit program and procedures |

### Standards Alignment

The EATGF is aligned with the following international standards:

- **COBIT 2019** – Control Objectives for Information and Related Technologies (ISACA)
- **ISO/IEC 27001:2022** – Information Security Management Systems
- **ISO/IEC 27002:2022** – Information Security Code of Practice
- **ISO/IEC 38500:2015** – Corporate Governance of Information Technology
- **ISO/IEC 42001:2023** – Artificial Intelligence Management Systems
- **ISO/IEC 19011:2018** – Guidelines for Auditing Management Systems
- **NIST SP 800-53 Rev. 5** – Security and Privacy Controls
- **NIST AI Risk Management Framework** – AI governance alignment
- **OWASP API Security Top 10** – API security framework

### Documentation Portal

The companion Docusaurus portal provides a formatted, navigable version of EATGF:

Repository: https://github.com/tariqsaidofficial/governance-docs-site

The portal renders this repository as its content source via Git submodule, ensuring documentation stays synchronized with the authoritative framework repository.

## Control Mapping

### ISO 27001:2022 Alignment
- **Clause 4.3** – Determining the scope of the ISMS
- **Clause 5.1** – Leadership and commitment
- **Clause 5.2** – Information security policies
- **Clause 6.1** – Planning to address risks and opportunities

### NIST SSDF v1.1 Alignment
- **PO1.1** – Establish or reuse secure development policy
- **PO2.1** – Document and communicate security requirements
- **PO3.1** – Use a consistent set of tools and methods
- **PO3.2** – Document, implement, and enforce versioning policy

### COBIT 2019 Alignment
- **EDM01** – Evaluate, Direct and Monitor the Establishment of Governance
- **APO01** – Manage the IT Management Framework
- **APO03** – Manage Enterprise Architecture
- **DSS06** – Manage IT Assets

## Developer Checklist

Before implementation or framework adoption:

- [ ] All 8 layers of EATGF reviewed and understood
- [ ] Framework navigation guide (this document) consulted
- [ ] Appropriate governance edition selected (Startup, SaaS, or Enterprise)
- [ ] Master Control Matrix reviewed as control authority source
- [ ] Standards alignment documents consulted for compliance mapping
- [ ] Documentation portal (governance-docs-site) accessible and current
- [ ] Governance policies reviewed for organizational applicability
- [ ] Implementation timeline and resource requirements documented

## Governance Implications

### Organizational Adoption

Organizations implementing EATGF must:
- Use the Master Control Matrix as the single authoritative control inventory
- Organize governance activities across all 8 EATGF layers
- Select appropriate governance edition based on organizational size
- Map internal controls to EATGF control taxonomy
- Maintain audit trails and evidence aligned with EATGF specifications

### Framework Governance

**Framework Authority:** Tariq Said Official  
**Governance Review Cycle:** Semi-annual (February and August)  
**Version Management:** Following EATGF-v1.0-Foundation baseline immutability constraints

Governance Enforcement Rules:
1. The Master Control Matrix is the single source of truth for all control definitions
2. All documents derive authority from the MCM
3. Control IDs follow the EATGF-[DOMAIN]-[CATEGORY]-[NUMBER] taxonomy exclusively
4. All documents conform to EATGF Official Formatting Standards
5. Changes to v1.0-Foundation require version increment to v1.1 or v2.0

### Change Authority

Changes to EATGF governance structure require:
- Phase 2 (Current): Governance Lead approval for clarifications
- Phase 2 Transition: CISO approval for integrity-related changes
- Phase 3 (Future): Framework Council approval for major versions

## Official References

- **NIST Special Publication 800-53 Rev. 5** – Security and Privacy Controls for Information Systems and Organizations (2020)
- **NIST Special Publication 800-218** – Secure Software Development Framework (2022)
- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
- **ISO/IEC 27002:2022** – Information Security Code of Practice (2022)
- **ISO/IEC 42001:2023** – Artificial Intelligence Management Systems (2023)
- **ISO/IEC 38500:2015** – Corporate Governance of Information Technology (2015)
- **ISO/IEC 19011:2018** – Guidelines for Auditing Management Systems (2018)
- **COBIT 2019** – Governance of Enterprise Information Technology (ISACA, 2019)
- **OWASP API Security Top 10** – API Security Risks (OWASP Foundation, 2023)
