# Internal Audit Procedure v1.0

Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field          | Value                         |
| -------------- | ----------------------------- |
| Document Type  | Internal Audit Procedure      |
| Version        | 1.1                           |
| Classification | Controlled                    |
| Effective Date | 2026-02-15                    |
| Authority      | Audit Committee (Board Level) |
| EATGF Layer    | 06_AUDIT_AND_ASSURANCE        |
| MCM Reference  | EATGF-MEA-AUD-01              |

---

## Purpose

This procedure defines the internal audit framework for validating conformity to the EATGF governance framework and the effectiveness of all 35 controls defined in the Master Control Matrix (MCM). It ensures:

- Compliance with ISO/IEC 27001:2022 Clause 9.2 (Internal Audit)
- Compliance with ISO/IEC 42001:2023 Clause 9 (Performance Evaluation)
- Continuous effectiveness monitoring of governance controls
- Evidence collection for certification bodies (ISO, SOC 2, etc.)
- Audit defensibility of control implementation

---

## Architectural Position

This document operates within **06_AUDIT_AND_ASSURANCE** as the implementation procedure for control EATGF-MEA-AUD-01.

- **EATGF Layer Placement:** 06_AUDIT_AND_ASSURANCE
- **Governance Scope:** Audit Methodology (Implementation Standard)
- **Control Authority Relationship:** Implements control EATGF-MEA-AUD-01 as defined in the MCM

**Upstream dependency:** Master Control Matrix (Layer 00) defines control EATGF-MEA-AUD-01 with audit scope, frequency, and evidence requirements.
**Downstream usage:** Internal audit is conducted by dedicated audit function or external consultants per procedure herein.
**Cross-layer reference:** All Layer 01-08 documents are subject to internal audit verification that their implementations conform to MCM controls.

## Governance Principles

1. **Audit Traceability** -- All audits scope directly from the MCM's 35 controls. No alternative audit scope is authorized.
2. **Audit Independence** -- Internal auditors must not audit their own work. Organizational structure prevents audit-function personnel from managing operational controls they would audit.
3. **Evidence-Based Audit** -- Audit findings are substantiated by documented evidence, control test results, and observable practices. Subjective "observations" are not acceptable audit findings.
4. **Control-Domain Integrity** -- Audits verify both the existence of controls and their effectiveness within their COBIT domain context.
5. **Continuous Assurance** -- Audit is not a point-in-time assessment. Organizations maintain ongoing control monitoring with periodic deep audits.

---

## Aligned Standards

Aligned with ISO/IEC 27001:2022 – Clause 9.2 (Internal Audit)
Aligned with ISO/IEC 42001:2023 – Clause 9 (Performance Evaluation)
Guided by ISO 19011:2018 (Guidelines for auditing management systems)

---

- Selected MCM controls
- Evidence validation
- Residual risk review

### 4.3 Thematic Audit

**Triggered by:**

- Major incident
- Regulatory change
- New AI deployment
- Cloud architecture redesign

---

## 5. Audit Program Planning (ISO 19011 Alignment)

Annual audit plan must define:

- Scope
- Criteria
- Frequency
- Methods
- Assigned auditors
- Reporting deadlines

**Audit criteria include:**

- ISO 27001 requirements
- ISO 42001 requirements
- MCM control definitions
- Internal policies

---

## 6. Audit Execution Process

### Step 1 – Preparation

- Define audit objective
- Select applicable MCM controls
- Notify control owners
- Request preliminary evidence

### Step 2 – Evidence Review

**Evidence types:**

- Document-based
- System-based
- Process-based
- Assessment-based

**Evidence must be:**

- Verifiable
- Current
- Traceable to control ID

### Step 3 – Interviews

Interview:

- Control owner
- Evidence owner
- Governance representative (if needed)

Validate:

- Practical implementation
- Control effectiveness
- Awareness level

### Step 4 – Testing

Where applicable:

- Sample change tickets
- Sample access reviews
- Sample vulnerability remediation
- Sample AI bias reports
- Sample cloud monitoring logs

---

## 7. Audit Findings Classification

| Severity        | Definition                                   |
| --------------- | -------------------------------------------- |
| **Critical**    | Control failure causing material risk        |
| **Major**       | Control partially implemented or ineffective |
| **Minor**       | Isolated deviation                           |
| **Observation** | Improvement opportunity                      |

**Each finding must include:**

- Control ID reference
- Evidence reference
- Root cause
- Risk impact
- Corrective action deadline
- Responsible owner

---

## 8. Reporting

**Audit report must include:**

- Scope
- Methodology
- Controls assessed
- Findings summary
- Overall maturity rating
- Residual risk trend

**Report issued within:** 14 calendar days of audit completion

**Submitted to:**

- Governance Council
- Executive Steering Committee
- Audit Committee (if critical findings)

---

## 9. Corrective Action Management

All findings must:

- Be logged in Corrective Action Register
- Have assigned owner
- Have deadline
- Be verified for closure

**Linked to:** EATGF-MEA-PERF-01

Closure verification required before status marked resolved.

---

## 10. Audit Frequency Matrix

| Domain         | Minimum Frequency          |
| -------------- | -------------------------- |
| EDM            | Annual                     |
| APO            | Annual                     |
| BAI            | Quarterly sampling         |
| DSS            | Quarterly                  |
| MEA            | Annual                     |
| AI Controls    | Per model release + Annual |
| Cloud Controls | Annual                     |
| DevSecOps      | Quarterly                  |
| BCP            | Annual test review         |

---

## 11. Records & Retention

**Audit records retained:**

- **Minimum:** 7 years
- **Location:** Central Evidence Repository
- **Access:** Restricted

**Records include:**

- Audit plan
- Working papers
- Evidence samples
- Interview notes
- Final report
- Corrective action log

---

## 12. Integration with ISMS & AIMS

This procedure satisfies:

- **ISO 27001 Clause 9.2** – Internal Audit
- **ISO 42001 Clause 9** – Performance Evaluation
- **MCM Control:** EATGF-MEA-AUD-01

No duplication of control text.

MCM remains control authority.

---

## Control Mapping

| EATGF Context              | ISO 27001:2022                      | NIST SSDF                                   | OWASP                | COBIT                                              |
| -------------------------- | ----------------------------------- | ------------------------------------------- | -------------------- | -------------------------------------------------- |
| Internal Audit Framework   | Clause 9.2 (Internal Audit)         | RV.1 (Identify and Confirm Vulnerabilities) | SAMM Verification    | MEA02 (Monitor, Evaluate, Assess Internal Control) |
| Audit Scope Determination  | Clause 6.1.2 (Risk assessment)      | PO.1 (Define Security Requirements)         | SAMM Governance      | APO13 (Manage Security and Privacy)                |
| Audit Evidence Collection  | Clause 8.1 (General competence)     | PW.1 (Design Software)                      | Testing Requirements | MEA01 (Monitor, Evaluate, Assess Performance)      |
| Corrective Action Tracking | Clause 10.2 (Continual improvement) | RV.2 (Analyze Maturity)                     | Risk Remediation     | MEA02 (Assess Control Effectiveness)               |

---

## Developer Checklist

- [ ] Schedule annual management system audit (ISMS + AIMS)
- [ ] Plan quarterly sampling audits of highest-risk controls (BAI, DSS, DevSecOps domains)
- [ ] Assign independent auditors (external or internal auditor function, not operational staff)
- [ ] Define audit evidence requirements for each control before audit begins
- [ ] Document all audit findings with specific evidence (not subjective observations)
- [ ] Log all findings in Corrective Action Register with owner assignment and deadline
- [ ] Verify corrective actions are implemented and evidence collected
- [ ] Report audit results to Audit Committee quarterly
- [ ] Maintain audit records for minimum 7 years per compliance requirements

---

## Governance Implications

**Risk if not implemented:** Without formal internal audit, control effectiveness is unverified. Compliance claims lack evidence. External auditors will cite lack of internal audit process as a finding.

**Operational impact:** Internal audit is cost-intensive (staffing or external consultants). However, absence of audit results in failed certifications, delayed sales cycles, and reputational damage.

**Audit consequences:** Absence of internal audit is a non-conformity finding under ISO 27001 Clause 9.2 and ISO 42001 Clause 9. External certification bodies will refuse to certify without internal audit evidence.

**Cross-team dependencies:** Internal audit requires access to all operational teams, infrastructure, source code, and change records. Audit function must be independent of operational control owners (no conflicts of interest).

---

## Official References

- ISO/IEC 27001:2022 -- Information security management system (Clause 9.2: Internal Audit)
- ISO/IEC 42001:2023 -- Artificial intelligence management system (Clause 9: Performance Evaluation)
- ISO 19011:2018 -- Guidelines for auditing management systems
- COBIT 2019 -- MEA domain (Monitor, Evaluate, Assess)

---

## Document Control

| Field                    | Value                                           |
| ------------------------ | ----------------------------------------------- |
| **Version**              | 1.1                                             |
| **Change Type**          | Structural Conformance (Template Applied)       |
| **Status**               | Conformant to EATGF Document Signature Template |
| **Last Updated**         | February 15, 2026                               |
| **Next Review**          | August 2026 or upon material changes to MCM     |
| **Owner**                | Chief Audit Officer / Internal Audit Function   |
| **Approver**             | Audit Committee (Board Level)                   |
| **Related Procedures**   | EATGF-MEA-AUD-01 (MCM)                          |
| **Framework References** | ISO 19011:2018, ISO 27001:2022, ISO 42001:2023  |
