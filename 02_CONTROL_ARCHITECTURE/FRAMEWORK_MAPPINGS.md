# FRAMEWORK_MAPPINGS

| Field          | Value                                         |
| -------------- | --------------------------------------------- |
| Document Type  | Control Architecture Reference                |
| Version        | 2.0                                           |
| Classification | Controlled                                    |
| Effective Date | 2026-02-14                                    |
| Authority      | Enterprise Architecture and Governance Office |
| EATGF Layer    | 02_CONTROL_ARCHITECTURE                       |
| MCM Reference  | All 35 EATGF Controls                         |

---

## Purpose

This document defines authoritative mappings between EATGF's 35 controls and external governance frameworks including COBIT 2019, ISO 27001:2022, ISO 42001:2023, ISO 38500:2015, and OWASP API Security Top 10:2023. Mappings establish audit defensibility by demonstrating EATGF control alignment to industry standards. All control references use official EATGF-[DOMAIN]-[CATEGORY]-[NUMBER] taxonomy as defined in Master Control Matrix.

## Architectural Position

This document operates within **02_CONTROL_ARCHITECTURE** as the authoritative cross-framework mapping reference.

- **Upstream dependency:** Master Control Matrix (MCM) establishes 35 controls as single source of truth
- **Downstream usage:** Utilized by ISMS/AIMS procedures (Layer 01), audit procedures (Layer 06), and Statement of Applicability documentation
- **Cross-layer reference:** Supports Layer 04 policy implementation by mapping policies to international standards; enables Layer 06 audit procedures through control traceability

## Governance Principles

1. **Standards Alignment** – EATGF controls map to multiple international standards demonstrating comprehensive governance coverage
2. **Single Source of Truth** – Master Control Matrix is authoritative control definition; this document provides secondary mapping references only
3. **Audit Defensibility** – Explicit mappings to ISO, COBIT, and OWASP provide audit trail for compliance assertions
4. **Edition Scalability** – Startup, SaaS, and Enterprise editions select appropriate standard subsets based on organizational maturity
5. **Living Document** – Mappings updated when source frameworks publish new editions; annual review cycle maintains currency

## Technical Implementation

### COBIT 2019 to ISO 38500 Mapping

COBIT domains aligned with ISO 38500 corporate governance principles:

| COBIT Domain | COBIT Process                                     | ISO 38500 Principle               |
| ------------ | ------------------------------------------------- | --------------------------------- |
| **EDM**      | EDM01 – Evaluate and direct IT governance         | Board responsibility              |
| **EDM**      | EDM02 – Ensure benefits realization               | Value delivery                    |
| **APO**      | APO01 – Manage IT management framework            | Strategic alignment               |
| **APO**      | APO02 – Manage strategy execution                 | Strategy implementation           |
| **BAI**      | BAI01 – Manage programs and projects              | Risk management                   |
| **BAI**      | BAI02 – Manage requirements definition            | Compliance assurance              |
| **DSS**      | DSS01 – Manage operations                         | Human resources management        |
| **DSS**      | DSS02 – Manage service requests                   | Compliance verification           |
| **MEA**      | MEA01 – Monitor, evaluate, and assess performance | Performance measurement           |
| **MEA**      | MEA02 – Monitor internal control system           | Control monitoring and assessment |

### EATGF Controls to ISO 27001:2022 Alignment

Comprehensive mapping of security controls to ISO 27001:2022 Annex A:

| EATGF Control                          | ISO 27001 Control | ISO 27001 Description                                                |
| -------------------------------------- | ----------------- | -------------------------------------------------------------------- |
| EATGF-DSS-SEC-01 (IAM)                 | A.9.1, A.9.2      | Access control policies and implementation; user access provisioning |
| EATGF-DSS-ENC-01 (Encryption)          | A.10.1, A.10.2    | Cryptography standards; encryption at rest and in transit            |
| EATGF-DSS-VULN-01 (Vulnerability Mgmt) | A.12.6            | Management of technical vulnerabilities; patch management            |
| EATGF-APO-ARCH-01 (Architecture)       | A.12.1            | Secure development and operations; architecture standards            |
| EATGF-DSS-INC-01 (Incident Response)   | A.16.1            | Incident management procedures and responsibilities                  |
| EATGF-APO-RISK-01 (Risk Assessment)    | A.12.6.1          | Risk evaluation and technical vulnerability assessment               |
| EATGF-APO-SEC-01 (ISMS)                | A.5 – A.18        | Complete information security management system                      |
| EATGF-DEV-SDLC-01 (Secure SDLC)        | A.14.2            | Security in development and support processes                        |
| EATGF-DEV-SCAN-01 (Code Scanning)      | A.14.2.8          | System security testing and code analysis                            |
| EATGF-DATA-PRIV-01 (Data Privacy)      | A.18.1.4          | Privacy and protection of personally identifiable information        |
| EATGF-BAI-CHG-01 (Change Mgmt)         | A.14.2.2          | System change control procedures                                     |
| EATGF-BAI-CONF-01 (Configuration Mgmt) | A.14.2.1          | Secure development policy and configuration baseline                 |
| EATGF-MEA-AUD-01 (Internal Audit)      | A.18.2            | Internal audit verification and compliance reviews                   |

**ISO 27001 Annex A Coverage Assessment:**

| Annex Category                       | Total Controls | EATGF Coverage | Coverage % |
| ------------------------------------ | -------------- | -------------- | ---------- |
| A.5 – Organizational Controls        | 2              | 2              | 100%       |
| A.6 – Personnel Security             | 3              | 3              | 100%       |
| A.7 – Asset Management               | 2              | 2              | 100%       |
| A.8 – Access Control                 | 8              | 8              | 100%       |
| A.9 – Cryptography                   | 2              | 2              | 100%       |
| A.10 – Physical and Environmental    | 3              | 1.5            | 50%        |
| A.11 – Operations Security           | 7              | 7              | 100%       |
| A.12 – Communications Security       | 7              | 7              | 100%       |
| A.13 – System Acquisition            | 5              | 5              | 100%       |
| A.14 – Supplier Relationships        | 3              | 3              | 100%       |
| A.15 – Information Security Incident | 5              | 5              | 100%       |
| A.16 – Business Continuity           | 2              | 1              | 50%        |

### EATGF Controls to ISO 42001:2023 Alignment

ISO 42001 Artificial Intelligence Management Systems mapping:

| EATGF Control     | ISO 42001 Section                  | Purpose                                                                 |
| ----------------- | ---------------------------------- | ----------------------------------------------------------------------- |
| EATGF-AI-LC-01    | Section 6 – Planning               | AI system lifecycle governance from development through decommissioning |
| EATGF-AI-RISK-01  | Section 8.1 – Operational planning | AI risk assessment, bias management, and fairness testing               |
| EATGF-DSS-ENC-01  | Section 8.2 – AI data governance   | AI training data protection and encryption                              |
| EATGF-APO-ARCH-01 | Section 6.1 – AI architecture      | AI system architecture planning and standards                           |
| EATGF-MEA-PERF-01 | Section 7 – Support                | AI performance metrics and monitoring                                   |
| EATGF-MEA-AUD-01  | Section 9 – Performance evaluation | AI control effectiveness and audit procedures                           |
| EATGF-APO-AI-01   | Sections 4-10 – Complete AIMS      | Full artificial intelligence management system implementation           |

**ISO 42001 Domains Addressed:**

- AI governance authority and management structure
- AI system development lifecycle and deployment procedures
- AI risk management and impact assessment
- Data governance specific to AI training and inference
- Transparency, explainability, and fairness requirements

### EATGF Controls to OWASP API Security Top 10:2023 Alignment

Complete OWASP API Security Top 10 coverage through EATGF API controls:

| EATGF Control               | OWASP Category                                         | Implementation                                                    |
| --------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------- |
| EATGF-API-LC-01 (Design)    | API1:2023 – Broken Object Level Authorization          | API design standards prevent direct object access vulnerabilities |
| EATGF-API-SEC-01 (Security) | API2:2023 – Broken Authentication                      | Authentication and authorization controls via OAuth 2.0 and mTLS  |
| EATGF-API-SEC-01            | API3:2023 – Broken Object Property Level Authorization | Role-based access control with field-level authorization          |
| EATGF-API-SEC-01            | API4:2023 – Unrestricted Resource Consumption          | Rate limiting, quota management, and resource throttling          |
| EATGF-API-SEC-01            | API5:2023 – Broken Function Level Authorization        | Function-level access controls and scope validation               |
| EATGF-API-SEC-01            | API6:2023 – Unrestricted Access to Sensitive Flows     | Business logic protection and workflow validation                 |
| EATGF-API-SEC-01            | API7:2023 – Server-Side Request Forgery                | Input validation, allowlists, and SSRF prevention                 |
| EATGF-API-SEC-01            | API8:2023 – Security Misconfiguration                  | Hardened defaults and configuration management procedures         |
| EATGF-API-LC-01             | API9:2023 – Improper Inventory Management              | API inventory control and catalog management                      |
| EATGF-API-SEC-01            | API10:2023 – Unsafe Consumption of APIs                | Third-party API validation and security assessment                |

### COBIT 2019 Domain Coverage

EATGF control distribution across COBIT domains:

| COBIT Domain                        | Total COBIT Processes | EATGF Controls Mapped                                                   | Coverage % |
| ----------------------------------- | --------------------- | ----------------------------------------------------------------------- | ---------- |
| **EDM** (Evaluate, Direct, Monitor) | 4                     | EATGF-EDM-RISK-01, EATGF-EDM-BEN-01, EATGF-EDM-GOV-01                   | 75%        |
| **APO** (Align, Plan, Organize)     | 13                    | EATGF-APO-ARCH-01, EATGF-APO-RISK-01, EATGF-APO-SEC-01, EATGF-APO-AI-01 | 31%        |
| **BAI** (Build, Acquire, Implement) | 10                    | EATGF-BAI-CHG-01, EATGF-BAI-CONF-01, EATGF-BAI-TEST-01                  | 30%        |
| **DSS** (Deliver, Service, Support) | 6                     | EATGF-DSS-SEC-01, EATGF-DSS-ENC-01, EATGF-DSS-VULN-01, EATGF-DSS-INC-01 | 67%        |
| **MEA** (Monitor, Evaluate, Assess) | 4                     | EATGF-MEA-AUD-01, EATGF-MEA-PERF-01, EATGF-MEA-MAT-01                   | 75%        |

### Standard Selection by Governance Edition

**Startup Edition (1-10 personnel):**

Applicable Standards:

- COBIT 2019 (lightweight subset of core domains)
- ISO 27001:2022 (core security categories only)
- ISO 38500:2015 (strategic governance guidance)
- ISO 42001:2023 (conditional – only if AI systems deployed)
- OWASP API Top 10:2023 (conditional – only if APIs exposed externally)

Focus Controls (Essential 4):

1. EATGF-DSS-SEC-01 – Identity and access management
2. EATGF-DSS-VULN-01 – Vulnerability and patch management
3. EATGF-APO-RISK-01 – Risk register maintenance
4. EATGF-DSS-ENC-01 – Data encryption standards

**SaaS Edition (10-50 personnel):**

Applicable Standards:

- COBIT 2019 (complete framework implementation)
- ISO 27001:2022 (full Annex A implementation)
- ISO 38500:2015 (full implementation with board oversight)
- ISO 42001:2023 (conditional – if AI systems deployed)
- OWASP API Top 10:2023 (full compliance for APIs)

Focus Controls (Enhanced 10):

- All Startup Edition controls (4)
- EATGF-AI-LC-01 – AI system lifecycle governance
- EATGF-AI-RISK-01 – AI risk and bias management
- EATGF-API-SEC-01 – API security controls
- EATGF-API-LC-01 – API lifecycle management
- EATGF-MEA-PERF-01 – Performance monitoring and KPIs
- EATGF-BAI-CHG-01 – Change management procedures

**Enterprise Edition (50+ personnel):**

Applicable Standards:

- COBIT 2019 (complete with advanced optimization)
- ISO 27001:2022 (complete with extended controls)
- ISO 38500:2015 (complete with board oversight and strategic alignment)
- ISO 42001:2023 (full implementation with AI governance expertise)
- OWASP API Top 10:2023 (advanced implementation with threat modeling)

Focus Controls: All 35 EATGF controls with full maturity targets

## Control Mapping

### COBIT 2019 Alignment

Mappings demonstrate comprehensive COBIT domain coverage:

- **EDM Domain:** Risk appetite, benefits, governance oversight (75% process coverage)
- **APO Domain:** Architecture, risk operations, security planning, AI policy (31% process coverage targeting strategic alignment)
- **BAI Domain:** Change, configuration, testing (30% process coverage for delivery assurance)
- **DSS Domain:** Security operations including IAM, encryption, vulnerability, incident (67% process coverage)
- **MEA Domain:** Audit, performance, maturity assessment (75% process coverage)

### ISO Standards Alignment

Framework mappings to ISO standards:

- **ISO 27001:2022:** 93% Annex A coverage across 16 control categories
- **ISO 42001:2023:** Complete AIMS coverage for AI governance when applicable
- **ISO 38500:2015:** Corporate governance principles mapped to COBIT EDM

### OWASP Alignment

OWASP API Security Top 10:2023 fully addressed through:

- **EATGF-API-SEC-01:** 8 of 10 OWASP categories (security controls)
- **EATGF-API-LC-01:** 2 of 10 OWASP categories (design and inventory)

## Developer Checklist

Before implementing EATGF controls using these mappings:

- [ ] Organization size determined (Startup/SaaS/Enterprise edition)
- [ ] Applicable standards identified based on edition and industry context
- [ ] Master Control Matrix reviewed for official control definitions
- [ ] ISO 27001 Annex A controls mapped to EATGF equivalents
- [ ] COBIT domain assignments understood for control ownership
- [ ] AI applicability assessed (ISO 42001:2023 conditional)
- [ ] API exposure assessed (OWASP Top 10:2023 conditional)
- [ ] Statement of Applicability drafted referencing this mapping document
- [ ] Audit procedures aligned with mapped international standards
- [ ] Control evidence requirements understood per ISO/COBIT/OWASP standards
- [ ] Edition-specific control prioritization applied
- [ ] Annual mapping review scheduled for framework currency

## Governance Implications

### Mapping Authority and Standards Currency

- Mappings in this document reference Master Control Matrix as single source of truth
- Framework mapping updates required when source standard publishes new edition
- Annual review cycle maintains mapping currency with evolving standards
- Coverage percentages recalculated during annual framework review

### Audit and Compliance

- Mappings provide audit trail for compliance assertions to multiple standards
- External auditors reference these mappings for ISO 27001 and ISO 42001 certification
- Statement of Applicability documentation cites this document for control justification
- Control gap analysis uses these mappings to identify uncovered standard requirements

### Edition-Specific Implementation

- Startup Edition focuses on essential 4 controls with ISO 27001 core security
- SaaS Edition expands to 10 controls with full ISO 27001 and conditional ISO 42001
- Enterprise Edition implements all 35 controls with advanced optimization
- Edition progression triggers control expansion and standard compliance deepening

### Framework Update Process

When external standards publish new editions:

1. Governance office reviews new standard requirements within 30 days
2. Gap analysis performed comparing new standard to current EATGF mappings
3. Master Control Matrix updated if new controls needed
4. This mapping document updated with new control alignments
5. Statement of Applicability refreshed with new standard references
6. Audit procedures updated to reflect new standard requirements

## Official References

- **COBIT 2019** – Governance of Enterprise Information Technology (ISACA, 2019)
- **ISO/IEC 27001:2022** – Information Security Management Systems (ISO, 2022)
- **ISO/IEC 27002:2022** – Code of practice for information security controls (ISO, 2022)
- **ISO/IEC 42001:2023** – Artificial Intelligence Management Systems (ISO, 2023)
- **ISO/IEC 38500:2015** – Corporate Governance of Information Technology (ISO, 2015)
- **OWASP API Security Top 10:2023** – API security controls (OWASP, 2023)

| COBIT Domain | COBIT Process                                                        | ISO 38500 Principle     |
| ------------ | -------------------------------------------------------------------- | ----------------------- |
| EDM          | EDM01 — Evaluate and direct IT governance                            | Board responsibility    |
| EDM          | EDM02 — Ensure benefits realisation                                  | Value delivery          |
| APO          | APO01 — Manage the IT management framework                           | Strategic alignment     |
| APO          | APO02 — Manage strategy                                              | Strategy execution      |
| BAI          | BAI01 — Manage programs and projects                                 | Risk management         |
| BAI          | BAI02 — Manage requirements definition                               | Compliance              |
| DSS          | DSS01 — Manage operations                                            | Human resources         |
| DSS          | DSS02 — Manage service requests                                      | Compliance              |
| MEA          | MEA01 — Monitor, evaluate, and assess performance                    | Performance measurement |
| MEA          | MEA02 — Monitor, evaluate, and assess the system of internal control | Control monitoring      |

---

## 3. EATGF Controls to ISO 27001:2022 Mapping

| EATGF Control                        | ISO 27001 Control | Description                                   |
| ------------------------------------ | ----------------- | --------------------------------------------- |
| EATGF-DSS-SEC-01 (IAM)               | A.9.1, A.9.2      | Access control policies and implementation    |
| EATGF-DSS-ENC-01 (Encryption)        | A.10.1, A.10.2    | Cryptography standards                        |
| EATGF-DSS-VULN-01 (Vuln Mgmt)        | A.12.6            | Management of technical vulnerabilities       |
| EATGF-APO-ARCH-01 (Architecture)     | A.12.1            | Secure development and operations             |
| EATGF-DSS-INC-01 (Incident Response) | A.16.1            | Incident management                           |
| EATGF-APO-RISK-01 (Risk Assessment)  | A.12.6.1          | Risk evaluation                               |
| EATGF-APO-SEC-01 (ISMS)              | A.5 — A.18        | Information security management system        |
| EATGF-DEV-SDLC-01 (Secure SDLC)      | A.14.2            | Security in development and support processes |
| EATGF-DEV-SCAN-01 (Code Scanning)    | A.14.2.8          | System security testing                       |
| EATGF-DATA-PRIV-01 (DPIA)            | A.18.1.4          | Privacy and protection of PII                 |

### ISO 27001 Control Set Coverage

**Fully Covered:** A.5 — A.16 (Core security controls)
**Partially Covered:** A.4 (Organization controls)
**Reference:** A.1 — A.3 (Context controls)

---

## 4. EATGF Controls to ISO 42001:2023 Mapping

| EATGF Control     | ISO 42001 Section | Purpose                                |
| ----------------- | ----------------- | -------------------------------------- |
| EATGF-AI-LC-01    | Section 6         | AI system lifecycle governance         |
| EATGF-AI-RISK-01  | Section 8.1       | AI risk assessment and bias management |
| EATGF-DSS-ENC-01  | Section 8.2       | AI data protection                     |
| EATGF-APO-ARCH-01 | Section 6.1       | AI system architecture                 |
| EATGF-MEA-PERF-01 | Section 7         | AI performance metrics                 |
| EATGF-MEA-AUD-01  | Section 9         | AI control effectiveness               |
| EATGF-APO-AI-01   | Section 4 — 10    | AI management system (full AIMS)       |

### ISO 42001 Domains Addressed

- AI governance and management
- AI system development and deployment
- AI risk and impact management
- Data governance for AI systems
- Transparency and explainability

---

## 5. EATGF Controls to OWASP API Security Top 10:2023 Mapping

| EATGF Control               | OWASP Category                                              | Implementation                                    |
| --------------------------- | ----------------------------------------------------------- | ------------------------------------------------- |
| EATGF-API-LC-01 (Design)    | API1:2023 — Broken Object Level Authorization               | API design standards prevent direct object access |
| EATGF-API-SEC-01 (Security) | API2:2023 — Broken Authentication                           | Authentication and authorization controls         |
| EATGF-API-SEC-01            | API3:2023 — Broken Object Property Level Authorization      | RBAC with field-level controls                    |
| EATGF-API-SEC-01            | API4:2023 — Unrestricted Resource Consumption               | Rate limiting and quota management                |
| EATGF-API-SEC-01            | API5:2023 — Broken Function Level Authorization             | Function-level access controls                    |
| EATGF-API-SEC-01            | API6:2023 — Unrestricted Access to Sensitive Business Flows | Business logic protection                         |
| EATGF-API-SEC-01            | API7:2023 — Server-Side Request Forgery                     | Input validation and allowlists                   |
| EATGF-API-SEC-01            | API8:2023 — Security Misconfiguration                       | Configuration standards                           |
| EATGF-API-LC-01             | API9:2023 — Improper Inventory Management                   | API inventory control                             |
| EATGF-API-SEC-01            | API10:2023 — Unsafe Consumption of APIs                     | Third-party API validation                        |

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

| Domain                          | Total Processes | EATGF Controls Mapped                                                   | Coverage |
| ------------------------------- | --------------- | ----------------------------------------------------------------------- | -------- |
| EDM (Evaluate, Direct, Monitor) | 4               | EATGF-EDM-RISK-01, EATGF-EDM-BEN-01, EATGF-EDM-GOV-01                   | 75%      |
| APO (Align, Plan, Organize)     | 13              | EATGF-APO-ARCH-01, EATGF-APO-RISK-01, EATGF-APO-SEC-01, EATGF-APO-AI-01 | 31%      |
| BAI (Build, Acquire, Implement) | 10              | EATGF-BAI-CHG-01, EATGF-BAI-CONF-01, EATGF-BAI-TEST-01                  | 30%      |
| DSS (Deliver, Service, Support) | 6               | EATGF-DSS-SEC-01, EATGF-DSS-ENC-01, EATGF-DSS-VULN-01, EATGF-DSS-INC-01 | 67%      |
| MEA (Monitor, Evaluate, Assess) | 4               | EATGF-MEA-AUD-01, EATGF-MEA-PERF-01, EATGF-MEA-MAT-01                   | 75%      |

### ISO 27001:2022 Coverage

| Annex                                | Metrics      | Coverage |
| ------------------------------------ | ------------ | -------- |
| A.5 — Organizational Controls        | 2/2 Controls | 100%     |
| A.6 — Personnel Security             | 3/3 Controls | 100%     |
| A.7 — Asset Management               | 2/2 Controls | 100%     |
| A.8 — Access Control                 | 8/8 Controls | 100%     |
| A.9 — Cryptography                   | 2/2 Controls | 100%     |
| A.10 — Physical and Environmental    | 3/3 Controls | 50%      |
| A.11 — Operations Security           | 7/7 Controls | 100%     |
| A.12 — Communications Security       | 7/7 Controls | 100%     |
| A.13 — System Acquisition            | 5/5 Controls | 100%     |
| A.14 — Supplier Relationships        | 3/3 Controls | 100%     |
| A.15 — Information Security Incident | 5/5 Controls | 100%     |
| A.16 — Business Continuity           | 2/2 Controls | 50%      |

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

| Framework          | Version | Last Updated | Next Review |
| ------------------ | ------- | ------------ | ----------- |
| COBIT              | 2019    | Feb 2026     | Aug 2026    |
| ISO 38500          | 2015    | Feb 2026     | Aug 2026    |
| ISO 27001          | 2022    | Feb 2026     | Aug 2026    |
| ISO 42001          | 2023    | Feb 2026     | Aug 2026    |
| OWASP API Security | 2023    | Feb 2026     | Feb 2027    |

---

## 10. Governance Enforcement Rules

1. All mapping tables in this document reference the EATGF control taxonomy as defined in the Master Control Matrix. Legacy identifiers (AC-01, SEC-01, etc.) are superseded.
2. Mapping updates require governance review when a source framework publishes a new edition.
3. Coverage percentages are recalculated during annual framework mapping reviews.

---

**Document Control**

| Version | Date       | Author                                      | Change Description                                                                                                                |
| ------- | ---------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-02-01 | Governance Office                           | Initial framework mappings with 14 legacy controls                                                                                |
| 2.0     | 2026-02-14 | Enterprise Architecture & Governance Office | Adopted EATGF-xxx taxonomy; expanded to 35 controls; corrected ISO 42001 to 2023; added EATGF header; removed placeholder content |

**Authority Sign-Off**

| Role                     | Name | Date | Signature |
| ------------------------ | ---- | ---- | --------- |
| Chief Governance Officer |      |      |           |
| Enterprise Architect     |      |      |           |
