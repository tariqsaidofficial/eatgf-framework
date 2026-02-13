# PHASE_2_STABILIZATION_PLAN.md

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**
Phase 2 Operational Validation – 6-Week Controlled Rollout

---

**Decision:** Phase 2 Architecture = Architecturally Complete  
**Next Action:** Phase 2 Operational Validation (NOT Phase 3 yet)  
**Timeline:** 6 weeks (Feb 13 – Mar 31, 2026)  
**Success Criteria:** Pilot audit passes, framework proven operational

---

## 🎯 Why Stabilize Phase 2 Before Phase 3?

**Risk of proceeding directly to Phase 3:**
- Untested framework deployed widely
- Edition deployment multiplies complexity
- Errors magnified across multiple editions
- Public reference framework built on assumptions

**Correct approach (Engineering discipline):**

```
Build → Integrate → Stress-Test → Then Scale
```

This document is your **stress-test plan**.

---

## 📋 Phase 2 Stabilization Roadmap

### WEEK 1 – Deploy Evidence Register

#### Objective
Build and operationalize the Excel Evidence Register.

#### Deliverables

**By Friday EOD:**

✅ **EVIDENCE_REGISTER_v1.0.xlsx** created
- CONTROL_MASTER sheet (all 35 MCM controls imported, read-only, locked)
- EVIDENCE_TRACKER sheet (formula architecture complete, tested)
- DASHBOARD sheet (KPIs auto-calculating)
- AUDIT_EXTRACT sheet (filtered view template ready)

✅ **Evidence Owners formally assigned**
- Role: Responsible for uploading evidence per frequency
- Training: 30-minute session on upload procedures

✅ **Control Owners formally assigned**
- Role: Responsible for validating evidence completeness
- Training: 30-minute session on validation workflow

✅ **Protection layer enabled**
- Formula columns locked (no manual override)
- Editable columns identified
- Access control enforced

#### Testing (Week 1)

**Test with 3 sample controls:**

| Control | Frequency | Test Scenario |
|---------|-----------|---------------|
| EDM-GOV-01 | Annual | Load evidence dated 01/10/2026, verify status = VALID |
| DSS-SEC-01 | Quarterly | Leave evidence location blank, verify status = MISSING |
| APO-RISK-01 | Semi-Annual | Load old evidence (dated 8/1/2025), verify status = EXPIRED |

**Verification checklist:**
- [ ] Formula logic works for each frequency
- [ ] Status auto-calculates correctly
- [ ] Escalation flags trigger on high-criticality gaps
- [ ] Conditional formatting applies correctly
- [ ] Lock/protection prevents formula modification

#### Week 1 Governance Gate

**Question:** Can the Evidence Register be operationalized?

**Pass criteria:** All tests pass, formulas correct, lock working

**If PASS:** Proceed to Week 2  
**If FAIL:** Debug, fix, re-test (same week)

---

### WEEK 2 – Populate High-Criticality Controls

#### Objective
Load evidence data for tier-1 critical controls to test operational workflow.

#### Load These 8 Controls ONLY

Why these? They're foundational to both ISMS + AIMS, used in Week 3 audit.

| Control | Domain | Frequency | Current Status | Responsible |
|---------|--------|-----------|-----------------|-------------|
| EATGF-EDM-GOV-01 | EDM | Annual | Should exist | General Counsel |
| EATGF-APO-SEC-01 | APO | Annual | Should exist | CISO |
| EATGF-APO-RISK-01 | APO | Annual | Should exist | CISO |
| EATGF-DSS-SEC-01 | DSS | Quarterly | Should exist | Manager, Identity |
| EATGF-DSS-ENC-01 | DSS | Annual | May be incomplete | Manager, Infrastructure |
| EATGF-DSS-INC-01 | DSS | Annual | May be incomplete | Manager, Incident Response |
| EATGF-AI-LC-01 | AI | Per Release | Pending (no models yet) | Chief AI Officer |
| EATGF-AI-RISK-01 | AI | Quarterly | Pending (no models yet) | Data Science Lead |

#### Data Entry Template

For each control, Evidence Owner completes:

```
Control ID: EATGF-DSS-SEC-01
Control Title: [Auto-populated]
Evidence Description: "Q4 2025 IAM Access Review – Signed PDF"
Evidence Location: "https://sharepoint.../evidence/DSS-SEC-01-Q4-2025.pdf"
Last Review Date: 12/15/2025
Audit Cycle: 2026-Q1
```

#### Deliverables

**By Friday EOD:**

✅ All 8 target controls have:
- Evidence Description (clear, specific)
- Evidence Location (working link/path)
- Last Review Date (realistic date)
- Audit Cycle designation

✅ Status columns auto-calculate:
- Expected Most: VALID (7 controls)
- Expected Some: EXPIRING SOON (if quarterly/per-release frequency approaching)
- Expected: MISSING only for AI controls (no models yet – mark as placeholder)

✅ Dashboard reflects:
- 70-90% coverage (8 controls loaded out of 35 total)
- No escalations expected (evidence current)
- Ready for sampling

#### Week 2 Governance Gate

**Question:** Can Evidence Owners enter data correctly?

**Pass criteria:**
- All 8 records complete
- No formula errors
- Status outputs match reality
- Dashboard reflects accurate coverage %

**If PASS:** Proceed to Week 3  
**If FAIL:** Retraining + re-entry (extend Week 2 if needed)

---

### WEEK 3 – Pilot Audit (10 Controls)

#### Objective
Run mini Internal Audit to validate procedures and identify framework gaps.

#### Audit Scope

**8 loaded controls (from Week 2) +**  
**2 additional controls (one MISSING, one EXPIRED intentionally)**

#### Audit Methodology

**Per INTERNAL_AUDIT_PROCEDURE_v1.0.md:**

- **Auditors:** 1 internal + 1 external consultant (to validate)
- **Time:** 4 days (2 days each control group)
- **Criteria:** 
  - Are controls defined as implemented?
  - Is evidence complete & verifiable?
  - Did controls operate as described during period?
  - Are risks mitigated?

#### Pilot Audit Checklist

```
For each of 10 controls:

[ ] Evidence Description clear (not vague)?
[ ] Evidence Location accessible (link works)?
[ ] Evidence dated & signed/verified?
[ ] Evidence format audit-defensible (PDF, not Word)?

Questions for Control Owner:
[ ] How is this control checked? (Monthly? Daily?)
[ ] Who performs it?
[ ] How do you know it's working?
[ ] Any failures or workarounds?

Register validation:
[ ] Status formula output correct?
[ ] Escalation flag accurate?
[ ] Frequency realistic for this control?
[ ] Ownership assignments make sense?

Process feedback:
[ ] Can auditor easily navigate evidence?
[ ] Are XLOOKUP formulas reliable?
[ ] Is conditional formatting helpful or distracting?
[ ] Any formula errors encountered?
```

#### Deliverables

**By Friday EOD:**

✅ **Pilot Audit Report** including:
- Scope (10 controls, test period Jan 15 – Feb 15, 2026)
- Methodology (sampling, interviews, evidence review)
- Findings:
  - **Compliant:** Controls operating as described
  - **Minor Gaps:** Isolated deviations (evidence format, dating)
  - **Process Issues:** Evidence Register workflow problems
- Recommendations for Week 4 hardening

✅ **Evidence Register Feedback:**
- Formula working? (✅/❌)
- Escalation logic triggered correctly? (✅/❌)
- Status outputs match auditor assessment? (✅/❌)
- Ownership clear? (✅/❌)
- Any data entry errors? (✅/❌ + list)

#### Week 3 Governance Gate

**Question:** Does the framework survive pilot audit?

**Pass criteria:**
- Zero critical findings
- ≤3 minor findings
- Audit report formally issued
- No formula logic errors discovered

**If PASS:** Proceed to Week 4 (hardening)  
**If FAIL:** Root-cause analysis → corrective action plan → re-test (extend Week 3)

---

### WEEK 4 – Gap Hardening

#### Objective
Based on pilot audit findings, refine (not restructure) the framework.

#### Refinements Only (No Structural Changes)

**Allowed changes:**
- Evidence format guidance (must be PDF, not Word)
- Frequency adjustment (if unrealistic)
- Ownership clarification (if ambiguous)
- Evidence description examples (for clarity)
- Status automation tweaks (edge cases)

**NOT allowed:**
- Change MCM control definitions
- Alter formula logic fundamentally
- Add new columns or remove columns
- Redefine audit frequency categories

#### Specific Hardening Tasks

**Task 1 – Evidence Format Standard**

```
Current Issue: Mix of PDF, Word, Excel, screenshots

Resolution:
  [ ] Require all evidence as PDF or system export
  [ ] If document: signed PDF (digital or scan)
  [ ] If system: exported report with timestamp
  [ ] Update Evidence Owner training

Document: Update EVIDENCE_REGISTER_MASTER.md § 8
```

**Task 2 – Frequency Validation**

```
Current Issue: Some controls marked "Per Release" with no releases

Resolution:
  [ ] Map each "Per Release" control to actual release schedule
  [ ] If no releases in period: mark as Annual + "awaiting release"
  [ ] Document trigger conditions for per-release audit

Affected Controls:
  • EATGF-AI-LC-01 (awaiting first model deployment)
  • EATGF-.*-REL-01 (if any per-release controls exist)
```

**Task 3 – Ownership Ambiguity**

```
Current Issue: Multiple people unclear on who uploads what

Resolution:
  [ ] For each control: confirm single Evidence Owner
  [ ] For each control: confirm single Control Owner
  [ ] Document escalation path (if Evidence Owner unavailable)

Deliver: EVIDENCE_OWNERSHIP_MATRIX.md (simple lookup table)
```

**Task 4 – Status Automation Edge Cases**

```
Current Issue: Formula doesn't handle [specific edge case]

Resolution:
  [ ] Document edge case (example: "Control frequency = Per Release, no releases yet")
  [ ] Decide: Is status VALID (no release = no audit required) or MISSING?
  [ ] Update formula if decision changes interpretation
  [ ] Add test case to validation protocol
```

#### Deliverables

**By Friday EOD:**

✅ **Updated EVIDENCE_REGISTER_v1.0.xlsx** with:
- Format guidance in column notes
- Frequency confirmed realistic
- Ownership disambiguated
- Status formulas verified

✅ **EVIDENCE_OWNERSHIP_MATRIX.md** created:
- Lists all 35 controls
- Evidence Owner role for each
- Control Owner role for each
- Escalation path if unavailable

✅ **Updated Evidence Owner Training Manual:**
- Evidence format requirements
- Frequency explainer (Monthly vs Quarterly vs Annual)
- Ownership & escalation rules

✅ **Pilot audit defects:** ✅ Closed (all minor items resolved)

#### Week 4 Governance Gate

**Question:** Is framework hardened for full deployment?

**Pass criteria:**
- All pilot audit findings addressed
- No formula errors remaining
- Ownership 100% clear
- Evidence standards documented & trained

**If PASS:** Proceed to Week 5 (full audit)  
**If FAIL:** Additional refinement (extend Week 4)

---

### WEEK 5–6 – Full Internal Audit Cycle

#### Objective
Run complete audit of all 35 MCM controls. Formal governance sign-off.

#### Scope

**All 35 controls** across all 7 domains (EDM, APO, BAI, DSS, MEA, AI, CLOUD)

**Evidence loading:**
- Week 5: Load remaining 27 controls (not from Week 2)
- Week 5: Evidence Owners populate data

**Audit execution:**
- Week 6: Full audit (sampling as per INTERNAL_AUDIT_PROCEDURE_v1.0.md)
- Week 6: Findings documented
- Week 6: Corrective action assigned

#### Audit Output

**Formal deliverables:**

✅ **Audit Report:**
- Scope: All 35 MCM controls, test period Dec 15, 2025 – Feb 28, 2026
- Methodology: Sampling per ISO 19011 (audit procedure)
- Overall maturity rating: [Level 1–5]
- Findings: Categorized by criticality
- Improvement recommendations

✅ **Corrective Action Log:**
- For each finding: root cause, responsible owner, deadline, status
- Linked to Evidence Register via Control ID

✅ **Management Review Documentation:**
- CISO review + sign-off
- Chief AI Officer review + sign-off
- Board-level governance review
- Minutes & decisions documented

✅ **Dashboard Snapshot:**
- % Valid Evidence (target: ≥95%)
- % Overdue Evidence (target: <5%)
- Critical Controls Coverage (target: 100%)
- Domain-by-domain breakdown

#### Week 5–6 Governance Gate

**Question:** Is framework ready for external auditor?

**Pass criteria:**
- Full audit report issued
- Overall compliance ≥90% (high bar for first cycle)
- ≤5 critical findings
- Management review completed
- Corrective action plan in place

**If PASS:** Framework officially operational ✅  
**If FAIL:** Extended corrective action phase (defer Phase 3)

---

## 🎯 DECISION TREE – After Week 6

```
Pilot Audit Results:
  ├─ PASS (90%+ compliance, <5 critical findings)
  │  └─ DECISION: Phase 2 Officially Operational
  │     ✅ Proceed to Phase 3 (Edition Deployment Model)
  │
  └─ FAIL (< 90% compliance, ≥5 critical findings)
     └─ Decision: Extended Stabilization
        ⏸ Pause Phase 3
        🔧 Continue corrective actions
        📅 Restart full audit (4 weeks later)
```

---

## 📊 Success Metrics – Phase 2 Stabilization

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Overall Compliance %** | ≥90% | (VALID / Total) × 100 |
| **Critical Controls 100%** | ≥100% | (High criticality VALID / High total) × 100 |
| **Evidence Completeness** | ≥95% | (Description + Location filled for all loaded) × 100 |
| **Formula Accuracy** | 100% | Status outputs match auditor assessment |
| **Audit Findings** | <5 critical | Per standard severity classification |
| **Corrective Action Closure** | 100% | By assigned deadline |

**If ALL metrics pass → Phase 2 Stabilization = ✅ COMPLETE**

---

## 🚀 After Phase 2 – What's Next?

### If Phase 2 Stabilization Successful:

**Phase 3 – Edition Deployment Model**

- **Startup Edition:** 5–8 foundational controls
- **SaaS Edition:** 18–22 core controls  
- **Enterprise Edition:** All 35 controls

Decision frameworks:
- Which controls mandatory per edition?
- Which controls optional/recommended?
- Deployment playbooks per edition type

### If Phase 2 Stabilization Requires Extension:

**Corrective Action Phase**
- Implement findings
- Re-audit (4-week cycle)
- Then proceed to Phase 3

---

## 📁 Phase 2 Stabilization Artifacts

### Documents to Create/Update

- ✅ **EVIDENCE_REGISTER_v1.0.xlsx** (Week 1)
- ✅ **Pilot Audit Report** (Week 3)
- ✅ **EVIDENCE_OWNERSHIP_MATRIX.md** (Week 4)
- ✅ **Updated Evidence Owner Training** (Week 4)
- ✅ **Full Internal Audit Report** (Week 6)
- ✅ **Corrective Action Log** (Week 6)
- ✅ **Management Review Minutes** (Week 6)

### Documents to NOT Create

- ❌ Phase 3 roadmap (only if Phase 2 passes)
- ❌ Edition-specific control matrices (only after Phase 3 planning)
- ❌ Public reference materials (only after full testing)

---

## 🏁 Phase 2 Stabilization Checklist

### Week 1
- [ ] Excel workbook built (4 sheets)
- [ ] 35 controls imported to CONTROL_MASTER
- [ ] Formula logic verified
- [ ] Protection layer implemented
- [ ] 3 test controls loaded & tested
- [ ] Evidence Owners trained
- [ ] PASS Week 1 governance gate

### Week 2
- [ ] 8 high-criticality controls populated with real evidence
- [ ] Dashboard showing 70-90% initial coverage
- [ ] Status outputs match reality
- [ ] PASS Week 2 governance gate

### Week 3
- [ ] Pilot audit executed (10 controls)
- [ ] Audit report issued
- [ ] Findings documented (<5 minor issues expected)
- [ ] PASS Week 3 governance gate

### Week 4
- [ ] Hardening tasks completed (format, frequency, ownership, formulas)
- [ ] Ownership matrix created
- [ ] Training updated
- [ ] Pilot findings closed
- [ ] PASS Week 4 governance gate

### Week 5–6
- [ ] All 35 controls loaded with evidence data
- [ ] Full audit executed
- [ ] Audit report issued (formal, signed)
- [ ] Management review completed
- [ ] Corrective action log documented
- [ ] PASS Week 5–6 governance gate (final)

### Final Gate
- [ ] All metrics ≥target
- [ ] Phase 2 Stabilization = ✅ COMPLETE
- [ ] Board approval for Phase 3
- [ ] Proceed to Edition Deployment Model

---

## 📞 Phase 2 Stabilization – Roles & Responsibilities

| Role | Responsibility | Phase 2 Involvement |
|------|-----------------|-------------------|
| **Governance Office** | Oversee register & process | Weekly gate reviews, escalation management |
| **Evidence Owners** | Populate evidence data | Upload data per schedule, respond to audit |
| **Control Owners** | Validate evidence & effectiveness | Confirm evidence, validate audit findings |
| **Internal Auditor** | Execute audit procedures | Week 3 pilot + Weeks 5–6 full audit |
| **External Consultant** | Validate framework design | Week 3 pilot observer, recommendations |
| **CISO / CAO** | Executive oversight | Week 5–6 management review sign-off |
| **Board / Steering Committee** | Governance approval | Final gate approval, Phase 3 decision |

---

## 📝 Phase 2 Stabilization Summary

**Duration:** 6 weeks (Feb 13 – Mar 31, 2026)

**Investment:**
- Excel developer: 1 week (build) + 1 week (testing/refinement)
- Governance team: 2 weeks (data entry, gate management)
- Auditors: 1 week (pilot) + 1 week (full audit)
- Management: 5 hours (reviews, sign-offs)

**Reward:**
- Validated, operationally-proven framework
- Risk discovered early (in weeks, not post-deployment)
- Evidence of excellence for external auditors
- Foundation for confident Phase 3 deployment

**Decision point:** Week 6 exit gate determines Phase 3 readiness

---

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | Ready for Execution |
| **Created** | February 13, 2026 |
| **Owner** | Governance Office Program Manager |
| **Timeline** | 6 weeks (Feb 13 – Mar 31, 2026) |
| **Related** | PHASE_2_COMPLETION_SUMMARY.md, INTERNAL_AUDIT_PROCEDURE_v1.0.md |

---

**🔒 Phase 2 Operational Validation – Ready to Execute**

Build → Integrate → Stress-Test → Then Scale

Week 1 deployment begins immediately.
