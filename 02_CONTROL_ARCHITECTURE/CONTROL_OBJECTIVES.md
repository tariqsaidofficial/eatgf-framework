# Control Objectives

## Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field | Value |
|-------|-------|
| Document Type | Control Architecture |
| Version | 2.0 |
| Classification | Internal |
| Effective Date | 2026-02-14 |
| Baseline | COBIT 2019, ISO/IEC 27001:2022, ISO/IEC 42001:2023, OWASP ASVS 4.0 |
| Authority | Enterprise Architecture & Governance Office |
| MCM Reference | All 35 EATGF Controls |

---

## 1. Purpose

This document defines the control objectives for all 35 controls within the EATGF Master Control Matrix. Each control specifies its objective, control requirements, evidence requirements, and applicability.

---

## 2. Control Taxonomy

All controls use the EATGF naming convention:

```
EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]
```

### Domain Summary

| Domain | Code | Controls | Scope |
|--------|------|----------|-------|
| Enterprise Direction and Management | EDM | 3 | Strategy, risk oversight, benefit realisation |
| Align, Plan and Organise | APO | 4 | Architecture, risk operations, security planning, AI policy |
| Build, Acquire and Implement | BAI | 3 | Change, configuration, test management |
| Deliver, Service and Support | DSS | 4 | IAM, encryption, vulnerability management, incident response |
| Monitor, Evaluate and Assess | MEA | 3 | Audit, performance, maturity |
| Artificial Intelligence | AI | 2 | AI lifecycle, AI risk and bias |
| Application Programming Interface | API | 2 | API security, API lifecycle |
| Cloud | CLD | 4 | Architecture, security, monitoring, resilience |
| Development | DEV | 4 | SDLC, code scanning, supply chain, CI/CD |
| Data | DATA | 3 | Privacy, retention, minimisation |
| Business Continuity Planning | BCP | 3 | Planning, testing, RTO/RPO |
| **Total** | | **35** | |

---

## 3. How to Read Control Entries

Each control entry follows this structure:

- **Objective** — The governance outcome the control achieves.
- **Control Requirements** — The specific activities and conditions that must be in place.
- **Evidence Requirements** — The artefacts required to demonstrate compliance.
- **Applicability** — The organisational contexts and team sizes where the control applies.

---

## 4. Control Reference Index

| Control ID | Domain | Short Title |
|-----------|--------|-------------|
| EATGF-EDM-RISK-01 | EDM | IT Risk Direction |
| EATGF-EDM-BEN-01 | EDM | Benefits Realisation |
| EATGF-EDM-GOV-01 | EDM | Governance Framework Oversight |
| EATGF-APO-ARCH-01 | APO | Enterprise Architecture |
| EATGF-APO-RISK-01 | APO | Operational Risk Process |
| EATGF-APO-SEC-01 | APO | Security Strategy |
| EATGF-APO-AI-01 | APO | AI Strategy and Policy |
| EATGF-BAI-CHG-01 | BAI | Change Management |
| EATGF-BAI-CONF-01 | BAI | Configuration Management |
| EATGF-BAI-TEST-01 | BAI | Test Management |
| EATGF-DSS-SEC-01 | DSS | Identity and Access Management |
| EATGF-DSS-ENC-01 | DSS | Encryption Standards |
| EATGF-DSS-VULN-01 | DSS | Vulnerability Management |
| EATGF-DSS-INC-01 | DSS | Incident Response |
| EATGF-MEA-AUD-01 | MEA | Internal Audit |
| EATGF-MEA-PERF-01 | MEA | Performance Monitoring |
| EATGF-MEA-MAT-01 | MEA | Maturity Assessment |
| EATGF-AI-LC-01 | AI | AI Lifecycle Governance |
| EATGF-AI-RISK-01 | AI | AI Risk and Bias Management |
| EATGF-API-SEC-01 | API | API Security |
| EATGF-API-LC-01 | API | API Lifecycle Management |
| EATGF-CLD-ARCH-01 | CLD | Cloud Architecture |
| EATGF-CLD-SEC-01 | CLD | Cloud Security |
| EATGF-CLD-MON-01 | CLD | Cloud Monitoring |
| EATGF-CLD-RES-01 | CLD | Cloud Resilience |
| EATGF-DEV-SDLC-01 | DEV | Secure SDLC |
| EATGF-DEV-SCAN-01 | DEV | Code Scanning |
| EATGF-DEV-SUP-01 | DEV | Supply Chain Security |
| EATGF-DEV-CI-01 | DEV | CI/CD Governance |
| EATGF-DATA-PRIV-01 | DATA | Data Privacy |
| EATGF-DATA-RET-01 | DATA | Data Retention |
| EATGF-DATA-MIN-01 | DATA | Data Minimisation |
| EATGF-BCP-PLAN-01 | BCP | Business Continuity Planning |
| EATGF-BCP-TEST-01 | BCP | Business Continuity Testing |
| EATGF-BCP-RTO-01 | BCP | RTO/RPO Targets |

---

## 5. EDM — Enterprise Direction and Management

### 5.1 EATGF-EDM-RISK-01: IT Risk Direction

**Objective:** Establish enterprise-level direction for IT risk management, ensuring risk appetite and risk tolerance are defined, communicated, and enforced across all technology domains.

**Control Requirements:**
- Define and document risk appetite at the board level.
- Communicate risk appetite to all teams and technology owners.
- Conduct annual risk appetite review aligned with strategic planning.
- Maintain alignment between risk direction and EATGF control implementation.

**Evidence Requirements:**
- Board-approved risk appetite statement.
- Minutes of annual risk appetite review.
- Risk tolerance thresholds documented per domain.

**Applicability:** All organisations. Scaled guidance available in the Governance by Team Size model.

### 5.2 EATGF-EDM-BEN-01: Benefits Realisation

**Objective:** Ensure that IT investments and governance initiatives deliver measurable business value.

**Control Requirements:**
- Establish benefits realisation tracking for governance programme.
- Define key performance indicators (KPIs) for each investment.
- Conduct post-implementation benefits review within 6 months of deployment.

**Evidence Requirements:**
- Benefits register with KPIs and targets.
- Post-implementation review reports.
- Annual benefits realisation summary.

**Applicability:** Organisations with formal IT investment programmes. Optional for teams of 10 or fewer.

### 5.3 EATGF-EDM-GOV-01: Governance Framework Oversight

**Objective:** Provide strategic oversight of the governance framework, ensuring it remains current, effective, and aligned with organisational objectives.

**Control Requirements:**
- Annual governance framework review by Governance Council.
- Quarterly monitoring of framework adoption metrics.
- Board-level reporting on governance maturity.

**Evidence Requirements:**
- Annual framework review report.
- Governance adoption dashboard.
- Board presentation materials.

**Applicability:** All organisations implementing EATGF.

---

## 6. APO — Align, Plan and Organise

### 6.1 EATGF-APO-ARCH-01: Enterprise Architecture

**Objective:** Establish and maintain an enterprise architecture practice that ensures technology decisions align with business strategy and governance requirements.

**Control Requirements:**
- Maintain enterprise architecture documentation (current state and target state).
- Ensure all new technology decisions include architecture review.
- Conduct architecture review board meetings at least quarterly.
- Align architecture decisions with EATGF control requirements.

**Evidence Requirements:**
- Architecture decision records.
- Architecture review board meeting minutes.
- Current-state and target-state architecture diagrams.

**Applicability:** All organisations. Lightweight architecture documentation is acceptable for teams of 20 or fewer.

### 6.2 EATGF-APO-RISK-01: Operational Risk Process

**Objective:** Implement and maintain operational risk management processes that identify, assess, and mitigate technology risks.

**Control Requirements:**
- Maintain an operational risk register.
- Conduct quarterly risk assessments.
- Assign risk owners for all identified risks.
- Track mitigation actions to completion.

**Evidence Requirements:**
- Risk register (current, with owner assignments).
- Quarterly risk assessment reports.
- Mitigation action tracking log.

**Applicability:** All organisations. Risk assessment frequency may be reduced to semi-annual for teams of 10 or fewer.

### 6.3 EATGF-APO-SEC-01: Security Strategy

**Objective:** Define and maintain a security strategy that aligns with organisational risk appetite and regulatory requirements.

**Control Requirements:**
- Publish an information security policy aligned with ISO/IEC 27001:2022.
- Conduct annual security strategy review.
- Maintain security roadmap with quarterly milestones.
- Ensure security strategy covers all EATGF domains.

**Evidence Requirements:**
- Information security policy (approved).
- Security strategy document.
- Annual security strategy review report.

**Applicability:** All organisations.

### 6.4 EATGF-APO-AI-01: AI Strategy and Policy

**Objective:** Establish governance direction for AI initiatives, including ethical frameworks, risk management, and compliance with ISO/IEC 42001:2023.

**Control Requirements:**
- Publish an AI governance policy.
- Define AI risk appetite and acceptable use boundaries.
- Establish AI ethics review board or committee.
- Maintain AI model inventory with risk categorisation.

**Evidence Requirements:**
- AI governance policy (approved).
- AI model inventory.
- AI ethics review board charter and meeting minutes.

**Applicability:** Organisations deploying or developing AI systems. Not applicable to organisations without AI capability.

---

## 7. BAI — Build, Acquire and Implement

### 7.1 EATGF-BAI-CHG-01: Change Management

**Objective:** Ensure all changes to production systems are authorised, documented, tested, and traceable.

**Control Requirements:**
- Implement a formal change management process.
- Require change approval prior to production deployment.
- Maintain a change log with rollback procedures.
- Conduct post-implementation reviews for significant changes.

**Evidence Requirements:**
- Change request records (approved).
- Change log with deployment timestamps.
- Post-implementation review reports.

**Applicability:** All organisations. Lightweight change tracking is acceptable for teams of 5 or fewer.

### 7.2 EATGF-BAI-CONF-01: Configuration Management

**Objective:** Maintain accurate and current configuration records for all managed assets.

**Control Requirements:**
- Implement a configuration management database (CMDB) or equivalent.
- Conduct quarterly configuration audits.
- Ensure all infrastructure changes are reflected in configuration records.

**Evidence Requirements:**
- CMDB or asset registry (current).
- Quarterly configuration audit reports.
- Configuration change log.

**Applicability:** All organisations. Spreadsheet-based tracking is acceptable for small teams.

### 7.3 EATGF-BAI-TEST-01: Test Management

**Objective:** Ensure all changes and new deployments are adequately tested before release.

**Control Requirements:**
- Define test strategy covering unit, integration, and acceptance testing.
- Require test evidence before production release approval.
- Maintain test results with traceability to requirements.
- Conduct security testing for changes affecting authentication, authorisation, or data handling.

**Evidence Requirements:**
- Test strategy document.
- Test execution reports.
- Defect tracking records.

**Applicability:** All organisations deploying software. Manual testing is acceptable for teams without automated test frameworks.

---

## 8. DSS — Deliver, Service and Support

### 8.1 EATGF-DSS-SEC-01: Identity and Access Management

**Objective:** Ensure that access to systems and data is restricted to authorised individuals, using the principle of least privilege.

**Control Requirements:**
- Implement role-based access control (RBAC) across all systems.
- Conduct quarterly access reviews.
- Enforce multi-factor authentication (MFA) for privileged and remote access.
- Implement automated provisioning and deprovisioning.

**Evidence Requirements:**
- RBAC policy and role definitions.
- Quarterly access review reports.
- MFA deployment evidence.
- Provisioning/deprovisioning audit logs.

**Applicability:** All organisations.

### 8.2 EATGF-DSS-ENC-01: Encryption Standards

**Objective:** Protect data confidentiality and integrity through encryption at rest and in transit.

**Control Requirements:**
- Encrypt all data at rest using AES-256 or equivalent.
- Enforce TLS 1.2 or higher for all data in transit.
- Implement key management procedures aligned with industry standards.
- Conduct annual cryptographic review.

**Evidence Requirements:**
- Encryption configuration evidence.
- Key management procedures document.
- Annual cryptographic review report.

**Applicability:** All organisations processing sensitive or regulated data.

### 8.3 EATGF-DSS-VULN-01: Vulnerability Management

**Objective:** Identify, assess, and remediate vulnerabilities across all managed systems within defined timelines.

**Control Requirements:**
- Conduct monthly vulnerability scans across all production systems.
- Define remediation SLAs by vulnerability severity (Critical: 72 hrs, High: 7 days, Medium: 30 days, Low: 90 days).
- Track remediation to completion.
- Report vulnerability metrics to Governance Council quarterly.

**Evidence Requirements:**
- Monthly vulnerability scan reports.
- Remediation tracking log with SLA compliance.
- Quarterly vulnerability dashboard.

**Applicability:** All organisations with externally facing or production systems.

### 8.4 EATGF-DSS-INC-01: Incident Response

**Objective:** Ensure that security incidents are detected, contained, and resolved according to documented procedures, with root cause analysis conducted for significant incidents.

**Control Requirements:**
- Maintain an incident response plan.
- Define incident severity levels and escalation procedures.
- Conduct post-incident reviews for all Severity 1 and 2 incidents.
- Conduct annual incident response tabletop exercises.

**Evidence Requirements:**
- Incident response plan (approved).
- Incident log with severity classification.
- Post-incident review reports.
- Tabletop exercise records.

**Applicability:** All organisations.

---

## 9. MEA — Monitor, Evaluate and Assess

### 9.1 EATGF-MEA-AUD-01: Internal Audit

**Objective:** Provide independent assurance that controls are operating effectively through periodic audit activities.

**Control Requirements:**
- Establish an annual audit plan covering all EATGF domains.
- Conduct audits using the internal audit procedure (EATGF Layer 6).
- Track audit findings to remediation.
- Report audit results to Governance Council.

**Evidence Requirements:**
- Annual audit plan.
- Audit reports with findings.
- Audit finding remediation tracker.

**Applicability:** All organisations. External audit may substitute for internal audit in organisations without a dedicated audit function.

### 9.2 EATGF-MEA-PERF-01: Performance Monitoring

**Objective:** Measure and report on the performance of governance controls and technology operations against defined KPIs.

**Control Requirements:**
- Define KPIs for all critical governance processes.
- Collect and report KPI data monthly.
- Conduct quarterly performance reviews.
- Initiate corrective action when KPIs fall below threshold.

**Evidence Requirements:**
- KPI definitions and thresholds.
- Monthly KPI reports.
- Quarterly performance review minutes.

**Applicability:** All organisations. KPI scope may be reduced for teams of 10 or fewer.

### 9.3 EATGF-MEA-MAT-01: Maturity Assessment

**Objective:** Assess organisational governance maturity periodically and identify improvement priorities.

**Control Requirements:**
- Conduct annual maturity assessment using the EATGF Maturity Model (Layer 3).
- Assess maturity across all 11 EATGF domains.
- Define improvement targets and track progress.
- Report maturity scoring to Governance Council.

**Evidence Requirements:**
- Annual maturity assessment report.
- Maturity scoring by domain.
- Improvement action plan.

**Applicability:** All organisations implementing EATGF.

---

## 10. AI — Artificial Intelligence

### 10.1 EATGF-AI-LC-01: AI Lifecycle Governance

**Objective:** Govern the full lifecycle of AI systems from design through deployment and decommission, ensuring compliance with ISO/IEC 42001:2023.

**Control Requirements:**
- Maintain an AI model inventory with lifecycle stage tracking.
- Require impact assessment before AI model deployment.
- Implement model monitoring for drift, performance degradation, and fairness.
- Conduct annual review of all deployed AI models.
- Define decommission criteria and procedures.

**Evidence Requirements:**
- AI model inventory (current).
- Pre-deployment impact assessments.
- Model monitoring dashboards.
- Annual AI model review reports.

**Applicability:** Organisations deploying AI/ML systems.

### 10.2 EATGF-AI-RISK-01: AI Risk and Bias Management

**Objective:** Identify, assess, and mitigate AI-specific risks including bias, fairness, explainability, and safety.

**Control Requirements:**
- Conduct bias testing during model development and before deployment.
- Define fairness thresholds (e.g., disparate impact ratio above 0.80).
- Implement explainability documentation for all high-risk AI models.
- Monitor production models for bias drift.
- Maintain an AI risk register distinct from the general risk register.

**Evidence Requirements:**
- Bias testing reports.
- Fairness threshold documentation.
- Explainability reports for high-risk models.
- AI risk register.

**Applicability:** Organisations deploying AI/ML systems, especially in regulated sectors or high-risk use cases.

---

## 11. API — Application Programming Interface

### 11.1 EATGF-API-SEC-01: API Security

**Objective:** Ensure all APIs are secured against OWASP API Security Top 10 risks and enforce authentication, authorisation, and rate limiting.

**Control Requirements:**
- Implement API gateway with authentication and rate limiting.
- Enforce OAuth 2.0 or equivalent for API authentication.
- Conduct API security testing aligned with OWASP ASVS 4.0.
- Monitor API traffic for anomalous patterns.

**Evidence Requirements:**
- API gateway configuration evidence.
- API security test reports.
- API traffic monitoring dashboards.

**Applicability:** Organisations exposing or consuming APIs.

### 11.2 EATGF-API-LC-01: API Lifecycle Management

**Objective:** Govern the full lifecycle of APIs from design through deprecation, ensuring version control, documentation, and consumer communication.

**Control Requirements:**
- Maintain an API catalogue with version, owner, and status.
- Define API deprecation policy with minimum notice period.
- Publish API documentation (e.g., OpenAPI specifications).
- Conduct quarterly API portfolio review.

**Evidence Requirements:**
- API catalogue (current).
- API deprecation notices.
- API documentation (published).
- Quarterly API review minutes.

**Applicability:** Organisations managing 5 or more APIs. Optional for smaller API portfolios.

---

## 12. CLD — Cloud

### 12.1 EATGF-CLD-ARCH-01: Cloud Architecture

**Objective:** Ensure cloud deployments follow a well-architected framework aligned with organisational standards.

**Control Requirements:**
- Define cloud architecture standards (e.g., landing zone design).
- Require architecture review for all new cloud workloads.
- Maintain cloud architecture documentation.
- Conduct annual well-architected review.

**Evidence Requirements:**
- Cloud architecture standards document.
- Cloud architecture review records.
- Annual well-architected review report.

**Applicability:** Organisations using public or hybrid cloud.

### 12.2 EATGF-CLD-SEC-01: Cloud Security

**Objective:** Implement cloud-specific security controls covering identity, network segmentation, logging, and data protection.

**Control Requirements:**
- Implement cloud-native identity and access management.
- Enforce network segmentation and security groups.
- Enable cloud audit logging across all accounts.
- Implement data protection controls (encryption, DLP).

**Evidence Requirements:**
- Cloud IAM configuration evidence.
- Network segmentation documentation.
- Cloud audit log retention evidence.
- Data protection configuration evidence.

**Applicability:** All organisations using cloud services.

### 12.3 EATGF-CLD-MON-01: Cloud Monitoring

**Objective:** Ensure real-time monitoring of cloud resources for performance, availability, and security events.

**Control Requirements:**
- Implement cloud monitoring covering compute, storage, network.
- Define alerting thresholds and escalation procedures.
- Retain monitoring data for a minimum of 12 months.
- Conduct monthly cloud monitoring review.

**Evidence Requirements:**
- Cloud monitoring configuration evidence.
- Alerting threshold documentation.
- Monthly monitoring review reports.

**Applicability:** All organisations using cloud services.

### 12.4 EATGF-CLD-RES-01: Cloud Resilience

**Objective:** Ensure cloud workloads are designed for resilience with defined availability targets and failover procedures.

**Control Requirements:**
- Define availability targets for all cloud workloads.
- Implement multi-availability-zone or multi-region deployments for critical workloads.
- Conduct annual failover testing.
- Maintain cloud disaster recovery documentation.

**Evidence Requirements:**
- Availability target documentation.
- Multi-AZ/region deployment evidence.
- Failover test reports.
- Cloud DR documentation.

**Applicability:** Organisations with production workloads in cloud.

---

## 13. DEV — Development

### 13.1 EATGF-DEV-SDLC-01: Secure SDLC

**Objective:** Embed security practices throughout the software development lifecycle.

**Control Requirements:**
- Define secure development standards.
- Require threat modelling for new applications.
- Conduct security reviews at design and pre-deployment gates.
- Provide security training for all developers annually.

**Evidence Requirements:**
- Secure development standards document.
- Threat model records.
- Security gate review records.
- Developer security training records.

**Applicability:** All organisations developing software.

### 13.2 EATGF-DEV-SCAN-01: Code Scanning

**Objective:** Detect and remediate code-level security vulnerabilities through static and dynamic analysis.

**Control Requirements:**
- Implement SAST (static application security testing) in CI/CD pipeline.
- Implement DAST (dynamic application security testing) for deployed applications.
- Define remediation SLAs by severity.
- Track scanning coverage across all repositories.

**Evidence Requirements:**
- SAST configuration and scan reports.
- DAST scan reports.
- Remediation tracking log.
- Coverage metrics.

**Applicability:** All organisations developing software. DAST may be deferred for internal-only applications.

### 13.3 EATGF-DEV-SUP-01: Supply Chain Security

**Objective:** Manage risks associated with third-party software dependencies and open-source components.

**Control Requirements:**
- Generate software bill of materials (SBOM) for all applications.
- Monitor dependencies for known vulnerabilities.
- Define approved and prohibited dependency lists.
- Conduct quarterly dependency review.

**Evidence Requirements:**
- SBOM records.
- Dependency vulnerability reports.
- Approved/prohibited dependency lists.
- Quarterly dependency review minutes.

**Applicability:** All organisations using third-party or open-source dependencies.

### 13.4 EATGF-DEV-CI-01: CI/CD Governance

**Objective:** Ensure CI/CD pipelines enforce governance gates including security scanning, testing, and approval workflows.

**Control Requirements:**
- Implement governance gates in CI/CD pipelines (build, test, scan, approve, deploy).
- Require human approval for production deployments.
- Maintain pipeline configuration in version control.
- Audit pipeline execution logs.

**Evidence Requirements:**
- Pipeline configuration records (in version control).
- Deployment approval records.
- Pipeline execution audit logs.

**Applicability:** All organisations using CI/CD. Manual deployment processes require equivalent governance controls.

---

## 14. DATA — Data

### 14.1 EATGF-DATA-PRIV-01: Data Privacy

**Objective:** Ensure personal and sensitive data is processed in accordance with applicable privacy legislation and organisational policy.

**Control Requirements:**
- Maintain a data processing inventory (register of processing activities).
- Conduct data protection impact assessments (DPIAs) for high-risk processing.
- Implement data subject rights procedures.
- Define and enforce data classification scheme.

**Evidence Requirements:**
- Data processing inventory.
- DPIA records.
- Data subject request log.
- Data classification policy.

**Applicability:** All organisations processing personal data.

### 14.2 EATGF-DATA-RET-01: Data Retention

**Objective:** Ensure data is retained for the period required by regulation and business need, and securely disposed of thereafter.

**Control Requirements:**
- Define data retention schedule by data category.
- Implement automated retention enforcement where feasible.
- Conduct annual retention compliance review.
- Maintain evidence of secure data disposal.

**Evidence Requirements:**
- Data retention schedule.
- Retention enforcement configuration evidence.
- Annual retention review report.
- Disposal certificates or logs.

**Applicability:** All organisations.

### 14.3 EATGF-DATA-MIN-01: Data Minimisation

**Objective:** Ensure that only the minimum data necessary for the stated purpose is collected and retained.

**Control Requirements:**
- Define data minimisation principles in data governance policy.
- Review data collection practices annually.
- Implement technical controls to limit data collection.
- Report data minimisation metrics to Governance Council.

**Evidence Requirements:**
- Data governance policy (with minimisation section).
- Annual data collection review report.
- Data minimisation metrics.

**Applicability:** All organisations processing personal or sensitive data.

---

## 15. BCP — Business Continuity Planning

### 15.1 EATGF-BCP-PLAN-01: Business Continuity Planning

**Objective:** Ensure the organisation has documented business continuity plans for critical technology services.

**Control Requirements:**
- Develop and maintain business continuity plans for all critical services.
- Define critical service inventory with business impact analysis.
- Conduct annual BCP review and update.
- Ensure BCP covers technology, people, and process.

**Evidence Requirements:**
- Business continuity plans (approved).
- Critical service inventory.
- Business impact analysis.
- Annual BCP review records.

**Applicability:** All organisations.

### 15.2 EATGF-BCP-TEST-01: Business Continuity Testing

**Objective:** Validate business continuity plans through periodic testing exercises.

**Control Requirements:**
- Conduct annual business continuity test (tabletop or failover).
- Document test results including gaps identified.
- Update BCP based on test findings.
- Report test results to Governance Council.

**Evidence Requirements:**
- BCP test plan and results.
- Gap analysis from testing.
- BCP update records post-test.

**Applicability:** All organisations. Tabletop exercises are acceptable for organisations without dedicated DR infrastructure.

### 15.3 EATGF-BCP-RTO-01: RTO/RPO Targets

**Objective:** Define and validate recovery time objectives (RTO) and recovery point objectives (RPO) for all critical services.

**Control Requirements:**
- Define RTO and RPO targets for each critical service.
- Validate RTO/RPO targets through testing.
- Ensure backup and recovery mechanisms support defined targets.
- Report RTO/RPO compliance to Governance Council.

**Evidence Requirements:**
- RTO/RPO target documentation.
- Test results validating RTO/RPO achievability.
- Backup and recovery configuration evidence.

**Applicability:** All organisations with critical technology services.

---

## 16. Implementation Summary

| Control ID | Domain | Objective Summary | Evidence Type | Review Frequency | Owner |
|-----------|--------|------------------|--------------|-----------------|-------|
| EATGF-EDM-RISK-01 | EDM | IT risk direction and appetite | Risk appetite statement | Annual | Board/CRO |
| EATGF-EDM-BEN-01 | EDM | Benefits realisation tracking | Benefits register | Annual | CFO |
| EATGF-EDM-GOV-01 | EDM | Governance framework oversight | Framework review report | Annual | Governance Council |
| EATGF-APO-ARCH-01 | APO | Enterprise architecture management | Architecture decision records | Quarterly | Enterprise Architect |
| EATGF-APO-RISK-01 | APO | Operational risk process | Risk register | Quarterly | Risk Manager |
| EATGF-APO-SEC-01 | APO | Security strategy alignment | Security policy | Annual | CISO |
| EATGF-APO-AI-01 | APO | AI strategy and policy | AI governance policy | Annual | AI Governance Lead |
| EATGF-BAI-CHG-01 | BAI | Change management | Change request records | Per change | Change Manager |
| EATGF-BAI-CONF-01 | BAI | Configuration management | CMDB/asset registry | Quarterly | IT Operations |
| EATGF-BAI-TEST-01 | BAI | Test management | Test execution reports | Per release | QA Lead |
| EATGF-DSS-SEC-01 | DSS | Identity and access management | Access review reports | Quarterly | IAM Lead |
| EATGF-DSS-ENC-01 | DSS | Encryption standards | Encryption configuration | Annual | Security Engineer |
| EATGF-DSS-VULN-01 | DSS | Vulnerability management | Scan reports | Monthly | Security Operations |
| EATGF-DSS-INC-01 | DSS | Incident response | Incident log | Per incident | Incident Manager |
| EATGF-MEA-AUD-01 | MEA | Internal audit | Audit reports | Annual | Internal Audit |
| EATGF-MEA-PERF-01 | MEA | Performance monitoring | KPI reports | Monthly | Governance Office |
| EATGF-MEA-MAT-01 | MEA | Maturity assessment | Maturity assessment report | Annual | Governance Office |
| EATGF-AI-LC-01 | AI | AI lifecycle governance | AI model inventory | Annual | AI Governance Lead |
| EATGF-AI-RISK-01 | AI | AI risk and bias management | Bias testing reports | Per deployment | AI Ethics Board |
| EATGF-API-SEC-01 | API | API security | API security test reports | Quarterly | API Lead |
| EATGF-API-LC-01 | API | API lifecycle management | API catalogue | Quarterly | API Lead |
| EATGF-CLD-ARCH-01 | CLD | Cloud architecture | Architecture review records | Annual | Cloud Architect |
| EATGF-CLD-SEC-01 | CLD | Cloud security | Cloud IAM config evidence | Quarterly | Cloud Security |
| EATGF-CLD-MON-01 | CLD | Cloud monitoring | Monitoring review reports | Monthly | Cloud Operations |
| EATGF-CLD-RES-01 | CLD | Cloud resilience | Failover test reports | Annual | Cloud Operations |
| EATGF-DEV-SDLC-01 | DEV | Secure SDLC | Threat model records | Per application | Dev Lead |
| EATGF-DEV-SCAN-01 | DEV | Code scanning | SAST/DAST scan reports | Per release | Security Engineering |
| EATGF-DEV-SUP-01 | DEV | Supply chain security | SBOM records | Quarterly | Dev Lead |
| EATGF-DEV-CI-01 | DEV | CI/CD governance | Pipeline audit logs | Per deployment | DevOps Lead |
| EATGF-DATA-PRIV-01 | DATA | Data privacy | Data processing inventory | Annual | DPO |
| EATGF-DATA-RET-01 | DATA | Data retention | Retention schedule | Annual | Data Governance |
| EATGF-DATA-MIN-01 | DATA | Data minimisation | Data collection review | Annual | Data Governance |
| EATGF-BCP-PLAN-01 | BCP | Business continuity planning | BCP documents | Annual | BC Manager |
| EATGF-BCP-TEST-01 | BCP | Business continuity testing | BCP test results | Annual | BC Manager |
| EATGF-BCP-RTO-01 | BCP | RTO/RPO targets | RTO/RPO validation results | Annual | BC Manager |

---

## 17. Governance Enforcement Rules

1. The Master Control Matrix is the single source of truth for control ownership, status, and evidence requirements. This document provides detailed objectives and requirements for each control.
2. All control references must use the `EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]` format. Legacy control identifiers are not valid for compliance reporting.
3. Evidence requirements listed in this document are minimum requirements. Additional evidence may be required based on regulatory context.
4. Control applicability is determined by organisational context. Exceptions must be documented and approved by the Governance Council.
5. Review frequencies specified in Section 16 are minimum requirements. Higher frequencies may be adopted based on risk assessment.

---

**Document Control**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-01 | Governance Office | Initial 14-control objectives catalogue |
| 2.0 | 2026-02-14 | Enterprise Architecture & Governance Office | Expanded to 35 controls across 11 domains; adopted EATGF-xxx control taxonomy; added implementation summary table; removed legacy control identifiers; added EATGF header; corrected tone to institutional register |

**Authority Sign-Off**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Chief Governance Officer | | | |
| Chief Information Security Officer | | | |

---

**Next Review:** August 2026
