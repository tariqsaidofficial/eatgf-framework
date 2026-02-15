# 06_VENDOR_AND_THIRD_PARTY_RISK_MANAGEMENT_POLICY

| Field          | Value                                                            |
| -------------- | ---------------------------------------------------------------- |
| Document Type  | Policy                                                           |
| Version        | 1.0                                                              |
| Change Type    | Major (Initial)                                                  |
| Classification | Controlled                                                       |
| Effective Date | 2026-02-16                                                       |
| Authority      | Chief Procurement Officer and Chief Information Security Officer |
| EATGF Layer    | 04_POLICY_LAYER                                                  |
| MCM Reference  | EATGF-APO-VEN-01, EATGF-APO-VEN-02, EATGF-DSS-VEN-01             |

---

## Purpose

This policy establishes the mandatory vendor and third-party risk management framework for assessing, monitoring, and mitigating risks from external service providers, technology vendors, and suppliers. The policy applies to all vendors providing services, systems, data processing, or infrastructure. All critical vendors must undergo security assessment before contract execution. Ongoing vendor compliance monitoring is mandatory; non-compliant vendors are subject to remediation or termination.

## Architectural Position

This policy operates within **04_POLICY_LAYER** as the primary vendor risk governance document.

- **Upstream dependency:** Governance Charter (01_GOVERNANCE_CHARTER.md) establishes CPO and CISO authority for vendor management; Information Security Policy (02_INFORMATION_SECURITY_POLICY.md) defines security requirements that vendors must meet
- **Downstream usage:** Operationalized through vendor risk assessments, security questionnaires, and vendor performance monitoring maintained by Procurement and Security teams; enforced through contract terms and vendor audits
- **Cross-layer reference:** Maps to EATGF vendor controls in Layer 02 (APO-VEN domain for vendor selection and monitoring), implements MCM controls for third-party risk assessment and compliance, implements audit procedures in Layer 06 for vendor audit compliance and remediation tracking

## Governance Principles

1. **Risk-Based Assessment** – Vendor risk assessment scope and depth proportional to criticality (critical vendors = extensive assessment, low-risk vendors = basic assessment)
2. **Security by Contract** – All contract terms enforce security requirements; non-compliance provisions enable remediation or termination
3. **Continuous Monitoring** – Vendor compliance monitored continuously through automated tools and periodic audits; compliance dashboard provides real-time status
4. **Supply Chain Transparency** – Vendors required to disclose subcontractors and sub-vendors; supply chain visibility maintained for risk assessment
5. **Exit Management** – Vendor termination process defines data return, access revocation, and knowledge transfer requirements to prevent service disruption

## Technical Implementation

### Vendor Classification and Risk Levels

All vendors classified by criticality and assigned assessment scope:

| Vendor Classification | Definition                                                                                             | Assessment Depth                                                        | Monitoring Frequency          | Contract Requirements                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------- |
| **Critical**          | Processes sensitive data, manages critical infrastructure, provides authentication, handles payments   | Comprehensive security assessment, on-site audit, continuous monitoring | Quarterly compliance review   | SOC 2 Type II, ISO 27001, incident notification SLA, insurance requirements            |
| **High**              | Provides non-critical systems, processes non-sensitive customer data, provides infrastructure services | Standard security questionnaire, evidence review, semi-annual audit     | Semi-annual compliance review | Security questionnaire signed, incident notification clause, compliance certifications |
| **Medium**            | Provides standard services, limited system integration, non-sensitive data access                      | Basic security questionnaire review                                     | Annual compliance review      | Signed security agreement, standard terms and conditions                               |
| **Low**               | Provides commoditized services, no system access, no data access                                       | Vendor website review and basic documentation                           | On-demand (ad-hoc)            | Standard commercial terms                                                              |

**Classification criteria:** Determined during vendor onboarding based on:

- Data access scope (personally identifiable information, confidential business data, customer data, restricted data)
- System integration level (API access, network connectivity, infrastructure access, authentication provider)
- Business continuity impact (availability SLA, dependency criticality, alternative vendor availability)

### Vendor Assessment Framework

**Phase 1: Pre-Selection Assessment (Before Contract Negotiation)**

**For Critical Vendors:**

1. Financial stability assessment: Review annual reports, SEC filings (if public), credit ratings; assess bankruptcy risk and financial viability (minimum: positive cash flow, debt-to-equity < 2:1)
2. Business history and reputation: Confirm operating history (minimum 3 years), customer references (minimum 3 reference customers), public incidents/litigation history
3. Regulatory compliance: Confirm regulatory licenses (if applicable), compliance certifications (SOC 2, ISO 27001, HITRUST, GDPR DPA, etc.)
4. Security questionnaire (CAIQ): Vendor completes Cloud Security Alliance CAIQ questionnaire; responses reviewed against security requirements
5. Reference calls: Contact customer references to validate service quality, incident response capability, and vendor responsiveness
6. On-site audit (optional): Conduct on-site security assessment if vendor handles highly sensitive data or critical infrastructure

**For High Vendors:**

1. Financial stability assessment: Review public financial information and credit rating
2. Business history: Confirm operating history and basic customer references
3. Security questionnaire: Vendor completes security questionnaire (CAIQ or equivalent)
4. Documentation review: Review existing certifications (SOC 2, ISO 27001) and audit reports

**For Medium Vendors:**

1. Basic vendor information: Confirm business registration, contact information, banking details
2. Security questionnaire: Vendor completes abbreviated security questionnaire (10-15 key questions)
3. Certification check: Confirm relevant security certifications if applicable

**For Low Vendors:**

1. Vendor verification: Confirm vendor identity and basic business information
2. Public information review: Check vendor website for security/privacy statements

**Assessment Documentation:** All assessments documented in vendor management system (Coupa, Verawide, or equivalent) with approval signoff by CISO and CPO before contract execution.

**Phase 2: Contract Negotiation and Terms**

**Critical Security Clauses (All Critical/High Vendors):**

| Clause                        | Requirement                                                                                                                                                                  | Consequence                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Data Protection**           | Vendor bound by organization's data protection standards; sub-processors approved in advance; data location restrictions (GDPR residency, CCPA limitations)                  | Breach of clause enables contract termination                                                                    |
| **Incident Notification**     | Vendor notifies organization within 24 hours of security incident affecting organization's data; notice includes incident classification (P1-P4), scope, and mitigation plan | Failure to notify triggers financial penalty (1-3% monthly fees); repeated violations (>2) enables termination   |
| **Audit Rights**              | Organization may conduct security audits (on-site or remote) up to twice annually for critical vendors, annually for high vendors; vendor must provide evidence of controls  | Denial of audit access triggers contract review; repeated denial enables termination                             |
| **Compliance Certifications** | Vendor maintains SOC 2 Type II (annual) or ISO 27001 (biennial); vendor shares audit reports within 30 days of issuance                                                      | Expired or missing certifications trigger remediation plan; unresolved deficiencies enable termination           |
| **Business Continuity**       | Vendor maintains RTO ≤ 4 hours for critical services, ≤ 8 hours for high services; annual testing validated and documented                                                   | Missed RTO targets trigger financial credit ($5K-$25K per miss); repeated misses enable termination              |
| **Exit Management**           | Upon contract termination, vendor returns all organization data within 30 days; data destruction certified; knowledge transfer completed within 90 days                      | Failure to return data within 30 days triggers legal action and regulatory notification                          |
| **Insurance Requirements**    | Vendor maintains cyber liability insurance ($5M minimum for critical, $2M minimum for high); organization named as additional insured; insurance verified annually           | Uninsured events trigger financial liability recovery from vendor; lapsed insurance triggers contract suspension |
| **Subcontractor Approval**    | All subcontractors approved in advance; subcontractors bound by same security requirements via flow-down clauses                                                             | Unapproved subcontractors trigger contract violation; vendor must remedy or terminate subcontractor              |

**Data Processing Agreement (DPA) [GDPR/CCPA]:**

- All vendors processing personal data execute a Data Processing Agreement (DPA)
- DPA incorporates Standard Contractual Clauses (SCCs) for international data transfers (GDPR Article 46)
- Vendor confirms CCPA compliance if personal information of California residents processed
- DPA reviewed by Legal and Security teams before execution

**Contract Governance:**

- Procurement has authority to approve contracts within policy parameters
- Contracts exceeding security policy thresholds (data residency, audit rights, insurance limits) require CISO and CPO joint approval
- Security non-negotiable terms (data protection, incident notification, audit rights) cannot be waived without executive exception (CFO/CISO approval)

### Vendor Due Diligence – Subcontractor Management

**Vendor Disclosure Requirements:**

- Vendors required to disclose all subcontractors who access organization data or systems
- Disclosure includes subcontractor name, location, services provided, and data access scope
- Subcontractor disclosure updated upon contract renewal and when subcontractor changes occur

**Subcontractor Assessment:**

- Each subcontractor classified (Critical/High/Medium) based on data access and criticality
- Critical and High subcontractors undergo same assessment as vendors (financial review, security questionnaire, audit rights)
- Medium and Low subcontractors assessed via questionnaire
- Subcontractor refusal to disclose security information results in vendor being marked non-compliant; vendor must substitute subcontractor or contract may be terminated

**Flow-down Clauses:**

- Vendor contracts include mandatory flow-down clauses requiring subcontractors to meet same security requirements
- Subcontractor assessments and compliance monitoring delegated to vendor; vendor held accountable for subcontractor compliance
- Organization retains right to audit subcontractors directly

### Ongoing Vendor Compliance Monitoring

**Tier 1: Critical Vendor Monitoring**

Monitoring cadence:

- **Monthly:** Automated alert verification (vendor confirms no unreported incidents)
- **Quarterly:** Compliance status dashboard review (certifications valid, audit rights exercised)
- **Semi-annual:** Security questionnaire refresh (vendor confirms no material changes in security controls)
- **Annual:** Comprehensive compliance review (audit report review, RTO/RPO validation, insurance verification) and on-site audit if indicated
- **Continuous:** Incident notification and response monitoring

Performance data tracked:

- Uptime and availability metrics (SLA compliance)
- Incident reports (frequency, severity, resolution time)
- Audit findings (prior findings remediation status, new findings)
- Certification status (SOC 2, ISO 27001 validity dates)
- Subcontractor changes and compliance status
- Insurance coverage validity and coverage limits

**Tier 2: High Vendor Monitoring**

- **Semi-annual:** Compliance review (certifications, audit status, incident review)
- **Annual:** Security questionnaire refresh, audit report review
- **Continuous:** Incident notification monitoring

**Tier 3: Medium Vendor Monitoring**

- **Annual:** Basic compliance check-in (certifications, operational status)

**Tier 4: Low Vendor Monitoring**

- **Ad-hoc:** Monitoring only if incident or concern raised

**Monitoring Tools and Process:**

- Vendor management system (Coupa, Verawide, or equivalent) tracks all compliance data and generates alerts
- Monthly compliance dashboard distributed to CISO, CPO, and account managers
- Quarterly executive summary prepared for governance committee
- Non-compliance escalated to vendor account manager for remediation; remediation plan required within 15 days

### Vendor Non-Compliance and Remediation

**Non-Compliance Triggers:**

1. Missed SLA targets (uptime, RTO, responsiveness)
2. Security certifications expired (SOC 2, ISO 27001)
3. Failure to undergo required audit within scheduled window
4. Incident not reported within contractual notification SLA
5. Unauthorized subcontractor engagement
6. Audit denial or obstruction
7. Insurance lapsed or coverage insufficient
8. Material security control failure identified

**Remediation Process:**

**Severity Level 1 (Minor Procedural):**

- Example: Certification renewal late by < 30 days, non-material audit finding
- Action: Written reminder to vendor; 15-day cure period
- Escalation: If not cured: Level 2 (see below)

**Severity Level 2 (Material Control Deficiency):**

- Example: Certification lapsed >30 days, audit finding affecting control effectiveness, incident reporting delayed
- Action: Formal remediation notice; 30-day cure period; financial penalty (1-2% monthly fees); compliance monitoring increased to weekly
- Escalation: If not cured: Level 3 (see below)

**Severity Level 3 (Critical Risk):**

- Example: Incident with customer data exposure not reported, unapproved subcontractor processing data, persistent SLA failures, audit denial
- Action: Contract suspension notice; 10-day cure period; executive escalation (CISO/CPO); option to terminate contract without penalty, or require comprehensive remediation plan with executive monitoring
- Escalation: If not cured: Contract termination

**Remediation Tracking:**

All remediation tracked in vendor management system with documented evidence of completion. Compliance committee reviews remediation status monthly until closure.

**Vendor Termination Process:**

Upon contract termination:

1. **Transition period:** Notify vendor of termination with 30-day notice (or shorter if critical non-compliance); establish transition schedule
2. **Data recovery:** Vendor returns all organization data and systems access restored to organization or successor vendor
3. **Data destruction:** Vendor certifies destruction of organization data (certificate of destruction retained)
4. **Knowledge transfer:** Vendor documents current state and configuration; technical teams briefed
5. **Access revocation:** All vendor access revoked (accounts, VPN, facilities, APIs)
6. **Escrow and source code:** If applicable, source code and escrow materials released to organization
7. **Legal settlement:** Final invoicing, dispute resolution, insurance claims (if applicable) processed
8. **Post-termination audit:** 90 days post-termination, organization may conduct final audit to verify data destruction and access revocation

### Vendor Security Incident Response

**Incident Notification to Vendor:**

- If organization's incident is caused by vendor, vendor notified within 24 hours with incident classification, scope, and initial findings
- Vendor required to provide incident assessment within 48 hours including root cause analysis, remediation plan, and prevention measures

**Vendor-Reported Incidents:**

- If vendor security incident affects organization's data, vendor must notify within 24 hours per contract terms
- Notification must include:
  - Incident description and timeline
  - Organization data affected (dataset, record count, data types)
  - Vendor's containment and mitigation actions
  - Impact assessment (likelihood of data exposure, regulatory notification requirement)
  - Remediation timeline
  - Prevention measures
- Organization conducts investigation within 72 hours; may require vendor incident investigation report and forensic evidence
- If regulatory notification required (GDPR 72-hour requirement, CCPA, etc.), organization proceeds with notification independent of vendor; vendor breach notification insurance may provide coverage

**Escalation and Recovery:**

- P1 vendor incidents (customer data exposure) escalate to CISO and Legal immediately; potential contract termination evaluated
- P2-P3 vendor incidents (non-critical data exposure, service disruption) escalate to account manager and CISO; remediation plan required
- Post-incident review conducted within 5 business days; root cause documented and corrective actions assigned

## Control Mapping

| EATGF Context                             | ISO 27001:2022                                                                                     | NIST SSDF                                     | COBIT                                                                               |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------- |
| Vendor risk assessment and classification | A.5.23 (Information security for supplier relationships), A.8.34 (Supplier relationships—security) | PM-2 (Supply Chain Risk Management), PM-9     | GOV05.02 (Governance of external service delivery), BAI05.04 (Manage third parties) |
| Contract terms and SLAs                   | A.8.34, A.8.35 (Supplier service delivery management)                                              | PS-7 (Supply Chain Protection)                | BAI05.04 (Service delivery agreement coordination)                                  |
| Ongoing compliance monitoring             | A.8.35 (Monitoring and review of supplier services), A.8.17 (Monitoring)                           | PM-9 (Monitoring supply chain compliance)     | MEA01.01 (Monitor governance objectives)                                            |
| Incident management for vendors           | A.5.23, A.6.10 (Incident management)                                                               | IR-1 (Coordination), IR-4 (Incident handling) | DSS06.03 (Report security incidents)                                                |
| Subcontractor management                  | A.5.23 (Supply chain visibility), A.8.34 (Subcontractor requirements)                              | PM-2 (Subcontractor security requirements)    | GOV05.02 (Third-party governance)                                                   |
| Vendor termination and exit               | A.8.34, A.8.35, A.5.23 (Data return and destruction)                                               | PS-7 (Supply chain exit)                      | BAI01.03 (Define and maintain service agreements)                                   |

## Developer Checklist

- [ ] Vendor classification framework defined (Critical/High/Medium/Low) with data access scope and assessment depth criteria documented
- [ ] Vendor risk assessment template created using Cloud Security Alliance CAIQ (Critical vendors) and abbreviated questionnaire for Medium/Low vendors
- [ ] Pre-selection assessment procedure documented including financial stability, business history, regulatory compliance, and reference checks
- [ ] Critical security clauses drafted for contracts (data protection, incident notification, audit rights, certifications, BC/DR, exit management, insurance, subcontractor approval)
- [ ] Data Processing Agreement (DPA) template created with Standard Contractual Clauses (SCC) for GDPR compliance
- [ ] Vendor management system (Coupa, Verawide, or equivalent) configured with vendor classification, assessment tracking, and compliance monitoring workflow
- [ ] On-site audit procedure documented for critical vendors including scope (security controls, access controls, data handling, incident response)
- [ ] Subcontractor disclosure requirement added to vendor contracts; subcontractor assessment and flow-down clause procedures documented
- [ ] Critical vendor monitoring dashboard created with monthly/quarterly/annual compliance tasks (certifications, audit rights, SLA tracking, incident monitoring)
- [ ] Non-compliance remediation process documented with severity levels, cure periods, financial penalties, and escalation triggers
- [ ] Vendor incident notification procedure documented with 24-hour notification SLA and required incident report contents (RCA, impact, remediation)
- [ ] Vendor termination checklist created covering data return, access revocation, knowledge transfer, and post-termination audit procedures
- [ ] Insurance verification process implemented; annual insurance certificate collection and verification automated
- [ ] Contract governance process documented with authority levels (CPO for standard contracts, CISO/CPO for security escalations)
- [ ] Quarterly vendor compliance summary prepared for executive governance; vendor risk trends analyzed

## Governance Implications

**Risk if not implemented:**

- Vendor security assessment skipped; vendor with weak controls processes sensitive data or accesses critical systems (data breach, system compromise, service disruption)
- Vendor incidents not reported; organization unaware of data exposure; regulatory notification deadline missed (GDPR 72-hour breach notification failure, legal penalty)
- Subcontractors not assessed; organization's data processed by unknown third parties without security oversight (supply chain risk materialization)
- Vendor contract lacks security terms; vendor can refuse security audits or avoid incident notification (governance framework bypassed)
- No monitoring; vendor SOC 2 certification lapses, insurance lapses, incident ignored (compliance gap, SLA miss, operational blind spot)

**Operational impact:**

- Vendor assessment process adds 30-60 days to vendor onboarding timeline (delays critical acquisitions unless process accelerated)
- Annual audit rights require vendor cooperation and require organization's audit resources (30-40 hours per critical vendor audit)
- Ongoing monitoring requires vendor management discipline; non-compliant vendors escalated, may require replacement if not remediated (operational friction)
- Vendor termination triggers complex data migration and access cutover; inadequate planning causes service disruption or data loss
- Insurance requirements add cost to vendor contracts; vendor cost increases passed to organization

**Audit consequences:**

- ISO 27001 auditors validate vendor assessment and monitoring against A.5.23 and A.8.34; absence of documented vendor assessments results in audit non-conformance
- SOC 2 auditors specifically validate third-party risk assessment; vendor assessment gaps result in SOC 2 audit exception
- GDPR DPA compliance verification: auditors confirm DPAs in place for all data processors; missing DPAs result in regulatory audit findings
- PCI-DSS auditors require validated Requirement 12.8 (Maintain and implement policies and procedures over third parties); inadequate vendor management results in PCI-DSS non-conformance
- Supply chain security regulations (NIST SP 800-53 PM-9, EO 14028) require documented vendor risk management; undocumented processes result in regulatory audit findings

**Cross-team dependencies:**

- Procurement depends on CISO security assessment; delayed CISO reviews slow contract negotiation
- IT operations must implement vendor monitoring tools and dashboard; requirement for SIEM integration and compliance tool configuration
- IT Security must conduct vendor audits; resource availability impacts audit scheduling and frequency
- Legal depends on CISO for security clauses and contract review; contract term negotiations may stall on security issues
- Finance must budget for vendor assessment costs (on-site audits, assessment tools, qualified auditors); cost control may result in reduced assessment depth
- Business unit leads select vendors but must provide security requirements and assessment participation (reference calls, audit scheduling)
- Incident response team must support vendor incident investigations and regulatory notification decisions; vendor incident timelines drive incident response processes

## Official References

- NIST SP 800-53 PM-9: Supply Chain Risk Management
- NIST SP 800-53 PS-7: Supply Chain Protection
- NIST SP 800-53 PM-2: Supply Chain Risk Assessment and Management
- ISO/IEC 27001:2022 Control A.5.23 (Information security for supplier relationships), A.8.34 (Supplier relationships), A.8.35 (Supplier service delivery management)
- ISO/IEC 27001:2022 Annex SL (Integration sections for third-party risk management)
- Cloud Security Alliance CAIQ (Cloud Controls Matrix)
- GDPR Articles 28-31 (Data Processing Agreements and Processor Requirements)
- CCPA Section 1798.140(ad) (Service Provider Definition and Requirements)
- CMMC (Cybersecurity Maturity Model Certification) Level 3 and 5 practice PS.3.3 (Third-party risk assessment)

---

**Version History**

| Version | Date       | Change Type     | Description                                              |
| ------- | ---------- | --------------- | -------------------------------------------------------- |
| 1.0     | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
