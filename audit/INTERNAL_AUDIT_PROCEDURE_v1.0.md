# INTERNAL_AUDIT_PROCEDURE_v1.0

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**

Aligned with ISO/IEC 27001:2022 – Clause 9.2  
Aligned with ISO/IEC 42001:2023 – Clause 9  
Guided by ISO 19011:2018

---

**Document Type:** Internal Audit Procedure  
**Authority:** Audit Committee (Board Level)  
**Control Reference:** EATGF-MEA-AUD-01  
**Control Authority:** MASTER_CONTROL_MATRIX.md (MCM v1.0)

---

## 1. Purpose

This procedure defines the internal audit framework for:

- Information Security Management System (ISMS)
- Artificial Intelligence Management System (AIMS)
- Master Control Matrix (MCM) governance controls

It ensures:

- Conformity to ISO/IEC 27001
- Conformity to ISO/IEC 42001
- Effectiveness of governance controls
- Continuous improvement

---

## 2. Scope

**Covers:**

- All 35 controls in MASTER_CONTROL_MATRIX.md
- ISMS clauses 4–10
- AIMS clauses 4–10
- AI lifecycle governance
- Cloud / DevSecOps / Privacy / BCP controls

**Applies to:**

- All business units
- All technology environments
- All AI systems in scope

---

## 3. Audit Governance Structure

### 3.1 Authority

Audit authority derives from: **EATGF-MEA-AUD-01**

Oversight by:

- Audit Committee (Board Level)
- Executive Steering Committee

### 3.2 Auditor Independence Model

Auditors must:

- Not audit their own work
- Not report to operational control owners
- Be independent of reviewed domain

**Permitted models by organization size:**

| Organization Size | Audit Model |
|-------------------|-------------|
| Startup | External consultant |
| SaaS | Internal cross-functional team |
| Enterprise | Dedicated internal audit function |

---

## 4. Audit Types

### 4.1 Management System Audit

**Frequency:** Annual

**Covers:**

- ISMS full lifecycle
- AIMS full lifecycle
- Risk treatment effectiveness
- Policy adherence

### 4.2 Control-Based Audit

**Frequency:** Quarterly sampling

**Covers:**

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

| Severity | Definition |
|----------|-----------|
| **Critical** | Control failure causing material risk |
| **Major** | Control partially implemented or ineffective |
| **Minor** | Isolated deviation |
| **Observation** | Improvement opportunity |

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

| Domain | Minimum Frequency |
|--------|-------------------|
| EDM | Annual |
| APO | Annual |
| BAI | Quarterly sampling |
| DSS | Quarterly |
| MEA | Annual |
| AI Controls | Per model release + Annual |
| Cloud Controls | Annual |
| DevSecOps | Quarterly |
| BCP | Annual test review |

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

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | Draft – Pending Governance Approval |
| **Last Updated** | February 13, 2026 |
| **Next Review** | Formal Review & Approval Cycle |
| **Owner** | Chief Audit Officer / Internal Audit Function |
| **Approver** | Audit Committee (Board Level) |
| **Related Procedures** | EATGF-MEA-AUD-01 (MCM) |
| **Framework References** | ISO 19011:2018, ISO 27001:2022, ISO 42001:2023 |
