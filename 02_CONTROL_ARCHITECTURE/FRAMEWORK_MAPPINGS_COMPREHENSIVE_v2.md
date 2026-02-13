# ENTERPRISE AI-ALIGNED TECHNICAL GOVERNANCE FRAMEWORK (EATGF)
## COMPREHENSIVE STANDARDS MAPPING DOCUMENT

**Framework:** EATGF v1.0  
**Document Type:** Technical Mapping Reference  
**Version:** 2.0 (MCM-Aligned)  
**Date:** February 13, 2026  
**Authority:** Enterprise Architecture & Governance Office  
**Classification:** Technical - For Auditors & Compliance Officers

---

## 📋 EXECUTIVE SUMMARY

This document provides **complete bidirectional mappings** between:

1. **EATGF Master Control Matrix (MCM)** - Central control authority
2. **COBIT 2019** - Governance domains (EDM/APO/BAI/DSS/MEA)
3. **ISO 27001:2022** - Information Security Management (76 Annex A controls)
4. **ISO 42001:2024** - AI Management Systems (if applicable)
5. **NIST AI Risk Management Framework (AI RMF)** - AI risk governance
6. **OWASP 2023** - API security controls
7. **NIST SP 800-53** - US government security controls (if applicable)

The mappings enable:
- ✅ Unified control architecture across standards
- ✅ Single evidence collection for multiple standards (cost efficiency)
- ✅ Audit readiness for ISO 27001, ISO 42001, SOC 2, frameworks
- ✅ Risk-based control prioritization
- ✅ Traceability from strategy to evidence

---

## 🔗 MAPPING ARCHITECTURE

### Central Hub Model

```
                        ┌─────────────────┐
                        │  EATGF MCM      │
                        │ (21 Controls)   │
                        └─────────────────┘
                                │
                ┌───────┬───────┼───────┬───────┬────────┐
                ↓       ↓       ↓       ↓       ↓        ↓
             COBIT   ISO     ISO    NIST    OWASP   NIST
             2019    27001   42001   AI RMF  2023    800-53
```

**Key Principle:** EATGF MCM is the **central control authority**. All standards are mapped TO the MCM, not vice versa. This:
1. Simplifies control implementation
2. Enables evidence reuse across standards
3. Reduces redundancy and conflicting controls
4. Provides unified governance dashboard

---

## 📊 SECTION 1: CONTROL-LEVEL MAPPINGS

### 1.1 EDM Domain - Evaluate, Direct, Monitor

#### EATGF-EDM-RISK-01: IT & AI Risk Appetite Definition

**Mapping Summary:**
| Standard | Reference | Applicability | Evidence Linkage |
|----------|-----------|---|---|
| COBIT 2019 | EDM03 | ✅ All | Risk tolerance statement |
| ISO 27001 | Clause 6.1.2 | ✅ SaaS/Enterprise | SoA, risk assessment |
| ISO 42001 | Clause 6 | ⚠️ AI systems | AI risk framework |
| NIST AI RMF | GOVERN-2 | ⚠️ AI systems | AI governance doc |

**Detailed Mapping:**
```
EATGF-EDM-RISK-01
├─ COBIT 2019
│  ├─ EDM03.01: Evaluate current IT governance
│  ├─ EDM03.02: Direct IT governance implementation
│  └─ EDM03.03: Monitor IT governance
├─ ISO 27001:2022
│  ├─ Clause 6.1.2: Risk assessment process
│  ├─ Clause 8.1: Operational planning and control
│  └─ Clause 9.1: Monitoring and measurement
├─ ISO 42001:2024
│  ├─ Clause 6.1: Risk and opportunities
│  └─ Clause 8.1: Operational planning
└─ NIST AI RMF
   ├─ GOVERN-2: Risk and benefit analysis
   └─ MEASURE-1: Data validation processes
```

**Minimum Evidence Required:**
1. Board-approved Risk Appetite Statement (signed/dated)
2. Risk tolerance thresholds (Critical/High/Medium/Low for each category)
3. AI-specific risk thresholds (if applicable)
4. Data breach/compliance thresholds
5. Annual review documentation

**Owner:** Chief Governance Officer / Risk Officer  
**Review Frequency:** Annual

---

#### EATGF-EDM-BEN-01: Technology Value & Benefits Monitoring

| Standard | Reference | Clauses | Applicability |
|----------|-----------|---------|---|
| COBIT 2019 | EDM02 | EDM02.01-03 | ✅ All |
| ISO 27001 | Clause 9.1 | 9.1.1, 9.1.2 | ✅ SaaS/Enterprise |
| NIST AI RMF | MEASURE-1 | Performance metrics | ⚠️ AI systems |

**Mapping Logic:**
- EDM02 (COBIT) = Benefits realization oversight → ISO 27001 Clause 9.1 (monitoring)
- Governance KPIs (DORA, security, compliance) = Evidence for both standards
- Monthly dashboards feed quarterly board reports

---

#### EATGF-EDM-GOV-01: Governance Model & Structure

| Standard | Reference | Mapping Type | Status |
|----------|-----------|---|---|
| COBIT 2019 | EDM01 | PRIMARY | ✅ Mapped |
| ISO 27001 | Clause 5.3 | Roles & responsibilities | ✅ Mapped |
| ISO 42001 | Clause 5.4 | Accountability | ⚠️ If AI |

**Evidence Mapping:**
```
Control Requirement:
├─ Governance Charter (2+ pages)
├─ RACI Matrix (responsibilities)
├─ Committee Charters (3+)
├─ Escalation Procedures
└─ Approval Authority Matrix

Satisfies:
├─ COBIT EDM01 (Governance structure)
├─ ISO 27001 5.3 (Roles & responsibilities)
├─ ISO 27001 5.2 (Information security policy)
└─ ISO 42001 5.4 (Accountability)
```

---

### 1.2 APO Domain - Align, Plan, Organize

#### EATGF-APO-ARCH-01: Enterprise Architecture Framework

**Multi-Standard Mapping:**

| COBIT | ISO | NIST | Evidence |
|-------|-----|------|----------|
| APO03.02 | A.8.21 | N/A | Architecture standards doc |
| APO03.03 | 5.4 | N/A | Current-state architecture |
| APO03.04 | N/A | N/A | Target-state architecture |

**Evidence Linkage:**
1. Architecture standards document (policies, patterns)
2. Architecture review board charter
3. Current-state vs target-state diagrams
4. Control mapping to architecture
5. ARB decision log (monthly)

**Applicability Note:**
- Mandatory for SaaS/Enterprise
- Optional for Startup (one-person team may document informally)

---

#### EATGF-APO-RISK-01: IT & AI Risk Register Management

**Comprehensive Mapping:**

```
EATGF-APO-RISK-01
├─ COBIT 2019: APO12 (Manage Risk)
│  ├─ 12.01: Risk identification
│  ├─ 12.02: Risk assessment
│  ├─ 12.03: Risk response
│  ├─ 12.04: Risk monitoring
│  └─ 12.05: Risk reporting
├─ ISO 27001: Clause 6.1.2
│  ├─ Risk assessment scope
│  ├─ Risk assessment methodology
│  ├─ Risk criteria
│  ├─ Risk analysis
│  └─ Risk evaluation
├─ ISO 42001: Clause 6.1.1
│  ├─ AI risk assessment
│  └─ Mitigation planning
└─ NIST AI RMF: GOVERN-1, MAP-1
   ├─ Risk categorization
   └─ Measurement frameworks
```

**Evidence Types:**
1. Risk register (spreadsheet/system) with 50+ identified risks
2. Risk assessment methodology documentation
3. Risk heat map (Probability × Impact)
4. Top 10 Critical/High risk mitigation plans
5. Monthly escalation tracking
6. Quarterly risk trending analysis

**System Integration:**
- Risk data feeds into: SoA, audit planning, board reporting
- Reused by: ISO 27001 RTO/RPO risk analysis
- Extended by: AI risk assessment (if applicable)

---

#### EATGF-APO-SEC-01: Information Security Management System (ISMS)

**Master Mapping (Requires Extensive Alignment):**

| COBIT | ISO 27001 | Scope |
|-------|-----------|-------|
| APO13 | Clauses 4-10 | Complete ISMS |
| APO13.01 | 5 (Leadership) | Policy governance |
| APO13.02 | 6 (Planning) | Risk planning |
| APO13.03 | 7 (Support) | Resource allocation |
| APO13.04 | 8 (Operations) | Control implementation |
| APO13.05 | 9 (Performance eval) | Measurement |

**Key Evidence:**
1. ISMS Manual (ISO 27001 structured)
2. Statement of Applicability (SoA) - 76 controls selected/excluded
3. Information security policy suite (7-10 policies)
4. Risk assessment report
5. Internal audit reports
6. Corrective/preventive action tracking
7. Management review documentation

**Evidence Reuse Benefit:**
- Single ISMS implementation satisfies both COBIT APO13 AND ISO 27001 requirements
- SoA directly supports audit readiness

---

#### EATGF-APO-AI-01: AI Governance System (AIMS)

**ISO 42001 Primary Mapping:**

| ISO 42001 Clause | COBIT Equivalent | Mapping |
|---|---|---|
| 4 (Context) | APO01 | Organization understanding |
| 5 (Leadership) | APO04 | AI governance leadership |
| 6 (Planning) | APO12 | AI risk planning |
| 7 (Support) | APO08 | Resource management |
| 8 (Operation) | BAI03 | AI system lifecycle |
| 9 (Performance) | MEA01 | AI performance monitoring |
| 10 (Improvement) | MEA03 | AI audit and review |

**NIST AI RMF Alignment:**

| NIST AI RMF | AIMS Clause | Evidence |
|---|---|---|
| GOVERN | 5, 6 | AI governance charter |
| MAP | 6 | AI risk mapping |
| MEASURE | 9 | Model performance metrics |
| MANAGE | 8 | AI lifecycle controls |

**Evidence Structure:**
1. AIMS Manual (ISO 42001 template)
2. AI System Registry (all AI systems listed)
3. AI governance committee charter
4. AI model documentation standard
5. Fairness/bias assessment process
6. Model performance monitoring dashboard
7. AI incident response procedures

---

### 1.3 BAI Domain - Build, Acquire, Implement

#### EATGF-BAI-CHG-01: Controlled Change Management

**Triple-Standard Mapping:**

| Framework | Standard | Example Clause |
|-----------|----------|---|
| COBIT | BAI06 | Change request & approval |
| ISO 27001 | A.8.19 | Change approval procedures |
| NIST 800-53 | CM-3 | Change control procedures |

**Evidence Unified Approach:**
```
Single process satisfies all three:
├─ Engineering change log (JIRA/ADO)
│  ├─ Change request [BAI06, A.8.19]
│  ├─ Risk assessment [BAI06]
│  ├─ Approval gate [CM-3]
│  └─ Deployment record [all three]
├─ Change Advisory Board (CAB)
│  ├─ Monthly meetings [BAI06.02]
│  ├─ Approval authority [all three]
│  └─ Decision log [all three]
└─ Rollback testing
   ├─ Recovery procedures [A.8.19]
   └─ Test results [all three]
```

**Integration:**
- Change log is audit evidence for ISO 27001, SOC 2, COBIT
- CAB minutes = Change impact assessment evidence
- Zero additional process needed for compliance

---

#### EATGF-BAI-CONF-01: Configuration & Version Control

**Mapping:**

| COBIT | ISO 27001 | Mapping |
|-------|-----------|---------|
| BAI10.01 | A.8.9 | Configuration baselines |
| BAI10.02 | A.8.9 | Configuration tracking |
| BAI10.03 | A.8.9 | Configuration integrity |

**Evidence Types:**
1. Git repository with branch protection rules
2. Commit history and signed commits
3. Configuration baseline docs
4. Access control for code/config (RBAC)
5. Monthly audit of configuration changes
6. Infrastructure-as-code documentation

**Satisfies:**
- COBIT: Configuration management control objectives
- ISO 27001: A.8.9 (Access to information and other assets)
- DevSecOps: Audit trail for compliance

---

#### EATGF-BAI-TEST-01: Quality Assurance & Testing

**Multi-Platform Mapping:**

| Framework | Reference | Element |
|-----------|-----------|---------|
| COBIT | BAI03 | Configuration testing |
| ISO 27001 | A.8.9 | Security testing |
| NIST 800-53 | CA-2 | Security assessment |
| OWASP | Testing Guide | SAST/DAST/SCA |

**Evidence Portfolio:**
```
Testing Requirements:
├─ Unit Test Results (70%+ coverage required)
├─ Integration Tests (100% of APIs)
├─ Security Tests
│  ├─ SAST (Static analysis) - per commit
│  ├─ DAST (Dynamic analysis) - pre-release
│  └─ SCA (Component scan) - continuous
├─ Performance Tests (vs. baseline)
├─ UAT Sign-Off (business acceptance)
└─ Security Scan Results (OWASP scan report)

Satisfies:
├─ COBIT: BAI03 (Service configuration)
├─ ISO 27001: A.8.9 (Change security testing)
├─ OWASP: Testing practices
└─ SOC 2: Change management
```

---

### 1.4 DSS Domain - Deliver, Service, Support

#### EATGF-DSS-SEC-01: Identity & Access Management (IAM)

**Universal Control (Applies to All Standards):**

| Standard | Clause | Scope |
|----------|--------|-------|
| COBIT | DSS05 (Manage Identity & Access) | All access types |
| ISO 27001 | A.5.15-A.5.18 | User access control |
| NIST 800-53 | AC-2, AC-3 | Account & access control |
| SOC 2 | CC6.1-6.2 | Access control |

**Control Architecture:**

```
IAM Foundation
├─ Centralized identity platform (Okta/Azure/similar)
├─ Authentication
│  ├─ MFA required for sensitive systems
│  ├─ SSO for all cloud systems
│  └─ Passwordless authentication (future target)
├─ Authorization (RBAC)
│  ├─ Role definitions per system
│  ├─ Access control matrix (RACI)
│  └─ Role review quarterly
├─ Provisioning
│  ├─ Automated (Okta/system connectors)
│  └─ Approval workflow
├─ Deprovisioning
│  ├─ Same-day removal on termination
│  └─ Service account rotation
└─ Monitoring
   ├─ Access review (quarterly)
   ├─ Audit logs (12-month retention)
   └─ Privileged access monitoring

Evidence Satisfies:
├─ COBIT DSS05 (5 control objectives)
├─ ISO 27001 A.5.15-A.5.18 (4 control objectives)
├─ NIST 800-53: AC-2, AC-3, AC-5
├─ SOC 2: CC6 (6 trust service criteria)
└─ Single audit exam for all frameworks
```

**Evidence Reuse:**
- Okta dashboard = COBIT evidence + ISO 27001 evidence + SOC 2 evidence
- Quarterly access review = Compliance across all frameworks
- Audit logs = Single evidence source for 4+ frameworks

---

#### EATGF-DSS-ENC-01: Data Encryption & Protection

**Mapping:**

| Framework | Reference | Requirement |
|-----------|-----------|---|
| COBIT | DSS07 | Cryptographic security |
| ISO 27001 | A.10.1 | Cryptographic controls |
| NIST 800-53 | SC-7, SC-28 | Boundary protection, encryption |

**Evidence Structure:**
```
Encryption Implementation:
├─ At-Rest Encryption
│  ├─ Database encryption (AES-256)
│  ├─ Backup encryption (AES-256)
│  └─ Archive encryption (AES-256)
├─ In-Transit Encryption
│  ├─ TLS 1.2+ (minimum)
│  ├─ Certificate management
│  └─ Perfect forward secrecy (ideal)
├─ Key Management
│  ├─ HSM for key storage
│  ├─ Key rotation schedule (bi-annual)
│  └─ Separation of duties
└─ Evidence
   ├─ Encryption audit report
   ├─ Configuration screenshots
   ├─ Key rotation logs
   └─ Certificate inventory

Satisfies:
├─ COBIT DSS07 (3 control objectives)
├─ ISO 27001 A.10.1 (2 control clauses)
├─ NIST 800-53: SC-28 (information protection)
└─ Regulatory: GDPR, HIPAA (encryption standards)
```

---

#### EATGF-DSS-VULN-01: Vulnerability & Patch Management

**Mapping (Critical for Operational Security):**

| Framework | Reference | Scope |
|----------|-----------|-------|
| COBIT | DSS06 | Integrated monitoring |
| ISO 27001 | A.12.6 | Vulnerability management |
| NIST 800-53 | SI-2 | Flaw remediation |

**Control Process:**

```
Vulnerability Management Lifecycle:
├─ Scanning (Monthly minimum)
│  ├─ Network scanning (Qualys/Tenable)
│  ├─ Application scanning (SAST/DAST)
│  └─ Threat intelligence integration
├─ Classification
│  ├─ Critical: 24-hour SLA
│  ├─ High: 7-day SLA
│  ├─ Medium: 30-day SLA
│  └─ Low: 90-day SLA
├─ Remediation
│  ├─ Patch development/testing
│  ├─ Deployment per SLA
│  └─ Verification testing
├─ Exception Process
│  ├─ Risk acceptance (if not patching)
│  ├─ Compensating control (required)
│  └─ Exception duration limit
└─ Evidence
   ├─ Monthly scan reports
   ├─ Patch deployment logs
   ├─ Exception tracking
   └─ Compliance metrics

Satisfies:
├─ COBIT: DSS06 (5 control objectives)
├─ ISO 27001: A.12.6 (3 control objectives)
├─ NIST 800-53: SI-2 (patch management)
└─ Security best practice
```

---

#### EATGF-DSS-INC-01: Incident Response Management

**Universal Control (All Standards):**

| Framework | Clause | Requirement |
|-----------|--------|---|
| COBIT | DSS02 | Incident management |
| ISO 27001 | A.5.24-A.5.27 | Incident management (4 controls) |
| NIST 800-53 | IR-1:IR-8 | Incident response |
| SOC 2 | C1 | Availability |

**Incident Response Process:**

```
Incident Management Framework:
├─ Detection
│  ├─ SIEM monitoring (24/7)
│  ├─ Alert thresholds
│  └─ Threat intelligence
├─ Response
│  ├─ Incident classification (Severity 1-4)
│  ├─ Notification (1 hour max)
│  ├─ Investigation
│  └─ Containment
├─ Recovery
│  ├─ Eradication
│  ├─ System restoration
│  └─ Evidence preservation
├─ Post-Incident
│  ├─ Root cause analysis (RCA)
│  ├─ Lessons learned
│  ├─ Improvement actions
│  └─ Regulatory notification (if breach)
└─ Evidence
   ├─ Incident tickets (100% documented)
   ├─ Timeline documentation
   ├─ RCA reports
   ├─ Remediation tracking
   └─ Trend analysis (quarterly)

Satisfies:
├─ COBIT: DSS02 (6 control objectives)
├─ ISO 27001: A.5.24-A.5.27 (responses & breach notification)
├─ NIST 800-53: IR-4 (incident handling)
├─ Breach notification laws (GDPR, CCPA, etc.)
└─ Insurance/ransomware response
```

---

### 1.5 MEA Domain - Monitor, Evaluate, Assess

#### EATGF-MEA-AUD-01: Internal Audit Program

**Mapping (Audit Oversight):**

| Framework | Reference | Role |
|-----------|-----------|------|
| COBIT | MEA03 | Audit compliance |
| ISO 27001 | Clause 9.2 | Internal audit requirements |
| ISO 42001 | Clause 9 | Performance evaluation |

**Audit Structure:**

```
Annual Internal Audit Program:
├─ Audit Plan
│  ├─ Audit scope (all major processes)
│  ├─ Risk-based selection of audit areas
│  ├─ Audit frequency per risk level
│  └─ Audit team (internal OR external)
├─ Audit Execution
│  ├─ Pre-audit: Planning & scoping
│  ├─ Fieldwork: Evidence gathering
│  ├─ Testing: Control testing
│  └─ Reporting: Findings documentation
├─ Finding Classification
│  ├─ Critical findings (immediate action)
│  ├─ Major findings (30-day remediation)
│  ├─ Minor findings (90-day remediation)
│  └─ Observations (informational)
├─ Remediation Tracking
│  ├─ Management action plan (MAP)
│  ├─ Responsible owner assignment
│  ├─ Deadline tracking
│  └─ Follow-up audit verification
└─ Governance
   ├─ Audit committee oversight
   ├─ Executive reporting (quarterly)
   ├─ Board presentation (annual)
   └─ Independence verification

Satisfies:
├─ COBIT: MEA03 (Monitor compliance)
├─ ISO 27001: 9.2 (Internal audit requirements)
├─ ISO 42001: 9 (Performance evaluation, if AI)
├─ Governance best practice
└─ Regulatory expectations
```

---

#### EATGF-MEA-PERF-01: Performance & Conformance Monitoring

**Strategic KPI Dashboard:**

| Framework | Metrics | Evidence |
|-----------|---------|----------|
| COBIT | Process performance, execution metrics | Dashboard/reports |
| ISO 27001 | Control effectiveness, compliance | Monitoring results |
| Business | DORA metrics, availability, security | Operational data |

**Evidence Dashboard:**

```
Governance KPI Monitor (Updated Monthly):

Strategic Level
├─ Control Implementation Rate: __95%
├─ Compliance Score: __90%
├─ Risk Trend: __Stable
└─ Board Approval: __Scheduled Board Meeting

Operational Level
├─ Patch Compliance: __95%
├─ Access Review: __On Schedule
├─ Incident Response: __<1 hour (avg)
└─ Change Success Rate: __98%

Reporting
├─ Monthly: Operational team
├─ Quarterly: Executive stakeholders
├─ Annual: Board of Directors
└─ Ad-hoc: Risk escalation

Satisfies:
├─ COBIT: MEA01 (Monitoring & measurement)
├─ ISO 27001: 9.1 (Monitoring & measurement req)
├─ Executive accountability
└─ Risk-aware leadership
```

---

#### EATGF-MEA-MAT-01: Governance Maturity Assessment

**EATGF Maturity Model (5 Levels):**

| Level | COBIT Equivalent | Organizational Readiness |
|-------|---|---|
| 1: Initial | Ad-hoc | Startup (basic controls) |
| 2: Developing | Repeatable | SaaS (documented processes) |
| 3: Defined | Defined | Enterprise (standardized) |
| 4: Managed | Managed | Data-driven optimization |
| 5: Optimized | Optimized | Predictive, continuous improvement |

**Assessment Methodology:**

```
Annual Maturity Assessment:
├─ Facilitated Workshop (2 days)
│  ├─ Cross-functional stakeholders
│  ├─ 5 COBIT Domain reviews
│  ├─ Process capability scoring
│  └─ Evidence validation
├─ Scoring (1-5 scale per domain)
│  ├─ 1 = Awareness level only
│  ├─ 2 = Process documented
│  ├─ 3 = Process standardized
│  ├─ 4 = Monitored & measured
│  └─ 5 = Optimized & automated
├─ Result
│  ├─ Maturity heatmap (5 domains)
│  ├─ Strengths & gaps analysis
│  ├─ 3-year improvement roadmap
│  └─ Executive presentation
└─ Governance
   ├─ Results approved by governance council
   ├─ Roadmap integrated into IT strategy
   └─ Annual progress tracking

Satisfies:
├─ COBIT: Capability assessment
├─ ISO 27001: Control effectiveness
├─ Strategic planning
└─ Investment prioritization
```

---

### 1.6 AI Governance Controls (Extension)

#### EATGF-AI-LC-01: AI System Lifecycle Governance

**ISO 42001 + NIST AI RMF Mapping:**

| Standard | Reference | Scope |
|----------|-----------|-------|
| ISO 42001 | Clause 8 | AI lifecycle end-to-end |
| NIST AI RMF | All categories | Governance → Measure → Manage |

**AI Lifecycle Stages:**

```
AI System Lifecycle:
├─ Stage 1: Intake & Planning
│  ├─ Business case approval
│  ├─ AI system registration
│  ├─ Risk classification
│  └─ Team assignment
├─ Stage 2: Design & Development
│  ├─ Expected fairness/accuracy targets
│  ├─ Data quality requirements
│  ├─ Model selection rationale
│  └─ Training & validation plan
├─ Stage 3: Validation & Testing
│  ├─ Fairness assessment (bias metrics)
│  ├─ Accuracy testing (holdout data)
│  ├─ Security testing (adversarial)
│  ├─ Explainability review (SHAP/LIME)
│  └─ Regulatory compliance check
├─ Stage 4: Deployment
│  ├─ Production release checklist
│  ├─ Monitoring setup
│  ├─ Incident procedures
│  └─ Stakeholder notification
├─ Stage 5: Monitoring & Management
│  ├─ Performance metrics (accuracy, fairness)
│  ├─ Model drift detection
│  ├─ Fairness drift detection
│  ├─ Incident response
│  └─ Scheduled retraining
└─ Stage 6: Retirement
   ├─ Deprecation timeline
   ├─ Migration plan
   ├─ Data archival
   └─ Impact assessment

Satisfies:
├─ ISO 42001: Clause 8 (AI system lifecycle)
├─ NIST AI RMF: MAP/MEASURE/MANAGE
├─ Trustworthy AI principles
└─ Governance accountability
```

---

#### EATGF-AI-RISK-01: AI Risk Assessment & Bias Management

**Bias Testing Framework:**

```
AI Fairness Requirements:
├─ Fairness Metrics (select applicable)
│  ├─ Demographic parity (equal positive rate)
│  ├─ Equalized odds (equal TPR & FPR across groups)
│  ├─ Calibration (equal prediction accuracy)
│  └─ Individual fairness (similar cases treated similarly)
├─ Test Methodology
│  ├─ Stratified holdout testing (by protected attributes)
│  ├─ Statistical testing (p-value < 0.05)
│  ├─ Problem-specific thresholds
│  └─ Domain expert review
├─ Acceptable Thresholds
│  ├─ Disparity difference: <5% (typical)
│  ├─ Accuracy variance: <2% across groups
│  ├─ False positive rate variance: <1%
│  └─ Custom thresholds per application
└─ Continuous Monitoring
   ├─ Monthly fairness metrics
   ├─ Drift detection (>5% change threshold)
   ├─ Incident investigation
   └─ Remediation tracking

Satisfies:
├─ ISO 42001: Clause 6 (Risk management)
├─ ISO 42001: Clause 8.2 (Processing activities)
├─ NIST AI RMF: MEASURE-3 (Fairness metrics)
└─ Responsible AI principles
```

---

### 1.7 API Governance Controls (Extension)

#### EATGF-API-SEC-01: API Authentication & Authorization

**OWASP API Security Mapping:**

| OWASP API | Title | Mapping |
|-----------|-------|---------|
| API1 | Broken Object Level Auth | EATGF-API-SEC-01 |
| API2 | Broken Authentication | EATGF-API-SEC-01 |
| API3 | Broken Object Property Auth | EATGF-API-SEC-01 |

**Control Implementation:**

```
API Security Architecture:
├─ API Gateway
│  ├─ Central authentication point
│  ├─ OAuth 2.0 or mTLS enforcement
│  ├─ Token validation
│  ├─ Rate limiting per client
│  └─ Threat detection
├─ Authentication
│  ├─ OAuth 2.0 (standard implementation)
│  ├─ Mutual TLS for service-to-service
│  ├─ API keys (for non-sensitive operations)
│  └─ Token expiration (max 1 hour)
├─ Authorization (RBAC)
│  ├─ Scope-based permissions
│  ├─ Resource-level access control
│  ├─ API version-specific permissions
│  └─ Dynamic policy enforcement
├─ Logging & Monitoring
│  ├─ All API calls logged (call, user, timestamp)
│  ├─ Audit trail (12-month minimum)
│  ├─ Anomaly detection
│  └─ Rate limit violations tracked
└─ Evidence
   ├─ API gateway configuration
   ├─ OAuth server setup documentation
   ├─ Rate limiting rules
   ├─ Audit log samples
   └─ Test results (authentication failures)

Satisfies:
├─ OWASP: API2 (Broken authentication)
├─ OWASP: API3 (Object-level authorization)
├─ COBIT: DSS05 (Access management)
├─ ISO 27001: A.5.18 (Access management)
└─ API security best practice
```

---

#### EATGF-API-LC-01: API Lifecycle Management

**OWASP API9 Mapping: Improper Inventory Management**

```
API Lifecycle:
├─ Design Phase
│  ├─ OpenAPI 3.0 specification (contract-first)
│  ├─ Versioning strategy (semantic versioning)
│  ├─ Breaking change policy
│  └─ Deprecation timeline
├─ Development
│  ├─ Standards compliance checking
│  ├─ Security review
│  ├─ Rate limiting configuration
│  └─ Documentation completeness
├─ Testing
│  ├─ Functional testing
│  ├─ Security testing (OWASP Top 10)
│  ├─ Performance testing
│  └─ Compatibility testing (backward)
├─ Release
│  ├─ Version tagging (Git)
│  ├─ Release notes (breaking changes highlighted)
│  ├─ Deployment approval
│  └─ Monitoring setup
├─ Maintenance
│  ├─ Performance monitoring
│  ├─ Error rate tracking
│  ├─ Security patch application
│  └─ Usage analytics
├─ Deprecation
│  ├─ Minimum 6-month notice
│  ├─ Migration guide provision
│  ├─ Client notification (90, 60, 30 days)
│  └─ Sunset date enforcement
└─ Evidence
   ├─ API Catalog (central registry)
   ├─ OpenAPI specs (all versions)
   ├─ Release notes (6+ months)
   ├─ Deprecation timeline (tracking)
   └─ Audit log of API changes

Satisfies:
├─ OWASP: API9 (Inventory management)
├─ COBIT: BAI03 (Service configuration)
├─ ISO 27001: A.8.19 (Change management)
└─ API ecosystem governance
```

---

## 📊 SECTION 2: CONTROL-TO-EVIDENCE MAPPING MATRIX

### Quick Reference: What Evidence Proves What?

| Evidence Type | COBIT | ISO 27001 | ISO 42001 | NIST AI RMF | OWASP |
|---|---|---|---|---|---|
| Policy document | EDM, APO | 5-7 | 5 | GOVERN | N/A |
| Risk register | APO12 | 6.1.2 | 6 | MAP | N/A |
| Audit report | MEA3 | 9.2 | 9 | MEASURE | N/A |
| Test results | BAI3, DSS6 | A.8.9 | 8.2 | MEASURE | All |
| Access logs | DSS5 | A.5.15-18 | N/A | N/A | N/A |
| Incident ticket | DSS2 | A.5.24-27 | 8.2 | GOVERN | N/A |
| Dashboard | MEA1 | 9.1 | 9 | MEASURE | N/A |
| Configuration | BAI10 | A.8.9 | 8.1 | N/A | N/A |
| Training record | APO13 | A.6.3 | 7 | GOVERN | N/A |
| Deployment log | BAI6 | A.8.19 | N/A | N/A | N/A |

---

## 📊 SECTION 3: APPLICABILITY MATRIX BY ORGANIZATION SIZE {#section-3-applicability-matrix-by-organization-size}

### Which Controls Are Mandatory by Edition?

| EATGF Control | Startup (1-10) | SaaS (10-50) | Enterprise (50+) |
|---|---|---|---|
| **EDM Controls** | | | |
| EATGF-EDM-RISK-01 | ❌ | ✅ | ✅ |
| EATGF-EDM-BEN-01 | ✅ | ✅ | ✅ |
| EATGF-EDM-GOV-01 | ❌ | ✅ | ✅ |
| **APO Controls** | | | |
| EATGF-APO-ARCH-01 | ❌ | ✅ | ✅ |
| EATGF-APO-RISK-01 | ✅ | ✅ | ✅ |
| EATGF-APO-SEC-01 | ❌ | ✅ | ✅ |
| EATGF-APO-AI-01 | ❌ | ⚠️* | ✅* |
| **BAI Controls** | | | |
| EATGF-BAI-CHG-01 | ✅ | ✅ | ✅ |
| EATGF-BAI-CONF-01 | ✅ | ✅ | ✅ |
| EATGF-BAI-TEST-01 | ✅ | ✅ | ✅ |
| **DSS Controls** | | | |
| EATGF-DSS-SEC-01 | ✅ | ✅ | ✅ |
| EATGF-DSS-ENC-01 | ✅ | ✅ | ✅ |
| EATGF-DSS-VULN-01 | ✅ | ✅ | ✅ |
| EATGF-DSS-INC-01 | ✅ | ✅ | ✅ |
| **MEA Controls** | | | |
| EATGF-MEA-AUD-01 | ❌ | ✅ | ✅ |
| EATGF-MEA-PERF-01 | ✅ | ✅ | ✅ |
| EATGF-MEA-MAT-01 | ✅ | ✅ | ✅ |
| **AI Controls** | | | |
| EATGF-AI-LC-01 | ❌ | ⚠️* | ✅* |
| EATGF-AI-RISK-01 | ❌ | ⚠️* | ✅* |
| **API Controls** | | | |
| EATGF-API-SEC-01 | ✅ | ✅ | ✅ |
| EATGF-API-LC-01 | ✅ | ✅ | ✅ |

**Legend:**
- ✅ = Mandatory
- ⚠️* = Conditional (if AI systems used)
- ❌ = Not applicable for this edition

---

## 🎯 SECTION 4: AUDITOR READINESS CHECKLIST

### Quick Audit Preparation

**Before ISO 27001 Certification Audit:**
```
Preparation Checklist (8 weeks before external audit):

Week 1-2: Gap Assessment
  ☐ Run internal audit on all mandatory controls
  ☐ Document any gaps
  ☐ Create remediation plan for gaps

Week 3-4: Evidence Gathering
  ☐ Collect all control evidence per MCM evidence checklist
  ☐ Organize evidence by control ID
  ☐ Verify evidence completeness per control

Week 5: SoA Finalization
  ☐ Complete SoA (all 76 controls included/excluded)
  ☐ Verify all inclusions have evidence
  ☐ Document all exclusion justifications

Week 6: Management Review
  ☐ Management review meeting (formal)
  ☐ Document meeting minutes
  ☐ Close all action items

Week 7: Final Preparation
  ☐ Conduct mock audit (if internal capability)
  ☐ Address any additional findings
  ☐ Prepare for auditor interviews

Week 8: Audit Readiness
  ☐ Brief control owners on audit focus areas
  ☐ Prepare evidence documentation
  ☐ Schedule auditor interviews
```

**During ISO 27001 Audit:**
```
Audit Support:
  ☐ Provide evidence per control selection
  ☐ Support auditor interviews
  ☐ Clarify control implementation approach
  ☐ Track any non-conformances
```

**Post-Audit:**
```
Certification:
  ☐ Address major non-conformances (before certificate issue)
  ☐ Plan for minor non-conformance closure
  ☐ Receive ISO 27001 certificate
  ☐ Begin maintenance audit cycles (annual)
```

---

## 📝 SECTION 5: REFERENCE & NAVIGATION

### How to Use This Document

**For Implementation Teams:**
1. Identify your organization edition (Startup/SaaS/Enterprise)
2. Go to [Section 3](#section-3-applicability-matrix-by-organization-size)
3. Find mandatory controls for your edition
4. Use MCM to implement each control
5. Collect evidence per control requirements

**For Auditors:**
1. Review control applicability per SoA
2. Reference mapping to ISO/COBIT/NIST standards
3. Verify evidence against MCM evidence checklists
4. Use auditor readiness checklist

**For Compliance Officers:**
1. Maintain SoA (Section 4, Layer 4)
2. Track control implementation status quarterly
3. Report compliance dashboard (MEA-PERF-01)
4. Plan audit schedule per MEA-AUD-01

**For Risk Managers:**
1. Reference control risk mapping
2. Use risk register to map risks to controls
3. Track remediation plans per control
4. Report to ESC quarterly

---

## 📚 APPENDICES

### Appendix A: COBIT 2019 Reference Link
[See https://www.isaca.org/resources/cobit for complete framework]

### Appendix B: ISO 27001:2022 Annex A - Complete Control List
[See https://www.iso.org/standard/75652.html for complete standard]

### Appendix C: ISO 42001:2024 Clause Structure
[See https://www.iso.org/standard/81399.html for complete standard]

### Appendix D: NIST AI RMF Categories
- GOVERN: Defines AI risks and values
- MAP: Maps risks to controls
- MEASURE: Measures control effectiveness
- MANAGE: Manages identified risks

### Appendix E: OWASP API Top 10 (2023)
- API1: Broken Object Level Authorization
- API2: Broken Authentication
- API3: Broken Object Property Level Authorization
...and 7 more

---

## 📅 MAINTENANCE

**Document Owner:** Enterprise Architecture & Governance Office  
**Review Frequency:** Semi-annual (Feb & Aug)  
**Version History:**
- v1.0 (Feb 2024) - Initial framework
- v2.0 (Feb 2026) - MCM-aligned with 21 controls

**Next Review Date:** August 13, 2026

---

**Framework:** Enterprise AI-Aligned Technical Governance Framework (EATGF)  
**Document Type:** Comprehensive Standards Mapping  
**Status:** ✅ **COMPLETE AND AUDITOR-READY**
