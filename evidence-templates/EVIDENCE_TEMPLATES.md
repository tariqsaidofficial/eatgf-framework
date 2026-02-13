# EVIDENCE COLLECTION TEMPLATES

**Framework Version:** 1.0  
**Effective Date:** February 2026

---

## EVIDENCE TEMPLATE 1: Policy Implementation

**Use for:** Demonstrate that a policy is active and communicated

**Template Name:** POL-EVIDENCE-001

---

### Policy: Information Security Policy

**Evidence Package Required:**

✅ **E1: Policy Document**
- [Attach] Information Security Policy (signed and dated)
- [Attach] Version history
- [Attach] Approval signatures

✅ **E2: Communication Evidence**
- [Attach] Email announcing policy release
- [Attach] Company announcement / newsletter
- [Attach] Training materials
- [Dates] When each communicated

✅ **E3: Acknowledgment Records**
- [Attach] Policy acknowledgment tracking list
- [Screenshot] LMS enrollment confirmation
- [Count] Total users: ___ / Acknowledged: ___ (% = ___)
- [Status] When completed: ___

✅ **E4: Implementation Status**
- [Checklist] Control implementation status by section
- [Links] Evidence for each implemented control
- [Dates] Implementation timeline

✅ **E5: Monitoring**
- [Attach] First compliance audit report
- [Dates] Audit frequency: [Monthly/Quarterly/Annual]
- [Count] Violations found: ___
- [Actions] Remediation for any violations

---

## EVIDENCE TEMPLATE 2: Control Implementation

**Use for:** Demonstrate that a specific control is operating

**Template Name:** CTL-EVIDENCE-001

---

### Control: SEC-01 (Identity & Access Management)

**Evidence Package Required:**

✅ **E1: Control Design**
- [Attach] Control architecture diagram (showing IAM system)
- [Attach] RBAC policy document
- [Screenshot] IAM system configuration
- [Dates] Control implemented: ___

✅ **E2: User Access Listing**
- [Attach] Current user access list (last 30 days export)
- [Format] Show: User | Role | Access Grant Date | Approver
- [Count] Total users managed: ___
- [Status] All access approved: Yes/No

✅ **E3: Access Review Evidence**
- [Attach] Last quarterly access review (signed)
- [Count] Users reviewed: ___ / Approved: ___ / Revoked: ___
- [Dates] Review date: ___
- [Approver] Signed by: ___

✅ **E4: Multi-Factor Authentication (MFA)**
- [Screenshot] MFA system settings
- [Count] Sensitive systems with MFA: ___
- [Percentage] % of users enrolled: ___
- [Report] MFA usage report (last 30 days)

✅ **E5: Testing/Audit**
- [Attach] Penetration test report (if available)
- [Date] Last security audit: ___
- [Status] Any findings from last audit: Yes/No
- [Actions] Remediation status: ___

✅ **E6: Training Evidence**
- [Attach] IAM training curriculum
- [Count] % of users trained: ___
- [Dates] Training frequency: [Annual/Bi-annual]

---

## EVIDENCE TEMPLATE 3: Key Control Testing

**Use for:** Document that a control is tested and verified working

**Template Name:** TEST-EVIDENCE-001

---

### Test Scenario: Access Control Test

**Test Plan:**

```
Test Name: SEC-01-TEST-001 (Verify IAM properly denies unauthorized access)
Test Date: February 15, 2026
Tester: John Smith (Security team)

Test Steps:
1. Create test user with minimal role
2. Attempt to access protected resource
3. Verify access is denied
4. Grant permission
5. Verify access is now allowed
6. Remove permission
7. Verify access is denied again

Expected Result: Access controlled by role-based permissions

Actual Result: ✅ PASS - All access controls working as designed

Observations:
- MFA challenge appeared as expected
- Audit log captured all activities
- System performance: <1 sec response time

Sign-off:
Tester: John Smith          Date: Feb 15
Reviewer: Jane Doe (Manager) Date: Feb 15
```

---

## EVIDENCE TEMPLATE 4: Vulnerability Assessment

**Use for:** Document security status and patching

**Template Name:** VULN-EVIDENCE-001

---

### Vulnerability Scan Report

**Report Date:** February 2026

✅ **Critical Vulnerabilities**
- Count: 0
- Status: None outstanding
- Average time to patch: N/A

✅ **High Severity**
- Count: 2
- Details:
  - CVE-2026-001: Remote code execution
    - Discovered: Jan 20
    - Patched: Jan 22 (2 days)
    - Status: ✅ Resolved
  
  - CVE-2026-002: SQL injection
    - Discovered: Feb 5
    - Target patch: Feb 12
    - Status: ⏳ In progress (73% patched)

✅ **Medium Severity**
- Count: 8
- Status: All scheduled for patching within 30 days
- % Patched: 50% (4/8)

✅ **Assessment Summary**
```
Scan Tool: Qualys VMDR
Scan Date: Feb 14, 2026
Systems Scanned: 234
Total Vulnerabilities: 10
Critical: 0 (Target: 0) ✅
High: 2 (Target: <3) ✅
Medium: 8 (Target: <20) ✅
Overall Risk: LOW ✅
```

---

## EVIDENCE TEMPLATE 5: Audit Trail / Activity Log

**Use for:** Document that systems log and preserve activity records

**Template Name:** AUDIT-EVIDENCE-001

---

### Activity Log Sample

**System:** Database Access Log  
**Period:** February 1-28, 2026

| Date | User | Action | Resource | Result | Log Record |
|------|------|--------|----------|--------|-----------|
| Feb 3 | user123 | Login | Database | Success | User logged in via MFA |
| Feb 3 | user123 | Query | Customers table | Success | SELECT * executed, 1,250 rows returned |
| Feb 5 | user456 | Login | Database | **FAIL** | Invalid password attempt - account locked |
| Feb 5 | admin1 | Admin | User unlock | Success | user456 unlocked by admin |
| Feb 10 | user789 | Export | Customer data | **BLOCKED** | Export attempt denied - no permission |

**Log Characteristics:**
- ✅ All actions logged automatically
- ✅ Timestamps recorded (accurate to second)
- ✅ User identification captured
- ✅ Action details recorded
- ✅ Results preserved (success/failure)
- ✅ Logs immutable (cannot be edited post-creation)
- ✅ Retention: 7 years (regulatory requirement)

**Sample Audit Query:**
```sql
SELECT timestamp, user, action, resource, result
FROM audit_log
WHERE timestamp >= '2026-02-01'
  AND user != 'system'
ORDER BY timestamp DESC
LIMIT 100;

Result: 4,247 audit records for February
```

---

## EVIDENCE TEMPLATE 6: Training & Competency

**Use for:** Document that team members are trained and competent

**Template Name:** TRAIN-EVIDENCE-001

---

### Governance Training Records

**Training Program:** Enterprise Governance Fundamentals

✅ **Curriculum**
- Module 1: Governance Framework Overview (1 hour)
- Module 2: Controls & Responsibilities (2 hours)
- Module 3: Risk Management (1.5 hours)
- Module 4: Compliance & Audit (1.5 hours)
- Total: 6 hours

✅ **Enrollment & Completion**

| Department | Required | Enrolled | Completed | % |
|-----------|----------|----------|-----------|-----|
| Security | 25 | 25 | 25 | 100% ✅ |
| Compliance | 15 | 15 | 15 | 100% ✅ |
| Engineering | 80 | 80 | 78 | 97.5% ✅ |
| Data | 30 | 30 | 29 | 96.7% ✅ |
| Operations | 50 | 50 | 48 | 96% ✅ |
| **Total** | **200** | **200** | **195** | **97.5%** ✅ |

✅ **Assessment Scores**
- Average score: 88% (Passing = 70%)
- Highest score: 98%
- Lowest score: 72%
- Retakes needed: 0

✅ **Certification**
- AI Governance Specialist Certified: 5 people
- API Security Certified: 3 people
- COBIT Foundation: 12 people

---

## EVIDENCE TEMPLATE 7: Risk Assessment

**Use for:** Document risk identification and mitigation

**Template Name:** RISK-EVIDENCE-001

---

### Risk Assessment Report

**Assessment Period:** Annual 2026  
**Assessment Date:** February 1-28, 2026

✅ **Risk Identification**
- Number of risks identified: 45
- Assessment method: Facilitated workshops (5 sessions)
- Participants: 25 leaders and SMEs
- Documentation: Comprehensive risk register

✅ **Risk Register Entry Example**

```
Risk ID: R-021
Name: Uncontrolled AI System Deployment
Category: Technology/AI Governance
Probability: 3 (Possible)
Impact: 4 (High)
Risk Score: 12 (Medium)
Owner: AI Program Manager

Description:
AI systems deployed without proper governance,
causing compliance violations and performance issues.

Current Controls:
- AI intake process exists
- Architecture review board approves projects
- Risk assessment required

Control Gaps:
- No real-time monitoring of deployed AI systems
- Fairness testing not automated
- No continuous retraining triggers

Mitigation Actions:
1. AI governance framework (DONE - Jan 2026)
2. Fairness monitoring dashboard (In progress - March)
3. Automated retraining system (Q2 2026)

Monitoring KPI:
- % of AI systems in governance framework
- Fairness monitoring coverage
- Automated retraining success rate

Target Risk Score: 6 (by Q3 2026)
Acceptable Residual Risk: Yes
Last Review: Feb 28, 2026
```

✅ **Risk Summary Heat Map**

```
Risk Distribution:
├── Critical (20-25): 1 risk
├── High (15-19): 7 risks
├── Medium (10-14): 18 risks
├── Low (5-9): 15 risks
└── Minimal (1-4): 4 risks

Trends:
- Q4 2025: 3 critical, 12 high
- Q1 2026: 1 critical, 7 high (improving ↓)
- Target: 0 critical, <5 high (by Q3)
```

---

## EVIDENCE TEMPLATE 8: Compliance Certification

**Use for:** Document certification to standards

**Template Name:** CERT-EVIDENCE-001

---

### ISO 27001:2022 Compliance Statement

**Organization:** Enterprise Inc.  
**Scope:** IT Security Management System  
**Assessment Date:** February 2026

✅ **Control Implementation Status**

| ISO 27001 Annex | Control | Status | Evidence |
|-----------------|---------|--------|----------|
| A.5 (Organizational) | A.5.1 | ✅ Designed | Policy signed |
| | A.5.2 | ✅ Designed | Charter approved |
| A.6 (Personnel) | A.6.1 | ✅ Implemented | Training records |
| | A.6.2 | ✅ Implemented | NDA repository |
| A.7 (Asset Mgmt) | A.7.1 | ✅ Implemented | Asset inventory |
| | A.7.2 | ✅ Implemented | Classification schema |
| A.8 (Access Ctrl) | A.8.1 | ✅ Implemented | RBAC system |
| | A.8.2 | ✅ Implemented | IAM audit logs |
| A.9 (Cryptography) | A.9.1 | ✅ Implemented | Encryption policy |
| | A.9.2 | ✅ Implemented | Key management SOP |

✅ **Overall Assessment: COMPLIANT**
- Total controls: 76
- Fully compliant: 72 (94.7%)
- Partially compliant: 4 (5.3%)
- Non-compliant: 0

✅ **Non-Conformities Found:**
1. A.10.1 - Physical security limited to data center
   - Remediation: Building security access controls (Q2 2026)
   
2. A.14.2 - Supplier security assessment not documented
   - Remediation: Assessment process formalized (Q1 2026)
   
3. A.16.1 - Incident response procedures need update
   - Remediation: New procedures drafted (Pending approval)
   
4. A.18.1 - Regulatory changes not captured in compliance calendar
   - Remediation: Calendar system implemented (Done)

✅ **Next Audit:** August 2026

---

## EVIDENCE STORAGE & RETENTION

**Evidence Repository:**
- Location: Compliance SharePoint Site
- Access: Compliance team + auditors
- Format: PDF (for permanence)
- Retention: Minimum 7 years
- Security: Encrypted, access controlled

**Document Naming Convention:**
```
[Category]-[Year]-[Month]-[Description]

Example:
POLICY-2026-02-InfoSecPolicy_Acknowledgment.pdf
CONTROL-2026-02-SEC01_AccessReview.pdf
TEST-2026-02-IAM_AccessDenial_Test.pdf
AUDIT-2026-02-DatabaseAuditLog_Feb2026.csv
RISK-2026-02-RiskAssessment_Annual.xlsx
```

---

## EVIDENCE COLLECTION TIMELINE

| Evidence Type | Collection Frequency | Owner | Timeline |
|--------------|-------------------|-------|----------|
| Policy acknowledgment | Monthly | Compliance | 5th of month |
| Control testing | Quarterly | Control owner | Month 1 of quarter |
| Access reviews | Quarterly | IAM lead | Month 3 of quarter |
| Vulnerability scans | Monthly | Security | 14th of month |
| Audit logs | Continuous | IT Ops | Real-time |
| Risk assessment | Annual | Risk officer | Feb |
| Training records | Monthly | HR | 15th of month |
| Compliance audit | Annual | External auditor | Aug-Sep |

---

**Questions?** Contact: compliance@enterprise.com  
**Evidence Portal:** [Link to SharePoint]
