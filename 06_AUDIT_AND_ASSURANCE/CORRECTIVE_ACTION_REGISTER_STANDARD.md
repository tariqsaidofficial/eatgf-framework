# CORRECTIVE_ACTION_REGISTER_STANDARD

| Field          | Value                                      |
| -------------- | ------------------------------------------ |
| Document Type  | Standard (Audit Governance)                |
| Version        | 1.0                                        |
| Change Type    | Major (Initial)                            |
| Classification | Controlled                                 |
| Effective Date | 2026-02-16                                 |
| Authority      | Chief Audit Officer and Governance Officer |
| EATGF Layer    | 06_AUDIT_AND_ASSURANCE                     |
| MCM Reference  | EATGF-MEA-AUD-01, EATGF-MEA-PERF-01        |

---

## Purpose

This standard establishes the mandatory Corrective Action Register (CAR) framework for documenting, tracking, and remediating all audit findings and control deficiencies. The CAR serves as the single authoritative log of findings, remediation plans, remediation progress, and closure evidence. All audit findings and identified control gaps must be entered into the CAR within 5 business days of finding discovery. The CAR is reviewed monthly by governance committee and used to assess organizational control maturity.

## Architectural Position

This standard operates within **06_AUDIT_AND_ASSURANCE** as the corrective action tracking and closure standard.

- **Upstream dependency:** Internal Audit Procedure (06_AUDIT_AND_ASSURANCE/INTERNAL_AUDIT_PROCEDURE_v1.0.md) defines audit findings; Audit Schedule Standard (peer document) defines audit cycle generating findings
- **Downstream usage:** CAR drives operational remediation; findings tracked through remediation to closure; executive reporting derived from CAR data; trend analysis identifies systemic deficiencies
- **Cross-layer reference:** CAR integrates audit findings (Layer 06), policy compliance gaps (Layer 04), control deficiencies (Layer 02), operational incidents (incident response), and process improvements (operational governance)

## Governance Principles

1. **Single Registry** – All findings (audit, incident, assessment) logged in single CAR; no parallel tracking systems
2. **Transparent Tracking** – CAR accessible to control owners and governance so remediation progress visible
3. **Accountability Assignment** – Each finding assigned to explicit responsible owner; remediation metrics tracked
4. **Closure Discipline** – No finding closed without evidence verification; closure authority differs by severity
5. **Trend Analysis** – CAR data analyzed quarterly to identify patterns (repeating findings, systemic gaps, risky areas)

## Technical Implementation

### Corrective Action Register (CAR) Structure and Data Model

**Master Finding Fields (Required for All Findings):**

| Field Name                | Data Type    | Description                     | Example                                                                                                                     |
| ------------------------- | ------------ | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Finding ID                | Alphanumeric | Unique identifier               | FIND-2026-001                                                                                                               |
| Finding Date              | Date         | Date finding identified         | 2026-01-15                                                                                                                  |
| Audit / Assessment Source | Dropdown     | Where finding came from         | Audit Q1 2026 / Incident Investigation / Management Assessment                                                              |
| Affected Control          | Dropdown     | MCM control(s) impacted         | EATGF-DSS-SEC-01 (Access Control)                                                                                           |
| Finding Category          | Dropdown     | Type of deficiency              | Design Gap / Operational Defect / Compliance Miss                                                                           |
| Finding Description       | Text         | Detailed description of finding | "Access reviews not performed for 3 business systems; inappropriate access levels discovered in sample of 20 user accounts" |
| Severity                  | Dropdown     | Assessed severity               | Critical / Major / Minor                                                                                                    |
| Root Cause                | Text         | Why finding occurred            | "Access review process scheduled quarterly, but not enforced; no calendar reminder set; responsibility unclear"             |

**Remediation Planning (Required for Severity ≥ Major):**

| Field Name                    | Data Type | Description                     | Example                                                                                            |
| ----------------------------- | --------- | ------------------------------- | -------------------------------------------------------------------------------------------------- |
| Remediation Responsible Owner | Text      | Person assigned remediation     | Sarah Chen, Director of Access Management                                                          |
| Remediation Owner Email       | Email     | Contact for progress updates    | <s.chen@company.com>                                                                               |
| Remediation Plan Summary      | Text      | High-level remediation approach | "Implement quarterly access review process automation; configure calendar reminders; document SOP" |
| Planned Remediation Date      | Date      | Target completion date          | 2026-04-30                                                                                         |
| Estimated Effort (Hours)      | Number    | Hours to remediate              | 40 hours (design process, automation config, testing)                                              |
| Dependencies                  | Text      | Other work/approvals needed     | Approval from CISO for access review scope; IT system access for scheduler configuration           |

**Remediation Progress Tracking (Updated Monthly):**

| Field Name          | Data Type  | Description               | Update Frequency                                                                               |
| ------------------- | ---------- | ------------------------- | ---------------------------------------------------------------------------------------------- |
| Current Status      | Dropdown   | Remediation progress      | Not Started / In Progress / Testing / Complete Pending Closure                                 |
| % Complete          | Percentage | Estimated completion %    | 0-100%                                                                                         |
| Hours Spent to Date | Number     | Actual hours consumed     | Updated monthly                                                                                |
| Status Comment      | Text       | Latest progress note      | "Completed access review process design; SOP documentation in progress; estimate 50% complete" |
| Last Update Date    | Date       | Most recent status update | Auto-populated on each update                                                                  |
| Updated By          | Text       | User who updated status   | "System auto-capture"                                                                          |

**Remediation Closure (Upon Completion):**

| Field Name                   | Data Type  | Description                       | Requirement                                                                                                                                  |
| ---------------------------- | ---------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Remediation Completion Date  | Date       | Date remediation work completed   | Actual completion date; ≤ Planned date indicates on-time delivery                                                                            |
| Closure Evidence             | Attachment | Documentation proving remediation | Links to: Updated policy, test results, training records, audit re-test findings, etc.                                                       |
| Closure Evidence Description | Text       | Explanation of evidence           | "Updated Access Review SOP added to documentation repository; Q1 2026 audit re-test confirmed quarterly reviews executed for all 12 systems" |
| Closure Reviewed By          | Text       | Authority who verified closure    | Chief Audit Officer or peer manager (depends on finding severity)                                                                            |
| Closure Status               | Dropdown   | Final status determination        | Closed / Reopened (if closure verification failed)                                                                                           |
| Closure Notes                | Text       | Rationale for closure decision    | "Remediation evidence verified; finding requirement satisfied; process now operating as designed"                                            |

### Finding Severity Classification

All findings classified by severity using consistent criteria:

| Severity     | Definition                                                                                              | Closure Requirement                                                   | Closure Timeline | Owner                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------- |
| **Critical** | Control not operating; risk to organization significant; regulatory violation likely; incident possible | Evidence of remediation AND audit re-test confirming control operates | ≤ 30 days        | Executive (COO, CISO, CFO depending on domain)              |
| **Major**    | Control operating defectively; control gap affecting compliance; risk mitigation incomplete             | Evidence of remediation AND evidence of control design verification   | ≤ 60 days        | Control owner + department head approval                    |
| **Minor**    | Control operating with inefficiency; documentation gap; procedure could be improved                     | Evidence of remediation (process update, training, documentation)     | ≤ 90 days        | Control owner (self-certification acceptable) in some cases |

**Closure authority levels:**

- Critical findings: Chief Audit Officer + Executive sponsor (CISO/CFO/COO) joint approval required
- Major findings: Department head + Chief Audit Officer approval required
- Minor findings: Control owner attestation sufficient; CAO spot-check 10% for verification

### Finding Entry and Initial Assessment

**Finding Discovery Triggers:**

Findings logged in CAR upon discovery from:

1. **Audit findings** (Internal Audit Procedure)
2. **Incident investigations** (Incident Response Policy)
3. **Regulatory audits** (External auditor findings)
4. **Management assessments** (Control owner or director identifying control gap)
5. **Process observations** (Operational teams identifying deficiency, e.g., missed SLA, procedure deviation)
6. **Customer complaints** (Customer identifying service/control deficiency)

**Finding Entry Timeline:**

- Finding date: Date when finding was first identified (not date investigation completed)
- CAR entry deadline: Within 5 business days of finding discovery
- Exemption: Critical findings requiring immediate escalation entered within 1 business day
- Later-discovered findings: If finding affects multiple periods, entry date is most recent discovery; historical scope noted

**Finding Assessment (Within 10 Days of Entry):**

Upon entry, Chief Audit Officer assesses:

1. **Control mapping:** Which MCM control(s) affected by finding
2. **Root cause:** Why did control gap occur (design flaw, operational failure, insufficient resources, insufficient monitoring)
3. **Scope:** Is this isolated to one system/location/user, or systemic across organization
4. **Severity:** Assess using severity matrix; re-assess during closure if evidence changes
5. **Regulatory risk:** Does finding create regulatory exposure (ISO 27001, SOC 2, GDPR, industry-specific)?
6. **Systemic potential:** Is this finding likely to recur? Is control design sufficient or does underlying design need rework?

CAO documents assessment in CAR; sends assessment to control owner for response (remediation plan) within defined timeline based on severity.

### Remediation Planning and Owner Assignment

**Remediation Plan Development (Due Within Specified Timeline):**

| Severity | Remediation Plan Due    | Format                                                                   |
| -------- | ----------------------- | ------------------------------------------------------------------------ |
| Critical | Within 3 business days  | Formal document signed by responsible owner and executive sponsor        |
| Major    | Within 10 business days | CAR entry with remediation plan; documented in meeting minutes           |
| Minor    | Within 15 business days | CAR entry with remediation plan or email summary of remediation approach |

**Remediation Plan Contents (For Critical/Major Findings):**

1. **Root cause explanation:** Control owner acknowledges finding and explains contributing factors
2. **Remediation approach:** Specific actions to remediate (design change, process improvement, training, control implementation)
3. **Success criteria:** How will we know remediation is successful (metrics, test results, audit re-test outcome)
4. **Resource requirements:** Staff needed, budget if applicable, external resources (consultants, vendors)
5. **Timeline/milestones:** Phased approach if multi-phase remediation; interim milestones with target dates
6. **Owner and accountability:** Named owner responsible for execution and progress reporting
7. **Executive sponsor:** For critical findings, named executive accountable to status report monthly

**Remediation Owner Selection Criteria:**

- Control owner (person responsible for control day-to-day operation) typically assigned
- If control owner unavailable or lacking authority, escalate to department head or functional leader
- Executive sponsor assigned for critical findings (CISO, CFO, COO, CIO)
- Multiple owners possible if remediation crosses departments (e.g., IT + HR for access control finding)

### Remediation Progress Tracking and Governance

**Monthly Status Updates (Due by 15th of Each Month):**

All findings with status other than "Closed" require monthly progress update:

| Finding Status               | Update Requirement                                       | Owner Responsibility                                                  |
| ---------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| **In Progress**              | Monthly progress update required; % complete estimated   | Control owner provides update; CAO monitors against timeline          |
| **Testing**                  | Weekly progress update required; test results documented | Control owner provides update; testing timeline tracked               |
| **Complete Pending Closure** | Weekly update until closure approved                     | Control owner provides closure evidence; CAO verification in progress |
| **Closed**                   | No further updates; closure documented in CAR            | CAO marks closed; closure evidence retained in CAR                    |

**Monthly CAR Governance Review (To Governance Committee):**

| Item                           | Description                                                                        | Frequency |
| ------------------------------ | ---------------------------------------------------------------------------------- | --------- |
| **New findings (month)**       | # of new findings entered in CAR this month; by severity                           | Monthly   |
| **Aging analysis**             | Findings open >30 days (critical), >60 days (major), >90 days (minor)              | Monthly   |
| **Overdue findings**           | Findings past planned remediation date                                             | Monthly   |
| **Closure trends**             | # of findings closed this month; closure evidence quality                          | Monthly   |
| **Current status by severity** | Current open findings count: # Critical, # Major, # Minor                          | Monthly   |
| **Systemic analysis**          | Findings affecting same control domain; repeating findings (audited, not resolved) | Quarterly |

**Example CAR Dashboard (Monthly Report to Governance Committee):**

```
CORRECTIVE ACTION REGISTER – MONTHLY STATUS
Report Period: February 2026

FINDINGS SUMMARY:
├─ Critical Findings: 2 (both < 30 days old, on track for remediation)
├─ Major Findings: 8 (5 in progress, 3 testing, 0 overdue)
├─ Minor Findings: 15 (10 in progress, 5 testing, 0 overdue)
└─ Total Open: 25

AGING ANALYSIS:
├─ New This Month (< 7 days): 3 findings
├─ 7-30 Days Old: 12 findings (on track for closure)
├─ 31-60 Days Old: 7 findings (1 overdue, accelerating closure plan)
└─ >60 Days Old: 3 findings (escalation review initiated)

SYSTEMIC OBSERVATIONS:
├─ Access Control Domain: 5 findings (3 remediation projects coordinated)
├─ Repeating Finding: Access Reviews not performed (year 2 audit finding, remediation plan progress 75% complete)
└─ New Risk Area: Vendor Management (3 critical findings from vendor audit initiation)

CLOSURE TREND:
├─ Closures This Month: 4 (2 Critical, 2 Major)
├─ Average Time to Closure: 45 days (target: <60 days major, <30 days critical)
└─ Closure Evidence Quality: 1 audit re-test required (prior month closure lacking verification)
```

**Monthly Governance Review Process:**

1. **CAO prepares report** (by 20th of month): Dashboard and findings analysis
2. **Control owners validate status** (by 10th of month): All owners update CAR status; email confirmations sent
3. **Governance committee reviews** (last week of month): CAO presents monthly status; aging findings discussed, overdue critical findings escalated
4. **Escalation if needed:** Overdue critical findings trigger executive-level escalation; remediation re-planning required; CAO reports to CISO/CFO
5. **Board reporting (quarterly)**: Material findings and systemic issues elevated to board audit committee

### Remediation Closure Procedures

**Closure Evidence Standards (By Finding Type):**

**Design Gap Findings** (Control definition was incomplete/incorrect):

Closure evidence required:

- Updated control documentation (policy, procedure, standard)
- Approval record (policy approval, control owner sign-off)
- Communication evidence (control owners/staff notified of change)
- Training evidence (if control operation changed, training documentation)
- Audit re-test findings (auditor tested updated control and confirmed operating per design)

Example: "Access review process was only documented for 8 of 12 systems. Closure evidence: Updated Access Review Policy to include all 12 systems (Approved Jan 30, 2026), training completed for all control owners (Training records, completion certificates), Q1 2026 audit re-test confirmed all 12 systems now have documented quarterly access reviews (Audit re-test report, page 4: 'Control now operating per design')."

**Operational Defect Findings** (Control was designed correctly but not operated properly):

Closure evidence required:

- Process change documentation (procedure updated, automation implemented, control modified)
- Monitoring/validation evidence (control owner conducted validation test; results documented)
- Training evidence (staff trained on corrected procedure)
- Audit re-test findings (auditor tested 10-30 samples of control operation and found compliance)

Example: "Access reviews performed but not documented in required register. Closure evidence: Access Review Register created in Google Sheets (template in Appendix B), automated email reminders configured for 3rd week of quarter (screenshot of Gmail automation rules), training provided to 12 system owners (training sign-in sheet), Q1 2026 audit re-test confirmed access reviews documented for 12 systems, min 8 owner signatures per system review (Audit test of 30 access reviews, 100% documented)."

**Compliance Miss Findings** (Required control not yet implemented):

Closure evidence required:

- Control implementation documentation (control procedures, system configuration, access policies)
- Test results (control tested; results document successful implementation)
- Audit re-test findings (auditor verified control operating)
- Evidence of sustained operation (control operated correctly for minimum 2 months before closure)

Example: "Quarterly risk assessments not performed. Closure evidence: Risk Assessment Policy drafted (v1.0, approved by CISO Jan 15, 2026), Risk Assessment Procedure documented defining assessment methodology (5-page SOP), Q1 2026 risk assessment completed (documentation in /Risk_Management/Assessments/2026_Q1/), control results presented to governance committee (meeting minutes Jan 30, 2026, page 3), Q2 2026 risk assessment scheduled (calendar holds in place, 3rd week of April), Q1 2026 audit re-test confirmed assessment performed and documented per procedure."

**Closure Approval Process:**

1. **Control owner submits closure request** with evidence attached to CAR
2. **CAO reviews closure evidence** (1-2 business days)
   - Is evidence sufficient per closure standard for finding type?
   - Does evidence actually resolve finding or just partial remediation?
   - Does control owner have authority to verify closure or does external confirmation needed?
3. **CAO may:**
   - **Approve closure:** Finding closed, evidence retained, finding status = Closed
   - **Request additional evidence:** CAO identifies gaps, requests control owner to supplement evidence
   - **Reopen finding:** If evidence does not support closure claim, finding reopened, control owner develops additional remediation
4. **For Critical findings:** CAO approval + Executive sponsor approval required before closure marked final
5. **Closure documentation:** Closure date, closure authority, closure evidence list, and any follow-up actions documented in CAR

**Reopened Findings:**

If finding closed but subsequent audit/assessment identifies issue not resolved:

- Finding reopened with "Reopened" status in CAR
- Reopened date and reason documented
- Control owner must develop additional remediation plan
- Reopened finding adds time to overall remediation (counts in aging analysis)
- Repeated reopenings (same finding reopened 2+ times) escalates to systemic review

### Systemic Finding Analysis and Trend Reporting

**Quarterly Systemic Review (By CAO):**

CAR data analyzed quarterly to identify patterns:

1. **Control domain frequency analysis:** Which control domains have most findings? (Suggests design/governance issues in those domains)
2. **Repeating findings:** Findings affecting same control in consecutive audit cycles (suggests remediation ineffective or control design flawed)
3. **Multi-control findings:** Findings affecting >3 related controls (suggests systemic issue in control area)
4. **Remediation time trends:** Average time to closure by severity; trends increasing/decreasing
5. **Overdue findings:** Findings aged >planned closure date; reasons documented; pattern analysis

**Systemic Issue Examples (Requiring Escalation):**

- **Example 1:** Access Control findings (EATGF-DSS-SEC-01) identified in 3 consecutive audit cycles affecting same control; root cause each time "Access reviews not performed". **Systemic issue:** Underlying control design insufficient; quarterly review not enforced; no accountability metric. **Escalation required:** Design review of access control framework; consider adding KPI for access review compliance.

- **Example 2:** Change Management findings trending upward: 2 findings in 2024, 4 in 2025, 7 in 2026. **Systemic issue:** Change volume increasing; process not scaling. **Escalation required:** Operations review; consider change process automation or additional staffing.

- **Example 3:** Vendor Risk findings clustered in Q1 2026 (5 findings, new area of audit). **Interpretation:** Vendor audit initiated for first time; likely baseline findings expected to decline in subsequent years. Monitor closure.

**Quarterly Executive Report (To Governance Committee / Board):**

| Section               | Content                                                                                        |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| **Executive Summary** | Total findings month-by-month, closure rate, average time to closure, critical findings status |
| **Systemic Issues**   | Identified patterns, recommendations for control redesign or governance improvement            |
| **Aging Analysis**    | Overdue findings requiring escalation, remediation acceleration plans                          |
| **Closure Quality**   | Trends in closure evidence quality, "stuck" findings (reopened multiple times)                 |
| **Outlook**           | Upcoming audit waves, anticipated new findings, resource needs                                 |

## Control Mapping

| EATGF Context                              | ISO 27001:2022                                                         | NIST SSDF                                                       | COBIT                                    |
| ------------------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------- |
| Finding documentation and tracking         | A.8.17 (Monitoring analysis and evaluation), A.6.7 (Management review) | CA-7 (Continuous monitoring), AU-5 (Response to audit findings) | MEA02.01 (Assess control effectiveness)  |
| Corrective action planning                 | A.5.26 (Response to incidents), A.6.7 (Management review)              | CA-7 (Monitoring findings), CA-8 (Audit response)               | MEA02.02 (Maintain corrective actions)   |
| Progress tracking and closure verification | A.8.17 (Reporting on findings), A.6.7 (Management review)              | CA-7 (Continuous monitoring reporting)                          | MEA02.01 (Evidence of monitoring)        |
| Systemic analysis and trend reporting      | A.8.17 (Analysis and reporting), A.6.7 (Management review)             | CA-7 (Insights from monitoring)                                 | MEA02.02 (Assess systemic improvements)  |
| Executive governance and escalation        | A.6.7 (Management review), A.6.1 (Executive direction)                 | CA-8 (Executive reporting)                                      | EDM03.01 (Provide board-level assurance) |

## Developer Checklist

- [ ] Corrective Action Register (CAR) designed with master finding data model: Finding ID, Date, Source, Control, Category, Severity, Root Cause, Description, Remediation Owner, Plan, Timeline, Evidence
- [ ] CAR tool/system selected and configured (spreadsheet template, Jira automation, Tableau dashboard, ISMS software module) with appropriate access controls
- [ ] Finding severity classification defined (Critical ≤30 days, Major ≤60 days, Minor ≤90 days) with closure timeline SLAs documented
- [ ] Remediation timeline expectations documented based on severity: Critical owners (Executive), Major owners (Department Head), Minor owners (Control Owner)
- [ ] Closure evidence standards documented by finding type (Design Gap, Operational Defect, Compliance Miss) with specific required documentation
- [ ] CAR entry procedures documented: Finding discovery triggers, 5-day entry deadline, 10-day initial assessment deadline, CAO assessment responsibilities
- [ ] Remediation plan development procedure documented: Format requirements, plan content requirements, owner selection, timeline by severity
- [ ] Monthly CAR status update process documented: Owner update deadline (10th), CAO report preparation (20th), governance committee review (last week)
- [ ] Monthly reporting dashboard template created: New findings, aging analysis, overdue findings, closure trends, systemic observations
- [ ] Governance committee review agenda item created: Monthly CAR status presentation, aging findings discussion, escalation decisions for overdue critical findings
- [ ] Closure approval workflow documented: CAO evidence review (1-2 days), approval decision (approve/request evidence/reopen), executive sponsor approval for critical findings
- [ ] Reopened finding procedure documented: Reopen triggers, documentation of reason, additional remediation plan requirement, tracking of reopens
- [ ] Systemic analysis procedure documented: Quarterly analysis by control domain, repeating finding identification, trend analysis, escalation criteria
- [ ] Quarterly systemic review report template created for governance committee: Executive summary, systemic issues identified, recommendations
- [ ] Audit re-test procedure documented: Timing (post-remediation completion), scope (how many samples tested for closure verification), results documentation
- [ ] Training completed for all finding discoverers (auditors, incident responders, control owners) on CAR entry, evidence standards, closure process
- [ ] Access controls configured in CAR: Read-only access for finance/compliance staff, edit access for CAO/control owners, executive dashboard for governance committee

## Governance Implications

**Risk if not implemented:**

- Findings documented inconsistently; no single source of truth; audit findings tracked separately from incident findings (fragmented governance)
- Findings entered months after discovery; remediation planning delayed; root cause analysis incomplete due to memory loss
- No remediation accountability; findings closed without evidence; closure claims unverified (phantom remediations)
- Repeating findings persist in consecutive audits unaddressed (control design never improved)
- Management unaware of finding trends; systemic issues not identified; control framework design gaps go unaddressed

**Operational impact:**

- CAR maintenance requires dedicated governance/compliance staff (0.5-1 FTE to manage updates, governance reporting, closure reviews)
- Remediation work estimated at 30-60 hours per major finding + 10-20 hours per minor finding; large finding volumes consume significant operational resources
- Monthly governance committee CAR review adds 1-2 hours monthly governance committee time
- Quarterly systemic analysis adds 5-10 hours CAO analysis and reporting work

**Audit consequences:**

- ISO 27001 auditors require evidence of systematic corrective action process; missing CAR or inadequate tracking results in audit non-conformance
- SOC 2 auditors validate corrective action timeliness and evidence adequacy; slow remediation affects SOC 2 Type II audit rating
- Regulatory audits (GDPR, PCI-DSS, HIPAA) review corrective action Register; unresolved prior audit findings identified during follow-up audit result in escalated findings (regulatory escalation to enforcement)
- External auditor follow-up audits specifically test whether prior findings closed; inadequate closure evidence = audit exception carries forward to next year

**Cross-team dependencies:**

- Control owners depend on CAO for finding severity assessment and remediation timeline guidance; disputed timelines escalate to executives
- Finance must approve budget for remediation projects; may delay remediation if budget not available
- IT operations must support control remediation (system changes, configuration updates, access modifications); competing operational priorities impact remediation timeline
- Executives assigned as remediation sponsors must commit monthly oversight; executive bandwidth limited creates bottleneck for critical finding progress
- Governance committee reviews monthly CAR status; governance calendar must accommodate monthly CAR presentations

## Official References

- NIST SP 800-53 Revision 5: Control CA-7 (Continuous Monitoring) and CA-8 (Penetration Testing and Analysis)
- ISO/IEC 27001:2022 Section 8.2.4 (Corrective Action)
- ISO/IEC 19011:2018 (Auditing Management Systems) Section on Corrective Actions
- COBIT 2019 Process MEA02: Monitor, Assess and Assure Compliance
- ISACA IT Audit Standards: Finding Classification and Corrective Action Tracking
- IIA (Institute of Internal Auditors): International Standards for the Professional Practice of Internal Auditing

---

**Version History**

| Version | Date       | Change Type     | Description                                              |
| ------- | ---------- | --------------- | -------------------------------------------------------- |
| 1.0     | 2026-02-16 | Major (Initial) | Initial publication aligning to EATGF mandatory template |
