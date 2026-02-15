# CONTROL_OBJECTIVES

| Field          | Value                                                      |
| -------------- | ---------------------------------------------------------- |
| Document Type  | Control Architecture                                       |
| Version        | 2.0                                                        |
| Classification | Controlled                                                 |
| Effective Date | 2026-02-14                                                 |
| Authority      | Enterprise Architecture and Governance Office              |
| EATGF Layer    | 02_CONTROL_ARCHITECTURE                                    |
| MCM Reference  | All 35 EATGF Controls                                      |
| Standards      | COBIT 2019, ISO 27001:2022, ISO 42001:2023, OWASP ASVS 4.0 |

---

## Purpose

This document establishes authoritative control objectives for all 35 controls within EATGF Master Control Matrix. Each control specifies objective, control requirements, evidence requirements, and applicability across 11 governance domains (EDM, APO, BAI, DSS, MEA, AI, API, CLD, DEV, DATA, BCP). This document serves as compliance reference for internal audit (Layer 06), control implementation planning, and evidence verification.

## Architectural Position

This document operates within **02_CONTROL_ARCHITECTURE** as the definitive control objectives specification.

- **Upstream dependency:** Master Control Matrix (00_FOUNDATION) defines 35 control taxonomy; Governance Charter (Layer 04) establishes control governance authority; Framework Mappings defines ISO 27001/COBIT/OWASP alignment
- **Downstream usage:** Internal Audit Procedure (Layer 06) references control objectives for audit scope; Maturity Assessment (Layer 03) evaluates control implementation maturity; Statement of Applicability (Layer 01) maps controls to organizational requirements
- **Cross-layer reference:** AI Governance Framework (Layer 05) implements AI-LC-01 and AI-RISK-01 controls; API Governance Framework (Layer 05) implements API-SEC-01 and API-LC-01 controls; Developer Governance Layer (Layer 08) implements DEV domain controls

## Governance Principles

1. **Control Clarity** – Every control objective documented with specific requirements and measurable evidence for audit defensibility
2. **Evidence-Based Assurance** – All controls require defined evidence artifacts to demonstrate compliance without ambiguity
3. **Risk-Based Implementation** – Control applicability scaled by organizational context, team size, and risk appetite per Governance by Team Size model
4. **Ownership Accountability** – Every control assigned to designated owner role responsible for implementation and evidence production
5. **Scalable Application** – Controls adapted across Startup (4 controls), SaaS (10 controls), Enterprise (35 controls) editions without sacrificing governance rigor

## Technical Implementation

### Control Taxonomy

All controls use the EATGF naming convention:

```
EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]
```

**Domain Summary:**

| Domain                              | Code | Controls | Scope                                                        |
| ----------------------------------- | ---- | -------- | ------------------------------------------------------------ |
| Enterprise Direction and Management | EDM  | 3        | Strategy, risk oversight, benefit realization                |
| Align, Plan and Organise            | APO  | 4        | Architecture, risk operations, security planning, AI policy  |
| Build, Acquire and Implement        | BAI  | 3        | Change, configuration, test management                       |
| Deliver, Service and Support        | DSS  | 4        | IAM, encryption, vulnerability management, incident response |
| Monitor, Evaluate and Assess        | MEA  | 3        | Audit, performance, maturity                                 |
| Artificial Intelligence             | AI   | 2        | AI lifecycle, AI risk and bias                               |
| Application Programming Interface   | API  | 2        | API security, API lifecycle                                  |
| Cloud                               | CLD  | 4        | Architecture, security, monitoring, resilience               |
| Development                         | DEV  | 4        | SDLC, code scanning, supply chain, CI/CD                     |
| Data                                | DATA | 3        | Privacy, retention, minimization                             |
| Business Continuity Planning        | BCP  | 3        | Planning, testing, RTO/RPO                                   |
| **Total**                           |      | **35**   |                                                              |

**How to Read Control Entries:**

Each control entry follows this structure:

- **Objective** – The governance outcome the control achieves
- **Control Requirements** – The specific activities and conditions that must be in place
- **Evidence Requirements** – The artifacts required to demonstrate compliance
- **Applicability** – The organizational contexts and team sizes where the control applies

### Control Reference Index

| Control ID         | Domain | Short Title                    |
| ------------------ | ------ | ------------------------------ |
| EATGF-EDM-RISK-01  | EDM    | IT Risk Direction              |
| EATGF-EDM-BEN-01   | EDM    | Benefits Realization           |
| EATGF-EDM-GOV-01   | EDM    | Governance Framework Oversight |
| EATGF-APO-ARCH-01  | APO    | Enterprise Architecture        |
| EATGF-APO-RISK-01  | APO    | Operational Risk Process       |
| EATGF-APO-SEC-01   | APO    | Security Strategy              |
| EATGF-APO-AI-01    | APO    | AI Strategy and Policy         |
| EATGF-BAI-CHG-01   | BAI    | Change Management              |
| EATGF-BAI-CONF-01  | BAI    | Configuration Management       |
| EATGF-BAI-TEST-01  | BAI    | Test Management                |
| EATGF-DSS-SEC-01   | DSS    | Identity and Access Management |
| EATGF-DSS-ENC-01   | DSS    | Encryption Standards           |
| EATGF-DSS-VULN-01  | DSS    | Vulnerability Management       |
| EATGF-DSS-INC-01   | DSS    | Incident Response              |
| EATGF-MEA-AUD-01   | MEA    | Internal Audit                 |
| EATGF-MEA-PERF-01  | MEA    | Performance Monitoring         |
| EATGF-MEA-MAT-01   | MEA    | Maturity Assessment            |
| EATGF-AI-LC-01     | AI     | AI Lifecycle Governance        |
| EATGF-AI-RISK-01   | AI     | AI Risk and Bias Management    |
| EATGF-API-SEC-01   | API    | API Security                   |
| EATGF-API-LC-01    | API    | API Lifecycle Management       |
| EATGF-CLD-ARCH-01  | CLD    | Cloud Architecture             |
| EATGF-CLD-SEC-01   | CLD    | Cloud Security                 |
| EATGF-CLD-MON-01   | CLD    | Cloud Monitoring               |
| EATGF-CLD-RES-01   | CLD    | Cloud Resilience               |
| EATGF-DEV-SDLC-01  | DEV    | Secure SDLC                    |
| EATGF-DEV-SCAN-01  | DEV    | Code Scanning                  |
| EATGF-DEV-SUP-01   | DEV    | Supply Chain Security          |
| EATGF-DEV-CI-01    | DEV    | CI/CD Governance               |
| EATGF-DATA-PRIV-01 | DATA   | Data Privacy                   |
| EATGF-DATA-RET-01  | DATA   | Data Retention                 |
| EATGF-DATA-MIN-01  | DATA   | Data Minimization              |
| EATGF-BCP-PLAN-01  | BCP    | Business Continuity Planning   |
| EATGF-BCP-TEST-01  | BCP    | Business Continuity Testing    |
| EATGF-BCP-RTO-01   | BCP    | RTO/RPO Targets                |

### EDM — Enterprise Direction and Management

#### EATGF-EDM-RISK-01: IT Risk Direction

**Objective:** Establish enterprise-level direction for IT risk management, ensuring risk appetite and risk tolerance are defined, communicated, and enforced across all technology domains.

**Control Requirements:**

- Define and document risk appetite at the board level
- Communicate risk appetite to all teams and technology owners
- Conduct annual risk appetite review aligned with strategic planning
- Maintain alignment between risk direction and EATGF control implementation

**Evidence Requirements:**

- Board-approved risk appetite statement
- Minutes of annual risk appetite review
- Risk tolerance thresholds documented per domain

**Applicability:** All organizations. Scaled guidance available in Governance by Team Size model.

#### EATGF-EDM-BEN-01: Benefits Realization

**Objective:** Ensure that IT investments and governance initiatives deliver measurable business value.

**Control Requirements:**

- Establish benefits realization tracking for governance program
- Define key performance indicators (KPIs) for each investment
- Conduct post-implementation benefits review within 6 months of deployment

**Evidence Requirements:**

- Benefits register with KPIs and targets
- Post-implementation review reports
- Annual benefits realization summary

**Applicability:** Organizations with formal IT investment programs. Optional for teams of 10 or fewer.

#### EATGF-EDM-GOV-01: Governance Framework Oversight

**Objective:** Provide strategic oversight of the governance framework, ensuring it remains current, effective, and aligned with organizational objectives.

**Control Requirements:**

- Annual governance framework review by Governance Council
- Quarterly monitoring of framework adoption metrics
- Board-level reporting on governance maturity

**Evidence Requirements:**

- Annual framework review report
- Governance adoption dashboard
- Board presentation materials

**Applicability:** All organizations implementing EATGF.

### APO — Align, Plan and Organise

#### EATGF-APO-ARCH-01: Enterprise Architecture

**Objective:** Establish and maintain an enterprise architecture practice that ensures technology decisions align with business strategy and governance requirements.

**Control Requirements:**

- Maintain enterprise architecture documentation (current state and target state)
- Ensure all new technology decisions include architecture review
- Conduct architecture review board meetings at least quarterly
- Align architecture decisions with EATGF control requirements

**Evidence Requirements:**

- Architecture decision records
- Architecture review board meeting minutes
- Current-state and target-state architecture diagrams

**Applicability:** All organizations. Lightweight architecture documentation is acceptable for teams of 20 or fewer.

#### EATGF-APO-RISK-01: Operational Risk Process

**Objective:** Implement and maintain operational risk management processes that identify, assess, and mitigate technology risks.

**Control Requirements:**

- Maintain an operational risk register
- Conduct quarterly risk assessments
- Assign risk owners for all identified risks
- Track mitigation actions to completion

**Evidence Requirements:**

- Risk register (current, with owner assignments)
- Quarterly risk assessment reports
- Mitigation action tracking log

**Applicability:** All organizations. Risk assessment frequency may be reduced to semi-annual for teams of 10 or fewer.

#### EATGF-APO-SEC-01: Security Strategy

**Objective:** Define and maintain a security strategy that aligns with organizational risk appetite and regulatory requirements.

**Control Requirements:**

- Publish an information security policy aligned with ISO 27001:2022
- Conduct annual security strategy review
- Maintain security roadmap with quarterly milestones
- Ensure security strategy covers all EATGF domains

**Evidence Requirements:**

- Information security policy (approved)
- Security strategy document
- Annual security strategy review report

**Applicability:** All organizations.

#### EATGF-APO-AI-01: AI Strategy and Policy

**Objective:** Establish governance direction for AI initiatives, including ethical frameworks, risk management, and compliance with ISO 42001:2023.

**Control Requirements:**

- Publish an AI governance policy
- Define AI risk appetite and acceptable use boundaries
- Establish AI ethics review board or committee
- Maintain AI model inventory with risk categorization

**Evidence Requirements:**

- AI governance policy (approved)
- AI model inventory
- AI ethics review board charter and meeting minutes

**Applicability:** Organizations deploying or developing AI systems. Not applicable to organizations without AI capability.

### BAI — Build, Acquire and Implement

#### EATGF-BAI-CHG-01: Change Management

**Objective:** Ensure all changes to production systems are authorized, documented, tested, and traceable.

**Control Requirements:**

- Implement a formal change management process
- Require change approval prior to production deployment
- Maintain a change log with rollback procedures
- Conduct post-implementation reviews for significant changes

**Evidence Requirements:**

- Change request records (approved)
- Change log with deployment timestamps
- Post-implementation review reports

**Applicability:** All organizations. Lightweight change tracking is acceptable for teams of 5 or fewer.

#### EATGF-BAI-CONF-01: Configuration Management

**Objective:** Maintain accurate and current configuration records for all managed assets.

**Control Requirements:**

- Implement a configuration management database (CMDB) or equivalent
- Conduct quarterly configuration audits
- Ensure all infrastructure changes are reflected in configuration records

**Evidence Requirements:**

- CMDB or asset registry (current)
- Quarterly configuration audit reports
- Configuration change log

**Applicability:** All organizations. Spreadsheet-based tracking is acceptable for small teams.

#### EATGF-BAI-TEST-01: Test Management

**Objective:** Ensure all changes and new deployments are adequately tested before release.

**Control Requirements:**

- Define test strategy covering unit, integration, and acceptance testing
- Require test evidence before production release approval
- Maintain test results with traceability to requirements
- Conduct security testing for changes affecting authentication, authorization, or data handling

**Evidence Requirements:**

- Test strategy document
- Test execution reports
- Defect tracking records

**Applicability:** All organizations deploying software. Manual testing is acceptable for teams without automated test frameworks.

### DSS — Deliver, Service and Support

#### EATGF-DSS-SEC-01: Identity and Access Management

**Objective:** Ensure that access to systems and data is restricted to authorized individuals, using the principle of least privilege.

**Control Requirements:**

- Implement role-based access control (RBAC) across all systems
- Conduct quarterly access reviews
- Enforce multi-factor authentication (MFA) for privileged and remote access
- Implement automated provisioning and deprovisioning

**Evidence Requirements:**

- RBAC policy and role definitions
- Quarterly access review reports
- MFA deployment evidence
- Provisioning/deprovisioning audit logs

**Applicability:** All organizations.

#### EATGF-DSS-ENC-01: Encryption Standards

**Objective:** Protect data confidentiality and integrity through encryption at rest and in transit.

**Control Requirements:**

- Encrypt all data at rest using AES-256 or equivalent
- Enforce TLS 1.2 or higher for all data in transit
- Implement key management procedures aligned with industry standards
- Conduct annual cryptographic review

**Evidence Requirements:**

- Encryption configuration evidence
- Key management procedures document
- Annual cryptographic review report

**Applicability:** All organizations processing sensitive or regulated data.

#### EATGF-DSS-VULN-01: Vulnerability Management

**Objective:** Identify, assess, and remediate vulnerabilities across all managed systems within defined timelines.

**Control Requirements:**

- Conduct monthly vulnerability scans across all production systems
- Define remediation SLAs by vulnerability severity (per VULNERABILITY_REMEDIATION_TERMINOLOGY.md: Critical: 24 hours end-to-end, High: 1 week, Medium: 1 month, Low: 3 months)
- Track remediation to completion
- Report vulnerability metrics to Governance Council quarterly

**Evidence Requirements:**

- Monthly vulnerability scan reports
- Remediation tracking log with SLA compliance
- Quarterly vulnerability dashboard

**Applicability:** All organizations with externally facing or production systems.

#### EATGF-DSS-INC-01: Incident Response

**Objective:** Ensure that security incidents are detected, contained, and resolved according to documented procedures, with root cause analysis conducted for significant incidents.

**Control Requirements:**

- Maintain an incident response plan
- Define incident severity levels and escalation procedures
- Conduct post-incident reviews for all Severity 1 and 2 incidents
- Conduct annual incident response tabletop exercises

**Evidence Requirements:**

- Incident response plan (approved)
- Incident log with severity classification
- Post-incident review reports
- Tabletop exercise records

**Applicability:** All organizations.

### MEA — Monitor, Evaluate and Assess

#### EATGF-MEA-AUD-01: Internal Audit

**Objective:** Provide independent assurance that controls are operating effectively through periodic audit activities.

**Control Requirements:**

- Establish an annual audit plan covering all EATGF domains
- Conduct audits using the internal audit procedure (EATGF Layer 6)
- Track audit findings to remediation
- Report audit results to Governance Council

**Evidence Requirements:**

- Annual audit plan
- Audit reports with findings
- Audit finding remediation tracker

**Applicability:** All organizations. External audit may substitute for internal audit in organizations without a dedicated audit function.

#### EATGF-MEA-PERF-01: Performance Monitoring

**Objective:** Measure and report on the performance of governance controls and technology operations against defined KPIs.

**Control Requirements:**

- Define KPIs for all critical governance processes
- Collect and report KPI data monthly
- Conduct quarterly performance reviews
- Initiate corrective action when KPIs fall below threshold

**Evidence Requirements:**

- KPI definitions and thresholds
- Monthly KPI reports
- Quarterly performance review minutes

**Applicability:** All organizations. KPI scope may be reduced for teams of 10 or fewer.

#### EATGF-MEA-MAT-01: Maturity Assessment

**Objective:** Assess organizational governance maturity periodically and identify improvement priorities.

**Control Requirements:**

- Conduct annual maturity assessment using the EATGF Maturity Model (Layer 3)
- Assess maturity across all 11 EATGF domains
- Define improvement targets and track progress
- Report maturity scoring to Governance Council

**Evidence Requirements:**

- Annual maturity assessment report
- Maturity scoring by domain
- Improvement action plan

**Applicability:** All organizations implementing EATGF.

### AI — Artificial Intelligence

#### EATGF-AI-LC-01: AI Lifecycle Governance

**Objective:** Govern the full lifecycle of AI systems from design through deployment and decommission, ensuring compliance with ISO 42001:2023.

**Control Requirements:**

- Maintain an AI model inventory with lifecycle stage tracking
- Require impact assessment before AI model deployment
- Implement model monitoring for drift, performance degradation, and fairness
- Conduct annual review of all deployed AI models
- Define decommission criteria and procedures

**Evidence Requirements:**

- AI model inventory (current)
- Pre-deployment impact assessments
- Model monitoring dashboards
- Annual AI model review reports

**Applicability:** Organizations deploying AI/ML systems.

#### EATGF-AI-RISK-01: AI Risk and Bias Management

**Objective:** Identify, assess, and mitigate AI-specific risks including bias, fairness, explainability, and safety.

**Control Requirements:**

- Conduct bias testing during model development and before deployment
- Define fairness thresholds (e.g., disparate impact ratio above 0.80)
- Implement explainability documentation for all high-risk AI models
- Monitor production models for bias drift
- Maintain an AI risk register distinct from the general risk register

**Evidence Requirements:**

- Bias testing reports
- Fairness threshold documentation
- Explainability reports for high-risk models
- AI risk register

**Applicability:** Organizations deploying AI/ML systems, especially in regulated sectors or high-risk use cases.

### API — Application Programming Interface

#### EATGF-API-SEC-01: API Security

**Objective:** Ensure all APIs are secured against OWASP API Security Top 10 risks and enforce authentication, authorization, and rate limiting.

**Control Requirements:**

- Implement API gateway with authentication and rate limiting
- Enforce OAuth 2.0 or equivalent for API authentication
- Conduct API security testing aligned with OWASP ASVS 4.0
- Monitor API traffic for anomalous patterns

**Evidence Requirements:**

- API gateway configuration evidence
- API security test reports
- API traffic monitoring dashboards

**Applicability:** Organizations exposing or consuming APIs.

#### EATGF-API-LC-01: API Lifecycle Management

**Objective:** Govern the full lifecycle of APIs from design through deprecation, ensuring version control, documentation, and consumer communication.

**Control Requirements:**

- Maintain an API catalog with version, owner, and status
- Define API deprecation policy with minimum notice period
- Publish API documentation (e.g., OpenAPI specifications)
- Conduct quarterly API portfolio review

**Evidence Requirements:**

- API catalog (current)
- API deprecation notices
- API documentation (published)
- Quarterly API review minutes

**Applicability:** Organizations managing 5 or more APIs. Optional for smaller API portfolios.

### CLD — Cloud

#### EATGF-CLD-ARCH-01: Cloud Architecture

**Objective:** Ensure cloud deployments follow a well-architected framework aligned with organizational standards.

**Control Requirements:**

- Define cloud architecture standards (e.g., landing zone design)
- Require architecture review for all new cloud workloads
- Maintain cloud architecture documentation
- Conduct annual well-architected review

**Evidence Requirements:**

- Cloud architecture standards document
- Cloud architecture review records
- Annual well-architected review report

**Applicability:** Organizations using public or hybrid cloud.

#### EATGF-CLD-SEC-01: Cloud Security

**Objective:** Implement cloud-specific security controls covering identity, network segmentation, logging, and data protection.

**Control Requirements:**

- Implement cloud-native identity and access management
- Enforce network segmentation and security groups
- Enable cloud audit logging across all accounts
- Implement data protection controls (encryption, DLP)

**Evidence Requirements:**

- Cloud IAM configuration evidence
- Network segmentation documentation
- Cloud audit log retention evidence
- Data protection configuration evidence

**Applicability:** All organizations using cloud services.

#### EATGF-CLD-MON-01: Cloud Monitoring

**Objective:** Ensure real-time monitoring of cloud resources for performance, availability, and security events.

**Control Requirements:**

- Implement cloud monitoring covering compute, storage, network
- Define alerting thresholds and escalation procedures
- Retain monitoring data for a minimum of 12 months
- Conduct monthly cloud monitoring review

**Evidence Requirements:**

- Cloud monitoring configuration evidence
- Alerting threshold documentation
- Monthly monitoring review reports

**Applicability:** All organizations using cloud services.

#### EATGF-CLD-RES-01: Cloud Resilience

**Objective:** Ensure cloud workloads are designed for resilience with defined availability targets and failover procedures.

**Control Requirements:**

- Define availability targets for all cloud workloads
- Implement multi-availability-zone or multi-region deployments for critical workloads
- Conduct annual failover testing
- Maintain cloud disaster recovery documentation

**Evidence Requirements:**

- Availability target documentation
- Multi-AZ/region deployment evidence
- Failover test reports
- Cloud DR documentation

**Applicability:** Organizations with production workloads in cloud.

### DEV — Development

#### EATGF-DEV-SDLC-01: Secure SDLC

**Objective:** Embed security practices throughout the software development lifecycle.

**Control Requirements:**

- Define secure development standards
- Require threat modeling for new applications
- Conduct security reviews at design and pre-deployment gates
- Provide security training for all developers annually

**Evidence Requirements:**

- Secure development standards document
- Threat model records
- Security gate review records
- Developer security training records

**Applicability:** All organizations developing software.

#### EATGF-DEV-SCAN-01: Code Scanning

**Objective:** Detect and remediate code-level security vulnerabilities through static and dynamic analysis.

**Control Requirements:**

- Implement SAST (static application security testing) in CI/CD pipeline
- Implement DAST (dynamic application security testing) for deployed applications
- Define remediation SLAs by severity
- Track scanning coverage across all repositories

**Evidence Requirements:**

- SAST configuration and scan reports
- DAST scan reports
- Remediation tracking log
- Coverage metrics

**Applicability:** All organizations developing software. DAST may be deferred for internal-only applications.

#### EATGF-DEV-SUP-01: Supply Chain Security

**Objective:** Manage risks associated with third-party software dependencies and open-source components.

**Control Requirements:**

- Generate software bill of materials (SBOM) for all applications
- Monitor dependencies for known vulnerabilities
- Define approved and prohibited dependency lists
- Conduct quarterly dependency review

**Evidence Requirements:**

- SBOM records
- Dependency vulnerability reports
- Approved/prohibited dependency lists
- Quarterly dependency review minutes

**Applicability:** All organizations using third-party or open-source dependencies.

#### EATGF-DEV-CI-01: CI/CD Governance

**Objective:** Ensure CI/CD pipelines enforce governance gates including security scanning, testing, and approval workflows.

**Control Requirements:**

- Implement governance gates in CI/CD pipelines (build, test, scan, approve, deploy)
- Require human approval for production deployments
- Maintain pipeline configuration in version control
- Audit pipeline execution logs

**Evidence Requirements:**

- Pipeline configuration records (in version control)
- Deployment approval records
- Pipeline execution audit logs

**Applicability:** All organizations using CI/CD. Manual deployment processes require equivalent governance controls.

### DATA — Data

#### EATGF-DATA-PRIV-01: Data Privacy

**Objective:** Ensure personal and sensitive data is processed in accordance with applicable privacy legislation and organizational policy.

**Control Requirements:**

- Maintain a data processing inventory (register of processing activities)
- Conduct data protection impact assessments (DPIAs) for high-risk processing
- Implement data subject rights procedures
- Define and enforce data classification scheme

**Evidence Requirements:**

- Data processing inventory
- DPIA records
- Data subject request log
- Data classification policy

**Applicability:** All organizations processing personal data.

#### EATGF-DATA-RET-01: Data Retention

**Objective:** Ensure data is retained for the period required by regulation and business need, and securely disposed of thereafter.

**Control Requirements:**

- Define data retention schedule by data category
- Implement automated retention enforcement where feasible
- Conduct annual retention compliance review
- Maintain evidence of secure data disposal

**Evidence Requirements:**

- Data retention schedule
- Retention enforcement configuration evidence
- Annual retention review report
- Disposal certificates or logs

**Applicability:** All organizations.

#### EATGF-DATA-MIN-01: Data Minimization

**Objective:** Ensure that only the minimum data necessary for the stated purpose is collected and retained.

**Control Requirements:**

- Define data minimization principles in data governance policy
- Review data collection practices annually
- Implement technical controls to limit data collection
- Report data minimization metrics to Governance Council

**Evidence Requirements:**

- Data governance policy (with minimization section)
- Annual data collection review report
- Data minimization metrics

**Applicability:** All organizations processing personal or sensitive data.

### BCP — Business Continuity Planning

#### EATGF-BCP-PLAN-01: Business Continuity Planning

**Objective:** Ensure the organization has documented business continuity plans for critical technology services.

**Control Requirements:**

- Develop and maintain business continuity plans for all critical services
- Define critical service inventory with business impact analysis
- Conduct annual BCP review and update
- Ensure BCP covers technology, people, and process

**Evidence Requirements:**

- Business continuity plans (approved)
- Critical service inventory
- Business impact analysis
- Annual BCP review records

**Applicability:** All organizations.

#### EATGF-BCP-TEST-01: Business Continuity Testing

**Objective:** Validate business continuity plans through periodic testing exercises.

**Control Requirements:**

- Conduct annual business continuity test (tabletop or failover)
- Document test results including gaps identified
- Update BCP based on test findings
- Report test results to Governance Council

**Evidence Requirements:**

- BCP test plan and results
- Gap analysis from testing
- BCP update records post-test

**Applicability:** All organizations. Tabletop exercises are acceptable for organizations without dedicated DR infrastructure.

#### EATGF-BCP-RTO-01: RTO/RPO Targets

**Objective:** Define and validate recovery time objectives (RTO) and recovery point objectives (RPO) for all critical services.

**Control Requirements:**

- Define RTO and RPO targets for each critical service
- Validate RTO/RPO targets through testing
- Ensure backup and recovery mechanisms support defined targets
- Report RTO/RPO compliance to Governance Council

**Evidence Requirements:**

- RTO/RPO target documentation
- Test results validating RTO/RPO achievability
- Backup and recovery configuration evidence

**Applicability:** All organizations with critical technology services.

### Implementation Summary

| Control ID         | Domain | Objective Summary                  | Evidence Type                 | Review Frequency | Owner                |
| ------------------ | ------ | ---------------------------------- | ----------------------------- | ---------------- | -------------------- |
| EATGF-EDM-RISK-01  | EDM    | IT risk direction and appetite     | Risk appetite statement       | Annual           | Board/CRO            |
| EATGF-EDM-BEN-01   | EDM    | Benefits realization tracking      | Benefits register             | Annual           | CFO                  |
| EATGF-EDM-GOV-01   | EDM    | Governance framework oversight     | Framework review report       | Annual           | Governance Council   |
| EATGF-APO-ARCH-01  | APO    | Enterprise architecture management | Architecture decision records | Quarterly        | Enterprise Architect |
| EATGF-APO-RISK-01  | APO    | Operational risk process           | Risk register                 | Quarterly        | Risk Manager         |
| EATGF-APO-SEC-01   | APO    | Security strategy alignment        | Security policy               | Annual           | CISO                 |
| EATGF-APO-AI-01    | APO    | AI strategy and policy             | AI governance policy          | Annual           | AI Governance Lead   |
| EATGF-BAI-CHG-01   | BAI    | Change management                  | Change request records        | Per change       | Change Manager       |
| EATGF-BAI-CONF-01  | BAI    | Configuration management           | CMDB/asset registry           | Quarterly        | IT Operations        |
| EATGF-BAI-TEST-01  | BAI    | Test management                    | Test execution reports        | Per release      | QA Lead              |
| EATGF-DSS-SEC-01   | DSS    | Identity and access management     | Access review reports         | Quarterly        | IAM Lead             |
| EATGF-DSS-ENC-01   | DSS    | Encryption standards               | Encryption configuration      | Annual           | Security Engineer    |
| EATGF-DSS-VULN-01  | DSS    | Vulnerability management           | Scan reports                  | Monthly          | Security Operations  |
| EATGF-DSS-INC-01   | DSS    | Incident Response                  | Incident log                  | Per incident     | Incident Manager     |
| EATGF-MEA-AUD-01   | MEA    | Internal audit                     | Audit reports                 | Annual           | Internal Audit       |
| EATGF-MEA-PERF-01  | MEA    | Performance monitoring             | KPI reports                   | Monthly          | Governance Office    |
| EATGF-MEA-MAT-01   | MEA    | Maturity assessment                | Maturity assessment report    | Annual           | Governance Office    |
| EATGF-AI-LC-01     | AI     | AI lifecycle governance            | AI model inventory            | Annual           | AI Governance Lead   |
| EATGF-AI-RISK-01   | AI     | AI risk and bias management        | Bias testing reports          | Per deployment   | AI Ethics Board      |
| EATGF-API-SEC-01   | API    | API security                       | API security test reports     | Quarterly        | API Lead             |
| EATGF-API-LC-01    | API    | API lifecycle management           | API catalog                   | Quarterly        | API Lead             |
| EATGF-CLD-ARCH-01  | CLD    | Cloud architecture                 | Architecture review records   | Annual           | Cloud Architect      |
| EATGF-CLD-SEC-01   | CLD    | Cloud security                     | Cloud IAM config evidence     | Quarterly        | Cloud Security       |
| EATGF-CLD-MON-01   | CLD    | Cloud monitoring                   | Monitoring review reports     | Monthly          | Cloud Operations     |
| EATGF-CLD-RES-01   | CLD    | Cloud resilience                   | Failover test reports         | Annual           | Cloud Operations     |
| EATGF-DEV-SDLC-01  | DEV    | Secure SDLC                        | Threat model records          | Per application  | Dev Lead             |
| EATGF-DEV-SCAN-01  | DEV    | Code scanning                      | SAST/DAST scan reports        | Per release      | Security Engineering |
| EATGF-DEV-SUP-01   | DEV    | Supply chain security              | SBOM records                  | Quarterly        | Dev Lead             |
| EATGF-DEV-CI-01    | DEV    | CI/CD governance                   | Pipeline audit logs           | Per deployment   | DevOps Lead          |
| EATGF-DATA-PRIV-01 | DATA   | Data privacy                       | Data processing inventory     | Annual           | DPO                  |
| EATGF-DATA-RET-01  | DATA   | Data retention                     | Retention schedule            | Annual           | Data Governance      |
| EATGF-DATA-MIN-01  | DATA   | Data minimization                  | Data collection review        | Annual           | Data Governance      |
| EATGF-BCP-PLAN-01  | BCP    | Business continuity planning       | BCP documents                 | Annual           | BC Manager           |
| EATGF-BCP-TEST-01  | BCP    | Business continuity testing        | BCP test results              | Annual           | BC Manager           |
| EATGF-BCP-RTO-01   | BCP    | RTO/RPO targets                    | RTO/RPO validation results    | Annual           | BC Manager           |

## Control Mapping

### ISO 27001:2022 Annex A

EATGF covers 93% of ISO 27001:2022 Annex A controls:

- **A.5 Organizational Controls** – Mapped to EDM and APO domains
- **A.6 People Controls** – Covered by DSS-SEC-01 (IAM) and training requirements across DEV
- **A.7 Physical Controls** – Not explicitly covered; organizations implement per context
- **A.8 Technological Controls** – Comprehensive coverage via DSS, DEV, CLD, API domains

### ISO 42001:2023 AI Management System

EATGF AI domain (AI-LC-01, AI-RISK-01) aligns with ISO 42001:2023:

- **Clause 5 Leadership** – APO-AI-01 establishes AI governance policy and ethics board
- **Clause 6 Planning** – AI-LC-01 requires impact assessments before deployment
- **Clause 8 Operation** – AI-RISK-01 implements bias testing and fairness monitoring
- **Clause 9 Performance Evaluation** – MEA-PERF-01 monitors AI system performance
- **Clause 10 Improvement** – AI-LC-01 annual reviews drive continuous improvement

### COBIT 2019

EATGF domains directly map to COBIT 2019 process areas:

- **EDM (Evaluate, Direct, Monitor)** – EATGF EDM domain
- **APO (Align, Plan, Organise)** – EATGF APO domain
- **BAI (Build, Acquire, Implement)** – EATGF BAI domain
- **DSS (Deliver, Service, Support)** – EATGF DSS domain
- **MEA (Monitor, Evaluate, Assess)** – EATGF MEA domain

### OWASP Standards

- **OWASP ASVS 4.0** – Referenced in DEV-SCAN-01 (code scanning) and API-SEC-01 (API security testing)
- **OWASP API Security Top 10:2023** – Covered 100% by API-SEC-01 control requirements
- **OWASP Top 10 Web Application Risks** – Addressed through DEV domain controls (SDLC, scanning, CI/CD)

## Developer Checklist

Before implementing EATGF controls:

- [ ] Review control applicability for organizational context using Governance by Team Size model
- [ ] Identify control owners for all applicable controls from Implementation Summary table
- [ ] Map required evidence artifacts to existing operational systems and processes
- [ ] Establish evidence collection procedures for quarterly and annual review cycles
- [ ] Configure CMDB or asset tracking system for BAI-CONF-01 configuration management
- [ ] Implement risk register for APO-RISK-01 and EDM-RISK-01 risk management processes
- [ ] Deploy AI model inventory for organizations with AI systems (AI-LC-01, AI-RISK-01)
- [ ] Configure API catalog for organizations managing 5+ APIs (API-LC-01)
- [ ] Establish audit plan covering all applicable EATGF domains for MEA-AUD-01
- [ ] Define KPIs for performance monitoring per MEA-PERF-01 requirements
- [ ] Schedule annual maturity assessment using EATGF Maturity Model (Layer 03)
- [ ] Integrate control objectives into Statement of Applicability document (Layer 01)
- [ ] Train control owners on evidence requirements and review procedures
- [ ] Establish governance reporting cadence (monthly KPIs, quarterly risk reviews, annual audits)

## Governance Implications

### Control Authority and Ownership

- Master Control Matrix (MCM) in Layer 00_FOUNDATION is single source of truth for control taxonomy
- Control owners designated in Implementation Summary table are accountable for control implementation and evidence production
- Governance Council has authority to approve control exceptions documented in Statement of Applicability
- Board-level controls (EDM domain) require executive or board sign-off

### Evidence Chain and Audit Trail

- All evidence requirements listed in this document are minimum for compliance demonstration
- Evidence artifacts must be retained per organizational retention schedule (minimum 3 years recommended)
- Internal Audit Procedure (Layer 06) references these control objectives for audit scope and testing
- Audit findings must reference specific control ID in remediation tracking

### Control Exception Handling

- Control exceptions require documented business justification and risk acceptance
- Exceptions approved by Governance Council and documented in Statement of Applicability
- All exceptions reviewed annually during governance framework oversight (EDM-GOV-01)
- Compensating controls required when baseline control not applicable

### Scalability and Edition Progression

- **Startup Edition:** Implement 4 baseline controls (EDM-RISK-01, DSS-SEC-01, DSS-VULN-01, MEA-AUD-01)
- **SaaS Edition:** Implement 10 controls adding API, Cloud, and Development domains
- **Enterprise Edition:** Full 35-control implementation across all 11 domains
- Organizations progress through editions as maturity and complexity increase

## Official References

- **ISO/IEC 27001:2022** – Information Security Management Systems, Requirements (ISO, 2022)
- **ISO/IEC 27002:2022** – Code of Practice for Information Security Controls (ISO, 2022)
- **ISO/IEC 42001:2023** – Artificial Intelligence Management System (ISO, 2023)
- **COBIT 2019** – Framework for Governance and Management of Enterprise IT (ISACA, 2019)
- **OWASP ASVS 4.0** – Application Security Verification Standard (OWASP, 2019)
- **OWASP API Security Top 10:2023** – API Security Risks (OWASP, 2023)
- **NIST SP 800-53 Rev. 5** – Security and Privacy Controls for Information Systems (NIST, 2020)
