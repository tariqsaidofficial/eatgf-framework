# AUDIT_SCHEDULE_STANDARD

| Field          | Value                                           |
| -------------- | ----------------------------------------------- |
| Document Type  | Standard (Audit Methodology)                    |
| Version        | 1.0                                             |
| Change Type    | Major (Initial)                                 |
| Classification | Controlled                                      |
| Effective Date | 2026-02-16                                      |
| Authority      | Chief Audit Officer and Internal Audit Function |
| EATGF Layer    | 06_AUDIT_AND_ASSURANCE                          |
| MCM Reference  | EATGF-MEA-AUD-01, EATGF-MEA-AUD-02              |

---

## Purpose

This standard establishes the mandatory audit schedule for assessing compliance with EATGF controls across the organization. The schedule defines the annual audit cycle, control rotation logic, sampling methodology, and audit timing. All controls are systematically audited on defined cadence; audit results documented in audit reports. The schedule ensures comprehensive control coverage while respecting organizational operations.

## Architectural Position

This standard operates within **06_AUDIT_AND_ASSURANCE** as the audit scheduling and planning methodology.

- **Upstream dependency:** Internal Audit Procedure (06_AUDIT_AND_ASSURANCE/INTERNAL_AUDIT_PROCEDURE_v1.0.md) defines audit methodology; Master Control Matrix (Layer 00) defines 35 EATGF controls subject to audit
- **Downstream usage:** Schedule drives audit planning, resource allocation, control owner notifications, and evidence collection schedules; audit results tracked in corrective action register and reported to governance committee
- **Cross-layer reference:** Supports all control compliance monitoring; audit schedule integrated with performance monitoring (Layer 08 KPI tracking), policies/procedures (Layers 04-05 compliance validation), maturity assessment (Layer 03 effectiveness measurement)

## Governance Principles

1. **Systematic Coverage** – All 35 MCM controls audited annually on documented schedule; no controls skipped or overlooked
2. **Risk-Based Rotation** – High-risk controls audited more frequently (quarterly); supporting controls audited annually
3. **Equitable Distribution** – Audit work evenly distributed across 4 quarters; no quarter has >40% of annual audit volume
4. **Evidence-Driven** – Audit schedule synchronized with evidence collection; control owners prepare evidence per audit timeline
5. **Transparency** – Audit schedule published in advance (January); control owners notified minimum 30 days before audit date

## Technical Implementation

### Annual Audit Cycle Structure

**5-Quarter Rolling Audit Schedule:**

The audit year runs September 2025 – August 2026 (correlating to fiscal year). Annual cycle divided into 5 phases:

| Phase       | Period              | Duration             | Scope                                   | Deliverable                                        |
| ----------- | ------------------- | -------------------- | --------------------------------------- | -------------------------------------------------- |
| **Phase 0** | Sept 2025           | 4 weeks              | Planning & prep                         | Annual audit plan approved by governance committee |
| **Phase 1** | Oct 2025 – Dec 2025 | 12 weeks (Q1)        | Full audit of 8-10 critical controls    | Phase 1 audit report with findings and ratings     |
| **Phase 2** | Jan 2026 – Mar 2026 | 12 weeks (Q2)        | Rolling sample of 8-10 controls         | Phase 2 audit report with findings and ratings     |
| **Phase 3** | Apr 2026 – Jun 2026 | 12 weeks (Q3)        | Rolling sample of 8-10 controls         | Phase 3 audit report with findings and ratings     |
| **Phase 4** | Jul 2026 – Aug 2026 | 8 weeks (Partial Q4) | Close-out and review remaining controls | Annual audit summary report + board presentation   |

**Total audit capacity:** 35 controls / 5 quarters = 7 controls per quarter average; adjusted by control criticality and complexity.

### Control Classification and Audit Frequency

All 35 EATGF controls classified by audit frequency:

| Frequency                | Definition                                                                         | # of Controls  | Audit Scope                                                | Rotation                       | Examples                                                                                   |
| ------------------------ | ---------------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------ |
| **Critical Annual**      | Foundational controls with organization-wide impact; security-critical             | 8-10           | Full control audit with design review, operational testing | Audited every 12 months        | Governance Charter, Master Control Matrix, Access Control Policy, Incident Response, BC/DR |
| **High Annual**          | Core operational controls with significant risk impact                             | 12-15          | Full control audit with sampling                           | Audited every 12 months        | Information Security Policy, Data Governance, Vendor Risk, Change Management               |
| **Supporting Annual**    | Control supporting higher-level controls; lower independent risk                   | 10-15          | Sampling-based audit; design review optional               | Audited every 12 months        | Logging and Monitoring, Backup & Recovery, Training & Awareness                            |
| **Quarterly Risk-Based** | Controls identified as higher-risk by governance committee or prior audit findings | 2-3 (variable) | Shorter audit focused on remediation progress              | Re-audited if deficiency found | Controls with prior audit exceptions, controls undergoing remediation                      |

**Classification maintained in:** Audit Schedule Register (maintained by Chief Audit Officer); reviewed and updated annually in August.

### Quarterly Audit Schedule – Phase 1 (OCT-DEC 2025) Sample

**Phase 1Q1 – October 2025 (Weeks 1-3):**

| Week | Control Code      | Control Name                           | Audit Type     | Auditor Assigned | Evidence Due |
| ---- | ----------------- | -------------------------------------- | -------------- | ---------------- | ------------ |
| Wk1  | Pre-audit         | Audit Prep & Planning                  | Administrative | Audit Manager    | -            |
| Wk2  | EATGF-EDM-GOV-01  | Governance Charter Effectiveness       | Full Audit     | Auditor A + B    | Sept 30      |
| Wk2  | EATGF-APO-SEC-01  | Information Security Policy Compliance | Full Audit     | Auditor C        | Sept 30      |
| Wk3  | EATGF-DSS-SEC-01  | Access Control Implementation          | Full Audit     | Auditor D + E    | Oct 7        |
| Wk3  | EATGF-APO-RISK-01 | Risk Assessment & Management           | Full Audit     | Auditor A        | Oct 7        |

**Phase 1Q2 – November 2025 (Weeks 5-9):**

| Week  | Control Code     | Control Name                            | Audit Type | Auditor Assigned | Evidence Due |
| ----- | ---------------- | --------------------------------------- | ---------- | ---------------- | ------------ |
| Wk5-6 | EATGF-BAI-CHG-01 | Change Management Implementation        | Full Audit | Auditor F        | Oct 28       |
| Wk6-7 | EATGF-DSS-INC-01 | Incident Response Capability Maturity   | Full Audit | Auditor G + H    | Nov 4        |
| Wk8   | EATGF-APO-BCM-01 | Business Continuity Plan Readiness      | Full Audit | Auditor C        | Nov 18       |
| Wk9   | EATGF-BAI-REC-01 | Disaster Recovery Testing Effectiveness | Full Audit | Auditor I        | Nov 25       |

**Phase 1Q3 – December 2025 (Weeks 11-13):**

| Week    | Control Code     | Control Name           | Audit Type     | Auditor Assigned | Evidence Due |
| ------- | ---------------- | ---------------------- | -------------- | ---------------- | ------------ |
| Wk11    | EATGF-DSS-VEN-01 | Vendor Risk Management | Full Audit     | Auditor J        | Dec 2        |
| Wk12-13 | Phase 1          | Reporting & Close-out  | Administrative | Audit Manager    | -            |

**Q1 Audit Load:** 9 controls audited; 5-6 full audits requiring design review + testing; 8 audit team members required (~250-300 hours total).

### Control Audit Roadmap – 12-Month View

**Year Cycle: September 2025 – August 2026**

**Critical Controls (Required Full Audit Every 12 Months):**

| Control                                        | Q1  | Q2  | Q3  | Q4  |
| ---------------------------------------------- | --- | --- | --- | --- |
| EATGF-EDM-GOV-01 (Governance Charter)          | X   |     |     |     |
| EATGF-APO-SEC-01 (Information Security Policy) | X   |     |     |     |
| EATGF-DSS-SEC-01 (Access Control)              | X   |     |     |     |
| EATGF-APO-BCM-01 (Business Continuity)         | X   |     |     |     |
| EATGF-DSS-INC-01 (Incident Response)           | X   |     |     |     |
| EATGF-APO-VEN-01 (Vendor Risk Mgmt)            | X   |     |     |     |
| EATGF-DSS-PRI-01 (Data Privacy)                |     | X   |     |     |
| EATGF-BAI-CHG-01 (Change Management)           | X   |     |     |     |
| EATGF-BAI-REC-01 (DR Testing)                  | X   |     |     |     |
| EATGF-APO-POL-01 (Acceptable Use)              |     |     | X   |     |

**High Risk Tier (Full Audit):**

15 controls rotated across Q2-Q3 and Q4; 3-4 controls per quarter.

**Supporting Tier (Sampling Audit or Focused Review):**

10-12 controls rotated across Q2-Q4; 2-3 controls per quarter.

**Quarterly Risk-Based Audits (As Required):**

Controls with prior audit exceptions or remediation in progress.

### Audit Timeline and Evidence Collection

**T-60 Days (Before Audit Period Starts):**

- Audit schedule published; control owners notified
- Audit objectives and scope communicated to control owners
- Preliminary evidence list sent to control owners (what to prepare)

**T-30 Days (Before Control Audit Date):**

- Control owners submit preliminary evidence (policies, test results, training records, logs, approvals)
- Auditors review evidence for completeness; request clarifications
- Audit preliminary findings shared with control owners (design defects, missing controls, etc.)

**Audit Week (Control Audit Execution):**

- Exit meeting with control owners; findings summarized, corrective actions discussed
- Field audit 2-3 days per critical control; 1 day per supporting control
- Interviews with control owners, operators, process participants
- Testing: Document review, walkthrough procedures, sample testing (30-50 transactions), configuration review, log review
- Findings classified: Design defect, operational defect, control gap, compliance miss

**T+10 Days (After Audit):**

- Draft audit findings issued to control owners for factual accuracy review
- Control owners have 5 business days to respond to findings (dispute, clarification, remediation plan)

**T+20 Days:**

- Final audit report issued with findings, observations, and recommendations
- Findings classification: Critical (control not operating), Major (control defective), Minor (design could improve)
- Corrective action plan required for all findings; remediation timeline assigned

### Evidence Requirements by Control Type

**Governance Controls** (Charter, Policy, Risk Mgmt, Maturity Model):

Evidence required (examples):

- Approved policy documents (Board/Executive approval, effective date, version control)
- Policy communication records (employee training completion, acknowledgment forms)
- Policy compliance monitoring (audit of policy implementation across organization)
- Review/approval records (annual policy review, governance committee approval)
- Incident investigation files (evidence policy was enforced when violations occurred)

Typical audit findings:

- Policy not approved by appropriate authority
- Policy not communicated to all affected personnel
- Policy not enforced (violations not addressed)
- Policy outdated (no annual review)

**Operational Controls** (Access Control, Change Mgmt, Incident Response):

Evidence required (examples for Access Control):

- Access control policy (whether it exists and is comprehensive)
- Role definitions (documented approved list of defined roles)
- Access provisioning records (requests, approvals, implementation, 5-10 sample audits)
- Quarterly access reviews (evidence managers reviewed access, identified inappropriate access, remediated)
- Access revocation procedures (employee termination checklist, access removal evidence, post-termination verification)
- Privilege escalation controls (who can grant admin, approval process, 3-5 sample audits)
- Abandoned account management (process to identify unused accounts, evidence accounts disabled after 60 days inactivity)

Typical audit findings:

- Access provisioning not approved
- Access reviews not conducted
- Inappropriate access not discovered or remediated
- Abandoned accounts active and un-monitored
- Privilege escalation not documented/approved

**Technology Controls** (Logging, Backup, Encryption, Monitoring):

Evidence required (examples for Logging):

- Logging configuration documentation (what events logged, retention periods, log formats)
- Log aggregation system documentation (SIEM configuration, log forwarding rules)
- Compliance monitoring (logs reviewed regularly for compliance violations, evidence of investigation)
- Evidence the logs are intact (log integrity validation, tamper-proof mechanisms)
- Sample log analysis (auditor reviews 50-100 recent log entries for accuracy, completeness)
- Incident investigation reliance on logs (evidence logs used in recent incidents)

Typical audit findings:

- Logs not captured (disabled logging, sparse log coverage)
- Logs not retained (short retention period, premature deletion)
- Logs not reviewed (no evidence of log analysis)
- Logs not secure (readable/modifiable without authorization)

**Assurance Controls** (Testing, Monitoring, Auditing):

Evidence required (examples for Incident Response Testing):

- Test plan (defined tabletop exercise, full recovery drill, or security event simulation)
- Test schedule (annual scheduled test date, participant list)
- Test execution records (actual test performed, timeline, participant attendance, responses)
- Test findings (control gaps identified, SLA misses documented)
- Corrective action plan (findings documented, remediation responsibility assigned, timeline defined)
- Remediation evidence (findings closed, next test does not repeat prior finding)

Typical audit findings:

- Testing not performed (no evidence of annual test)
- Testing not documented (test occurred, but no records/recordings)
- Testing findings not tracked (test revealed gaps, no corrective action assigned)
- Repeated findings (same gap identified in current and prior year test)

### Audit Resource Planning

**Annual Audit Team:**

- Chief Audit Officer (1 FTE): Oversight, governance committee reporting, audit plan approval
- Audit Manager (1 FTE): Audit scheduling, auditor assignment, quality review, evidence management
- Senior Auditors (2 FTE): Lead audits on critical controls, mentor junior auditors
- Auditors (3-4 FTE): Conduct audits on assigned controls, document findings, evidence collection

**Total Audit Capacity:** 7-8 FTE equivalent (in-house + contract audit resources)

**Estimated Annual Audit Hours:**

| Phase     | Controls                 | Hours per Control | Total Hours   | FTE Allocation |
| --------- | ------------------------ | ----------------- | ------------- | -------------- |
| **Q1**    | 9 (8 critical)           | 25-30 hours       | 240 hours     | 1.5 FTE        |
| **Q2**    | 9 (4 high, 5 supporting) | 15-25 hours       | 180 hours     | 1.1 FTE        |
| **Q3**    | 9 (3 high, 6 supporting) | 12-20 hours       | 150 hours     | 0.95 FTE       |
| **Q4**    | 8 (close-out, summary)   | 10-15 hours       | 100 hours     | 0.6 FTE        |
| **Total** | 35 controls              | 12-25 hours avg   | **670 hours** | **4.2 FTE**    |

**Resource assumptions:** In-house auditors handle 70% of audit work (~470 hours); contract auditors handle 30% (~200 hours) for expertise/surge capacity.

### Key Audit Milestones and Deliverables

**Annual Audit Plan (January):**

- Approved schedule for all 35 controls with rotation logic documented
- Risk assessment for quarterly risk-based audits (which controls to prioritize if audit budget exceeded)
- Auditor assignments and skill mapping (complex controls assigned to experienced auditors)
- Board/governance approval of audit plan

**Quarterly Audit Reports (March, June, September, December):**

- Summary of controls audited in quarter
- Findings by severity (critical, major, minor)
- Corrective action summary (prior quarter findings status)
- Executive summary (audit metrics, trends, risk assessment)

**Annual Audit Summary Report (September):**

- All 35 controls audit status for 12-month period
- Controls audited (35/35 = 100% coverage)
- Overall compliance rating (% of controls operating effectively)
- Systemic deficiencies identified (patterns, repeating findings, design gaps)
- Recommendations for control design/operating model improvements
- Board audit committee presentation with visual dashboard

**Auditor Qualification Management:**

- All auditors minimum 2-3 years audit experience
- IATIA (Institute of Auditors) or equivalent certification required for senior auditors
- Domain expertise maintained through training (security, technology, operations, governance)
- Annual auditor training on new controls, regulatory updates, emerging risks

### Audit Schedule Governance

**Annual Review (August):**

- Audit schedule reviewed against control environment changes
- New controls (if added to MCM) incorporated into next year's schedule
- Decommissioned controls removed from schedule
- Risk assessment updated; audits for high-risk areas increased/prioritized

**Audit Committee Oversight:**

- Monthly audit status dashboard shown to governance committee (% complete, findings summary, remediation status)
- Quarterly audit reports reviewed by governance committee with recommendation discussion
- Annual audit plan approved by board audit committee
- Audit effectiveness assessed annually (audit findings later confirmed during management control testing; audit relevance validated)

**Escalation Triggers:**

- Critical findings (control not operating) trigger executive escalation; remediation plan due within 10 days
- Repeated findings (same control failed in consecutive years) indicate systemic issue; executive investigation required
- Systemic deficiencies affecting >5 controls trigger control framework re-evaluation (MCM, policies, operating procedures)
- Audit gaps (control not audited in 24 months) trigger backlog remediation; catch-up audit schedule created

## Control Mapping

| EATGF Context                  | ISO 27001:2022                                                                                         | NIST SSDF                                                     | COBIT                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Audit planning and scheduling  | A.8.17 (Monitoring, measurement, analysis and evaluation), A.6.7 (Management of information security)  | CA-7 (Continuous monitoring), CA-8 (Penetration testing)      | MEA01.01 (Monitor governance), MEA02.01 (Assess internal control effectiveness) |
| Annual control audit cycle     | A.8.15 (Logging), A.8.16 (Monitoring), A.8.17 (Analysis and evaluation)                                | CA-2 (Security assessment), CA-7 (Continuous monitoring)      | MEA02.01 (Assess control effectiveness)                                         |
| Evidence collection and timing | A.8.17 (Monitoring records), A.7.1 (Personnel with access)                                             | CA-2 (Assessor competency), AU-5 (Response to audit findings) | MEA03.01 (Collect, process data)                                                |
| Audit reporting and findings   | A.8.17 (Reporting), A.6.7 (Management review)                                                          | CA-8 (Continuous monitoring reporting)                        | MEA01.01 (Monitor awareness)                                                    |
| Corrective action tracking     | A.5.26 (Response to incidents), A.6.7 (Management review), A.8.36 (Evaluation of supplier performance) | CA-7 (Continuous monitoring), IR-4 (Incident handling)        | MEA02.01 (Assess improvements)                                                  |

## Developer Checklist

- [ ] Annual audit schedule created for 35 EATGF controls with quarterly rotation logic (Critical Q1, High spread Q2-Q3, Supporting spread Q2-Q4)
- [ ] Control classification audit frequency documented (Critical Annual, High Annual, Supporting Annual, Quarterly Risk-Based) with # of controls per category
- [ ] Quarterly audit roadmap created showing control sequence, auditor assignment, evidence due dates for 12-month cycle
- [ ] Full 5-quarter phase plan documented (Phase 0: Planning, Phase 1-3: Execution, Phase 4: Close-out) with weekly milestone timeline
- [ ] Evidence requirements specified by control type (Governance, Operational, Technology, Assurance) with examples of required evidence documentation
- [ ] Audit team resource plan documented: Chief Audit Officer (1 FTE), Audit Manager (1 FTE), Senior Auditors (2 FTE), Auditors (3-4 FTE); total 7-8 FTE with allocation by quarter
- [ ] Annual audit hour estimate calculated (~670 hours total, 4.2 FTE equivalent); in-house vs. contract audit resource mix defined (70/30 split)
- [ ] Audit timeline and evidence collection schedule documented: T-60 days (notification), T-30 days (evidence due), Audit Week (execution), T+10 (draft findings), T+20 (final report)
- [ ] Audit risk assessment completed identifying controls with higher risk/higher audit frequency (2-3 quarterly risk-based controls identified for pilot year)
- [ ] Monthly audit status dashboard created for governance committee tracking (% complete, findings by severity, remediation status, upcoming milestones)
- [ ] Annual audit plan template created with approval authority (Board/Audit Committee) and published January of each fiscal year
- [ ] Quarterly audit report template created with sections: controls audited, findings by severity, corrective action status, executive summary
- [ ] Annual audit summary report template created for board presentation with: 35/35 controls audit completion, overall compliance rating, systemic recommendations
- [ ] Auditor qualification standards defined: 2-3 years audit experience minimum, IATIA certification for senior auditors, domain expertise training maintained
- [ ] Audit governance process documented: Annual review (August), selection/prioritization of quarterly risk-based controls, governance committee approval, escalation triggers
- [ ] Audit schedule published and communicated to all control owners minimum 90 days before audit cycle begins (September)

## Governance Implications

**Risk if not implemented:**

- Audit schedule non-existent; audits conducted ad-hoc; some controls never audited (no assurance of control operating effectiveness)
- Audit schedule too ambitious relative to resources; audits rushed or incomplete, findings missed (surface-level audits, control gaps not detected)
- Audit schedule does not include high-risk controls; high-risk controls audited infrequently; control defects accumulate unremediated
- No evidence collection timeline; control owners unprepared for audits; audit scope reduced, findings incomplete

**Operational impact:**

- Audit resource planning requires 4+ FTE dedicated staff annually (significant personnel cost)
- Control owners must dedicate time to evidence collection; estimated 10-20 hours per control per year in documentation work
- Audit execution interrupts normal operations (interviews with process owners, system access for testing); operational throughput reduced during audit intensive periods
- Audit findings may require remediation work (policy updates, control re-design, procedure changes); estimated 50-100 hours per major finding remediation
- Governance committee time required for monthly dashboard reviews and quarterly reporting; 2-3 hours per month governance committee time

**Audit consequences:**

- ISO 27001 auditors require evidence of control audit program; missing audit schedule results in audit non-conformance
- SOC 2 auditors validate audit frequency and control testing; inadequate audit schedule documented in SOC 2 audit report
- Regulatory audits (GDPR, PCI-DSS, HIPAA) expect control audit evidence; absence of audit program results in audit findings
- Control audit findings cascade to regulatory audits; auditors use control audit findings to scope regulatory audit testing
- Litigation discovery: Audit findings discoverable in litigation; control gaps documented in audit reports inform litigation strategy

**Cross-team dependencies:**

- Control owners must coordinate with auditors to provide evidence; competing operational priorities may delay evidence collection
- IT operations must support auditor access for system review, log analysis, configuration review; system access management required
- Finance/HR must provide personnel records, approval documentation, training records for auditor review
- Governance committee must make time for monthly/quarterly audit reporting; executive schedule coordination required
- Board audit committee must approve annual audit plan; audit schedule dependent on board meeting calendars

## Official References

- NIST SP 800-53 Revision 5: Control CA-2 (Security Assessment) and CA-7 (Continuous Monitoring)
- ISO/IEC 19011:2018 Guidelines for Auditing Management Systems
- ISO/IEC 27001:2022 Section 9.2 (Internal Audit)
- COBIT 2019 Process MEA02: Monitor, Assess and Assure IT Compliance
- Internal Audit Standards (Internal Audit Institute, IATIA)
- ISACA CISA Review Manual: Chapter on IT Audit Planning and Execution

---

**Version History**

| Version | Date       | Change Type     | Description                                              |
| ------- | ---------- | --------------- | -------------------------------------------------------- |
| 1.0     | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
