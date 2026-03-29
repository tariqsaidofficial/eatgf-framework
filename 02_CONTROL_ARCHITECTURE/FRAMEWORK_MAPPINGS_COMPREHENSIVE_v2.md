# FRAMEWORK_MAPPINGS_COMPREHENSIVE

| Field | Value |
|-------|-------|
| Document Type | Technical Mapping Reference |
| Version | 2.0 |
| Classification | Controlled |
| Effective Date | 2026-02-14 |
| Authority | Enterprise Architecture and Governance Office |
| EATGF Layer | 02_CONTROL_ARCHITECTURE |
| MCM Reference | All 35 EATGF Controls |
| Standards | COBIT 2019, ISO 27001:2022, ISO 42001:2023, NIST AI RMF, NIST SP 800-53, OWASP 2023 |

---

## Purpose

This document provides authoritative bidirectional mappings between EATGF Master Control Matrix (35 controls) and external frameworks: COBIT 2019, ISO 27001:2022 (76 Annex A controls), ISO 42001:2023, NIST AI RMF, OWASP 2023 standards, and NIST SP 800-53. These mappings enable unified control architecture implementation, single evidence collection satisfying multiple standards, audit readiness across ISO/COBIT/SOC 2 frameworks, and traceability from strategic governance to tactical controls.

## Architectural Position

This document operates within **02_CONTROL_ARCHITECTURE** as the comprehensive cross-framework mapping authority.

- **Upstream dependency:** Master Control Matrix (00_FOUNDATION) defines 35 EATGF controls as central hub; Control Objectives document specifies requirements for each control; Governance Charter (Layer 04 establishes control authority
- **Downstream usage:** Statement of Applicability (Layer 01) maps organizational context to standard requirements; Internal Audit Procedure (Layer 06) uses mappings to scope multi-framework audits; Maturity Assessment (Layer 03) evaluates implementation across mapped standards
- **Cross-layer reference:** Framework Mappings (basic) provides summary mappings; this document provides comprehensive detail for audit and compliance teams

## Governance Principles

1. **Central Hub Model** – EATGF MCM serves as central control authority; all external standards mapped TO the MCM (not vice versa) for unified governance
2. **Evidence Reuse** – Single control implementation with unified evidence collection satisfies multiple framework requirements simultaneously
3. **Audit Defensibility** – Explicit bidirectional mapping tables demonstrate compliance chain from EATGF control to ISO/COBIT/NIST requirements
4. **Edition Scalability** – Control applicability varies by organizational size (Startup/SaaS/Enterprise); mappings maintained across all editions
5. **Living Documentation** – Mappings updated semi-annually aligned with framework publication cycles (ISO amendments, COBIT updates, OWASP releases)

## Technical Implementation

### Mapping Architecture Model

EATGF MCM (35 controls) serves as central control authority with bidirectional mappings to:
- COBIT 2019 (Process domains: EDM, APO, BAI, DSS, MEA)
- ISO 27001:2022 (Information Security Management, 76 Annex A controls)
- ISO 42001:2023 (AI Management System, when applicable)
- NIST AI RMF (AI risk governance: GOVERN, MAP, MEASURE, MANAGE)
- OWASP 2023 (API Security Top 10, Application Security)
- NIST SP 800-53 (US government security controls, when applicable)

Key principle: EATGF MCM is central authority. This architecture simplifies control implementation, enables evidence reuse across standards, reduces redundancy, and provides unified governance dashboard.

### Control-Level Detailed Mappings

#### EDM Domain — Evaluate, Direct, Monitor

**EATGF-EDM-RISK-01: IT and AI Risk Appetite Definition**

Mapping Summary:

| Standard | Reference | Applicability | Evidence Linkage |
|----------|-----------|---------------|------------------|
| COBIT 2019 | EDM03 (Risk optimization) | All organizations | Risk tolerance statement |
| ISO 27001:2022 | Clause 6.1.2 (Risk assessment) | SaaS/Enterprise | SoA, risk assessment |
| ISO 42001:2023 | Clause 6 (Planning, risks/opportunities) | AI systems only | AI risk framework |
| NIST AI RMF | GOVERN-2 (Risk and benefit analysis) | AI systems only | AI governance document |

Detailed Mapping Structure:
- COBIT 2019: EDM03.01 (Evaluate current IT governance), EDM03.02 (Direct IT governance implementation), EDM03.03 (Monitor IT governance)
- ISO 27001:2022: Clause 6.1.2 (Risk assessment process), Clause 8.1 (Operational planning), Clause 9.1 (Monitoring)
- ISO 42001:2023: Clause 6.1 (Risks and opportunities), Clause 8.1 (Operational planning)
- NIST AI RMF: GOVERN-2 (Risk and benefit analysis), MEASURE-1 (Data validation processes)

Minimum Evidence Required:
- Board-approved Risk Appetite Statement (signed/dated)
- Risk tolerance thresholds (Critical/High/Medium/Low per category)
- AI-specific risk thresholds (if deploying AI systems)
- Data breach and compliance thresholds
- Annual review documentation

Owner: Chief Governance Officer / Chief Risk Officer  
Review Frequency: Annual

**EATGF-EDM-BEN-01: Technology Value and Benefits Monitoring**

Mapping Summary:

| Standard | Reference | Clauses | Applicability |
|----------|-----------|---------|---------------|
| COBIT 2019 | EDM02 (Benefits realization) | EDM02.01-03 | All organizations |
| ISO 27001:2022 | Clause 9.1 (Monitoring/measurement) | 9.1.1, 9.1.2 | SaaS/Enterprise |
| NIST AI RMF | MEASURE-1 | Performance metrics | AI systems only |

Mapping Logic:
- EDM02 (COBIT benefits realization oversight) aligns to ISO 27001 Clause 9.1 (monitoring and measurement)
- Governance KPIs (DORA metrics, security metrics, compliance metrics) serve as evidence for both standards
- Monthly dashboards feed quarterly board reporting requirements

**EATGF-EDM-GOV-01: Governance Model and Structure**

Mapping Summary:

| Standard | Reference | Mapping Type | Status |
|----------|-----------|--------------|--------|
| COBIT 2019 | EDM01 (Governance framework) | PRIMARY | Mapped |
| ISO 27001:2022 | Clause 5.3 (Roles/responsibilities) | SECONDARY | Mapped |
| ISO 42001:2023 | Clause 5.4 (Accountability) | CONDITIONAL | If AI systems |

Evidence Mapping Chain:
- Control Requirements: Governance Charter (2+ pages), RACI Matrix, Committee Charters (3+), Escalation Procedures, Approval Authority Matrix
- Satisfies: COBIT EDM01 (Governance structure), ISO 27001 Clause 5.3 (Roles/responsibilities), ISO 27001 Clause 5.2 (Information security policy), ISO 42001 Clause 5.4 (Accountability)

#### APO Domain — Align, Plan, Organize

**EATGF-APO-ARCH-01: Enterprise Architecture Framework**

Multi-Standard Mapping:

| COBIT 2019 | ISO 27001:2022 | NIST SP 800-53 | Evidence |
|------------|----------------|----------------|----------|
| APO03.02 (Architecture standards) | A.8.21 (Secure architecture) | N/A | Architecture standards document |
| APO03.03 (Current state) | Clause 5.4 (Responsibilities) | N/A | Current-state architecture diagrams |
| APO03.04 (Target state) | N/A | N/A | Target-state architecture diagrams |

Evidence Linkage:
- Architecture standards document (policies, patterns, controls)
- Architecture review board charter
- Current-state vs target-state architecture diagrams
- Control mapping to architecture decisions
- ARB decision log (monthly minimum)

Applicability Note: Mandatory for SaaS/Enterprise editions; optional for Startup edition (single-person teams may document informally).

**EATGF-APO-RISK-01: IT and AI Risk Register Management**

Comprehensive Mapping Structure:
- COBIT 2019 APO12 (Manage Risk): APO12.01 (Risk identification), APO12.02 (Risk assessment), APO12.03 (Risk response), APO12.04 (Risk monitoring), APO12.05 (Risk reporting)
- ISO 27001:2022 Clause 6.1.2: Risk assessment scope, Risk assessment methodology, Risk criteria, Risk analysis, Risk evaluation
- ISO 42001:2023 Clause 6.1.1: AI risk assessment, Mitigation planning
- NIST AI RMF GOVERN-1, MAP-1: Risk categorization, Measurement frameworks

Evidence Types Required:
- Risk register (spreadsheet or system with 50+ identified risks minimum)
- Risk assessment methodology documentation
- Risk heat map (Probability x Impact matrix)
- Top 10 Critical/High risk mitigation plans
- Monthly escalation tracking log
- Quarterly risk trending analysis

System Integration: Risk data feeds into SoA, audit planning, board reporting; reused by ISO 27001 RTO/RPO risk analysis; extended by AI risk assessment (if AI systems deployed).

**EATGF-APO-SEC-01: Information Security Management System (ISMS)**

Master Mapping (Extensive Alignment):

| COBIT 2019 | ISO 27001:2022 Clause | Scope |
|------------|----------------------|-------|
| APO13 (Manage Security) | Clauses 4-10 | Complete ISMS |
| APO13.01 | Clause 5 (Leadership) | Policy governance |
| APO13.02 | Clause 6 (Planning) | Risk planning |
| APO13.03 | Clause 7 (Support) | Resource allocation |
| APO13.04 | Clause 8 (Operations) | Control implementation |
| APO13.05 | Clause 9 (Performance evaluation) | Measurement |

Key Evidence Requirements:
- ISMS Manual (structured per ISO 27001 clauses 4-10)
- Statement of Applicability (SoA) with all 76 Annex A controls selected or excluded
- Information security policy suite (7-10 policies minimum)
- Risk assessment report
- Internal audit reports
- Corrective/preventive action tracking log
- Management review meeting documentation

Evidence Reuse Benefit: Single ISMS implementation satisfies both COBIT APO13 AND ISO 27001 requirements simultaneously; SoA directly supports audit readiness.

**EATGF-APO-AI-01: AI Governance System (AIMS)**

ISO 42001:2023 Primary Mapping:

| ISO 42001 Clause | COBIT Equivalent | Mapping |
|------------------|------------------|---------|
| Clause 4 (Context) | APO01 | Organization understanding |
| Clause 5 (Leadership) | APO04 | AI governance leadership |
| Clause 6 (Planning) | APO12 | AI risk planning |
| Clause 7 (Support) | APO08 | Resource management |
| Clause 8 (Operation) | BAI03 | AI system lifecycle |
| Clause 9 (Performance) | MEA01 | AI performance monitoring |
| Clause 10 (Improvement) | MEA03 | AI audit and review |

NIST AI RMF Alignment:

| NIST AI RMF Category | ISO 42001 Clause | Evidence |
|----------------------|------------------|----------|
| GOVERN | Clauses 5, 6 | AI governance charter |
| MAP | Clause 6 | AI risk mapping |
| MEASURE | Clause 9 | Model performance metrics |
| MANAGE | Clause 8 | AI lifecycle controls |

Evidence Structure Required:
- AIMS Manual (ISO 42001 template structure)
- AI System Registry (all AI systems catalogued)
- AI governance committee charter
- AI model documentation standard
- Fairness/bias assessment process
- Model performance monitoring dashboard
- AI incident response procedures

#### BAI Domain — Build, Acquire, Implement

**EATGF-BAI-CHG-01: Controlled Change Management**

Triple-Standard Mapping:

| Framework | Standard | Example Clause |
|-----------|----------|----------------|
| COBIT | BAI06 (Manage changes) | Change request and approval procedures |
| ISO 27001 | A.8.19 | Change approval procedures |
| NIST SP 800-53 | CM-3 | Configuration change control procedures |

Unified Evidence Approach (Single process satisfies all three):
- Engineering change log (JIRA/Azure DevOps/ServiceNow): Change request [BAI06, A.8.19], Risk assessment [BAI06], Approval gate [CM-3], Deployment record [all three]
- Change Advisory Board (CAB): Monthly meetings [BAI06.02], Approval authority [all three], Decision log [all three]
- Rollback testing: Recovery procedures [A.8.19], Test results [all three]

Integration Benefit: Change log serves as audit evidence for ISO 27001, SOC 2, and COBIT simultaneously; CAB minutes provide change impact assessment evidence; zero additional process overhead for multi-framework compliance.

**EATGF-BAI-CONF-01: Configuration and Version Control**

Mapping:

| COBIT 2019 | ISO 27001:2022 | Mapping |
|------------|----------------|---------|
| BAI10.01 (Configuration baselines) | A.8.9 (Asset management) | Configuration baselines |
| BAI10.02 (Configuration tracking) | A.8.9 | Configuration tracking |
| BAI10.03 (Configuration integrity) | A.8.9 | Configuration integrity |

Evidence Types Required:
- Git repository with branch protection rules enforced
- Commit history and signed commits (GPG signatures)
- Configuration baseline documentation
- Access control for code and configuration (RBAC implementation)
- Monthly audit of configuration changes
- Infrastructure-as-code documentation (Terraform/CloudFormation)

Satisfies: COBIT configuration management control objectives, ISO 27001 A.8.9 (Access to information and other assets), DevSecOps audit trail requirements.

**EATGF-BAI-TEST-01: Quality Assurance and Testing**

Multi-Platform Mapping:

| Framework | Reference | Element |
|-----------|-----------|---------|
| COBIT 2019 | BAI03 (Solutions implementation) | Configuration testing |
| ISO 27001:2022 | A.8.9 (Asset management) | Security testing requirements |
| NIST SP 800-53 | CA-2 (Security assessments) | Security assessment and authorization |
| OWASP | Testing Guide | SAST/DAST/SCA methodologies |

Evidence Portfolio Structure:
- Unit Test Results (70%+ code coverage required)
- Integration Tests (100% of API endpoints)
- Security Tests: SAST (per commit), DAST (pre-release), SCA (continuous dependency scanning)
- Performance Tests (comparison against baseline)
- UAT Sign-Off (business acceptance documentation)
- Security Scan Results (OWASP ZAP or similar scan reports)

Satisfies: COBIT BAI03, ISO 27001 A.8.9, OWASP testing practices, SOC 2 change management requirements.

#### DSS Domain — Deliver, Service, Support

**EATGF-DSS-SEC-01: Identity and Access Management (IAM)**

Universal Control (Applies to All Standards):

| Standard | Clause | Scope |
|----------|--------|-------|
| COBIT 2019 | DSS05 (Manage Identity and Access) | All access types |
| ISO 27001:2022 | A.5.15-A.5.18 | User access control |
| NIST SP 800-53 | AC-2, AC-3 | Account and access control |
| SOC 2 | CC6.1-6.2 | Logical access controls |

Control Architecture Components:
- Centralized identity platform (Okta/Azure AD/similar)
- Authentication: MFA required for sensitive systems, SSO for all cloud systems, passwordless authentication (future target)
- Authorization (RBAC): Role definitions per system, Access control matrix (RACI), Quarterly role review
- Provisioning: Automated provisioning (Okta/system connectors), Approval workflow
- Deprovisioning: Same-day removal on termination, Service account rotation
- Monitoring: Quarterly access review, 12-month audit log retention, Privileged access monitoring

Evidence Satisfies:
- COBIT DSS05 (5 control objectives)
- ISO 27001 A.5.15-A.5.18 (4 control objectives)
- NIST SP 800-53 AC-2, AC-3, AC-5
- SOC 2 CC6 (6 trust service criteria)
- Single audit examination for all frameworks

Evidence Reuse Efficiency: Okta dashboard serves as evidence for COBIT, ISO 27001, and SOC 2 simultaneously; quarterly access review satisfies compliance across all frameworks; audit logs provide single evidence source for 4+ frameworks.

**EATGF-DSS-ENC-01: Data Encryption and Protection**

Mapping:

| Framework | Reference | Requirement |
|-----------|-----------|-------------|
| COBIT 2019 | DSS07 (Cryptographic security) | Cryptographic key management |
| ISO 27001:2022 | A.10.1 (Cryptographic controls) | Cryptographic policy and key management |
| NIST SP 800-53 | SC-7, SC-28 | Boundary protection, protection of information at rest |

Evidence Structure:
- At-Rest Encryption: Database encryption (AES-256), Backup encryption (AES-256), Archive encryption (AES-256)
- In-Transit Encryption: TLS 1.2+ minimum, Certificate management procedures, Perfect forward secrecy (recommended)
- Key Management: HSM for production key storage, Key rotation schedule (bi-annual minimum), Separation of duties for key access
- Evidence Artifacts: Encryption audit report, Configuration screenshots/exports, Key rotation logs, Certificate inventory

Satisfies: COBIT DSS07 (3 control objectives), ISO 27001 A.10.1 (2 control clauses), NIST SP 800-53 SC-28 (information protection), Regulatory requirements (GDPR, HIPAA encryption standards).

**EATGF-DSS-VULN-01: Vulnerability and Patch Management**

Mapping (Critical for Operational Security):

| Framework | Reference | Scope |
|-----------|-----------|-------|
| COBIT 2019 | DSS06 (Integrated monitoring) | Security monitoring |
| ISO 27001:2022 | A.12.6 (Technical vulnerability management) | Vulnerability management lifecycle |
| NIST SP 800-53 | SI-2 (Flaw remediation) | Flaw identification and remediation |

Vulnerability Management Lifecycle:
- Scanning (Monthly minimum): Network scanning (Qualys/Tenable), Application scanning (SAST/DAST), Threat intelligence integration
- Classification and SLAs: Critical (24-hour remediation SLA), High (7-day SLA), Medium (30-day SLA), Low (90-day SLA)
- Remediation: Patch development/testing, Deployment per SLA, Verification testing post-deployment
- Exception Process: Risk acceptance (if not patching feasible), Compensating control (required for exceptions), Exception duration limit enforcement
- Evidence: Monthly vulnerability scan reports, Patch deployment logs, Exception tracking log, Compliance metrics dashboard

Satisfies: COBIT DSS06 (5 control objectives), ISO 27001 A.12.6 (3 control objectives), NIST SP 800-53 SI-2 (patch management), Security operational best practices.

**EATGF-DSS-INC-01: Incident Response**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| COBIT 2019 | DSS02 (Manage service requests and incidents) | Incident lifecycle management |
| ISO 27001:2022 | A.5.24-A.5.27 | Incident response planning and management |
| NIST SP 800-53 | IR-4, IR-5, IR-6 | Incident handling, monitoring, reporting |

Control Requirements:
- Incident response plan with defined roles and procedures
- Incident severity classification (Severity 1-4 definitions)
- Escalation procedures with defined timelines
- Post-incident review requirements for Severity 1-2 incidents
- Annual incident response tabletop exercises

Evidence Requirements:
- Incident response plan (approved by CISO)
- Incident log with severity classification and timestamps
- Post-incident review reports with root cause analysis
- Tabletop exercise records and lessons learned

Satisfies: COBIT DSS02, ISO 27001 A.5.24-A.5.27, NIST SP 800-53 IR family, SOC 2 CC7 (system operations).

#### MEA Domain — Monitor, Evaluate, Assess

**EATGF-MEA-AUD-01: Internal Audit**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| COBIT 2019 | MEA03 (Independent assurance) | Internal audit function |
| ISO 27001:2022 | Clause 9.2 (Internal audit) | ISMS audit requirements |
| ISO 42001:2023 | Clause 9.2 (Internal audit) | AI MS audit requirements |

Requirements:
- Annual audit plan covering all EATGF domains
- Audit execution per Internal Audit Procedure (Layer 06)
- Audit finding remediation tracking
- Audit results reporting to Governance Council

Evidence: Annual audit plan, Audit reports with findings, Remediation tracker, Governance Council reporting.

**EATGF-MEA-PERF-01: Performance Monitoring**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| COBIT 2019 | MEA01 (Performance monitoring) | Performance and conformance |
| ISO 27001:2022 | Clause 9.1 (Monitoring and measurement) | ISMS performance |
| ISO 42001:2023 | Clause 9.1 (Monitoring and measurement) | AI MS performance |

Requirements:
- KPI definitions for critical governance processes
- Monthly KPI data collection and reporting
- Quarterly performance reviews
- Corrective action initiation when thresholds breached

Evidence: KPI definitions and thresholds, Monthly KPI reports, Quarterly performance review minutes.

**EATGF-MEA-MAT-01: Maturity Assessment**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| COBIT 2019 | MEA02 (Maturity tracking) | Process maturity |
| ISO 27001:2022 | Clause 10 (Continual improvement) | ISMS improvement |

Requirements:
- Annual maturity assessment using EATGF Maturity Model (Layer 03)
- Maturity assessment across all 11 domains
- Improvement target definition and tracking
- Reporting to Governance Council

Evidence: Annual maturity assessment report, Maturity scoring by domain, Improvement action plan.

#### AI Domain — Artificial Intelligence

**EATGF-AI-LC-01: AI Lifecycle Governance**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 42001:2023 | Clause 8 (Operation) | AI system lifecycle management |
| NIST AI RMF | MANAGE category | AI system management |

Requirements:
- AI model inventory with lifecycle stage tracking
- Pre-deployment impact assessments
- Model monitoring for drift and fairness
- Annual review of deployed AI models
- Decommission criteria and procedures

Evidence: AI model inventory, Impact assessments, Model monitoring dashboards, Annual review reports.

**EATGF-AI-RISK-01: AI Risk and Bias Management**

Mapping:

| Framework | Reference | Scope ||-----------|-----------|-------|
| ISO 42001:2023 | Clause 6.1 (Risks and opportunities) | AI risk management |
| NIST AI RMF | GOVERN-2, MAP, MEASURE | AI risk governance |

Requirements:
- Bias testing during model development and before deployment
- Fairness thresholds definition (e.g., disparate impact > 0.80)
- Explainability documentation for high-risk AI models
- Production model bias drift monitoring
- AI risk register distinct from general risk register

Evidence: Bias testing reports, Fairness threshold documentation, Explainability reports, AI risk register.

#### API Domain — Application Programming Interface

**EATGF-API-SEC-01: API Security**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| OWASP API Top 10:2023 | All 10 risks | API security controls |
| ISO 27001:2022 | A.8.3 (Information transfer) | Secure information exchange |
| NIST SP 800-53 | SC-8 (Transmission confidentiality) | Transmission protection |

Requirements:
- API gateway with authentication and rate limiting
- OAuth 2.0 or equivalent for API authentication
- API security testing aligned with OWASP ASVS 4.0
- API traffic monitoring for anomalous patterns

Evidence: API gateway configuration, API security test reports, Traffic monitoring dashboards.

**EATGF-API-LC-01: API Lifecycle Management**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.8.3 (Information transfer) | Secure API management |
| COBIT 2019 | BAI03 (Solutions implementation) | API lifecycle oversight |

Requirements:
- API catalog with version, owner, status
- API deprecation policy with minimum notice period
- API documentation (OpenAPI specifications)
- Quarterly API portfolio review

Evidence: API catalog, Deprecation notices, API documentation, Quarterly review minutes.

#### CLD Domain — Cloud

**EATGF-CLD-ARCH-01: Cloud Architecture**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| COBIT 2019 | APO03 (Enterprise architecture) | Cloud architecture standards |
| ISO 27001:2022 | A.8.21 (Secure architecture) | Cloud-specific architecture |

Requirements:
- Cloud architecture standards (landing zone design)
- Architecture review for all new cloud workloads
- Cloud architecture documentation maintenance
- Annual well-architected review

Evidence: Cloud architecture standards document, Architecture review records, Annual review report.

**EATGF-CLD-SEC-01: Cloud Security**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.23 (Cloud services security) | Cloud security controls |
| NIST SP 800-53 | AC-4 (Information flow enforcement) | Network segmentation |

Requirements:
- Cloud-native IAM implementation
- Network segmentation and security groups enforcement
- Cloud audit logging across all accounts
- Data protection controls (encryption, DLP)

Evidence: Cloud IAM configuration, Network segmentation documentation, Audit log retention evidence, Data protection configuration.

**EATGF-CLD-MON-01: Cloud Monitoring**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| COBIT 2019 | DSS06 (Integrated monitoring) | Cloud resource monitoring |
| ISO 27001:2022 | A.8.16 (Monitoring activities) | Security monitoring |

Requirements:
- Cloud monitoring covering compute, storage, network
- Alerting thresholds and escalation procedures definition
- 12-month minimum monitoring data retention
- Monthly cloud monitoring review

Evidence: Cloud monitoring configuration, Alerting threshold documentation, Monthly monitoring review reports.

**EATGF-CLD-RES-01: Cloud Resilience**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.30 (ICT readiness for business continuity) | Cloud availability |
| COBIT 2019 | DSS04 (Manage continuity) | Cloud disaster recovery |

Requirements:
- Availability targets for all cloud workloads defined
- Multi-availability-zone or multi-region deployments for critical workloads
- Annual failover testing
- Cloud disaster recovery documentation maintenance

Evidence: Availability target documentation, Multi-AZ/region deployment evidence, Failover test reports, Cloud DR documentation.

#### DEV Domain — Development

**EATGF-DEV-SDLC-01: Secure SDLC**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| NIST SSDF | All practices | Secure software development |
| ISO 27001:2022 | A.8.25 (Secure development lifecycle) | Development security |
| OWASP | SAMM (Software Assurance Maturity Model) | Development maturity |

Requirements:
- Secure development standards definition
- Threat modeling for new applications
- Security reviews at design and pre-deployment gates
- Annual security training for all developers

Evidence: Secure development standards document, Threat model records, Security gate review records, Developer security training records.

**EATGF-DEV-SCAN-01: Code Scanning**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| OWASP | ASVS 4.0 | Application security verification |
| NIST SSDF | PW.1, PW.2 | Secure coding practices |
| ISO 27001:2022 | A.8.25 (Secure development) | Code security testing |

Requirements:
- SAST (static application security testing) in CI/CD pipeline
- DAST (dynamic application security testing) for deployed applications
- Remediation SLAs by severity defined
- Scanning coverage tracking across all repositories

Evidence: SAST configuration and scan reports, DAST scan reports, Remediation tracking log, Coverage metrics.

**EATGF-DEV-SUP-01: Supply Chain Security**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| NIST SSDF | PW.4.1 (Software component verification) | Dependency security |
| ISO 27001:2022 | A.5.19 (Information security in supplier relationships) | Supply chain risk |
| OWASP | Dependency-Check | Component analysis |

Requirements:
- SBOM (Software Bill of Materials) generation for all applications
- Dependency vulnerability monitoring
- Approved and prohibited dependency lists definition
- Quarterly dependency review

Evidence: SBOM records, Dependency vulnerability reports, Approved/prohibited dependency lists, Quarterly dependency review minutes.

**EATGF-DEV-CI-01: CI/CD Governance**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.8.19 (Change control) | Deployment governance |
| NIST SSDF | PW.9 (Build automation) | Pipeline security |

Requirements:
- Governance gates in CI/CD pipelines (build, test, scan, approve, deploy)
- Human approval requirement for production deployments
- Pipeline configuration maintained in version control
- Pipeline execution log auditing

Evidence: Pipeline configuration records (version controlled), Deployment approval records, Pipeline execution audit logs.

#### DATA Domain — Data

**EATGF-DATA-PRIV-01: Data Privacy**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.33- A.5.36 (Privacy and PII protection) | Personal data protection |
| GDPR | Articles 5, 30, 35 | Privacy compliance |
| CCPA | Section 1798.100 | California privacy compliance |

Requirements:
- Data processing inventory (register of processing activities)
- DPIAs (Data Protection Impact Assessments) for high-risk processing
- Data subject rights procedures implementation
- Data classification scheme definition and enforcement

Evidence: Data processing inventory, DPIA records, Data subject request log, Data classification policy.

**EATGF-DATA-RET-01: Data Retention**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.34 (Privacy and PII protection) | Data retention controls |
| GDPR | Article 5(1)(e) | Storage limitation |

Requirements:
- Data retention schedule defined by data category
- Automated retention enforcement where feasible
- Annual retention compliance review
- Secure data disposal evidence maintenance

Evidence: Data retention schedule, Retention enforcement configuration, Annual retention review report, Disposal certificates or logs.

**EATGF-DATA-MIN-01: Data Minimization**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.33 (Privacy and PII protection) | Data minimization |
| GDPR | Article 5(1)(c) | Data minimization principle |

Requirements:
- Data minimization principles defined in data governance policy
- Annual review of data collection practices
- Technical controls implementation to limit data collection
- Data minimization metrics reporting to Governance Council

Evidence: Data governance policy (with minimization section), Annual data collection review report, Data minimization metrics.

#### BCP Domain — Business Continuity Planning

**EATGF-BCP-PLAN-01: Business Continuity Planning**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.30 (ICT readiness for business continuity) | Business continuity planning |
| COBIT 2019 | DSS04 (Manage continuity) | Continuity management |

Requirements:
- Business continuity plans for all critical services
- Critical service inventory with business impact analysis
- Annual BCP review and update
- BCP coverage of technology, people, and process

Evidence: Business continuity plans (approved), Critical service inventory, Business impact analysis, Annual BCP review records.

**EATGF-BCP-TEST-01: Business Continuity Testing**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.30 (ICT readiness for business continuity) | Continuity testing |
| COBIT 2019 | DSS04.08 (Manage continuity) | Test continuity plans |

Requirements:
- Annual business continuity test (tabletop or failover)
- Test results documentation including gaps identified
- BCP update based on test findings
- Test results reporting to Governance Council

Evidence: BCP test plan and results, Gap analysis from testing, BCP update records post-test.

**EATGF-BCP-RTO-01: RTO/RPO Targets**

Mapping:

| Framework | Reference | Scope |
|-----------|-----------|-------|
| ISO 27001:2022 | A.5.30 (ICT readiness for business continuity) | Recovery objectives |
| COBIT 2019 | DSS04.02 (Manage continuity) | Define continuity requirements |

Requirements:
- RTO and RPO targets defined for each critical service
- RTO/RPO targets validated through testing
- Backup and recovery mechanisms support defined targets
- RTO/RPO compliance reporting to Governance Council

Evidence: RTO/RPO target documentation, Test results validating RTO/RPO achievability, Backup and recovery configuration evidence.

### Evidence Cross-Reference Matrix

| Evidence Type | COBIT | ISO 27001 | ISO 42001 | NIST AI RMF | NIST 800-53 |
|---------------|-------|-----------|-----------|-------------|-------------|
| Risk register | APO12 | 6.1.2 | 6 | MAP | N/A |
| Audit report | MEA03 | 9.2 | 9 | MEASURE | N/A |
| Test results | BAI03, DSS06 | A.8.9 | 8.2 | MEASURE | All domains |
| Access logs | DSS05 | A.5.15-A.5.18 | N/A | N/A | AC-2, AC-3 |
| Incident ticket | DSS02 | A.5.24-A.5.27 | 8.2 | GOVERN | IR-4, IR-5, IR-6 |
| Dashboard | MEA01 | 9.1 | 9 | MEASURE | N/A |
| Configuration | BAI10 | A.8.9 | 8.1 | N/A | CM-2, CM-3 |
| Training record | APO13 | A.6.3 | 7 | GOVERN | AT-2, AT-3 |
| Deployment log | BAI06 | A.8.19 | N/A | N/A | CM-3 |
| AI model inventory | N/A | N/A | 8 | ALL | N/A |
| Bias testing report | N/A | N/A | 9 | MEASURE | N/A |
| API catalog | BAI03 | A.8.3 | N/A | N/A | N/A |
| Cloud audit logs | DSS06 | A.8.16 | N/A | N/A | AU-6, SI-4 |

### Applicability Matrix by Organization Size

Control applicability varies by edition:

| EATGF Control | Startup (1-10) | SaaS (10-50) | Enterprise (50+) |
|---------------|----------------|--------------|------------------|
| **EDM Controls** | | | |
| EATGF-EDM-RISK-01 | Not applicable | Mandatory | Mandatory |
| EATGF-EDM-BEN-01 | Mandatory | Mandatory | Mandatory |
| EATGF-EDM-GOV-01 | Not applicable | Mandatory | Mandatory |
| **APO Controls** | | | |
| EATGF-APO-ARCH-01 | Not applicable | Mandatory | Mandatory |
| EATGF-APO-RISK-01 | Mandatory | Mandatory | Mandatory |
| EATGF-APO-SEC-01 | Not applicable | Mandatory | Mandatory |
| EATGF-APO-AI-01 | Not applicable | Conditional (if AI) | Conditional (if AI) |
| **BAI Controls** | | | |
| EATGF-BAI-CHG-01 | Mandatory | Mandatory | Mandatory |
| EATGF-BAI-CONF-01 | Mandatory | Mandatory | Mandatory |
| EATGF-BAI-TEST-01 | Mandatory | Mandatory | Mandatory |
| **DSS Controls** | | | |
| EATGF-DSS-SEC-01 | Mandatory | Mandatory | Mandatory |
| EATGF-DSS-ENC-01 | Mandatory | Mandatory | Mandatory |
| EATGF-DSS-VULN-01 | Mandatory | Mandatory | Mandatory |
| EATGF-DSS-INC-01 | Mandatory | Mandatory | Mandatory |
| **MEA Controls** | | | |
| EATGF-MEA-AUD-01 | Not applicable | Mandatory | Mandatory |
| EATGF-MEA-PERF-01 | Mandatory | Mandatory | Mandatory |
| EATGF-MEA-MAT-01 | Mandatory | Mandatory | Mandatory |
| **AI Controls** | | | |
| EATGF-AI-LC-01 | Not applicable | Conditional (if AI) | Conditional (if AI) |
| EATGF-AI-RISK-01 | Not applicable | Conditional (if AI) | Conditional (if AI) |
| **API Controls** | | | |
| EATGF-API-SEC-01 | Mandatory | Mandatory | Mandatory |
| EATGF-API-LC-01 | Mandatory | Mandatory | Mandatory |
| **CLD Controls** | | | |
| EATGF-CLD-ARCH-01 | Not applicable | Mandatory | Mandatory |
| EATGF-CLD-SEC-01 | Mandatory | Mandatory | Mandatory |
| EATGF-CLD-MON-01 | Mandatory | Mandatory | Mandatory |
| EATGF-CLD-RES-01 | Not applicable | Mandatory | Mandatory |
| **DEV Controls** | | | |
| EATGF-DEV-SDLC-01 | Mandatory | Mandatory | Mandatory |
| EATGF-DEV-SCAN-01 | Mandatory | Mandatory | Mandatory |
| EATGF-DEV-SUP-01 | Mandatory | Mandatory | Mandatory |
| EATGF-DEV-CI-01 | Mandatory | Mandatory | Mandatory |
| **DATA Controls** | | | |
| EATGF-DATA-PRIV-01 | Conditional (if PII) | Mandatory | Mandatory |
| EATGF-DATA-RET-01 | Mandatory | Mandatory | Mandatory |
| EATGF-DATA-MIN-01 | Conditional (if PII) | Mandatory | Mandatory |
| **BCP Controls** | | | |
| EATGF-BCP-PLAN-01 | Not applicable | Mandatory | Mandatory |
| EATGF-BCP-TEST-01 | Not applicable | Mandatory | Mandatory |
| EATGF-BCP-RTO-01 | Not applicable | Mandatory | Mandatory |

## Control Mapping

### ISO 27001:2022 Coverage

EATGF provides 93% coverage of ISO 27001:2022 Annex A controls:

- **A.5 Organizational Controls (37 controls)** – Mapped to EDM, APO, MEA domains
- **A.6 People Controls (8 controls)** – Covered by DSS-SEC-01 (IAM), training requirements across DEV
- **A.7 Physical Controls (14 controls)** – Not explicitly covered; organizations implement per physical security context
- **A.8 Technological Controls (34 controls)** – Comprehensive coverage via DSS, DEV, CLD, API domains

### ISO 42001:2023 AI Management System Coverage

EATGF AI domain (AI-LC-01, AI-RISK-01) aligns with ISO 42001:2023 structure:

- **Clause 4 Context** – APO-AI-01 establishes organizational context for AI
- **Clause 5 Leadership** – APO-AI-01 establishes AI governance policy and ethics board
- **Clause 6 Planning** – AI-LC-01 requires impact assessments before deployment
- **Clause 7 Support** – APO-AI-01 allocates resources for AI governance
- **Clause 8 Operation** – AI-RISK-01 implements bias testing and fairness monitoring
- **Clause 9 Performance Evaluation** – MEA-PERF-01 monitors AI system performance
- **Clause 10 Improvement** – AI-LC-01 annual reviews drive continuous improvement

### COBIT 2019 Process Mapping

EATGF domains directly map to COBIT 2019 process areas with 75% coverage:

- **EDM (Evaluate, Direct, Monitor)** – EATGF EDM domain (3 controls) covers EDM01-EDM03
- **APO (Align, Plan, Organise)** – EATGF APO domain (4 controls) covers APO01, APO03, APO12, APO13
- **BAI (Build, Acquire, Implement)** – EATGF BAI domain (3 controls) covers BAI03, BAI06, BAI10
- **DSS (Deliver, Service, Support)** – EATGF DSS domain (4 controls) covers DSS02, DSS05, DSS06, DSS07
- **MEA (Monitor, Evaluate, Assess)** – EATGF MEA domain (3 controls) covers MEA01, MEA02, MEA03

### NIST AI RMF Mapping

EATGF AI controls map to NIST AI Risk Management Framework functions:

- **GOVERN** – APO-AI-01 (AI governance policy and structure)
- **MAP** – APO-RISK-01 (AI risk mapping), AI-RISK-01 (AI-specific risk identification)
- **MEASURE** – AI-RISK-01 (Bias testing and fairness measurement), MEA-PERF-01 (AI performance monitoring)
- **MANAGE** – AI-LC-01 (AI lifecycle management and mitigation implementation)

### OWASP Standards Mapping

- **OWASP ASVS 4.0** – Referenced in DEV-SCAN-01 (code scanning requirements), API-SEC-01 (API security testing)
- **OWASP API Security Top 10:2023** – 100% coverage by API-SEC-01 control requirements
- **OWASP Top 10 Web Application Risks** – Addressed through DEV domain controls (SDLC, scanning, CI/CD)
- **OWASP SAMM** – Aligned with DEV-SDLC-01 for development process maturity

## Developer Checklist

Before implementing comprehensive framework mappings:

- [ ] Review organizational context and determine applicable edition (Startup/SaaS/Enterprise)
- [ ] Review applicability matrix for mandatory vs conditional controls
- [ ] Identify external compliance requirements (ISO 27001, ISO 42001, SOC 2, GDPR, etc.)
- [ ] Map external compliance requirements to EATGF controls using mapping tables
- [ ] Identify evidence reuse opportunities (single evidence artifact satisfying multiple standards)
- [ ] Configure unified evidence collection processes per evidence cross-reference matrix
- [ ] Establish control ownership per Implementation Summary in Control Objectives document
- [ ] Schedule audit readiness activities per framework certification requirements
- [ ] Integrate EATGF mapping into Statement of Applicability (Layer 01)
- [ ] Train audit teams on bidirectional mapping approach for multi-framework audits
- [ ] Configure governance dashboard to report compliance across mapped frameworks
- [ ] Establish semi-annual mapping review process to incorporate framework updates
- [ ] Document any control implementation deviations with compensating controls
- [ ] Prepare evidence portfolio organized by EATGF control ID (not external framework structure)

## Governance Implications

### Central Hub Authority

- Master Control Matrix (MCM) in Layer 00_FOUNDATION is single source of truth for all control requirements
- External framework controls (ISO/COBIT/NIST) map TO the MCM (not vice versa) to establish unified governance
- Organizations implement EATGF controls once; mappings demonstrate compliance to multiple frameworks simultaneously
- Evidence collection unified under EATGF control structure eliminates redundant audit artifacts

### Evidence Reuse and Cost Efficiency

- Single control implementation with unified evidence satisfies multiple framework requirements (e.g., IAM evidence for COBIT DSS05, ISO 27001 A.5.15-A.5.18, SOC 2 CC6)
- Evidence cross-reference matrix demonstrates how each artifact type satisfies multiple standard clauses
- Organizations achieve 40-60% audit preparation time reduction through evidence reuse
- Audit costs reduced by conducting unified multi-framework audits referencing single EATGF control implementation

### Audit Scope and Planning

- Internal Audit Procedure (Layer 06) scopes audits using EATGF control structure
- Auditors map EATGF findings to external framework requirements using bidirectional mapping tables
- Audit reports demonstrate compliance across all applicable frameworks (ISO 27001, ISO 42001, COBIT, SOC 2) simultaneously
- Statement of Applicability (Layer 01) documents control applicability and mapping justifications for audit defensibility

### Edition Progression and Scalability

- Organizations progress through editions as complexity increases (Startup → SaaS → Enterprise)
- Control applicability scales per applicability matrix; mappings maintained across all editions
- Framework requirements (e.g., ISO 27001 mandatory for SaaS/Enterprise) inform control prioritization
- Edition progression documented in governance maturity assessment (MEA-MAT-01)

## Official References

- **COBIT 2019** – Framework for Governance and Management of Enterprise IT (ISACA, 2019)
- **ISO/IEC 27001:2022** – Information Security Management Systems, Requirements (ISO, 2022)
- **ISO/IEC 27002:2022** – Code of Practice for Information Security Controls (ISO, 2022)
- **ISO/IEC 42001:2023** – Artificial Intelligence Management System, Requirements (ISO, 2023)
- **NIST AI Risk Management Framework** – AI RMF 1.0 (NIST, 2023)
- **NIST SP 800-53 Revision 5** – Security and Privacy Controls for Information Systems (NIST, 2020)
- **NIST Secure Software Development Framework (SSDF)** – SP 800-218 (NIST, 2022)
- **OWASP ASVS 4.0** – Application Security Verification Standard (OWASP, 2019)
- **OWASP API Security Top 10:2023** – API Security Risks (OWASP, 2023)
- **OWASP SAMM** – Software Assurance Maturity Model (OWASP, 2020)
