# EVIDENCE_INTEGRITY_AND_REPOSITORY_CONTROL_POLICY.md

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
Evidence Integrity & Repository Control Policy

---

**Document Type:** Operational Policy  
**Authority:** Chief Audit Officer / Governance Office  
**Effective Date:** February 13, 2026  
**Applies To:** All evidence stored in authorization of EATGF controls  
**Compliance:** Supports ISO 27001 Clause 7.5 (Documented Information Control)

---

## 1. Purpose

This policy establishes controls to ensure that evidence of control implementation:

- **Remains unchanged** from date of upload through audit completion
- **Is traceable** to specific evidence owner and timestamp
- **Survives audit challenge** with proof of integrity
- **Meets auditor requirements** for non-repudiation

**Scope:** All evidence uploaded to Evidence Repository in support of MASTER_CONTROL_MATRIX.md controls

---

## 2. Evidence Repository Requirements

### 2.1 Three Mandatory Capabilities

The Evidence Repository (SharePoint, OneDrive, Confluence, Git, or equivalent) MUST provide:

#### Capability 1: Version History (Non-Destructive)

**Requirement:**
- Every file upload creates immutable, timestamped version record
- Previous versions retained indefinitely (minimum 7 years per control)
- No file can be deleted without IT audit trail
- Evidence Owner cannot "overwrite" – only upload new version

**Verification:**
- Repository administrator confirms: "Version history enabled, disabled deletion"
- Test: Upload PDF → Check version history → Previous versions accessible
- Audit trail: All uploads logged with timestamp + user ID

**Examples:**
-  **Microsoft SharePoint:** Version History enabled (default), retention policies set
-  **OneDrive for Business:** Restore previous versions enabled
-  **Confluence:** Page history retained (all edits tracked)
-  **Git:** Immutable commit history (cannot be altered post-sign)
-  **AWS S3:** Versioning enabled, S3 Object Lock for immutability
-  **Shared folder (\\server):** No version history → NOT APPROVED
-  **Email attachment:** No audit trail → NOT APPROVED

---

#### Capability 2: Restricted Write Access (Role-Based)

**Requirement:**
- **Evidence Owners:** Can UPLOAD new evidence, READ own files, cannot DELETE
- **Control Owners:** Can READ all evidence for their control, cannot DELETE
- **Internal Auditors:** Can READ all evidence for audit scope, cannot DELETE
- **Governance Office:** Can READ all, manage folder structure, cannot DELETE evidence files
- **IT/Archive:** Only role that can DELETE (after 7-year retention expires)

**Implementation:**

| Repository | Mechanism |
|-------------|-----------|
| **SharePoint** | Folder permissions: Evidence Owners=Contribute, Control Owners=Read, Auditors=Read, IT=Full Control |
| **OneDrive** | Shared folder with restricted permissions + audit logging |
| **Confluence** | Page restrictions: Contributors can edit own docs, Readers can view only |
| **Git** | Branch protection: Main branch locked, PRs require review, no force-push |
| **AWS S3** | IAM policies: Users have s3:PutObject (upload) but not s3:DeleteObject |

**Verification:**
- Test: Evidence Owner successfully uploads file
- Test: Evidence Owner attempts delete → DENIED (permission error)
- Test: Control Owner attempts delete → DENIED
- Audit trail: Failed delete attempts logged

---

#### Capability 3: Access Logging & Immutable Audit Trail

**Requirement:**
- Every action logged: date, time, user ID, action type (upload, download, delete, modify)
- Logs retained minimum 1 year (longer if evidence retention active)
- Logs themselves immutable (cannot be deleted or modified by regular users)
- Auditable by: Governance Office, Internal Audit, IT compliance

**Implementation:**

| Repository | Audit Trail Feature |
|-------------|-------------------|
| **SharePoint** | Audit Logs (Admin Center) – minimal 90 days |
| **OneDrive** | Microsoft 365 Audit Log – 90 days |
| **Confluence** | Activity Stream + Audit Log (Admin) – 30 days minimum |
| **Git** | Commit log + audit (git log) – indefinite |
| **AWS S3** | CloudTrail logging + S3 access logging |

**Verification:**
- Request: "Provide access log for file [name] from [date range]"
- Audit trail provided to: Governance Office, Chief Audit Officer, Finance (if needed)

---

## 3. Evidence Integrity Controls

### 3.1 Cryptographic Hashing (Optional, Recommended for High-Criticality Controls)

**When to Use:**
- Control: EDM (governance layer)
- Control: DSS-SEC-01, DSS-ENC-01 (access/encryption proof)
- Control: Any control where auditor may challenge file originality

**How It Works:**

Evidence Owner uploads PDF evidence of control compliance.

After upload, Evidence Owner:

1. Downloads file from repository
2. Calculates SHA256 hash:
   - Windows: `certutil -hashfile "C:\path\file.pdf" SHA256`
   - Mac: `shasum -a 256 /path/file.pdf`
   - Online: Use sha256online.com (if document is non-confidential)
3. Copies 64-character hex string
4. Pastes into EVIDENCE_REGISTER Column T (Evidence Hash)

**Hash example:**
```
a3e8c72b9f4b1e6dfc2a9d5e1b3c4f6a8e9d2c5a7b8e9f0d1c2a3b4e5f6a7b
```

**During Audit:**

Auditor retrieves evidence file and repeats hash calculation:
- If hash matches Column T →  File unchanged since upload
- If hash differs →  File modified after upload (investigate)

**Cost:**
- Each file: 30 seconds to calculate + paste hash
- Per audit cycle (35 controls): ~30 minutes total
- Result: Audit defensibility boost

---

### 3.2 Repository-Level Integrity (Built-In)

**What Repository Provides by Default:**

All three major repositories (SharePoint, OneDrive, Git) provide:

| Integrity Feature | How It Protects Evidence |
|------------------|-------------------------|
| **Version History** | All previous uploads preserved – auditor can verify file as-of date X |
| **Timestamp** | Every version marked with creation date + uploading user – proof of originality |
| **Access Logging** | Download/upload attempts recorded – auditor can see who accessed when |
| **Non-Repudiation** | User cannot claim "I didn't upload that" – logs prove they did |

**Example Audit Scenario:**

*Auditor challenge:* "This access control review seems outdated. When was it actually performed?"

*Defense:*
1. Open Evidence Repository
2. Filter version history for evidence file
3. Show: Created 01/15/2026, by [Evidence Owner Name]
4. Show: Access logs confirming no modifications since upload
5. If hash present: Show hash unchanged since upload
6. Conclusion: Evidence is contemporary, unmodified 

---

## 4. Evidence Repository Selection Guidance

### Recommended Repositories (Meet All 3 Requirements)

####  Microsoft SharePoint

**Why:** Enterprise standard, built-in version history, audit logging

**Setup:**
```
Create folder: /sites/governance/Evidence
Subfolder: /2026, /2027, etc. (by year)
Permissions:
  - Evidence Owners: Contribute
  - Control Owners: Read
  - Auditors: Read
  - IT: Full Control
Retention: 7 years (via retention policies)
```

**Cost:** Included in Microsoft 365

---

####  Git (for Development/Cloud Controls)

**Why:** Immutable commits, perfect audit trail, DevOps-native

**Setup:**
```
Repository: governance-evidence
Branch: main (protected, no force-push)
Folder structure:
  /2026/Q1/[Control]/evidence.pdf
  /2026/Q1/[Control]/evidence-hash.txt (optional)
```

**Cost:** Free (GitHub public or private)

---

####  AWS S3 (for Cloud Environments)

**Why:** Enterprise scale, versioning, CloudTrail logging

**Setup:**
```
Bucket: company-governance-evidence
Versioning: Enabled
Server-side encryption: Enabled
Access Logging: Enabled
S3 Object Lock: Optional (immutability enforcement)
```

**Cost:** Minimal (<$1/month for typical volume)

---

###  Acceptable but Limited

#### Confluence Wiki

**Why:** Good for documents, limited version history
-  Version history exists (30-day audit trail)
-  Shorter audit retention than SharePoint
-  Access logging available

**Use when:** Non-critical evidence, policy documents, reference material

**Not suitable for:** Critical evidence, direct control proof

---

###  NOT Approved

#### Email Attachments
-  No version history
-  No access control
-  Limited audit trail
- Risk: File can be "accidentally" replaced, auditor cannot verify originality

#### USB Drives / Local Folders
-  No audit trail
-  No access control
-  Files can be deleted/modified
- Risk: Complete audit trail loss

#### Manual Paper Files
-  No version control
-  Physical tampering risk
-  Acceptable ONLY if encrypted scanned + stored in approved digital repository afterward

---

## 5. Evidence Upload Procedure

### Step-by-Step Process (Evidence Owner)

**Week 2 (Data Population Cycle):**

1. **Prepare evidence:**
   - Ensure document in PDF format (or system export with timestamp)
   - Ensure signed/dated (if document-based)
   - Ensure file name descriptive: "Q1-2026-IAM-AccessReview-SIGNED.pdf"

2. **Calculate evidence hash (optional but recommended for High criticality):**
   ```
   Windows: certutil -hashfile "C:\path\file.pdf" SHA256
   Mac: shasum -a 256 /path/file.pdf
   Copy 64-char string
   ```

3. **Upload to approved repository:**
   - Navigate to: /governance/Evidence/[YEAR]/[MONTH]/
   - Upload file
   - Confirm: Version history shows new entry

4. **Record in EVIDENCE_REGISTER:**
   - Column G (Evidence Description): "Q1 2026 IAM Access Review – Signed PDF"
   - Column H (Evidence Location): URL/path to repository
   - Column I (Last Review Date): "01/15/2026"
   - Column T (Evidence Hash): Paste hash if calculated
   - (Columns J, L, U auto-populate via formulas)

5. **Notify Control Owner:**
   - Send: "Evidence uploaded for [Control ID]"
   - Reference: EVIDENCE_REGISTER row #
   - Action: Control Owner reviews, validates completeness

6. **Confirmation:**
   - Control Owner: "Validated "
   - EVIDENCE_REGISTER Status (Column L): Auto-updates to "VALID"

---

## 6. Evidence Audit & Verification (During Audit Week)

### Auditor Verification Procedure

**Week 3 (Pilot Audit) & Weeks 5–6 (Full Audit):**

1. **Receive EVIDENCE_TRACKER export** from Governance Office

2. **For each control to audit:**

   a) **Check repository for evidence file:**
      - Navigate to folder for that control
      - Confirm file present & accessible
      - Check version history: "Created [date] by [owner name]"

   b) **If Column T has hash:**
      - Download file locally
      - Calculate hash on auditor's machine:
        ```
        Windows: certutil -hashfile "C:\Downloads\file.pdf" SHA256
        Mac: shasum -a 256 ~/Downloads/file.pdf
        ```
      - Compare result to Column T
      - If match:  File integrity confirmed
      - If mismatch:  FILE MODIFIED AFTER UPLOAD → Escalate

   c) **Review evidence quality:**
      - Is evidence clear & legible?
      - Is evidence dated?
      - Is evidence signed/authorized (if required)?
      - Does evidence prove control operation?

   d) **Document findings:**
      - Auditor Notes (Column Q): "Evidence reviewed, confirmed integrity"
      - Status (Column L): Update to "VERIFIED" if audit passed

3. **If evidence integrity issue found:**
   - Escalate to Governance Office immediately
   - Corrective action: Evidence Owner re-uploads unmodified file
   - Root cause investigation: How was file modified?

---

## 7. Roles & Responsibilities

### Evidence Owner (Role)
-  Uploads evidence on schedule
-  Calculates hash if required
-  Verifies evidence file is correct before upload
-  CANNOT delete or overwrite uploaded evidence
-  CANNOT modify evidence after upload (only upload new version)

### Control Owner (Role)
-  Reviews evidence for completeness & quality
-  Confirms control operated as described
-  Signs off on evidence validity
-  CANNOT modify evidence
-  CANNOT delete evidence

### Governance Office (Role)
-  Administers evidence repository
-  Manages folder structure & permissions
-  Monitors upload deadlines
-  Escalates missing/late evidence
-  CANNOT force delete evidence (only IT, after retention window)

### Internal Auditor (Role)
-  Accesses evidence for audit sampling
-  Verifies evidence integrity (hash or repository logs)
-  Documents audit findings
-  Escalates integrity violations
-  CANNOT modify evidence

### IT/Storage Admin (Role)
-  Configures repository (version history, permissions, logging)
-  Maintains backup & disaster recovery
-  Verifies audit logs
-  Deletes evidence ONLY after 7-year retention expires
-  Assists with evidence recovery if needed

---

## 8. Implementation Checklist (Before Week 1)

### Repository Selection (Friday, Feb 13)

- [ ] **Confirm which repository to use:**
  -  SharePoint (recommended)
  -  OneDrive
  -  Git
  -  AWS S3
  -  Confluence (acceptable, limited)

- [ ] **Verify 3 Capabilities:**
  1. [ ] Version History: ENABLED
  2. [ ] Write Restrictions: CONFIGURED (by role)
  3. [ ] Access Logging: ACTIVE

### Repository Setup (Mon–Tue, Feb 16–17)

- [ ] **Folder structure created:**
  ```
  /governance/Evidence/
   ├── 2026/
   │   ├── Q1/
   │   ├── Q2/
   │   ├── Q3/
   │   └── Q4/
  ```

- [ ] **Permissions configured:**
  - [ ] Evidence Owners: Contribute (can upload)
  - [ ] Control Owners: Read-only
  - [ ] Auditors: Read-only
  - [ ] IT: Full control

- [ ] **Audit logging enabled:**
  - [ ] All access logged (date, time, user, action)
  - [ ] Logs retained ≥1 year
  - [ ] Logs not deletable by regular users

- [ ] **Retention policies set:**
  - [ ] Evidence retained minimum 7 years (per EVIDENCE_REGISTER Column S)

### Training (Wed, Feb 17)

- [ ] **Evidence Owners trained:**
  - How to upload evidence
  - How to calculate hash (if applicable)
  - What evidence format is acceptable (PDF preferred)
  - Where to store files (exact folder path)

- [ ] **Control Owners trained:**
  - How to validate evidence
  - Hash verification process (if applicable)
  - Auditor questions to expect

- [ ] **Auditors trained:**
  - How to verify evidence integrity
  - Hash calculation (if applicable)
  - Repository navigation
  - Escalation process if integrity issue found

### Final Verification (Thu, Feb 18)

- [ ] **Repository access test:**
  - Evidence Owner uploads test file 
  - Control Owner downloads & reads file 
  - Auditor accesses file 
  - Check version history present 
  - Check audit logs recorded 

- [ ] **If Phase 2 Stabilization Go-Ahead:**
  - All checks pass → Week 1 deployment ready 

---

## 9. Escalation for Evidence Integrity Issues

### If File Hash Mismatch Detected (During Audit)

**Severity:** CRITICAL (potential audit failure)

**Response:**

1. **Auditor:** Report immediately to Chief Audit Officer
2. **Chief Audit Officer:** Notify Governance Office
3. **Governance Office:** Contact Evidence Owner
4. **Investigation:**
   - When was file modified?
   - By whom?
   - Why was it modified?
   - Is modification authorized?
   - Should evidence be accepted or rejected?
5. **Corrective Action:**
   - If authorized modification: Document rationale
   - If unauthorized: Evidence rejected, new evidence required
   - Add corrective action to audit log

**Prevention:**
- More frequent auditing of this control
- Tighter repository access restrictions
- Hash verification mandatory for future cycles

---

### If Evidence File Deleted/Missing (During Audit)

**Severity:** CRITICAL (evidence unavailable for audit)

**Response:**

1. **Auditor:** Check repository version history
   - Can file be restored from version history? 
   - If yes: Restore file, audit proceeds
   - If no: Escalate immediately

2. **Governance Office:** Investigate deletion
   - Who deleted file?
   - When?
   - Authorization?
   - IT recovery possible?

3. **Corrective Action:**
   - Audit finding: "Evidence integrity control failure"
   - Remediation: Repository access restrictions tightened
   - Deadline: Implement within 30 days
   - Follow-up audit: Verify controls re-implemented

---

## 10. Compliance with ISO Standards

### ISO 27001 Clause 7.5 – Documented Information Control

This policy implements:

-  A.7.5 – "Ensure documented information is adequately protected"
-  Controlled storage (version history, immutability)
-  Controlled access (role-based permissions)
-  Evidence of implementation (audit trails)

### ISO 19011 – Evidence Requirements

This policy ensures:

-  Evidence is retained for audit evaluation
-  Evidence integrity can be verified
-  Evidence chain of custody documented
-  Auditor can challenge evidence authenticity

---

## 11. Retention & Archival

### 7-Year Retention Enforcement

- **Retention Period:** 7 years from Last Review Date (per Column S)
- **Archival Process:** After 7-year window:
  1. IT backup evidence to long-term storage
  2. Delete from active repository
  3. Document archival in Evidence Register
  4. Provide archived link if auditor requests after period ends

- **Exception:** If evidence related to unresolved finding, retain until finding closed + 1 year

---

## 12. Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | Effective Immediately (Feb 13, 2026) |
| **Authority** | Chief Audit Officer / Governance Office |
| **Applies To** | All evidence supporting EATGF MCM controls |
| **Review Date** | August 13, 2026 (6 months) |
| **Next Update** | Post-Phase 2 Stabilization assessment |

---

** Evidence Integrity is Foundation of Audit Defensibility**

Repository locks the evidence.  
Hashing proves authenticity.  
Logs prove non-repudiation.

Together: Auditor confidence.

---

## Appendix A: Repository Verification Checklist

### Before Week 1 Launch (Use This to Verify Your Repository)

```
REPOSITORY: [Name SharePoint / OneDrive / Git / AWS S3 / Other]

CAPABILITY 1 – VERSION HISTORY:
  [ ] Previous versions retained (not overwritten)
  [ ] Timestamp on each version
  [ ] User attribution on each version
  [ ] Test: Upload file → Modify → Check history → See both versions? YES/NO

CAPABILITY 2 – RESTRICTED WRITE:
  [ ] Evidence Owner can UPLOAD: YES/NO
  [ ] Evidence Owner cannot DELETE: YES/NO
  [ ] Control Owner can READ only: YES/NO
  [ ] Auditor can READ only: YES/NO
  [ ] Test: Non-owner attempts delete → DENIED? YES/NO

CAPABILITY 3 – ACCESS LOGGING:
  [ ] Upload events logged: YES/NO
  [ ] Download events logged: YES/NO
  [ ] Delete attempts logged: YES/NO
  [ ] Reports accessible to Governance Office: YES/NO
  [ ] Logs retained ≥1 year: YES/NO
  [ ] Test: Request access log for file → Provided? YES/NO

DECISION:
  [ ] ALL 3 CAPABILITIES CONFIRMED → READY FOR WEEK 1 
  [ ] ANY CAPABILITY MISSING → CANNOT START (must remediate first) 
```

---

**By signing this policy, organization confirms:**

Evidence Repository meets all 3 integrity requirements.  
Evidence Owners trained on upload procedures.  
Evidence integrity protection operational.  

**Approvers:**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Chief Audit Officer | __________ | Feb 13, 2026 | __________ |
| Governance Office | __________ | Feb 13, 2026 | __________ |
| IT/Repository Admin | __________ | Feb 13, 2026 | __________ |

---

**Phase 2 Stabilization Week 1 is GO.**
