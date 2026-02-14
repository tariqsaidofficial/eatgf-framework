# 01_MANAGEMENT_SYSTEMS

| Field | Value |
|-------|-------|
| Document Type | Layer Navigation & Overview |
| Version | 2.0 |
| Classification | Controlled |
| Effective Date | 2026-02-14 |
| Authority | Enterprise Architecture and Governance Office |
| EATGF Layer | 01_MANAGEMENT_SYSTEMS |

---

## Purpose

This layer contains the formal ISO-aligned management systems that operationalize EATGF across the enterprise. The Information Security Management System (ISMS) and Artificial Intelligence Management System (AIMS) provide the procedural framework for implementing and maintaining governance according to international standards.

## Architectural Position

This layer operates within **01_MANAGEMENT_SYSTEMS** and establishes formal management system procedures.

- **Upstream dependency:** Layer 00 (Foundation) defines controls; Layer 02 provides control specifications
- **Downstream usage:** Policies in Layer 04 operationalize these systems; Layer 06 audits compliance
- **Cross-layer reference:** Systems trace all controls to Layer 00 MCM and map to Layer 02 control architecture

## Governance Principles

1. **Standards Compliance** – ISMS fully implements ISO 27001:2022; AIMS fully implements ISO 42001:2023
2. **Integrated Systems** – ISMS and AIMS operate together as complementary governance systems
3. **Evidence Traceability** – All procedures include evidence requirements for audit demonstration
4. **Audit Defensibility** – Formal management systems document compliance for external certification
5. **Dual Governance** – Information security and AI governance formalized alongside each other

## Technical Implementation

### Information Security Management System (ISMS)

**Standard:** ISO 27001:2022  
**Scope:** All information security procedures and controls  
**Document:** ISMS_MANUAL_v1.0.md

ISMS Coverage:
- Clause 4 – Context of the organization (scope and boundaries)
- Clause 5 – Leadership and commitment (responsibility and policy)
- Clause 6 – Planning (risk assessment, objectives, change management)
- Clause 7 – Support (resources, competence, awareness, communication)
- Clause 8 – Operation (implementation of controls and procedures)
- Clause 9 – Performance evaluation (monitoring, measurement, internal audit)
- Clause 10 – Improvement (nonconformity handling, corrective actions)

ISMS Procedures Include:
- Information security policies and procedures
- Access control procedures
- Asset management and classification
- Incident response procedures
- Supplier risk management
- Security awareness training program
- Security patch and change management

### Artificial Intelligence Management System (AIMS)

**Standard:** ISO 42001:2023  
**Scope:** All AI and machine learning system procedures and controls  
**Document:** AIMS_MANUAL_v1.0.md

AIMS Coverage:
- Clause 4 – Context of the organization (AI system scope)
- Clause 5 – Leadership and commitment (AI governance commitment)
- Clause 6 – Planning (AI risk management, objectives)
- Clause 7 – Support (AI competence, resources, training)
- Clause 8 – Operation (AI system implementation and monitoring)
- Clause 9 – Performance evaluation (AI model performance, audit)
- Clause 10 – Improvement (AI system optimization and lifecycle)

AIMS Procedures Include:
- AI system procurement and acquisition procedures
- AI model development and training processes
- Bias detection and mitigation procedures
- Model transparency and explainability documentation
- Continuous performance monitoring and alerting
- Model retraining and lifecycle management
- AI system decommissioning and retirement

### Statement of Applicability Template

**Document:** 01_STATEMENT_OF_APPLICABILITY_TEMPLATE.md

The Statement of Applicability (SoA) provides a framework for documenting control applicability:

Purpose:
- Mark each EATGF control as applicable or not applicable
- Document justification for control exclusions
- Map controls to evidence artifacts
- Support audit readiness and preparation

Usage:
- Complete SoA before formal ISO audit
- Use as control-to-evidence traceability tool
- Share with external auditors and certification bodies
- Update when organization scope or risk profile changes

### Integration with Other Layers

Layer Relationships:

- **Layer 00 (Foundation):** MCM controls implemented via ISMS + AIMS procedures
- **Layer 02 (Control Architecture):** ISMS + AIMS procedures mapped to COBIT domains
- **Layer 03 (Governance Models):** ISMS/AIMS compliance measured against maturity model
- **Layer 04 (Policy Layer):** Formal policies operationalize ISMS + AIMS requirements
- **Layer 06 (Audit & Assurance):** Internal audits verify ISMS and AIMS compliance

## Control Mapping

### ISO 27001:2022 Alignment
- **Clause 4.4** – Determining the scope of the ISMS
- **Clause 5.1** – Leadership and commitment
- **Clause 5.2** – Information security policies
- **Clause 6.1** – Planning to address risks and opportunities
- **Clause 7.1** – Resources
- **Clause 8.1** – Operational planning and control

### ISO 42001:2023 Alignment
- **Clause 4.4** – Determining the scope of the AI management system
- **Clause 5.1** – Leadership and commitment to AI governance
- **Clause 6.1** – Planning for AI risk management
- **Clause 7.2** – Competence for AI governance
- **Clause 8.1** – AI system operational control
- **Clause 8.2** – Lifecycle management for AI systems

### COBIT 2019 Alignment
- **APO01** – Manage IT Management Framework (extends to AI/security)
- **BAI01** – Manage Programmes and Projects
- **DSS02** – Manage User Access
- **DSS03** – Manage Security
- **MEA02** – Monitor, Evaluate and Assess Compliance with Requirements

## Developer Checklist

Before implementing management systems:

- [ ] ISMS_MANUAL_v1.0.md reviewed and understood
- [ ] AIMS_MANUAL_v1.0.md reviewed and understood
- [ ] Statement of Applicability template obtained
- [ ] Organization scope documented (for ISMS and AIMS applicability)
- [ ] Risk assessment methodology defined
- [ ] Control implementation responsibilities assigned
- [ ] Evidence tracking procedures established
- [ ] Internal audit schedule defined for ISMS and AIMS

## Governance Implications

### Dual Management System Implementation

Organizations must implement both ISMS and  AIMS formal management systems. This includes:

- Establishing formal governance bodies for each system
- Documenting policies and procedures per ISO specifications
- Implementing control procedures across organization
- Maintaining evidence and records for audit demonstration
- Conducting internal audits and management reviews
- Pursuing external certification when strategic goals require

### Roles and Responsibilities

**ISMS Governance:**
- Information Security Manager – Responsible for ISMS operation
- CISO – Oversees information security governance
- Management Representative – Formal liaison between management and ISMS implementation

**AIMS Governance:**
- AI Governance Officer – Responsible for AIMS operation
- Chief AI Officer – Oversees AI governance strategy
- AI Ethics Committee – Ensures fairness and responsible AI practices

### Audit and Certification

ISMS Audits:
- Internal audits per ISO 19011:2018
- External certification audits by accredited certification bodies
- Annual surveillance and multi-year recertification audits

AIMS Audits:
- Internal audits per ISO 42001:2023
- External audits by ISO 42001 qualified auditors
- Continuous monitoring for AI-specific risks

## Official References

- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
- **ISO/IEC 27002:2022** – Information Security Code of Practice (2022)
- **ISO/IEC 42001:2023** – Artificial Intelligence Management Systems (2023)
- **ISO/IEC 19011:2018** – Guidelines for Auditing Management Systems (2018)
- **ISO/IEC 27005:2022** – Information Security Risk Management (2022)
- **Layer 04 (Policy Layer):** Policies are operationalized through ISMS + AIMS procedures
- **Layer 06 (Audit):** Audit program verifies ISMS + AIMS compliance

---

## 📊 Version & Status

**Framework Version:** EATGF-v1.0-Foundation  
**ISMS Version:** v1.0 (per ISO 27001:2022)  
**AIMS Version:** v1.0 (per ISO 42001:2023)  
**Status:** ✅ Complete & Audit Ready  
**Last Updated:** February 13, 2026
