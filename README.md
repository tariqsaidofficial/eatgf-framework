# Enterprise AI-Aligned Technical Governance Framework (EATGF)

**Global Reference Governance Architecture & Knowledge Centre**
**Version 1.0 – Foundation Edition**

---

## 1. Purpose

EATGF is a vendor-neutral, standards-aligned governance architecture designed to provide a structured and traceable model for:

- **Enterprise IT Governance** – Infrastructure, systems, and technology controls
- **Information Security Governance** – Aligned with ISO/IEC 27001:2022
- **AI Governance** – Aligned with ISO/IEC 42001:2023 and NIST AI RMF
- **API Governance** – Security and lifecycle management (OWASP-aligned)
- **Risk & Assurance Models** – Assessment frameworks and audit methodology

This repository serves as the **Authoritative Knowledge Centre Edition** of the framework. It provides governance architecture, structured control definitions, cross-standard alignment, adoption guidance, and reference implementations for organizations of varying sizes and maturity levels.

---

## 2. Scope

This repository includes:

 **Master Control Matrix** – Single authoritative control inventory (35 controls across 7 COBIT domains)

 **ISO-aligned Management System Specifications** – ISMS (ISO/IEC 27001:2022) and AIMS (ISO/IEC 42001:2023)

 **Cross-standard Mapping Architecture** – COBIT ↔ ISO ↔ NIST alignment matrices

 **Governance Maturity and Performance Models** – Capability assessment frameworks and KPI definitions

 **Policy Architecture Examples** – Governance charters and formal policy templates

 **Domain-specific Governance Extensions** – AI and API governance frameworks

 **Audit and Assurance Framework Design** – Methodology aligned with ISO 19011:2018

**This repository does not include:**

 Operational tooling (no Excel, SharePoint, or deployment scripts)

 Vendor-specific configurations

 Organization-specific execution playbooks

 Deployment automation

---

## 3. Architectural Principles

EATGF is built on seven core architectural principles:

1. **Single Control Authority** – The Master Control Matrix serves as the sole control source of truth; no alternative control taxonomies

2. **Standards Traceability** – Every control and policy maps to recognized international standards (ISO, COBIT, NIST)

3. **Governance Before Tooling** – Architectural decisions precede technology selection; no vendor lock-in

4. **Architecture Before Execution** – Supply the governance model; organizations implement according to their context

5. **Vendor Neutrality** – Framework operates independently of any commercial platform or proprietary solution

6. **Audit Defensibility** – All controls defensible against external audit standards and regulatory frameworks

7. **Scalable Governance Models** – Single architecture adapts to startups, SaaS, and large regulated enterprises

---

## 4. Framework Architecture (8 Layers)

EATGF is organized into eight authoritative layers, each serving a distinct governance function:

### **[00_FOUNDATION](00_FOUNDATION/README.md)**

Authority, naming conventions, and control inventory

- **OFFICIAL_DESIGNATION.md** – Framework identity and naming standards
- **MASTER_CONTROL_MATRIX.md** – 35 controls, 7 domains (sole control authority)
- **GOVERNANCE_FRAMEWORK_README.md** – Framework overview and governance philosophy
- **BASELINE_DECLARATION_v1.0.md** – Official baseline declaration (naming freeze, version freeze, governance anchor)

---

### **[01_MANAGEMENT_SYSTEMS](01_MANAGEMENT_SYSTEMS/README.md)**

ISO-aligned formal management systems

**ISMS (ISO 27001:2022)**

- **ISMS_MANUAL_v1.0.md** – Complete ISMS implementation (clauses 4–10)
- **01_STATEMENT_OF_APPLICABILITY_TEMPLATE.md** – SoA framework for audits

**AIMS (ISO 42001:2023)**

- **AIMS_MANUAL_v1.0.md** – Complete AIMS implementation (clauses 4–10, AI lifecycle)

---

### **[02_CONTROL_ARCHITECTURE](02_CONTROL_ARCHITECTURE/README.md)**

Controls, mappings, and risk framework

- **CONTROL_OBJECTIVES.md** – Control objectives and effectiveness criteria
- **FRAMEWORK_MAPPINGS.md** – Cross-standard alignment (COBIT, ISO, NIST)
- **FRAMEWORK_MAPPINGS_COMPREHENSIVE_v2.md** – Detailed mapping matrix
- **RISK_FRAMEWORK.md** – Risk assessment and management methodology

---

### **[03_GOVERNANCE_MODELS](03_GOVERNANCE_MODELS/README.md)**

Maturity, performance, and team-sizing models

**Maturity Model**

- **MATURITY_ASSESSMENT.md** – Capability level definitions (CMM-style)

**Performance Model**

- **PERFORMANCE_MODEL.md** – KPI framework and measurement approach

**Team Sizing**

- **GOVERNANCE_BY_TEAM_SIZE.md** – Governance adaptation for organizations of all sizes

---

### **[04_POLICY_LAYER](04_POLICY_LAYER/README.md)**

Formal governance policies and charters

- **GOVERNANCE_CHARTER_FORMAL_v2.md** – Formal charter (authoritative governance document)
- **01_GOVERNANCE_CHARTER.md** – Charter components and governance structure
- **02_INFORMATION_SECURITY_POLICY.md** – Security policy implementation
- **03_DATA_GOVERNANCE_POLICY.md** – Data and privacy governance policy
- **04_INCIDENT_RESPONSE_POLICY.md** – Incident response procedures and SLAs
- **05_BUSINESS_CONTINUITY_AND_DISASTER_RECOVERY_POLICY.md** – BC/DR architecture and testing
- **06_VENDOR_AND_THIRD_PARTY_RISK_MANAGEMENT_POLICY.md** – Vendor assessment and compliance
- **07_DATA_PRIVACY_AND_PROTECTION_POLICY.md** – GDPR and personal data protection
- **08_ACCEPTABLE_USE_POLICY.md** – System usage governance and discipline

---

### **[05_DOMAIN_FRAMEWORKS](05_DOMAIN_FRAMEWORKS/README.md)**

Domain-specific governance extensions

- **AI_GOVERNANCE_FRAMEWORK.md** – AI/ML governance and compliance
- **API_GOVERNANCE_FRAMEWORK.md** – API security and governance standards

---

### **[06_AUDIT_AND_ASSURANCE](06_AUDIT_AND_ASSURANCE/README.md)**

Audit methodology and assurance framework

- **INTERNAL_AUDIT_PROCEDURE_v1.0.md** – ISO 19011:2018 audit methodology
  - Annual full audits
  - Quarterly sampling audits
  - Thematic audits
  - Auditor independence and qualifications
- **AUDIT_SCHEDULE_STANDARD.md** – 5-quarter audit cycle and control frequency matrix
- **CORRECTIVE_ACTION_REGISTER_STANDARD.md** – Finding documentation and remediation tracking
- **CERTIFICATION_READINESS_CHECKLIST_STANDARD.md** – Pre-audit control readiness validation
- **EVIDENCE_GOVERNANCE_STANDARD.md** – Evidence storage, retention, access, and disposal

---

### **[07_REFERENCE_AND_EVOLUTION](07_REFERENCE_AND_EVOLUTION/README.md)**

Implementation history, evolution records, and historical artifacts

Framework development history, strategic decisions from governance architecture evolution, and historical implementation materials. **Reference-only layer:** Not part of the authoritative governance framework; provided for context and governance methodology understanding.

---

## 5. Standards Alignment

EATGF structurally aligns with leading international governance frameworks:

| Standard                              | Scope                           | EATGF Alignment                               |
| ------------------------------------- | ------------------------------- | --------------------------------------------- |
| **COBIT 2019**                        | IT investment & risk management | Control mapping (7 domains, 35 controls)      |
| **ISO/IEC 27001:2022**                | Information security management | ISMS manual + Annex A controls + SoA template |
| **ISO/IEC 42001:2023**                | AI governance & risk management | AIMS manual + 7-area AI lifecycle framework   |
| **ISO 19011:2018**                    | Audit methodology               | Internal audit procedure design               |
| **ISO 31000**                         | Risk management framework       | Risk assessment methodology + definitions     |
| **NIST AI Risk Management Framework** | AI governance                   | Control alignment + lifecycle integration     |
| **NIST SP 800-53**                    | Information security controls   | Cross-reference mapping to COBIT/ISO          |
| **OWASP API Security Top 10**         | API security governance         | Domain framework alignment                    |

**Important Note:** EATGF respects the intellectual property rights of all referenced standards. The framework does not reproduce proprietary standard content and does not claim certification equivalence.

---

## 6. Adoption Model

EATGF is designed for organizations of varying sizes and maturity levels:

**Foundational Support:**

- Startups (essential governance foundation)
- SaaS organizations (security & compliance baseline)
- Medium-sized enterprises (scalable governance)
- Large regulated enterprises (audit-defensible architecture)

**Governance Adaptation Factors:**

Organizations adapt EATGF based on:

- **Organizational size** – Startup vs. enterprise governance complexity
- **Regulatory exposure** – Industry-specific compliance requirements
- **AI usage intensity** – From minimal to mission-critical AI deployment
- **Risk profile** – Data sensitivity, criticality, and stakeholder exposure
- **Maturity level** – Initial to optimized capability progression

**Implementation Philosophy:** EATGF supplies the governance architecture and structuring models. Implementation decisions remain organization-specific and context-dependent.

---

## 7. Versioning Policy

**Version Progression Model:**

- **Structural modifications** (architecture changes, domain additions) → Major version increment (v2.0+)
- **Control clarifications, policy updates** → Minor increment (v1.1, v1.2)
- **Documentation improvements, examples** → Patch increment (v1.0.1)

**Baseline Immutability:** Versions tagged in git are immutable. All structural governance specifications are locked at tag time.

---

## 8. Intellectual Property & Attribution

**Standards References:**

All referenced standards remain the intellectual property of their respective issuing bodies:

- ISO/IEC standards – International Organization for Standardization
- COBIT – Information Systems Audit and Control Association (ISACA)
- NIST frameworks – National Institute of Standards and Technology (USA)
- OWASP – Open Worldwide Application Security Project

**EATGF Intellectual Property:**

EATGF represents an original governance architecture synthesis developed by combining and structuring guidance from multiple international standards into a unified, traceable framework.

EATGF:

-  Creates novel control taxonomy and cross-standard alignment
-  Provides original governance architecture design
-  Supplies structured implementation guidance
-  Does not replicate proprietary standard content
-  Does not claim certification equivalence
-  Does not substitute for acquiring licenses to referenced standards

**Attribution Format:**

```
Enterprise AI-Aligned Technical Governance Framework (EATGF)
Version 1.0 – Foundation Edition
Source: https://github.com/tariqsaidofficial/eatgf-framework
```

---

## 9. Repository Status

| Element                    | Status                                                     |
| -------------------------- | ---------------------------------------------------------- |
| **Repository Type**        | Public – Reference Architecture & Knowledge Centre         |
| **Framework Status**       | v1.0 Foundation + v1.1 Policy/Assurance Layer Enhancements |
| **Edition Type**           | Foundation – Governance Architecture (non-operational)     |
| **Operational Status**     | Reference-only; no deployment automation included          |
| **Version Control**        | Git with immutable baseline tags                           |
| **Documentation Language** | English (UK)                                               |
| **Last Updated**           | 16 February 2026                                           |

---

##  How to Use This Framework

**For Governance Professionals:** Start with [00_FOUNDATION](00_FOUNDATION/README.md) to understand framework authority and control inventory.

**For Security Teams:** Review [01_MANAGEMENT_SYSTEMS](01_MANAGEMENT_SYSTEMS/README.md) for ISMS architecture aligned with ISO 27001:2022.

**For AI Governance:** Study [05_DOMAIN_FRAMEWORKS](05_DOMAIN_FRAMEWORKS/README.md) for AI lifecycle governance aligned with ISO 42001:2023.

**For Compliance & Audit:** Use [06_AUDIT_AND_ASSURANCE](06_AUDIT_AND_ASSURANCE/README.md) for audit methodology and control assessment.

**For Architecture Decisions:** Reference [02_CONTROL_ARCHITECTURE](02_CONTROL_ARCHITECTURE/README.md) for control definitions and cross-standard alignment.

---

**EATGF – Governance Architecture & Knowledge Centre**
**Version 1.0 – Foundation Baseline**
**Authoritative Reference Edition**
