# Framework Mappings

## Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field | Value |
|-------|-------|
| Document Type | Reference |
| Version | 2.0 |
| Classification | Internal |
| Effective Date | 2026-02-14 |
| Baseline | COBIT 2019, ISO 27001:2022, ISO 42001:2023, ISO 38500:2015, OWASP API Top 10:2023 |
| Authority | Enterprise Architecture & Governance Office |
| MCM Reference | All 35 EATGF Controls |

---

## 1. Purpose

This document defines the mappings between EATGF controls and the external standards, frameworks, and industry benchmarks from which they derive authority. All control IDs follow the authoritative `EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]` taxonomy as defined in the Master Control Matrix.

---

## 2. COBIT 2019 to ISO 38500 Mapping

| COBIT Domain | COBIT Process | ISO 38500 Principle |
|-------------|------|----------|
| EDM | EDM01 — Evaluate and direct IT governance | Board responsibility |
| EDM | EDM02 — Ensure benefits realisation | Value delivery |
| APO | APO01 — Manage the IT management framework | Strategic alignment |
| APO | APO02 — Manage strategy | Strategy execution |
| BAI | BAI01 — Manage programs and projects | Risk management |
| BAI | BAI02 — Manage requirements definition | Compliance |
| DSS | DSS01 — Manage operations | Human resources |
| DSS | DSS02 — Manage service requests | Compliance |
| MEA | MEA01 — Monitor, evaluate, and assess performance | Performance measurement |
| MEA | MEA02 — Monitor, evaluate, and assess the system of internal control | Control monitoring |

---

## 3. EATGF Controls to ISO 27001:2022 Mapping

| EATGF Control | ISO 27001 Control | Description |
|-------------|--------|----------|
| EATGF-DSS-SEC-01 (IAM) | A.9.1, A.9.2 | Access control policies and implementation |
| EATGF-DSS-ENC-01 (Encryption) | A.10.1, A.10.2 | Cryptography standards |
| EATGF-DSS-VULN-01 (Vuln Mgmt) | A.12.6 | Management of technical vulnerabilities |
| EATGF-APO-ARCH-01 (Architecture) | A.12.1 | Secure development and operations |
| EATGF-DSS-INC-01 (Incident Response) | A.16.1 | Incident management |
| EATGF-APO-RISK-01 (Risk Assessment) | A.12.6.1 | Risk evaluation |
| EATGF-APO-SEC-01 (ISMS) | A.5 — A.18 | Information security management system |
| EATGF-DEV-SDLC-01 (Secure SDLC) | A.14.2 | Security in development and support processes |
| EATGF-DEV-SCAN-01 (Code Scanning) | A.14.2.8 | System security testing |
| EATGF-DATA-PRIV-01 (DPIA) | A.18.1.4 | Privacy and protection of PII |

### ISO 27001 Control Set Coverage

**Fully Covered:** A.5 — A.16 (Core security controls)
**Partially Covered:** A.4 (Organization controls)
**Reference:** A.1 — A.3 (Context controls)

---

## 4. EATGF Controls to ISO 42001:2023 Mapping

| EATGF Control | ISO 42001 Section | Purpose |
|-------------|--------|----------|
| EATGF-AI-LC-01 | Section 6 | AI system lifecycle governance |
| EATGF-AI-RISK-01 | Section 8.1 | AI risk assessment and bias management |
| EATGF-DSS-ENC-01 | Section 8.2 | AI data protection |
| EATGF-APO-ARCH-01 | Section 6.1 | AI system architecture |
| EATGF-MEA-PERF-01 | Section 7 | AI performance metrics |
| EATGF-MEA-AUD-01 | Section 9 | AI control effectiveness |
| EATGF-APO-AI-01 | Section 4 — 10 | AI management system (full AIMS) |

### ISO 42001 Domains Addressed

- AI governance and management
- AI system development and deployment
- AI risk and impact management
- Data governance for AI systems
- Transparency and explainability

---

## 5. EATGF Controls to OWASP API Security Top 10:2023 Mapping

| EATGF Control | OWASP Category | Implementation |
|-------------|--------|----------|
| EATGF-API-LC-01 (Design) | API1:2023 — Broken Object Level Authorization | API design standards prevent direct object access |
| EATGF-API-SEC-01 (Security) | API2:2023 — Broken Authentication | Authentication and authorization controls |
| EATGF-API-SEC-01 | API3:2023 — Broken Object Property Level Authorization | RBAC with field-level controls |
| EATGF-API-SEC-01 | API4:2023 — Unrestricted Resource Consumption | Rate limiting and quota management |
| EATGF-API-SEC-01 | API5:2023 — Broken Function Level Authorization | Function-level access controls |
| EATGF-API-SEC-01 | API6:2023 — Unrestricted Access to Sensitive Business Flows | Business logic protection |
| EATGF-API-SEC-01 | API7:2023 — Server-Side Request Forgery | Input validation and allowlists |
| EATGF-API-SEC-01 | API8:2023 — Security Misconfiguration | Configuration standards |
| EATGF-API-LC-01 | API9:2023 — Improper Inventory Management | API inventory control |
| EATGF-API-SEC-01 | API10:2023 — Unsafe Consumption of APIs | Third-party API validation |

---

## 6. Governance Framework Alignment Architecture

```
+--------------------------------------------------------------+
|              Enterprise AI-Aligned Technical                  |
|              Governance Framework (EATGF)                     |
|                35 Controls - 11 Domains                       |
+------+----------+----------+----------+-----------+-----------+
       |          |          |          |           |
   +---v---+  +---v---+  +--v----+  +-v------+  +-v------+
   | COBIT |  |  ISO  |  |  ISO  |  | OWASP  |  |  NIST  |
   | 2019  |  | 38500 |  | 27001 |  | API    |  | AI RMF |
   |(Core) |  |(Corp) |  | (Sec) |  |Top 10  |  |        |
   +---+---+  +---+---+  +---+---+  +---+----+  +---+----+
       |          |          |          |           |
       +----------+----------+----------+-----------+
                      |
          +-----------+-----------+
          |           |           |
      +---v--+    +---v--+   +---v--+
      | ISO  |    | Risk |   | KPI  |
      |42001 |    |Model |   |Model |
      | (AI) |    |      |   |      |
      +------+    +------+   +------+
```

---

## 7. EATGF Control Coverage by Source Framework

### COBIT 2019 Coverage

| Domain | Total Processes | EATGF Controls Mapped | Coverage |
|--------|---------|-------------|----------|
| EDM (Evaluate, Direct, Monitor) | 4 | EATGF-EDM-RISK-01, EATGF-EDM-BEN-01, EATGF-EDM-GOV-01 | 75% |
| APO (Align, Plan, Organize) | 13 | EATGF-APO-ARCH-01, EATGF-APO-RISK-01, EATGF-APO-SEC-01, EATGF-APO-AI-01 | 31% |
| BAI (Build, Acquire, Implement) | 10 | EATGF-BAI-CHG-01, EATGF-BAI-CONF-01, EATGF-BAI-TEST-01 | 30% |
| DSS (Deliver, Service, Support) | 6 | EATGF-DSS-SEC-01, EATGF-DSS-ENC-01, EATGF-DSS-VULN-01, EATGF-DSS-INC-01 | 67% |
| MEA (Monitor, Evaluate, Assess) | 4 | EATGF-MEA-AUD-01, EATGF-MEA-PERF-01, EATGF-MEA-MAT-01 | 75% |

### ISO 27001:2022 Coverage

| Annex | Metrics | Coverage |
|-------|---------|----------|
| A.5 — Organizational Controls | 2/2 Controls | 100% |
| A.6 — Personnel Security | 3/3 Controls | 100% |
| A.7 — Asset Management | 2/2 Controls | 100% |
| A.8 — Access Control | 8/8 Controls | 100% |
| A.9 — Cryptography | 2/2 Controls | 100% |
| A.10 — Physical and Environmental | 3/3 Controls | 50% |
| A.11 — Operations Security | 7/7 Controls | 100% |
| A.12 — Communications Security | 7/7 Controls | 100% |
| A.13 — System Acquisition | 5/5 Controls | 100% |
| A.14 — Supplier Relationships | 3/3 Controls | 100% |
| A.15 — Information Security Incident | 5/5 Controls | 100% |
| A.16 — Business Continuity | 2/2 Controls | 50% |

---

## 8. Standard Selection by Governance Edition

### Startup Edition (1-10 personnel)

**Applicable Standards:**
- COBIT 2019 (Lightweight subset)
- ISO 27001 (Core categories only)
- ISO 38500 (Strategic guidance)
- ISO 42001 (Conditional — only if AI systems exist)
- OWASP (Conditional — only if APIs exposed)

**Focus Controls:**
1. EATGF-DSS-SEC-01 — Identity and access management
2. EATGF-DSS-VULN-01 — Vulnerability management
3. EATGF-APO-RISK-01 — Risk register management
4. EATGF-DSS-ENC-01 — Data encryption

---

### SaaS Edition (10-50 personnel)

**Applicable Standards:**
- COBIT 2019 (Full framework)
- ISO 27001 (Complete)
- ISO 38500 (Full implementation)
- ISO 42001 (Conditional — if AI systems exist)
- OWASP (Full compliance)

**Focus Controls:**
1. All Startup Edition controls
2. EATGF-AI-LC-01 — AI system lifecycle
3. EATGF-AI-RISK-01 — AI risk and bias management
4. EATGF-API-SEC-01 — API security
5. EATGF-API-LC-01 — API lifecycle management
6. EATGF-MEA-PERF-01 — Performance monitoring

---

### Enterprise Edition (50+ personnel)

**Applicable Standards:**
- COBIT 2019 (Complete)
- ISO 27001 (Complete with extended controls)
- ISO 38500 (Complete with board alignment)
- ISO 42001 (Full with AI expertise)
- OWASP (Advanced with threat modeling)

**Focus Controls:**
1. All 35 EATGF controls fully implemented
2. Advanced AI governance (EATGF-AI-LC-01, EATGF-AI-RISK-01)
3. Complex API ecosystems (EATGF-API-SEC-01, EATGF-API-LC-01)
4. Enterprise risk management (EATGF-EDM-RISK-01, EATGF-APO-RISK-01)
5. Continuous optimization (EATGF-MEA-MAT-01)

---

## 9. Mapping Update Schedule

| Framework | Version | Last Updated | Next Review |
|-----------|---------|-------------|------------|
| COBIT | 2019 | Feb 2026 | Aug 2026 |
| ISO 38500 | 2015 | Feb 2026 | Aug 2026 |
| ISO 27001 | 2022 | Feb 2026 | Aug 2026 |
| ISO 42001 | 2023 | Feb 2026 | Aug 2026 |
| OWASP API Security | 2023 | Feb 2026 | Feb 2027 |

---

## 10. Governance Enforcement Rules

1. All mapping tables in this document reference the EATGF control taxonomy as defined in the Master Control Matrix. Legacy identifiers (AC-01, SEC-01, etc.) are superseded.
2. Mapping updates require governance review when a source framework publishes a new edition.
3. Coverage percentages are recalculated during annual framework mapping reviews.

---

**Document Control**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-01 | Governance Office | Initial framework mappings with 14 legacy controls |
| 2.0 | 2026-02-14 | Enterprise Architecture & Governance Office | Adopted EATGF-xxx taxonomy; expanded to 35 controls; corrected ISO 42001 to 2023; added EATGF header; removed placeholder content |

**Authority Sign-Off**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Chief Governance Officer | | | |
| Enterprise Architect | | | |
