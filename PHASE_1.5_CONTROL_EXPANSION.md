# ENTERPRISE AI-ALIGNED TECHNICAL GOVERNANCE FRAMEWORK (EATGF)
## Master Control Matrix - EXPANSION LAYER (Phase 1.5)
### Adding Cloud, DevSecOps, Data Privacy, and Business Continuity Controls

**Framework:** EATGF v0.9 → v1.0  
**Document Type:** Control Expansion Specification  
**Version:** Phase 1.5  
**Date:** February 13, 2026  
**Purpose:** Complete MCM from 21 to 35+ controls before Management System layer  
**Classification:** Technical - Internal Use

---

## 📊 EXPANSION OVERVIEW

### Current State (MCM v0.9)
- 21 controls across 5 COBIT domains
- Coverage: EDM (3) / APO (4) / BAI (3) / DSS (4) / MEA (3)
- Extensions: AI (2) / API (2)
- **Gap:** No Cloud Governance, DevSecOps, Data Privacy, BCP controls

### Target State (MCM v1.0)
- **35-45 controls** across **8 domains**
- New domains: CLD (Cloud), DEV (DevSecOps), DATA (Data Privacy), BCP (Business Continuity)
- **Complete coverage** of ISO 27001 Annex A requirements
- **Audit-ready** for SaaS/Enterprise operations

### Why Required

| Gap Area | ISO 27001 | ISO 42001 | Impact | Fix |
|----------|-----------|-----------|--------|-----|
| Cloud Governance | A.5.23, A.8.28 | 8.2 | SaaS undefendable | Add CLD controls |
| DevSecOps | A.8.19, A.8.25 | 8.1 | SDLC gaps | Add DEV controls |
| Data Privacy | A.5.31-32 | 8.2 | GDPR unready | Add DATA controls |
| Business Continuity | A.5.29-30, A.8.24-26 | N/A | RPO/RTO undefined | Add BCP controls |

---

## 🔷 NEW DOMAIN 4: CLOUD GOVERNANCE (CLD)

**Alignment:** ISO 27001 A.5.23 (Supplier relationships), A.8.28 (ICT readiness)  
**Standards:** NIST 800-53 SC/AC, CSA CAIQ, Cloud Controls Matrix  
**Owner:** Chief Cloud Officer / Cloud Architect  
**Applicability:** SaaS / Enterprise (conditional Startup)

---

### EATGF-CLD-ARCH-01: Cloud Architecture & Design Standards

| Field | Value |
|-------|-------|
| **Control Title** | Cloud Architecture & Design Standards |
| **Control Description** | Organization maintains cloud architecture standards including multi-cloud strategy, region selection, network design, and shared responsibility model documentation. |
| **Governance Domain** | CLD (Cloud) - APO equivalent |
| **Control Type** | Preventive |
| **COBIT Equivalent** | APO03 (Enterprise Architecture) + APO13 (Security) |
| **ISO 27001 Mapping** | A.5.23 (Supplier relationships), A.8.28 (ICT readiness) |
| **ISO 42001 Mapping** | 8.1 (Operational planning for AI systems) |
| **NIST 800-53** | SA-3 (System development life cycle) |
| **Evidence Required** | Cloud architecture document, multi-cloud strategy, region policy, network architecture diagram, shared responsibility matrix |
| **Control Owner** | Chief Cloud Officer / Cloud Architect |
| **Evidence Owner** | Cloud Architecture Team |
| **Review Frequency** | Annual (or per major cloud migration) |
| **Applicability** | SaaS / Enterprise |

**Evidence Checklist:**
- [ ] Cloud architecture standards document published
- [ ] Multi-cloud strategy approved (single vs. multi-cloud decision)
- [ ] Region selection policy (data residency, geopolitical)
- [ ] Network architecture diagram (VPC/VNet/networking)
- [ ] Shared Responsibility Model documented per provider
- [ ] DR/failover strategy cross-region
- [ ] Cost optimization framework
- [ ] Quarterly architecture review

**Key Elements:**
```
Cloud Architecture Standards:
├─ Deployment Model
│  ├─ Primary: [AWS/Azure/GCP]
│  ├─ Secondary: [Multi-cloud strategy if applicable]
│  └─ Rationale: [Business/technical/cost drivers]
├─ Region Strategy
│  ├─ Primary region: [us-east / eu-west / etc.]
│  ├─ Backup region: [specified]
│  └─ Data residency rules: [GDPR / regulatory]
├─ Network Design
│  ├─ Segmentation (VPC/security groups)
│  ├─ Private vs. public subnets
│  └─ WAF/DDoS protection
├─ Shared Responsibility
│  ├─ AWS/Azure/GCP responsibilities (compliance, infrastructure)
│  └─ Organization responsibilities (data, access, encryption)
└─ DR Strategy
   ├─ RTO target (hours)
   └─ RPO target (minutes/hours)
```

---

### EATGF-CLD-SEC-01: Cloud Security & Compliance Controls

| Field | Value |
|-------|-------|
| **Control Title** | Cloud Security & Compliance Configuration |
| **Control Description** | Cloud infrastructure enforces security baselines: encryption, network security, access control, compliance monitoring. Automated compliance checking in place. |
| **Governance Domain** | CLD |
| **Control Type** | Preventive |
| **COBIT Equivalent** | DSS05 (Access) / DSS07 (Encryption) |
| **ISO 27001 Mapping** | A.5.18 (Access control), A.8.3 (Encryption), A.8.8 (Network security) |
| **NIST 800-53** | AC-3, AC-5, SC-7, SC-28 |
| **CSA CAIQ** | GRC-01 / ILM-03 / EKM-01 |
| **Evidence Required** | Cloud security configuration, CloudTrail/audit logging, compliance scanner results, IAM policies, encryption settings |
| **Control Owner** | Chief Information Security Officer / Cloud Security Lead |
| **Evidence Owner** | Cloud Security Team |
| **Review Frequency** | Monthly |
| **Applicability** | All (SaaS mandatory, Enterprise mandatory) |

**Evidence Checklist:**
- [ ] Cloud security baseline document (AWS/Azure/GCP CIS benchmarks)
- [ ] Network security groups/firewall rules configured
- [ ] Encryption at rest (S3/blob storage) enabled
- [ ] Encryption in transit (TLS 1.2+) enforced
- [ ] CloudTrail/diagnostic logging enabled and retention set (12 months)
- [ ] MFA enabled for all cloud console access
- [ ] Cloud compliance scanner deployed (Config/Advisor/Azure Policy)
- [ ] Monthly compliance scan results reviewed
- [ ] Critical/High findings remediation tracking

**Key Controls:**
```
Cloud Security Baselines:
├─ Identity & Access
│  ├─ Root account password locked away
│  ├─ MFA required for console access
│  └─ IAM roles/policies least-privilege
├─ Network Security
│  ├─ VPC isolation (no public internet access except via ALB/WAF)
│  ├─ Security groups restrict inbound to necessary ports
│  └─ VPN/private link for cross-region/hybrid
├─ Data Protection
│  ├─ Encryption at rest (AES-256) enabled on all storage
│  ├─ Encryption in transit (TLS 1.2+) enforced
│  └─ Key management (KMS/Key Vault) with rotation
├─ Monitoring
│  ├─ CloudTrail/audit logging enabled and protected
│  ├─ Cloud security posture scanner running
│  └─ Alerts for critical events
└─ Compliance
   ├─ CIS Benchmark scoring 80%+ (automated)
   └─ Quarterly manual compliance assessment
```

---

### EATGF-CLD-MON-01: Cloud Cost, Performance & Compliance Monitoring

| Field | Value |
|-------|-------|
| **Control Title** | Cloud Operations Monitoring & Cost Governance |
| **Control Description** | Real-time monitoring of cloud infrastructure performance, cost, and compliance. Automated alerts for anomalies. Monthly cost reviews. Compliance drift detection. |
| **Governance Domain** | CLD |
| **Control Type** | Detective |
| **COBIT Equivalent** | MEA01 (Monitoring) |
| **ISO 27001 Mapping** | A.5.23 (Supplier monitoring), 9.1 (Monitoring & measurement) |
| **Evidence Required** | Cost dashboard, performance metrics, compliance violation alerts, monthly cost reports, cost optimization actions |
| **Control Owner** | Chief Financial Officer / Cloud Cost Manager |
| **Evidence Owner** | Cloud Operations Team |
| **Review Frequency** | Monthly |
| **Applicability** | All |

**Evidence Checklist:**
- [ ] Cloud cost dashboard live (AWS Cost Explorer / Azure Cost Management)
- [ ] Cost anomaly alerts configured (>10% variance threshold)
- [ ] Monthly cost review meeting held with stakeholders
- [ ] Performance dashboard for application latency/uptime
- [ ] Compliance violation dashboard (automated scanning)
- [ ] Unused resource identification (aged snapshots, orphaned IPs)
- [ ] Cost optimization recommendations tracked and implemented
- [ ] Quarterly cost optimization report

**Key Metrics:**
```
Cloud Operations Metrics:
├─ Cost Management
│  ├─ Monthly spend trend
│  ├─ Cost per service (compute/storage/data transfer)
│  └─ Budget variance (vs. forecast)
├─ Performance
│  ├─ Application latency (p50/p95/p99)
│  ├─ Uptime %
│  └─ API error rates
├─ Compliance
│  ├─ CIS benchmark score
│  ├─ Policy violations detected
│  └─ Unpatched resources count
└─ Optimization
   ├─ Unused resources (instances, IPs, snapshots)
   ├─ Reserved instance utilization
   └─ Cost reduction opportunities identified
```

---

### EATGF-CLD-RES-01: Cloud Resilience & Disaster Recovery

| Field | Value |
|-------|-------|
| **Control Title** | Cloud Resilience & Disaster Recovery Management |
| **Control Description** | Cloud infrastructure implements multi-region/availability zone redundancy. Backup strategy, failover procedures, and RTO/RPO targets defined and tested. |
| **Governance Domain** | CLD / BCP |
| **Control Type** | Preventive |
| **COBIT Equivalent** | DSS03 (Delivery of services) + BAI06 (Availability planning) |
| **ISO 27001 Mapping** | A.5.29 (Information security incident management), A.8.24 (Recovery procedures) |
| **ISO 22301** | 8.1-8.5 (BC/DR requirements) |
| **Evidence Required** | Cloud resilience architecture, backup strategy, RTO/RPO SLAs, failover test results, disaster recovery plan |
| **Control Owner** | Chief Technology Officer / Disaster Recovery Lead |
| **Evidence Owner** | Cloud Operations / Disaster Recovery Team |
| **Review Frequency** | Quarterly (testing), Annual (strategy review) |
| **Applicability** | SaaS / Enterprise |

**Evidence Checklist:**
- [ ] Multi-AZ/region architecture diagram
- [ ] RTO target defined (e.g., 4 hours max)
- [ ] RPO target defined (e.g., 1 hour max)
- [ ] Backup strategy documented (frequency, retention)
- [ ] Backup testing completed (monthly)
- [ ] Failover procedures documented
- [ ] Annual disaster recovery drill completed (full system recovery test)
- [ ] DR plan approved and communicated

**Key Elements:**
```
Cloud Resilience Architecture:
├─ Availability
│  ├─ Multi-AZ deployment (minimum 2 AZs)
│  ├─ Load balancing across AZs
│  └─ Auto-scaling configured
├─ Backup Strategy
│  ├─ Database: Automated daily, retention 30 days, multi-region
│  ├─ File storage: Versioning enabled, replication
│  └─ Configuration: Infrastructure-as-Code versioned in Git
├─ Disaster Recovery
│  ├─ Secondary region identifiable
│  ├─ Failover scripts tested
│  ├─ RTO: 4 hours (or defined)
│  └─ RPO: 1 hour (or defined)
└─ Testing
   ├─ Monthly backup restoration test
   ├─ Quarterly failover drill
   └─ Annual full DR exercise
```

---

## 🔷 NEW DOMAIN 5: DEVSECOPS (DEV)

**Alignment:** ISO 27001 A.8.19 (Change), A.8.25 (Dev/Test separation)  
**Standards:** OWASP SAMM, NIST SSDF, SLSA Framework  
**Owner:** Engineering Lead / Application Security Lead  
**Applicability:** All

---

### EATGF-DEV-SDLC-01: Secure Software Development Lifecycle

| Field | Value |
|-------|-------|
| **Control Title** | Secure Software Development Lifecycle (Secure SDLC) |
| **Control Description** | All software development follows secure SDLC practices: threat modeling, secure coding standards, peer review, security testing in each phase. |
| **Governance Domain** | DEV |
| **Control Type** | Preventive |
| **COBIT Equivalent** | BAI03 (Service configuration), BAI06 (Change) |
| **ISO 27001 Mapping** | A.8.19 (Change management), A.8.9 (Access control in development) |
| **OWASP SAMM** | Design / Implementation / Verification maturity levels |
| **Evidence Required** | SDLC policy, threat modeling examples, code review logs, security testing results |
| **Control Owner** | Engineering Lead / CISO |
| **Evidence Owner** | Development Team |
| **Review Frequency** | Per release |
| **Applicability** | All |

**Evidence Checklist:**
- [ ] SDLC process documented with security phases
- [ ] Threat modeling performed for critical systems
- [ ] Secure coding standards published (OWASP Top 10)
- [ ] Code review mandatory before merge (GitHub protected branches)
- [ ] Security testing checklist per phase (design/code/test/release)
- [ ] Security training for developers completed
- [ ] SAST/DAST integrated into CI/CD
- [ ] Critical vulnerabilities blocked from production

**Key SDLC Phases:**
```
Secure SDLC Process:
├─ DESIGN
│  ├─ Threat modeling (STRIDE/DFD)
│  ├─ Security architecture review
│  └─ Data flow analysis
├─ DEVELOPMENT
│  ├─ Secure coding guidelines adherence
│  ├─ Peer code review (security-focused)
│  └─ Static analysis (SAST) - pre-commit
├─ TESTING
│  ├─ Unit test with security cases
│  ├─ Integration testing (including security)
│  ├─ Dynamic testing (DAST) - pre-release
│  └─ Penetration testing (critical systems)
├─ DEPLOYMENT
│  ├─ Security approval gate
│  ├─ Deployment verification
│  └─ Post-deployment monitoring
└─ MONITORING
   ├─ Runtime security monitoring
   ├─ Incident response
   └─ Lessons learned captured
```

---

### EATGF-DEV-SCAN-01: SAST/DAST/SCA Integration

| Field | Value |
|-------|-------|
| **Control Title** | Automated Security Code Scanning (SAST/DAST/SCA) |
| **Control Description** | All code changes scanned with SAST (static), DAST (dynamic), and SCA (composition). Vulnerability thresholds enforced. |
| **Governance Domain** | DEV |
| **Control Type** | Detective |
| **COBIT Equivalent** | DSS06 (Integrated monitoring) |
| **ISO 27001 Mapping** | A.8.9 (Access & config security), A.12.6 (Vulnerability management) |
| **OWASP** | OWASP Top 10 A01-A10 coverage |
| **Evidence Required** | SAST/DAST/SCA tool configuration, scan reports, critical findings remediation |
| **Control Owner** | Application Security Lead |
| **Evidence Owner** | Security Engineering Team |
| **Review Frequency** | Per commit (continuous), Monthly reports |
| **Applicability** | All |

**Evidence Checklist:**
- [ ] SAST tool integrated in CI/CD (SonarQube/Checkmarx)
- [ ] SAST blocking on CRITICAL findings before merge
- [ ] DAST scanner configured for pre-release testing
- [ ] SCA tool for dependency vulnerabilities (npm audit/safety)
- [ ] Monthly scan summary report
- [ ] Critical/High vulnerabilities remediation SLA tracked
- [ ] False-positive ratio <5% maintained
- [ ] Developer training on vulnerability fixes

**Scanning Coverage:**
```
Code Scanning Pipeline:
├─ SAST (Static Analysis)
│  ├─ Trigger: On every commit
│  ├─ Tools: SonarQube, Checkmarx, or similar
│  ├─ Block on: CRITICAL vulnerabilities only
│  ├─ Coverage target: 70%+ path coverage
│  └─ Time limit: <5 minutes per scan
├─ SCA (Composition Analysis)
│  ├─ Trigger: On dependency change
│  ├─ Tools: npm audit, Safety, Snyk, Dependabot
│  ├─ Block on: CRITICAL vulns in direct dependencies
│  ├─ Known vulnerabilities: Update or exception required
│  └─ License compliance: Check enabled
├─ DAST (Dynamic Analysis)
│  ├─ Trigger: Pre-release (staging environment)
│  ├─ Tools: OWASP ZAP, Burp Suite automation
│  ├─ Scope: All public APIs, web interfaces
│  ├─ Time: Nightly + pre-release
│  └─ Block on: CRITICAL findings
└─ Metrics
   ├─ Scan success rate: >99%
   ├─ False-positive rate: <5%
   └─ Remediation time: <7 days for Critical
```

---

### EATGF-DEV-SUP-01: Software Supply Chain & SBOM Management

| Field | Value |
|-------|-------|
| **Control Title** | Software Supply Chain Security & SBOM |
| **Control Description** | All software components tracked via SBOM (Software Bill of Materials). Dependency vulnerabilities assessed. Build artifacts signed and verified. |
| **Governance Domain** | DEV |
| **Control Type** | Preventive |
| **COBIT Equivalent** | BAI06 (Change) + APO13 (Security) |
| **ISO 27001 Mapping** | A.8.19 (Change management), A.12.1 (Requirement analysis) |
| **SLSA Framework** | Levels 1-3 (Build security) |
| **NIST SSDF** | PO / PS / PO (Practice implementation) |
| **Evidence Required** | SBOM for each release, signed artifacts, dependency scan results |
| **Control Owner** | Engineering Lead / DevOps Lead |
| **Evidence Owner** | Build & Release Team |
| **Review Frequency** | Per release |
| **Applicability** | All |

**Evidence Checklist:**
- [ ] SBOM generated for each release (CycloneDX/SPDX format)
- [ ] Dependency vulnerability scanning (npm audit, pip check)
- [ ] Artifact signing (Docker image signatures, code signing)
- [ ] Provenance tracking (where dependencies came from)
- [ ] Build environment hardened (no root, immutable)
- [ ] Artifact repository access controlled (pull-only operations)
- [ ] Supply chain risk assessment documented
- [ ] Incident response for compromised dependencies

**Supply Chain Security:**
```
SBOM & Supply Chain:
├─ Bill of Materials
│  ├─ Direct dependencies listed
│  ├─ Transitive dependencies included
│  ├─ Version pinning enforced
│  └─ License compliance checked
├─ Artifact Security
│  ├─ Build: Immutable, signed
│  ├─ Storage: Access controlled (repo auth)
│  ├─ Distribution: Signed verification
│  └─ Retention: 1+ year for critical builds
├─ Dependency Monitoring
│  ├─ Vulnerability scanner continuous
│  ├─ Alert on new CVEs in dependencies
│  ├─ Auto-update PRs for patches
│  └─ Manual review for major upgrades
└─ Incident Response
   ├─ Compromised dependency protocol
   ├─ Rapid response (<24 hours)
   └─ Communication plan to customers
```

---

### EATGF-DEV-CI-01: CI/CD Pipeline Integrity & Automation Security

| Field | Value |
|-------|-------|
| **Control Title** | CI/CD Pipeline Integrity & Security |
| **Control Description** | CI/CD pipeline protected: only authorized changes deployed, all stages logged, rollback capability, automated testing enforced. |
| **Governance Domain** | DEV |
| **Control Type** | Preventive |
| **COBIT Equivalent** | BAI06 (System change control) |
| **ISO 27001 Mapping** | A.8.19 (Change management), A.8.25 (Dev/test/prod separation) |
| **Evidence Required** | CI/CD configuration, pipeline logs, approval records, test results |
| **Control Owner** | DevOps Lead |
| **Evidence Owner** | Development Operations Team |
| **Review Frequency** | Monthly audit, per change |
| **Applicability** | All |

**Evidence Checklist:**
- [ ] CI/CD pipeline documented (GitHub Actions/GitLab CI/Jenkins)
- [ ] Automated tests required before deployment
- [ ] Code review approval required before merge (GitHub CODEOWNERS)
- [ ] Security scanning gates (SAST/DAST) blocking critical findings
- [ ] Staging environment deployment before production
- [ ] Rollback capability tested quarterly
- [ ] Pipeline secrets managed securely (no hardcoded credentials)
- [ ] Audit logging enabled for all pipeline steps

**CI/CD Pipeline:**
```
Pipeline Stages:
├─ COMMIT
│  ├─ Pre-commit hooks (lint, secrets scan)
│  ├─ Branch protection enabled
│  └─ Signed commits required (GPG)
├─ BUILD
│  ├─ Automated tests (unit, integration)
│  ├─ SAST + SCA scanning
│  ├─ Code quality gates (coverage, complexity)
│  └─ Artifact creation & signing
├─ STAGE
│  ├─ Deploy to staging environment
│  ├─ DAST scanning
│  ├─ Performance testing
│  └─ Manual acceptance testing
├─ RELEASE
│  ├─ Security approval gate
│  ├─ Production deployment
│  ├─ Rollback readiness verified
│  └─ Monitoring setup
└─ MONITORING
   ├─ Error rate tracking
   ├─ Performance metrics
   ├─ Security incidents
   └─ Automatic rollback if critical
```

---

## 🔷 NEW DOMAIN 6: DATA PRIVACY (DATA)

**Alignment:** ISO 27001 A.5.31-32, GDPR Articles 5/25/30, CCPA/CASL  
**Standards:** ISO 27701 (Privacy extension), NIST Privacy Framework  
**Owner:** Chief Data Officer / Privacy Officer  
**Applicability:** All (conditional on data types)

---

### EATGF-DATA-PRIV-01: Data Protection Impact Assessment (DPIA)

| Field | Value |
|-------|-------|
| **Control Title** | Data Protection Impact Assessment (DPIA) for High-Risk Processing |
| **Control Description** | All high-risk data processing activities undergo Data Protection Impact Assessment (DPIA). Assessments document risks, mitigation, and stakeholder consultation. |
| **Governance Domain** | DATA |
| **Control Type** | Preventive |
| **COBIT Equivalent** | APO12 (Risk management) |
| **ISO 27001 Mapping** | A.5.31 (Identification of applicable law), A.5.32 (Data protection compliance) |
| **ISO 27701** | 8.1 (General requirements for privacy controls) |
| **GDPR** | Article 35 (Data Protection Impact Assessment) |
| **Evidence Required** | DPIA template, completed assessments, risk analysis, mitigation plans |
| **Control Owner** | Chief Data Officer / Data Privacy Officer |
| **Evidence Owner** | Privacy Team |
| **Review Frequency** | Per new processing activity / Annual for existing |
| **Applicability** | All (mandatory if processing PII/sensitive data) |

**Evidence Checklist:**
- [ ] DPIA process documented and approved
- [ ] DPIA template created (cover processing purpose, lawfulness, necessity, proportionality)
- [ ] Risk assessment for data handling (unauthorized access, loss, etc.)
- [ ] Mitigation controls mapped to identified risks
- [ ] Data Controllers & Processors consulted
- [ ] Regulatory authority consultation if residual risks remain
- [ ] DPIAs tracked in central register
- [ ] Annual review of high-risk DPIAs

**DPIA Components:**
```
Data Protection Impact Assessment:
├─ Processing Description
│  ├─ Purpose (why collecting/processing)
│  ├─ Data categories (email, phone, SSN, biometric, etc.)
│  ├─ Data subject categories
│  └─ Retention period
├─ Necessity & Proportionality
│  ├─ Legal basis for processing (consent/contract/legal/legitimate interest)
│  ├─ Necessity: Is processing necessary for purpose?
│  └─ Proportionality: Does benefit justify data collection?
├─ Risk Assessment
│  ├─ Risk: Unauthorised access
│  │  └─ Probability / Impact / Mitigation
│  ├─ Risk: Data loss or corruption
│  │  └─ Probability / Impact / Mitigation
│  └─ Risk: Disclosure to third parties
│     └─ Probability / Impact / Mitigation
├─ Mitigation Measures
│  ├─ Technical (encryption, access control)
│  ├─ Organizational (training, audit)
│  └─ Contractual (DPA with processors)
└─ Conclusion
   ├─ Residual risk acceptable?
   ├─ Regulatory consultation required?
   └─ Approved by DPO/CISO/Business owner
```

---

### EATGF-DATA-RET-01: Data Retention & Lifecycle Governance

| Field | Value |
|-------|-------|
| **Control Title** | Data Retention Schedule & Lifecycle Management |
| **Control Description** | Data retention schedules defined per data type and regulatory requirement. Automated retention enforcement and secure deletion. Regular compliance reviews. |
| **Governance Domain** | DATA |
| **Control Type** | Preventive |
| **COBIT Equivalent** | DSS01 (Service continuity) + APO12 (Risk) |
| **ISO 27001 Mapping** | A.5.32 (Data protection compliance), A.8.26 (Data deletion) |
| **GDPR** | Article 5 (Storage limitation), Article 17 (Right to erasure) |
| **Evidence Required** | Retention schedule, deletion logs, compliance verification |
| **Control Owner** | Chief Data Officer |
| **Evidence Owner** | Data Governance Team |
| **Review Frequency** | Annual retention review + continuous enforcement |
| **Applicability** | All (if any personal/sensitive data) |

**Evidence Checklist:**
- [ ] Data retention schedule documented (all data types)
- [ ] Retention periods based on: legal requirement, business need, regulatory standard
- [ ] Automated deletion process implemented (jobs/rules)
- [ ] Backup retention aligned with production retention
- [ ] Right-to-erasure process documented for individuals
- [ ] Monthly deletion verification logs
- [ ] Annual compliance review of retention adherence
- [ ] Exception process for legal holds documented

**Retention Schedule Template:**
```
Data Retention Matrix:
├─ Customer Data
│  ├─ Customer account info: Retention period + 12 months deletion grace
│  ├─ Transaction history: 7 years (tax requirement)
│  ├─ Communication logs: 3 years
│  └─ Deleted customer data: Secure deletion within 30 days
├─ Operational Data
│  ├─ System logs: 12 months (current) + 7 years archive
│  ├─ Access logs (audit): 7 years
│  ├─ Backup archives: 1 year
│  └─ Configuration backup: 1 year
├─ Financial Data
│  ├─ Transaction records: 7 years
│  ├─ Financial reports: 7 years
│  └─ Audit records: 7 years
└─ Deletion Process
   ├─ Data marked for deletion: Logical deletion first
   ├─ Retention period expires: Automated job initiates deletion
   ├─ Verification: Backup verified as deleted
   └─ Compliance: Monthly audit of deletions
```

---

### EATGF-DATA-MIN-01: Data Minimization & Purpose Limitation

| Field | Value |
|-------|-------|
| **Control Title** | Data Minimization & Purpose Limitation Enforcement |
| **Control Description** | Data collection limited to necessary for stated purpose. Regular audits verify only required data collected. Purpose limitation enforced in code/policies. |
| **Governance Domain** | DATA |
| **Control Type** | Preventive |
| **ISO 27001 Mapping** | A.5.31-32 (Data protection), A.5.32 (Data protection as per principle) |
| **GDPR** | Article 5 (Data minimization principle) |
| **Evidence Required** | Data minimization policy, vendor compliance audits, code review findings |
| **Control Owner** | Chief Data Officer / Privacy Officer |
| **Evidence Owner** | Privacy Team |
| **Review Frequency** | Annual audit + quarterly random sample review |
| **Applicability** | All (if collecting any personal data) |

**Evidence Checklist:**
- [ ] Data minimization policy documented
- [ ] Customer-facing forms/APIs collect only necessary fields
- [ ] Data science/analytics teams restricted to non-PII or clearly consented PII
- [ ] Periodic audit of data collected vs. stated purpose (quarterly sample)
- [ ] Access control restricts employees to minimum necessary data (need-to-know)
- [ ] Data sharing with third parties explicitly approved by legal/DPO
- [ ] Training on data minimization for data handlers

**Data Minimization Approach:**
```
Purpose Limitation Framework:
├─ Collection
│  ├─ Purpose stated clearly to data subject
│  ├─ Only necessary fields collected
│  ├─ Explicit consent obtained for non-essential
│  └─ Code review ensures adherence
├─ Usage
│  ├─ Production data: Only for stated purpose
│  ├─ Non-production (dev/test): Avoid real PII (synthetic data)
│  ├─ Analytics: Anonymize/pseudonymize before access
│  └─ Third parties: Explicit contract with purpose limitations
├─ Retention
│  ├─ Retention period tied to purpose
│  ├─ Deletion when purpose ceases
│  └─ Exception: Legal hold clearly documented
└─ Enforcement
   ├─ Access control: Restrict to necessary employees
   ├─ Code scanning: Detect unintended PII transmission
   ├─ Audit: Quarterly sample of data usage
   └─ Incident: Unauthorized usage → investigation → remediation
```

---

## 🔷 NEW DOMAIN 7: BUSINESS CONTINUITY & DISASTER RECOVERY (BCP)

**Alignment:** ISO 27001 A.5.29-30, ISO 22301, NFPA 1600  
**Standards:** ISO 27001 A.8.24-26, ITIL Service Continuity  
**Owner:** Chief Resilience Officer / Business Continuity Manager  
**Applicability:** SaaS / Enterprise

---

### EATGF-BCP-PLAN-01: Business Continuity & Disaster Recovery Planning

| Field | Value |
|-------|-------|
| **Control Title** | Business Continuity & Disaster Recovery Planning |
| **Control Description** | Organization maintains comprehensive BC/DR plans covering all critical systems. Plans include: recovery procedures, communication, alternative facilities, roles/responsibilities. |
| **Governance Domain** | BCP |
| **Control Type** | Preventive |
| **COBIT Equivalent** | DSS03 (Service continuity) + BAI06 (Enterprise change enablement) |
| **ISO 27001 Mapping** | A.5.29 (Information security incident response), A.5.30 (Continuity of operations) |
| **ISO 22301** | 8.1-8.5 (Business continuity management system) |
| **Evidence Required** | BC/DR plan document, system recovery procedures, contact lists, communication templates |
| **Control Owner** | Chief Resilience Officer / BC Manager |
| **Evidence Owner** | Business Continuity Team |
| **Review Frequency** | Annual plan review + per material change |
| **Applicability** | SaaS / Enterprise |

**Evidence Checklist:**
- [ ] BC/DR plan document (10+ pages) comprehensive
- [ ] Critical systems identified and prioritized (RTO/RPO per system)
- [ ] Recovery procedures detailed for each critical system
- [ ] Alternative sites/facilities identified (hot/warm/cold standby)
- [ ] Communication plan (internal/external/customer notification)
- [ ] Contact lists (roles, phone numbers, escalation path)
- [ ] Recovery team assigned with specific roles
- [ ] Plan approved by executive leadership
- [ ] Annual plan review completed

**BC/DR Plan Structure:**
```
Business Continuity Plan:
├─ INTRODUCTION
│  ├─ Purpose & scope
│  ├─ Critical systems priority
│  └─ Recovery objectives (RTO/RPO)
├─ ORGANIZATION
│  ├─ Recovery team structure
│  ├─ Roles & responsibilities
│  └─ Contact information (current, tested quarterly)
├─ RECOVERY PROCEDURES
│  ├─ System 1: Application Server
│  │  ├─ RTO: 2 hours
│  │  ├─ Recovery steps
│  │  └─ Testing frequency
│  ├─ System 2: Database
│  │  ├─ RTO: 1 hour
│  │  ├─ Recovery steps
│  │  └─ Testing frequency
│  └─ ... (all critical systems)
├─ COMMUNICATION
│  ├─ Internal notification (employees)
│  ├─ Customer notification (templates)
│  ├─ Regulatory notification (if required)
│  └─ Media response (if public incident)
├─ ALTERNATIVE FACILITIES
│  ├─ Hot site: Fully operational backup facility
│  ├─ Warm site: Partially operational
│  └─ Cold site: Equipment available but not running
└─ TESTING & MAINTENANCE
   ├─ Annual full-scale test
   ├─ Semi-annual tabletop exercise
   └─ Quarterly document review
```

---

### EATGF-BCP-TEST-01: Business Continuity Testing & Validation

| Field | Value |
|-------|-------|
| **Control Title** | Business Continuity Testing & Validation |
| **Control Description** | BC/DR plans tested annually (full exercise) and semi-annually (tabletop). Test results documented, gaps identified, lessons learned captured. |
| **Governance Domain** | BCP |
| **Control Type** | Detective |
| **COBIT Equivalent** | MEA01 (Monitoring) + MEA03 (Monitoring compliance) |
| **ISO 27001 Mapping** | A.8.24 (Testing procedures), A.8.25 (Redundancy) |
| **Evidence Required** | BC test plan, test results, gap findings, corrective actions |
| **Control Owner** | Chief Resilience Officer / BC Manager |
| **Evidence Owner** | Business Continuity Team |
| **Review Frequency** | Annual (full test) + Semi-annual (tabletop) |
| **Applicability** | SaaS / Enterprise |

**Evidence Checklist:**
- [ ] Annual BC/DR test plan documented (scope, systems, procedures)
- [ ] Full-scale recovery test completed (actual system failover)
- [ ] Test results documented (success/failure, time to recover)
- [ ] Lessons learned meeting held post-test
- [ ] Gaps identified and tracked to closure
- [ ] Tabletop exercise completed (semi-annual)
- [ ] RTO/RPO validation against test results
- [ ] Improvements incorporated into next year's plan

**Testing Types:**
```
BC/DR Testing Program:
├─ TABLETOP EXERCISE (Semi-Annual)
│  ├─ Scenario: [earthquake/data center outage/cyberattack]
│  ├─ Participants: Recovery team, management
│  ├─ Duration: 2-4 hours
│  ├─ Objectives: Test knowledge, identify gaps
│  └─ Output: Findings, improvement list
├─ PARTIAL TEST (Quarterly)
│  ├─ Test 1-2 critical systems
│  ├─ Simulated failure + recovery
│  ├─ Measure actual RTO
│  └─ Validate backup functionality
└─ FULL-SCALE TEST (Annual)
   ├─ All critical systems involved
   ├─ Actual failover to alternate facility
   ├─ Test communications & notifications
   ├─ Measure RTO/RPO achievement
   └─ Validate all recovery procedures
```

---

### EATGF-BCP-RTO-01: Recovery Time Objective (RTO) & Recovery Point Objective (RPO) Management

| Field | Value |
|-------|-------|
| **Control Title** | RTO/RPO Definition, Achievement & Monitoring |
| **Control Description** | RTO (max tolerable downtime) and RPO (max acceptable data loss) defined per system. Monitoring validates achievement. Alerts on SLA breach. |
| **Governance Domain** | BCP / DSS |
| **Control Type** | Detective |
| **COBIT Equivalent** | MEA01 (Monitoring) |
| **ISO 27001 Mapping** | A.8.26 (Recovery planning and restoration), 9.1 (Monitoring) |
| **Evidence Required** | RTO/RPO targets per system, monitoring dashboard, SLA compliance |
| **Control Owner** | Chief Technology Officer / Ops Lead |
| **Evidence Owner** | Operations Team |
| **Review Frequency** | Monthly monitoring + Annual target review |
| **Applicability** | All (critical systems mandatory) |

**Evidence Checklist:**
- [ ] RTO targets defined per system (max hours downtime acceptable)
- [ ] RPO targets defined per system (max hours data loss acceptable)
- [ ] Backup frequency aligns with RPO (e.g., hourly backups for 1-hour RPO)
- [ ] RTO/RPO dashboard live (automated monitoring)
- [ ] Monthly SLA compliance reports
- [ ] Breach notifications and root cause analysis
- [ ] Improvement actions tracked
- [ ] Test verification that RTO/RPO targets achievable

**RTO/RPO Matrix:**
```
System Recovery Targets:

CRITICAL SYSTEMS:
├─ Customer API
│  ├─ RTO: 1 hour (max downtime)
│  ├─ RPO: 15 minutes (max data loss)
│  └─ Backup: Every 5 minutes
├─ Database (customer data)
│  ├─ RTO: 2 hours
│  ├─ RPO: 30 minutes
│  └─ Backup: Every 10 minutes
├─ Billing System
│  ├─ RTO: 4 hours
│  ├─ RPO: 1 hour
│  └─ Backup: Every 15 minutes
└─ Web Application
   ├─ RTO: 4 hours
   ├─ RPO: N/A (stateless)
   └─ Backup: Continuous deployment ready

MONITORING:
├─ Backup completion time: Alert if >target
├─ Backup verification: Automated restoration test weekly
├─ Failover readiness: Alert if failover not current
└─ Monthly report: SLA compliance %
```

---

## 📊 PHASE 1.5 SUMMARY TABLE

**New Controls Being Added:**

| Domain | Control ID | Title | Type | Applicability |
|--------|-----------|-------|------|---|
| **CLD** | EATGF-CLD-ARCH-01 | Cloud Architecture & Design | Preventive | SaaS/Ent |
| **CLD** | EATGF-CLD-SEC-01 | Cloud Security & Compliance | Preventive | All |
| **CLD** | EATGF-CLD-MON-01 | Cloud Cost/Performance Monitoring | Detective | All |
| **CLD** | EATGF-CLD-RES-01 | Cloud Resilience & DR | Preventive | SaaS/Ent |
| **DEV** | EATGF-DEV-SDLC-01 | Secure SDLC | Preventive | All |
| **DEV** | EATGF-DEV-SCAN-01 | SAST/DAST/SCA Integration | Detective | All |
| **DEV** | EATGF-DEV-SUP-01 | Software Supply Chain & SBOM | Preventive | All |
| **DEV** | EATGF-DEV-CI-01 | CI/CD Pipeline Integrity | Preventive | All |
| **DATA** | EATGF-DATA-PRIV-01 | Data Protection Impact Assessment | Preventive | All* |
| **DATA** | EATGF-DATA-RET-01 | Data Retention & Lifecycle | Preventive | All* |
| **DATA** | EATGF-DATA-MIN-01 | Data Minimization | Preventive | All* |
| **BCP** | EATGF-BCP-PLAN-01 | BC/DR Planning | Preventive | SaaS/Ent |
| **BCP** | EATGF-BCP-TEST-01 | BC/DR Testing | Detective | SaaS/Ent |
| **BCP** | EATGF-BCP-RTO-01 | RTO/RPO Management | Detective | All |

**Total New Controls:** 14  
**Previous Total:** 21  
**New Total:** 35  
**Target Range:** 35-45 (ON TRACK) ✅

---

## 🎯 APPLICABILITY NOTES

- **All**: Applies to Startup/SaaS/Enterprise
- **SaaS/Ent**: Applies to SaaS & Enterprise (not Startup <10 people)
- **All***: Applies only if processing personal/sensitive data

---

## 📅 NEXT STEPS AFTER PHASE 1.5 COMPLETION

1. **Integrate new controls into MCM** (update main document)
2. **Update Framework Mappings** (add cloud/dev/data/bcp sections)
3. **Update SoA Template** (add 14 new controls with examples)
4. **Update Governance Charter** (add new governance domains)
5. **Freeze MCM v1.0** (ready for ISMS/AIMS/Audit layer)
6. **Proceed to Phase 2** (ISMS Manual, AIMS Manual, Internal Audit)

---

**Framework:** EATGF v0.9 → v1.0  
**Phase 1.5 Status:** 🔨 **READY FOR IMPLEMENTATION**  
**Target Completion:** This week (Feb 13-17, 2026)  
**Output:** Integrated MCM v1.0 (35 controls)
