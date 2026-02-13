# FRAMEWORK MAPPINGS

**Version:** 1.0  
**Effective Date:** February 2026

---

## 1. COBIT 2019 ↔ ISO 38500 MAPPING

| COBIT Domain | COBIT Process | ISO 38500 Principle |
|-------------|------|----------|
| EDM | EDM01 - Evaluate and direct IT governance | Board responsibility |
| EDM | EDM02 - Ensure benefits realisation | Value delivery |
| APO | APO01 - Manage the IT management framework | Strategic alignment |
| APO | APO02 - Manage strategy | Strategy execution |
| BAI | BAI01 - Manage programs and projects | Risk management |
| BAI | BAI02 - Manage requirements definition | Compliance |
| DSS | DSS01 - Manage operations | Human resources |
| DSS | DSS02 - Manage service requests | Compliance |
| MEA | MEA01 - Monitor, evaluate, and assess performance | Performance measurement |
| MEA | MEA02 - Monitor, evaluate, and assess the system of internal control | Control monitoring |

---

## 2. COBIT 2019 ↔ ISO 27001 MAPPING

| COBIT Control | ISO 27001 Control | Description |
|-------------|--------|----------|
| SEC-01 (IAM) | A.9.1, A.9.2 | Access control policies and implementation |
| SEC-02 (Encryption) | A.10.1, A.10.2 | Cryptography standards |
| SEC-03 (Vuln Mgmt) | A.12.6 | Management of technical vulnerabilities |
| AC-01 (Architecture) | A.12.1 | Secure development and operations |
| DSS02 (Incident Response) | A.16.1 | Incident management |
| RISK-01 (Risk Assessment) | A.12.6.1 | Risk evaluation |

### ISO 27001 Control Set Coverage

**Fully Covered:** A.5-A.16 (Core security controls)  
**Partially Covered:** A.4 (Organization controls)  
**Reference:** A.1-A.3 (Context controls)

---

## 3. COBIT 2019 ↔ ISO 42001 (AI MANAGEMENT) MAPPING

| COBIT Control | ISO 42001 Section | Purpose |
|-------------|--------|----------|
| AI-01 | Section 6 | AI system lifecycle |
| AI-02 | Section 8.1 | AI risk assessment |
| SEC-02 | Section 8.2 | AI data protection |
| AC-01 | Section 6.1 | AI system architecture |
| PERF-01 | Section 7 | AI performance metrics |
| MEA-02 | Section 9 | AI control effectiveness |

### ISO 42001 Domains Addressed
- ✅ AI governance and management
- ✅ AI system development and deployment
- ✅ AI risk and impact management
- ✅ Data governance for AI systems
- ✅ Transparency and explainability

---

## 4. API GOVERNANCE ↔ OWASP MAPPING

| API Control | OWASP Category | Implementation |
|-------------|--------|----------|
| API-01 (Design) | API1:2023 - Broken Object Level Authorization | API design standards prevent direct object access |
| API-02 (Security) | API2:2023 - Broken Authentication | Authentication/authorization controls |
| API-02 | API3:2023 - Broken Object Property Level Authorization | RBAC with field-level controls |
| API-02 | API4:2023 - Unrestricted Resource Consumption | Rate limiting and quota management |
| API-02 | API5:2023 - Broken Function Level Authorization | Function-level access controls |
| API-02 | API6:2023 - Unrestricted Access to Sensitive Business Flows | Business logic protection |
| API-02 | API7:2023 - Server-Side Request Forgery | Input validation and allowlists |
| API-02 | API8:2023 - Security Misconfiguration | Configuration standards |
| API-02 | API9:2023 - Improper Inventory Management | API inventory control (API-01) |
| API-02 | API10:2023 - Unsafe Consumption of APIs | Third-party API validation |

---

## 5. GOVERNANCE FRAMEWORK ALIGNMENT MATRIX

```
┌─────────────────────────────────────────────────────────────┐
│                    Enterprise Governance                     │
│                     Framework (This)                         │
└──────┬──────────────┬──────────────┬──────────────┬──────────┘
       │              │              │              │
   ┌───▼───┐      ┌───▼───┐     ┌───▼───┐     ┌───▼────┐
   │ COBIT │      │ ISO   │     │ ISO   │     │ OWASP  │
   │ 2019  │      │ 38500 │     │ 27001 │     │        │
   │ (Core)│      │(Corp) │     │(Sec)  │     │(API)   │
   └───┬───┘      └───┬───┘     └───┬───┘     └───┬────┘
       │              │              │              │
       └──────────────┴──────────────┴──────────────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
      ┌───▼──┐    ┌───▼──┐   ┌───▼──┐
      │ ISO  │    │ Risk │   │ KPI  │
      │42001 │    │Model │   │Model │
      │(AI)  │    │      │   │      │
      └──────┘    └──────┘   └──────┘
```

---

## 6. CONTROL MAPPING BY FRAMEWORK

### COBIT 2019 Coverage

| Domain | Total Processes | Our Controls | Coverage |
|--------|---------|-------------|----------|
| EDM (Evaluate, Direct, Monitor) | 4 | RISK-01, RISK-02 | 50% |
| APO (Align, Plan, Organize) | 13 | AC-01, AC-03 | 15% |
| BAI (Build, Acquire, Implement) | 10 | AC-02, AI-01, API-01 | 30% |
| DSS (Deliver, Service, Support) | 6 | SEC-01, SEC-02, SEC-03, API-02 | 67% |
| MEA (Monitor, Evaluate, Assess) | 4 | AI-02, PERF-01, PERF-02 | 75% |

### ISO 27001 Coverage

| Annex | Metrics | Coverage |
|-------|---------|----------|
| A.5 - Organizational Controls | 2/2 Controls | ✅ 100% |
| A.6 - Personnel Security | 3/3 Controls | ✅ 100% |
| A.7 - Asset Management | 2/2 Controls | ✅ 100% |
| A.8 - Access Control | 8/8 Controls | ✅ 100% |
| A.9 - Cryptography | 2/2 Controls | ✅ 100% |
| A.10 - Physical & Environmental | 3/3 Controls | ⚠️ 50% |
| A.11 - Operations Security | 7/7 Controls | ✅ 100% |
| A.12 - Communications Security | 7/7 Controls | ✅ 100% |
| A.13 - System Acquisition | 5/5 Controls | ✅ 100% |
| A.14 - Supplier Relationships | 3/3 Controls | ✅ 100% |
| A.15 - Information Security Incident | 5/5 Controls | ✅ 100% |
| A.16 - Business Continuity | 2/2 Controls | ⚠️ 50% |

---

## 7. STANDARD SELECTION BY TEAM SIZE

### Startup Edition (1-10 people)

**Applicable Standards:**
- ✅ COBIT 2019 (Lightweight subset)
- ✅ ISO 27001 (Core categories only)
- ⚠️ ISO 38500 (Strategic guidance)
- ❌ ISO 42001 (Only if AI systems exist)
- ⚠️ OWASP (If APIs exposed)

**Focus Areas:**
1. Basic security (SEC-01, SEC-03)
2. Access control (SEC-01)
3. Risk awareness (RISK-01)
4. Data protection basics (SEC-02)

---

### SaaS Edition (10-50 people)

**Applicable Standards:**
- ✅ COBIT 2019 (Full framework)
- ✅ ISO 27001 (Complete)
- ✅ ISO 38500 (Full implementation)
- ✅ ISO 42001 (If AI systems exist)
- ✅ OWASP (Full compliance)

**Focus Areas:**
1. Complete security controls
2. AI governance (AI-01, AI-02)
3. API governance (API-01, API-02)
4. Risk management
5. Performance metrics

---

### Enterprise Edition (50+ people)

**Applicable Standards:**
- ✅ COBIT 2019 (Complete)
- ✅ ISO 27001 (Complete + extras)
- ✅ ISO 38500 (Complete + board alignment)
- ✅ ISO 42001 (Full with AI expertise)
- ✅ OWASP (Advanced + threat modeling)

**Focus Areas:**
1. All controls fully implemented
2. Advanced AI governance
3. Complex API ecosystems
4. Enterprise risk management
5. Continuous optimization

---

## 8. MAPPING UPDATE SCHEDULE

| Framework | Version | Last Updated | Next Review |
|-----------|---------|-------------|------------|
| COBIT | 2019 | Feb 2026 | Aug 2026 |
| ISO 38500 | 2015 | Feb 2026 | Aug 2026 |
| ISO 27001 | 2022 | Feb 2026 | Aug 2026 |
| ISO 42001 | 2024 | Feb 2026 | Aug 2026 |
| OWASP API Security | 2023 | Feb 2026 | Feb 2027 |

---

**Questions?** Contact: governance@enterprise.com
