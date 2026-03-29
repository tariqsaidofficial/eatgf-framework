# EVIDENCE_REGISTER_EXCEL_BUILD_SPECIFICATION.md

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
Evidence Register v1.0 – Excel Technical Build Specification

**Buildable. Testable. Audit-Defensible.**

---

**Document:** Technical Implementation Specification  
**Target User:** Excel Developer / Governance Operations  
**Timeline:** 2-day build (experienced) / 1 week (first-time)  
**Testing:** 6-week pilot cycle

---

##  Build Objective

Create a **fully operational, formula-driven, audit-defensible** Evidence Register in Excel that:
-  Enforces time-bound evidence tracking (no manual override)
-  Auto-calculates status based on evidence currency
-  Escalates high-criticality gaps automatically
-  Generates audit-ready reports
-  Maintains 7-year retention enforcement
-  Prevents control duplication or definition drift

---

##  File Structure Overview

```
EVIDENCE_REGISTER_v1.0.xlsx
├── CONTROL_MASTER (Sheet 1) – Read-Only
├── EVIDENCE_TRACKER (Sheet 2) – Primary Operational
├── DASHBOARD (Sheet 3) – Real-time KPIs
├── AUDIT_EXTRACT (Sheet 4) – Report-ready view
└── [Optional] POWER_BI_CONNECTOR (for external BI)
```

---

##  SHEET 1: CONTROL_MASTER

### Purpose
Single source of truth for all 35 MCM controls. Read-only reference layer.

### Column Headers & Source Data

| Column | Name | Type | Source | Locked |
|--------|------|------|--------|--------|
| A | Control ID | Text | MCM v1.0 |  Yes |
| B | Control Title | Text | MCM v1.0 |  Yes |
| C | Domain | Text | MCM v1.0 |  Yes |
| D | Criticality | Text | MCM v1.0 |  Yes |
| E | Residual Risk | Text | MCM v1.0 |  Yes |
| F | Review Frequency | Text | MCM v1.0 |  Yes |
| G | Control Owner | Text | MCM v1.0 |  Yes |
| H | Evidence Owner (Role) | Text | MCM v1.0 |  Yes |

### Sample Data (First 5 Controls)

```
Row 1: Headers
Row 2: EATGF-EDM-GOV-01 | Governance Charter | EDM | High | Medium | Annual | General Counsel | Director, Governance
Row 3: EATGF-EDM-RISK-01 | Risk Criteria Definition | EDM | High | Medium | Annual | CISO | Manager, Risk
Row 4: EATGF-APO-SEC-01 | Information Security Policy | APO | High | Low | Annual | CISO | Manager, Security
Row 5: EATGF-APO-RISK-01 | Risk Assessment & Treatment | APO | High | High | Annual | CISO | Manager, Risk
Row 6: EATGF-APO-AI-01 | AI Policy & Leadership | APO | High | Medium | Semi-Annual | Chief AI Officer | Manager, AI Governance
...
Row 36: [Last control from MCM]
```

### Implementation Steps

1. **Create Sheet Named:** `CONTROL_MASTER`
2. **Add Headers** in Row 1 (A1:H1)
3. **Import Data** from MASTER_CONTROL_MATRIX.md (rows 2–36)
4. **No Editing:** Lock ALL cells (Format → Cells → Protection → Locked)
5. **Protect Sheet:** Sheet → Protect Sheet (set password optional)

---

##  SHEET 2: EVIDENCE_TRACKER (PRIMARY OPERATIONAL)

### Purpose
Live evidence tracking. One row per control per audit cycle.

### Column Headers (Row 1)

| Col | Name | Type | Formula / Validation | Editable |
|-----|------|------|---------------------|----------|
| A | Control ID | Dropdown | Source: CONTROL_MASTER!A:A |  Edit |
| B | Control Title | Auto-lookup | =XLOOKUP(A2,...) |  Read-only |
| C | Domain | Auto-lookup | =XLOOKUP(A2,...) |  Read-only |
| D | Criticality | Auto-lookup | =XLOOKUP(A2,...) |  Read-only |
| E | Residual Risk | Auto-lookup | =XLOOKUP(A2,...) |  Read-only |
| F | Review Frequency | Auto-lookup | =XLOOKUP(A2,...) |  Read-only |
| G | Evidence Description | Text | Max 255 chars |  Edit |
| H | Evidence Location | URL/Path | Validation: URL format |  Edit |
| I | Last Review Date | Date | MM/DD/YYYY format |  Edit |
| J | Next Review Date | Auto-calc | Date formula |  Read-only |
| K | Days Until Expiry | Auto-calc | Days formula |  Read-only |
| L | Evidence Status | Auto-calc | Status formula |  Read-only |
| M | Audit Cycle | Dropdown | 2026-Q1, 2026-Q2, 2026-Annual, etc. |  Edit |
| N | Control Owner | Auto-lookup | =XLOOKUP(A2,...) |  Read-only |
| O | Evidence Owner | Auto-lookup | =XLOOKUP(A2,...) |  Read-only |
| P | Escalation Flag | Auto-calc | IF formula (High + Not Valid) |  Read-only |
| Q | Auditor Notes | Text | Max 500 chars |  Edit |
| R | Corrective Action ID | Text | Link format (e.g., CAL-2026-001) |  Edit |
| S | Retention Until | Auto-calc | =EDATE(I2, 84) |  Read-only |
| T | Evidence Hash (Optional) | Text | SHA256 hex string |  Read-only |
| U | Evidence Integrity Status | Auto-calc | VERIFIED / TAMPERED / N/A |  Read-only |

---

##  FORMULAS – CRITICAL IMPLEMENTATION

### Column A – Control ID (Dropdown Validation)

**Type:** Data Validation (Dropdown)

**Steps:**
1. Select cells A2:A1000
2. Data → Data Validation
3. Allow: List
4. Source: `=CONTROL_MASTER!$A$2:$A$36`
5. In-cell dropdown:  Checked
6. Error Alert:  Checked (message: "Select valid Control ID")

---

### Column B – Control Title (Auto-Lookup)

**Formula:**
```excel
=XLOOKUP(A2, CONTROL_MASTER!$A$2:$A$36, CONTROL_MASTER!$B$2:$B$36, "")
```

**If XLOOKUP not available (older Excel):**
```excel
=IFERROR(INDEX(CONTROL_MASTER!$B$2:$B$36, MATCH(A2, CONTROL_MASTER!$A$2:$A$36, 0)), "")
```

**Steps:**
1. Click cell B2
2. Paste formula
3. Copy down to row 1000 (Ctrl+C, select range, Ctrl+V)
4. Lock cell (Format → Cells → Protection → Locked )

---

### Column C – Domain (Auto-Lookup)

**Formula:**
```excel
=XLOOKUP(A2, CONTROL_MASTER!$A$2:$A$36, CONTROL_MASTER!$C$2:$C$36, "")
```

**Apply same process as Column B**

---

### Column D – Criticality (Auto-Lookup)

**Formula:**
```excel
=XLOOKUP(A2, CONTROL_MASTER!$A$2:$A$36, CONTROL_MASTER!$D$2:$D$36, "")
```

**Conditional formatting:**
- If "High" → Light Red background
- If "Medium" → Light Yellow background
- If "Low" → Light Green background

---

### Column E – Residual Risk (Auto-Lookup)

**Formula:**
```excel
=XLOOKUP(A2, CONTROL_MASTER!$A$2:$A$36, CONTROL_MASTER!$E$2:$E$36, "")
```

---

### Column F – Review Frequency (Auto-Lookup)

**Formula:**
```excel
=XLOOKUP(A2, CONTROL_MASTER!$A$2:$A$36, CONTROL_MASTER!$F$2:$F$36, "")
```

---

### Column G – Evidence Description (Manual Entry)

**Type:** Text

**Validation:**
- Required: Yes (Data Validation → Allow: Custom → Formula: `=LEN(G2)>0`)
- Max length: 255 characters (note: not enforced by Excel, but document requirement)

**Examples:**
- "Q1 2026 IAM Access Review – Signed PDF"
- "AWS Config Audit Report Feb 2026"
- "Model XYZ Bias Test Report v1.2"

---

### Column H – Evidence Location (URL or File Path)

**Type:** URL/Path

**Validation:**
```
Data Validation → Custom Formula:
=OR(ISNUMBER(SEARCH("http", H2)), ISNUMBER(SEARCH("\\", H2)), ISNUMBER(SEARCH("/", H2)))
```

**Examples:**
- `https://sharepoint.company.com/sites/governance/Evidence/2026-Q1-IAM.pdf`
- `\\governance\Evidence\2026\Q1\IAM.pdf`
- `/Volumes/Governance/Evidence/2026/Q1/IAM.pdf` (Mac)

**Required:** Yes (cannot be blank if Last Review Date is filled)

---

### Column I – Last Review Date (Manual Entry)

**Type:** Date (MM/DD/YYYY)

**Validation:**
```
Data Validation → Allow: Date
Between: 01/01/2000 and TODAY()
```

**Notes:**
- Auditors must enter the date evidence was validated
- Leave blank if no evidence uploaded yet
- By entering this date, Next Review Date auto-calculates

---

### Column J – Next Review Date (AUTO-CALCULATE)

**THE CRITICAL FORMULA – DRIVES ENTIRE WORKFLOW**

```excel
=IF(OR(A2="", F2=""), "",
  IF(F2="Monthly", EDATE(I2, 1),
    IF(F2="Quarterly", EDATE(I2, 3),
      IF(F2="Semi-Annual", EDATE(I2, 6),
        IF(F2="Annual", EDATE(I2, 12),
          IF(F2="Per Release", "", ""))))))
```

**Logic Explanation:**
- If Control ID blank → leave blank
- If Frequency blank → leave blank
- If Monthly → add 1 month to Last Review Date
- If Quarterly → add 3 months
- If Semi-Annual → add 6 months
- If Annual → add 12 months
- If Per Release → leave blank (manual trigger)

**Example:**
- Last Review Date: 01/15/2026, Frequency: Quarterly
- Next Review Date: 04/15/2026

---

### Column K – Days Until Expiry (AUTO-CALCULATE)

**Formula:**
```excel
=IF(J2="", "", J2 - TODAY())
```

**Conditional Formatting:**
- If value < 0 → Red background (EXPIRED)
- If value ≤ 14 → Yellow background (EXPIRING SOON)
- If value > 14 → Green background (OK)

---

### Column L – Evidence Status (AUTO-CALCULATE)  **CRITICAL**

**THIS COLUMN DRIVES ALL AUDIT DECISIONS**

```excel
=IF(OR(A2="", E2=""), "",
  IF(H2="", "MISSING",
    IF(I2="", "MISSING",
      IF(TODAY() > J2, "EXPIRED",
        IF(K2 <= 14, "EXPIRING SOON",
          "VALID")))))
```

**Logic Explanation:**
1. **If no Control ID or no Residual Risk** → blank (skip incomplete rows)
2. **If no Evidence Location** → `MISSING`
3. **If no Last Review Date** → `MISSING`
4. **If TODAY > Next Review Date** → `EXPIRED`
5. **If Days Until Expiry ≤ 14** → `EXPIRING SOON`
6. **Otherwise** → `VALID`

**Possible Outputs (Only):**
-  `VALID` – Evidence current, on schedule
-  `EXPIRING SOON` – Will expire in ≤14 days
-  `EXPIRED` – Past review date, no current evidence
-  `MISSING` – No evidence linked
- [blank] – Incomplete row (skip)

**NO MANUAL OVERRIDE ALLOWED**

---

### Column M – Audit Cycle (Manual Dropdown)

**Type:** Data Validation (Dropdown)

**Options:**
```
2026-Annual
2026-Q1
2026-Q2
2026-Q3
2026-Q4
2026-Incident
[blank]
```

**Purpose:** Track which audit cycle this evidence belongs to.

---

### Column N – Control Owner (Auto-Lookup)

**Formula:**
```excel
=XLOOKUP(A2, CONTROL_MASTER!$A$2:$A$36, CONTROL_MASTER!$G$2:$G$36, "")
```

---

### Column O – Evidence Owner (Auto-Lookup)

**Formula:**
```excel
=XLOOKUP(A2, CONTROL_MASTER!$A$2:$A$36, CONTROL_MASTER!$H$2:$H$36, "")
```

---

### Column P – Escalation Flag (AUTO-CALCULATE) 

**DRIVES EXECUTIVE NOTIFICATIONS**

```excel
=IF(OR(A2="", D2="", L2=""), "",
  IF(AND(D2="High", L2<>"VALID"), "ESCALATE",
    IF(AND(E2="High", L2="EXPIRED"), "ESCALATE",
      IF(AND(L2="MISSING", D2="High"), "ESCALATE",
        ""))))
```

**Logic:**
1. **High Criticality + Not Valid** → `ESCALATE`
2. **High Residual Risk + Expired** → `ESCALATE`
3. **Missing + High Criticality** → `ESCALATE`
4. Otherwise → [blank]

**Conditional Formatting:**
- If P2 = "ESCALATE"
  - Entire row: **Bold text + Red border**
  - Row background: Light red

**Usage:** Governance Office scans for "ESCALATE" flags for board notification.

---

### Column Q – Auditor Notes (Manual Entry)

**Type:** Text

**Max Length:** 500 characters (document requirement)

**Examples:**
- "Approved during audit – no deviations"
- "Evidence incomplete – remediation due by 03/15/2026"
- "Control owner absent – evidence validation deferred"

---

### Column R – Corrective Action ID (Manual Reference)

**Type:** Text (Link format)

**Format:** `[Audit Log ID]-[Control ID]-[Year]`

**Examples:**
- `CAL-2026-001-DSS-SEC-01`
- `CAL-2026-015-AI-RISK-01`

**Usage:** Links evidence record to specific corrective action ticket.

---

### Column S – Retention Until (AUTO-CALCULATE)

**Formula:**
```excel
=IF(I2="", "", EDATE(I2, 84))
```

**Logic:** Evidence must be retained 7 years from Last Review Date
- 7 years = 84 months
- EDATE(date, 84) calculates exact retention deadline

**Example:**
- Last Review Date: 01/15/2026
- Retention Until: 01/15/2033

**Conditional Formatting:**
- If TODAY() is within 6 months → Yellow (archival approaching)
- If TODAY() > Retention Until → Red (ARCHIVE IMMEDIATELY)

---

### Column T – Evidence Hash (OPTIONAL – Evidence Integrity Protection)

**Purpose:** Cryptographic proof that evidence file has NOT been modified after upload

**Type:** Text (SHA256 hex string)

**Implementation Options:**

**Option 1: Manual Hash Entry (Easy)**
- Evidence Owner calculates SHA256 hash of PDF
- Command line (Windows): `certutil -hashfile "C:\path\file.pdf" SHA256`
- Command line (Mac): `shasum -a 256 /path/file.pdf`
- Copies hex string into Column T
- Cost: 30 seconds per file

**Option 2: Automated Hash Calculation (Advanced)**
- Scripts hash on upload (requires IT)
- PowerShell script monitors folder
- On file arrival: calculates SHA256, enters into Excel
- Cost: Setup time, then automatic

**Storage:** 64-character hexadecimal string
```
Example: a3e8c72b9f4b1e6dfc2a9d5e1b3c4f6a8e9d2c5a7b8e9f0d1c2a3b4e5f6a7b
```

**Format:** Read-only, locked cell (no manual edits allowed)

**Verification Process (During Audit):**

Auditor validates integrity:
```
Step 1: Download evidence file from repository
Step 2: Calculate SHA256 hash of downloaded file
Step 3: Compare with Column T value
        IF Match →  VERIFIED (file unchanged since upload)
        IF Different →  TAMPERED (file modified, investigate)
```

---

### Column U – Evidence Integrity Status (AUTO-CALCULATED)

**Purpose:** Real-time flag indicating evidence integrity state

**Type:** Auto-calculated (locked, no edit)

**Logic:**

If Column T is blank:
```excel
"N/A" (hash not tracked for this evidence)
```

If Column T has value AND evidence file still in repository:
```excel
"VERIFIED" (physical hash verification pending auditor check)
```

If Column T has value AND evidence file MISSING from repository:
```excel
"FILE MISSING" (evidence reference broken, investigate)
```

**Display:** Shows integrity confidence
-  N/A = No hash tracking (acceptable)
-  VERIFIED = Hash present, file present (good)
-  FILE MISSING = Critical (evidence unavailable)

**Auditor Use:** During audit, if any "FILE MISSING" → immediate escalation

---

### Evidence Integrity Workflow (During Audit)

**Week 3 (Pilot Audit) Procedure:**

1. **Auditor receives Excel register** (EVIDENCE_TRACKER)
2. **For each control with high evidence importance:**
   - Check: Does Column T have hash value?
   - Download evidence file from repository
   - Calculate: `shasum -a 256 [file]` (or `certutil` on Windows)
   - Compare: Result with Column T
   - Document:  VERIFIED or  TAMPERED
3. **If hash mismatch found:**
   - Escalate to Governance Office immediately
   - Root cause: Who modified? When? Why?
   - Corrective action: Re-upload unmodified evidence
4. **Audit finding (if applicable):**
   - Evidence integrity violation
   - Control: Requires repository access controls

---

##  Evidence Repository Control Requirements

**Before Week 1 Launch, Confirm Repository Supports:**

### Requirement 1: Version History
-  Every file upload creates timestamped version
-  Previous versions retained (not overwritten)
-  Auditor can request version as of [specific date]

**Check:** SharePoint / OneDrive / Confluence / Git all support this by default

### Requirement 2: Restricted Write Access
-  Evidence Owners can UPLOAD (write)
-  Evidence Owners can READ their own evidence
-  Control Owners can READ (not write/delete)
-  Auditors can READ (not write/delete)
-  NO ONE can DELETE uploaded evidence (except IT after 7-year retention)

**Check:** Apply folder-level permissions (NTFS or cloud equivalent)

### Requirement 3: Access Logging
-  Every file access logged (date, time, user, action)
-  Logs retained minimum 1 year
-  Logs auditable (not deletable by regular users)

**Check:** SharePoint → Site Audit Logs active?  OneDrive → Audit retained?  Confluence → Access tracking enabled?

---

**If ALL 3 Repository Requirements MET:**
→ Evidence Hash column is OPTIONAL (nice-to-have)
→ Week 1 can proceed immediately

**If ANY Repository Requirement NOT MET:**
→ Must create temporary policy
→ Deploy "Evidence Integrity & Repository Control Policy" first
→ Then proceed Week 1

---

##  SHEET 2: CONDITIONAL FORMATTING RULES

### Rule 1 – Evidence Status Color Coding

**Apply to Column L (Evidence Status)**

```
Format as follows:

IF L2 = "VALID"
  → Fill Color: Light Green (#C6EFCE)
  → Font Color: Dark Green

IF L2 = "EXPIRING SOON"
  → Fill Color: Light Yellow (#FFEB9C)
  → Font Color: Orange

IF L2 = "EXPIRED"
  → Fill Color: Light Red (#FFC7CE)
  → Font Color: Dark Red

IF L2 = "MISSING"
  → Fill Color: Dark Red / White text
  → Font Color: White
```

---

### Rule 2 – Escalation Flag Row Highlighting

**Apply to Columns A:S (Entire row)**

```
IF P2 = "ESCALATE"
  → Fill Color: Light Red (#FFE6E6)
  → Border: Thick red line (2pt)
  → Font: Bold

Purpose: Visual alert that row requires immediate attention
```

---

### Rule 3 – Criticality Color Coding

**Apply to Column D (Criticality)**

```
IF D2 = "High"
  → Fill Color: Light Red (#FFC7CE)
  → Font: Bold

IF D2 = "Medium"
  → Fill Color: Light Yellow (#FFEB9C)

IF D2 = "Low"
  → Fill Color: Light Green (#C6EFCE)
```

---

### Rule 4 – Days to Expiry Warning

**Apply to Column K (Days Until Expiry)**

```
IF K2 < 0
  → Fill: Red, Font: White, Bold
  → Message: EXPIRED

IF K2 between 0-14
  → Fill: Yellow
  → Message: EXPIRING SOON

IF K2 > 14
  → Fill: Green
  → Message: OK
```

---

##  SHEET 3: DASHBOARD (Real-Time KPIs)

### Purpose
Executive visibility into governance compliance status.

### KPI Layout

**Row 1–2: Overall Metrics**

| Cell | KPI | Formula | Target | Current |
|------|-----|---------|--------|---------|
| A1 | **GOVERNANCE COMPLIANCE DASHBOARD** | | | |
| A3 | Overall Evidence Compliance % | `=COUNTIF(EVIDENCE_TRACKER!L:L,"VALID")/COUNTA(EVIDENCE_TRACKER!A:A)*100` | ≥95% | [Auto] |
| A4 | Evidence Overdue % | `=COUNTIF(EVIDENCE_TRACKER!L:L,"EXPIRED")/COUNTA(EVIDENCE_TRACKER!A:A)*100` | <5% | [Auto] |
| A5 | Evidence Missing % | `=COUNTIF(EVIDENCE_TRACKER!L:L,"MISSING")/COUNTA(EVIDENCE_TRACKER!A:A)*100` | <3% | [Auto] |
| A6 | Escalations Pending | `=COUNTIF(EVIDENCE_TRACKER!P:P,"ESCALATE")` | <5 | [Auto] |

---

**Row 7–12: By Domain**

| Domain | Count | Valid % | Status |
|--------|-------|---------|--------|
| EDM | `=COUNTIF(EVIDENCE_TRACKER!C:C,"EDM")` | `=COUNTIFS(EVIDENCE_TRACKER!C:C,"EDM",EVIDENCE_TRACKER!L:L,"VALID")/COUNTIF(EVIDENCE_TRACKER!C:C,"EDM")*100` | [Conditional] |
| APO | [Similar] | [Similar] | [Conditional] |
| BAI | [Similar] | [Similar] | [Conditional] |
| DSS | [Similar] | [Similar] | [Conditional] |
| MEA | [Similar] | [Similar] | [Conditional] |
| AI | [Similar] | [Similar] | [Conditional] |
| CLOUD | [Similar] | [Similar] | [Conditional] |

---

**Row 13–16: By Criticality**

| Criticality | Count | Valid % | Escalation % |
|-------------|-------|---------|--------------|
| High | `=COUNTIF(EVIDENCE_TRACKER!D:D,"High")` | `=COUNTIFS(EVIDENCE_TRACKER!D:D,"High",EVIDENCE_TRACKER!L:L,"VALID")/COUNTIF(EVIDENCE_TRACKER!D:D,"High")*100` | `=COUNTIFS(EVIDENCE_TRACKER!D:D,"High",EVIDENCE_TRACKER!P:P,"ESCALATE")/COUNTIF(EVIDENCE_TRACKER!D:D,"High")*100` |
| Medium | [Similar] | [Similar] | [Similar] |
| Low | [Similar] | [Similar] | [Similar] |

---

**Row 17–20: Upcoming Deadlines (Next 30 Days)**

```
Control ID | Next Review Date | Days | Status | Owner
[Filtered list from EVIDENCE_TRACKER where K2 <= 30 and K2 >= 0]
```

**Formula approach:** Create pivot table or manual filter + copy

---

##  SHEET 2: DATA PROTECTION & LOCKING

### Protection Strategy

**Unlock these cells ONLY (allow editing):**
- Column A (Control ID selection)
- Column G (Evidence Description)
- Column H (Evidence Location)
- Column I (Last Review Date)
- Column M (Audit Cycle)
- Column Q (Auditor Notes)
- Column R (Corrective Action ID)

**Lock ALL other cells** (formulas, lookups, calculations)

### Steps to Implement

1. **Select all cells:** Ctrl+A
2. **Lock all:** Format → Cells → Protection tab →  Locked
3. **Select editable columns:** Hold Ctrl, click each column header
4. **Unlock selected:** Format → Cells → Protection tab →  Uncheck Locked
5. **Protect sheet:** Review tab → Protect Sheet → Set password (optional)

---

##  AUTOMATED WORKFLOWS

### Workflow 1 – Monthly Governance Alert (Email Export)

**Trigger:** 1st of each month

**Filter EVIDENCE_TRACKER for:**
- L column = "EXPIRED" OR "EXPIRING SOON" OR "MISSING"

**Export to PDF & email:**
- **To:** All Control Owners + Governance Office
- **Subject:** "Monthly Governance Compliance Alert – Action Required"
- **Body:** Summary of non-compliant controls + owners + due dates

---

### Workflow 2 – Quarterly Audit Extract

**Trigger:** Start of each audit quarter (Jan 1, Apr 1, Jul 1, Oct 1)

**Filter EVIDENCE_TRACKER for:**
- M column = "2026-Q1" (or current quarter)

**Export to PDF & send to:**
- **To:** Internal Audit Function + Governance Council
- **Timestamp:** Audit cycle identifier

---

### Workflow 3 – Critical Escalation Alert

**Trigger:** Any time P column = "ESCALATE"

**Action:**
- Flag row
- Email to: CISO + Chief AI Officer + Governance Council
- **Subject:** " CRITICAL – Control Escalation Required"
- **Content:** Control ID + Owner + Issue + Deadline

---

##  FILE SETUP CHECKLIST

- [ ] Create new Excel workbook
- [ ] Create CONTROL_MASTER sheet (import from MCM, lock all)
- [ ] Create EVIDENCE_TRACKER sheet with headers A–S
- [ ] Setup Column A – Dropdown validation (Control ID)
- [ ] Setup Columns B–F, N–O, P – XLOOKUP formulas
- [ ] Setup Column J – Next Review Date formula
- [ ] Setup Column K – Days Until Expiry formula
- [ ] Setup Column L – Evidence Status formula (test logic)
- [ ] Setup Column P – Escalation Flag formula
- [ ] Setup Column S – Retention Until formula
- [ ] Apply conditional formatting (all 4 rules)
- [ ] Lock formula columns (protect editable columns)
- [ ] Protect CONTROL_MASTER sheet (read-only)
- [ ] Create DASHBOARD sheet with KPI formulas
- [ ] Create AUDIT_EXTRACT sheet (filtered view)
- [ ] Test with sample data (3 controls, different frequencies)
- [ ] Save as EVIDENCE_REGISTER_v1.0.xlsx
- [ ] Version in footer: v1.0 – Built [Date] – By [Name]

---

##  TESTING PROTOCOL

### Test Case 1 – Annual Control with Valid Evidence

```
Input:
  Control ID: EATGF-EDM-GOV-01
  Evidence Description: Board Approval – Governance Charter v2.1
  Evidence Location: https://sharepoint.../governance-charter.pdf
  Last Review Date: 01/10/2026
  Frequency: Annual

Expected Output:
  Next Review Date: 01/10/2027
  Days Until Expiry: 332
  Evidence Status: VALID 
  Escalation Flag: [blank]
```

---

### Test Case 2 – Quarterly Control with Missing Evidence

```
Input:
  Control ID: EATGF-DSS-SEC-01
  Evidence Description: [blank]
  Evidence Location: [blank]
  Last Review Date: [blank]
  Frequency: Quarterly

Expected Output:
  Next Review Date: [blank]
  Days Until Expiry: [blank]
  Evidence Status: MISSING 
  Escalation Flag: ESCALATE  (if Criticality = High)
```

---

### Test Case 3 – Quarterly Control with Expired Evidence

```
Input:
  Control ID: EATGF-DSS-ENC-01
  Evidence Description: Q4 2025 Encryption Audit
  Evidence Location: \\governance\evidence\2025\Q4\encryption.pdf
  Last Review Date: 11/01/2025
  Frequency: Quarterly

Expected Output:
  Next Review Date: 02/01/2026
  Days Until Expiry: -13 (today is Feb 15, 2026)
  Evidence Status: EXPIRED 
  Escalation Flag: ESCALATE  (if Criticality = High)
```

---

### Test Case 4 – Semi-Annual Control (Expiring Soon)

```
Input:
  Control ID: EATGF-APO-AI-01
  Evidence Description: 2026 AI Risk Assessment
  Evidence Location: https://drive.../ai-risk-2026.pdf
  Last Review Date: 01/20/2026
  Frequency: Semi-Annual

Expected Output:
  Next Review Date: 07/20/2026
  Days Until Expiry: 156 (today is Feb 15, 2026)
  Evidence Status: VALID 
  Escalation Flag: [blank]
```

---

##  STABILIZATION PILOT SEQUENCE

### Week 1 – Load & Test

```
Tasks:
  [ ] Build Excel structure (all 4 sheets)
  [ ] Import 35 controls into CONTROL_MASTER
  [ ] Test with 3 sample controls (different frequencies)
  [ ] Verify all formulas working
  [ ] Lock/protect sheets

Deliverable:
  EVIDENCE_REGISTER_v1.0.xlsx (test build)
```

---

### Week 2 – Populate High-Criticality Controls

```
Controls to load (evidence data):
   EATGF-EDM-GOV-01 (Governance Charter)
   EATGF-APO-SEC-01 (Information Security Policy)
   EATGF-APO-RISK-01 (Risk Assessment & Treatment)
   EATGF-DSS-SEC-01 (IAM & Access Control)
   EATGF-DSS-ENC-01 (Encryption Standards)
   EATGF-DSS-INC-01 (Incident Management)
   EATGF-AI-LC-01 (AI Lifecycle Governance)
   EATGF-AI-RISK-01 (AI Risk Management)

For each:
  [ ] Evidence Description: Clear, specific
  [ ] Evidence Location: Working URL/path
  [ ] Last Review Date: Realistic date
  [ ] Formula outputs (Status, Escalation) verify automatically

Deliverable:
  Populated register (8 high-criticality controls with evidence)
```

---

### Week 3 – Pilot Audit (10 Controls)

```
Audit these 10 controls:
  • 8 loaded controls (above)
  • 2 additional controls (sample missing evidence)

Auditor validation:
  [ ] Is evidence clear & verifiable?
  [ ] Do formula outputs match reality?
  [ ] Is escalation logic working?
  [ ] Are dates auto-calculating correctly?
  [ ] Can auditor add notes without breaking formulas?

Deliverable:
  Pilot Audit Report (documented findings)
```

---

### Week 4 – Gap Hardening

```
Based on pilot findings:
  [ ] Adjust frequency if needed
  [ ] Clarify evidence descriptions
  [ ] Verify ownership assignments
  [ ] Test edge cases (Per Release frequency, null values)
  [ ] Check date format consistency

No structural changes. Only refinements.

Deliverable:
  Updated EVIDENCE_REGISTER_v1.0.XLSX (refined)
```

---

### Week 5–6 – Full Internal Audit

```
Audit all 35 controls:
  [ ] Load all remaining controls (evidencedata)
  [ ] Run complete audit cycle
  [ ] Generate audit report
  [ ] Execute corrective action process
  [ ] Formal Management Review

Deliverable:
  Complete Audit Report
  Corrective Action Log
  Management Review Minutes
```

---

## � PRE-WEEK 1 CHECKLIST – Before Excel Build Starts

**CRITICAL:** Verify Evidence Repository meets integrity requirements BEFORE starting Week 1

### Repository Integrity Verification (Friday, Feb 13)

Use the verification checklist from:  
[EVIDENCE_INTEGRITY_AND_REPOSITORY_CONTROL_POLICY.md](EVIDENCE_INTEGRITY_AND_REPOSITORY_CONTROL_POLICY.md)

**Three Mandatory Capabilities:**

```
[ ] CAPABILITY 1 – VERSION HISTORY
    [ ] Previous versions retained (not overwritten)
    [ ] Timestamp recorded for each version
    [ ] Test: Upload file → Modify → Check history → Both visible?
    STATUS:  PASS /  FAIL

[ ] CAPABILITY 2 – RESTRICTED WRITE
    [ ] Evidence Owner can UPLOAD
    [ ] Evidence Owner CANNOT DELETE
    [ ] Control Owner can READ ONLY
    [ ] Test: Try delete as non-owner → DENIED?
    STATUS:  PASS /  FAIL

[ ] CAPABILITY 3 – ACCESS LOGGING
    [ ] All uploads logged (date, time, user)
    [ ] All downloads logged
    [ ] Logs retained ≥1 year
    [ ] Test: Request access log for file → Provided?
    STATUS:  PASS /  FAIL
```

**Decision Gate:**

-  **ALL 3 PASS:** → Excel build can start Monday (Feb 16)
-  **ANY FAIL:** → Remediate repository first (policy: Section 5 has setup steps)

### Evidence Hash Setup (If Using)

**If deploying SHA256 hash verification:**

- [ ] Evidence Owner computers have:
  - Windows: certutil installed (built-in)
  - Mac: shasum installed (built-in)
- [ ] Test hash calculation on sample file works
- [ ] EVIDENCE_REGISTER Column T ready (template cell for hash paste)

**If NOT using hash:**
- [ ] Note: Repository-level version history + access logging alone sufficient
- [ ] Leave Column T empty (optional feature)

### Team Training Prep

**Materials to review before Week 1:**

- [ ] Evidence Owner: "How to Upload Evidence" guide (from this spec)
- [ ] Control Owner: "How to Validate Evidence" checklist
- [ ] Auditor: "Hash Verification Procedure" (if hashing enabled)

**Training sessions scheduled:**

- [ ] Evidence Owners: 30 min (Wed, Feb 17)
- [ ] Control Owners: 30 min (Wed, Feb 17)
- [ ] Auditors: 45 min (potentially, depends on complexity)

---

## � After Phase 2 Stabilization Complete

**If pilot audit is successful:**

 ISMS operational  
 AIMS operational  
 Audit procedures validated  
 Evidence tracking proven  

**Decision:** Proceed to **Phase 3 – Edition Deployment Model**

- Startup Edition (5-8 critical controls)
- SaaS Edition (18-22 controls)
- Enterprise Edition (all 35 controls)

---

##  Document Control

| Field | Value |
|-------|-------|
| **Document** | EVIDENCE_REGISTER_EXCEL_BUILD_SPECIFICATION.md |
| **Version** | 1.0 |
| **Status** | Ready for Implementation |
| **Build Time Estimate** | 2 days (experienced) / 1 week (first-time) |
| **Testing Timeline** | 6 weeks (phase 2 stabilization) |
| **Date Created** | February 13, 2026 |
| **Owner** | Governance Operations / Excel Developer |

---

** This is NOT a template.**

**This is a fully specified build plan. Give to developer → They build → Test → Use.**

**Ready to execute Phase 2 Stabilization?**
