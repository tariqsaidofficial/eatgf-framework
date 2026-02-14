# Enterprise Risk Framework

## Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field | Value |
|-------|-------|
| Document Type | Framework |
| Version | 2.0 |
| Classification | Internal |
| Effective Date | 2026-02-14 |
| Baseline | COBIT 2019, ISO 31000:2018, ISO 27005:2022 |
| Authority | Enterprise Architecture & Governance Office |
| MCM Reference | EATGF-EDM-RISK-01, EATGF-APO-RISK-01, EATGF-AI-RISK-01 |

---

## 1. Risk Management Overview

This framework establishes the methodology for identifying, assessing, and managing risks across all EATGF-governed domains.

### Core Principles

1. **Risk Ownership** — Every risk has an assigned owner responsible for mitigation.
2. **Risk Transparency** — All material risks are reported and tracked in the enterprise risk register.
3. **Risk-Based Prioritization** — Resources are allocated based on risk impact scoring.
4. **Continuous Monitoring** — Risk status is reviewed monthly at minimum.
5. **Escalation Procedures** — Critical risks are escalated immediately per the defined escalation chain.

---

## 2. Risk Assessment Process

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

| Category | Assessment |
|----------|-----------|
| **Probability** | 1 (Rare) to 5 (Very Likely) |
| **Impact** | 1 (Minimal) to 5 (Critical) |
| **Risk Score** | Probability x Impact (1-25) |
| **Current Controls** | Existing EATGF controls mapped to risk |
| **Gap** | Required control gaps identified |

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

| Risk Level | Escalation Trigger | Owner | Timeline |
|-----------|------------------|-------|----------|
| **Red** | Probability or Impact increases by 1+ level | CISO/CFO | Immediate (1 hour) |
| **Orange** | Without mitigation, could become critical | CRO | 1 business day |
| **Yellow** | Mitigation not on track | Risk Owner | Weekly |
| **Green** | Standard monitoring | Process Owner | Monthly |

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

| KPI | Current | Target | Status |
|-----|---------|--------|--------|
| Red risks (Critical) | 2 | 0 | Off track |
| Orange risks (High) | 8 | <5 | Below target |
| Risk mitigation on-time | 85% | 95% | Improvement needed |
| Unplanned outages | 3/year | <1/year | On track |
| Security incidents | 2/year | <1/year | On track |
| Compliance violations | 0 | 0 | On track |

---

## 10. Governance Enforcement Rules

1. Risk identification and assessment follow the methodology defined in this document. The Master Control Matrix is the single source of truth for controls that map to identified risks.
2. All risk register entries must reference the applicable EATGF control IDs using the `EATGF-[DOMAIN]-[CATEGORY]-[NUMBER]` format.
3. Risk acceptance for Red-level risks requires CFO/CEO sign-off.
4. Annual risk assessment results feed into the maturity assessment cycle (EATGF-MEA-MAT-01).

---

**Document Control**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-01 | Governance Office | Initial risk framework |
| 2.0 | 2026-02-14 | Enterprise Architecture & Governance Office | Adopted EATGF-xxx control taxonomy; added AI and API control-risk mappings; added EATGF header; removed placeholder content; corrected tone to institutional register |

**Authority Sign-Off**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Chief Risk Officer | | | |
| Chief Governance Officer | | | |

---

**Next Annual Risk Assessment:** February 2027
**Next Review:** August 2026
