# CERTIFICATION_READINESS_CHECKLIST_STANDARD

| Field          | Value                                                                   |
| -------------- | ----------------------------------------------------------------------- |
| Document Type  | Standard (Pre-Audit Checklist)                                          |
| Version        | 1.0                                                                     |
| Change Type    | Major (Initial)                                                         |
| Classification | Internal                                                                |
| Effective Date | 2026-02-16                                                              |
| Authority      | Chief Audit Officer and Control Owners                                  |
| EATGF Layer    | 06_AUDIT_AND_ASSURANCE                                                  |
| MCM Reference  | EATGF-MEA-CAR-02, EATGF-MEA-AUD-01                                      |

---

## Purpose

This standard defines the mandatory pre-audit certification checklist that control owners must complete prior to scheduled control audits. The checklist ensures control documentation is complete, evidence is staged, control design has been validated, and control operation has been verified. Controls failing the certification checklist may have audits delayed pending remediation. Certified controls demonstrate readiness for independent audit verification and reduce audit time/cost.

## Architectural Position

This standard operates within **06_AUDIT_AND_ASSURANCE** as the control certification and audit readiness standard.

- **Upstream dependency:** Audit Schedule Standard (peer document) provides audit schedule and 30-day notification; Internal Audit Procedure defines audit scope and evidence expectations
- **Downstream usage:** Certification checklist submitted to auditors 15 days before audit; auditors use checklist to scope audit work; certified controls audit faster/more efficiently
- **Cross-layer reference:** Supports all control compliance activities; certification checklist drives control owner accountability; checklist status reported to governance committee monthly

## Governance Principles

1. **Control Owner Accountability** – Control owners certify control readiness; certification signature indicates accountability for represented control state
2. **Pre-Audit Verification** – Control owners conduct self-assessment before independent audit; design/operational gaps identified and corrected pre-audit
3. **Evidence Staging** – All evidence assembled and organized before auditor arrival; audit time reduced, evidence quality improved
4. **Design/Operation Separation** – Separate certification for control design (is control designed correctly?) and operation (is control executed correctly?)
5. **Executive Cosign** – Department head cosigns certification for critical controls; executive validation of control statement accountability

## Technical Implementation

### Certification Checklist Components

**Section A: Control Overview (Design Validation)**

This section validates the control is properly designed before operational testing

**A.1 Control Definition and Design:**

- [ ] Control is documented in current policy or procedure (document name, version, effective date recorded)
- [ ] Control objectives clearly defined (what business risk does control mitigate? what is control purpose?)
- [ ] Control scope defined (to which systems, locations, data types, users applies?)
- [ ] Control boundaries defined (what activities/data/systems are out of scope?)
- [ ] Responsible owner identified (owner name, title, contact information documented)
- [ ] Support team identified (IT, finance, HR roles supporting control operation documented)

**A.2 Control Design Validation:**

- [ ] I have reviewed the current control design against the control objectives
- [ ] The control, if operating as designed, will achieve stated control objectives
- [ ] The control design is practical (can be operated with available resources)
- [ ] The control design is documented (written procedures exist that personnel can follow)
- [ ] Frequency/timing of control operation is documented (how often, what schedule)
- [ ] Roles and responsibilities for control operation are documented (who performs control, who approves, who reviews)
- [ ] Control decision criteria are documented (how control decisions are made, thresholds, approval levels)

**A.3 Documented Control Procedures:**

- [ ] Written procedure(s) exist documenting how control is executed step-by-step
- [ ] Procedure is current (reviewed and updated within past 12 months)
- [ ] Procedure specifies roles/titles responsible for each step
- [ ] Procedure specifies how evidence of control execution is documented
- [ ] Procedure specifies frequency and timing of control operation
- [ ] Procedure specifies exception handling (what if exception occurs? who approves exceptions?)
- [ ] Procedure is accessible to control operators (stored in controlled repository, version controlled)

**A.4 Training and Competency:**

- [ ] Personnel executing control receive annual training on control procedures
- [ ] Training documentation available (sign-in sheet, learning management system records, training completion data)
- [ ] Training covers: procedure steps, evidence documentation, what triggers control execution, frequency
- [ ] New employees receive training within 30 days of onboarding
- [ ] Training is documented in HR system or control-specific training log

**A.5 Control Design Governance:**

- [ ] Control design changes require approval (policy authority or CISO approval for security controls)
- [ ] Change approval documented (approval email, meeting minutes, checklists)
- [ ] Control design changes communicated to control operators
- [ ] Impacted personnel retrained on design changes
- [ ] Audit/compliance informed of control design changes that affect audit scope

**Sign-off by Control Owner:**

> I certify that the above control design items are accurate and complete. I am responsible for maintaining control design documentation current and communicating changes to my team.

**Signature:** ________________________  **Date:** __________

**Print Name & Title:** _________________________________

**Section B: Control Operation (Operational Readiness)**

This section validates the control is currently operating as designed

**B.1 Evidence of Control Execution:**

- [ ] Evidence documenting control execution exists for past 30 days (recent activity confirmed)
- [ ] Sample control execution records reviewed and verified accurate
- [ ] Evidence format matches documented procedure (expected artifacts present)
- [ ] Evidence dating/timelines match procedure frequency (control executed on required schedule)
- [ ] Evidence quality sufficient for audit review (legible, complete, signed/approved where required)

**B.2 Performance Against SLA/Frequency:**

- [ ] Control executed on required schedule (100% of required cycles in past 3 months documented)
- [ ] If quarterly control: 3 quarterly cycles executed in past 12 months documented
- [ ] If monthly control: 12 monthly cycles executed in past 12 months documented
- [ ] If continuous control: Continuous operation verified via system logs or periodic sampling
- [ ] Control execution delays or missed cycles documented (if any) with explanations

**B.3 Exception Handling and Escalation Evidence:**

- [ ] Procedures define what constitutes exception (documented criteria)
- [ ] Exceptions occurred in past 3 months logged (date, description, approval documented)
- [ ] Exceptions escalated per procedure (documented evidence of escalation)
- [ ] Exceptions resolved within documented escalation timeline
- [ ] Non-compliance with exception handling procedure (if any) documented and corrected

**B.4 Monitoring Evidence:**

If control has monitoring/review component:

- [ ] Reviews of control execution conducted per procedure (weekly, monthly, quarterly as specified)
- [ ] Review evidence documented (sign-off, meeting minutes, dashboard review evidence)
- [ ] Trends identified during monitoring (control performing per targets, any issues identified)
- [ ] Monitoring findings escalated if threshold exceeded (approval levels, escalation documentation)

**B.5 Remediation of Control Gaps:**

- [ ] If prior audit findings exist for this control, evidence of remediation documented
- [ ] Remediation actions completed per corrective action register timeline
- [ ] Re-testing of remediation completed (evidence control now operates per design)
- [ ] Control owner confirms prior findings no longer applicable

**B.6 System/Technology Controls:**

If control relies on IT systems or automation:

- [ ] System configuration documented (controls in place, rules appropriate, access restricted)
- [ ] System access controls verified (authorized users can access, unauthorized cannot)
- [ ] System logs generated for control-relevant events (enabled, retained per policy)
- [ ] System monitoring rules configured to alert on control failures
- [ ] System change management applied to control-related changes (pending or recent)

**B.7 Compliance with Related Requirements:**

- [ ] Control complies with related policies (information security, data protection, acceptable use, etc.)
- [ ] No conflicts identified between this control and other controls
- [ ] Control operates within approved budgets/resources
- [ ] Third-party vendors supporting control (if any) maintain required certifications (SOC 2, ISO 27001)

**Sign-off by Control Owner:**

> I certify that the above control operation items are accurate and complete. The control is currently operating as designed. I have verified evidence of control execution for the past 30 days. Any prior audit findings have been remediated. The control is ready for independent audit.

**Signature:** ________________________  **Date:** __________

**Print Name & Title:** _________________________________

**Section C: Evidence Staging and Documentation**

This section ensures all audit evidence is organized and accessible for auditor review

**C.1 Evidence Organization:**

- [ ] Evidence organized in single location (folder, system, or drive accessible to auditor)
- [ ] Evidence organized by category (policies, procedures, test results, training records, monitoring evidence, exception logs)
- [ ] Index created documenting all evidence (what evidence, location, date range covered)
- [ ] Evidence retention policy documented (how long is evidence kept, when is evidence deleted)
- [ ] Access controls applied to evidence location (read-only for auditor, write access for control owner)

**C.2 Required Evidence Checklist:**

- [ ] Current control policy (version, approval date, effective date)
- [ ] Control procedures (step-by-step documentation of how control executed)
- [ ] Role definitions (documented roles responsible for control, approval layers)
- [ ] Frequency/timing specifications (schedule showing when control executed, in what intervals)
- [ ] Evidence of control execution for past 90 days (sample: 10-30 execution instances)
- [ ] Training records (employee names, training dates, training completion confirmation)
- [ ] Quarterly/annual control monitoring results (self-assessments, management reviews)
- [ ] Prior audit reports (if any) with findings
- [ ] Prior audit remediation evidence (if any findings, evidence of fixes)
- [ ] Exception logs (control exceptions, escalation, resolution documentation for past 12 months)
- [ ] System access controls documentation (if IT control: access matrix, approved users, system configuration)
- [ ] System logs (if IT control: 30-90 days logs showing control operation)
- [ ] Compliance with related policies (evidence control complies with sec, privacy, acceptable use, etc.)

**C.3 Evidence Quality Standards:**

- [ ] All evidence is legible (scans readable, archived documents not faded)
- [ ] Evidence is dated (dates present on documents, or filing dates captured)
- [ ] Evidence is signed/approved where policy requires (approver identified, signature/email confirmation present)
- [ ] Evidence is authentic (original documents preferred, copies acceptable if certified as accurate copies)
- [ ] Confidential/restricted evidence marked appropriately (access restricted if needed for audit)
- [ ] No proprietary competitor information inadvertently included in evidence (if non-public info included, marked confidential)

**C.4 Evidence Access and Preservation:**

- [ ] Evidence location communicated to auditor 15 days before audit (drive/folder URL, system login, physical location)
- [ ] Auditor confirmed able to access evidence 7 days before audit (test access verified)
- [ ] Evidence will not be modified during audit period (read-only access configured if possible)
- [ ] Backup evidence preserved (original not altered during audit)

**Sign-off by Documentation/Evidence Owner:**

> I certify that all evidence listed above is complete, organized, and accessible. Evidence quality is appropriate for audit review. Evidence has been preserved (not modified) and will be available for auditor review during scheduled audit period.

**Signature:** ________________________  **Date:** __________

**Print Name & Title:** _________________________________

**Section D: Executive Certification (For Critical Controls Only)**

This section ensures department head cosigns control statement; executive accountability for control control statement validity

**D.1 Executive Review and Validation:**

- [ ] Department head has reviewed control design and operation certification
- [ ] Department head is satisfied control is properly designed and currently operating
- [ ] Department head is aware of any control gaps or deficiencies (noted in exceptions section)
- [ ] Department head confirms necessary resources are allocated to control operation
- [ ] Department head confirms control priority within department operations

**D.2 Executive Accountability:**

- [ ] Department head understands control is subject to independent audit
- [ ] Department head is accountable for control design and operation to executive governance
- [ ] Department head commits to remediate any audit findings within timelines specified by governance
- [ ] Department head acknowledges responsibility for escalating control issues that impede operations
- [ ] Department head will review audit findings and participate in remediation planning

**Executive Cosign (Critical Controls Only):**

> I, the Department Head, confirm I have reviewed the above control certification. I am satisfied the control is appropriately designed and is currently operating as intended. I am accountable for this control's effectiveness and will ensure any audit findings are remediated in alignment with organizational expectations.

**Executive Signature:** ________________________  **Date:** __________

**Print Name & Title:** _________________________________

**Section E: Exceptions and Deviations (Optional – Use if control is not fully ready)**

This section documents any known gaps or deviations from control design; used only if control is not fully certified

**E.1 Known Control Gaps:**

If control is not fully ready for audit, document known gaps:

| Gap Description | Why Gap Exists | Remediation Plan | Target Remediation Date | Impact on Audit Readiness |
|---|---|---|---|---|
| Example: Access reviews not completed for DB system #3 | System transferred to new team; transition not completed | Training scheduled for new team; access reviews will be completed Oct 15 | 2026-10-15 | Control partially unverified; audit will identify as design gap untested |
| ... | | | | |

**E.2 Audit Readiness Assessment (If Not Fully Ready):**

- [ ] Control is partially ready; some evidence/components not yet available
- [ ] Estimated completion date for full readiness: _________
- [ ] Request for audit deferral OR accept audit with limitation that [specific component] not yet audited
- [ ] Alternative: Proceed with audit; identify gap as operational deficiency; develop remediation plan

**E.3 Control Owner and Executive Acknowledgment of Preparation Gap:**

> I acknowledge the above control is not fully prepared for audit. I am requesting [defer audit / proceed with audit with limitation documented above]. I confirm remediation plan and timeline, and accept responsibility for closing this gap.

**Signature:** ________________________  **Date:** __________

### Certification Checklist Process and Deadlines

**Timeline:**

| Milestone | Deadline | Owner | Action |
|---|---|---|---|
| **Audit Schedule Published** | January 31 | Chief Audit Officer | 35 controls for year published; control owners notified |
| **T-90 Days Before Audit** | Control owner receives 90-day notice | Chief Audit Officer | Email notification with audit date, scope, checklist form |
| **T-60 Days Before Audit** | Certification checklist work begins | Control Owner | Control owner reviews checklist; begins evidence staging |
| **T-30 Days Before Audit** | Control owner submits draft certification | Control Owner | Checklist submitted to auditor for review; request evidence feedback |
| **T-15 Days Before Audit** | Final certification submitted | Control Owner | Updated checklist submitted; all exceptions/gaps confirmed; evidence packaged |
| **Audit Execution** | Scheduled audit period | Auditor | Independent audit conducted using certification checklist as reference |

**Submission Process:**

1. **Control owner downloads** certification checklist template for their control
2. **Completes Sections A-B** (Design and Operation validation) by T-30 days
3. **Auditor reviews draft** (T-28 to T-25): Auditor provides feedback on evidence quality/completeness; control owner makes adjustments
4. **Completes Sections C** (Evidence Staging) by T-15 days
5. **Executive cosigns Section D** (if critical control) by T-10 days
6. **Final checklist submitted** by T-15 days; readiness status confirmed (Certified / Partially Ready / Not Ready)

**Readiness Statuses:**

| Status | Definition | Audit Outcome | Notes |
|---|---|---|---|
| **Certified Ready** | All checklist items complete; no exceptions; all evidence staged; executive cosign (if req'd) | Audit proceeds per schedule; expected quick/efficient audit | Ideal state |
| **Partially Ready** | Some checklist items incomplete; documented gaps; remediation plan in progress | Audit proceeds with limitation; specific gaps noted as scope limitation | Acceptable if gaps minor; control owner commits timeline |
| **Not Ready** | Major gaps; evidence not staged; control not operating per design | Audit deferred pending control readiness improvements | Rare; requires control owner and executive to agree deferral acceptable |

**Escalation if Control Inadequate:**

If control fails certification (Not Ready status):

1. Control owner documents remediation plan and timeline
2. Control owner and department head agree deferral is appropriate
3. Chief Audit Officer approves deferral and reschedules audit for T+30 or T+60 days
4. Updated checklist due before rescheduled audit date
5. Repeated certification failure escalates to CISO/CFO for executive review

### Audit Coverage and Evidence Sufficiency

**Evidence Sufficiency Standards (For Each Control):**

| Control Component | Minimum Evidence Expected | Sample Size | Audit Verification Method |
|---|---|---|---|
| **Design validation** | Policy/procedure document + approval | 1 policy | Auditor reviews current policy; confirms reflects control design |
| **Operation verification** | Execution records for past 90 days | 10-30 samples (proportional to control frequency) | Auditor samples execution records; verifies match procedure; confirms evidence of execution complete and signed |
| **Training** | Training records for past 12 months | Count: 100% of control operators should be trained; Auditor verifies ≥80% trained within 12 months | Training completion records reviewed; dates verified; new hire training verified |
| **Monitoring** | Monitoring/review evidence for past quarter | 1 quarterly review minimum | Auditor reviews monitoring documentation; confirms action on findings if any |
| **Exceptions** | Exception logs for past 12 months | 100% of exceptions should be logged | Auditor spot-checks: select 3-5 situations where exception could have occurred; verify either evidence of execution or documentation why exception occurred |

### Certification Checklist Reporting

**Monthly Certification Status Report (To Governance Committee):**

| Metric | Definition | Target | Current (Month) |
|---|---|---|---|
| **Certification Completion Rate** | % of controls certified prior to audit | 100% | 87% (34/35 audited, 28/34 Certified Ready, 6/34 Partially Ready, 1/34 deferred) |
| **Early Certification** | % certified ≥30 days before audit | 80% | 76% |
| **Evidence Completeness** | % of certified controls with all evidence staged | 95% | 93% |
| **Executive Cosign Rate** | % of critical controls with executive cosign | 100% | 100% (8/8 critical controls cosigned) |
| **Audit Efficiency Impact** | Average audit time per control (Certified vs. Not Certified controls) | Certified: 8 hours avg; Not Certified: 16 hours avg | Certified: 7.5 hrs; Not Certified: 15.5 hrs (confirms efficiency gain) |

**Escalation Triggers:**

- Certification completion <90% one month before audit: Escalate to department heads; target remediation 2 weeks before audit
- Certification completion <75% two weeks before audit: Request deferral or proceed with audit delay implications accepted
- Evidence completeness <80%: Audit timeframe extended; auditor will spend more time collecting evidence vs. testing execution

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | COBIT |
|---|---|---|---|
| Control readiness and self-assessment | A.8.17 (Monitoring, measurement, analysis and evaluation), A.6.7 (Management review) | CA-7 (Continuous monitoring), CA-8 (Penetration testing and analysis) | MEA01.01 (Monitor effectiveness), MEA02.01 (Assess control maturity) |
| Evidence preparation and staging | A.8.17 (Monitoring records), A.6.7 (Management review) | AU-2 (Audit events), AU-5 (Response to audit findings) | MEA03.01 (Collect and analyze data) |
| Control design validation | A.5.1 (Information security policies), A.6.7 (Management review) | CA-2 (Security assessments), CA-3 (Assessment procedures) | APO13.01 (Establish governance framework) |
| Control operation verification | A.8.15 (Logging), A.8.16 (Monitoring), A.8.17 (Monitoring analysis) | CA-7 (Continuous monitoring), SI-4 (Information system monitoring) | DSS05.02 (Ensure security compliance) |
| Executive accountability | A.6.1 (Executive direction), A.6.2 (Information security roles) | CA-8 (Penetration testing), IR-1 (Incident coordination) | EDM01.01 (Evaluate strategy and objective) |

## Developer Checklist

- [ ] Certification checklist template created with Sections A-E (Design, Operation, Evidence, Executive, Exceptions)
- [ ] Section A (Design Validation) detailed with 5 subsections (Control Definition, Design Validation, Procedures, Training, Governance)
- [ ] Section B (Operation Readiness) detailed with 7 subsections (Execution Evidence, SLA, Exception Handling, Monitoring, Remediation, Technology, Compliance)
- [ ] Section C (Evidence Staging) detailed with 4 subsections (Organization, Required Evidence, Quality, Access/Preservation)
- [ ] Section D (Executive Certification) created with executive review items and cosign requirement (for critical controls)
- [ ] Section E (Exceptions) created for documenting known gaps if control not fully ready
- [ ] Control owner sign-off language created for each section with date/name/title fields
- [ ] Timeline and deadline schedule created: T-90 (notification), T-60 (work begins), T-30 (draft), T-15 (final), T-0 (audit)
- [ ] Process documented: Checklist download → Sections A-B completion → Draft submission → Auditor feedback → Revision → Final submission
- [ ] Readiness status categories defined (Certified Ready / Partially Ready / Not Ready) with audit implications documented
- [ ] Remediation plan format documented for Partially Ready controls (gap description, why exists, plan, target date, impact)
- [ ] Escalation procedure documented if control fails certification (deferral decision, executive approval, reschedule)
- [ ] Monthly certification status report template created for governance committee: % completion, early cert %, evidence completeness %, executive cosign %, audit efficiency metrics
- [ ] Escalation thresholds defined: <90% completion one month before = escalate; <75% two weeks before = deferral or extended timeline
- [ ] Training created for control owners on checklist completion, evidence standards, submission deadlines
- [ ] Audit scheduling system updated to send automatic reminders at T-90, T-60, T-30, T-15 days
- [ ] Auditor guidance created on how to use certification checklist during audit (as reference, as gap analyzer, as evidence compilation guide)

## Governance Implications

**Risk if not implemented:**

- Control owners unprepared for audits; evidence scattered and incomplete; auditors spend 50% of time collecting evidence instead of testing execution
- Control design assumptions unstated; auditors discover during audit that control not operating as designed (late deficiency discovery)
- Executive leadership unaware of control readiness; discovers during audit meeting that critical control has major gaps
- Prior audit findings not remediated; same finding reappears in current year audit (repeat findings accumulate)
- Audits extended and expensive (inefficient evidence collection, rework); audit budget overruns

**Operational impact:**

- Control owners must dedicate 10-20 hours per control per audit cycle to certification checklist completion and evidence staging
- Department heads must allocate time for executive review and cosign (2-5 hours for critical controls annually)
- Evidence organization requires dedicated effort (1-5 hours per control depending on evidence volume)
- Audit preparation cycle adds 2-3 months of operational activity before audit execution

**Audit consequences:**

- ISO 27001 auditors expect documented evidence of control operation; lack of staged evidence indicates control owner not prioritizing governance (audit finding implication)
- SOC 2 auditors validate control design through review of policies, procedures, and evidence; inadequate evidence impacts SOC 2 audit scope
- Regulatory audits appreciate certified controls with staged evidence (signals organizational governance maturity); impacts auditor confidence and audit efficiency
- Audit deficiencies documented in audit report; repeat findings (same control, consecutive audits) indicate inadequate remediation (escalates to regulatory finding)

**Cross-team dependencies:**

- Control owners must gather evidence from multiple sources (IT, HR, Finance, Operations); cross-team coordination required
- IT must provide system logs, access control documentation, system change records for IT-dependent controls
- HR must provide training records, employee termination documentation, onboarding records
- Finance must provide approval records, payment records, budget allocation records
- Documentation/records management team may manage centralized evidence repository (coordinated storage, access controls)

## Official References

- NIST SP 800-53 Revision 5: Control CA-2 (Security Assessment) and CA-8 (Penetration Testing and Analysis)
- ISO/IEC 27001:2022 Section 9.2 (Internal Audit)
- ISO/IEC 19011:2018 (Auditing Management Systems) Section on Planning
- COBIT 2019 Process MEA02 (Monitor Compliance and Internal Control)
- ISACA IT Audit Standards: Audit Planning and Evidence Standards
- SOC 2 Trust Service Criteria: Design and operating effectiveness controls

---

**Version History**

| Version | Date | Change Type | Description |
|---------|------|-------------|-------------|
| 1.0 | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
