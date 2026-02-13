# EVIDENCE_REGISTER_MASTER_v1.0

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
Centralized Audit Evidence Tracking System

---

**Document Type:** Evidence Register Template (Master Specification)  
**Authority:** Chief Audit Officer / Governance Office  
**Control Reference:** EATGF-MEA-AUD-01  
**Framework Reference:** ISO/IEC 27001:2022, ISO/IEC 42001:2023, ISO 19011:2018

---

## 1. Purpose

This document defines the architecture and operational specifications for the EVIDENCE_REGISTER—the centralized tracking system for all control-level evidence required to demonstrate conformity with:

- ISO/IEC 27001:2022
- ISO/IEC 42001:2023
- EATGF Master Control Matrix
- Internal Audit Procedure

**The Evidence Register operationalizes MCM controls into an auditable, time-bound, accountability-driven system.**

---

## 2. Architecture Philosophy

The Evidence Register must:

✅ **Be control-centric** – MCM ID driven (not process-driven)  
✅ **Be time-bounded** – Review frequency enforced, not optional  
✅ **Be ownership-bound** – Clear accountability layers  
✅ **Be audit-traceable** – Links to specific audit cycle  
✅ **Be version-controlled** – Every entry immutable, timestamped  
✅ **Be exportable** – Ready for external auditor consumption  

---

## 3. Required Implementation Files

### Primary File (Operational)
```
/governance/EVIDENCE_REGISTER.xlsx
```

**Format:** Microsoft Excel or LibreOffice Calc

**Why Excel:**
- Easy filtering for audit cycles
- Exportable to PDF for external auditors
- Formula-driven status automation
- No external tool dependencies

### Secondary File (Documentation & Reference)
```
/governance/EVIDENCE_REGISTER_MASTER.md
```

**This document** – serves as specification and training reference.

---

## 4. Core Column Definitions (Non-Negotiable)

### Excel Column Layout

| Col | Column Name | Type | Source | Requirement | Notes |
|-----|-------------|------|--------|-------------|-------|
| A | Control ID | Text | MCM | Mandatory | Format: EATGF-[DOMAIN]-[CONTROL]-[#] |
| B | Control Title | Text | MCM | Mandatory | Short description from MCM |
| C | Domain | Text | MCM | Mandatory | EDM / APO / BAI / DSS / MEA / AI / CLOUD |
| D | Criticality | Dropdown | MCM | Mandatory | High / Medium / Low |
| E | Residual Risk Level | Dropdown | MCM | Mandatory | High / Medium / Low |
| F | Clause Reference | Text | ISMS/AIMS | Informational | ISO 27001 Clause or ISO 42001 Clause |
| G | Evidence Type | Dropdown | MCM | Mandatory | Document / System / Process / Assessment / AI-Specific |
| H | Evidence Description | Text | Control Def | Mandatory | Specific evidence name/ID (e.g., "Access Review Q1 2026") |
| I | Evidence Location | URL/Path | Owner | Mandatory | SharePoint link, Confluence URL, Git commit, or system path |
| J | Evidence Owner (Role) | Text | MCM | Mandatory | Title/Function responsible for evidence upload |
| K | Control Owner (Role) | Text | MCM | Mandatory | Title/Function responsible for control validation |
| L | Review Frequency | Dropdown | MCM | Mandatory | Monthly / Quarterly / Semi-Annual / Annual |
| M | Last Review Date | Date | Manual | Mandatory | Date evidence was last validated |
| N | Next Review Date | Date | Formula | Auto | = Last Review Date + Frequency Interval |
| O | Days Until Due | Number | Formula | Auto | = Next Review Date – TODAY() |
| P | Audit Cycle | Text | Audit Prog | Informational | 2026-Q1 / 2026-Annual / 2026-Incident |
| Q | Status | Auto-Dropdown | Formula | Mandatory | VALID / EXPIRED / MISSING / ACTION REQUIRED |
| R | Status Color | Conditional | Formula | Visual | Green / Yellow / Red / Gray |
| S | Auditor Notes | Text | Audit Week | Optional | Findings, observations, context |
| T | Corrective Action Ref | Text | Audit Log | Conditional | Link to remediation ticket if Status = ACTION REQUIRED |
| U | Evidence Retention Until | Date | Policy | Mandatory | = Evidence Date + 7 years |
| V | Last Updated By | Text | System | Auto | Audit trail |
| W | Last Updated Date | Timestamp | System | Auto | Audit trail |

---

## 5. Excel Workbook Tab Structure

### **Tab 1: MASTER_CONTROL_IMPORT**

**Purpose:** Single source of truth for all 35 MCM controls.

**Content:**
- Import all controls from MASTER_CONTROL_MATRIX.md
- No manual typing; auto-import via copy-paste or API
- Frozen (locked sheet)

**Columns:**
| Control ID | Title | Domain | Criticality | Residual Risk | Clause Ref | Frequency |
|------------|-------|--------|-------------|---------------|-----------|-----------|
| EATGF-EDM-GOV-01 | Governance Charter | EDM | High | Medium | 27001:5.1 | Annual |
| EATGF-EDM-RISK-01 | Risk Criteria Definition | EDM | High | Medium | 27001:6.1 | Annual |
| EATGF-APO-SEC-01 | Information Security Policy | APO | High | Low | 27001:5.2 | Annual |
| ... | ... | ... | ... | ... | ... | ... |

---

### **Tab 2: ACTIVE_EVIDENCE_TRACKER**

**Purpose:** Primary working sheet. Universal access point for governance operations.

**Content:**
- One row per control per review cycle
- If control freq = Quarterly → 4 rows per year (Q1, Q2, Q3, Q4)
- If control freq = Annual → 1 row per year

**Example structure:**

| Control ID | Control Title | Domain | Evidence Description | Evidence Location | Evidence Owner | Last Review Date | Next Review Date | Days Until Due | Status | Auditor Notes |
|------------|---------------|--------|----------------------|-------------------|-----------------|-----------------|-----------------|---|--------|---|
| EATGF-DSS-SEC-01 | IAM & Access Control | DSS | Access Review Q1 2026 | SharePoint: Access-Review-Q1-2026.pdf | Manager, IAM | 2026-01-15 | 2026-04-15 | 45 | VALID | Approved, 0 deviations |
| EATGF-DSS-SEC-01 | IAM & Access Control | DSS | Access Review Q2 2026 | [Pending] | Manager, IAM | — | 2026-07-15 | 92 | MISSING | Escalated to CISO |
| EATGF-DSS-ENC-01 | Encryption Standards | DSS | Quarterly Encryption Audit Feb 2026 | Confluence: Encryption-Report-Feb-2026 | Manager, Infrastructure | 2026-02-01 | 2026-05-01 | 61 | VALID | Passed all compliance checks |
| EATGF-AI-RISK-01 | AI Risk Management | AI | Bias Test Report – Model XYZ v1.2 | Git: /models/xyz/bias-report-v1.2.pdf | Data Science, Lead | 2026-02-01 | 2026-05-01 | 61 | VALID | Model deployed, monitoring active |

---

### **Tab 3: AUDIT_VIEW**

**Purpose:** Filtered, read-only dashboard used during audit weeks.

**Auto-populated filters:**
- Show: Controls with Next Review Date ≤ 30 days from TODAY()
- Show: All controls with Status = MISSING
- Show: All controls with Status = ACTION REQUIRED
- Show: All controls with Criticality = High
- Show: All AI controls (if AI-specific audit)
- Show: All Cloud controls (if cloud-specific audit)

**Auditor interaction:**
- Add observations in "Auditor Notes" column
- Flag priority controls
- Attach evidence samples

---

### **Tab 4: DASHBOARD**

**Purpose:** Real-time governance KPI visibility.

**Metrics (auto-calculated):**

| KPI | Formula | Target | Current |
|-----|---------|--------|---------|
| **Overall Compliance %** | (VALID / Total Controls) × 100 | ≥95% | [Auto] |
| **Critical Controls Coverage %** | (VALID Critical / Total Critical) × 100 | 100% | [Auto] |
| **Evidence Overdue %** | (EXPIRED / Total Controls) × 100 | <5% | [Auto] |
| **AI Controls Coverage %** | (VALID AI / Total AI) × 100 | 100% | [Auto] |
| **Cloud Controls Coverage %** | (VALID Cloud / Total Cloud) × 100 | ≥95% | [Auto] |
| **Corrective Actions Open** | COUNT(Status = "ACTION REQUIRED") | <10 | [Auto] |
| **Corrective Actions Overdue** | COUNT(Days Until Due < 0 AND Status = "ACTION REQUIRED") | 0 | [Auto] |
| **Audit Findings Trend** | [3-month rolling average] | Decreasing | [Auto] |

**Visual Elements:**
- Conditional color coding (Green ≥95%, Yellow 80-95%, Red <80%)
- Pie charts: Coverage by domain
- Timeline: Upcoming evidence due dates
- Heat map: High-risk control status

---

## 6. Status Logic & Auto-Calculation Rules

### Status Column Formula Logic

```
IF(Evidence_Location = BLANK, "MISSING",
  IF(TODAY() > Next_Review_Date, "EXPIRED",
    IF(Last_Review_Date < [7 days ago], "ACTION REQUIRED",
      "VALID")))
```

### Status Values & Meaning

| Status | Condition | Action Required |
|--------|-----------|-----------------|
| **VALID** | Evidence uploaded & within review frequency | None – continue monitoring |
| **MISSING** | No evidence location provided | Upload evidence immediately |
| **EXPIRED** | Review date has passed, no new evidence | Perform review & upload |
| **ACTION REQUIRED** | Flagged during audit or corrective action | Assign owner & deadline |

### No Manual Override

- Status column is formula-driven
- Overrides disabled (protection enforced)
- Ensures objective, consistent scoring

---

## 7. Evidence Type Specifications

### By Control Domain

#### **EDM Controls**
- **Evidence Type:** Document / Assessment
- **Examples:** Board minutes, governance charter, risk appetite statements, policy approvals
- **Format:** PDF, Word, signed digital

#### **APO Controls**
- **Evidence Type:** Document / Process / Assessment
- **Examples:** Risk registers, security policies, SoA, audit reports, training records
- **Format:** Spreadsheet, PDF, signed

#### **BAI Controls**
- **Evidence Type:** Process / System / Document
- **Examples:** Change tickets, test results, CI/CD logs, deployment records
- **Format:** Screenshots, Git commits, system exports

#### **DSS Controls**
- **Evidence Type:** System / Process / Assessment
- **Examples:** Vulnerability reports, access reviews, incident logs, encryption configs
- **Format:** System-generated reports, PDF exports

#### **MEA Controls**
- **Evidence Type:** Assessment / Document
- **Examples:** Audit reports, maturity assessments, KPI dashboards, meeting minutes
- **Format:** PDF, Spreadsheet

#### **AI Controls (42001)**
- **Evidence Type:** AI-Specific
- **Examples:** Model cards, bias reports, dataset documentation, drift metrics, explainability tests
- **Format:** Jupyter notebooks, PDF reports, system metrics
- **Must Include:** Model version, dataset version, timestamp, test ID

#### **Cloud Controls**
- **Evidence Type:** System / Document
- **Examples:** Config snapshots, IAM policies, network diagrams, compliance scans
- **Format:** JSON configs, PNG/PDF, system exports
- **Must Include:** Region, account ID, last scan date, compliance framework

---

## 8. Evidence Validation Rules

### Minimum Requirements for ALL Evidence

✅ **Dated** – Must have clear date (creation or last modified)  
✅ **Signed** – If document: digital signature or attestation  
✅ **Log-Generated** – If system: timestamp and source logged  
✅ **Immutable** – Original format preserved (PDF preferred)  
✅ **Traceable** – Linked to specific Control ID  
✅ **Accessible** – URL valid or documentation location clear  

### AI-Specific Evidence Validation

For any EATGF-AI-* control:

✅ **Model Version** – Exact version number  
✅ **Dataset Version** – Training data snapshot ID  
✅ **Test Report ID** – Bias/drift/accuracy test reference  
✅ **Deployment Timestamp** – When model went live  
✅ **Monitoring Link** – Active dashboard URL  

### Cloud-Specific Evidence Validation

For any EATGF-CLD-* or cloud-related control:

✅ **Region** – Geographic deployment location  
✅ **Account ID** – Cloud provider account identifier  
✅ **Configuration Snapshot** – Point-in-time config export  
✅ **Scan Date** – Last compliance/security scan  
✅ **Compliance Framework** – CIS, PCI-DSS, SOC 2, etc.  

---

## 9. Integration Points

### Bidirectional Linking

| System | Integration Type | Purpose |
|--------|------------------|---------|
| **MCM** | → Evidence Register | Control authority sourcing |
| **ISMS Manual** | ← Evidence Register | Clause validation proof |
| **AIMS Manual** | ← Evidence Register | AI lifecycle evidence |
| **Internal Audit Procedure** | ← Evidence Register | Sampling population |
| **Statement of Applicability** | ← Evidence Register | Annex A justification |
| **Corrective Action Log** | ← Evidence Register | Remediation tracking |
| **Risk Register** | ← Evidence Register | Residual risk proof |

### Export Workflows

**For External Auditors:**
```
Export Evidence Register (AUDIT_VIEW tab) 
→ Filter by audit cycle 
→ PDF with redactions 
→ Deliver with evidence samples
```

**For Management Review:**
```
Export Dashboard tab 
→ Monthly scorecard 
→ Governance council presentation
```

**For Certification Body:**
```
Export MASTER_CONTROL_IMPORT + ACTIVE_EVIDENCE_TRACKER 
→ Full control matrix with evidence status 
→ Certification audit submission
```

---

## 10. Governance Rules & Accountability

### Evidence Owner Responsibilities
- Upload evidence within 7 days of deadline
- Ensure evidence meets validation rules
- Notify Control Owner of upload
- Maintain evidence immutability

### Control Owner Responsibilities
- Validate evidence completeness
- Confirm control effectiveness via evidence
- Flag gaps or exceptions
- Sign off on review

### Governance Office Responsibilities
- Monitor tab for missing/expired controls
- Escalate overdue entries
- Maintain access controls
- Manage annual archival

### Internal Audit Responsibilities
- Sample evidence during audit week
- Verify authenticity and currency
- Document findings in Auditor Notes
- Approve audit cycle completion

### Escalation Protocol

| Days Overdue | Action |
|-------------|--------|
| 0–3 days | Reminder email to Evidence Owner |
| 4–7 days | Copied to Control Owner, escalated |
| 8–14 days | Escalated to Governance Office |
| >14 days | Escalated to Executive Steering Committee |

---

## 11. Evidence Lifecycle

### Phase 1: Generation
- Evidence created during normal operations
- Dated, signed, versioned
- Location recorded

### Phase 2: Upload
- Evidence Owner uploads to designated location
- Link added to Evidence Register
- Status auto-updates to VALID (if within frequency)

### Phase 3: Validation
- Control Owner reviews evidence
- Confirms completeness
- Adds comments if needed

### Phase 4: Audit
- Internal audit samples evidence
- External auditor may request copies
- Auditor Notes logged

### Phase 5: Archival
- After 7-year retention window
- Evidence moved to archive folder
- Register row marked ARCHIVED
- Evidence deleted per data governance policy

---

## 12. Data Protection & Retention

### Security Controls

| Aspect | Requirement |
|--------|------------|
| **Access** | Role-based (view/edit permissions locked by role) |
| **Encryption** | At rest (folder) and in transit (HTTPS only) |
| **Backup** | Covered under BCP controls (EATGF-BCP-*) |
| **Audit Trail** | Version history enabled, timestamps immutable |
| **Integrity** | Formula-driven status prevents manual manipulation |

### Retention Policy

| Category | Retention Period |
|----------|------------------|
| **Active Evidence** | Current review cycle + 1 year |
| **Archived Evidence** | 7 years from generation |
| **Audit Records** | 7 years minimum |
| **Dashboard Snapshots** | 3 years (historical trend) |

---

## 13. Implementation Checklist

### Pre-Launch (Week 1)

- [ ] Create Excel workbook with 4 tabs
- [ ] Import all 35 MCM controls into MASTER_CONTROL_IMPORT tab
- [ ] Define formulas for auto-calculations
- [ ] Set up conditional formatting for status colors
- [ ] Lock all formula columns
- [ ] Configure role-based access

### Launch (Week 2)

- [ ] Train Evidence Owners on upload procedures
- [ ] Train Control Owners on validation process
- [ ] Set up automated reminder emails
- [ ] Load historical evidence (if any)
- [ ] Publish to shared governance folder

### Ongoing (Monthly)

- [ ] Monitor DASHBOARD for trending KPIs
- [ ] Escalate overdue evidence
- [ ] Archive completed audit cycles
- [ ] Update MCM linkages if controls change

---

## 14. Sample Evidence Register Rows

### Example 1: Security Control (DSS)

| Control ID | Control Title | Evidence Description | Evidence Location | Evidence Owner | Last Review Date | Next Review Date | Status |
|------------|---------------|----------------------|-------------------|-----------------|-----------------|-----------------|--------|
| EATGF-DSS-SEC-01 | IAM & Access Control | Q1 2026 Access Review Report | [SharePoint URL] | Manager, Identity | 2026-01-20 | 2026-04-20 | VALID |

### Example 2: Governance Control (EDM)

| Control ID | Control Title | Evidence Description | Evidence Location | Evidence Owner | Last Review Date | Next Review Date | Status |
|------------|---------------|----------------------|-------------------|-----------------|-----------------|-----------------|--------|
| EATGF-EDM-GOV-01 | Governance Charter | Board Approval – Governance Charter v2.1 | [Confluence URL] | General Counsel | 2026-01-10 | 2027-01-10 | VALID |

### Example 3: AI Control (42001)

| Control ID | Control Title | Evidence Description | Evidence Location | Evidence Owner | Last Review Date | Next Review Date | Status |
|------------|---------------|----------------------|-------------------|-----------------|-----------------|-----------------|--------|
| EATGF-AI-RISK-01 | AI Risk Management | Bias Test Report – Model XYZ v2.0 (Dataset v1.3) | [Git: /models/xyz/bias-report-v2.0.pdf] | Lead, Data Science | 2026-02-01 | 2026-05-01 | VALID |

### Example 4: Missing Evidence

| Control ID | Control Title | Evidence Description | Evidence Location | Evidence Owner | Last Review Date | Next Review Date | Status |
|------------|---------------|----------------------|-------------------|-----------------|-----------------|-----------------|--------|
| EATGF-CLD-SEC-01 | Cloud Security Config | Q1 2026 AWS Config Audit | [EMPTY] | Manager, Cloud Ops | — | 2026-03-30 | MISSING |

---

## 15. Governance & Approval

This Evidence Register architecture is:

✅ **ISO 27001:2022 Compliant** – Operationalizes Clause 9.2 (Internal Audit)  
✅ **ISO 42001:2023 Compliant** – Operationalizes Clause 9 (Performance Evaluation)  
✅ **ISO 19011:2018 Aligned** – Supports audit evidence collection  
✅ **MCM Authority** – All controls sourced from MASTER_CONTROL_MATRIX.md  

No control duplication. MCM remains sole authority.

---

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | Ready for Implementation |
| **Last Updated** | February 13, 2026 |
| **Owner** | Chief Audit Officer / Governance Office |
| **Approver** | Audit Committee (Board Level) |
| **Implementation Timeline** | Week 1-2 of Phase 2 rollout |
| **Related Documents** | ISMS_MANUAL_v1.0, AIMS_MANUAL_v1.0, INTERNAL_AUDIT_PROCEDURE_v1.0 |
