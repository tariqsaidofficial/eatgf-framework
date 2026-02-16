# Change Approval Standard

| Property           | Value                                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| **Document Type**  | Implementation Standard                                                                        |
| **Version**        | 1.0                                                                                            |
| **Classification** | Governance                                                                                     |
| **Effective Date** | February 16, 2026                                                                              |
| **Authority**      | Chief Technology Officer                                                                       |
| **EATGF Layer**    | 08_DEVELOPER_GOVERNANCE_LAYER / 06_APPLICATION_LIFECYCLE_GOVERNANCE                            |
| **MCM Reference**  | [EATGF-BAI-CHG-01: Controlled Change Management](../../00_FOUNDATION/MASTER_CONTROL_MATRIX.md) |

---

## Purpose

Change control prevents unauthorized, untested, or risky modifications from reaching production. This standard establishes:

- **Change classification** (routine, standard, emergency by risk)
- **Approval authorities** (who must approve each change type)
- **Emergency change procedures** (approval after implementation for critical incidents)
- **Change tracking** (audit trail of all modifications)
- **Communication** (change windows, impact analysis, stakeholder notification)

**Mandatory:** All production changes must be classified and approved per this standard.

---

## Architectural Position

**Upstream Dependencies:**

- Layer 02 Control Architecture [EATGF-BAI-CHG-01: Controlled Change Management]
- Layer 04 GOVERNANCE_CHARTER (change authority roles)
- Layer 08.06 RELEASE_GOVERNANCE_STANDARD (release process uses change approvals)

**Downstream Usage:**

- Layer 06 AUDIT_AND_ASSURANCE (change audit trails)
- Layer 08.06 ROLLBACK_AND_INCIDENT_RESPONSE_STANDARD (change rollback)

**Cross-Layer References:**

- INFRASTRUCTURE_AS_CODE_GOVERNANCE.md (infrastructure change approval)
- MULTI_TENANCY_GOVERNANCE_STANDARD.md (customer-impact changes)

---

## Governance Principles

1. **Risk-Based Approval:** Approval complexity matches change risk
2. **Authority Hierarchy:** Clear decision-maker for each change type
3. **Predictable Windows:** Scheduled changes pre-approved; only emergency changes out-of-window
4. **Stakeholder Awareness:** All impacted parties notified before change
5. **Rollback Readiness:** Before approval, rollback procedure verified

---

## Technical Implementation

### 1. Change Classification

**Change Categories by Risk:**

```
╔════════════════════════════════════════════════════════════════╗
║ CATEGORY A: ROUTINE CHANGES (Low Risk)                         ║
╠════════════════════════════════════════════════════════════════╣
║ Approval: Deploying engineer + team lead (can be async)       ║
║ Window: Any business day (no off-hours restriction)            ║
║ Estimate: Trivial impact; can be rolled back in <5 minutes    ║
║ Notice: 24 hours (internal team only; no customer impact)      ║
║                                                                 ║
║ Examples:                                                       ║
║ - Update npm dependency (dev tool, not production code)         ║
║ - Configuration change (UI text, internal tool setting)         ║
║ - Log level adjustment (debugging, no behavior change)         ║
║ - Deploy to non-production environment (staging, dev)          ║
║ - Documentation update (no code change)                        ║
║ - Monitoring rule addition (observability only)                ║
║                                                                 ║
║ Rollback: Not tested (should be trivial)                       ║
║ Communication: Slack #engineering; no customer notice          ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ CATEGORY B: STANDARD CHANGES (Medium Risk)                     ║
╠════════════════════════════════════════════════════════════════╣
║ Approval: Engineering + Product Manager (sync within 24h)     ║
║ Window: During business hours (8am-5pm local time)             ║
║ Estimate: Limited scope; can be rolled back in <30 minutes    ║
║ Notice: 48 hours (internal + support team aware)               ║
║                                                                 ║
║ Examples:                                                       ║
║ - Production code release (features, bug fixes)                ║
║ - Database schema change (non-breaking)                        ║
║ - New infrastructure resource (additional servers, RDS)        ║
║ - API update (backward-compatible)                            ║
║ - Dependency upgrade (security patch)                          ║
║ - Cache configuration (performance tuning)                     ║
║                                                                 ║
║ Rollback: Tested in staging (72h minimum)                      ║
║ Communication: Release notes sent 24h before                   ║
║ Customer Impact: Possible (features, API changes)              ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ CATEGORY C: MAJOR CHANGES (High Risk)                          ║
╠════════════════════════════════════════════════════════════════╣
║ Approval: CTO + VP Engineering + Customer Success (sync)       ║
║ Window: Scheduled maintenance window (e.g., Sunday 2am UTC)    ║
║ Estimate: Broad impact; may require data migration             ║
║ Notice: 1 week (customers notified of maintenance window)      ║
║                                                                 ║
║ Examples:                                                       ║
║ - Major version release (breaking changes)                     ║
║ - Database migration (major schema redesign)                   ║
║ - Architecture change (multi-region failover, service split)   ║
║ - Third-party integration (payment provider, email service)    ║
║ - SaaS to on-prem migration (data residency change)            ║
║ - Encryption key rotation (full data re-encryption)            ║
║                                                                 ║
║ Rollback: Complex; pre-tested in production-scale environment ║
║ Communication: Customer webinar; dedicated on-call team        ║
║ Stakeholders: Finance (billing impact), Legal (data handling)  ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ CATEGORY D: EMERGENCY CHANGES (Critical Risk / Out-of-Window)  ║
╠════════════════════════════════════════════════════════════════╣
║ Approval: CTO + VP Engineering (can approve after impl.)       ║
║ Window: Any time (no advance notice required)                  ║
║ Timeline: Deploy immediately; brief on-call team               ║
║                                                                 ║
║ Examples:                                                       ║
║ - Critical security vulnerability fix (0-day exploit active)   ║
║ - Data loss incident (database corruption, data deletion)      ║
║ - Service outage (P1 incident, 100% downtime)                  ║
║ - DDoS attack mitigation (emergency rate limiting)             ║
║ - Account breach response (immediate lock-down)                ║
║                                                                 ║
║ Deployed: Now (before approval if absolutely necessary)        ║
║ Approval: Post-implementation (within 2 hours) by CTO          ║
║ Notification: After deployment (customers notified of fix)     ║
║ Post-Mortem: Mandatory within 48 hours                         ║
╚════════════════════════════════════════════════════════════════╝
```

### 2. Change Request & Approval Workflow

**Change Request Ticket Template (Jira/Linear):**

```markdown
## Title

[CATEGORY A/B/C/D] Production Database Migration (PostgreSQL 13 → 15)

## Description

Upgrade PostgreSQL version to 13→15 for performance improvements and security patches.

- Current: PostgreSQL 13.10 (end-of-life Sept 2025)
- Target: PostgreSQL 15.5 (stable; security backports until Oct 2027)
- Benefit: 20-30% query performance improvement (benchmarked)
- Risk: Any query incompatibility (tested in staging)

## Change Classification

**CATEGORY: B (Standard Change)**

- Scope: Database-only; application code unchanged
- Risk: Medium (query incompatibility possible but unlikely; tested)
- Rollback: Database backup available; downtime ~30 min
- Customers: Possible brief latency during upgrade (5-10 sec)

## Approval Requirements

- [ ] Engineering Lead: Code review of migration script
- [ ] Product Manager: Customer impact assessment
- [ ] (Not required: CTO, Finance, Customer Success)

## Schedule

- Change Window: Sat 2026-02-20 2:00-4:00 UTC (off-peak)
- Notice: Sent to customers (48h before)
- Rollback Decision: By Feb 19, 2pm UTC

## Impact Analysis

| Component           | Impact           | Evidence                  |
| ------------------- | ---------------- | ------------------------- |
| API Latency         | +0-5% (expected) | Benchmark vs. v13         |
| Database Downtime   | ~5-10 minutes    | Migration test in staging |
| Query Compatibility | 100% (verified)  | Regression test suite     |

## Rollback Plan

1. Stop application (prevent writes during failover)
2. Restore PostgreSQL from backup (snapshot before upgrade)
3. Verify data integrity (row counts match)
4. Resume application
5. Estimated duration: 30 minutes

Rollback tested in staging: Confirmed successful 

## Approvers (Required for CATEGORY B)

- [ ] Engineering Lead: ********\_******** (date: TBD)
- [ ] Product Manager: ********\_******** (date: TBD)

---

STATUS: Awaiting approvals (submitted 2026-02-16)
```

### 3. Approval Authority Matrix

**Decision Matrix: Who Approves What?**

```
APPROVAL MATRIX:

╔═════════════════════╦═══════════╦═════════════╦═════════════╦══════════╗
║ Change Category     ║ Engineer  ║ Team Lead   ║ Product Mgr ║ CTO/VP   ║
╠═════════════════════╬═══════════╬═════════════╬═════════════╬══════════╣
║ Category A (Routine)║ Approves  ║ Inform only ║ N/A         ║ N/A      ║
║                     ║ (sync)    ║             ║             ║          ║
╠═════════════════════╬═══════════╬═════════════╬═════════════╬══════════╣
║ Category B (Standard)║ Approves ║ Approves    ║ Approves    ║ N/A      ║
║                     ║ (code)    ║ (schedule)  ║ (customer)  ║          ║
╠═════════════════════╬═══════════╬═════════════╬═════════════╬══════════╣
║ Category C (Major)  ║ Approves  ║ Approves    ║ Approves    ║ Approves ║
║                     ║ (code)    ║ (schedule)  ║ (customer)  ║ (risk)   ║
╠═════════════════════╬═══════════╬═════════════╬═════════════╬══════════╣
║ Category D (Emerge) ║ Implements║ Escalates   ║ Observes    ║ Approves ║
║                     ║ NOW       ║ immediately ║ post-deploy ║ post-impl║
╚═════════════════════╩═══════════╩═════════════╩═════════════╩══════════╝

ESCALATION LOGIC:
- If change impacts customer data availability: Product Manager approval required
- If change affects data security: Security Lead review required
- If change requires downtime: CTO approval + Customer Success notification
- If change is out-of-window: CTO emergency approval required
- If change affects compliance (GDPR, SOC 2): DPO/Legal review required
```

### 4. Emergency Change Procedure

**Scenario: P1 Incident Requires Immediate Fix**

```
SITUATION: Production database at 99% disk capacity; service will fail in 2 hours

NORMAL PROCESS (Category B):
├─ Submit change request
├─ Engineering lead reviews (2h)
├─ Product manager reviews (2h)
├─ Schedule change window (24-48h later)
└─ PROBLEM: By then, service may be down 

EMERGENCY CHANGE PROCEDURE (Category D):
├─ T+0: Declare P1 emergency; invoke emergency change protocol
├─ T+5min: CTO notified (can be async; may implement before approval)
├─ T+10min: Issue fix (add disk capacity; stop log accumulation)
├─ T+15min: Monitor; confirm service stable
├─ T+30min: CTO approves post-implementation (mandatory)
│          "Agreed. Emergency fix appropriate. Approved."
├─ T+1h: Send customer notification
│        "Brief service stress detected and mitigated. No action needed."
└─ T+next day: Post-mortem meeting scheduled

POST-MORTEM ANALYSIS (24h later):
1. Why wasn't this caught earlier?
   → Disk monitoring threshold set to 90% (was 95%)
   → Alert was firing but ignored
2. Permanent fix?
   → Automated log cleanup script (daily, keep 7 days only)
   → Alert escalation (page on-call if >90% disk)
3. Prevent similar emergency?
   → Capacity planning review (disk growth trending)
   → Monitoring tuning (reduce mean-time-to-engagement from 2h to 30min)
```

### 5. Change Communication & Notification

**Change Notification Timeline:**

```
CATEGORY A (Routine): 24 hours notice
├─ T-24h: Slack #engineering (team visibility)
├─ T-1h: Confirmation (change still scheduled)
└─ T+30min: Done (announce completion)

CATEGORY B (Standard): 48 hours notice
├─ T-48h: Internal email + Slack (IT team aware)
├─ T-24h: Customer-facing notification (release notes)
├─ T-2h: Reminder (support team standing by)
├─ T-5min: Change window announcement (on-call team ready)
└─ T+30min: Completion announcement (customers can confirm)

CATEGORY C (Major): 1 week notice
├─ T-7d: Customer webinar (Q&A about changes)
├─ T-5d: Migration guide published (step-by-step instructions)
├─ T-2d: Email reminder (set calendar invitation)
├─ T-24h: Customer success calls (confirm readiness)
├─ T-1h: Full team standby (engineering, support, ops)
├─ T+1h: Completion announcement
└─ T+follow-up: Webinar replay available

CATEGORY D (Emergency): Immediate notification
├─ T-during deployment: Technical team aware
├─ T+5min post-deploy: Customer notification (issue + fix)
├─ T+24h: Post-mortem findings published
```

**Customer Notification Template (CATEGORY B):**

```
Subject: [MAINTENANCE] Production Updates - Saturday, Feb 20

Dear Customers,

We're scheduling maintenance on Saturday, Feb 20 from 2:00-4:00 UTC
to upgrade the database and improve performance.

 What's changing: Database engine from v13 to v15
 Expected impact: ~5 minute brief latency (queries may feel slower)
 Customer action required: None (automatic)
 Rollback plan: If issues occur, we'll revert (30 min downtime max)
 Support team: Standing by all weekend

Questions? Reply to this email or visit our status page.

Thank you for your patience.
---
Engineering Team
```

---

## Control Mapping

| EATGF Control        | ISO 27001:2022 | NIST SSDF  | COBIT 2019          | OWASP   |
| -------------------- | -------------- | ---------- | ------------------- | ------- |
| Change Management    | A.8.32, A.6.7  | PW.4, PW.5 | BAI01, BAI07, DSS04 | SAMM SM |
| Change Authorization | A.8.32         | PW.4       | BAI07.05            | SAMM SM |
| Change Communication | A.8.32, A.8.17 | RV.1       | DSS04.01            | SAMM SM |

---

## Developer Checklist

- [ ] Classify change correctly (routine/standard/major/emergency)
- [ ] Identify approval authorities required for this category
- [ ] Submit change request with full description and impact analysis
- [ ] Perform rollback procedure in staging (except routine changes)
- [ ] Identify stakeholders who need notification
- [ ] Schedule change window (or invoke emergency procedure)
- [ ] Obtain all required approvals (documented in ticket)
- [ ] Send customer notification 48h/7d before scheduled change
- [ ] Ensure on-call team briefed on change and rollback procedure
- [ ] Execute change during scheduled window (or immediately for emergencies)
- [ ] Document actual change details (time, approver, rollback decision)
- [ ] For emergencies: conduct post-mortem within 24h; update procedures
- [ ] Archive change ticket for audit trail

---

## Governance Implications

**Risk if not implemented:**

- Unapproved changes reach production without oversight
- No rollback plan → extended downtime on failure
- Customers surprised by changes → support load increases
- Compliance violations (changes not tracked for audits)

**Operational impact:**

- Clear escalation path for urgent fixes
- Product and engineering aligned on customer-impacting changes
- Support team prepared for customer questions

**Audit consequences:**

- Every production change traceable to approval authority
- Change decisions documented and justified
- Compliance auditors verify change control effectiveness

**Cross-team dependencies:**

- **Engineering:** Develop and test change
- **Product:** Assess customer impact
- **Operations:** Execute change; monitor; handle rollback
- **Customer Success:** Notify customers and field questions
- **Executive:** (CTO) Approve major/emergency changes

---

## Official References

- **NIST SP 800-53 CM-3:** Change Control
- **ISO 27001:2022 Annex A.8.32:** Change of information and cryptographic controls
- **COBIT 2019 BAI07:** Manage IT Security
- **ITIL Change Management:** https://www.itil.org/ (change control best practices)

---

## Version History

| Version | Date         | Change Type | Notes                                                                                                                |
| ------- | ------------ | ----------- | -------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Feb 16, 2026 | Major       | Initial release; four-category change classification, approval matrix, emergency procedures, communication timelines |

---

_Last Updated: February 16, 2026_
_EATGF v1.0-Foundation: Change Approval Standard_
