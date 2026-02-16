# 02_CONTROL_ARCHITECTURE

| Field | Value |
|-------|-------|
| Document Type | Layer Navigation & Overview |
| Version | 2.0 |
| Classification | Controlled |
| Effective Date | 2026-02-14 |
| Authority | Enterprise Architecture and Governance Office |
| EATGF Layer | 02_CONTROL_ARCHITECTURE |

---

## Purpose

This layer defines the principles for how controls work, how they map across international standards, and how enterprise risk is assessed. It bridges control definitions (Layer 00) with formal management systems (Layer 01).

## Architectural Position

This layer operates within **02_CONTROL_ARCHITECTURE** as the definitive control alignment and mapping authority.

- **Upstream dependency:** Layer 00 (Foundation) defines MCM; Layer 01 implements through management systems
- **Downstream usage:** Layer 03 measures control maturity; Layer 06 audits against defined objectives
- **Cross-layer reference:** All layers reference control mappings for standards alignment

## Governance Principles

1. **Standards Alignment** – Every EATGF control maps to COBIT, ISO, NIST, and OWASP frameworks
2. **Control Effectiveness** – Measurable objectives define what successful control implementation means
3. **Risk-Based Governance** – Enterprise risk assessment drives control prioritization and enforcement
4. **Audit Defensibility** – Control mappings provide evidence for compliance with external standards
5. **Continuous Assessment** – Control effectiveness monitored and improved through formal audit program

## Technical Implementation

### Control Objectives Specification

Document: CONTROL_OBJECTIVES.md

Defines effectiveness criteria for all 35 MCM controls:
- Control objective and scope
- What success looks like (measurable criteria)
- Evidence requirements for audit demonstration
- Performance indicators and KPIs
- Audit reference points for compliance

### Framework Mappings

Document: FRAMEWORK_MAPPINGS.md

Cross-standard mapping matrix aligning EATGF to:
- COBIT 2019 (Information Technology governance domains)
- ISO 27001:2022 (Information Security Management System)
- NIST SP 800-53 Rev. 5 (Federal security standards)
- ISO 42001:2023 (Artificial Intelligence Management System)
- OWASP Top 10 (Web application security)

Mapping demonstrates how each EATGF control satisfies external standard requirements.

### Comprehensive Mapping with Justifications

Document: FRAMEWORK_MAPPINGS_COMPREHENSIVE_v2.md

Detailed justifications explaining:
- Why each EATGF control satisfies external standard requirements
- How controls map across multiple standards
- Audit trail for compliance verification
- Domain-by-domain detailed alignment

### Risk Framework and Assessment

Document: RISK_FRAMEWORK.md

Risk governance methodology aligned with ISO 31000:
- Risk assessment process and procedures
- Risk tolerance and appetite definition
- Mitigation strategies and controls
- Risk monitoring and reporting cadence
- Enterprise risk register structure

### Document Integration

Layer Relationships:
- **Layer 00 (Foundation):** Maps MCM controls to external standards
- **Layer 01 (Management Systems):** ISMS and AIMS implement controls defined here
- **Layer 03 (Governance Models):** Maturity and performance measured per control effectiveness
- **Layer 06 (Audit & Assurance):** Internal audit uses control objectives to assess effectiveness

## Control Mapping

### ISO 27001:2022 Alignment
- **Clause 5.1** – Leadership and commitment to information security
- **Clause 6.1** – Planning to address risks and opportunities
- **Clause 6.2** – Information security objectives and planning
- **Clause 8.1** – Operational planning and control
- **Clause 9.1** – Monitoring, measurement, analysis and evaluation

### NIST SSDF v1.1 Alignment
- **PO1.2** – Establish and maintain information and data security requirements
- **PO3.1** – Identify and maintain a consistent set of tools
- **PO3.2** – Document and enforce a versioning policy
- **PL1.1** – Assess processes for conducting security and threat modeling

### COBIT 2019 Alignment
- **EDM01** – Evaluate, Direct and Monitor the Establishment of Governance
- **APO01** – Manage the IT Management Framework
- **APO02** – Manage Strategy
- **APO03** – Manage Enterprise Architecture

## Developer Checklist

Before control implementation or audit:

- [ ] CONTROL_OBJECTIVES.md reviewed for all relevant controls
- [ ] FRAMEWORK_MAPPINGS reviewed for standards alignment
- [ ] RISK_FRAMEWORK methodology understood
- [ ] Control effectiveness criteria documented
- [ ] Evidence collection plan established
- [ ] Audit procedures defined per control objectives
- [ ] KPIs and performance indicators tracked
- [ ] Risk register established and monitored

## Governance Implications

### Control Ownership and Accountability

Each of the 35 MCM controls requires:
- Clear ownership assignment
- Documented control procedures
- Evidence collection and retention
- Periodic effectiveness assessment
- Improvement planning based on findings

### External Compliance Demonstration

Framework mappings provide evidence for:
- ISO 27001:2022 certification audits
- ISO 42001:2023 compliance assessment
- NIST SP 800-53 compliance reporting
- Regulatory audit requirements
- Third-party security assessments

### Risk Governance Authority

Framework Authority: Enterprise Architecture and Governance Office  
Risk Governance: Enterprise Risk Committee  
Control Oversight: Internal Audit Function

Changes to control architecture require formal approval and cross-standard impact assessment.

## Official References

- **NIST Special Publication 800-53 Rev. 5** – Security and Privacy Controls (2020)
- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
- **ISO/IEC 27002:2022** – Information Security Code of Practice (2022)
- **ISO 31000:2018** – Risk Management Framework (2018)
- **COBIT 2019** – Governance of Enterprise Information Technology (ISACA, 2019)
- **OWASP Top 10** – Application Security Framework (OWASP Foundation)

**Framework Version:** EATGF-v1.0-Foundation  
**Status:**  Complete  
**Audit Ready:** Yes  
**Last Updated:** February 13, 2026
