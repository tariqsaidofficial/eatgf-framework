# EVIDENCE_REGISTER_IMPLEMENTATION_GUIDE.md

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
Evidence Register – Excel Workbook Setup Guide

---

## Quick Start: Building EVIDENCE_REGISTER.xlsx

This guide takes you from specification to operational in **2 hours**.

---

## Step 1: Create Excel Workbook Structure

### Create 4 Worksheets:
1. MASTER_CONTROL_IMPORT
2. ACTIVE_EVIDENCE_TRACKER
3. AUDIT_VIEW
4. DASHBOARD

**In Excel:**
```
Right-click tab → Insert Sheet → Name each tab
```

---

## Step 2: Setup MASTER_CONTROL_IMPORT Tab

### Column Headers (Row 1):
```
A: Control ID
B: Control Title
C: Domain
D: Criticality
E: Residual Risk
F: Clause Reference
G: Evidence Type
H: Frequency
```

### Import All 35 MCM Controls

**Source:** MASTER_CONTROL_MATRIX.md

**Method:**
1. Open MCM document
2. Copy control data (Control ID, Title, Domain, etc.)
3. Paste into MASTER_CONTROL_IMPORT rows 2–36

**Example rows:**

```
Row 2:  EATGF-EDM-GOV-01 | Governance Charter | EDM | High | Medium | 27001:5.1 | Document | Annual
Row 3:  EATGF-EDM-RISK-01 | Risk Criteria Definition | EDM | High | Medium | 27001:6.1 | Assessment | Annual
Row 4:  EATGF-APO-SEC-01 | Information Security Policy | APO | High | Low | 27001:5.2 | Document | Annual
...
Row 36: EATGF-AI-RISK-01 | AI Risk Management | AI | High | Medium | 42001:6.1 | Assessment | Quarterly
```

### Lock This Tab
**In Excel:**
```
Review tab → Protect Sheet → Password protect (optional)
Purpose: Prevent accidental edits to control definitions
```

---

## Step 3: Setup ACTIVE_EVIDENCE_TRACKER Tab

### Column Headers (Row 1):
```
A: Control ID
B: Control Title
C: Domain
D: Criticality
E: Residual Risk
F: Clause Ref
G: Evidence Type
H: Evidence Description
I: Evidence Location
J: Evidence Owner (Role)
K: Control Owner (Role)
L: Review Frequency
M: Last Review Date
N: Next Review Date
O: Days Until Due
P: Audit Cycle
Q: Status
R: Status Color
S: Auditor Notes
T: Corrective Action Ref
U: Evidence Retention Until
V: Last Updated By
W: Last Updated Date
```

### Populate Starting Rows

**For each control in MASTER_CONTROL_IMPORT:**

If Control = Annual Frequency:
```
Create 1 row per year
Example: EATGF-EDM-GOV-01 (Annual)
  Row 2: 2026 evidence cycle
  Row 3: 2027 evidence cycle (placeholder)
```

If Control = Quarterly Frequency:
```
Create 4 rows per year
Example: EATGF-DSS-SEC-01 (Quarterly)
  Row 2: Q1 2026
  Row 3: Q2 2026
  Row 4: Q3 2026
  Row 5: Q4 2026
```

### Formula Setup

**Column N (Next Review Date) – Calculate based on frequency:**

```Excel
=IF(L2="Monthly", M2+30,
  IF(L2="Quarterly", M2+90,
    IF(L2="Semi-Annual", M2+180,
      IF(L2="Annual", M2+365, ""))))
```

**Column O (Days Until Due):**

```Excel
=IF(N2="", "", N2-TODAY())
```

**Column Q (Status) – Auto-calculated:**

```Excel
=IF(I2="", "MISSING",
  IF(TODAY()>N2, "EXPIRED",
    IF(M2="", "MISSING",
      IF(O2>0, "VALID", "EXPIRED"))))
```

**Column R (Status Color) – For conditional formatting:**

```Excel
=IF(Q2="VALID", "Green",
  IF(Q2="EXPIRED", "Red",
    IF(Q2="MISSING", "Orange",
      IF(Q2="ACTION REQUIRED", "Red", "Gray"))))
```

**Column U (Evidence Retention Until) – 7-year retention:**

```Excel
=IF(M2="", "", DATE(YEAR(M2)+7, MONTH(M2), DAY(M2)))
```

### Conditional Formatting

**For Column Q (Status):**

```
New Rule → Formula Is
Green fill:   =Q2="VALID"
Yellow fill:  =Q2="ACTION REQUIRED"
Orange fill:  =Q2="MISSING"
Red fill:     =Q2="EXPIRED"
```

---

## Step 4: Setup AUDIT_VIEW Tab

### Purpose: Read-only filtered views for audit weeks

### Setup Method:

1. **Copy** all columns from ACTIVE_EVIDENCE_TRACKER
2. **Add data validation filters** (automatic refresh)
3. **Filter criteria** (Excel AutoFilter):

```
Show ONLY if:
  • Next Review Date ≤ TODAY() + 30 days
  OR
  • Status = "MISSING"
  OR
  • Status = "ACTION REQUIRED"
  OR
  • Criticality = "High"
```

### How to Apply AutoFilter in Excel:

```
1. Select all data in tab
2. Data menu → AutoFilter
3. Click dropdown arrows on each column header
4. Custom Filter → Set conditions above
```

### Auditor Workflow:
- Auditors open AUDIT_VIEW during audit week
- Pre-filtered to show controls requiring attention
- Add notes in Column S (Auditor Notes)
- Click evidence links in Column I for validation

---

## Step 5: Setup DASHBOARD Tab

### Purpose: Real-time KPI visibility

### Dashboard Layout:

**Row 1-5: SLA Metrics**

```
A1: KPI
B1: Target
C1: Current
D1: Status

A2: Overall Compliance %
B2: >=95%
C2: =COUNTIF(ACTIVE_EVIDENCE_TRACKER!Q:Q,"VALID")/COUNTA(ACTIVE_EVIDENCE_TRACKER!A:A)
D2: =IF(C2>=B2," PASS", " FAIL")

A3: Critical Controls Coverage %
B3: 100%
C3: =COUNTIFS(ACTIVE_EVIDENCE_TRACKER!D:D,"High",ACTIVE_EVIDENCE_TRACKER!Q:Q,"VALID")/COUNTIF(ACTIVE_EVIDENCE_TRACKER!D:D,"High")
D3: =IF(C3=1," PASS", " FAIL")

A4: Evidence Overdue %
B4: <5%
C4: =COUNTIF(ACTIVE_EVIDENCE_TRACKER!Q:Q,"EXPIRED")/COUNTA(ACTIVE_EVIDENCE_TRACKER!A:A)
D4: =IF(C4<B4," PASS", " FAIL")

A5: Corrective Actions Open
B5: <10
C5: =COUNTIF(ACTIVE_EVIDENCE_TRACKER!Q:Q,"ACTION REQUIRED")
D5: =IF(C5<B5," PASS", " FAIL")
```

**Row 7-10: Coverage by Domain**

| Domain | Count | Coverage | Status |
|--------|-------|----------|--------|
| EDM | 7 | 100% |  |
| APO | 8 | 88% |  |
| BAI | 6 | 100% |  |
| DSS | 8 | 100% |  |
| MEA | 2 | 100% |  |
| AI | 3 | 100% |  |
| CLOUD | 1 | 100% |  |

**Formula Example (for EDM):**

```Excel
A7: EDM
B7: =COUNTIF(ACTIVE_EVIDENCE_TRACKER!C:C,"EDM")
C7: =COUNTIFS(ACTIVE_EVIDENCE_TRACKER!C:C,"EDM",ACTIVE_EVIDENCE_TRACKER!Q:Q,"VALID")/B7
D7: =IF(C7>=0.95,"","")
```

**Row 12-15: Upcoming Deadlines (Next 30 days)**

```
A12: Next Review Due Within 30 Days
A13-A20: Control ID | Next Review Date | Days | Status
[Auto-filter from ACTIVE_EVIDENCE_TRACKER 
 where Next Review Date <= TODAY()+30]
```

---

## Step 6: Access Control & Protection

### Role-Based Access:

| Role | MASTER | TRACKER | AUDIT | DASHBOARD |
|------|--------|---------|-------|-----------|
| Governance Office | R | RW | RW | RO |
| Evidence Owner | R | RW | — | RO |
| Control Owner | R | R | RW | RO |
| Internal Auditor | R | R | RW | RO |
| Executive | R | — | — | RO |

### Set Permissions in Excel:

```
File → Info → Protect Workbook → Restrict Access
OR
File → Properties → Advanced → Shared Workbooks
```

---

## Step 7: Automation (Optional – Advanced)

### Option 1: Power Automate (Microsoft 365)

Trigger: Weekly run

```
1. Check for Status = "MISSING" OR "EXPIRED"
2. Send email to Evidence Owner
3. CC Control Owner
4. Include Evidence Description + Due Date
```

### Option 2: VBA Macro (if you have IT support)

```VBA
Sub HighlightOverdueControls()
  ' Auto-highlight EXPIRED controls
  ' Run daily
End Sub
```

### Option 3: Google Sheets + Apps Script

```JavaScript
function checkOverdueEvidence() {
  // Parse ACTIVE_EVIDENCE_TRACKER
  // Find Status = EXPIRED
  // Send email notification
}
```

---

## Step 8: Initial Data Load (Weeks 1-2)

### Week 1: Setup infrastructure

- [ ] Create Excel workbook
- [ ] Define all columns & formulas
- [ ] Lock MASTER_CONTROL_IMPORT tab
- [ ] Test AutoFilter on AUDIT_VIEW
- [ ] Verify DASHBOARD calculations

### Week 2: Load evidence

- [ ] Contact Evidence Owners for current evidence
- [ ] Populate Last Review Date column
- [ ] Add Evidence Descriptions
- [ ] Add Evidence Locations (URLs/paths)
- [ ] Validate all links accessible

### Week 3: Training & Launch

- [ ] Train Evidence Owners (30 min session)
- [ ] Train Control Owners (30 min session)
- [ ] Train Internal Auditors (45 min session)
- [ ] Publish to shared folder
- [ ] Send reminder schedule

---

## Step 9: Ongoing Operations

### Monthly Governance Cycle:

**Week 1 of Month:**
- Governance Office opens DASHBOARD
- Reviews KPIs
- Identifies MISSING or EXPIRED controls

**Week 2 of Month:**
- Send reminders to Evidence Owners (overdue evidence)
- Escalate to Control Owners (if >7 days overdue)

**Week 3-4 of Month:**
- Evidence Owners upload new evidence
- Control Owners validate
- Status auto-updates

### Quarterly Audit Cycle:

- Open AUDIT_VIEW
- Auditors sample evidence
- Add Auditor Notes
- Link Corrective Actions if needed
- Export to PDF for auditor deliverable

---

## Step 10: External Auditor Handoff

### What to Export:

**For ISO 27001 Auditor:**
```
Export ACTIVE_EVIDENCE_TRACKER 
Filter: All DSS + MEA + EDM controls
PDF → "EATGF_ISMS_Evidence_Register_2026.pdf"
```

**For ISO 42001 Auditor:**
```
Export ACTIVE_EVIDENCE_TRACKER 
Filter: All AI controls + supporting controls
PDF → "EATGF_AIMS_Evidence_Register_2026.pdf"
```

**For Combined Certification:**
```
Export all tabs → ZIP file → send to audit firm
Include: MASTER_CONTROL_IMPORT, ACTIVE_EVIDENCE_TRACKER, DASHBOARD
```

---

## Troubleshooting

### Issue: Formulas not calculating

**Solution:**
```
Excel → Options → Formulas → 
Check "Automatic" is selected (not Manual)
Press Ctrl+Shift+F9 to recalculate all
```

### Issue: Status always shows "MISSING"

**Solution:**
```
Check Evidence Location column (I) not blank
Verify date format is MM/DD/YYYY (or your locale)
Re-enter formula: =IF(I2="", "MISSING", ...)
```

### Issue: DASHBOARD shows errors

**Solution:**
```
Verify MASTER_CONTROL_IMPORT has all 35 controls
Check column references match exactly
Use Ctrl+` (backtick) to show formulas, debug
```

---

## File Organization

```
/governance/
├── EVIDENCE_REGISTER.xlsx              [Primary operational file]
├── EVIDENCE_REGISTER_MASTER.md         [This specification]
├── EVIDENCE_REGISTER_IMPLEMENTATION_GUIDE.md
├── evidence-archive/                   [7-year retention storage]
│   └── 2025-Q4-Archive/
│   └── 2024-Archive/
```

---

## Next Steps After Launch

1. **Month 1:** Stabilize data entry (Evidence Owners trained)
2. **Month 2:** Run pilot audit (Internal Audit samples AUDIT_VIEW)
3. **Month 3:** Generate baseline DASHBOARD snapshot
4. **Month 6:** External auditor uses register during certification audit
5. **Ongoing:** Monthly KPI reviews, quarterly audit cycles

---

**Ready to build?**

Start with **Step 1 → Step 5** (takes ~2 hours)  
Complete **Step 6 → Step 9** by end of Week 1  
Full operational by **Week 2**
