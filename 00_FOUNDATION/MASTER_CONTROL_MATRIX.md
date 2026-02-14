# ENTERPRISE AI-ALIGNED TECHNICAL GOVERNANCE FRAMEWORK (EATGF)
## Master Control Matrix (MCM) v1.0

**Framework Name:** Enterprise AI-Aligned Technical Governance Framework  
**Document Type:** Master Control Matrix (Central Control Authority)  
**Version:** 1.0  
**Effective Date:** February 2026  
**Classification:** Controlled - Internal Use Only  
**Authority:** Board of Directors / Executive Steering Committee

---

## ⚠️ IMPORTANT LEGAL DISCLAIMERS

### Implementation Status Statement

The **Status** field in this MCM reflects the current **internal governance maturity level only** and does not constitute:
- Certification or conformity statements under ISO/IEC standards
- Claims of compliance with regulatory requirements
- Auditor-verified controls (requires external audit validation)

Organizations using this framework must conduct independent assessments and obtain formal certifications from accredited bodies if required.

### Standards Alignment & Usage

This framework provides **interpretive alignment references** to international standards:
- **COBIT 2019 Framework** - governance reference model
- **ISO/IEC 27001:2022** - information security management system
- **ISO/IEC 42001:2023** - AI management system
- **ISO/IEC 27701:2019** - Privacy extension (guidance only - does not imply PIMS certification requirement)
- **NIST AI Risk Management Framework 1.0** - AI governance alignment
- **OWASP API Security Top 10 (2023)** - API security guidance
- **NIST SP 800-53 Rev. 5** - security control baseline reference

**This framework does not reproduce copyrighted standards text.** All mappings represent derivative interpretations for governance guidance only.

---

## 📋 DOCUMENT OVERVIEW

The **Master Control Matrix (MCM)** is the authoritative, single source of truth for all governance controls within EATGF. It maps internal controls to international standards and provides the foundation for ISO 27001 Statement of Applicability (SoA), ISO 42001 compliance, and audit readiness.

### Purpose
- Provide unified control identifier across all standards
- Enable traceability from policy → control → evidence
- Support ISO 27001 SoA and audit documentation
- Ensure consistency in governance implementation
- Facilitate internal and external audits

### Scope
- **35 core governance controls** across 11 domains
- Mappings to COBIT 2019, ISO 27001, ISO 42001, NIST AI RMF, OWASP, NIST 800-53
- Evidence and ownership definitions
- Applicability by organization size (Startup/SaaS/Enterprise)
- Environment profiles (Cloud/Hybrid/On-Prem/Multi-Cloud)

---

## 🔑 CONTROL ID NAMING CONVENTION

**Format:** `EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]`

**Domain Codes:**
- `EDM` = Evaluate, Direct, Monitor
- `APO` = Align, Plan, Organize
- `BAI` = Build, Acquire, Implement
- `DSS` = Deliver, Service, Support
- `MEA` = Monitor, Evaluate, Assess
- `CLD` = Cloud Governance
- `DEV` = DevSecOps & Development Practices
- `DATA` = Data Privacy & Protection
- `BCP` = Business Continuity & Disaster Recovery
- `AI` = AI-Specific Governance
- `API` = API Security & Lifecycle

**Category Codes:**
| Code | Category | Domain | Examples |
|------|----------|--------|----------|
| RISK | Risk Management | EDM/APO/AI | Risk appetite, mitigation |
| ARCH | Architecture | APO/CLD | Design standards, integration |
| CHG | Change Management | BAI | Change control process |
| SEC | Security | DSS/CLD/API | Authentication, encryption |
| INC | Incident Response | DSS | Breach notification, response |
| AUD | Audit & Assurance | MEA | Internal audit, testing |
| PERF | Performance | MEA/CLD | KPI, dashboards |
| LC | Lifecycle | BAI/AI/API/CLD | System/AI/API/Cloud lifecycle |
| CONF | Configuration | BAI | Version control, baselines |
| MON | Monitoring | MEA/CLD | Cloud monitoring, cost |
| RES | Resilience | CLD/BCP | Disaster recovery |
| SDLC | Development Lifecycle | DEV | Secure SDLC |
| SCAN | Code Scanning | DEV | SAST/DAST/SCA |
| SUP | Supply Chain | DEV | SBOM, dependencies |
| CI | CI/CD Pipeline | DEV | Pipeline integrity |
| PRIV | Privacy | DATA | DPIA, compliance |
| RET | Retention | DATA | Data lifecycle |
| MIN | Minimization | DATA | Data minimization |
| PLAN | Planning | BCP | BC/DR planning |
| TEST | Testing | BCP | Recovery testing |
| RTO | Recovery Objectives | BCP | RTO/RPO targets |

**Number:** Sequential (01, 02, 03...)

**Examples:**
- `EATGF-EDM-RISK-01` = Risk Appetite Definition
- `EATGF-CLD-ARCH-01` = Cloud Architecture
- `EATGF-DEV-SCAN-01` = SAST/DAST/SCA Integration
- `EATGF-BCP-RTO-01` = RTO/RPO Management

---

## 📊 MCM FIELD DEFINITIONS

| Field | Description | Required |
|-------|-------------|----------|
| **EATGF Control ID** | Unique internal identifier (e.g., EATGF-EDM-RISK-01) | Yes |
| **Control Title** | Short, descriptive control name (5-10 words) | Yes |
| **Control Description** | Detailed control objective (2-3 sentences) | Yes |
| **Governance Domain** | COBIT domain (EDM/APO/BAI/DSS/MEA/CLD/DEV/DATA/BCP) | Yes |
| **Control Type** | Governance / Preventive / Detective / Corrective | Yes |
| **COBIT Reference** | COBIT process ID (e.g., APO13) | Yes |
| **COBIT Supporting Reference** | Secondary COBIT alignment (if applicable) | Conditional |
| **ISO 27001 Clause** | Management system clause (4-10) | Conditional |
| **ISO 27001 Annex A** | Control reference (e.g., A.8.1) | Conditional |
| **ISO 42001 Clause** | AI system clause (if AI-related) | Conditional |
| **NIST AI RMF** | GOVERN/MAP/MEASURE/MANAGE if AI-applicable | Conditional |
| **OWASP/RFC/NIST Reference** | Standard reference for API/security | Conditional |
| **Evidence Required** | Type of evidence to demonstrate compliance | Yes |
| **Control Owner** | Role responsible for implementation | Yes |
| **Evidence Owner** | Role responsible for evidence maintenance | Yes |
| **Review Frequency** | Monthly / Quarterly / Annual / Per Release | Yes |
| **Applicability** | Startup / SaaS / Enterprise (or combinations) | Yes |
| **Environment Profile** | Cloud / Hybrid / On-Prem / Multi-Cloud | Yes |
| **Criticality** | High / Medium / Low (Risk-based prioritization) | Yes |
| **Residual Risk Level** | Low / Medium / High (Post-mitigation risk) | Conditional |
| **Status** | Framework Baseline / Planned / In Progress / Not Implemented | Yes |

---

## 🔷 LAYER 1: GOVERNANCE-LEVEL CONTROLS (EDM Domain)

### EATGF-EDM-RISK-01: IT & AI Risk Appetite Definition

| Field | Value |
|-------|-------|
| **Title** | IT & AI Risk Appetite Definition |
| **Description** | Board establishes and communicates IT and AI risk tolerance levels. Documents specific risk thresholds for technology, data security, AI fairness, and regulatory compliance. |
| **Governance Domain** | EDM (Evaluate, Direct, Monitor) |
| **Control Type** | Governance |
| **COBIT Reference** | EDM03 (Evaluate and Direct IT Governance) |
| **ISO 27001 Clause** | 6.1.2 (Information security risk assessment process) |
| **ISO 42001 Clause** | 6 (Organization of AI governance) |
| **NIST AI RMF** | GOVERN (Governance Processes) |
| **Evidence Required** | Board-approved Risk Appetite Statement, signed and dated |
| **Control Owner** | Chief Governance Officer / Executive Steering Committee |
| **Evidence Owner** | Governance Council |
| **Review Frequency** | Annual (or upon material change) |
| **Applicability** | SaaS / Enterprise |
| **Criticality** | High |
| **Residual Risk Level** | Low |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Risk Appetite Statement approved and signed by Board
- [ ] Risk thresholds defined (Critical/High/Medium/Low)
- [ ] AI-specific risk appetite documented
- [ ] Data breach/compliance thresholds defined
- [ ] Last review date and next review scheduled

---

### EATGF-EDM-BEN-01: Technology Value & Benefits Monitoring

| Field | Value |
|-------|-------|
| **Title** | Technology Value & Benefits Monitoring |
| **Description** | Board monitors IT/AI investments to ensure they deliver promised business value. Tracks benefit realization through KPIs (DORA metrics, customer satisfaction, cost reduction). |
| **Governance Domain** | EDM |
| **Control Type** | Detective |
| **COBIT Reference** | EDM02 (Ensure Benefits Realisation) |
| **ISO 27001 Clause** | 9.1 (Monitoring, measurement, analysis and evaluation) |
| **Evidence Required** | KPI dashboards, DORA metrics (deployment frequency, lead time, change failure rate, MTTR) |
| **Control Owner** | CFO / CTO |
| **Evidence Owner** | Performance Management Team |
| **Review Frequency** | Quarterly |
| **Applicability** | All (Startup / SaaS / Enterprise) |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Benefits realization dashboard live and updated
- [ ] DORA metrics tracked monthly
- [ ] Quarterly executive review meeting held
- [ ] KPI targets vs actual documented
- [ ] Trend analysis completed

---

### EATGF-EDM-GOV-01: Governance Model & Structure

| Field | Value |
|-------|-------|
| **Title** | Governance Model & Structure |
| **Description** | Establishes formal governance structure with clear roles, responsibilities, and decision rights. Defines governance committees, escalation paths, and authority levels. |
| **Governance Domain** | EDM |
| **Control Type** | Governance |
| **COBIT Reference** | EDM01 (Establish and Maintain IT Governance) |
| **ISO 27001 Clause** | 5.3 (Organizational roles, responsibilities and authorities) |
| **ISO 42001 Clause** | 5.4 (Accountability) |
| **Evidence Required** | Governance Charter, RACI matrix, committee charters |
| **Control Owner** | Chief Governance Officer |
| **Evidence Owner** | Governance Council |
| **Review Frequency** | Annual |
| **Applicability** | SaaS / Enterprise |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Governance Charter signed and approved
- [ ] RACI matrix for governance decisions documented
- [ ] Committee charters for each governance body
- [ ] Escalation procedures documented
- [ ] Roles and responsibilities assigned

---

## 🔷 LAYER 2: ARCHITECTURE & STRATEGY CONTROLS (APO Domain)

### EATGF-APO-ARCH-01: Enterprise Architecture Framework

| Field | Value |
|-------|-------|
| **Title** | Enterprise Architecture Framework |
| **Description** | Organization maintains and follows an enterprise architecture framework that guides technology decisions. Documents current and target architecture states, technology standards, and integration patterns. |
| **Governance Domain** | APO (Align, Plan, Organize) |
| **Control Type** | Preventive |
| **COBIT Reference** | APO03 (Establish and Maintain Information Governance) |
| **ISO 27001:2022** | A.5.1 (Policies for information security), A.5.2 (Information security roles and responsibilities) |
| **ISO 42001 Clause** | 8.1 (Operational planning and control) |
| **Evidence Required** | Architecture standards document, architecture review board minutes, current-state & target-state diagrams |
| **Control Owner** | Chief Architecture Officer / Architecture Lead |
| **Evidence Owner** | Enterprise Architecture Team |
| **Review Frequency** | Annual (with quarterly checkpoints) |
| **Applicability** | SaaS / Enterprise |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Architecture framework adopted (TOGAF/FEA/custom)
- [ ] Technology standards document published
- [ ] Architecture review board established with charter
- [ ] Current-state architecture documented
- [ ] Target-state architecture documented
- [ ] Architecture decisions log maintained

---

### EATGF-APO-RISK-01: IT & AI Risk Register Management

| Field | Value |
|-------|-------|
| **Title** | IT & AI Risk Register Management |
| **Description** | Organization maintains a comprehensive risk register identifying all material IT and AI risks. Risks are assessed, scored, and mitigation plans tracked with ownership and timelines. |
| **Governance Domain** | APO |
| **Control Type** | Preventive |
| **COBIT Reference** | APO12 (Manage Risk) |
| **ISO 27001 Clause** | 6.1.2 (Risk assessment process) |
| **ISO 42001 Clause** | 6 (Organization of AI governance) |
| **NIST AI RMF** | GOVERN (Risk identification) |
| **Evidence Required** | Risk register (50+ risks identified), risk heat map, mitigation plans with owners and dates |
| **Control Owner** | Chief Risk Officer / Risk Management Lead |
| **Evidence Owner** | Risk Management Office |
| **Review Frequency** | Quarterly |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Risk register maintained with 50+ material risks
- [ ] Risks scored (Probability × Impact)
- [ ] Risk heat map created and shared
- [ ] Top 10 critical/high risks have mitigation plans
- [ ] Mitigation owners assigned
- [ ] Monthly escalation tracking for Red risks

---

### EATGF-APO-SEC-01: Information Security Management System (ISMS)

| Field | Value |
|-------|-------|
| **Title** | Information Security Management System (ISMS) |
| **Description** | Organization establishes, implements, and maintains an ISO 27001-compliant ISMS. Documents security policies, procedures, and controls across all information assets. |
| **Governance Domain** | APO |
| **Control Type** | Governance |
| **COBIT Reference** | APO13 (Manage Information Technology Security) |
| **ISO 27001 Clause** | 4-10 (Complete ISMS lifecycle) |
| **ISO 27001 Annex A** | A.5-A.18 (All 76 control objectives) |
| **Evidence Required** | ISMS Manual, Statement of Applicability (SoA), security policy suite, audit reports |
| **Control Owner** | Chief Information Security Officer (CISO) |
| **Evidence Owner** | Information Security Team |
| **Review Frequency** | Annual (with quarterly compliance checks) |
| **Applicability** | SaaS / Enterprise |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] ISMS Manual (ISO 27001:2022) created and approved
- [ ] Statement of Applicability (SoA) completed with justifications
- [ ] All 76 Annex A controls mapped to organization
- [ ] Security policy suite published (7-10 policies)
- [ ] Internal audit completed and findings tracked
- [ ] Certification or external audit planning underway

---

### EATGF-APO-AI-01: AI Governance System (AIMS)

| Field | Value |
|-------|-------|
| **Title** | AI Governance System (AIMS) |
| **Description** | Organization establishes, implements, and maintains an ISO 42001-aligned AI Management System. Documents AI governance policies, AI system lifecycle, and responsible AI practices. |
| **Governance Domain** | APO |
| **Control Type** | Governance |
| **COBIT Reference** | APO04 (Manage IT Architecture) |
| **ISO 42001:2023 Clauses** | 4 (Context of organization) + 5 (Leadership) + 6 (Planning) + 8 (Operation) + 9 (Performance Evaluation) + 10 (Improvement) |
| **NIST AI RMF** | MAP / MEASURE / MANAGE (Complete AI governance) |
| **Evidence Required** | AIMS Manual, AI System Registry, AI risk assessments, fairness audit reports |
| **Control Owner** | Chief AI Officer / AI Governance Lead |
| **Evidence Owner** | AI Governance Office |
| **Review Frequency** | Quarterly (per AI system release) |
| **Applicability** | SaaS / Enterprise (if AI systems exist) |
| **Status** | In Progress ⏳ |

**Evidence Checklist:**
- [ ] AIMS Manual (ISO 42001:2023) created
- [ ] AI System Registry populated and maintained
- [ ] AI governance committee established
- [ ] AI risk assessment process documented
- [ ] Bias/fairness testing procedures defined
- [ ] Model documentation and versioning standards

---

## 🔷 LAYER 3: CHANGE & DEVELOPMENT CONTROLS (BAI Domain)

### EATGF-BAI-CHG-01: Controlled Change Management

| Field | Value |
|-------|-------|
| **Title** | Controlled Change Management |
| **Description** | All technology changes follow a formal change management process with approval gates. Changes are categorized (emergency/standard/major), tested, approved, and documented before deployment. |
| **Governance Domain** | BAI (Build, Acquire, Implement) |
| **Control Type** | Preventive |
| **COBIT Reference** | BAI06 (Manage IT Changes) |
| **ISO 27001 Annex A** | A.8.19 (Change management) |
| **Evidence Required** | Change log with approvals, CAB meeting minutes, deployment records, rollback plans |
| **Control Owner** | Engineering Lead / DevOps Lead |
| **Evidence Owner** | Change Management Team |
| **Review Frequency** | Monthly |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Change management process documented
- [ ] Change Advisory Board (CAB) established and meeting
- [ ] Change categories defined (emergency/standard/major)
- [ ] Change log maintained with approval history
- [ ] Testing requirements per change type
- [ ] Rollback procedures documented

---

### EATGF-BAI-CONF-01: Configuration & Version Control

| Field | Value |
|-------|-------|
| **Title** | Configuration & Version Control |
| **Description** | All application code, infrastructure configurations, and AI models are version controlled. Maintains configuration baselines, audit trails, and change history for compliance and traceability. |
| **Governance Domain** | BAI |
| **Control Type** | Detective |
| **COBIT Reference** | BAI10 (Manage Configuration) |
| **ISO 27001 Annex A** | A.8.9 (Access control for configuration files) |
| **Evidence Required** | Git repository, commit history, configuration baseline documentation, access controls |
| **Control Owner** | DevOps Lead |
| **Evidence Owner** | Infrastructure Team |
| **Review Frequency** | Continuous (with monthly audits) |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Git repository centralized (GitHub/GitLab)
- [ ] Commit signing enabled
- [ ] Branch protection rules configured
- [ ] Configuration baselines documented
- [ ] Access control to repositories enforced
- [ ] Monthly audit of configuration changes

---

### EATGF-BAI-TEST-01: Quality Assurance & Testing

| Field | Value |
|-------|-------|
| **Title** | Quality Assurance & Testing |
| **Description** | All changes undergo testing (unit, integration, security, performance, UAT) before production deployment. Testing coverage requirements and pass/fail criteria defined. |
| **Governance Domain** | BAI |
| **Control Type** | Preventive |
| **COBIT Reference** | BAI03 (Manage IT Service Configuration) - Primary Reference |
| **Supporting COBIT** | BAI07 (Managed IT Change Acceptance and Transitioning) |
| **ISO 27001:2022** | A.8.9 (Change management security) + A.8.32 (Change management requirements) |
| **NIST AI RMF** | MEASURE (AI model testing and validation) |
| **Evidence Required** | Test results, coverage reports, security scan results, UAT sign-off |
| **Control Owner** | QA Lead |
| **Evidence Owner** | Quality Assurance Team |
| **Review Frequency** | Per release |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Test plan for each release
- [ ] Minimum code coverage standards (70%+)
- [ ] Security testing required (SAST/DAST)
- [ ] Performance testing baseline established
- [ ] UAT sign-off documentation
- [ ] Defect tracking and resolution

---

## 🔷 LAYER 4: OPERATIONS & SECURITY CONTROLS (DSS Domain)

### EATGF-DSS-SEC-01: Identity & Access Management

| Field | Value |
|-------|-------|
| **Title** | Identity & Access Management (IAM) |
| **Description** | Centralized identity management with role-based access control (RBAC). MFA required for sensitive systems. Quarterly access reviews ensure principle of least privilege. |
| **Governance Domain** | DSS (Deliver, Service, Support) |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS05 (Manage Identity and Access) |
| **ISO 27001 Annex A** | A.5.15-A.5.18 (User access control) |
| **Evidence Required** | Access control matrix (RBAC), MFA deployment status, quarterly access review reports |
| **Control Owner** | Security Team / IAM Owner |
| **Evidence Owner** | Identity & Access Team |
| **Review Frequency** | Quarterly |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] IAM platform deployed (Okta/Auth0/similar)
- [ ] RBAC matrix documented
- [ ] MFA enabled for all sensitive systems
- [ ] Service accounts managed and rotated
- [ ] Quarterly access review completed
- [ ] Access removal within 24 hours of termination

---

### EATGF-DSS-ENC-01: Data Encryption & Protection

| Field | Value |
|-------|-------|
| **Title** | Data Encryption & Protection |
| **Description** | All sensitive data encrypted at rest (AES-256) and in transit (TLS 1.2+). Encryption key management procedures follow industry standards. |
| **Governance Domain** | DSS |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS05 (Manage Security Services) - Primary Reference |
| **Supporting COBIT** | APO13 (Manage IT Security Services) - Key Management |
| **ISO 27001:2022** | A.8.21 (Cryptography) + A.8.22 (Key management) |
| **Evidence Required** | Encryption audit report, key management procedure documentation, configuration screenshots |
| **Control Owner** | Security Team |
| **Evidence Owner** | Security Engineering Team |
| **Review Frequency** | Quarterly |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Data classification scheme implemented
- [ ] Encryption standards documented (AES-256, TLS 1.2+)
- [ ] Encryption enabled for all databases
- [ ] Key management procedure documented
- [ ] Key rotation schedule established
- [ ] Quarterly encryption audit completed

---

### EATGF-DSS-VULN-01: Vulnerability & Patch Management

| Field | Value |
|-------|-------|
| **Title** | Vulnerability & Patch Management |
| **Description** | Vulnerability scanning performed monthly. Patches applied per SLA: Critical (24h), High (7d), Medium (30d). Vulnerability tracking system maintained. |
| **Governance Domain** | DSS |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS05 (Manage Security Services) - Primary Reference |
| **Supporting COBIT** | BAI06 (Manage IT Security) - Patch Management |
| **ISO 27001:2022** | A.8.16 (Monitoring and maintaining security) + A.8.25 (Vulnerability management) |
| **Evidence Required** | Vulnerability scan reports, patch deployment logs, SLA compliance metrics |
| **Control Owner** | Security Team |
| **Evidence Owner** | Vulnerability Management Team |
| **Review Frequency** | Monthly |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Vulnerability scanning tool deployed (Qualys/Tenable/similar)
- [ ] Monthly scans executed and reported
- [ ] Remediation SLAs defined and tracked
- [ ] Critical patches deployed within 24 hours
- [ ] Patch exception process documented
- [ ] Monthly vulnerability trend report

---

### EATGF-DSS-INC-01: Incident Response Management

| Field | Value |
|-------|-------|
| **Title** | Incident Response Management |
| **Description** | Formal incident management process with severity classification, notification procedures, root cause analysis, and continuous improvement. Security incidents reported within 1 hour of discovery. |
| **Governance Domain** | DSS |
| **Control Type** | Corrective |
| **COBIT Reference** | DSS02 (Manage Security Incident Response) |
| **ISO 27001 Annex A** | A.5.24-A.5.27 (Incident management) |
| **ISO 42001 Clause** | 8.2 (Incident management for AI systems) |
| **Evidence Required** | Incident tickets, incident response procedures, RCA reports, trend analysis |
| **Control Owner** | Security Team / Incident Response Lead |
| **Evidence Owner** | Incident Response Team |
| **Review Frequency** | Per incident (with quarterly trending) |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Incident response plan published and tested
- [ ] Severity classification scheme defined
- [ ] Escalation procedures documented
- [ ] Incidents logged in ticketing system
- [ ] 1-hour notification requirement tracked
- [ ] Post-incident reviews conducted

---

## 🔷 LAYER 5: MONITORING & AUDIT CONTROLS (MEA Domain)

### EATGF-MEA-AUD-01: Internal Audit Program

| Field | Value |
|-------|-------|
| **Title** | Internal Audit Program |
| **Description** | Annual internal audit program covering all major processes and controls. Third-party or independent audit function. Audit scope includes EATGF controls, ISO 27001 compliance, and governance effectiveness. |
| **Governance Domain** | MEA (Monitor, Evaluate, Assess) |
| **Control Type** | Detective |
| **COBIT Reference** | MEA03 (Monitor, Evaluate, and Assess Compliance with External Requirements) |
| **ISO 27001 Clause** | 9.2 (Internal audit) |
| **ISO 42001 Clause** | 9 (Performance evaluation) |
| **Evidence Required** | Annual audit schedule, audit reports, findings & remediation tracking, audit committee documentation |
| **Control Owner** | Compliance Officer / Internal Audit Lead |
| **Evidence Owner** | Internal Audit Function |
| **Review Frequency** | Annual |
| **Applicability** | SaaS / Enterprise |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Annual audit plan developed
- [ ] Audit scope includes all major processes
- [ ] Audit team independence confirmed
- [ ] Audit reports issued within 2 weeks of completion
- [ ] Management action plan for findings within 30 days
- [ ] Audit committee meeting quarterly

---

### EATGF-MEA-PERF-01: Performance & Conformance Monitoring

| Field | Value |
|-------|-------|
| **Title** | Performance & Conformance Monitoring |
| **Description** | Monitor and report on governance performance including KPIs, compliance metrics, control effectiveness, and risk trends. Dashboards updated monthly and reviewed by leadership. |
| **Governance Domain** | MEA |
| **Control Type** | Detective |
| **COBIT Reference** | MEA01 (Monitor, Measure, and Assess the Information and Technology Resources) |
| **ISO 27001 Clause** | 9.1 (Monitoring and measurement) |
| **ISO 42001 Clause** | 9 (Performance evaluation) |
| **Evidence Required** | KPI dashboard, monthly compliance reports, control testing results, executive scorecards |
| **Control Owner** | Governance Lead / Performance Manager |
| **Evidence Owner** | Governance Office |
| **Review Frequency** | Quarterly |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] KPI framework defined (COBIT metrics, security metrics, AI metrics)
- [ ] Live dashboards created
- [ ] Monthly reports generated and shared
- [ ] Quarterly governance council review
- [ ] Trend analysis and forecasting
- [ ] Remediation tracking for underperforming areas

---

### EATGF-MEA-MAT-01: Governance Maturity Assessment

| Field | Value |
|-------|-------|
| **Title** | Governance Maturity Assessment |
| **Description** | Annual evaluation of governance maturity across 5 COBIT domains using EATGF Maturity Model (Levels 1-5). Results inform next year's governance roadmap. |
| **Governance Domain** | MEA |
| **Control Type** | Detective |
| **COBIT Reference** | MEA01 (Assess current state against maturity model) |
| **ISO 27001 Clause** | 9.1 (Plan and implement monitoring procedures) |
| **Evidence Required** | Maturity assessment questionnaire responses, evidence validation, maturity roadmap |
| **Control Owner** | Governance Lead |
| **Evidence Owner** | Governance Council |
| **Review Frequency** | Annual |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] Maturity assessment conducted (facilitated session)
- [ ] All 5 COBIT domains scored (1-5 scale)
- [ ] Evidence validated for each rating
- [ ] Maturity report issued with recommendations
- [ ] Improvement roadmap created
- [ ] Executive presentation and approval

---

## 🔷 LAYER 6: AI GOVERNANCE CONTROLS

### EATGF-AI-LC-01: AI System Lifecycle Governance

| Field | Value |
|-------|-------|
| **Title** | AI System Lifecycle Governance |
| **Description** | All AI/ML systems follow formal lifecycle from intake through retirement. Includes design, development, validation, deployment, monitoring, and decommission stages. Each stage has approval gates and evidence requirements. |
| **Governance Domain** | BAI (with APO supporting context) |
| **Control Type** | Preventive |
| **COBIT Reference** | APO04 (Manage IT Architecture) + BAI03 (Manage IT Service Configuration) |
| **ISO 42001 Clause** | 8 (Life cycle of AI systems) |
| **NIST AI RMF** | MAP / MEASURE / MANAGE (Complete lifecycle) |
| **Evidence Required** | AI registry, model documentation, deployment records, performance monitoring logs |
| **Control Owner** | AI Governance Lead / Chief AI Officer |
| **Evidence Owner** | AI Operations Team |
| **Review Frequency** | Per model release / update |
| **Applicability** | SaaS / Enterprise (if AI systems exist) |
| **Status** | In Progress ⏳ |

**Evidence Checklist:**
- [ ] AI intake process documented
- [ ] AI system registry with all systems listed
- [ ] Model development standards (framework, versioning)
- [ ] Validation requirements (accuracy, fairness, security)
- [ ] Deployment approval gate
- [ ] Monitoring dashboard per model
- [ ] Incident/adverse event tracking
- [ ] Model retirement procedure

---

### EATGF-AI-RISK-01: AI Risk Assessment & Bias Management

| Field | Value |
|-------|-------|
| **Title** | AI Risk Assessment & Bias Management |
| **Description** | Comprehensive risk assessment for all AI systems including bias, fairness, security, and regulatory risks. Bias testing conducted before deployment. Fairness metrics monitored continuously. |
| **Governance Domain** | EDM (with APO supporting context) |
| **Control Type** | Preventive |
| **COBIT Reference** | EDM03 (Evaluate and Direct IT Governance) + APO12 (Manage Risk) |
| **ISO 42001 Clause** | 6 (Organization of AI governance) |
| **ISO 42001 Clause** | 8.2 (Processing activities for AI system) |
| **NIST AI RMF** | MEASURE (Performance monitoring for bias and fairness) |
| **Evidence Required** | AI risk assessments, bias audit reports, fairness testing results, continuous monitoring dashboards |
| **Control Owner** | AI Risk Officer / Chief Data Officer |
| **Evidence Owner** | AI Ethics & Compliance Team |
| **Review Frequency** | Per model update / Quarterly for monitoring |
| **Applicability** | SaaS / Enterprise (if AI systems exist) |
| **Status** | In Progress ⏳ |

**Evidence Checklist:**
- [ ] AI risk assessment template created
- [ ] Bias testing framework defined (disparate impact, calibration, etc.)
- [ ] Fairness metrics defined per model
- [ ] Pre-deployment bias testing completed
- [ ] Continuous fairness monitoring live
- [ ] Quarterly fairness audit process
- [ ] Remediation process for biased models

---

## 🔷 LAYER 7: API GOVERNANCE CONTROLS

### EATGF-API-SEC-01: API Authentication & Authorization

| Field | Value |
|-------|-------|
| **Title** | API Authentication & Authorization |
| **Description** | All APIs enforce strong authentication (OAuth 2.0, mTLS) and role-based authorization. API gateway enforces rate limiting, threat detection, and audit logging. OWASP API Top 10 controls implemented. |
| **Governance Domain** | DSS |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS05 (Manage Identity and Access) |
| **ISO 27001 Annex A** | A.8.3 (Authentication and cryptography) |
| **OWASP Ref** | API2 (Broken Authentication), API3 (Broken Object Property Level Authorization) |
| **Evidence Required** | API gateway configuration, OAuth/mTLS deployment, rate limiting settings, API audit logs |
| **Control Owner** | API Security Lead |
| **Evidence Owner** | API Gateway Operations |
| **Review Frequency** | Quarterly |
| **Applicability** | All (Startup / SaaS / Enterprise) |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] OAuth 2.0 or mTLS configured
- [ ] API gateway deployed (Kong/Apigee/similar)
- [ ] Rate limiting configured per tier
- [ ] Audit logging enabled for all API calls
- [ ] Quarterly security review of API authentication
- [ ] OWASP compliance verification

---

### EATGF-API-LC-01: API Lifecycle Management

| Field | Value |
|-------|-------|
| **Title** | API Lifecycle Management |
| **Description** | All APIs follow formal lifecycle from design through deprecation. Includes contract-first design (OpenAPI), versioning strategy, compatibility policy, and deprecation timeline. API catalog maintained. |
| **Governance Domain** | BAI |
| **Control Type** | Preventive |
| **COBIT Reference** | BAI03 (Manage IT Service Configuration) |
| **ISO 27001 Annex A** | A.8.19 (Change management) |
| **OWASP Ref** | API9 (Improper Inventory Management) |
| **Evidence Required** | API catalog/registry, OpenAPI specifications, API versioning policy, deprecation schedule |
| **Control Owner** | API Product Manager / API Architect |
| **Evidence Owner** | API Governance Team |
| **Review Frequency** | Per API release / Quarterly catalog review |
| **Applicability** | All |
| **Status** | Framework Baseline |

**Evidence Checklist:**
- [ ] OpenAPI 3.0 spec for all APIs
- [ ] API catalog with current listing
- [ ] Versioning policy documented (e.g., semantic versioning)
- [ ] Breaking change notification process
- [ ] Deprecation policy (6-month minimum)
- [ ] API governance committee reviews

---
## 🔷 LAYER 8: CLOUD GOVERNANCE CONTROLS ⭐ NEW

### EATGF-CLD-ARCH-01: Cloud Architecture & Design Standards

| Field | Value |
|-------|-------|
| **Title** | Cloud Architecture & Design Standards |
| **Description** | Organization maintains cloud architecture standards including multi-cloud strategy, region selection, network design, and shared responsibility model documentation. |
| **Governance Domain** | CLD (Cloud Governance) |
| **Control Type** | Preventive |
| **COBIT Reference** | APO03 (Manage Enterprise Architecture) + APO13 (Manage Security Services) |
| **ISO 27001 Clause** | 5.23 (Supplier relationships), 8.28 (ICT readiness) |
| **ISO 27001:2022** | A.8.23 (Cloud service provider relationships) |
| **ISO 42001:2023 Clause** | 8.1 (Operational planning for AI systems) |
| **NIST 800-53** | SA-3 (System development life cycle), SA-9 (External services) |
| **Evidence Required** | Cloud architecture document, multi-cloud strategy, region policy, network architecture diagram, shared responsibility matrix |
| **Control Owner** | Chief Cloud Officer / Cloud Architect |
| **Evidence Owner** | Cloud Architecture Team |
| **Review Frequency** | Annual (or per major cloud migration) |
| **Applicability** | SaaS / Enterprise |
| **Environment Profile** | Cloud / Multi-Cloud / Hybrid |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Cloud architecture standards document published
- [ ] Multi-cloud strategy approved (single vs. multi-cloud decision)
- [ ] Region selection policy (data residency, geopolitical)
- [ ] Network architecture diagram (VPC/VNet design)
- [ ] Shared Responsibility Model documented per provider
- [ ] Disaster recovery strategy (cross-region failover)
- [ ] Cost optimization framework documented
- [ ] Quarterly architecture review process

---

### EATGF-CLD-SEC-01: Cloud Security & Compliance Configuration

| Field | Value |
|-------|-------|
| **Title** | Cloud Security & Compliance Configuration |
| **Description** | Cloud infrastructure enforces security baselines: encryption, network security, access control, compliance monitoring. Automated compliance checking deployed. |
| **Governance Domain** | CLD |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS05 (Manage Identity and Access) + DSS06 (Manage Logical Access) |
| **ISO 27001:2022** | A.8.21 (Encryption), A.8.22 (Network segmentation) |
| **ISO 42001:2023 Clause** | 8 (Operational control of AI systems) |
| **NIST 800-53** | AC-3, AC-5, SC-7, SC-28 (Encryption & network) |
| **CSA CAIQ** | GRC-01 / ILM-03 / EKM-01 (Cloud controls) |
| **Evidence Required** | Cloud security configuration, CloudTrail/audit logs, compliance scanner results, IAM policies |
| **Control Owner** | Chief Information Security Officer / Cloud Security Lead |
| **Evidence Owner** | Cloud Security Team |
| **Review Frequency** | Monthly |
| **Applicability** | All |
| **Environment Profile** | Cloud / Multi-Cloud / Hybrid |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Cloud security baseline document (AWS/Azure/GCP CIS benchmarks applied)
- [ ] Network security groups/firewall rules configured correctly
- [ ] Encryption at rest (S3/blob storage) enabled with customer-managed keys
- [ ] Encryption in transit (TLS 1.2+) enforced
- [ ] CloudTrail/diagnostic logging enabled with 12-month retention
- [ ] MFA enabled for all cloud console access
- [ ] Cloud compliance scanner deployed (AWS Config/Azure Policy)
- [ ] Monthly compliance scan results reviewed and tracked
- [ ] Critical/High findings with remediation timeline

---

### EATGF-CLD-MON-01: Cloud Cost, Performance & Compliance Monitoring

| Field | Value |
|-------|-------|
| **Title** | Cloud Operations Monitoring & Cost Governance |
| **Description** | Real-time monitoring of cloud infrastructure performance, cost, and compliance. Automated alerts for anomalies. Monthly cost reviews. Compliance drift detection. |
| **Governance Domain** | CLD |
| **Control Type** | Detective |
| **COBIT Reference** | MEA01 (Monitor, Measure, and Assess IT Resources) |
| **ISO 27001:2022** | A.5.23 (Supplier monitoring), 9.1 (Monitoring & measurement) |
| **ISO 42001:2023 Clause** | 9 (Performance evaluation) |
| **Evidence Required** | Cost dashboard, performance metrics, compliance alerts, monthly cost reports |
| **Control Owner** | Chief Financial Officer / Cloud Cost Manager |
| **Evidence Owner** | Cloud Operations Team |
| **Review Frequency** | Monthly |
| **Applicability** | All |
| **Environment Profile** | Cloud / Multi-Cloud / Hybrid |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Cloud cost dashboard live (AWS Cost Explorer / Azure Cost Management)
- [ ] Cost anomaly alerts configured (>10% variance threshold)
- [ ] Monthly cost review meeting held with stakeholders
- [ ] Application performance dashboard for latency/uptime
- [ ] Compliance violation dashboard with automated scanning
- [ ] Unused resource identification and cleanup process
- [ ] Cost optimization recommendations tracked
- [ ] Quarterly cost optimization report

---

### EATGF-CLD-RES-01: Cloud Resilience & Disaster Recovery

| Field | Value |
|-------|-------|
| **Title** | Cloud Resilience & Disaster Recovery Management |
| **Description** | Cloud infrastructure implements multi-region/availability zone redundancy. Backup strategy, failover procedures, and RTO/RPO targets defined and tested annually. |
| **Governance Domain** | CLD |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS03 (Manage Service Continuity) + BAI03 (Manage IT Service Configuration) |
| **ISO 27001:2022** | A.8.24 (Recovery procedures) + A.8.25 (Redundancy) |
| **ISO 42001:2023 Clause** | 8.2 (Information security for AI systems) |
| **ISO 22301** | 8.1-8.5 (Business Continuity/DR requirements) |
| **Evidence Required** | Cloud resilience architecture, backup strategy, RTO/RPO SLAs, failover test results |
| **Control Owner** | Chief Technology Officer / Disaster Recovery Lead |
| **Evidence Owner** | Cloud Operations / DR Team |
| **Review Frequency** | Quarterly testing / Annual strategy |
| **Applicability** | SaaS / Enterprise |
| **Environment Profile** | Cloud / Multi-Cloud / Hybrid |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Multi-AZ/region architecture diagram documented
- [ ] RTO target defined per system (e.g., 4 hours max)
- [ ] RPO target defined per system (e.g., 1 hour max)
- [ ] Database backup strategy (frequency, retention, multi-region)
- [ ] Backup restoration testing completed monthly
- [ ] Failover procedures documented and tested
- [ ] Annual disaster recovery drill completed
- [ ] DR plan approved and communicated to organization

---

## 🔷 LAYER 9: DEVSECOPS CONTROLS ⭐ NEW

### EATGF-DEV-SDLC-01: Secure Software Development Lifecycle

| Field | Value |
|-------|-------|
| **Title** | Secure Software Development Lifecycle (Secure SDLC) |
| **Description** | All software development follows secure SDLC practices: threat modeling, secure coding standards, peer code review, security testing in each phase. |
| **Governance Domain** | DEV (DevSecOps & Development Practices) |
| **Control Type** | Preventive |
| **COBIT Reference** | BAI03 (Manage IT Service Configuration) + BAI06 (Manage IT Security) |
| **ISO 27001:2022** | A.8.19 (Change management) + A.8.25 (Development/test separation) + A.8.28 (Secure coding) + A.8.29 (Security testing in development) |
| **ISO 42001:2023 Clause** | 8 (Operational control of AI systems) |
| **OWASP SAMM** | Design / Implementation / Verification practices |
| **NIST SSDF** | Process evidence (PE) + Security practices (PO) |
| **Evidence Required** | SDLC policy, threat modeling docs, code review logs, security testing results |
| **Control Owner** | Engineering Lead / Application Security Lead |
| **Evidence Owner** | Development Team |
| **Review Frequency** | Per release |
| **Applicability** | All |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] SDLC process documented with security phases (design, code, test, deploy)
- [ ] Threat modeling performed for critical systems (STRIDE/DFD)
- [ ] Secure coding standards published (OWASP Top 10 compliance)
- [ ] Code review mandatory before merge (GitHub protected branches)
- [ ] Security testing checklist per phase documented
- [ ] Security training for developers completed (annual)
- [ ] SAST/DAST integrated into CI/CD pipeline
- [ ] Critical vulnerabilities block production deployment

---

### EATGF-DEV-SCAN-01: Automated Security Code Scanning (SAST/DAST/SCA)

| Field | Value |
|-------|-------|
| **Title** | Automated Security Code Scanning (SAST/DAST/SCA) |
| **Description** | All code changes scanned with SAST (static), DAST (dynamic), and SCA (composition). Vulnerability thresholds enforced. Findings tracked to closure. |
| **Governance Domain** | DEV |
| **Control Type** | Detective |
| **COBIT Reference** | BAI06 (Manage IT Security) - Primary / MEA01 (Monitor, Measure, and Assess) - Supporting |
| **ISO 27001:2022** | A.8.9 (Access control) + A.8.16 (Monitoring - vulnerability management) |
| **ISO 42001:2023 Clause** | 8.3 (AI system testing) |
| **OWASP Top 10** | A01-A10 (All vulnerability categories) |
| **Evidence Required** | SAST/DAST/SCA tool reports, scan results, remediation tracking |
| **Control Owner** | Application Security Lead |
| **Evidence Owner** | Security Engineering Team |
| **Review Frequency** | Per commit/continuous + Monthly reports |
| **Applicability** | All |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] SAST tool integrated in CI/CD (SonarQube/Checkmarx/similar)
- [ ] SAST blocking on CRITICAL findings before merge
- [ ] DAST scanner configured for pre-release testing (staging)
- [ ] SCA tool deployed for dependency vulnerability scanning (npm audit/Safety)
- [ ] Monthly security scan summary report
- [ ] Critical/High vulnerabilities remediation SLA tracked (7 days)
- [ ] False-positive ratio maintained <5%
- [ ] Developer training on vulnerability fixes completed

---

### EATGF-DEV-SUP-01: Software Supply Chain & SBOM Management

| Field | Value |
|-------|-------|
| **Title** | Software Supply Chain Security & SBOM Management |
| **Description** | All software components tracked via Software Bill of Materials (SBOM). Dependency vulnerabilities assessed. Build artifacts signed and verified. |
| **Governance Domain** | DEV |
| **Control Type** | Preventive |
| **COBIT Reference** | BAI06 (Manage IT Security) + APO13 (Manage IT Security Services) |
| **ISO 27001:2022** | A.8.19 (Change management) + A.8.1 (Information security policies - supply chain requirements) |
| **ISO 42001:2023 Clause** | 8.1 (Operational control) |
| **SLSA Framework** | Levels 1-3 (Supply chain leveling) |
| **NIST SSDF** | PO Practice (Supply chain security) |
| **Evidence Required** | SBOM for each release (CycloneDX/SPDX), signed artifacts, dependency scan results |
| **Control Owner** | Engineering Lead / DevOps Lead |
| **Evidence Owner** | Build & Release Team |
| **Review Frequency** | Per release |
| **Applicability** | All |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] SBOM generated for each release (CycloneDX or SPDX format)
- [ ] Dependency vulnerability scanning implemented (npm audit/pip check/Snyk)
- [ ] Build artifact signing enabled (Docker image signatures)
- [ ] Provenance tracking for all dependencies documented
- [ ] Build environment hardened (no root, immutable images)
- [ ] Artifact repository access controlled (pull-only)
- [ ] Supply chain risk assessment documented
- [ ] Incident response plan for compromised dependencies

---

### EATGF-DEV-CI-01: CI/CD Pipeline Integrity & Automation Security

| Field | Value |
|-------|-------|
| **Title** | CI/CD Pipeline Integrity & Security |
| **Description** | CI/CD pipeline protected: only authorized changes deployed, all stages logged, rollback capability enabled, automated testing enforced. |
| **Governance Domain** | DEV |
| **Control Type** | Preventive |
| **COBIT Reference** | BAI06 (Manage IT Security) |
| **ISO 27001:2022** | A.8.19 (Change management) + A.8.25 (Development/test separation) |
| **ISO 42001:2023 Clause** | 8 (Operational control) |
| **Evidence Required** | CI/CD pipeline configuration, pipeline logs, approval records, test results |
| **Control Owner** | DevOps Lead |
| **Evidence Owner** | Development Operations Team |
| **Review Frequency** | Monthly audit + per change |
| **Applicability** | All |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] CI/CD pipeline documented (GitHub Actions/GitLab CI/Jenkins)
- [ ] Automated tests required before deployment to production
- [ ] Code review approval required before merge (CODEOWNERS)
- [ ] Security scanning gates blocking critical findings
- [ ] Staging environment deployment before production
- [ ] Rollback capability tested quarterly
- [ ] Pipeline secrets managed securely (no hardcoded credentials)
- [ ] Audit logging enabled for all pipeline steps

---

## 🔷 LAYER 10: DATA PRIVACY CONTROLS ⭐ NEW

### EATGF-DATA-PRIV-01: Data Protection Impact Assessment (DPIA)

| Field | Value |
|-------|-------|
| **Title** | Data Protection Impact Assessment (DPIA) |
| **Description** | All high-risk data processing activities undergo Data Protection Impact Assessment. Assessments document risks, mitigation, and stakeholder consultation. |
| **Governance Domain** | DATA (Data Privacy & Protection) |
| **Control Type** | Preventive |
| **COBIT Reference** | APO12 (Manage Risk) |
| **ISO 27001:2022** | A.8.1 (Information security policies and procedures) |
| **ISO 27701:2019** | 8.1 (General requirements for privacy controls) |
| **ISO 42001:2023 Clause** | 6 (Organization of AI governance) |
| **GDPR** | Article 35 (Data Protection Impact Assessment) |
| **Evidence Required** | DPIA template, completed assessments, risk analysis, mitigation plans |
| **Control Owner** | Chief Data Officer / Data Privacy Officer |
| **Evidence Owner** | Privacy & Compliance Team |
| **Review Frequency** | Per new processing activity / Annual for existing |
| **Applicability** | All (mandatory if processing PII/sensitive data) |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] DPIA process documented and approved
- [ ] DPIA template created (processing purpose, lawfulness, necessity)
- [ ] Risk assessment for data handling completed
- [ ] Mitigation controls mapped to identified risks
- [ ] Data Controllers & Processors consulted
- [ ] Regulatory authority consultation if residual risks remain
- [ ] DPIAs tracked in central register
- [ ] Annual review of high-risk DPIAs

---

### EATGF-DATA-RET-01: Data Retention & Lifecycle Governance

| Field | Value |
|-------|-------|
| **Title** | Data Retention Schedule & Lifecycle Management |
| **Description** | Data retention schedules defined per data type and regulatory requirement. Automated retention enforcement and secure deletion implemented. Regular compliance reviews. |
| **Governance Domain** | DATA |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS01 (Manage Operations) + APO12 (Manage Risk) |
| **ISO 27001:2022** | A.8.1 (Information security) |
| **ISO 27701:2019** | 8.1 (Privacy controls) |
| **GDPR** | Article 5 (Storage limitation) + Article 17 (Right to erasure) |
| **Evidence Required** | Retention schedule document, deletion logs, compliance verification reports |
| **Control Owner** | Chief Data Officer |
| **Evidence Owner** | Data Governance Team |
| **Review Frequency** | Annual retention review + monthly enforcement |
| **Applicability** | All (if any personal/sensitive data) |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Data retention schedule documented (all data types and retention periods)
- [ ] Retention periods based on legal requirement, business need, compliance
- [ ] Automated deletion process implemented (scheduled jobs)
- [ ] Backup retention aligned with production retention policies
- [ ] Right-to-erasure process documented for individuals
- [ ] Monthly deletion verification logs maintained
- [ ] Annual compliance review of retention adherence
- [ ] Exception process for legal holds documented

---

### EATGF-DATA-MIN-01: Data Minimization & Purpose Limitation

| Field | Value |
|-------|-------|
| **Title** | Data Minimization & Purpose Limitation Enforcement |
| **Description** | Data collection limited to necessary for stated purpose. Regular audits verify only required data collected. Purpose limitation enforced in code and policies. |
| **Governance Domain** | DATA |
| **Control Type** | Preventive |
| **COBIT Reference** | APO12 (Manage Risk) |
| **ISO 27001:2022** | A.8.1 (Information security) |
| **ISO 27701:2019** | 8.2 (Privacy-by-design) |
| **GDPR** | Article 5 (Data minimization principle) |
| **Evidence Required** | Data minimization policy, audit results, vendor compliance reviews |
| **Control Owner** | Chief Data Officer / Privacy Officer |
| **Evidence Owner** | Privacy & Compliance Team |
| **Review Frequency** | Annual audit + quarterly sample review |
| **Applicability** | All (if collecting any personal data) |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Data minimization policy documented and approved
- [ ] Customer-facing forms/APIs collect only necessary fields
- [ ] Data science/analytics teams restricted to non-PII or consented PII
- [ ] Quarterly audit of data collected vs. stated purpose
- [ ] Access control restricts employees to minimum necessary data
- [ ] Data sharing with third parties has explicit legal approval
- [ ] Training on data minimization for data handlers completed

---

## 🔷 LAYER 11: BUSINESS CONTINUITY CONTROLS ⭐ NEW

### EATGF-BCP-PLAN-01: Business Continuity & Disaster Recovery Planning

| Field | Value |
|-------|-------|
| **Title** | Business Continuity & Disaster Recovery Planning |
| **Description** | Organization maintains comprehensive BC/DR plans covering all critical systems. Plans include: recovery procedures, communication, alternative facilities, roles/responsibilities. |
| **Governance Domain** | BCP (Business Continuity & Disaster Recovery) |
| **Control Type** | Preventive |
| **COBIT Reference** | DSS03 (Manage Service Continuity) + BAI06 (Manage IT Security) |
| **ISO 27001:2022** | A.8.24 (Recovery procedures) + A.8.25 (Redundancy) |
| **ISO 22301:2019** | 8.1-8.5 (Business Continuity Management System) |
| **Evidence Required** | BC/DR plan document, recovery procedures, contact lists, communication templates |
| **Control Owner** | Chief Resilience Officer / BC Manager |
| **Evidence Owner** | Business Continuity Team |
| **Review Frequency** | Annual plan review + per material change |
| **Applicability** | SaaS / Enterprise |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Comprehensive BC/DR plan document created (10+ pages)
- [ ] Critical systems identified and prioritized with RTO/RPO
- [ ] Recovery procedures detailed for each critical system
- [ ] Alternative sites/facilities identified (hot/warm/cold standby)
- [ ] Internal & external communication plans documented
- [ ] Contact lists with roles, phone numbers, escalation
- [ ] Recovery team assigned with specific roles
- [ ] Plan approved by executive leadership

---

### EATGF-BCP-TEST-01: Business Continuity Testing & Validation

| Field | Value |
|-------|-------|
| **Title** | Business Continuity Testing & Validation |
| **Description** | BC/DR plans tested annually (full exercise) and semi-annually (tabletop). Test results documented, gaps identified, lessons learned captured. |
| **Governance Domain** | BCP |
| **Control Type** | Detective |
| **COBIT Reference** | MEA01 (Monitor IT Resources) + MEA03 (Monitor Compliance) |
| **ISO 27001:2022** | A.8.24 (Testing) + A.8.25 (Redundancy) |
| **ISO 22301:2019** | 8.3 (Testing and exercise) |
| **Evidence Required** | BC test plan, test results, gap findings, corrective actions |
| **Control Owner** | Chief Resilience Officer / BC Manager |
| **Evidence Owner** | Business Continuity Team |
| **Review Frequency** | Annual full test + Semi-annual tabletop |
| **Applicability** | SaaS / Enterprise |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] Annual BC/DR test plan documented (scope, systems, procedures)
- [ ] Full-scale recovery test completed (actual system failover)
- [ ] Test results documented (success/failure, time to recover)
- [ ] Lessons learned meeting held post-test
- [ ] Gaps identified and tracked to closure
- [ ] Tabletop exercise completed (semi-annual)
- [ ] RTO/RPO validation against test results
- [ ] Improvements incorporated into next year's plan

---

### EATGF-BCP-RTO-01: Recovery Time Objective (RTO) & Recovery Point Objective (RPO) Management

| Field | Value |
|-------|-------|
| **Title** | RTO/RPO Definition, Achievement & Monitoring |
| **Description** | RTO (max tolerable downtime) and RPO (max acceptable data loss) defined per system. Monitoring validates achievement. Alerts on SLA breach. |
| **Governance Domain** | BCP |
| **Control Type** | Detective |
| **COBIT Reference** | MEA01 (Monitor IT Resources) |
| **ISO 27001:2022** | A.8.24 (Recovery procedures) + 9.1 (Monitoring) |
| **ISO 22301:2019** | 8.5 (Continuity monitoring) |
| **Evidence Required** | RTO/RPO targets per system, monitoring dashboard, SLA compliance reports |
| **Control Owner** | Chief Technology Officer / Operations Lead |
| **Evidence Owner** | Operations & Resilience Team |
| **Review Frequency** | Monthly monitoring + Annual target review |
| **Applicability** | All (critical systems mandatory) |
| **Environment Profile** | Cloud / Hybrid / On-Prem |
| **Status** | Planned |

**Evidence Checklist:**
- [ ] RTO targets defined per system (max hours downtime acceptable)
- [ ] RPO targets defined per system (max hours data loss acceptable)
- [ ] Backup frequency aligns with RPO targets
- [ ] RTO/RPO dashboard live (automated monitoring)
- [ ] Monthly SLA compliance reports reviewed
- [ ] Breach notifications and root cause analysis
- [ ] Improvement actions tracked and implemented
- [ ] Test verification that RTO/RPO targets are achievable

---
## � CONTROL SUMMARY TABLE (Updated)

| ID | Title | Domain | Type | Owner | Frequency | Startup | SaaS | Enterprise | Environment |
|----|-------|--------|------|-------|-----------|---------|------|------------|---|
| **GOVERNANCE LAYER** | | | | | | | | | |
| EATGF-EDM-RISK-01 | Risk Appetite Definition | EDM | Governance | CGO | Annual | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-EDM-BEN-01 | Benefits Monitoring | EDM | Detective | CFO | Quarterly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-EDM-GOV-01 | Governance Model | EDM | Governance | CGO | Annual | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| **STRATEGY LAYER** | | | | | | | | | |
| EATGF-APO-ARCH-01 | Architecture Framework | APO | Preventive | CArch | Annual | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-APO-RISK-01 | Risk Register | APO | Preventive | CRO | Quarterly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-APO-SEC-01 | ISMS | APO | Governance | CISO | Annual | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-APO-AI-01 | AIMS | APO | Governance | CAI | Quarterly | ❌ | ⚠️ | ✅ | Cloud/Hybrid/On-Prem |
| **BUILD & CHANGE LAYER** | | | | | | | | | |
| EATGF-BAI-CHG-01 | Change Management | BAI | Preventive | Eng Lead | Monthly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-BAI-CONF-01 | Configuration Control | BAI | Detective | DevOps | Continuous | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-BAI-TEST-01 | QA & Testing | BAI | Preventive | QA Lead | Per Release | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| **OPERATIONS & SECURITY LAYER** | | | | | | | | | |
| EATGF-DSS-SEC-01 | IAM | DSS | Preventive | Security | Quarterly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DSS-ENC-01 | Encryption | DSS | Preventive | Security | Quarterly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DSS-VULN-01 | Patch Management | DSS | Preventive | Security | Monthly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DSS-INC-01 | Incident Response | DSS | Corrective | Security | Per Incident | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| **MONITORING & AUDIT LAYER** | | | | | | | | | |
| EATGF-MEA-AUD-01 | Internal Audit | MEA | Detective | Compliance | Annual | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-MEA-PERF-01 | Performance Monitoring | MEA | Detective | Governance | Quarterly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-MEA-MAT-01 | Maturity Assessment | MEA | Detective | Governance | Annual | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| **CLOUD GOVERNANCE LAYER** ⭐ NEW | | | | | | | | | |
| EATGF-CLD-ARCH-01 | Cloud Architecture | CLD | Preventive | Cloud Arch | Annual | ❌ | ✅ | ✅ | Cloud/Multi-Cloud/Hybrid |
| EATGF-CLD-SEC-01 | Cloud Security | CLD | Preventive | Cloud Sec | Monthly | ❌ | ✅ | ✅ | Cloud/Multi-Cloud/Hybrid |
| EATGF-CLD-MON-01 | Cloud Monitoring | CLD | Detective | Cloud Ops | Monthly | ❌ | ✅ | ✅ | Cloud/Multi-Cloud/Hybrid |
| EATGF-CLD-RES-01 | Cloud Resilience | CLD | Preventive | CTO | Quarterly | ❌ | ✅ | ✅ | Cloud/Multi-Cloud/Hybrid |
| **DEVSECOPS LAYER** ⭐ NEW | | | | | | | | | |
| EATGF-DEV-SDLC-01 | Secure SDLC | DEV | Preventive | Eng Lead | Per Release | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DEV-SCAN-01 | SAST/DAST/SCA | DEV | Detective | AppSec | Continuous | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DEV-SUP-01 | Supply Chain & SBOM | DEV | Preventive | DevOps | Per Release | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DEV-CI-01 | CI/CD Pipeline | DEV | Preventive | DevOps | Per Deploy | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| **DATA PRIVACY LAYER** ⭐ NEW | | | | | | | | | |
| EATGF-DATA-PRIV-01 | DPIA | DATA | Preventive | DPO | Per Activity | ✅* | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DATA-RET-01 | Data Retention | DATA | Preventive | CDO | Annual | ✅* | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-DATA-MIN-01 | Data Minimization | DATA | Preventive | DPO | Quarterly | ✅* | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| **BUSINESS CONTINUITY LAYER** ⭐ NEW | | | | | | | | | |
| EATGF-BCP-PLAN-01 | BC/DR Planning | BCP | Preventive | Resilience | Annual | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-BCP-TEST-01 | BC/DR Testing | BCP | Detective | Resilience | Annual | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-BCP-RTO-01 | RTO/RPO Management | BCP | Detective | Ops | Monthly | ❌ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| **AI GOVERNANCE LAYER** | | | | | | | | | |
| EATGF-AI-LC-01 | AI Lifecycle | BAI | Preventive | AI Lead | Per Release | ❌ | ⚠️ | ✅ | Cloud/Hybrid |
| EATGF-AI-RISK-01 | AI Risk & Bias | EDM | Preventive | AI Risk | Per Update | ❌ | ⚠️ | ✅ | Cloud/Hybrid |
| **API GOVERNANCE LAYER** | | | | | | | | | |
| EATGF-API-SEC-01 | API Auth | DSS | Preventive | API Lead | Quarterly | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |
| EATGF-API-LC-01 | API Lifecycle | BAI | Preventive | API PM | Per Release | ✅ | ✅ | ✅ | Cloud/Hybrid/On-Prem |

**Legend:**
- ✅ = Mandatory for edition
- ❌ = Not applicable for edition
- ⚠️ = Conditional (if applicable to organization)
- ✅* = Conditional (if processing personal data)
- Cloud/Hybrid/On-Prem/Multi-Cloud = Applicable environment(s)

---

## 🔗 MCM TO EVIDENCE MAPPING

Each control maps to specific evidence requirements:

### Evidence Types
1. **Document-based:** Policy, procedure, charter, manual
2. **System-based:** Dashboard, log, audit trail, configuration
3. **Process-based:** Meeting minutes, review record, approval log
4. **Assessment-based:** Assessment report, test results, audit report

### Evidence Lifecycle
- **Collection:** Evidence gathered per review frequency
- **Storage:** Centralized evidence repository (SharePoint/Confluence)
- **Verification:** Evidence validated before audit
- **Retention:** Minimum 7 years (regulatory requirement)
- **Destruction:** Secure deletion per data retention policy

---

## 📊 MCM USAGE GUIDE

### For ISO 27001 SoA
1. Filter/copy controls marked "ISO 27001 Annex A"
2. Populate SoA Template with column mappings
3. Add applicability justifications
4. Review and approve

### For Audit Preparation
1. Review all controls in MCM
2. Gather evidence per checklist
3. Verify completeness
4. Submit to auditor

### For Control Assessment
1. Select control by ID
2. Review description and evidence
3. Assess current state (implemented/partial/not)
4. Plan remediation if needed

### For Compliance Reporting
1. Filter by applicability (Startup/SaaS/Enterprise)
2. Generate status dashboard
3. Create exception report
4. Executive summary

---

## 📅 VERSION & STATUS

**Framework:** EATGF v1.0 (MCM Complete - Phase 1.5 Integrated)  
**Total Controls:** 35 (21 Foundation + 14 Expansion)  
**Document Version:** 1.0 (Integrated)  
**Last Updated:** February 13, 2026  
**Status:** ✅ **UNIFIED MCM READY FOR PHASE 2**  

---

## 📅 NEXT STEPS (Phase 2)

**These steps will be completed AFTER MCM v1.0 is fully integrated:**

**Phase 2A (Week 1):**
- [ ] Update Statement of Applicability Template with 35 controls
- [ ] Update Governance Charter with CLD/DEV/DATA/BCP domains
- [ ] Validate Framework Mappings with new controls

**Phase 2B (Week 2):**
- [ ] Create ISMS Manual outline (ISO 27001 - Layer 3)
- [ ] Create AIMS Manual outline (ISO 42001 - Layer 3)
- [ ] Create Internal Audit Procedure (MEA-AUD-01 implementation)

**Phase 2C (Week 3):**
- [ ] Create Evidence Register Template (centralized tracking)
- [ ] Create Risk Appetite Statement (formal EDM-RISK-01 doc)
- [ ] Create Management System Layer documentation

---

## 📞 GOVERNANCE & MAINTENANCE

**MCM Authority:** Chief Governance Officer  
**MCM Owner:** Governance Council  
**Update Frequency:** Semi-annual (Feb & Aug)  
**Emergency Updates:** As-needed for regulatory changes  

**Questions:** Directed to the Governance Council via internal channels.  
**Escalation:** Directed to the Chief Governance Officer via the defined escalation chain.

---

## 🔗 STANDARDS ALIGNMENT STATEMENT

This **Master Control Matrix (MCM) v1.0** framework aligns with the following international standards and frameworks:

| Standard | Version | Alignment Scope | Reference Type |
|----------|---------|-----------------|-----------------|
| **COBIT 2019** | 2019 | Primary governance framework | Normative |
| **ISO/IEC 27001** | 2022 | Information security management | Normative |
| **ISO/IEC 42001** | 2023 | AI management system | Normative |
| **ISO/IEC 27701** | 2019 | Privacy extension guidance | Informative |
| **ISO 31000** | 2018 | Risk management principles | Informative |
| **NIST AI Risk Management Framework** | 1.0 | AI governance alignment | Informative |
| **NIST SP 800-53** | Revision 5 | Security control reference | Informative |
| **OWASP API Security Top 10** | 2023 | API security guidance | Informative |
| **OWASP SAMM** | 2.0 | Development maturity model | Informative |

### Intellectual Property Notice

- **COBIT 2019** is © ISACA. All rights reserved.
- **ISO/IEC Standards** are © ISO. All rights reserved.
- **NIST Framework** is public domain (U.S. Government).
- **OWASP Materials** are open source and subject to OWASP licensing.

This MCM does not reproduce or extract copyrighted text from these standards. All mappings represent **derivative interpretations and guidance references only** and are not intended as republication or translation of the original standards.

### Framework Authorities & Limitations

**Governance Coverage:**
- This framework provides comprehensive coverage of governance controls across COBIT 2019, ISO 27001:2022, and ISO 42001:2023.
- Coverage is based on alignment interpretation and does not guarantee complete coverage of all standards' provisions.

**Audit & Compliance:**
- This MCM is designed for **internal governance guidance** and **audit preparation**.
- External certification bodies must conduct independent compliance assessments and validation.
- Status field reflects internal maturity only and requires external audit for certification claims.

**AI Management System (AIMS):**
- Controls mapped to ISO 42001:2023 reflect AI governance best practices.
- ISO 27701 references for privacy controls are **informative guidance only** and do not imply PIMS (Privacy Information Management System) certification.

---

**Framework:** Enterprise AI-Aligned Technical Governance Framework (EATGF)  
**Document Type:** Master Control Matrix (Unified - Phase 1.5 Integrated)  
**Document Version:** 1.0 (Phase 1.5 Complete: 35 Controls Integrated)  
**Last Updated:** February 13, 2026  
**Next Review:** August 2026  
**Status:** ✅ **MCM v1.0 UNIFIED - READY FOR PHASE 2 (ISMS/AIMS/Audit Layer)**
