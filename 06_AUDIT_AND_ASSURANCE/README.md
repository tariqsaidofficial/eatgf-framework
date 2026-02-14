# 06_AUDIT_AND_ASSURANCE

| Field | Value |
|-------|-------|
| Document Type | Layer Navigation & Overview |
| Version | 2.0 |
| Classification | Controlled |
| Effective Date | 2026-02-14 |
| Authority | Chief Audit Officer and Internal Audit Function |
| EATGF Layer | 06_AUDIT_AND_ASSURANCE |

---

## Purpose

This layer defines the internal audit methodology for independently assessing compliance with EATGF controls across the organization. It ensures auditor objectivity and drives continuous governance improvement through formal audit processes.

## Architectural Position

This layer operates within **06_AUDIT_AND_ASSURANCE** as the independent assurance authority for governance.

- **Upstream dependency:** Layers 00-05 describe what is being audited
- **Downstream usage:** Audit findings inform improvement in Layers 00-05
- **Cross-layer reference:** All control compliance assessed against audit procedures

## Governance Principles

1. **Auditor Independence** – Auditors independent from audit subject; reporting to governance authority
2. **Comprehensive Coverage** – Annual audit cycle covers all 35 MCM controls
3. **Professional Discipline** – Audits conducted per ISO 19011:2018 standards
4. **Evidence-Based Assessment** – Audit findings based on documented evidence and objective testing
5. **Continuous Improvement** – Audit findings drive systematic corrective actions and enhancements

## Technical Implementation

### Internal Audit Methodology

Document: INTERNAL_AUDIT_PROCEDURE_v1.0.md

Audit methodology per ISO 19011:2018:

Annual Full Audit (Q1):
- Comprehensive assessment of all 35 MCM controls
- Detailed control testing and evidence collection
- Executive summary and detailed audit report
- Findings and corrective action recommendations

Quarterly Sampling Audits (Q2-Q4):
- Rolling sample of 10-15 controls per quarter
- Risk-based selection of controls to test
- Focused testing on high-risk or critical controls
- Summary report and findings tracking

Thematic Audits (ad-hoc):
- Risk-based focus on specific governance areas
- Response to significant findings or changes
- Compliance verification for new initiatives
- Executive steering committee direction

Auditor Qualifications:
- Professional certifications (CIA, CISA, or equivalent)
- EATGF framework knowledge and training
- Internal audit methodology expertise
- Information security domain knowledge

Audit Independence Requirements:
- Auditors independent from audited functions
- Reporting line directly to governance authority
- Cannot audit own areas of responsibility
- Maintain confidentiality of audit information
- Apply impartial professional judgment

Audit Execution Procedures:
- Audit planning and preparation
- Auditable unit understanding and risk assessment
- Fieldwork and evidence collection
- Finding documentation and impact rating
- Auditor communication and follow-up

### Findings and Corrective Action

Audit Finding Management:
- Classification: Critical, High, Medium, Low
- Root cause analysis for significant findings
- Corrective action planning and assignment
- Executive accountability for resolution
- Closure verification and follow-up

Finding Tracking:
- Audit finding register maintained
- Status tracking to closure
- Management response and remediation evidence
- Closure verification by auditors
- Trend analysis and reporting

### Audit Reporting and Communication

Audit Communications:
- Post-audit management conference
- Formal audit report to governance council
- Executive summary for senior leadership
- Detailed findings for control owners
- Aggregate governance effectiveness report

Management Review:
- Governance council review of audit findings
- Resource allocation for corrective actions
- Executive sponsorship for remediation
- Process improvement initiatives
- Governance effectiveness assessment

### Audit Schedule

Annual Audit Cycle:
- Q1 (Jan-Mar): Full audit of all 35 controls
- Q2 (Apr-Jun): Quarterly sampling audit
- Q3 (Jul-Sep): Quarterly sampling audit
- Q4 (Oct-Dec): Quarterly sampling audit

Plus thematic audits as risk-based and approved by governance council.

Management review and reporting:
- Fortnightly finding updates
- Monthly management dashboard
- Quarterly governance council reports
- Annual effectiveness assessment

## Control Mapping

### ISO 19011:2018 Alignment
- **Clause 5.2** – Auditor competence (qualifications and training)
- **Clause 6.1** – Audit planning and preparation
- **Clause 6.3** – Auditor independence and impartiality
- **Clause 7.6** – Follow-up audits and corrective action verification

### ISO 27001:2022 Alignment
- **Clause 9.2** – Internal audit (audit planning, execution, reporting)
- **Clause 10.2** – Nonconformity and corrective action (management response)
- **Clause 10.3** – Continual improvement (improvement from audit findings)

### COBIT 2019 Alignment
- **MEA01** – Monitor, Evaluate and Assess Conformance with External Requirements
- **MEA02** – Monitor, Evaluate and Assess System of Internal Control
- **MEA03** – Monitor, Evaluate and Assess Governance

## Developer Checklist

Before audit implementation:

- [ ] Internal audit procedure reviewed and understood
- [ ] Auditor independence requirements established
- [ ] Auditor competencies assessed and training planned
- [ ] Annual audit schedule published
- [ ] Audit evidence requirements documented
- [ ] Findings tracking and closure procedures established
- [ ] Governance council audit reporting established
- [ ] Corrective action process defined

## Governance Implications

### Audit Governance Authority

Chief Audit Officer – Independent audit authority  
Internal Audit Function – Execution and administration  
Governance Council – Oversight and resource authorization  
Control Owners – Corrective action accountability

Auditor independence maintained through:
- Direct reporting to governance council, not operations
- Separate budget and resource authority
- Annual audit plan approved by governance council
- Executive protection of auditor independence

### Corrective Action Accountability

Control owners assigned accountability for:
- Timely response to audit findings
- Root cause analysis and corrective action planning
- Resource allocation for remediation
- Timeline adherence for closure
- Quality of corrective actions

### Continuous Improvement Cycle

Audit findings inform improvement:
- Control procedure enhancements
- Policy clarifications and updates
- Process standardization
- Technology and automation investments
- Training and capability development

## Official References

- **ISO/IEC 19011:2018** – Guidelines for Auditing Management Systems (2018)
- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
- **ISO/IEC 27002:2022** – Information Security Code of Practice (2022)
- **COBIT 2019** – Governance of Enterprise Information Technology (ISACA, 2019)
- **The IIA Standards** – Institute of Internal Auditors, International Professional Practices Framework
