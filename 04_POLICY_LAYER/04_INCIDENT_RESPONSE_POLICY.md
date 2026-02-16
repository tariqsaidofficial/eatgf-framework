# 04_INCIDENT_RESPONSE_POLICY

| Field          | Value                                                              |
| -------------- | ------------------------------------------------------------------ |
| Document Type  | Policy                                                             |
| Version        | 1.0                                                                |
| Change Type    | Major (Initial)                                                    |
| Classification | Controlled                                                         |
| Effective Date | 2026-02-16                                                         |
| Authority      | Chief Information Security Officer and Incident Response Team Lead |
| EATGF Layer    | 04_POLICY_LAYER                                                    |
| MCM Reference  | EATGF-DSS-INC-01, EATGF-MEA-AUD-01                                 |

---

## Purpose

This policy establishes the mandatory incident response framework for detecting, investigating, containing, and remediating security incidents. The policy applies to all employees, contractors, third parties, systems, and operational environments. All incidents classified as P1-P4 require documented investigation and corrective action. Non-compliance with response SLAs triggers escalation to executive governance.

## Architectural Position

This policy operates within **04_POLICY_LAYER** as the primary incident response governance document.

- **Upstream dependency:** Governance Charter (01_GOVERNANCE_CHARTER.md) establishes CISO authority; Information Security Policy (02_INFORMATION_SECURITY_POLICY.md) defines baseline protections that incident response enforces
- **Downstream usage:** Operationalized through incident response runbooks maintained by Security Operations Center (SOC); enforced through SLA tracking and executive reporting
- **Cross-layer reference:** Maps to EATGF incident controls in Layer 02 (DSS domain incident detection and response), implements MCM controls for incident management, implements audit procedures in Layer 06 for evidence preservation and corrective action tracking

## Governance Principles

1. **Incident-Centric Response** – All incidents processed through standardized incident response phases (Detection, Analysis, Containment, Eradication, Recovery, Lessons Learned)
2. **Time-Critical Escalation** – Incident severity determines response SLA; executive notification occurs within defined timelines regardless of complexity
3. **Evidence Preservation** – All incident investigations preserve digital evidence per chain-of-custody requirements; documentation auditable under ISO 27001 A.5.26
4. **Organizational Alignment** – Incident response authority vested in CISO and delegated to Incident Response Team; legal, compliance, and communications teams coordinate per plan
5. **Continuous Improvement** – Post-incident reviews (PIRs) generate corrective actions mapped to control deficiencies; systemic failures trigger control re-evaluation

## Technical Implementation

### Incident Classification and Severity Matrix

All incidents classified by impact severity and response SLA:

| Severity          | Definition                                                       | Impact                                                               | Response SLA                   | Escalation                  |
| ----------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------ | --------------------------- |
| **P1 - Critical** | Confirmed data breach, active attack, system compromise          | Organizational operations halted, data exfiltration, customer impact | 1 hour detection-to-response   | CISO, CEO, Board            |
| **P2 - High**     | Suspicious activity, unauthorized access, malware detected       | Operational degradation, elevated risk to critical systems           | 4 hours detection-to-response  | CISO, CTO, line management  |
| **P3 - Medium**   | Configuration issues, failed access attempts, policy violations  | System availability degraded, non-critical data at risk              | 8 hours detection-to-response  | SOC Team Lead, ISMS Manager |
| **P4 - Low**      | Informational alerts, routine policy violations, isolated errors | No immediate operational impact                                      | 24 hours detection-to-response | SOC Team, documented in log |

**Escalation authority:** P1 incidents escalated to CISO within 1 hour of detection regardless of confirmation status. Retroactive classification review conducted within 6 hours.

### Incident Response Phases

**Phase 1: Detection & Reporting (SLA: Detection within 24 hours)**

- Security monitoring tools (SIEM, EDR, IDS) configured with alert rules for:
  - Unauthorized authentication attempts (5+ failures in 10 minutes)
  - Abnormal data access patterns (user accessing >10% outside normal parameters)
  - Malware signature matches
  - Policy violation triggers (Confidential data to external storage, etc.)
  - Network traffic anomalies (DDoS signatures, beaconing patterns)
- Employees empowered to report suspected incidents via incident hotline (24/7 availability)
- Reported incidents logged in incident tracking system with timestamp, reporter, and initial description

**Phase 2: Initial Analysis (SLA: Triage within 4 hours for P1-P2, 8 hours for P3)**

- Incident classification assigned per severity matrix
- Preliminary scope assessment: affected systems, users, data, timeline
- Initial containment measures evaluated (e.g., account disable, network isolation, system shutdown)
- Digital evidence collected: logs, memory dumps, disk images per forensic protocol
- Affected parties notified internally (IT Security, system owners, data controllers)

**Phase 3: Containment (SLA: Containment within 8 hours for P1-P2, 24 hours for P3)**

Short-term containment objectives:

- Isolate affected systems from network (physical or logical segregation)
- Disable compromised accounts
- Block malicious IP addresses/domains at perimeter
- Increase monitoring on related systems for lateral movement

Long-term containment objectives:

- Patch or remediate root cause vulnerability
- Restore services from clean backup if system compromised
- Implement detection rules to identify similar compromise patterns

**Phase 4: Eradication (SLA: Root cause removal within 24-72 hours depending on P1-P4)**

- Remove malware, backdoors, and attacker artifacts
- Remediate exploited vulnerabilities per vulnerability remediation SLA
- Reset credentials for affected accounts
- Verify absence of persistence mechanisms
- Forensic analysis documents attack chain and attacker methodology

**Phase 5: Recovery & Restoration (SLA: Service restoration within 24 hours for P1-P2)**

- Restore affected systems from verified clean backups or rebuild
- Perform security verification testing before restoring to production
- Restore user data and re-enable accounts
- Validate system functionality and data integrity
- Monitor restored systems for 72 hours for attack re-emergence

**Phase 6: Post-Incident Review (SLA: Complete within 5 business days of incident closure)**

- Incident Post-Incident Review (PIR) conducted with:
  - Incident responders (SOC, forensics, IR lead)
  - System owner and business unit lead
  - Relevant technical teams (network, application, database)
- PIR documents:
  - Incident timeline and chain of events
  - Root cause analysis (RCA) identifying systemic control failure
  - Contributing factors (detection gap, response delay, insufficient hardening)
  - Corrective actions with assigned owner and completion date
  - Detection and response improvements implemented
  - Knowledge base article created for future reference
- PIR classified and retained per evidence governance requirements (Layer 06)

### Incident Response Team Structure

**Incident Response Team Composition:**

| Role                     | Responsibility                                                       | Authority                                                               |
| ------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **CISO**                 | Incident classification, executive escalation, response direction    | Authorizes evidence handling, external reporting, service interruptions |
| **SOC Manager**          | Day-to-day incident coordination, team leadership                    | Incident triage, containment decisions, team tasking                    |
| **Incident Responder**   | Investigation, evidence collection, technical analysis               | Evidence handling per chain-of-custody, system access for investigation |
| **Forensics Specialist** | Digital forensics, evidence preservation, attack analysis            | Forensic toolkit deployment, legal-grade evidence collection            |
| **Communications Lead**  | External notifications, regulatory reporting, customer communication | Press releases, regulator notifications, customer incident disclosure   |
| **Legal Counsel**        | Regulatory obligations, notification requirements, legal liability   | Guidance on breach notification, privilege claims, subpoena response    |

**Escalation Path:** SOC Manager → CISO → CTO/COO → CEO/Board (for P1 incidents affecting customer data or brand reputation)

### Mandatory Notification Requirements

**Internal Notification:**

- CISO and SOC team notified within 1 hour of P1 incident detection
- CEO and Board informed within 4 hours of confirmed P1 incident
- Affected data controllers informed within 24 hours of data breach confirmation
- Legal and Communications leaders engaged for external notification planning

**Regulatory Notification (per GDPR Article 33, CCPA Section 1798.82):**

- Personal data breach reported to regulatory authorities within 72 hours
- Notification must include:
  - Breach description and affected data categories
  - Likely consequences for data subjects
  - Measures taken or proposed to address breach
  - Contact point for further information
- Notification waived only if breach unlikely to cause risk to data subject rights and freedoms

**Data Subject Notification (per GDPR Article 34, CCPA Section 1798.100):**

- Affected individuals notified without undue delay if breach likely to result in high risk
- Notification must include:
  - Breach description in clear, plain language
  - Likely consequences
  - Measures taken to mitigate risk
  - Contact point for further information
- Notification delivery: email, SMS, or post per communication preferences

**Third-Party Notification:**

- Customers informed of incidents affecting their systems/data within 24 hours of breach confirmation
- Business partners notified if their data or systems affected
- Notification includes:
  - Incident summary and scope
  - Impact to their systems/data
  - Remediation timeline
  - Recommended preventive actions

### Evidence Handling and Chain of Custody

**Digital Evidence Collection:**

- All evidence collected per NIST SP 800-86 digital forensics guidelines
- Evidence handling documented in incident tracking system with:
  - Evidence identifier and description
  - Collection timestamp and method
  - Collector name and signature
  - Transfer handoffs with timestamps
  - Storage location and access controls
- Hash values (MD5/SHA-256) calculated for all disk images and files to detect tampering
- Chain of custody maintained for minimum 5 years per regulatory requirements

**Evidence Retention & Protection:**

- Evidence stored in segregated, encrypted storage with access restricted to forensics team and authorized investigators
- Evidence access logged and auditable; access justification documented
- Evidence retention period defined per litigation holds, regulatory requirements, and data classification:
  - P1 incidents (suspected breach): 7 years (potential litigation period)
  - P2 incidents (unauthorized access): 3 years
  - P3 incidents (suspicious activity): 1 year
  - P4 incidents (routine): 90 days
- Expired evidence destroyed via certified destruction process per data disposal policy

### Incident Response Tools and Technology

**Required Capabilities:**

- Security Information and Event Management (SIEM) for centralized log correlation and alerting
- Endpoint Detection and Response (EDR) for process-level visibility and containment
- Network monitoring and packet capture for traffic analysis
- Vulnerability scanner for post-incident verification of remediation
- Forensic toolkit (EnCase, Volatility, or equivalent) for digital forensics
- Incident tracking and workflow system (Jira, ServiceNow, or equivalent) for case management
- Communication and collaboration tools (Slack, Teams, conference bridge) for rapid coordination

**Tool Access Controls:**

- Access to incident response tools restricted to authorized SOC and forensics personnel
- Administrative access requires CISO approval and dual-control (two authorized users required for sensitive operations)
- Tool usage logged and auditable; access reviews conducted quarterly

### Incident Response Testing and Tabletops

**Annual Testing Requirements:**

- Full incident response tabletop conducted annually (Q1) to test incident response procedures, communication paths, and team coordination
- Red team engagement conducted annually to identify detection gaps and response deficiencies
- Tool functionality testing conducted quarterly to verify SIEM, EDR, and forensic toolkit operability
- All testing documented with findings and corrective actions tracked to closure

**Testing Participants:**

- CISO and incident response team leads
- System owners and business unit representatives
- Communications and legal representatives
- IT operations and infrastructure teams

## Control Mapping

| EATGF Context                              | ISO 27001:2022                                                                                                            | NIST SSDF                                         | OWASP                                          | COBIT                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------- | ---------------------------------------- |
| Incident detection and classification      | A.5.26 (Response to information security incidents)                                                                       | PO.1.2 (Incident coordination process)            | SAMM Governance 2.1 (Incident Management)      | DSS06.01 (Prepare for incident handling) |
| Response SLA and escalation                | A.5.26, A.6.10 (Information security incident management procedures)                                                      | PO.3.2 (Incident response execution)              | ASVS 9.2 (Data breach response)                | DSS06.02 (Detect security incidents)     |
| Investigation and containment              | A.5.26, A.6.11 (Restoring information systems)                                                                            | PO.3.2 (Containment and eradication)              | SAMM Operations 1.1 (Incident Analysis)        | DSS06.03 (Report security incidents)     |
| Post-incident review and RCA               | A.5.26, A.8.17 (Monitoring and review of information security)                                                            | PO.1.1 (Policy and strategy)                      | SAMM Operations 2.2 (Post-incident assessment) | MEA01.01 (Monitor effectiveness)         |
| Evidence preservation and chain of custody | A.5.23 (Information security to be addressed in supplier agreements), A.7.1 (Positions with access to information assets) | PO.1.3 (Records and forensic evidence management) | ASVS 9.2.5 (Forensic evidence gathering)       | DSS06.06 (Implement improvements)        |
| Regulatory notification                    | A.6.10, A.6.11 (Notification procedures)                                                                                  | PO.3.3 (Stakeholder notification)                 | ASVS 8.3.2 (Breach notification)               | APO12.06 (Compliance reporting)          |

## Developer Checklist

- [ ] Incident response team identified and contact list established (CISO, SOC Manager, Responders, Forensics, Legal, Communications)
- [ ] Incident severity classification matrix implemented in incident tracking system with P1-P4 definitions and SLAs
- [ ] SIEM configured with alerting rules for data exfiltration, unauthorized access, malware, policy violation, and anomalous behavior (20+ base rule sets)
- [ ] EDR or equivalent endpoint monitoring deployed on all critical systems with alert forwarding to SIEM
- [ ] Incident response runbooks created for top 5 incident types (data breach, malware infection, unauthorized access, DDoS, insider threat) with step-by-step procedures
- [ ] Forensic toolkit installed on isolated forensics workstation with air-gapped storage for evidence
- [ ] Incident response communication channels established (emergency hotline, Slack channel, runbook distribution list)
- [ ] Chain of custody form created and deployed with mandatory fields: evidence ID, collector, timestamp, hash values, transfer handoffs, storage location
- [ ] Incident tracking system (Jira, ServiceNow, etc.) configured with incident workflow, SLA alerts, and escalation automation
- [ ] Response SLA monitoring dashboard created and reviewed daily by SOC Manager; P1 auto-escalates to CISO if breached
- [ ] Annual incident response tabletop scheduled and facilitated with executive, security, operations, and business participants; findings tracked to corrective action register
- [ ] Post-incident review template created with RCA section requiring systemic control failure identification and corrective action assignment
- [ ] Evidence retention policy documented with retention periods by incident severity (P1: 7 years, P2: 3 years, P3: 1 year, P4: 90 days)
- [ ] Regulatory notification procedures documented and reviewed by Legal for GDPR 72-hour requirement, CCPA notification rules, and sector-specific breach laws
- [ ] Incident response training delivered annually to all staff; SOC and forensics teams trained quarterly on tool updates and procedure changes

## Governance Implications

**Risk if not implemented:**

- Undetected security incidents remain active in environment (attackers maintain persistence, exfiltrate additional data)
- Incident investigations lack evidence preservation, rendering forensic analysis unreliable and preventing legal recourse
- Response delays exceed regulatory notification timelines, triggering fines under GDPR (up to EUR 10M or 2% revenue), CCPA, and sector-specific laws
- Lack of standardized response procedures creates inconsistent coverage, with some incidents handled well and others mismanaged

**Operational impact:**

- Incident response SLAs require 24/7 on-call staffing (SOC monitoring, incident responder availability)
- System isolation during containment may impact business operations; business continuity planning required to manage acceptable downtime
- Forensic investigation timelines (5-24 hours depending on complexity) delay service restoration; business units must understand investigation is prerequisite to recovery
- Tabletop exercises require cross-functional participation including executives; annual scheduling must account for availability

**Audit consequences:**

- ISO 27001 auditors assess incident response maturity against A.5.26 and A.6.10; absence of documented procedures results in non-conformance
- Regulatory audits (GDPR, CCPA, SOC 2, PCI-DSS) specifically validate breach notification procedures and timelines; non-compliance results in audit findings
- Legal discovery in breach litigation requires production of incident response documentation; inadequate evidence preservation damages litigation defensibility
- Evidence handling failures (broken chain of custody, evidence tampering) render forensic findings inadmissible in legal proceedings, eliminating attacker attribution and recovery options

**Cross-team dependencies:**

- SOC operations team must monitor and alert on incidents; requires SIEM deployment, alert configuration, and 24/7 staffing agreement
- System owners must support forensic data collection (memory dump, disk image, log export) and participate in post-incident reviews; IT operations impacted by containment actions (system isolation, service shutdown)
- Legal team must validate regulatory notification decisions and manage breach disclosure liability; Communications team manages media response to public breaches
- Business continuity team must coordinate with incident response on alternate systems activation if recovery timeline exceeds RTO; Procurement may need to engage third-party forensics contractors for complex investigations

## Official References

- NIST SP 800-61 Revision 3: Computer Security Incident Handling Guide
- NIST SP 800-86: Guide to Integrating Forensic Techniques into Incident Response
- ISO/IEC 27001:2022 Control A.5.26 (Response to information security incidents)
- ISO/IEC 27035:2016 Information Security Incident Management
- GDPR Articles 33-34: Notification of a Personal Data Breach
- OWASP SAMM 2.0: Operations Process Area (Incident Management)
- COBIT 2019: Governance Object DSS06 (Manage IT Security Incidents and Continuity)

---

**Version History**

| Version | Date       | Change Type     | Description                                              |
| ------- | ---------- | --------------- | -------------------------------------------------------- |
| 1.0     | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
