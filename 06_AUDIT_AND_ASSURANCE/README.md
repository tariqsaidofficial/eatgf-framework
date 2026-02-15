# 06_AUDIT_AND_ASSURANCE

| Field | Value |
|-------|-------|
| Document Type | Layer Navigation & Overview |
| Version | 2.1 |
| Classification | Controlled |
| Effective Date | 2026-02-16 |
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

### Audit Schedule Standard

Document: AUDIT_SCHEDULE_STANDARD.md

Formal audit scheduling standard establishing:
- 5-quarter rolling audit cycle with phase-based execution (Phase 0 planning, Phases 1-3 quarterly execution, Phase 4 close-out)
- Control frequency classification matrix (Critical Annual 8-10 controls; High Annual 12-15 controls; Supporting Annual 10-15 controls; Quarterly Risk-Based 2-3 controls)
- Quarterly audit roadmap with specific controls, auditor assignments, and evidence collection timeline
- 12-month full control roadmap distributing all 35 MCM controls across audit year
- Audit resource planning (Chief Audit Officer, Audit Manager, Senior Auditors, Auditors; 7-8 FTE total; ~670 annual audit hours)
- Evidence requirements by control type (governance/operational/technology/assurance)
- Audit risk assessment for quarterly risk-based control selection
- Governance committee oversight with monthly dashboard and quarterly reports
- Annual plan approval and escalation trigger procedures

### Corrective Action Register Standard

Document: CORRECTIVE_ACTION_REGISTER_STANDARD.md

Formal CAR standard establishing:
- Data model for finding documentation (Master Finding fields: ID, date, source, control, category, severity, description, root cause)
- Remediation tracking fields (owner, plan, timeline, effort estimate, dependencies, status, % complete, progress updates)
- Closure procedures with evidence standards differentiated by finding type (Design Gap, Operational Defect, Compliance Miss)
- Severity classification matrix with timeline escalation (Critical ≤30 days; Major ≤60 days; Minor ≤90 days with approval authority differentiation)
- Finding entry procedure (5-day deadline post-discovery; CAO 10-day assessment)
- Remediation planning timelines (3-day for critical; 10-day for major; 15-day for minor)
- Monthly status updates required for all non-closed findings
- Monthly governance committee reporting (new findings, aging analysis, closure trends, systemic observations)
- Closure approval workflow (CAO evidence review → decision → critical findings require executive sponsorship)
- Reopened finding handling with additional remediation required
- Quarterly systemic analysis (control domain frequency, repeating findings, multi-control findings, time trends)

### Certification Readiness Checklist Standard

Document: CERTIFICATION_READINESS_CHECKLIST_STANDARD.md

Formal certification readiness standard establishing:
- 5-section checklist structure (Section A: Design Validation; Section B: Operation Readiness; Section C: Evidence Staging; Section D: Executive Certification; Section E: Exceptions)
- Section A design validation covering control definition, design documentation, procedures, training, governance
- Section B operation readiness covering execution evidence, SLA compliance, exception handling, monitoring, remediation of prior findings
- Sign-offs required at each section (control owner for A-C; executive for D on critical controls)
- Readiness status categories (Certified Ready; Partially Ready with documented gaps; Not Ready with audit implications)
- Pre-audit timeline (T-90 notification; T-60 work begins; T-30 draft; T-15 final; T-10 executive cosign)
- Evidence sufficiency standards for design, operation, training, monitoring, and exceptions
- Monthly certification status reporting with completion %, early cert %, evidence completeness %, executive cosign % metrics
- Escalation procedures (completion <90% one month before audit escalates to department heads; <75% two weeks before triggers deferral consideration)

### Evidence Governance Standard

Document: EVIDENCE_GOVERNANCE_STANDARD.md

Formal evidence governance standard establishing:
- Evidence classification by type with retention periods (audit 7-10 years; investigations 5-7 years; certifications 7 years; investigations 5-7 years; training 3 years; logs 90 days-2 years)
- Data classification levels (Public/Internal/Confidential/Restricted) with access and storage requirements
- Centralized evidence repository with folder structure, access controls, audit trail, version history, encryption
- Approved storage solutions (SharePoint, Google Drive, Records Management System, on-premises file server)
- Backup strategy with daily backups, geographic redundancy, recovery RTO 4 hours, annual restore testing
- Retention matrix differentiated by evidence type (Critical controls 10 years; Standard controls 7 years)
- Litigation hold procedure with Legal-initiated override of automatic deletion
- Access permission matrix by role (Auditors, Control Owners, CAO, CISO/Executive, Legal, External Auditors, Regulatory)
- Access logging and quarterly access audits by CAO
- Chain of custody for sensitive evidence with form, transfer tracking, storage logging
- Evidence protection controls (confidentiality: encryption AES-256 at rest; integrity: versioning and modification prevention; availability: backups and redundancy)
- Evidence disposal procedure (digital: 3x overwrite or key destruction; physical: certified shredding; verification required)
- Certificate of Destruction requirements with EID, date, method, verified by information
- Annual evidence audit with 10-20% sampling and verification of completeness, integrity, retention, classification, access

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

- [ ] INTERNAL_AUDIT_PROCEDURE_v1.0.md reviewed per ISO 19011:2018
- [ ] Auditor independence requirements established and documented
- [ ] Auditor competencies assessed; professional certifications verified
- [ ] AUDIT_SCHEDULE_STANDARD.md adopted with 5-quarter rolling cycle
- [ ] Quarterly audit roadmap published with control assignments and timeline
- [ ] Annual audit resource allocation planned (7-8 FTE; 670 hours)
- [ ] CORRECTIVE_ACTION_REGISTER_STANDARD.md system configured with data model
- [ ] CAR tracking tool or system implemented with status reporting dashboard
- [ ] Severity classification matrix and remediation timelines established
- [ ] CERTIFICATION_READINESS_CHECKLIST_STANDARD.md 5-section template distributed
- [ ] Control owner training on certification checklist process completed
- [ ] EVIDENCE_GOVERNANCE_STANDARD.md evidence repository established
- [ ] Evidence classification, retention matrix, and access permissions configured
- [ ] Litigation hold procedure and chain of custody process documented
- [ ] Governance council audit reporting and oversight structure established
- [ ] Annual audit effectiveness assessment scheduled

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
