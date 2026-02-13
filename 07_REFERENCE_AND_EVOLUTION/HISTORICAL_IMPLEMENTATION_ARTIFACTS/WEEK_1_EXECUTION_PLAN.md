# WEEK_1_EXECUTION_PLAN.md

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
Phase 2 Stabilization – Week 1 Operational Execution Plan

---

**Status:** 🟢 **EXECUTION MODE ACTIVE**  
**Week 1 Dates:** February 16–20, 2026  
**Approved Repository:** Microsoft SharePoint  
**Integrity Layer:** SHA256 Hash Verification Activated  
**Go Decision:** ✅ APPROVED BY ALL STAKEHOLDERS

---

## 📋 Repository Selection & Justification

### Chosen Repository: Microsoft SharePoint

**Technical Justification:**

| Requirement | SharePoint Capability | Status |
|-------------|----------------------|--------|
| **Version History** | Native immutable versions with timestamp + user attribution | ✅ YES |
| **Restricted Write Access** | Role-based folder/file permissions (RBAC) | ✅ YES |
| **Access Logging** | Microsoft 365 Unified Audit Log (all actions tracked) | ✅ YES |
| **Evidence Integrity** | Purview retention policies + legal hold support | ✅ YES |
| **Audit Compliance** | ISO 27001 / SOC 2 ready, no additional tools needed | ✅ YES |

**Governance Justification:**

- Enterprise standard (no auditor red flags)
- Already deployed (no licensing delays)
- Integrated with M365 ecosystem
- Legal holds enforced at platform level
- Audit logs immutable (cannot be deleted by users)

---

## 🎯 Week 1 Breakdown

### DAY 1–2: Excel Workbook Build

#### Task 1: Create Master Workbook

**File Name:**
```
EATGF_EVIDENCE_REGISTER_v1.0.xlsx
```

**Storage Location:**
```
Local dev folder during build
(Will be moved to SharePoint after validation)
```

**Four Sheets Required:**

1. **CONTROL_MASTER** (Read-only, locked)
   - Import all 35 MCM controls
   - Columns: Control ID, Title, Domain, Criticality, Residual Risk, Frequency, Owner, Evidence Owner
   - No manual editing allowed

2. **EVIDENCE_TRACKER** (Primary operational sheet)
   - Columns A–U (20 columns total)
   - Ready for Week 2 data entry
   - All formulas in place, tested

3. **DASHBOARD** (Real-time KPIs)
   - Compliance % metric
   - Critical controls coverage
   - Expiry warnings
   - Domain breakdown

4. **AUDIT_EXTRACT** (Filtered view for auditors)
   - Auto-filters for audit scope
   - Not populated until Week 3

---

#### Task 2: Implement Integrity Layer (Columns T & U)

**Column T – Evidence Hash (SHA256)**

```
Type: Text (manual entry by Evidence Owner)
Format: 64-character hexadecimal SHA256 hash
Example: a3e8c72b9f4b1e6dfc2a9d5e1b3c4f6a8e9d2c5a7b8e9f0d1c2a3b4e5f6a7b
Editable: YES (Evidence Owner pastes hash after upload)
Purpose: Cryptographic proof of file authenticity
Locked Cell: NO (must allow paste, but read-only after entry – can use data validation)
```

**Column U – Integrity Status (Auto-Calculated)**

```excel
=IF(T2="", "HASH NOT TRACKED",
  IF(T2=[Auditor Recalculated Hash], "✅ VERIFIED",
    "⚠️ HASH MISMATCH - INVESTIGATE"))
```

**Note:** Auditor recalculates hash during audit week; comparison is manual verification step.

---

#### Task 3: Core Formulas (Critical Implementation)

**Column J – Next Review Date:**
```excel
=IF(OR(A2="", F2=""), "",
  IF(F2="Monthly", EDATE(I2, 1),
    IF(F2="Quarterly", EDATE(I2, 3),
      IF(F2="Semi-Annual", EDATE(I2, 6),
        IF(F2="Annual", EDATE(I2, 12), "")))))
```

**Column K – Days Until Expiry:**
```excel
=IF(J2="", "", J2 - TODAY())
```

**Column L – Evidence Status (CRITICAL):**
```excel
=IF(OR(A2="", E2=""), "",
  IF(H2="", "MISSING",
    IF(I2="", "MISSING",
      IF(TODAY() > J2, "EXPIRED",
        IF(K2 <= 14, "EXPIRING SOON",
          "VALID")))))
```

**Column P – Escalation Flag (CRITICAL):**
```excel
=IF(OR(A2="", D2="", L2=""), "",
  IF(AND(D2="High", L2<>"VALID"), "🚨 ESCALATE",
    IF(AND(E2="High", L2="EXPIRED"), "🚨 ESCALATE", "")))
```

**Column S – Retention Until:**
```excel
=IF(I2="", "", EDATE(I2, 84))
```
*(7 years = 84 months)*

---

#### Task 4: Conditional Formatting (Visual Controls)

**Apply to Column L (Evidence Status):**

```
IF Status = "VALID"       → Green fill (#C6EFCE)
IF Status = "EXPIRING SOON" → Yellow fill (#FFEB9C)
IF Status = "EXPIRED"     → Red fill (#FFC7CE)
IF Status = "MISSING"     → Dark Red fill (#C00000) + white text
```

**Apply to Entire Row (P2:U2) if Escalation Flag Present:**

```
IF P2 = "🚨 ESCALATE"     → Bold font + Red border (2pt)
```

**Apply to Column K (Days Until Expiry):**

```
IF K2 < 0                 → Red background
IF K2 between 0-14        → Yellow background
IF K2 > 14                → Green background
```

---

#### Task 5: Sheet Protection

**CONTROL_MASTER Sheet:**
- Protect sheet: YES (read-only)
- Allow: View only
- All cells locked

**EVIDENCE_TRACKER Sheet:**
- Protect sheet: YES (formula integrity)
- Locked columns: B–F (lookups), J–L (status formulas), N–O (ownership), P (escalation), S–U (calculations)
- Editable columns: A (Control ID dropdown), G–I (evidence data), M (audit cycle), Q–R (audit notes/CAL)

**DASHBOARD & AUDIT_EXTRACT:**
- Protect sheet: YES
- All read-only (data flows from EVIDENCE_TRACKER)

---

### DAY 3: SharePoint Configuration

#### Task 1: Create Folder Structure

**Repository Root:** `/EATGF_EVIDENCE/` (in Shared Documents or dedicated site)

**Domain-Based Subfolders:**

```
/EATGF_EVIDENCE/
│
├── /EDM/              (Evaluate, Direct, Monitor)
├── /APO/              (Align, Plan, Organize)
├── /BAI/              (Build, Acquire, Implement)
├── /DSS/              (Deliver, Service, Support)
├── /MEA/              (Monitor, Evaluate, Assess)
├── /CLD/              (Cloud-specific controls)
├── /DEV/              (Development/DevSecOps)
├── /DATA/             (Data & Privacy)
├── /BCP/              (Business Continuity)
├── /AI/               (AI Governance)
└── /API/              (API Security)
```

**Year-Based Subfolders (within each domain):**

```
/EATGF_EVIDENCE/DSS/
├── /2026/
│   ├── /Q1/
│   ├── /Q2/
│   ├── /Q3/
│   └── /Q4/
└── /2027/
    ├── /Q1/
    etc.
```

#### Task 2: Configure Role-Based Access (Permissions)

**SharePoint Site/Folder Level:**

| Role | Permission | Details |
|------|-----------|---------|
| **Evidence Owner** | Contribute | Can upload new files, edit own uploads |
| **Control Owner** | Read | Can view all evidence for their control |
| **Internal Auditor** | Read | Can view all evidence for audit scope |
| **Governance Office** | Contribute | Can manage folder structure, monitor uploads |
| **Repository Admin** | Full Control | Can delete (only after 7-year retention) |

**Implementation Steps:**

1. Open SharePoint site → Site Permissions
2. Create Security Groups:
   - `EATGF_Evidence_Owners` → Add Evidence Owners
   - `EATGF_Control_Owners` → Add Control Owners
   - `EATGF_Auditors` → Add Internal Auditors
   - `EATGF_GovernanceOffice` → Add governance staff

3. Assign permissions to `/EATGF_EVIDENCE/` folder:
   - `EATGF_Evidence_Owners` → Contribute
   - `EATGF_Control_Owners` → Read
   - `EATGF_Auditors` → Read
   - `EATGF_GovernanceOffice` → Contribute

4. **CRITICAL:** Remove "Delete" permission from all groups except Repository Admin

---

#### Task 3: Enable Version History

**In SharePoint:**

1. Navigate to `/EATGF_EVIDENCE/` folder
2. Click folder → Details → Version History
3. Set: **Keep all versions** (or minimum 500 versions)
4. **CRITICAL:** Ensure "Preserve Version History on Deletion" = YES

**Result:**
- Every file upload creates timestamped version
- Files cannot be overwritten; only new versions created
- Previous versions accessible for audit (up to 7 years)

---

#### Task 4: Retention Policy (7-Year Enforcement)

**Using Microsoft Purview:**

1. Go to Purview Compliance Portal
2. Create Retention Label: `EATGF_Evidence_7_Year`
3. Settings:
   - Retention period: 7 years
   - Action after period: Permanently delete (after audit archival)
   - Lock mode: Compliance lock (cannot be disabled)

4. Apply label to `/EATGF_EVIDENCE/` folder
   - All new uploads inherit 7-year retention automatically

**Result:**
- Evidence automatically protected for 7 years
- No manual intervention needed
- Auditor can verify retention active

---

#### Task 5: Enable Audit Logging

**In Microsoft 365 Audit Log:**

1. Go to Microsoft 365 Compliance Center
2. Audit section → Keyword search
3. Configure searches to include:
   - Activities: Upload, Download, Delete, Move, Modify
   - Users: All Evidence Owners
   - Resources: /EATGF_EVIDENCE/ path

4. Set retention: Minimum 1 year (preferably 3 years)

**Verification:**
- Try uploading test file to SharePoint
- Search Audit Log → Should show upload event within 24 hours

---

### DAY 4: Team Training (30 Minutes Only)

#### Agenda

**Duration:** 30 minutes  
**Participants:** Evidence Owners + Control Owners + Auditors + Repository Admin

**Topics:**

1. **SHA256 Hash Calculation (10 min)**
   - Tool recommendation: Windows built-in `certutil` or 7-Zip
   - Example: `certutil -hashfile "C:\path\file.pdf" SHA256`
   - Result: 64-character hex string
   - Copy → Paste into EVIDENCE_REGISTER Column T

2. **Evidence Upload Procedure (10 min)**
   - Navigate to correct SharePoint folder (/EATGF_EVIDENCE/[Domain]/[Year]/[Quarter]/)
   - Upload evidence file (PDF preferred, no overwrites)
   - Confirm version history shows new entry
   - Record file name + upload date

3. **Hash Integrity Discipline (5 min)**
   - Evidence Owner responsibility: Calculate hash after upload
   - If file modified after upload → Hash mismatch → Integrity violation
   - Auditor will verify hash during audit week
   - Escalation: If hash mismatch found → Investigation required

4. **What Happens Next (5 min)**
   - Week 2: Load 8 real controls with evidence
   - Week 3: Pilot audit (hash verification)
   - Weeks 4–6: Full audit
   - Mar 31: Framework operational

**Materials Provided:**
- 1-page "How to Calculate SHA256" quick guide
- SharePoint folder navigator guide
- EVIDENCE_REGISTER_v1.0.xlsx walkthrough (5 min demo)

---

### DAY 5: Week 1 Gate Validation (Go/No-Go Checklist)

#### Pre-Validation Checklist

**Excel Workbook:**
- [ ] All 4 sheets created (CONTROL_MASTER, EVIDENCE_TRACKER, DASHBOARD, AUDIT_EXTRACT)
- [ ] 35 controls imported to CONTROL_MASTER
- [ ] Columns A–U defined & formulas tested
- [ ] Conditional formatting applied
- [ ] Sheet protection applied (formulas locked, data entry columns editable)
- [ ] 3 test controls loaded with dummy data
- [ ] Formulas calculate correctly (dates, status, escalation)
- [ ] Test: Expiry logic works (try past date → Status = EXPIRED)
- [ ] Test: Escalation logic works (High criticality + Not Valid → 🚨 ESCALATE)
- [ ] No Excel errors or circular references

**SharePoint Configuration:**
- [ ] Folder structure created (/EDM, /APO, /BAI, /DSS, /MEA, /CLD, /DEV, /DATA, /BCP, /AI, /API)
- [ ] Year/quarter subfolders created (2026/Q1, Q2, Q3, Q4)
- [ ] Role-based permissions configured (Evidence Owner/Control Owner/Auditor/Admin)
- [ ] Delete permission restricted to Repository Admin only
- [ ] Version history enabled (keep all versions)
- [ ] Retention policy applied (7 years, Compliance Lock)
- [ ] Audit logging enabled & verified (test upload shows in audit log within 24h)

**Integrity Layer:**
- [ ] Column T (Evidence Hash) editable as text
- [ ] Column U (Integrity Status) formula-driven
- [ ] Test: Upload PDF → Calculate SHA256 → Paste to Column T → Status = auto-update
- [ ] Test: Hash verification procedure documented & understood

**Team Readiness:**
- [ ] Evidence Owners trained (5 people)
- [ ] Control Owners trained
- [ ] Auditors trained on hash verification
- [ ] Repository Admin confirmed setup complete

#### Go/No-Go Decision Criteria

**PASS (Go to Week 2):** ✅ All checkboxes completed

**FAIL (Do NOT proceed):** ❌ Any item unchecked
- Identify root cause
- Remediate same day (Friday)
- Retry validation (Friday afternoon)
- If still fails → Extend Week 1 by 1 week

#### Success Metrics for Week 1

| Metric | Target | Status |
|--------|--------|--------|
| Excel workbook functional | 100% formulas working | ✅ PASS or ❌ FAIL |
| SharePoint configured | All permissions correct | ✅ PASS or ❌ FAIL |
| Version history active | Immutable versions | ✅ PASS or ❌ FAIL |
| Hash verification operational | Test hash calculated & verified | ✅ PASS or ❌ FAIL |
| Team trained | All roles understand procedures | ✅ PASS or ❌ FAIL |
| Audit log verified | Events recorded in M365 log | ✅ PASS or ❌ FAIL |

**If ALL PASS → Week 2 Deployment Begins Monday (Feb 23)**

---

## 📅 Week 2 Preview (Next Week)

### Scope: Load 8 High-Criticality Controls

**Controls to Populate with Real Evidence:**

| # | Control ID | Type | Frequency |
|---|-----------|------|-----------|
| 1 | EATGF-EDM-GOV-01 | Governance | Annual |
| 2 | EATGF-EDM-RISK-01 | Governance | Annual |
| 3 | EATGF-APO-SEC-01 | Security | Annual |
| 4 | EATGF-DSS-SEC-01 | Security | Quarterly |
| 5 | EATGF-DSS-ENC-01 | DevSecOps | Annual |
| 6 | EATGF-DSS-INC-01 | DevSecOps | Quarterly |
| 7 | EATGF-AI-LC-01 | AI Governance | Per Release |
| 8 | EATGF-AI-RISK-01 | AI Governance | Quarterly |

**By Friday EOD (Feb 27):**
- All 8 controls have evidence uploaded to SharePoint
- EVIDENCE_REGISTER populated with real data
- Dashboard shows ~70–90% coverage (8 of 35 controls)
- Status outputs match reality (no formula errors)
- Hash verification tested on at least 3 controls

---

## 🚨 Critical Reminders

### Governance Discipline

**Do NOT proceed to Phase 3 until:**
- ✅ Week 3: Pilot audit completed (10 controls)
- ✅ ≥90% compliance score achieved
- ✅ Zero integrity violations detected
- ✅ Management review approved

**Build → Integrate → STRESS-TEST → Then Scale**

The 6-week stabilization plan is not optional. It is how we prove the framework works operationally.

### Evidence Integrity Non-Negotiable

- **No file overwrites** (SharePoint versioning enforces this)
- **No manual hash tampering** (audit verification catches mismatches)
- **No deletion without audit trail** (Purview locks + Audit Log)
- **No exceptions** (auditor will find them)

---

## 📋 Week 1 Daily Standup (Optional but Recommended)

**Each morning (10 min telecon):**

- What completed yesterday?
- Any blockers?
- On track for Friday gate?

**Participants:** Excel Developer, SharePoint Admin, Governance Lead

---

## 📞 Escalation Contacts

**If Issue Found:**

- **Excel Formula Error:** Contact Governance Office + Developer
- **SharePoint Permission Issue:** Contact Repository Admin
- **Hash Calculation Failed:** Contact Repository Admin (validate tool)
- **Gate Validation Fails:** Contact CISO (determine: fix or extend Week 1?)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document** | WEEK_1_EXECUTION_PLAN.md |
| **Version** | 1.0 |
| **Status** | 🟢 **ACTIVE EXECUTION** |
| **Week 1 Dates** | February 16–20, 2026 |
| **Repository** | Microsoft SharePoint (APPROVED) |
| **Integrity Layer** | SHA256 Hash Verification (ACTIVE) |
| **Gate Validation** | Friday, Feb 20 (GO/NO-GO) |
| **Created** | February 13, 2026 |

---

**🚀 WEEK 1 STARTS MONDAY, FEB 16**

No additional planning. Pure execution.

Build the register. Verify integrity. Train the teams. Gate the deliverables.

Then Week 2 begins with real controls, real evidence, real operational testing.

This is how you prove a framework works before scaling it to the world.
