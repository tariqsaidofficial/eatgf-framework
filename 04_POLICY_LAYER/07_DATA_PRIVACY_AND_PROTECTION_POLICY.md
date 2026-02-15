# 07_DATA_PRIVACY_AND_PROTECTION_POLICY

| Field          | Value                                                        |
| -------------- | ------------------------------------------------------------ |
| Document Type  | Policy                                                       |
| Version        | 1.0                                                          |
| Change Type    | Major (Initial)                                              |
| Classification | Controlled                                                   |
| Effective Date | 2026-02-16                                                   |
| Authority      | Chief Privacy Officer and Chief Information Security Officer |
| EATGF Layer    | 04_POLICY_LAYER                                              |
| MCM Reference  | EATGF-APO-PRI-01, EATGF-APO-PRI-02, EATGF-DSS-PRI-01         |

---

## Purpose

This policy establishes mandatory data protection and privacy standards for collecting, processing, storing, and disposing of personal data and sensitive information. The policy applies to all employees, contractors, third parties, systems, and business units. The policy implements GDPR, CCPA, and sector-specific privacy regulations. All personal data processing activities must be documented in a Data Processing Register. Non-compliance triggers disciplinary action and regulatory penalties.

## Architectural Position

This policy operates within **04_POLICY_LAYER** as the primary data privacy governance document.

- **Upstream dependency:** Governance Charter (01_GOVERNANCE_CHARTER.md) establishes Chief Privacy Officer authority; Information Security Policy (02_INFORMATION_SECURITY_POLICY.md) defines technical protection requirements for data
- **Downstream usage:** Operationalized through Data Processing Agreements (GDPR), Privacy Impact Assessments, data subject rights procedures, and Data Protection Officer (DPO) functions; enforced through privacy-by-design controls and data governance procedures
- **Cross-layer reference:** Maps to EATGF privacy controls in Layer 02 (APO-PRI domain for privacy governance, DSS-PRI domain for privacy protections), implements MCM controls for personal data handling, works with Vendor Risk Policy (Layer 04) for processor data agreements, implements audit procedures in Layer 06 for privacy compliance audits

## Governance Principles

1. **Privacy-by-Design** – Personal data collection minimized; data processing limited to specified purposes only; privacy impact assessed before new processing
2. **Regulatory Compliance** – GDPR (EU), CCPA/CPRA (California), PIPEDA (Canada), LGPD (Brazil), and sector-specific regulations (HIPAA, FERPA, GLBA) applied based on data subject jurisdiction
3. **Data Subject Rights** – Right to access, rectification, erasure, portability, restriction, and objection honored per regulatory requirements
4. **Retention and Erasure** – Personal data retained only per regulatory requirements or business need; automated retention policies enforce data deletion upon expiration
5. **Accountability and Governance** – Data Processing Register maintained for all processing; privacy impact assessments conducted for high-risk processing; DPO oversees privacy compliance

## Technical Implementation

### Personal Data Classification and Handling

**Personal Data Definition:**

Any information relating to an identified or identifiable natural person. Examples:

- Direct identifiers: Name, contact information, identification numbers, customer IDs
- Sensitive data: Health information, financial information, biometric data, racial/ethnic origin, political affiliations, religious beliefs, trade union membership, genetic data
- Usage data: IP addresses, cookies, device identifiers, location data, behavioral data
- Derived data: Inferred preferences, risk assessments, profiling data

**Data Classification Standard:**

| Classification              | Definition                                                                             | Protection Level                                                 | Retention Basis                                           |
| --------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------- |
| **Public**                  | Information approved for public disclosure                                             | Basic protection                                                 | As published (indefinite)                                 |
| **Internal**                | Non-sensitive business information; no personal data                                   | Standard protection                                              | Per business need (e.g., 3-7 years)                       |
| **Personal Data**           | Information identifiable to individual; non-sensitive                                  | Enhanced protection (pseudonymization, encryption)               | Per GDPR Art. 5 (storage limitation)                      |
| **Sensitive Personal Data** | Health, financial, racial/ethnic, political, religious, union, biometric, genetic      | Maximum protection (encryption at rest/transit, strict access)   | Narrow retention window (1-2 years) or immediate deletion |
| **Restricted**              | Classified personal data, combined datasets enabling re-identification, health records | Highest protection (role-based access, approval-required access) | Minimum legally required retention                        |

**Processing Activity Documentation:**

All personal data processing documented in Data Processing Register including:

- Processing purpose (e.g., "customer account management", "payroll processing", "marketing communications")
- Data categories processed (customer names, email addresses, transaction history, etc.)
- Personal data sources (customer input, transaction logs, third-party providers, etc.)
- Legal basis for processing (contract performance, legal obligation, consent, legitimate interest, EU data adequacy, etc.)
- Data subjects affected (customers, employees, applicants, etc.)
- Retention period
- Recipients of personal data (internal departments, third-party processors, downstream recipients, etc.)
- Processor Data Processing Agreements (for third-party processing)
- Security measures implemented
- DPA and Privacy Impact Assessment (if applicable)

### Legal Basis for Personal Data Processing

All personal data processing requires documented legal basis per GDPR Article 6:

| Legal Basis              | Definition                                                          | Examples                                                           | Conditions                                                                                   |
| ------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| **Consent**              | Data subject gives informed, explicit consent                       | Marketing email, behavioral tracking, optional data requests       | Consent must be freely given, specific, informed, unambiguous; right to withdraw at any time |
| **Contract**             | Processing necessary to fulfill contract with data subject          | Customer order processing, account management, service delivery    | Contract performance only; not extended to unrelated purposes                                |
| **Legal Obligation**     | Processing required by law                                          | Payroll tax reporting, regulatory reporting, legal hold responses  | Limited to legally required processing; minimum data necessary                               |
| **Vital Interests**      | Necessary to protect vital interests of data subject or third party | Emergency health data, life-threatening situations                 | Only justified in non-alternative circumstances                                              |
| **Public Task**          | Processing necessary for public administration tasks                | Government agencies operating in official capacity                 | (Not applicable to most private organizations)                                               |
| **Legitimate Interests** | Processing necessary for organization's legitimate interests        | Fraud prevention, account security, analytics, product improvement | Legitimate interest must outweigh data subject privacy rights; interest assessment required  |

**Legitimate Interest Assessment (LIA):**

For processing based on legitimate interest, documented assessment confirms:

- Legitimate interest is identified and documented (e.g., "fraud detection", "marketing insight")
- Processing is necessary to achieve the interest (less invasive alternatives considered)
- Data subject rights and interests do not override organization's interest (balancing test)
- Examples of LIA: Fraud prevention, security monitoring, analytics for service improvement, direct marketing to existing customers

**Legal Basis Documentation:**

All processing activities linked to legal basis entry in Data Processing Register. Processing without documented legal basis prohibited.

### Data Subject Rights and Procedures

**Right of Access (GDPR Article 15, CCPA Section 1798.100):**

- Data subject may request all personal data held
- Response deadline: 30 calendar days (45 days if complex); can extend 2 additional months if necessary with notice
- Response format: Machine-readable format for GDPR requests, human-readable format for CCPA
- Response must include: Data processed, purpose, recipients, retention period, data source, automated decision-making (if any)
- Verification: Data subject identity verified before disclosure (government ID confirmation)
- Fees: No fee unless request frivolous or excessive; multiple requests (>1 per year) may incur processing fee ($0-$45 per CCPA)

**Right of Rectification (GDPR Article 16):**

- Data subject may request correction of inaccurate personal data
- Verification procedure: Confirm identity; verify record and claim of inaccuracy
- Correction made within 30 days of verified request
- Downstream notification: All recipients notified of correction (except if impossible or disproportionate)

**Right of Erasure ("Right to Forget") (GDPR Article 17):**

- Data subject may request deletion if:
  - Data no longer necessary for purpose collected
  - Consent withdrawn (if consent was basis)
  - Legal basis no longer valid (contract ended, legal obligation expired)
  - Object to processing and no overriding organizational interest
- Exceptions: Erasure refused if:
  - Legal obligation requires retention (tax law, litigation hold)
  - Legitimate interests require retention
  - Data needed for scientific/historical research with safeguards
  - Automated decision-making data needed for explanation
- Deletion timeline: Within 30 days of verified request; data expunged from active systems and backups (excluded from standard retention policies)
- Upstream notification: Processors notified to delete data from their systems
- Documentation: Deletion logged per chain-of-custody requirements

**Right to Restrict Processing (GDPR Article 18):**

- Data subject may request processing suspension (but not deletion)
- Restriction triggers: Data subject disputes accuracy; processing unlawful but data subject opposes deletion; organization no longer needs data but data subject claims need; data subject objects to processing
- Restricted data marked in system and excluded from active processing; data retained but not accessed except for storage or consent
- Lifted upon data subject request, accuracy confirmation, or legal basis reinstatement

**Right to Data Portability (GDPR Article 20):**

- Data subject may request data in structured, commonly-used, machine-readable format (CSV, JSON, XML)
- Data must be provided in format enabling transmission to another controller without obstruction
- Applies to data: Provided by data subject, processed on basis of consent or contract
- Deadline: 30 days; can extend 2 months if complex
- Direct transmission: Data may be transmitted directly to another controller if technically feasible
- Scope: Limited to data provided by subject; derived or inferred data not included

**Right to Object (GDPR Article 21):**

- Data subject may object to processing for direct marketing (absolute right); processing must cease immediately
- Data subject may object to processing for legitimate interest (data subject must prove compelling interest)
- Organization assesses objection; if upheld, processing ceases; if overridden, documented reasoning provided
- Marketing objection: Immediate unsubscribe; name added to do-not-contact list

**Rights Related to Automated Decision-Making (GDPR Article 22):**

- Data subject has right not to be subject to automated decision-making that produces legal or similarly significant effect
- Examples of affected decisions: Credit decisions, hiring decisions, insurance underwriting, benefit eligibility
- Safeguards: Human review required for significant automated decisions; transparency requirement (data subject informed of automated decision)
- Exceptions: Decision necessary for contract performance; explicitly authorized by law; data subject consented
- Right of explanation: Data subject may request explanation of automated decision, challenge accuracy, request human review

**Data Subject Rights Procedures:**

| Step                          | Owner                               | Timeline                                                                                              |
| ----------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Request reception             | DPO/Privacy team                    | Within 1 business day: Acknowledge receipt; confirm identity verification required                    |
| Identity verification         | DPO/Privacy team                    | Within 5 business days: Verify identity (government ID, email confirmation); confirm request validity |
| Request assessment            | Privacy team + relevant data owners | Within 5-10 business days: Determine scope, legal basis, applicable exceptions                        |
| Data collection & preparation | Data owners                         | Within 15 business days: Compile data, format per standard format requirements                        |
| Response preparation & review | Privacy team + Legal                | Within 20-28 business days: Prepare response, legal review, completion notice preparation             |
| Response delivery             | DPO/Privacy team                    | By day 30: Deliver response to data subject via secure channel; document delivery                     |
| Dispute resolution            | DPO/Privacy team + Legal            | If data subject disputes response: Review within 10 days, escalate to Legal; mediation if necessary   |

### Privacy Impact Assessment (PIA)

**Required for Processing Activities:**

- High-risk processing activities (large-scale processing, automated decision-making, vulnerable populations, tracking)
- New processing purposes or data categories
- Change to existing processing (new data sources, new recipients, change to processing location)
- Significant technology changes affecting data processing

**PIA Procedure:**

1. **Description:** Document processing activity, data categories, data subjects, purpose, legal basis
2. **Necessity Assessment:** Confirm processing necessary for purpose; less invasive alternatives considered
3. **Risk Assessment:** Identify risks to data subject rights (unauthorized access, data loss, discrimination, loss of control)
4. **Risk Mitigation:** Identify technical and organizational measures to mitigate identified risks
5. **Residual Risk:** Assess residual risk after mitigation; confirm acceptable level
6. **DPA Consultation:** If high residual risk, consult with Data Protection Authority prior to processing (GDPR Article 36)
7. **Documentation:** PIA documented and retained; available for audit

**High-Risk Indicators Requiring DPA Consultation:**

- Systematic monitoring of public spaces at large scale (CCTV, facial recognition)
- Automated decision-making with legal/significant effect for vulnerable populations (children, elderly)
- Biometric data processing at scale
- Genetic data processing for non-medical purposes
- Large-scale processing of sensitive data categories

### Data Retention and Automated Deletion

**Retention Schedule:**

| Data Category                      | Retention Period                              | Justification                                            | Deletion Method                              |
| ---------------------------------- | --------------------------------------------- | -------------------------------------------------------- | -------------------------------------------- |
| **Customer account data**          | Duration of relationship + 3 years            | Legal obligation (tax law, accounting)                   | System purge and backup exclusion            |
| **Transaction data**               | 7 years                                       | Legal obligation (tax, financial audit)                  | System purge post-retention expiration       |
| **Marketing data** (consent-based) | Until consent withdrawn or 2 years inactivity | Consent basis; legitimate interest (product improvement) | Immediate upon consent withdrawal            |
| **Employee data**                  | During employment + 3 years                   | Legal (employment law, tax)                              | Secure deletion per data disposal policy     |
| **Log data** (non-sensitive)       | 90 days                                       | Operational and incident response                        | Automatic deletion via log rotation          |
| **Incident investigation data**    | 3 years minimum (7 years if breach)           | Legal (litigation risk), incident evidence               | Secure deletion per evidence protocols       |
| **Audit data**                     | 3-5 years                                     | Regulatory audit requirements                            | Secure deletion per audit retention schedule |

**Automated Retention Enforcement:**

- Retention policies configured in data management systems; automated purge jobs execute deletions at expiration
- Retention expiration monitored; reports generated 30 days before deletion (final review opportunity)
- Deletion events logged and auditable; evidence of deletion documented
- Failed deletion alerts escalated; manual review and remediation required

### Data Processing Agreements (DPA) and Processors

**Processor Agreement Requirements (GDPR Article 28):**

All data processors (third parties processing personal data on behalf of organization) must execute a Data Processing Agreement (DPA) including:

- Processing scope: Data categories, processing types, duration, purpose
- Processor obligations: Ensure compliance, implement safeguards, assist with data subject rights, notify of breaches, provide assurance (audit reports)
- Sub-processor management: Processor must notify organization of sub-processors; organization may object to sub-processors
- International transfers: If data transferred outside EU/EEA, Standard Contractual Clauses (SCCs) incorporated
- Termination: Data return or destruction upon contract termination
- Audit rights: Organization may audit processor compliance; processor must provide audit reports (SOC 2, ISO 27001)

**Processor Vetting:**

All processors undergo security assessment per Vendor Risk Management Policy (Layer 04, Document 06); processors confirmed capable of complying with DPA terms before contract execution.

**Processor Sub-processor Changes:**

- Processor must notify organization of sub-processor changes minimum 30 days in advance
- Organization reviews sub-processor security; may object if inadequate controls
- Objection triggers renegotiation or contract termination

### International Data Transfers

**GDPR Restrictions on Transfer:**

Personal data may only be transferred outside EU/EEA to countries with "adequate" data protection (European Commission adequacy decision) or with appropriate safeguards.

**Legitimate Transfer Mechanisms:**

1. **Adequacy Decision:** European Commission confirmed recipient country has adequate protection (Switzerland, Japan, UK, Canada, South Korea, etc.) – no additional safeguards required
2. **Standard Contractual Clauses (SCCs):** EU Commission pre-approved contract terms binding processor/recipient to GDPR-equivalent protections; used for transfers to non-adequacy countries (US, India, etc.)
3. **Binding Corporate Rules (BCRs):** Multi-entity organizations may use BCRs establishing group-wide data protection standards; approved by data protection authority
4. **Government Data Requests:** If U.S. government requests personal data of EU/UK citizens, SCCs supplemented with additional safeguards (Schrems II compliance)

**Transfer Documentation:**

All transfers documented with legal mechanism:

- SCC-based transfers require DPA supplement and Transfer Impact Assessment (TIA)
- Adequacy-decision transfers require processor DPA but no additional assessment
- Historical transfer assessment (Schrems II 2020): Evaluate U.S. government access laws vs. GDPR Article 44(1) standard; implement supplementary measures if inadequate

### Data Breach Notification and GDPR Article 33-34

**Breach Definition:**

Breach = unlawful or accidental processing event resulting in personal data destruction, loss, alteration, unauthorized disclosure, or unauthorized access.

**Breach Notification to Authority (Article 33):**

- Authority notification required within 72 hours of breach discovery (unless no risk to rights/freedoms)
- Notification must include: Breach description, data subjects affected, categories, likely consequences, remediation measures, DPO contact point
- Exemption: Notification not required if data protected by encryption/pseudonymization (unrecoverable by attacker)
- Notification timeline: 72 hours from discovery (not immediately upon incident detection); allows for fact-finding and risk assessment

**Breach Notification to Data Subjects (Article 34):**

- Data subject notification required if breach likely to result in high risk to rights/freedoms
- High risk factors: Loss of financial data, health information, authentication data (passwords), sensitive personal information, large-scale breach affecting many subjects
- Notification timing: Without undue delay; minimum same-day/next-day (depends on discovery timeline)
- Notification method: Email preferred; SMS or phone for urgent matters
- Notification content: Breach description in plain language, likely consequences, remediation measures, DPO contact
- Notification language: Data subject's native language or organization's primary communication language

**Breach Log and Investigation:**

- All breaches logged in breach register with: Date discovered, date of incident (if earlier), description, data subjects affected, record count, remediation actions
- Investigation conducted within 48-72 hours including: Root cause analysis (technical failure, human error, policy breach), scope assessment (data count, data types), impact assessment (regulatory notification required?)
- Investigation findings documented; corrective actions assigned to prevent recurrence

### Consent Management

**Consent Requirements:**

Consent = freely given, specific, informed, unambiguous affirmative action confirming agreement to processing.

Non-compliant consent:

- Pre-ticked boxes (opt-out model)
- Bundled consent (linking unrelated processing)
- Consent coerced by conditional service provision
- Consent requested from children < 16 without parental consent

**Compliant Consent Procedures:**

- Separate checkbox per processing purpose (not bundled)
- Plain language explanation of processing and purpose
- Clear opt-in (not pre-ticked)
- Documented proof of consent: timestamp, IP address, purpose confirmed, consent withdrawal process explained
- Consent withdrawal: Can withdraw at any time via simple method (email unsubscribe, account settings, etc.)

**Consent Language Requirement:**

- Consent requested in data subject's language (not generic privacy policy)
- "I consent to receive marketing emails about product updates and offers" (specific, not "consent to data processing")
- Consent screenshots/logs retained for audit proof

### Data Governance and Privacy by Design

**Privacy-by-Design Principle:**

- All new systems, products, processes, and data processing activities designed with privacy protections from inception
- Privacy requirements incorporated into system design, not added retroactively
- Privacy impact assessment completed before system deployment
- Data minimization enforced: Collect only data necessary for stated purpose; do not retain longer than necessary
- User controls provided: Users can access, correct, delete, and restrict their personal data

**Technical Safeguards:**

- Pseudonymization: Replace direct identifiers with pseudonyms enabling de-identification where possible
- Anonymization: Remove identifiers enabling re-identification; truly anonymous data exempt from GDPR
- Encryption: Personal data encrypted at rest (AES-256) and in transit (TLS 1.2+)
- Access controls: Role-based access; principle of least privilege
- Audit logging: All personal data access logged and auditable; unauthorized access detected and investigated

## Control Mapping

| EATGF Context                               | ISO 27001:2022                                                                                    | NIST SSDF                                                            | COBIT                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------- |
| Personal data classification and processing | A.5.1 (Policies for information security), A.8.8 (Classification of information)                  | PS-4 (Personnel security), PS-5 (Access control)                     | APO13.01 (Establish data governance framework)           |
| Data subject rights and procedures          | A.5.6 (Information security roles and responsibilities), A.8.4 (Information handling and storage) | PS-6 (Contractor security)                                           | APO13.02 (Establish information and data classification) |
| Data retention and deletion                 | A.6.8 (Backup of information), A.8.3 (Media handling), A.8.16 (Removal of access rights)          | AT-1 (Security awareness and training), CA-7 (Continuous monitoring) | DSS05.07 (Manage IT assets and configurations)           |
| Data breach investigation and notification  | A.5.26 (Response to information security incidents), A.6.10 (Incident procedures)                 | IR-4 (Incident handling), IR-5 (CIRT establishment)                  | DSS06.03 (Report security incidents)                     |
| Privacy impact assessment                   | A.5.1 (Policies), A.8.2 (Asset inventory)                                                         | PM-2 (Supply chain risk management)                                  | APO13.01 (Governance framework)                          |
| International data transfers                | A.5.23 (Information security in supplier relationships), A.8.34 (Supplier relationships)          | PS-7 (Supply chain protection)                                       | BAI05.04 (Manage third parties)                          |

## Developer Checklist

- [ ] Personal data classification framework created (Public, Internal, Personal Data, Sensitive Personal Data, Restricted) with handling requirements per classification
- [ ] Data Processing Register established and populated with all active personal data processing activities (purpose, legal basis, data categories, recipients, retention period)
- [ ] Legal basis assessment completed for all processing; documented entries in Processing Register linked to legal basis
- [ ] Privacy Impact Assessment (PIA) template created; PIA procedure documented for high-risk processing activities
- [ ] Data subject rights procedures implemented: Access requests (30-day response SLA), rectification, erasure, portability, objection, automated decision-making explanation
- [ ] Data subject request workflow configured in ticketing system (Request reception → ID verification → Data collection → Response preparation → Delivery) with timeline tracking
- [ ] Data retention and deletion policy documented with retention periods per data category; automated purge jobs configured in data systems
- [ ] Data Processing Agreements (DPA) template created with Standard Contractual Clauses (SCC) for international transfers; all current processors assessed and DPA status documented
- [ ] Consent management system implemented (separate consent per purpose, plain language, documented timestamp/IP/purpose, easy withdrawal); consent records auditable
- [ ] Breach notification procedure established with 72-hour authority notification timeline (GDPR), immediate data subject notification process (high-risk breaches), breach log maintained
- [ ] Privacy-by-design controls documented for new systems/products (data minimization, encryption, access controls, audit logging, pseudonymization where applicable)
- [ ] International data transfer mechanisms identified for all cross-border processing (adequacy decisions, SCCs, BCRs); transfer documentation completed
- [ ] Privacy training completed by all staff with access to personal data; annual training refresher scheduled
- [ ] Data Protection Officer (DPO) appointed and contact information published; DPO authority and confidentiality safeguards documented
- [ ] Privacy notice updated and published for all processing activities (collecting, tracking, automated decision-making); privacy notice includes legal basis, rights explanation, DPO contact
- [ ] Vendor processor compliance audit conducted annually; processor SOC 2/ISO 27001 audit reports collected and reviewed
- [ ] Privacy governance documentation compiled for regulatory authority inspection (Processing Register, DPAs, breach logs, PIAs, consent records, audit reports, DPO communications)

## Governance Implications

**Risk if not implemented:**

- Personal data collected and processed without documented legal basis; GDPR Article 6 violation results in regulatory finding and monetary penalty (up to EUR 20M or 4% annual revenue)
- Data subject access request ignored or delayed beyond 30 days; GDPR Article 15 violation results in regulatory finding and €1,000-€2,000 civil liability per data subject
- Data breach not reported to regulatory authority within 72 hours; GDPR Article 33 violation results in administrative fine (up to EUR 10M or 2% revenue)
- Personal data retained indefinitely; GDPR Article 5 (storage limitation) violation results in regulatory finding
- Data transferred outside EU without SCC/adequacy mechanism (Schrems II); personal data exposed to U.S. government surveillance; GDPR violation

**Operational impact:**

- Data subject rights requests (access, erasure, portability) require manual processing; high-volume organizations need 2-3 FTEs for request handling
- Privacy impact assessments required for new systems; delays system deployment by 2-4 weeks for complex processing
- Data retention policies require purge automation; infrastructure changes needed (database cleanup, backup deletion, log rotation)
- Consent management system requires integration with marketing/analytics platforms; implementation 4-8 weeks for complex tech stacks
- Processor DPA compliance audits require vendor engagement; annual audit resource commitment for 10+ processors

**Audit consequences:**

- GDPR Supervisory Authority investigation triggered by data subject complaint; investigation may require data processing audit, data subject interview, organizational interview; potential sanctions
- SOC 2 auditors validate GDPR/CCPA compliance as part of C1 (Governance) trust service criteria; gaps result in SOC 2 audit exception
- Privacy litigation from data subjects (class action for data breach, access denied, discrimination) damages organization reputation and may result in significant settlements
- Regulatory breach notification requirements (GDPR 72-hour authority notification, CCPA consumer notification) create legal liability and public reputation risk
- Pre-litigious e-discovery: Breach investigation discovery, litigation hold documentation, breach communications discoverable in litigation

**Cross-team dependencies:**

- Marketing team depends on Privacy team for consent management and processing basis approval; delays campaign launch if processing basis contested
- Product/Engineering team must implement privacy-by-design controls (data minimization, encryption, access controls); increases design/implementation effort by 10-15%
- IT Operations must implement retention policies, backup purge procedures, log deletion; infrastructure changes needed for automated purge workflows
- HR team must process employee data subject requests (access, rectification, erasure); administration burden for employee data access requests
- Sales team must track customer consent status and preferences; sales system integration required for consent verification before marketing contact
- Legal team must interpret privacy requirements, negotiate processor DPAs, respond to regulatory inquiries; legal review delays for new processing activities

## Official References

- GDPR (EU) 2016/679: General Data Protection Regulation (Articles 1-99)
- GDPR Recitals 1-173: Preamble and interpretation guidance
- California Consumer Privacy Act (CCPA) Section 1798.100-1798.185
- California Privacy Rights Act (CPRA) Amendments (2020)
- PIPEDA (Canada): Personal Information Protection and Electronic Documents Act
- LGPD (Brazil): Lei Geral de Proteção de Dados
- HIPAA (US Health Information): 45 CFR Parts 160-164
- FERPA (US Education): 20 U.S.C. § 1232g
- GLBA (US Financial): 15 U.S.C. § 6801-6809
- ISO/IEC 27001:2022 Section A.5 (Privacy controls)
- NIST SP 800-53 Revision 5 Family PS (Personnel Security)
- EU Standard Contractual Clauses (2010/87/EU, 2001/45/EU amendments)

---

**Version History**

| Version | Date       | Change Type     | Description                                              |
| ------- | ---------- | --------------- | -------------------------------------------------------- |
| 1.0     | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
