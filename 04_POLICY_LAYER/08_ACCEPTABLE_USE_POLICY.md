# 08_ACCEPTABLE_USE_POLICY

| Field          | Value                                                                |
| -------------- | -------------------------------------------------------------------- |
| Document Type  | Policy                                                               |
| Version        | 1.0                                                                  |
| Change Type    | Major (Initial)                                                      |
| Classification | Internal                                                             |
| Effective Date | 2026-02-16                                                           |
| Authority      | Chief Information Security Officer and Chief Human Resources Officer |
| EATGF Layer    | 04_POLICY_LAYER                                                      |
| MCM Reference  | EATGF-DSS-SEC-01, EATGF-APO-SEC-01, EATGF-EDM-GOV-01                 |

---

## Purpose

This policy defines acceptable and prohibited uses of organizational systems, data, networks, and computing resources. The policy applies to all employees, contractors, temporary staff, interns, business partners, and authorized external users. The policy prohibits illegal activity, unauthorized access, data theft, intellectual property violation, and harassment. Violations trigger investigation, disciplinary action, and potential legal proceedings. All system usage is monitored and auditable.

## Architectural Position

This policy operates within **04_POLICY_LAYER** as the primary acceptable use governance document.

- **Upstream dependency:** Governance Charter (01_GOVERNANCE_CHARTER.md) establishes authority for acceptable use enforcement; Information Security Policy (02_INFORMATION_SECURITY_POLICY.md) defines protection requirements that acceptable use supports
- **Downstream usage:** Operationalized through system access agreements, acceptable use acknowledgment forms, monitoring procedures, and investigation protocols; enforced through system audit logging, user activity monitoring, and incident investigation
- **Cross-layer reference:** Maps to EATGF control domain APO-POL (policy governance) and DSS-USE (system usage governance), implements MCM controls for system behavior expectations and consequences, works with Incident Response Policy and privacy controls for investigatory procedures

## Governance Principles

1. **Clear Expectations** – Acceptable use requirements defined explicitly; ambiguous policies clarified during onboarding
2. **Consistent Enforcement** – All users held to same standards; disciplinary consequences applied consistently
3. **Monitor and Detect** – System usage monitored and auditable; suspicious activity triggered investigation
4. **Privacy Balanced with Security** – Monitoring conducted with appropriate notice; privacy expectations managed
5. **Legal Alignment** – Prohibited conduct aligned to criminal law, employment law, and intellectual property rights

## Technical Implementation

### Acceptable Use – General Principles

**Users May:**

- Use organizational systems for authorized business purposes
- Access data and systems needed to perform assigned job functions
- Use approved communication tools (email, Slack, Teams, etc.) for business purposes
- Engage in reasonable personal use during breaks (email, web browsing limited duration)
- Report security concerns and suspicious activity without retaliation

**Users Must:**

- Comply with security policies and procedures (password policy, encryption, VPN usage, clean desk)
- Protect access credentials (passwords, tokens, certificates); share credentials only with authorized personnel for legitimate access restoration
- Report suspected compromised credentials or security incidents to IT Security immediately
- Use organizational data only for authorized purposes; data classification honored (public/internal/confidential/restricted)
- Respect intellectual property rights: Do not reproduce, distribute, or use others' copyrighted/trademarked/proprietary work without authorization
- Comply with export control regulations (ITAR, EAR) when handling controlled technical data
- Complete required security awareness training and privacy training annually

### Prohibited Use – Definitions

**Illegal Activity:**

Users are prohibited from engaging in any illegal activity using organizational systems or data. Examples:

- Hacking, unauthorized access, cracking, or exploitation of systems
- Distribution of illegal content (child sexual abuse material, counterfeit goods, stolen property)
- Fraud, embezzlement, theft, extortion, bribery, money laundering
- Violation of trade secret laws (misappropriation, unauthorized disclosure)
- Violation of export control laws (unauthorized export of controlled technology)
- Identity theft, forgery, unauthorized impersonation

**Unauthorized Access and Data Breach:**

Users are prohibited from:

- Accessing systems or data without authorization (using others' credentials, password guessing, exploiting vulnerabilities)
- Accessing data beyond job functions (curiosity audit, competitor research, personal interest)
- Downloading, exfiltrating, or copying data to personal devices or external storage without authorization
- Installing unauthorized software or modifying system configurations
- Circumventing security controls (VPN bypass, firewall bypass, encryption circumvention, MFA bypass)
- Sharing access credentials with unauthorized personnel; credential sharing with authorized personnel permitted only for legitimate access restoration/incident response
- Attempting to escalate privileges (privilege escalation, admin access unauthorized)

**Intellectual Property Violation:**

Users are prohibited from:

- Reproducing copyrighted material (software, published works, photos) without license
- Using trademarked/branded materials without authorization (company logos, product names)
- Distributing proprietary information (trade secrets, business plans, customer lists, financial data) to unauthorized recipients
- Plagiarizing content (passing off others' work as own, inadequate citation)
- Reverse engineering proprietary software without authorization
- Publishing organizational information or source code publicly without authorization

**Data Misuse:**

Users are prohibited from:

- Using personal data for non-business purposes (customer data for personal marketing, employee data for personal research)
- Selling, trading, or commercializing organizational or customer data
- Sharing data beyond intended recipients (data classification boundaries)
- Unauthorized data analysis (employee performance data, customer behavioral data, salary data used without authorization)
- Processing child's personal data (users < 16) without verifiable parental consent where required
- Health data processing without HIPAA authorization/business associate agreement
- Financial data processing without PCI-DSS compliance and authorization

**Harmful Content:**

Users are prohibited from:

- Distribution of malware, viruses, ransomware, spyware, or other malicious software
- Distribution of unsolicited bulk communications (spam, phishing, commercial email without consent)
- Harassment, bullying, intimidation, threats, or abusive language targeting individuals or groups
- Discrimination based on race, ethnicity, religion, sex, gender identity, national origin, age, disability, sexual orientation
- Sexual harassment, inappropriate sexual content, or sexual solicitation
- Obscene, profane, or vulgar content; gratuitous violence or glorification of harm

**Resource Abuse:**

Users are prohibited from:

- Unauthorized cryptocurrency mining using organizational systems
- Unauthorized file sharing services (BitTorrent, peer-to-peer networks, distributed systems)
- Excessive bandwidth usage (video streaming, file uploads, downloads consuming >50% available bandwidth)
- Resource hoarding: Excessive storage, compute, or network resource consumption preventing others from accessing systems
- System disruption: Denial-of-service (DoS) attacks, intentional system crashes, network flooding
- Testing or exploitation of systems without authorization (port scanning, vulnerability scanning, penetration testing)

**Personal Use Restrictions:**

- Business systems not to be used for personal business activities (side businesses, commercial ventures, personal investments)
- Commercial activity prohibited (selling products/services using organizational systems/data/network, affiliate marketing, multi-level marketing)
- Gambling, betting, or wagering activities prohibited
- Religion/political proselytizing or activism limited; advocacy permissible only in designated channels with appropriate disclaimers

### Monitoring and Audit

**System Monitoring Scope:**

Organization reserves right to monitor system usage to ensure compliance with this policy and protect organizational assets. Monitoring includes:

- Email content and attachments (scanned for malware, data loss prevention, policy violation)
- Email metadata (sender, recipient, subject, timestamp, file attachments)
- Web browsing history and destination URLs (category filtering for policy compliance)
- Application usage (which applications launched, duration, resource consumption)
- Network traffic: Source/destination IP, port, data volume (not packet content unless security incident investigation)
- File transfers: Source, destination, file size, file type (content scanning for malware and DLP)
- Login activity: Timestamp, source IP, success/failure, multi-factor authentication verification
- System commands and script execution (for administrative accounts, developers)
- Removable media usage: USB device insertion, CD/DVD access, external drive connections
- Printing activity: Destination printer, document identification, user, timestamp

**Monitoring Technology:**

- Email gateway: Scans inbound/outbound email for malware, DLP violations, policy non-compliance
- Web filter: Blocks prohibited categories (illegal content, malware, inappropriate content); logs web access
- Data Loss Prevention (DLP): Scans email, cloud uploads, removable media for sensitive data exfiltration
- Endpoint Detection and Response (EDR): Monitors process execution, network connections, file access on endpoints
- Firewall and proxy: Logs network traffic, applies access control policies
- SIEM: Aggregates security events, generates alerts for suspicious activity
- User behavior analytics: Identifies unusual access patterns, potential insider threats

**Monitoring Notice:**

- All users acknowledged liability of monitoring upon account creation (acceptable use acknowledgment form)
- Annual reminders provided via security awareness training
- Monitoring conducted transparently; users advised "we monitor systems to protect organizational assets"
- Monitoring does not create expectation of privacy; communications are organizational property except where required by law (attorney-client, religious counseling, medical treatment)

**Monitoring Limitations:**

- Monitoring does not extend to personal devices used on personal networks (BYOD not monitored)
- Off-hours personal use (reasonable breaks, personal email) afforded minimal monitoring consistent with policy enforcement
- Monitoring respects legal bounds (attorney-client privilege, physician-patient confidentiality, legal work product, union organizing, whistleblower communications)

### Investigation and Discipline

**Investigation Trigger:**

Acceptable use violations detected via:

- Automated alert: System monitoring tool flags potential violation (DLP event, malware detection, policy-blocked URL, suspicious login)
- User report: Employee reports potential violation by colleague
- Incident investigation: Incident response investigation identifies underlying policy violation (example: hacking incident leads to discovery of employee credential misuse)
- Audit finding: Internal audit identifies acceptable use violation during control testing

**Investigation Process:**

1. **Notification and Preservation:** Suspected user notified of investigation; email accounts/systems preserved (backup not deleted); office searched only with authorization (HR, Legal, CISO)
2. **Evidence Collection:** IT Security collects evidence (email dumps, file access logs, web history, network traffic, device forensics); chain-of-custody maintained
3. **Fact-Finding:** User interviewed to explain activity; opportunity to provide context or exculpatory evidence (IR investigation subject contacted, allowed to respond)
4. **Legal Review:** Legal counsel reviews facts and applicable law; determines if criminal referral warranted
5. **Disciplinary Assessment:** HR reviews findings with employee; disciplinary action determined (written warning, suspension, termination)
6. **Remediation:** User accepts discipline; technical remediation implemented (account reset, system rebuild, credential revocation)

**Disciplinary Framework:**

| Violation Type                                                                                          | First Offense                                    | Second Offense                          | Third Offense           |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------- | ----------------------- |
| **Minor Policy Violation** (policy unclear interpretation, isolated incident, no impact)                | Verbal warning + training                        | Written warning + policy review meeting | Suspension (1-3 days)   |
| **Moderate Violation** (clear policy breach, remediated, minor impact)                                  | Written warning                                  | Suspension (1-5 days)                   | Termination or demotion |
| **Serious Violation** (intentional breach, sensitive data involved, repeated despite warning)           | Suspension (1-5 days)                            | Termination or extended suspension      | Termination             |
| **Severe/Criminal Violation** (unauthorized access, data theft, illegal activity, malware distribution) | Immediate termination + law enforcement referral | N/A                                     | N/A                     |

**Special Considerations for Severe Violations:**

- Criminal violation: Referral to law enforcement; forensic evidence preserved for investigation
- Data breach (unauthorized data disclosure): Investigation per Data/Privacy Policy (Layer 04, Document 07); potential regulatory notification
- Intellectual property theft: Referral to Legal; potential civil litigation; asset tracing (where did IP go, what recipient, compensation possible)
- Insider threat (coordinated data theft, extortion, sabotage): Investigation per Incident Response Policy; law enforcement involvement considered

**Appeal Process:**

- Disciplinary decision may be appealed to HR Director within 10 business days
- Appeal request reviewed by party other than original decision-maker
- Appeal findings provided within 5 business days; final decision binding

**Documentation:**

- All investigations documented in personnel file (confidential, limited access)
- Disciplinary action documented with violation details, investigation summary, decision, and appeal outcome
- Training completion documented upon remediation

### Acceptable Use Acknowledgment

**Requirement:**

All users must acknowledge understanding of Acceptable Use Policy:

- At hiring/onboarding: Signed acknowledgment form part of employment/contract agreement
- Annual refresh: Acknowledgment form re-signed annually during policy review period (January)
- Access restoration: Users who violate and remediate acknowledge understanding before account re-enabled

**Acknowledgment Form Contents:**

- Confirmation of policy receipt and understanding
- Acknowledgment of monitoring and lack of privacy expectation
- Commitment to protect credentials and report suspicious activity
- Understanding of prohibited activities and consequences
- Electronic signature (if remote) or printed signature with witness

**Non-Acknowledgment:**

- Users refusing to acknowledge policy cannot be granted system access
- Employment/contractor relationship requires policy acknowledgment as condition of engagement

### Third-Party and Contractor Acceptable Use

**Third-Party Requirements:**

- All contractors, vendors, partners with system access bound by Acceptable Use Policy
- Policy incorporated in contracts via acceptable use exhibit or data processing agreement
- Third parties trained on policy requirements before access granted
- Acceptable use violations by third parties trigger contract remediation or termination

**Business Partner Access:**

- Business partners (API integrations, data exchanges) operate under separate Partner Agreement including acceptable use terms
- Partner acceptable use aligned to data classification and data sensitivity
- Partner non-compliance results in access suspension or partnership termination

## Control Mapping

| EATGF Context                         | ISO 27001:2022                                                                                                | NIST SSDF                                                          | COBIT                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| Acceptable use policy and definition  | A.5.1 (Information security policy), A.5.7 (Human resources security—code of conduct)                         | PS-7 (Supply chain protection), AU-2 (Audit events)                | APO01.06 (Enforce policies), DSS05.05 (Enforce policy)                  |
| Monitoring and audit logging          | A.8.15 (Logging), A.8.16 (Monitoring), A.8.17 (Analysis and evaluation)                                       | AU-6 (Audit review/analysis), SI-4 (Information system monitoring) | MEA01.01 (Monitor effectiveness), DSS05.02 (Ensure security compliance) |
| Prohibited activities and enforcement | A.5.10 (Information security incident procedures), A.5.14 (Password management)                               | IR-4 (Incident handling), AC-2 (Account management)                | DSS06.01 (Manage IT security incidents)                                 |
| Investigation and disciplinary action | A.5.26 (Response to security incidents), A.6.10 (Incident management), A.8.37 (Employment termination/change) | IR-4 (Incident handling), AU-9 (Protection of audit information)   | DSS06.01 (Incident management), APO07.03 (Human resources compliance)   |
| Third-party acceptable use            | A.5.23 (Information security in supplier relationships), A.8.34 (Supplier relationships)                      | PS-7 (Supply chain protection)                                     | BAI05.04 (Manage third parties)                                         |

## Developer Checklist

- [ ] Acceptable use policy drafted covering general principles, acceptable use, prohibited use (illegal, unauthorized access, IP violation, data misuse, harmful content, resource abuse, personal use)
- [ ] Acceptable use acknowledgment form created with required content acknowledgments; form integrated into HR onboarding workflow
- [ ] Monitoring technology inventory validated: Email gateway (malware scanning, DLP), web filter, DLP, EDR, firewall/proxy, SIEM, user behavior analytics all deployed and configured
- [ ] Monitoring scope documented with approved monitoring boundaries (no personal device monitoring, respect for attorney-client privilege, union organizing protection)
- [ ] Report types and alert thresholds validated (DLP events, malware detection, web blocks, suspicious logins, unusual data access, impossible travel alerts)
- [ ] Alert routing configured in SIEM with escalation rules (critical alerts to CISO immediately, moderate alerts to SOC Manager, informational alerts logged)
- [ ] Investigation procedure documented including evidence collection, chain-of-custody form, interview process, legal review, disciplinary decision
- [ ] Disciplinary framework defined (minor/moderate/serious/severe categories) with first/second/third offense consequences documented
- [ ] Appeal process documented with timeline (10-day appeal submission window, 5-day decision timeline, independent reviewer requirement)
- [ ] Personnel file documentation template created for recording investigation findings, disciplinary action, appeal outcome
- [ ] Contractor and third-party acceptable use agreements drafted; exhibits created for partner integration agreements
- [ ] Annual acknowledgment refresh process scheduled (January) with tracking of who has signed vs. outstanding signatures
- [ ] Training materials created covering: Acceptable use expectations, monitoring reality, investigation process, disciplinary consequences, appeal rights
- [ ] Sensitive data handling procedures incorporated into acceptable use with classification-specific rules (Public/Internal/Confidential/Restricted access and transmission rules)
- [ ] Credit card handling compliance verified: No credit card PII processing without PCI-DSS authorization; prohibition on unencrypted storage/transmission documented
- [ ] Regular audit of high-risk users (admin access, data access, privileged accounts) conducted quarterly to identify suspicious patterns or policy non-compliance
- [ ] Termination procedures documented including account disablement, device collection, access revocation, final checkout verification

## Governance Implications

**Risk if not implemented:**

- Acceptable use policy absent or unenforced; employees freely engage in prohibited activity (data theft, malware distribution, illegal activity) without consequence
- Employee steals customer data for personal gain (fraud, competitive intelligence); organization unaware due to lack of monitoring
- Contractor accesses systems beyond authorization; contractor steals intellectual property; IP theft goes undetected
- Employee installs unauthorized software on system; malware deployed; incident response delayed due to lack of logging
- Resource hoarding or cryptocurrency mining; system performance degraded; other users experience denied service

**Operational impact:**

- Monitoring system deployment requires infrastructure investment: Email gateway costs, EDR license costs, DLP license costs (typical: $50-$200 per user annually)
- Investigation process requires IT Security and HR time; investigation may take 1-2 weeks for complex cases
- Disciplinary actions potentially create employee disputes; termination decisions require legal review and severance administration
- Investigation with law enforcement involvement may delay resolution; criminal referral complicates employment dispute
- Monitoring may reveal policy violations at scale; high organizational volume of violations requires investigation prioritization (triage by severity)

**Audit consequences:**

- ISO 27001 auditors validate acceptable use policy and monitoring controls per A.5.1 and A.8.15; missing policy results in non-conformance
- SOC 2 auditors validate monitoring controls (C1.2, C1.4) and investigate/remediation procedures; inadequate monitoring results in audit exception
- Employment litigation discovery: Acceptable use investigation and disciplinary action discoverable; investigation quality and consistency evaluated by opposing counsel (termination decisions scrutinized for discrimination)
- Criminal proceeding: Evidence collected during investigation (email, logs, interviews) discoverable by prosecution/defense; evidence quality and chain-of-custody critical for admissibility
- Regulatory investigation (trade secret misappropriation, data breach): Investigation quality determined by external auditors; weak investigation undermines organizational credibility

**Cross-team dependencies:**

- HR depends on IT Security for investigation findings; investigation timeline critical to disciplinary decision deadline (30-60 days typical)
- IT Operations required to preserve systems/email upon notice; preservation procedures non-standard and require training
- Legal involved in criminal referral decision and disciplinary appeal; legal review delays investigation closure
- Finance responsible for severance calculations and final payroll for terminated employees; disciplinary action feeds termination processing
- Compliance team notified of regulatory violations identified in investigation (export control, trade secret law, data protection); evidence forwarding required
- Incident Response team engaged for severe violations (data breach, malware, hacking); investigation merges acceptable use and incident response workflows

## Official References

- NIST SP 800-53 Control AU-2: Audit Events
- NIST SP 800-53 Control AU-6: Audit Review, Analysis, and Reporting
- NIST SP 800-53 Control AC-2: Account Management
- ISO/IEC 27001:2022 Control A.5.1 (Information security policy)
- ISO/IEC 27001:2022 Control A.5.10 (Prevention and dormancy of information security incidents)
- ISO/IEC 27001:2022 Control A.8.15 (Logging)
- ISO/IEC 27001:2022 Control A.8.16 (Monitoring activities)
- Employee Investigations: Best Practices for Today's Workplace (Society for Human Resource Management)
- COBIT 2019 Process APO01: Manage the IT Management Framework

---

**Version History**

| Version | Date       | Change Type     | Description                                              |
| ------- | ---------- | --------------- | -------------------------------------------------------- |
| 1.0     | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
