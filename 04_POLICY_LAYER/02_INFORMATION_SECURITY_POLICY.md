# 02_INFORMATION_SECURITY_POLICY

| Field          | Value                                                                   |
| -------------- | ----------------------------------------------------------------------- |
| Document Type  | Policy                                                                  |
| Version        | 2.0                                                                     |
| Classification | Controlled                                                              |
| Effective Date | 2026-02-14                                                              |
| Authority      | Chief Information Security Officer                                      |
| EATGF Layer    | 04_POLICY_LAYER                                                         |
| MCM Reference  | EATGF-APO-SEC-01, EATGF-DSS-SEC-01, EATGF-DSS-ENC-01, EATGF-DSS-VULN-01 |

---

## Purpose

This policy establishes information security requirements for protecting confidentiality, integrity, and availability of organizational information assets. The policy applies to all employees, contractors, third parties, systems, and data across all business units and geographies. Non-compliance triggers disciplinary action up to termination and legal liability for data breaches.

## Architectural Position

This policy operates within **04_POLICY_LAYER** as the primary security governance document.

- **Upstream dependency:** Governance Charter (01_GOVERNANCE_CHARTER.md) establishes authority structure; Baseline Declaration establishes security as foundational control
- **Downstream usage:** Operationalized through ISO 27001:2022 ISMS procedures; enforced through data protection procedures, incident response, and access control procedures
- **Cross-layer reference:** Maps to EATGF security controls in Layer 02 (APO-SEC domain, DSS security controls for confidentiality/encryption/vulnerability management)

## Governance Principles

1. **Confidentiality, Integrity, and Availability (CIA)** – Information asset protection through access control, encryption, and availability assurance mechanisms
2. **Defense in Depth** – Multiple security layers (technical, process, organizational) prevent unauthorized access
3. **Risk-Based Security** – Security controls aligned to asset criticality and threat environments
4. **Regulatory Compliance** – Policy implements GDPR, CCPA, HIPAA, and other regulatory requirements
5. **User Accountability** – All users held accountable for security compliance; disciplinary framework for violations

## Technical Implementation

### Information Asset Classification

All information assets classified according to:

| Classification   | Definition                                      | Protection Level    |
| ---------------- | ----------------------------------------------- | ------------------- |
| **Public**       | Information approved for public disclosure      | Basic protection    |
| **Internal**     | Information intended for internal use only      | Standard protection |
| **Confidential** | Sensitive business or personal information      | Enhanced protection |
| **Restricted**   | Highly sensitive (trade secrets, personal data) | Maximum protection  |

Classification determines encryption, access control, retention, and disposal requirements.

### Access Control Requirements

**Role-Based Access Control (RBAC):**

- All systems implement RBAC with predefined roles aligned to job functions
- Principle of Least Privilege applied: users granted minimum access for job performance
- Segregation of Duties enforced: authorization, approval, and fulfillment not performed by same person
- Annual access review performed by system owner to verify appropriateness

**Authentication:**

- Multi-Factor Authentication (MFA) required for:
  - All administrative/privileged access
  - All remote/VPN access
  - Any access to Confidential or Restricted information
  - Third-party access to organizational systems
- Password policy compliance verified through technical controls
- Service accounts prohibited from interactive login; exceptions require CISO approval

### Data Protection Requirements

**Encryption Standards:**

- **At Rest:** AES-256 for all Confidential and Restricted data; AES-128 minimum for Internal data
- **In Transit:** TLS 1.2 or higher for all data transmission; DTLS for wireless protocols
- End-to-end encryption where data passes through untrusted networks
- Encryption key management via dedicated key management service (KMS)

**Data Retention and Disposal:**

- Retention periods defined per regulatory requirements and business need
- Automated purge procedures for data exceeding retention period
- Secure disposal procedures for physical media (certified shredding, degaussing, or destruction)
- Disposal documented with certificate of destruction; accessible to audit

**Data Subject Rights:**

- 30-day response requirement for Data Subject Access Requests (DSAR)
- Right to erasure honored where legally permitted
- Data portability provided in machine-readable format where required
- Right to object to processing honored per GDPR Article 21

### Incident Management

** NOTE ON SLA CONTEXT:** The timelines below refer to INCIDENT ESCALATION and NOTIFICATION, which is different from VULNERABILITY REMEDIATION SLA defined in [VULNERABILITY_REMEDIATION_TERMINOLOGY.md](../02_CONTROL_ARCHITECTURE/VULNERABILITY_REMEDIATION_TERMINOLOGY.md). CVE patching follows a separate 24-hour end-to-end SLA.

**Breach Notification Requirement:**

- Critical incidents reported to CISO within 1 hour (escalation timeline)
- Regulatory authorities notified within 72 hours per GDPR (or applicable regulation)
- Affected data subjects notified per regulatory requirements

**Incident Severity Classification:**

| Level                  | Criteria                                              | Timeline         | Escalation       |
| ---------------------- | ----------------------------------------------------- | ---------------- | ---------------- |
| **Level 1 (Critical)** | Major data breach, extended outage, external attack   | 1 hour           | CISO, CEO, Board |
| **Level 2 (High)**     | Significant security event, partial outage \| 4 hours | CISO, CFO, Legal |
| **Level 3 (Medium)**   | Authentication failure, failed security scan          | 24 hours         | Security team    |
| **Level 4 (Low)**      | Informational issue, policy deviation                 | 5 days           | Domain team      |

**Root Cause Analysis (RCA):**

- Mandatory for Level 1-2 incidents
- Completed within 10 days of incident
- RCA report includes: timeline, root cause, contributing factors, corrective actions, preventive measures
- RCA approved by CISO prior to closure

**Incident Reporting:**

- Monthly incident report to Governance Council
- Quarterly incident and trend analysis to executive steering committee
- Annual incident report to Board

### Third-Party Security Management

**Contractual Requirements:**

- Non-Disclosure Agreement (NDA) required before access to any proprietary information
- Data Protection Agreement specify regulatory compliance requirements
- Right to audit clause permits security assessment by organization
- Insurance requirements: minimum $5M cyber liability coverage
- Breach liability clause: third party liable for data breach resulting from third-party negligence

**Third-Party Assessment:**

- Annual security assessment conducted (on-site or questionnaire-based)
- Critical vendor assessed before onboarding; repeated annually
- Assessment results used for risk determination
- High-risk vendors under enhanced monitoring

**Data Handling Requirements:**

- Third parties restricted to minimum data access necessary
- Prohibited from subcontracting without written approval
- Data returned or destroyed upon contract termination
- Compliance verified through contractual audit rights

### Vulnerability Management

**Vulnerability Scanning:**

- Automated scanning of all internet-facing systems minimum weekly
- Internal network scanning minimum monthly
- Vulnerability scan results reviewed by security team within 5 days
- Critical vulnerabilities remediated within 24 hours end-to-end (per VULNERABILITY_REMEDIATION_TERMINOLOGY.md)

**Patch Management:**

- Critical patches validated and deployed within 4 hours
- High patches applied within 7 days
- Standard patches applied within 30 days
- Emergency out-of-cycle patching for zero-day exploits
- Reference: [VULNERABILITY_REMEDIATION_TERMINOLOGY.md](../02_CONTROL_ARCHITECTURE/VULNERABILITY_REMEDIATION_TERMINOLOGY.md)

## Control Mapping

### ISO 27001:2022 Alignment

Policy implements ISO 27001 controls:

- **A.5.1** – Policies for information security (this document)
- **A.8.1** – User access management (access control requirements)
- **A.8.2** – User responsibilities (training and compliance)
- **A.8.3** – Password management (authentication requirements)
- **A.10.1** – Cryptography (encryption requirements)
- **A.12.2** – Change management (vulnerability and patch management)
- **A.13.1** – Network security (data in transit protection)

### GDPR Alignment

Policy implements GDPR articles:

- **Article 32** – Security of processing (encryption, access control, incident response)
- **Article 33** – Breach notification to supervisory authority (1-hour internal, 72-hour external)
- **Article 34** – Breach notification to data subjects (required where high risk)
- **Article 35** – DPIA requirements (data classification determines assessment triggers)

### CCPA Alignment

Policy supports CCPA compliance:

- **Section 1798.100** – Consumer right to know; DSAR 30-day response
- **Section 1798.105** – Consumer right to delete; erasure procedures
- **Section 1798.120** – Consumer right to portability; machine-readable format

### NIST Cybersecurity Framework

Policy aligns with NIST functions:

- **Protect (PR)** – Access control, encryption, user training
- **Respond (RS)** – Incident classification, breach notification, RCA procedures

## Developer Checklist

Before deploying information security policy:

- [ ] User classification framework documented (Public/Internal/Confidential/Restricted)
- [ ] RBAC implemented on all systems with role definitions documented
- [ ] MFA configured for all administrative and sensitive data access
- [ ] Encryption at rest (AES-256) enabled for Confidential and Restricted data
- [ ] TLS 1.2+ configured for all data in transit protection
- [ ] Data retention schedule documented with regulatory justification
- [ ] Automated purge procedures configured for expired data
- [ ] Secure disposal procedures documented with audit capability
- [ ] Incident classification levels defined and communicated
- [ ] Incident response procedures including 1-hour notification requirement established
- [ ] Vulnerability scanning schedule documented (weekly external, monthly internal)
- [ ] Patch management SLAs established (4 hours critical, 7 days high, 30 days standard)
- [ ] Vulnerability remediation tracking system operational
- [ ] All employees completed information security training
- [ ] Third-party contractual requirements documented (NDA, DPA, insurance, audit rights)
- [ ] Third-party security assessment procedure established with scoring methodology

## Governance Implications

### Security Ownership and Authority

- **Chief Information Security Officer:** Policy ownership; incident escalation authority; security exception approval
- **Information Security Team:** Control implementation, vulnerability management, incident response execution
- **Business Unit Heads:** Departmental compliance accountability; user training oversight
- **Individual Users:** Accountability for personal security behavior; policy violations subject to discipline

### Non-Compliance and Enforcement

- Policy violations escalate per Governance Charter escalation procedure
- First-time violations: documented warning and retraining
- Repeated violations: disciplinary action (suspension, termination)
- Data breach resulting from policy violation: personal liability exposure
- Third-party violations: contract termination authority; law enforcement referral for criminal cases

### Incident Response Authority

- Level 1-2 incidents trigger executive and board notification
- CISO determines incident classification and escalation
- RCA authority rests with CISO; approved by executive steering committee
- Regulatory authority notification via legal counsel coordination
- Executive steering committee approves remediation strategy for material breaches

### Policy Amendment Process

Security policy amendment requires:

- CISO proposal with security justification
- Security steering committee review (minimum 2 weeks)
- CTO and CFO approval for control scope changes
- 30-day notice to all personnel before effective date
- Training updated prior to enforcement

## Official References

- **ISO/IEC 27001:2022** – Information Security Management Systems (ISO, 2022)
- **ISO/IEC 27002:2022** – Code of practice for information security controls (ISO, 2022)
- **NIST Special Publication 800-53:Revision 5** – Security and Privacy Controls for Information Systems (NIST, 2020)
- **Regulation (EU) 2016/679** – General Data Protection Regulation (GDPR) (EU, 2016)
- **California Consumer Privacy Act (CCPA)** – California Civil Code Section 1798.100 et seq. (California, 2018)
- **NIST Cybersecurity Framework 2.0** – Information Security Management (NIST, 2024)
