# ISMS_MANUAL_v1.0

**Enterprise AI-Aligned Technical Governance Framework**
(ISO/IEC 27001:2022 Aligned – Audit-Ready Structure)

---

**Document Type:** Information Security Management System Manual  
**Authority:** Board of Directors / Executive Steering Committee  
**Control Authority Reference:** MASTER_CONTROL_MATRIX.md (MCM v1.0 – Freeze Edition)

---

## 1. Purpose

This manual defines the Information Security Management System (ISMS) established by the organization in accordance with ISO/IEC 27001:2022 Clauses 4–10.

The ISMS:

- Protects confidentiality, integrity, and availability of information assets
- Integrates with EATGF Master Control Matrix
- Supports regulatory, contractual, and stakeholder requirements
- Provides structured risk-based security governance

**Note:** This manual does not reproduce ISO/IEC 27001 text. It defines the organization's implementation model.

---

## 2. Scope of the ISMS (Clause 4.3)

### 2.1 Organizational Scope

The ISMS applies to:

- All business units operating digital platforms
- All cloud, hybrid, and on-prem environments
- All employees, contractors, and third parties
- All IT, data, AI, API, and cloud systems

### 2.2 System Scope

**Included:**

- Production systems
- Development & CI/CD environments
- AI systems and data pipelines
- Cloud infrastructure (IaaS/PaaS/SaaS)
- API gateways
- Supporting governance systems

**Excluded (if applicable):**

- Systems explicitly listed in Scope Exclusion Register (controlled document)

Scope is reviewed annually under: **EATGF-MEA-MAT-01**

---

## 3. Context of the Organization (Clause 4)

### 3.1 Internal Issues

- Cloud-native architecture
- AI-enabled product capabilities
- DevSecOps operating model
- Distributed workforce

### 3.2 External Issues

- Regulatory obligations
- Data protection laws
- Client contractual security requirements
- Cyber threat landscape

### 3.3 Interested Parties

- Customers
- Regulators
- Shareholders
- Employees
- Partners
- Audit bodies

Interested party requirements are mapped into: **EATGF-APO-RISK-01 (Risk Register)**

---

## 4. Leadership (Clause 5)

### 4.1 Governance Structure

ISMS governance is defined by: **EATGF-EDM-GOV-01**

Roles include:

- Board of Directors
- Executive Steering Committee
- Chief Information Security Officer (CISO)
- Governance Council

### 4.2 Information Security Policy

Maintained under: **EATGF-APO-SEC-01**

Policy includes:

- Security objectives
- Risk-based commitment
- Continuous improvement commitment

### 4.3 Roles and Responsibilities

Defined in:

- Governance Charter
- RACI Matrix
- MCM Control Ownership Fields

---

## 5. Planning (Clause 6)

### 5.1 Risk Assessment Process (6.1.2)

Defined by: **EATGF-APO-RISK-01**

Includes:

- Risk identification
- Likelihood and impact scoring
- Heat map visualization
- Mitigation tracking

Risk criteria are derived from: **EATGF-EDM-RISK-01**

### 5.2 Risk Treatment Process (6.1.3)

Treatment options:

- Avoid
- Mitigate
- Transfer
- Accept

Controls selected from: **MASTER_CONTROL_MATRIX (MCM)**

Statement of Applicability derived from: **STATEMENT_OF_APPLICABILITY_TEMPLATE.md**

### 5.3 Information Security Objectives (6.2)

Objectives defined annually:

- Reduce critical vulnerabilities
- Maintain <X MTTR
- Zero high-risk audit findings
- Maintain SLA compliance

Performance tracked via: **EATGF-MEA-PERF-01**

---

## 6. Support (Clause 7)

### 6.1 Resources

Allocated annually through governance budgeting process.

### 6.2 Competence

Training records maintained. Security awareness program linked to: **EATGF-DSS-SEC-01**

### 6.3 Awareness

Mandatory security training for all personnel.

### 6.4 Communication

Internal and external communication protocols defined under: **EATGF-DSS-INC-01**

### 6.5 Documented Information (7.5)

All ISMS documents:

- Version controlled
- Stored in centralized repository
- Retained minimum 7 years
- Reviewed annually

---

## 7. Operation (Clause 8)

### 7.1 Operational Planning & Control

Operational controls implemented through:

| Area | Control Reference |
|------|-------------------|
| Change Management | EATGF-BAI-CHG-01 |
| Configuration | EATGF-BAI-CONF-01 |
| QA & Testing | EATGF-BAI-TEST-01 |
| IAM | EATGF-DSS-SEC-01 |
| Encryption | EATGF-DSS-ENC-01 |
| Vulnerability Mgmt | EATGF-DSS-VULN-01 |
| Incident Response | EATGF-DSS-INC-01 |
| DevSecOps | EATGF-DEV-* |
| Cloud Governance | EATGF-CLD-* |
| BCP | EATGF-BCP-* |
| Data Privacy | EATGF-DATA-* |

### 7.2 Secure Development

Governed by:

- DEV-SDLC-01
- DEV-SCAN-01
- DEV-SUP-01
- DEV-CI-01

---

## 8. Performance Evaluation (Clause 9)

### 8.1 Monitoring & Measurement

Governed by: **EATGF-MEA-PERF-01**

Metrics include:

- DORA metrics
- Vulnerability remediation time
- Incident response time
- Audit finding closure rate

### 8.2 Internal Audit

Governed by: **EATGF-MEA-AUD-01**

- Annual audit program
- Independent reviewers
- Findings tracked to closure

### 8.3 Management Review

- Quarterly governance council review
- Annual board review

---

## 9. Improvement (Clause 10)

### 9.1 Nonconformity & Corrective Action

Incident root cause analysis: **EATGF-DSS-INC-01**

Audit findings remediation: **EATGF-MEA-AUD-01**

### 9.2 Continual Improvement

Driven by:

- Maturity assessments
- Risk trend analysis
- Post-incident reviews
- Regulatory updates

---

## 10. Annex – Linkage to Master Control Matrix

The ISMS does not duplicate controls.

All technical and governance controls are defined exclusively in:

**`/controls/MASTER_CONTROL_MATRIX.md`**

The MCM serves as:

- Control authority
- SoA foundation
- Audit reference index

Any control modification requires:

- Governance Council approval
- Version increment
- Impact review on SoA

---

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | Draft – Pending Governance Approval |
| **Last Updated** | February 13, 2026 |
| **Next Review** | Formal Review & Approval Cycle |
| **Owner** | Chief Information Security Officer |
| **Approver** | Board of Directors / Executive Steering Committee |
