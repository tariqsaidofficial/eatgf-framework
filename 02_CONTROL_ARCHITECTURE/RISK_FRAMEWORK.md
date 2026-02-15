# RISK_FRAMEWORK

| Field          | Value                                                  |
| -------------- | ------------------------------------------------------ |
| Document Type  | Framework                                              |
| Version        | 2.0                                                    |
| Classification | Controlled                                             |
| Effective Date | 2026-02-14                                             |
| Authority      | Enterprise Architecture and Governance Office          |
| EATGF Layer    | 02_CONTROL_ARCHITECTURE                                |
| MCM Reference  | EATGF-EDM-RISK-01, EATGF-APO-RISK-01, EATGF-AI-RISK-01 |
| Standards      | ISO 31000:2018, ISO 27005:2022, COBIT 2019             |

---

## Purpose

This framework establishes enterprise methodology for identifying, assessing, and managing technology risks across all EATGF-governed domains. It defines risk assessment process, risk appetite by category, risk reporting cadence, escalation procedures, and control-risk mappings. All organizational technology risks must be assessed using this framework; deviations require Chief Risk Officer approval.

## Architectural Position

This framework operates within **02_CONTROL_ARCHITECTURE** as the risk assessment and management methodology.

- **Upstream dependency:** Master Control Matrix defines 35 controls for risk mitigation; Governance Charter (Layer 04) establishes risk governance structure and escalation authority
- **Downstream usage:** Risk register maintained per this framework; utilized by internal audit (Layer 06) for risk-based audit planning; informs maturity assessment (Layer 03) risk maturity scoring
- **Cross-layer reference:** Risk appetite statement in Governance Charter implemented through this framework; AI risk assessment procedures (AI-RISK-01) documented here; API risk assessment integrated

## Governance Principles

1. **Risk Ownership** – Every identified risk assigned to designated owner responsible for mitigation execution and status reporting
2. **Risk Transparency** – All material risks (medium and above) reported in enterprise risk register with board visibility for critical risks
3. **Risk-Based Prioritization** – Resources allocated based on risk impact scoring using probability x impact methodology
4. **Continuous Monitoring** – Risk status reviewed monthly minimum; critical risks reviewed weekly with executive oversight
5. **Escalation Discipline** – Critical risks escalated within 1 hour; defined escalation chain enforced without exception

## Technical Implementation

### Risk Assessment Process

**Four-Step Risk Assessment Methodology:**

**Step 1: Risk Identification**

Annual Risk Assessment (comprehensive):

- Technology risks (infrastructure, application, platform)
- Compliance and regulatory risks (GDPR, CCPA, industry-specific)
- Operational risks (service delivery, availability, performance)
- Strategic risks (technology strategy alignment, competitive positioning)
- Financial risks (cost overruns, technology debt)
- AI-specific risks (model bias, data drift, explainability failures)
- API-specific risks (unauthorized access, rate limit bypass, data leakage)
- Cloud risks (multi-tenancy, data residency, vendor lock-in)

Quarterly Risk Reviews:

- Update risk register with newly identified risks
- Reassess existing risk scores based on control effectiveness
- Identify emerging risks from threat intelligence

**Step 2: Risk Analysis**

For each identified risk, assess:

| Assessment Category       | Scoring Scale                                                                    |
| ------------------------- | -------------------------------------------------------------------------------- |
| **Probability**           | 1 (Rare - <5% annually) to 5 (Very Likely - >80% annually)                       |
| **Impact**                | 1 (Minimal - <$10K impact) to 5 (Critical - >$1M impact or regulatory violation) |
| **Risk Score**            | Probability x Impact (range 1-25)                                                |
| **Current Controls**      | EATGF controls mapped to risk mitigation                                         |
| **Control Effectiveness** | Assessment of current control adequacy (0-100%)                                  |
| **Residual Risk**         | Risk score after current controls applied                                        |
| **Gap Analysis**          | Required additional controls identified                                          |

**Step 3: Risk Prioritization**

Risk Heat Map (Probability vs Impact):

```
Impact
  5 |  5   10   15   20   25
  4 |  4    8   12   16   20
  3 |  3    6    9   12   15
  2 |  2    4    6    8   10
  1 |  1    2    3    4    5
    +-------------------------
      1    2    3    4    5
           Probability
```

**Risk Level Classification:**

- **Red (20-25):** Critical – CEO escalation required within 1 hour
- **Orange (15-19):** High – Board visibility required; escalation within 4 hours
- **Yellow (10-14):** Medium – Governance Council monitoring; weekly status
- **Green (5-9):** Low – Business as usual; monthly review
- **Blue (1-4):** Minimal – Track only; quarterly review

**Step 4: Mitigation Planning**

For each high and critical risk, develop mitigation plan:

```
Risk Mitigation Plan Template

Risk ID: [R-xxx]
Risk Description: [Specific risk scenario]
Risk Owner: [Name/Department/Title]
Current Score: [Probability x Impact]
Target Score: [After mitigation]
Risk Appetite: [Within/Exceeds organizational tolerance]

Mitigation Actions:
1. Action: [Specific mitigation activity description]
   Owner: [Responsible party name and title]
   Timeline: [Target completion date with milestones]
   Cost: [Estimated budget for mitigation]
   Status: [Not Started / In Progress / Complete]
   Expected Risk Reduction: [Impact on risk score]

2. [Additional mitigation actions]

Current EATGF Controls:
- [EATGF-XXX-XXX-XX] – [Control effectiveness %]
- [Additional controls]

Control Gaps:
- [Gap description and required control]

Monitoring KPIs:
- KPI: [Specific metric demonstrating mitigation progress]
- Frequency: [Measurement interval – daily/weekly/monthly]
- Alert Threshold: [Value triggering escalation]
- Escalation Route: [Conditions and escalation path]

Review Schedule: [Weekly/Monthly/Quarterly]
Next Review: [Scheduled date]
```

### Risk Register Template Examples

**Example 1: Data Breach Risk**

```
Risk ID: R-001
Category: Security
Probability: 3 (Possible – 20-40% annually)
Impact: 5 (Critical – GDPR violation, reputational damage, >$1M fines)
Risk Score: 15 (High – Orange)

Description:
Unauthorized access to customer personally identifiable information due to:
- Weak user credential management
- Unpatched systems with known vulnerabilities
- Insider threat from privileged user access
- Third-party vendor security gaps

Mapped EATGF Controls:
- EATGF-DSS-SEC-01 (Identity and Access Management) – 85% effective
- EATGF-DSS-ENC-01 (Data Encryption) – 90% effective
- EATGF-DSS-VULN-01 (Vulnerability Management) – 75% effective
- EATGF-DSS-INC-01 (Incident Response) – 80% effective

Control Gaps Identified:
- Endpoint Detection and Response (EDR) not deployed to 40% of endpoints
- Annual security awareness training compliance at 70% (target: 100%)
- Third-party security assessments performed only annually (target: quarterly for critical vendors)

Mitigation Plan:
1. Deploy EDR to 100% of endpoints by Q2 2026 (Owner: CISO, Budget: $2M)
2. Mandate security training completion by Q1 2026 with enforcement (Owner: HR, Budget: $50K)
3. Implement quarterly security assessments for critical vendors (Owner: Vendor Management, Budget: $100K)
4. Implement privileged access management (PAM) solution (Owner: Security, Budget: $500K, Timeline: Q3 2026)

Monitoring KPIs:
- Percentage of systems with EDR deployed (Target: 100% by Q2 2026)
- Security training completion rate (Target: 100% by Q1 2026)
- Critical vulnerabilities remediated within 24 hours end-to-end (Target: 95%, per VULNERABILITY_REMEDIATION_TERMINOLOGY.md)
- Privileged account usage logged and monitored (Target: 100%)

Escalation: If actual breach detected, escalate to CEO immediately; notify Board within 4 hours
```

**Example 2: AI System Bias Risk**

```
Risk ID: R-012
Category: AI/Governance
Probability: 4 (Likely – 60-80% without controls)
Impact: 4 (High – regulatory exposure, discrimination lawsuit, reputational harm)
Risk Score: 16 (High – Orange)

Description:
AI models exhibit statistical bias in hiring recommendations affecting protected characteristics (race, gender, age, disability status), leading to:
- Discriminatory hiring outcomes
- EEOC or regulatory investigation
- Legal liability and settlements
- Organizational reputation damage

Mapped EATGF Controls:
- EATGF-AI-LC-01 (AI Lifecycle Governance) – 70% effective
- EATGF-AI-RISK-01 (AI Risk and Bias Management) – 65% effective
- EATGF-MEA-PERF-01 (Performance Monitoring) – 60% effective

Control Gaps Identified:
- No real-time fairness monitoring in production
- No automated model retraining trigger based on drift detection
- Limited bias detection capabilities; only tested during initial deployment
- No external fairness audit schedule

Mitigation Plan:
1. Implement real-time fairness monitoring dashboard (Owner: Data Science, Q1 2026, Budget: $150K)
2. Configure automated retraining triggers when disparate impact detected (Owner: MLOps, Q2 2026, Budget: $75K)
3. Establish quarterly external fairness audit with third-party AI ethics consultancy (Owner: Compliance, Budget: $200K annually)
4. Implement model explainability tooling (SHAP/LIME) for all high-risk AI decisions (Owner: Data Science, Q2 2026, Budget: $100K)

Monitoring KPIs:
- Disparate Impact Ratio by protected attribute (Target: maintain >0.80 per EEOC guidelines)
- Model drift detection (Target: alert if >10% distribution shift)
- Fairness metric tracking (Target: demographic parity within 5%)
- External audit findings (Target: zero critical findings)

Escalation: If Disparate Impact Ratio falls below 0.80, pause model deployment immediately and escalate to Chief AI Officer and General Counsel
```

### Risk Appetite by Domain

**Strategic Risk Appetite: Moderate**

- Accept up to 20% probability of technology strategy disruption
- Acceptable mitigation investment: up to $5M annually
- Strategic technology bets evaluated with risk/reward analysis

**Technology Risk Appetite: Low**

- Accept up to 5% probability of critical system failure
- Service Level Agreement targets: 99.95% availability minimum
- Planned downtime windows limited to 4 hours/quarter maximum

**Compliance Risk Appetite: Minimal**

- Accept zero tolerance for regulatory violations
- All compliance risks require immediate mitigation
- Compliance gaps identified through audit escalate to Board

**AI Risk Appetite: Low-Moderate**

- Accept fairness gaps if demographic disparity below 10% (Disparate Impact >0.90)
- Bias mitigation required if statistical disparity detected
- Explainability required for all high-stakes AI decisions

**API Security Risk Appetite: Low**

- Accept minimal risk of API security vulnerabilities
- OWASP Top 10 compliance mandatory before production deployment
- API security testing required quarterly minimum

### Risk Reporting Cadence

**Monthly Risk Dashboard (Executive Leadership):**

- Top 10 risks by score with current status
- Status changes since previous reporting period
- Mitigation progress percentage completion
- New risks identified during period
- Control effectiveness trends

**Quarterly Risk Review (Governance Council):**

- Detailed assessment of top 5 risks
- Mitigation effectiveness evaluation
- Risk trend analysis (improving/deteriorating)
- Updated enterprise risk register
- Risk appetite alignment verification
- Emerging risk identification

**Annual Risk Assessment (Board and Executive Team):**

- Comprehensive risk landscape review across all domains
- Risk strategy alignment with business strategy
- Risk tolerance recalibration based on organizational changes
- Next year's risk management priorities and budget
- Risk maturity assessment per EATGF-MEA-MAT-01

### Risk Escalation Procedures

**Escalation Triggers:**

| Risk Level          | Escalation Trigger                                 | Alert Recipient             | Response Timeline          |
| ------------------- | -------------------------------------------------- | --------------------------- | -------------------------- |
| **Red (Critical)**  | Probability or Impact increases by 1+ level        | CISO, CRO, CFO, CEO         | Immediate (1 hour maximum) |
| **Orange (High)**   | Risk could escalate to critical without mitigation | Chief Risk Officer          | 4 hours                    |
| **Yellow (Medium)** | Mitigation plan not on track; timeline slipping    | Risk Owner, Department Head | 1 business day             |
| **Green (Low)**     | Standard monitoring; no immediate action           | Process Owner               | 1 week                     |
| **Blue (Minimal)**  | Routine tracking                                   | Process Owner               | Monthly review             |

**Escalation Chain:**

```
Level 1: Risk Owner identifies issue and attempts mitigation
         ↓ (if unresolved within defined timeline)
Level 2: Department Head reviews and allocates additional resources
         ↓ (if unresolved or requires cross-department coordination)
Level 3: Governance Council approves mitigation plan and budget
         ↓ (if strategic impact or requires significant investment)
Level 4: CFO/CEO executive decision and resource allocation
         ↓ (if extreme impact, regulatory, or reputational risk)
Level 5: Board of Directors notification and strategic direction
```

### Control-Risk Mapping

**Security Controls Mapping to Security Risk:**

```
Risk: Data Breach (Impact: Critical, Score: 15-20)

Applied Controls and Risk Reduction:
├─ EATGF-DSS-SEC-01 (IAM) → Reduces probability by 30% (access control)
├─ EATGF-DSS-ENC-01 (Encryption) → Reduces impact by 40% (data protection)
├─ EATGF-DSS-VULN-01 (Vulnerability Mgmt) → Reduces probability by 20% (patch management)
├─ EATGF-DSS-INC-01 (Incident Response) → Reduces impact by 25% (rapid response)
└─ Residual Risk: 10% (within acceptable risk appetite)

Risk Mitigation Assessment: Acceptable with continuous monitoring
```

**AI Controls Mapping to AI Bias Risk:**

```
Risk: AI System Bias (Impact: High, Score: 12-16)

Applied Controls and Risk Reduction:
├─ EATGF-AI-LC-01 (Lifecycle Governance) → Reduces probability by 25% (design standards)
├─ EATGF-AI-RISK-01 (Risk and Bias Mgmt) → Reduces probability by 35% (fairness testing)
├─ EATGF-MEA-PERF-01 (Performance Monitoring) → Reduces probability by 15% (continuous monitoring)
├─ Third-party fairness audit → Reduces probability by 10% (independent validation)
└─ Residual Risk: 15% (requires additional controls; above risk appetite)

Risk Mitigation Assessment: Additional controls required; implement real-time monitoring
```

**API Controls Mapping to API Security Risk:**

```
Risk: API Security Breach (Impact: High, Score: 15-18)

Applied Controls and Risk Reduction:
├─ EATGF-API-SEC-01 (API Security) → Reduces probability by 40% (authentication, authorization, rate limiting)
├─ EATGF-API-LC-01 (API Lifecycle) → Reduces probability by 20% (secure design, testing)
├─ EATGF-DSS-SEC-01 (IAM) → Reduces probability by 15% (identity management)
├─ EATGF-DEV-SCAN-01 (Code Scanning) → Reduces probability by 10% (vulnerability detection)
└─ Residual Risk: 15% (monitored via EATGF-MEA-PERF-01)

Risk Mitigation Assessment: Acceptable with quarterly OWASP Top 10 reassessment
```

### Risk Acceptance Template

When controls cannot eliminate risk to acceptable appetite level:

```
Risk Acceptance Form

Risk ID: [R-xxx]
Risk Description: [Specific risk scenario]
Risk Owner: [Name and Title]
Risk Level (Current): [Before controls] → [After all feasible controls]
Residual Risk: [Risk score after controls]

Mitigation Options Evaluated:
1. Option: [Control description]
   Cost: $[Amount]
   Risk Reduction: [Probability/Impact reduction]
   Implementation Timeline: [Duration]
   Reason Not Selected: [Business justification]

2. [Additional options evaluated]

Decision:
[ ] Accept residual risk – No additional controls justified by cost/benefit
[ ] Implement partial controls – Cost/benefit optimization achieved
[ ] Transfer risk – Insurance or contractual transfer
[ ] Avoid risk – Discontinue activity creating risk

Residual Risk Level: [Final risk score]
Within Risk Appetite: [Yes / No]
Business Justification: [Explanation if exceeds appetite]

Approval Authority:
- Risk Owner: [Signature] [Date]
- Department Head: [Signature] [Date]
- Chief Risk Officer: [Signature] [Date] (required for Orange/Red risks)
- CFO/CEO: [Signature] [Date] (required for Red risks)

Review Schedule: [Quarterly / Annually]
Next Review Date: [Scheduled date]
Expiration: [Risk acceptance expires and requires renewal]
```

### Risk Monitoring Dashboard

**Standard Risk KPIs:**

| KPI                             | Current Value | Target | Status             | Trend        |
| ------------------------------- | ------------- | ------ | ------------------ | ------------ |
| Red risks (Critical)            | 2             | 0      | Off track          | ↑ Increasing |
| Orange risks (High)             | 8             | <5     | Below target       | → Stable     |
| Risk mitigation completion rate | 85%           | 95%    | Improvement needed | ↑ Improving  |
| Controls operating effectively  | 92%           | 95%    | Near target        | ↑ Improving  |
| Unplanned outages (annual)      | 3             | <1     | Off track          | → Stable     |
| Security incidents (annual)     | 2             | <1     | Near target        | ↓ Decreasing |
| Compliance violations           | 0             | 0      | On track           | → Stable     |
| Overdue risk reviews            | 5%            | 0%     | Improvement needed | ↓ Decreasing |

## Control Mapping

### ISO 31000:2018 Risk Management

Framework implements ISO 31000 risk management principles:

- Integrated risk management across organization
- Structured and comprehensive risk assessment process
- Customized risk framework for technology governance
- Inclusive stakeholder engagement through risk ownership
- Dynamic risk monitoring and continual improvement

### ISO 27005:2022 Information Security Risk Management

Framework aligns with ISO 27005 for security risk:

- Information security risk assessment methodology
- Risk treatment options (mitigate, accept, transfer, avoid)
- Residual risk acceptance procedures
- Continuous monitoring and review

### COBIT 2019 Risk Management

Framework supports COBIT risk governance:

- **EDM03** – Risk optimization through control effectiveness
- **APO12** – Operational risk management procedures
- Risk appetite alignment with business objectives

## Developer Checklist

Before implementing risk framework:

- [ ] Risk categories defined for organization (technology, security, AI, API, compliance, operational, strategic, financial)
- [ ] Risk scoring criteria established (probability 1-5, impact 1-5)
- [ ] Risk appetite defined by category and approved by Board
- [ ] Risk register template created and risk tracking system operational
- [ ] Risk owners assigned for all identified risks
- [ ] Escalation procedures documented and communicated
- [ ] EATGF controls mapped to organizational risks
- [ ] Monthly risk dashboard configured for executive reporting
- [ ] Quarterly risk review scheduled with Governance Council
- [ ] Annual risk assessment scheduled with Board presentation
- [ ] Risk acceptance form template created and approval workflow established
- [ ] Integration with audit procedures (Layer 06) for risk-based audit planning
- [ ] Integration with maturity assessment (Layer 03) for risk maturity scoring
- [ ] Risk monitoring KPIs defined and baseline measurements established

## Governance Implications

### Risk Ownership and Accountability

- Every risk requires designated owner with mitigation responsibility
- Risk owners accountable to Governance Council for timely mitigation
- Critical risk failures escalate to executive compensation review
- Persistent risk ownership failures result in accountability review

### Risk Escalation Authority

- Level 1-2 escalations managed by operational teams
- Level 3 escalations require Governance Council approval and resource allocation
- Level 4 escalations require CEO/CFO decision authority
- Level 5 escalations (Board level) triggered for regulatory, reputational, or >$5M impact risks

### Risk Acceptance Authority

- Risk acceptance for Red-level risks requires CFO or CEO sign-off
- Risk acceptance for Orange-level risks requires Chief Risk Officer sign-off
- All risk acceptances expire and require annual renewal
- Risk acceptances exceeding organizational risk appetite require Board notification

### Risk-Based Control Prioritization

- High and critical risks drive control implementation priority
- Control investments allocated based on risk reduction value
- Annual budget process includes risk mitigation funding requirements
- Maturity assessment (EATGF-MEA-MAT-01) incorporates risk management effectiveness

## Official References

- **ISO 31000:2018** – Risk Management Guidelines (ISO, 2018)
- **ISO/IEC 27005:2022** – Information Security Risk Management (ISO, 2022)
- **COBIT 2019** – Risk Optimization and Governance (ISACA, 2019)
- **NIST SP 800-30:Revision 1** – Guide for Conducting Risk Assessments (NIST, 2012)
- **COSO Enterprise Risk Management Framework** – Integrating with Strategy and Performance (COSO, 2017)

### Step 1: Risk Identification

**Annual Risk Assessment:** Identify all material risks across the following categories:

- Technology risks
- Compliance and regulatory risks
- Operational risks
- Strategic risks
- Financial risks
- AI-specific risks (bias, drift, explainability)

**Quarterly Reviews:** Update risk register with new and emerging risks.

### Step 2: Risk Analysis

**For each identified risk:**

| Category             | Assessment                             |
| -------------------- | -------------------------------------- |
| **Probability**      | 1 (Rare) to 5 (Very Likely)            |
| **Impact**           | 1 (Minimal) to 5 (Critical)            |
| **Risk Score**       | Probability x Impact (1-25)            |
| **Current Controls** | Existing EATGF controls mapped to risk |
| **Gap**              | Required control gaps identified       |

### Step 3: Risk Prioritization

**Risk Heat Map**

```
Impact
  5 | == 5  == 10 == 15 == 20 == 25
  4 | == 4  == 8  == 12 == 16 == 20
  3 | == 3  == 6  == 9  == 12 == 15
  2 | == 2  == 4  == 6  == 8  == 10
  1 | == 1  == 2  == 3  == 4  == 5
    +----------------------------------
      1    2    3    4    5
              Probability
```

**Risk Levels:**

- **Red (20-25):** Critical — CEO escalation required
- **Orange (15-19):** High — Board visibility required
- **Yellow (10-14):** Medium — Management monitoring
- **Green (5-9):** Low — Business as usual
- **Blue (1-4):** Minimal — Track only

### Step 4: Mitigation Planning

**For each high/critical risk:**

```
Risk: [Description]
Owner: [Name/Department]
Score: [Current] -> [Target]

Mitigation Actions:
1. Action: [Description of mitigation activity]
   Owner: [Responsible party]
   Timeline: [Target completion date]
   Status: [Not started / In progress / Complete]

2. [Subsequent actions]

Monitoring:
- KPI: [Metric that demonstrates progress]
- Frequency: [Measurement interval]
- Escalation: [Conditions triggering escalation]
```

---

## 3. Risk Register Template

### Example: Data Breach Risk

```
Risk ID: R-001
Category: Security
Probability: 3 (Possible)
Impact: 5 (Critical — GDPR violation)
Risk Score: 15 (High)

Description:
Unauthorized access to customer data due to:
- Weak credentials
- Unpatched systems
- Insider threat

Mapped EATGF Controls:
- EATGF-DSS-SEC-01 (IAM)
- EATGF-DSS-ENC-01 (Encryption)
- EATGF-DSS-VULN-01 (Vulnerability Management)
- EATGF-DSS-INC-01 (Incident Response)

Gaps:
- EDR (Endpoint Detection and Response) not deployed
- Annual security training compliance at 70%

Mitigation Plan:
1. Deploy EDR by Q2 2026 (Owner: CISO, $2M budget)
2. Mandate security training by Q1 2026 (Owner: HR)
3. Quarterly penetration testing (Owner: Security)

Monitoring:
- KPI: Percentage of systems with EDR deployed
- Target: 100% by Q2
- Escalation: If breach detected, escalate to CEO
```

### Example: AI System Bias Risk

```
Risk ID: R-012
Category: AI/Governance
Probability: 4 (Likely)
Impact: 4 (High — regulatory exposure)
Risk Score: 16 (High)

Description:
AI models exhibit bias in hiring recommendations
affecting protected attributes.

Mapped EATGF Controls:
- EATGF-AI-LC-01 (AI Lifecycle Governance)
- EATGF-AI-RISK-01 (AI Risk and Bias Management)

Gaps:
- No real-time fairness monitoring
- No continuous retraining trigger
- Limited bias detection in production

Mitigation Plan:
1. Implement fairness monitoring dashboard (Owner: Data, Q1)
2. Set automated retraining triggers (Owner: MLOps, Q2)
3. Quarterly external fairness audit (Owner: Compliance, $5K)

Monitoring:
- KPI: Disparate Impact Ratio by protected attribute
- Target: Maintain above 0.80
- Escalation: If below 0.80, pause model immediately
```

---

## 4. Risk Appetite by Domain

### Strategic Risk Appetite: Moderate

- Accept up to 20% probability of strategy disruption
- Acceptable mitigation cost: up to $5M

### Technology Risk Appetite: Low

- Accept up to 5% probability of system failure
- SLAs: 99.95% availability target

### Compliance Risk Appetite: Minimal

- Accept zero regulatory violations
- All compliance risks must be addressed immediately

### AI Risk Appetite: Low-Moderate

- Accept fairness gaps if disparity is below 10%
- Bias mitigation is required if disparate impact is detected

---

## 5. Risk Reporting Cadence

### Monthly Risk Dashboard

**For Executive Leadership:**

- Top 10 risks (current status)
- Status changes since previous reporting period
- Mitigation progress
- New risks identified

### Quarterly Risk Review

**For Governance Council:**

- Detailed review of top 5 risks
- Mitigation effectiveness assessment
- Risk trend analysis
- Updated risk register

### Annual Risk Assessment

**For Board and Executive Team:**

- Comprehensive risk landscape review
- Risk strategy alignment verification
- Risk tolerance recalibration (if warranted)
- Next year's risk management priorities

---

## 6. Risk Escalation Procedures

### Escalation Triggers

| Risk Level | Escalation Trigger                          | Owner         | Timeline           |
| ---------- | ------------------------------------------- | ------------- | ------------------ |
| **Red**    | Probability or Impact increases by 1+ level | CISO/CFO      | Immediate (1 hour) |
| **Orange** | Without mitigation, could become critical   | CRO           | 1 business day     |
| **Yellow** | Mitigation not on track                     | Risk Owner    | Weekly             |
| **Green**  | Standard monitoring                         | Process Owner | Monthly            |

### Escalation Chain

```
Level 1: Risk Owner identifies issue
  |
Level 2: Department Head reviews
  |
Level 3: Governance Council approves plan
  |
Level 4: CFO/CEO executive decision
  |
Level 5: Board notification (if extreme impact)
```

---

## 7. Control-Risk Mapping

### Security Controls — Security Risk Reduction

```
Risk: Data Breach (Impact: Critical)
+-- EATGF-DSS-SEC-01 (IAM) -> Reduces risk by 30%
+-- EATGF-DSS-ENC-01 (Encryption) -> Reduces risk by 40%
+-- EATGF-DSS-VULN-01 (Vulnerability Mgmt) -> Reduces risk by 20%
+-- Residual Risk: 10% (within acceptable appetite)
```

### AI Controls — AI Risk Reduction

```
Risk: AI System Bias (Impact: High)
+-- EATGF-AI-LC-01 (Lifecycle Governance) -> Reduces risk by 25%
+-- EATGF-AI-RISK-01 (Risk and Bias Mgmt) -> Reduces risk by 35%
+-- EATGF-MEA-PERF-01 (Performance Monitoring) -> Reduces risk by 15%
+-- Residual Risk: 25% (requires continuous monitoring)
```

### API Controls — API Risk Reduction

```
Risk: API Security Breach (Impact: High)
+-- EATGF-API-SEC-01 (API Security) -> Reduces risk by 40%
+-- EATGF-API-LC-01 (API Lifecycle) -> Reduces risk by 20%
+-- EATGF-DSS-SEC-01 (IAM) -> Reduces risk by 15%
+-- Residual Risk: 25% (monitored via EATGF-MEA-PERF-01)
```

---

## 8. Risk Acceptance Template

**When controls cannot eliminate risk, the following form is required:**

```
Risk Acceptance Form

Risk: [Description]
Risk Owner: [Name]
Risk Level: [Before controls] -> [After controls]

Mitigation Options Considered:
1. Control option 1: Cost $X, Benefit Y
2. Control option 2: Cost $X, Benefit Y
3. [Additional options]

Decision:
[ ] Accept risk — No additional controls
[ ] Implement partial controls — Cost/benefit optimal
[ ] Implement full controls — Zero risk tolerance

Residual Risk Level: [Accepted level]
Sign-off: [CFO/CEO approval required for Red risks]
Date: [Date]

Review Schedule: [Quarterly/Annually]
```

---

## 9. Risk Monitoring Dashboard

**Standard KPIs:**

| KPI                     | Current | Target  | Status             |
| ----------------------- | ------- | ------- | ------------------ |
| Red risks (Critical)    | 2       | 0       | Off track          |
| Orange risks (High)     | 8       | <5      | Below target       |
| Risk mitigation on-time | 85%     | 95%     | Improvement needed |
| Unplanned outages       | 3/year  | <1/year | On track           |
| Security incidents      | 2/year  | <1/year | On track           |
| Compliance violations   | 0       | 0       | On track           |

---

## 10. Governance Enforcement Rules

1. Risk identification and assessment follow the methodology defined in this document. The Master Control Matrix is the single source of truth for controls that map to identified risks.
2. All risk register entries must reference the applicable EATGF control IDs using the `EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]` format.
3. Risk acceptance for Red-level risks requires CFO/CEO sign-off.
4. Annual risk assessment results feed into the maturity assessment cycle (EATGF-MEA-MAT-01).

---

**Document Control**

| Version | Date       | Author                                      | Change Description                                                                                                                                                    |
| ------- | ---------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-02-01 | Governance Office                           | Initial risk framework                                                                                                                                                |
| 2.0     | 2026-02-14 | Enterprise Architecture & Governance Office | Adopted EATGF-xxx control taxonomy; added AI and API control-risk mappings; added EATGF header; removed placeholder content; corrected tone to institutional register |

**Authority Sign-Off**

| Role                     | Name | Date | Signature |
| ------------------------ | ---- | ---- | --------- |
| Chief Risk Officer       |      |      |           |
| Chief Governance Officer |      |      |           |

---

**Next Annual Risk Assessment:** February 2027
**Next Review:** August 2026
