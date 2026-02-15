# EVIDENCE_GOVERNANCE_STANDARD

| Field          | Value                                                                   |
| -------------- | ------|
| Document Type  | Standard (Evidence Management)                                          |
| Version        | 1.0                                                                     |
| Change Type    | Major (Initial)                                                         |
| Classification | Controlled                                                              |
| Effective Date | 2026-02-16                                                              |
| Authority      | Chief Audit Officer and Records Administrator                           |
| EATGF Layer    | 06_AUDIT_AND_ASSURANCE                                                  |
| MCM Reference  | EATGF-MEA-EVD-01, EATGF-APO-REC-01                                      |

---

## Purpose

This standard establishes the mandatory governance framework for managing evidence used in control audits, investigations, certifications, and regulatory submissions. Evidence includes: audit working files, control testing results, incident investigation records, certification documentation, compliance evidence, correspondence with auditors, and supporting materials. The standard defines evidence classification, retention periods, access controls, storage/protection requirements, and disposal procedures. All evidence must be preserved per legal/regulatory obligations; unauthorized alteration or destruction prohibited.

## Architectural Position

This standard operates within **06_AUDIT_AND_ASSURANCE** as the evidence management and records governance standard.

- **Upstream dependency:** Internal Audit Procedure (peer document), Audit Schedule Standard (peer document), Corrective Action Register Standard (peer document) all generate evidence requiring governance
- **Downstream usage:** Evidence sourced by auditors for control testing, by incident responders for investigation, by certifiers (SOC 2, ISO 27001) for audit, by legal in litigation
- **Cross-layer reference:** Evidence used to demonstrate control effectiveness across all layers (policies, controls, operations, assurance); supports regulatory compliance and litigation defense

## Governance Principles

1. **Legal Holds and Duty to Preserve** – All evidence subject to presumed litigation hold; evidence preserved throughout documented retention period; authorized destruction only after retention expiration
2. **Chain of Custody** – Evidence ownership and handling tracked; alterations documented; evidence integrity assured
3. **Confidentiality Protection** – Confidential/restricted evidence access controlled; unauthorized disclosure prohibited
4. **Accessibility for Legitimate Requests** – Auditors, regulators, legal counsel can access evidence per defined procedures; access logged
5. **Sustainability and Disposal** – Expired evidence securely destroyed per documented procedure; destruction evidence retained

## Technical Implementation

### Evidence Classification and Categorization

**Evidence Types and Source Documents:**

| Evidence Category | Evidence Types | Retention Period | Classification |
|---|---|---|---|
| **Audit Evidence** | Audit working files, test results, finding documentation, audit reports, management responses | 7 years (10 for critical controls) | Controlled |
| **Control Testing Evidence** | Test results, sample testing documentation, walkthrough evidence, configuration testing | 3-5 years | Internal |
| **Investigation Evidence** | Incident investigation reports, witness interviews, forensic reports, forensic data, breach notifications | 5-7 years (breach evidence: 7 years minimum) | Confidential |
| **Certification Evidence** | SOC 2 audit reports, ISO 27001 audit reports, regulatory audit reports, certification documents | 7 years | Controlled |
| **Training and Awareness** | Training sign-in sheets, training completion records, awareness campaign evidence | 3 years | Internal |
| **Compliance Evidence** | Policy acknowledgments, compliance certifications, regulatory submissions, compliance monitoring results | 3-7 years (regulatory specific) | Controlled |
| **Correspondence** | Auditor communications, regulatory authority communications, certification body communications | 5 years (keep with related evidence) | Controlled |
| **System/Log Evidence** | System logs, database logs, access logs, network traffic, configuration files | 90 days – 2 years (per data type) | Internal/Confidential |
| **Financial/Supporting** | Cost tracking for audit remediations, budget allocations, vendor invoicing | 7 years (per accounting standards) | Internal |

**Data Classification (In Addition to Category):**

| Classification | Definition | Access Restrictions | Storage Requirements |
|---|---|---|---|
| **Public** | Evidence approved for public disclosure (published audit reports, certifications) | Wide access; publishable | Standard storage |
| **Internal** | Non-sensitive organizational evidence (training completion, general test results) | Employees only | Controlled repository with audit trail |
| **Confidential** | Sensitive organizational information (incident details, control gaps, investigation findings) | Limited access (Audit, Executive, Legal) | Encrypted storage; access logged |
| **Restricted** | Highly sensitive (breach investigation, forensic evidence, competitor intelligence) | Executive + legal only; subpoena-qualified access | Encrypted storage; dual control access; audit trail |

### Evidence Storage and Retention

**Centralized Evidence Repository:**

All evidence stored in single authorized repository with:

- **Folder structure:** Organized by audit year / audit cycle / control / or by incident
- **Access controls:** Role-based access (Audit team full access, Control owners read-only, Executives view-only per classification)
- **Audit trail:** All access logged (who, when, what accessed, duration)
- **Version history:** Document edits tracked; prior versions retained
- **Encryption:** Sensitive evidence encrypted at rest (AES-256)

**Approved Storage Solutions:**

- Microsoft SharePoint with appropriate permissions and audit logging enabled
- Google Drive / Google Workspace with access controls and audit logging
- Dedicated Records Management System (e.g., Everteam, Entity, specialized audit evidence systems)
- On-premises file server with encryption and access controls
- NOT APPROVED: Unencrypted USB drives, personal email, personal cloud storage, shared group email boxes without audit trail

**Backup and Redundancy:**

- Evidence repository backed up daily; backups encrypted and retained per retention policy
- Geographic backup: Backups replicated to secondary location for disaster recovery
- Evidence restoration tested annually; backup integrity validated

**Retention Period Matrix:**

| Evidence Type | Retention Period | Start Date | Disposal Trigger | Notes |
|---|---|---|---|---|
| **Audit working files (Critical controls)** | 10 years | Audit completion date | 10 years post-audit | Critical controls: governance structural importance warrants extended retention |
| **Audit working files (Standard controls)** | 7 years | Audit completion date | 7 years post-audit | Standard retention aligns with ISO 27001 audit evidence retention |
| **Incident/breach investigation** | 7 years minimum | Incident closure date | Statute of limitations (litigation risk) + 7 years | Breach investigations subject to extended litigation risk; 7-year baseline covers most statutes of limitations |
| **SOC 2 / ISO 27001 audit reports** | 7 years | Audit report issuance date | Report aged 7 years | Certification evidence retained throughout certification validity + retention period |
| **Regulatory submissions** | 7 years | Submission date | Per regulatory requirement; typically 7 years minimum | GDPR, PCI-DSS, and others specify retention periods; use most restrictive |
| **Training records** | 3 years | Training completion date | Employee departure + 3 years | Employment law requires retention through covered periods; post-employment 3 years for potential disputes |
| **System logs (audit-related)** | 1-2 years | Log generation date | Operational log rotation | Operational logs; deleted per standard log rotation unless under litigation hold |
| **System logs (security incidents)** | Litigation hold + 7 years | Incident discovery date | Statute of limitations + 7 years | Incident-related logs preserved per investigation requirements; deleted only after litigation risk expires |
| **Control testing results** | 5 years | Test completion date | 5 years post-testing | Control test results retained enabling trend analysis; support repeat audits, remediation verification |
| **Compliance certifications** | 3-7 years | Certification issue date | Per regulatory requirement | Standard: 3 years; GDPR/Privacy: longer if data processed; use most restrictive applicable |

**Litigation Hold Override:**

If litigation involving organizational controls is reasonably anticipated:

1. Legal counsel triggers litigation hold (written directive to Records Administrator)
2. All related evidence placed on hold (retention extended until litigation concludes)
3. Hold applies to: Audit evidence, investigation files, policy documents, control testing, emails/communications about control
4. Hold removed only by written directive from General Counsel once litigation resolved/settled
5. Evidence on litigation hold not destroyed even if normal retention period expires

### Evidence Access and Chain of Custody

**Access Types and Permissions:**

| User Role | Evidence Access | Purpose | Approval Required |
|---|---|---|---|
| **Auditor conducting audit** | Full access to relevant control evidence | Perform control audit testing | Pre-audit authorization per audit schedule |
| **Control Owner** | Read-only access to own control evidence | Review audit results, certification checklist | Self-service (authenticated access) |
| **Chief Audit Officer** | Full access to all evidence | Oversight, governance reporting, audit planning | Role-based (CAO role authorized full access) |
| **CISO/Executive sponsor** | Access to critical findings, investigation evidence, executive summary | Executive governance,  remediation oversight | Role-based authority |
| **General Counsel** | Confidential evidence, investigation evidence, litigation evidence | Legal review, litigation support, regulatory response | Role-based authority |
| **External auditor (SOC 2, ISO 27001)** | Limited evidence scoped to certification | Certification audit | Executed audit engagement letter; access time-limited |
| **Regulatory authority** | Subpoena-specified evidence, voluntary submissions | Regulatory investigation, examination | Legal written directive; access logged and monitored |

**Evidence Access Log:**

All evidence accessed recorded automatically in system audit trail:

| Log Entry | Details |
|---|---|
| **Access timestamp** | Date and exact time of access |
| **Accessor identity** | User ID, name, role of person accessing |
| **Evidence accessed** | Specific file/folder/document accessed |
| **Access type** | Read-only, download, print, etc. |
| **Access duration** | How long evidence accessed |
| **IP address / location** | System from which accessed (organizational network, remote, etc.) |

**Quarterly Access Audit:**

Chief Audit Officer reviews access logs quarterly:

- Unauthorized access attempts detected and investigated
- Excessive printing/downloading flagged for appropriateness review
- External auditor/regulator access verified per engagement letter
- Anomalies (after-hours access, bulk downloads) escalated to Security team

**Chain of Custody:**

For sensitive evidence (forensic evidence, breach investigation):

- **Custody form completed** upon evidence collection: Description, collector, timestamp, initial condition/state
- **Transfer documented** each time custody transferred: From, to, timestamp, handoff signature/email
- **Storage location logged** with access restrictions noted
- **Destruction documented** with signed certificate of destruction upon retention expiration

Example: "Drive image collected from server XYZ during incident investigation taken offline Jan 15, 2026 at 14:30 UTC by IT Security (John Smith). Drive imaged to external USB (hash: SHA-256 xxxxxxxx). Drive transferred to Forensics team Jan 15 16:00 UTC (signed by I.T. John Smith and Forensics Sarah Chen). Forensic analysis completed Feb 5, 2026 (Analysis report: /Evidence/Investigation/Incident-2026-001/Forensic_Report_Final.pdf). Drive imaged data retained in encrypted repository for 7 years (destruction scheduled Jan 2033). Destruction verified Jan 15, 2033 via Certificate of Destruction signed by Records Administrator."

### Evidence Protection and Security

**Confidentiality Controls:**

- Confidential/Restricted evidence encrypted at rest (AES-256 minimum)
- Confidential/Restricted evidence encrypted in transit if transmitted (TLS 1.2+)
- Audit trail enabled: All access logged, unauthorized access attempts blocked
- "Need to know" principle: Access granted only to users with explicit need for evidence

**Integrity Controls:**

- Document versioning enabled: All edits tracked, prior versions retained
- Hash values calculated for forensic evidence: Integrity verified on retrieval
- Unauthorized modification prevented: Audit evidence marked read-only once finalized
- Audit trail detects any modifications: Tampering attempts logged and investigated

**Availability Controls:**

- Evidence backed up daily; recovery tested quarterly
- Redundant storage: Primary + secondary location; geographic distribution
- Disaster recovery: Backup recovery achieved within 4-hour RTO
- Business continuity: Alternative evidence access method if primary storage unavailable

### Evidence Disposal and Destruction

**Disposal Procedure:**

Upon retention expiration, evidence disposed securely:

| Evidence Type | Disposal Method | Verification |
|---|---|---|
| **Digital evidence (files, documents)** | Secure deletion from primary + backup storage; data overwritten 3x per NIST SP 800-88 | Certificate of destruction issued; hash values verified unrecoverable |
| **Physical evidence (printed documents)** | Certified shredding by approved vendor; non-recoverable destruction | Certificate of destruction from shredding vendor retained |
| **Encrypted evidence** | Delete encryption keys; original data destruction not required if keys destroyed | Key destruction verified; evidence unrecoverable without keys |
| **System logs** | Automated log deletion per log retention policy; deletion logged | IT operations confirms logs deleted per schedule |
| **Forensic media (USB, drives, tapes)** | Certified physical destruction (degaussing, incineration, shredding) | Certificate from destruction vendor retained; destruction verified |

**Destruction Evidence:**

- Certificate of destruction document created with: Evidence ID, date destroyed, method, verified by (person/vendor), date verified
- Certificate scanned and retained in central records for 3 years (evidence of destruction documented)
- Litigation holds prevent automatic destruction: Hold must be explicitly released by Legal

**Exception – Evidence Not Eligible for Destruction:**

Evidence not destroyed if:

1. **Litigation hold active:** Legal hold remains until litigation resolved
2. **Regulatory hold:** Regulatory requirement mandates extended retention (GDPR, HIPAA, etc.)
3. **Statutes of limitation running:** Litigation risk continues (statute not yet expired)
4. **Active investigation:** Investigation not closed
5. **Remediation incomplete:** Associated corrective action not closed

### Evidence Audit and Verification

**Annual Evidence Audit (By Records Administrator):**

Once per year (January), comprehensive evidence audit performed:

1. **Sampling test:** 10-20% of evidence folders randomly selected
2. **Completeness check:** Verify expected evidence present (per audit scope, control, incident)
3. **Integrity check:** Spot-verify evidence annotations (dates, signatures, approvals) match evidence content
4. **Retention compliance:** Verify retention periods correctly applied; evidence not destroyed prematurely
5. **Classification accuracy:** Verify evidence classified appropriately (not over/under classified)
6. **Access appropriateness:** Audit sample of access logs; verify access aligned to user roles and legitimate purposes
7. **Storage integrity:** Verify backup integrity, encryption status, no unauthorized access attempts found in logs

**Evidence Audit Report:**

Records Administrator reports findings to Chief Audit Officer:

- % of evidence properly classified
- % of evidence retention periods correctly applied
- Issues identified (premature destruction, over-classification, unauthorized access)
- Recommendations for process improvement

**Remediation of Audit Findings:**

- Over-classified evidence: Reclassified
- Under-classified evidence: Reclassified  
- Retention errors: Corrected; extended if premature deletion risk
- Access violations: Reviewed by Security; unauthorized access investigated
- Process improvements: Implemented for next audit cycle

### Evidence Governance Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **Chief Audit Officer** | Overall evidence governance accountability; storage location selection; retention policy approval; litigation hold authorization; access approvals for external auditors |
| **Records Administrator** | Day-to-day evidence management; evidence intake and storage; access log review; retention enforcement; destruction scheduling and verification; evidence audit coordination |
| **Control Owners** | Provide evidence to auditors; maintain control-specific evidence; certify evidence completeness before audits |
| **Auditors** | Collect and document evidence during audits; preserve evidence per chain of custody; submit evidence to Records Administrator for storage; log access to Repository |
| **General Counsel** | Litigation hold decisions; retention policy legal review; regulatory hold interpretation; evidence handling for investigations |
| **IT Security** | Repository infrastructure security; encryption; backup integrity; access control implementation; incident investigation evidence preservation |
| **Data Protection Officer** | Personal data in evidence; ensures evidence retention complies with GDPR/CCPA (e.g., no excessive personal data retention) |

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | COBIT |
|---|---|---|---|
| Evidence retention and preservation | A.8.17 (Monitoring, measurement, analysis and evaluation), A.6.7 (Management review) | AU-2 (Audit events), AU-4 (Audit log protection) | MEA03.01 (Collect, process, and analyze data) |
| Evidence storage and protection | A.8.15 (Logging), A.8.16 (Monitoring), A.8.17 (Analysis and evaluation) | SI-4 (Information system monitoring), SC-7 (Boundary protection) | DSS05.02 (Ensure security compliance) |
| Access controls and confidentiality | A.5.14 (Password management), A.8.2 (Asset management) | AC-2 (Account management), AC-3 (Access enforcement) | DSS05.01 (Manage access levels) |
| Chain of custody and integrity | A.8.13 (Handling of assets), A.8.14 (Asset disposal) | SI-4 (System monitoring), SC-4 (Information in shared resources) | DSS05.02 (Ensure audit trails) |
| Destruction and disposal | A.8.4 (Information handling and storage), A.8.14 (Asset disposal) | SC-4 (Shared resources), SC-7 (Sanitization) | DSS03 (Deliver service results) |

## Developer Checklist

- [ ] Evidence governance policy framework drafted with classification levels (Public, Internal, Confidential, Restricted) and retention period matrix
- [ ] Centralized evidence repository selected and configured (SharePoint, Google Drive, dedicated system) with access controls and audit logging enabled
- [ ] Storage encryption implemented for Confidential/Restricted evidence (AES-256 at rest, TLS 1.2+ in transit)
- [ ] Backup and recovery procedures documented; daily backups configured with geographic redundancy; disaster recovery RTO 4 hours validated
- [ ] Retention schedule created by evidence type: Audit evidence 7-10 years, investigations 7 years, certifications 7 years, logs 90 days-2 years, training 3 years
- [ ] Litigation hold procedure documented: Legal directive triggers hold, hold applies to related evidence, removal requires written General Counsel directive
- [ ] Access control matrix created: Auditor access (authorized per audit), Control owner read-only, CAO full access, Executive access (per classification), Legal access, External auditors limited access
- [ ] Access log review procedure documented: Quarterly CAO audit of access logs, unauthorized access escalation, anomaly investigation protocols
- [ ] Chain of custody form created for sensitive evidence: Description, collector, timestamp, transfer documentation, custody signatures, storage notation
- [ ] Evidence disposal procedure documented: Digital deletion method (3x overwrite, key destruction), physical destruction (certified shredding), verification required (certificates)
- [ ] Certificate of destruction template created documenting: Evidence ID, destruction date, method, verified by (person/vendor), verification date
- [ ] Annual evidence audit procedure documented: 10-20% sampling, completeness/integrity/retention verification, classification accuracy, access appropriateness
- [ ] Records administrator role defined with responsibilities: Evidence intake, storage location management, access log review, retention enforcement, destruction verification, audit coordination
- [ ] Chief Audit Officer role defined: Governance oversight, storage selection, retention policy approval, litigation hold authorization, external auditor access approval
- [ ] General Counsel role defined: Litigation hold decisions, retention policy legal review, regulatory hold interpretation, investigation evidence handling
- [ ] Quarterly access audit report template created documenting: Access violations, after-hours/bulk download anomalies, external auditor access verification
- [ ] Staff training created covering: Evidence classifications and retention, access controls and confidentiality, chain of custody for sensitive evidence, destruction procedures, litigation hold requirements

## Governance Implications

**Risk if not implemented:**

- Evidence stored inconsistently; control testing results not preserved; audits cannot verify prior findings remediated
- Sensitive investigation evidence accessible to unauthorized personnel; breach confidentiality, litigation disadvantage
- Evidence destroyed prematurely; litigation hold violated; evidence spoliation sanctions imposed by courts
- Evidence altered/modified: Undetected changes undermine audit credibility, litigation challenges audit findings authenticity
- Evidence lost due to lack of backup; critical evidence unavailable for regulatory examination or litigation

**Operational impact:**

- Evidence repository requires dedicated space (cloud storage cost, licensing, infrastructure)
- Records Administrator role required (0.5-1 FTE managing evidence storage, access, disposal, audits)
- Quarterly access audits add 2-4 hours Records Administrator work
- Annual evidence audit adds 3-5 hours Records Administrator work
- Litigation holds created immediately upon legal notice; active monitoring of evidence retention during litigation (no routine destruction)

**Audit consequences:**

- ISO 27001 auditors validate evidence retention (A.8.17); absence of evidence preservation results in audit non-conformance
- SOC 2 auditors evaluate evidence storage security and access controls (C1.1, C1.2); inadequate controls result in audit exception
- Regulatory audits (GDPR, HIPAA, PCI-DSS) inspect evidence retention; non-compliance results in regulatory finding
- Litigation discovery: Evidence preservation quality and chain of custody evaluated by opposing counsel; poor evidence management damages litigation position

**Cross-team dependencies:**

- IT must support repository infrastructure (backup, encryption, access control implementation)
- Security team must support investigation evidence preservation and forensic evidence handling
- Legal must authorize litigation holds and advise on retention requirements for active litigation
- HR must provide personnel records as evidence source (training records, compliance documentation)
- Finance must retain audit-related cost documentation and budget allocation evidence
- Auditors must provide complete evidence from audit field work; submit to Records Administrator for archival

## Official References

- NIST SP 800-88: Guidelines for Media Sanitization
- NIST SP 800-53: Control AU-4 (Audit Log Protection)
- ISO/IEC 27001:2022 Section A.8.17 (Monitoring, measurement, analysis and evaluation)
- EDRM (Electronic Discovery Reference Model): Evidence and Preservation Guidelines
- Federal Rules of Civil Procedure Rule 26 (Discovery): Evidence and Document Preservation Requirements
- Sedona Conference: Document Retention Best Practices for Organizations
- COBIT 2019 Process MEA03: Monitor, Assess, and Report IT Compliance and Performance

---

**Version History**

| Version | Date | Change Type | Description |
|---------|------|-------------|-------------|
| 1.0 | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
