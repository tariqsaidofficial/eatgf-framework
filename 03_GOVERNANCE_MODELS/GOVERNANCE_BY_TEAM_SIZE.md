# GOVERNANCE BY TEAM SIZE

**Guide Version:** 1.0  
**Effective Date:** February 2026

---

## EDITION 1: STARTUP GOVERNANCE (1-10 People)

**Philosophy:** Lightweight, practical governance that doesn't slow down product delivery.

---

### Core Governance Requirements (Startup)

**Essential:**
1. ✅ Basic information security controls
2. ✅ Data backup and disaster recovery
3. ✅ Access control (passwords + basics)
4. ✅ Risk awareness
5. ✅ Documentation of key processes

**Nice to have:**
- Formal policies (informal guidelines okay)
- Compliance certifications (focus on practice)
- AI governance (only if building AI)

---

### Startup Control Implementation

| Control | Requirement | Implementation | Time |
|---------|------------|-----------------|------|
| **SEC-01** (Access) | Passwords + strong auth | 1Password or similar | 1 week |
| **SEC-02** (Encryption) | Encrypt sensitive data | Use default TLS/encryption | Already done |
| **SEC-03** (Vulnerabilities) | Keep systems patched | Auto-updates enabled | Ongoing |
| **AC-01** (Architecture) | Document system design | 1-page architecture diagram | 1 day |
| **RISK-01** (Risk Register) | Know your top 5 risks | Spreadsheet with actions | 1 day |
| **PERF-01** (KPIs) | Track what matters | System uptime + customer issues | 1 day |

**Total Setup Time:** ~2 weeks for full startup pack

---

### Startup Policies (Minimal Set)

**Create 3 short policies (1-2 pages each):**

1. **Information Security Policy**
   - Use default/strong passwords
   - Never share passwords
   - Report suspicious activity

2. **Data Privacy Policy**
   - How we handle customer data
   - Retention periods
   - Secure deletion

3. **Remote Work Policy**
   - VPN required for company access
   - No sensitive data on personal devices
   - Laptop encryption mandatory

**Effort:** 4 hours total writing time

---

### Startup Team Responsibilities

| Role | Who | Hours/Week |
|------|-----|-----------|
| Security lead | 1 founder/dev | 4 hours |
| Data steward | 1 person | 2 hours |
| Risk awareness | Everyone | 15 min/month |

**Total governance effort:** ~6-8 hours/week across small team

---

### Startup Risk Focus

**Top 5 risks to monitor:**

1. **Customer data breach** → Encrypted backups, access control
2. **Ransomware/malware** → Backups, updated OS
3. **Account compromise** → Password manager, MFA
4. **Accidental data loss** → Backup system + testing
5. **Vendor dependency** → Know 1-2 backup vendors

---

### Startup Compliance Reality

**What investors/customers actually care about:**
- ✅ Data is encrypted and backed up
- ✅ Access is logged and controlled
- ✅ You have a security incident plan
- ✅ You can demonstrate SOC 2 Type I basics

**Avoid:**
- ❌ Lengthy 50-page policies nobody reads
- ❌ Formal governance committees
- ❌ Heavy compliance tools (spreadsheets are fine)
- ❌ Over-engineering security before you have customers

---

## EDITION 2: SAAS GOVERNANCE (10-50 People)

**Philosophy:** Structured governance with clear ownership without enterprise bureaucracy.

---

### SaaS Governance Requirements

**Essential:**
1. ✅ Formal policies with acknowledgment
2. ✅ Access control with quarterly reviews
3. ✅ Vulnerability management process
4. ✅ Incident response plan
5. ✅ Regular risk assessment (annual)
6. ✅ KPI tracking and reporting
7. ✅ AI governance (if applicable)
8. ✅ API security standards (if SaaS APIs)

**Supporting:**
- Governance council (monthly meetings)
- Risk register (quarterly updates)
- Compliance tracking (monthly status)
- Training program (annual)

---

### SaaS Control Implementation

| Domain | Control | Implementation |
|--------|---------|-----------------|
| **Architecture** | AC-01 | System architecture documented |
| | AC-02 | Integration architecture + API specs |
| | AC-03 | Technology platform standards |
| **Security** | SEC-01 | IAM system (Okta/Auth0) |
| | SEC-02 | Full encryption at rest + in transit |
| | SEC-03 | Monthly vulnerability scanning |
| **AI** | AI-01 | AI system intake & governance |
| | AI-02 | Fairness/bias assessment |
| **API** | API-01 | API design standards + OpenAPI |
| | API-02 | OAuth 2.0 authentication |
| **Risk** | RISK-01 | Annual risk assessment |
| | RISK-02 | Monthly risk dashboard |
| **Perf** | PERF-01 | Monthly KPI reporting |
| | PERF-02 | Annual maturity assessment |

---

### SaaS Organizational Structure

```
CEO/Founder
├── CTO/Tech Lead
│   ├── Engineering Lead
│   ├── Security Officer
│   └── DevOps/SRE
├── Product Lead
│   └── Product Manager
├── Operations
│   ├── Finance
│   └── HR
└── Compliance Officer (part-time role)
    └── Governance administration
```

**Governance Council (Monthly):**
- CTO (chair)
- Security Officer
- Product Lead
- Compliance Officer
- Risk representative (if hired)

---

### SaaS Policies (Comprehensive Set)

**Create formal policies:**
1. Information Security Policy (2 pages)
2. Data Governance Policy (2 pages)
3. Access Control Policy (2 pages)
4. AI Governance Policy (if applicable) (3 pages)
5. API Governance Policy (if applicable) (2 pages)
6. Risk Management Policy (1 page)
7. Data Retention & Disposal (1 page)
8. Incident Response Plan (3 pages)

**Communication:**
- Email announcement to all staff
- Training session (30 min monthly)
- Printed copy in office
- Annual re-acknowledgment requirement

---

### SaaS Control Testing

**Quarterly Control Testing:**
- Sample testing of 5-10 key controls
- Document results in evidence template
- Remediate any gaps within 30 days
- Report results to governance council

**Example Test Schedule:**

| Quarter | Controls Tested |
|---------|-----------------|
| Q1 | Access control, Data encryption |
| Q2 | Vulnerability management, Backups |
| Q3 | Incident response, API security |
| Q4 | Maturity assessment, Risk review |

---

### SaaS Reporting Cadence

| Report | Frequency | Owner |
|--------|-----------|-------|
| Risk dashboard | Monthly | Security/Risk officer |
| KPI metrics | Monthly | Governance lead |
| Compliance status | Monthly | Compliance officer |
| Incident summary | Monthly | Security |
| Governance council notes | Monthly | CTO |
| Audit readiness | Quarterly | Compliance officer |
| Risk assessment | Annual | Governance council |
| Maturity assessment | Annual | External assessor |

---

### SaaS Governance Effort

| Role | Hours/Week |
|------|-----------|
| CTO (governance oversight) | 4-6 hours |
| Security Officer | 10-15 hours |
| Compliance Officer (part-time) | 8-10 hours |
| Team acknowledgments/training | 1 hour each |

**Total:** 25-35 hours/week governance team

---

### SaaS Customers Expectations

**What typical SaaS customers ask for:**
- SOC 2 Type II certification (annual external audit)
- Data location options (US/EU)
- Encryption transparency (we have it)
- Incident response SLA (24-hour response)
- Penetration testing reports (annual)

**Governance alignment:** All addressed through formal controls and auditing

---

## EDITION 3: ENTERPRISE GOVERNANCE (50+ People)

**Philosophy:** Enterprise-grade governance with distributed accountability and continuous optimization.

---

### Enterprise Governance Requirements

**All SaaS requirements, plus:**
1. ✅ Executive governance committee
2. ✅ CISO role (dedicated person)
3. ✅ Chief Compliance Officer or equivalent
4. ✅ Internal audit function
5. ✅ Formal maturity model assessment
6. ✅ Regulatory compliance (SOC 2, ISO 27001, etc.)
7. ✅ Advanced risk management (predictive)
8. ✅ AI governance with fairness audit
9. ✅ API management platform
10. ✅ Compliance tools & automation

---

### Enterprise Organizational Structure

```
Board / Executive Committee
├── CEO
│   ├── CTO
│   │   ├── Chief Information Security Officer (CISO)
│   │   │   ├── Security Engineering Lead
│   │   │   ├── Threat & Vulnerability Lead
│   │   │   └── Security Operations (SOC)
│   │   ├── VP Engineering
│   │   ├── VP Infrastructure
│   │   └── Data Chief
│   ├── Chief Compliance Officer (CCO)
│   │   ├── Compliance Manager
│   │   ├── Audit Manager
│   │   ├── Risk Manager
│   │   └── Legal/Privacy Officer
│   ├── Chief Financial Officer
│   └── Chief Governance Officer (optional)
```

**Key Committees:**

1. **Risk & Compliance Committee** (Monthly)
   - CISO + CCO + CFO + Internal Audit Lead
   - Reviews risk dashboard, compliance status, audit findings

2. **Enterprise Architecture Board** (Quarterly)
   - CTO + Domain architects + Security lead
   - Approves major technology decisions

3. **AI Governance Board** (Quarterly)
   - Chief AI Officer + Data Lead + Ethics representative
   - Governs all AI/ML systems

4. **Board-Level Audit Committee** (Quarterly)
   - Board members + CFO + Internal audit director
   - Reviews governance effectiveness, audit results

---

### Enterprise Control Implementation

**Full implementation of ALL controls:**
- Architecture controls (3 controls)
- Security controls (3 controls - mature level)
- AI governance controls (full framework)
- API controls (full governance platform)
- Risk management framework
- Performance measurement (mature level)

---

### Enterprise Governance Tools

| Function | Tool Category | Example |
|----------|--------------|---------|
| Policy Mgmt | Document Management | SharePoint + workflow |
| Risk Mgmt | Specialized platform | AuditBoard / LogicGate |
| Compliance | Continuous monitoring | Domo / Tableau |
| Security monitoring | SIEM + EDR | Splunk + CrowdStrike |
| Identity Mgmt | Enterprise IAM | Okta Enterprise |
| API Management | Platform | Apigee / Kong |
| Audit | Audit platform | AuditBoard / Workiva |
| Data Governance | Data catalog | Collibra / Alation |
| Vulnerability Mgmt | Platform | Qualys / Tenable |
| Incident Response | SOAR | ServiceNow / Demisto |

**Annual spend:** $2-5M depending on organization size

---

### Enterprise Compliance Standards

**Typical compliance requirements:**

| Standard | Requirement | Frequency |
|----------|------------|-----------|
| **SOC 2 Type II** | Security & operational controls | Annual audit |
| **ISO 27001** | Information security mgmt | Annual/bi-annual audit |
| **GDPR** | Data privacy for EU customers | Ongoing + DPA review |
| **HIPAA** | Healthcare data (if applicable) | Annual audit |
| **PCI-DSS** | Payment card data (if applicable) | Annual audit |
| **FedRAMP** | US federal sales (if applicable) | Annual assessment |
| **Industry-specific** | Financial/healthcare/etc. | Varies |

---

### Enterprise Risk Management

**Sophisticated approach:**

1. **Quarterly Risk Assessment**
   - Identify 50+ potential risks
   - Risk scoring with heat maps
   - Mitigation plans tracked
   - Board escalation for critical risks

2. **Predictive Risk Modeling**
   - Trend analysis over time
   - Forecast future risk states
   - Early warning indicators
   - Scenario planning

3. **Real-time Risk Monitoring**
   - Dashboards showing current state
   - Automated alerts for threshold breaches
   - Incident correlation
   - Vulnerability trending

---

### Enterprise Governance Effort

| Role | Team Size | Hours/Week |
|------|-----------|-----------|
| CISO | 1 | 50-60 |
| Security team | 5-10 | 200+ |
| Compliance officer | 1-2 | 40-50 |
| Audit team | 2-3 | 80-120 |
| Risk team | 1-2 | 40-80 |
| Governance administration | 1-2 | 40-60 |

**Total:** 500-800+ hours/week (8-12 FTEs)

---

### Enterprise Maturity Target

**Target governance maturity: Level 4-5 (Managed/Optimized)**

```
Governance Maturity by Domain:
  EDM:  4.5 (Managed + Strategic oversight)
  APO:  4.2 (Managed + Planning)
  BAI:  4.0 (Managed)
  DSS:  4.5 (Managed + Resilience)
  MEA:  4.8 (Optimized + Continuous improvement)

Overall: 4.4 (Managed - Excellent practices)
```

---

## COMPARING THE THREE EDITIONS

| Factor | Startup | SaaS | Enterprise |
|--------|---------|------|-----------|
| **Team size** | 1-10 | 10-50 | 50+ |
| **Governance effort** | 1-2 FTE | 2-3 FTE | 8-12 FTE |
| **Annual cost** | $50K | $200K | $2-5M |
| **Policies** | 3 short | 7-8 formal | 15+ detailed |
| **Risk reviews** | Annual | Quarterly | Monthly |
| **Maturity target** | 2 (Dev) | 3-4 (Def/Mgmt) | 4-5 (Mgmt/Opt) |
| **Compliance certs** | None required | SOC 2 Type II | Multiple |
| **Board oversight** | Informal | CTO + board member | Audit committee |
| **Tools** | Spreadsheets | 3-5 tools | 10+ tools |
| **Internal audit** | No | Maybe | Yes (dedicated) |

---

## SCALING FROM ONE EDITION TO NEXT

### Startup → SaaS (Managing Growth)

**Trigger:** Reaching 8-10 people

**Key changes needed:**
1. Hire dedicated security person
2. Formalize policies
3. Implement IAM system (Okta/Auth0)
4. Monthly governance meetings
5. Create risk register
6. Establish compliance focus

**Timeline:** 2-3 months

---

### SaaS → Enterprise (Maturing)

**Trigger:** Reaching 40+ people or $10M+ revenue

**Key changes needed:**
1. Hire CISO (executive-level)
2. Hire Compliance officer
3. Implement compliance tools
4. Create governance committees (plural)
5. Establish audit function
6. Advanced risk management

**Timeline:** 4-6 months

---

**Questions?** Contact: governance@enterprise.com  
**Edition Assessment:** Need help determining your edition? scheduling-tool.com
