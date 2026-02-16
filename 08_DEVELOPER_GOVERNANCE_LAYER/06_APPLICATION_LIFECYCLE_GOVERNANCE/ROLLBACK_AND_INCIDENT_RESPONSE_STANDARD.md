# Rollback and Incident Response Standard

| Property           | Value                                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| **Document Type**  | Implementation Standard                                                                        |
| **Version**        | 1.0                                                                                            |
| **Classification** | Governance                                                                                     |
| **Effective Date** | February 16, 2026                                                                              |
| **Authority**      | Vice President of Engineering                                                                  |
| **EATGF Layer**    | 08_DEVELOPER_GOVERNANCE_LAYER / 06_APPLICATION_LIFECYCLE_GOVERNANCE                            |
| **MCM Reference**  | [EATGF-DSS-INC-01: Incident Response Management](../../00_FOUNDATION/MASTER_CONTROL_MATRIX.md) |

---

## Purpose

Production failures happen. Rapid recovery minimizes customer impact. This standard ensures:

- **Fast rollback** (revert to last known-good state in <10 minutes)
- **Clear decision criteria** (when to rollback vs. forward-fix)
- **Incident classification** (by severity and impact)
- **On-call procedures** (escalation, communication, post-mortems)
- **Recovery tracking** (metrics to improve over time)

**Mandatory:** All production changes must have rollback procedures tested before deployment. All incidents must be documented with root cause analysis.

---

## Architectural Position

**Upstream Dependencies:**

- Layer 02 Control Architecture [EATGF-DSS-INC-01: Incident Response Management]
- Layer 04 INCIDENT_RESPONSE_POLICY (incident severity definition)
- Layer 08.06 RELEASE_GOVERNANCE_STANDARD (releases have rollback plans)

**Downstream Usage:**

- Layer 06 AUDIT_AND_ASSURANCE (incident metrics and trends)

**Cross-Layer References:**

- 04_INCIDENT_RESPONSE_POLICY.md (incident severity P1-P4)
- MONITORING_AND_OBSERVABILITY_STANDARD.md (alerting thresholds)

---

## Governance Principles

1. **Speed Over Perfection:** Rollback to restore service; root-cause analysis happens after
2. **Decision Clarity:** Explicit criteria for rollback vs. forward fix
3. **Automation First:** Pre-tested rollback scripts run with one command
4. **Transparency:** Every customer-impacting incident documented
5. **Continuous Improvement:** Post-mortem findings prevent recurrence

---

## Technical Implementation

### 1. Incident Severity & Escalation

**Incident Classification:**

```
P1 CRITICAL (≤1 hour SLA)
├─ Definition: Total service outage OR data loss/corruption
├─ Examples:
│  - Database completely unavailable (100% request failure)
│  - Data corrupted or deleted (customer data lost)
│  - Security breach (customer data exposed)
├─ Alert: Page on-call VP Engineering immediately
├─ Response: All hands on deck; pause other work
├─ Communication: Customer notification within 30 min
└─ Decision: Rollback or forward fix within 60 min

P2 HIGH (≤4 hour SLA)
├─ Definition: Partial service degradation OR feature broken
├─ Examples:
│  - API latency >5 seconds (some requests failing)
│  - Payment transactions failing (10% error rate)
│  - Reporting feature broken (critical for customers)
├─ Alert: Page on-call Engineering Lead
├─ Response: Focused incident team (3-5 engineers)
├─ Communication: Customer notification within 2 hours
└─ Decision: Rollback or forward fix within 4 hours

P3 MEDIUM (≤8 hour SLA)
├─ Definition: Non-critical feature or performance issue
├─ Examples:
│  - API latency 2-5 seconds (no errors, just slow)
│  - Non-critical feature broken (UI glitch, minor data)
│  - Memory leak (performance degrades over hours)
├─ Alert: Slack notification to #incidents
├─ Response: Secondary on-call engineer
├─ Communication: Customer notified within 4 hours
└─ Decision: Forward fix or rollback (24-hour window)

P4 LOW (≤24 hour SLA)
├─ Definition: Cosmetic or internal-only issue
├─ Examples:
│  - UI typo (incorrect wording)
│  - Log message error (not customer-visible)
│  - Monitoring metric incorrect (doesn't affect decisions)
├─ Alert: Jira ticket created
├─ Response: Fix in next sprint
└─ Decision: Fix or defer (no rollback needed)
```

### 2. Rollback Procedure: Pre-Deployment Testing

**Before Any Release: Verify Rollback Works**

```
RELEASE PROCEDURE:

Phase 1: Development & Staging
├─ Code developed and tested in staging
├─ All CI/CD gates passing

Phase 2: Pre-Deployment Testing (MANDATORY)
├─ T-48h before production deploy
├─ Deploy to staging (simulate production)
├─ Run production traffic for 72 hours
├─ Measure: Performance, errors, data consistency
├─ Decision point: Proceed or delay release?

Phase 3: Rollback Test (MANDATORY)
├─ With staging data/traffic active:
│  ├─ Trigger: Simulated customer request fails
│  ├─ Decision: Rollback (don't try forward fix)
│  ├─ Execute: Run rollback script
│  ├─ Measure: Time to revert to previous version
│  ├─ Verify: Data integrity, previous version stable
│  └─ Success criterion: <5 min rollback, zero data loss
├─ If rollback fails: Fix issues before deploying to production
├─ If rollback succeeds: Proceed to production deploy

Phase 4: Production Deploy
├─ Execute release (code deployed)
├─ Automated health checks run
├─ Monitoring dashboards establish baseline metrics
└─ On-call team standing by

Phase 5: Monitoring & Decision Point
├─ If no errors within 30 minutes: Release successful ✓
├─ If errors detected:
│  ├─ 30-min critical decision: Rollback or forward fix?
│  ├─ Rollback decision: Run pre-tested rollback script
│  ├─ Forward fix decision: Deploy hotfix (if simple)
│  └─ Timeout: If no decision by 30 min, rollback automatic
```

### 3. Rollback Decision Matrix

**When to Rollback vs. Forward Fix:**

```
DECISION TREE:

Is the issue CRITICAL (P1)?
├─ YES: ROLLBACK (don't debug; restore service first)
└─ NO: Continue

Is the issue a DATA LOSS or CORRUPTION incident?
├─ YES: ROLLBACK (prevent further data damage)
└─ NO: Continue

Is the issue in the DEPLOYMENT?
├─ YES: Is the deployment simple to revert?
│  ├─ Simple (.jar swap, config change): ROLLBACK
│  └─ Complex (schema change): Continue below
└─ NO: Continue

Is the issue in the DATABASE MIGRATION?
├─ YES: Can you restore from pre-migration backup?
│  ├─ YES, <30 min: ROLLBACK
│  └─ NO, >30 min: FORWARD FIX (restore data + patched code)
└─ NO: Continue

Can the fix be deployed in <30 min?
├─ YES: FORWARD FIX
│  - Hotfix already coded
│  - Hot reload available (no downtime)
│  - Changes are simple/safe
└─ NO: ROLLBACK

Final Decision:
├─ ROLLBACK: Use pre-tested rollback script
├─ FORWARD FIX: Deploy hotfix with priority
└─ HYBRID: Rollback infra + deploy patch simultaneously
```

### 4. Automated Rollback Scripts

**Rollback Implementation: Example (API Release)**

```bash
#!/bin/bash
# rollback-api-v1.3.0.sh
# Automated rollback from v1.3.0 → v1.2.3

set -e  # Exit on any error
LOG_FILE="/var/log/rollback-$(date +%s).log"

log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

CURRENT_VERSION="1.3.0"
TARGET_VERSION="1.2.3"
START_TIME=$(date +%s)

log "=== ROLLBACK INITIATED: $CURRENT_VERSION → $TARGET_VERSION ==="

# Step 1: Verify pre-deployment backup exists
log "Verifying database backup..."
if ! aws s3 ls s3://backups/api-db/pre-deploy-1.3.0/ > /dev/null; then
  log "ERROR: Pre-deployment backup not found!"
  exit 1
fi
log "✓ Backup verified"

# Step 2: Stop accepting new requests
log "Draining connections..."
kubectl patch deployment api --patch '{"spec":{"replicas":0}}'
sleep 10  # Allow in-flight requests to complete
log "✓ New requests stopped"

# Step 3: Database rollback (schema changes)
log "Rolling back database schema..."
# Pre-compiled downgrade SQL script (tested in staging)
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" \
  -f "/home/app/migrations/rollback-1.3.0.sql" \
  2>&1 | tee -a "$LOG_FILE"
log "✓ Database schema reverted"

# Step 4: Application rollback
log "Redeploying application v$TARGET_VERSION..."
docker pull registry.internal/api:v$TARGET_VERSION  # Pre-built image
kubectl set image deployment/api "api=registry.internal/api:v$TARGET_VERSION" \
  --record --rollout=history
kubectl wait --for=condition=available \
  --timeout=300s deployment/api
log "✓ Application container running"

# Step 5: Health check
log "Running health checks..."
for i in {1..5}; do
  if curl -f http://localhost:8080/health > /dev/null; then
    log "✓ Health check passed (attempt $i)"
    break
  else
    log "Health check failed (attempt $i); waiting..."
    sleep 5
  fi
done

# Step 6: Resume traffic
log "Re-enabling requests..."
kubectl patch deployment api --patch '{"spec":{"replicas":3}}'
kubectl wait --for=condition=ready pod -l app=api --timeout=60s
log "✓ Requests resumed"

# Step 7: Verification
log "Verifying rollback..."
V_CURRENT=$(curl -s http://localhost:8080/version | jq -r '.version')
if [[ "$V_CURRENT" == "$TARGET_VERSION" ]]; then
  log "✓ Application version verified: $V_CURRENT"
else
  log "ERROR: Version mismatch. Expected $TARGET_VERSION, got $V_CURRENT"
  exit 1
fi

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

log "=== ROLLBACK SUCCESSFUL ==="
log "Duration: ${DURATION}s"
log "Previous version: $CURRENT_VERSION"
log "Current version: $V_CURRENT"
log "Status: READY FOR TRAFFIC"
log "Action: Customer notification required within 30 min"
log "---"
echo "$LOG_FILE"  # Output log file path for incident tracking
```

**Verification:**

- Tested in staging: ✓ (72h before production)
- Manual run time: <5 min
- Automated trigger: On error detection (P1 incidents)
- Success rate: 100% (tested pre-release)

### 5. Incident Response & Post-Mortem

**P1 Incident Timeline:**

```
T+0min: Issue Detected
├─ Alert fired (API error rate >5%)
├─ On-call VP Engineering paged immediately
└─ Slack #incident created

T+2min: Incident Declared
├─ P1 incident status declared
├─ All hands called (engineering, product, ops)
├─ Customer success notified (prepare for calls)
├─ Incident commander assigned (VP Eng)
└─ Dedicated Slack channel #p1-incident-feb16

T+5min: Initial Response
├─ VS Code opened; code deployed in prod 30 min ago reviewed
├─ Recent changes identified (v1.3.0 release 30 min ago)
├─ Hypothesis: Release caused issue (high probability)
├─ Decision: ROLLBACK to v1.2.3
└─ Rollback script triggered

T+10min: Rollback Complete
├─ Application reverted to v1.2.3
├─ Health checks passing ✓
├─ Error rate dropped to 0.1% (normal) ✓
├─ Incident severity: RESOLVED (technically)
└─ Status: Service restored; investigation continues

T+12min: Customer Notification
├─ Customer success sends email:
│  "Experienced brief service disruption due to deployment issue.
│   Issue resolved; service fully restored. Apologies for inconvenience."
├─ Status page updated: "Incident resolved"
└─ Customers can verify service is back

T+30min: Incident Post-Mortem Meeting
├─ Attendees: VP Eng, Release Engineer, Product, On-call
├─ Question 1: What specifically failed in v1.3.0?
│  └─ Answer: New database query had N+1 problem (loads in loop)
│          → Caused 100x more queries → database connection exhaustion
├─ Question 2: Why didn't staging catch this?
│  └─ Answer: Staging traffic volume was too low
│          →Traffic pattern issue not reproduced in test
├─ Question 3: How do we prevent this?
│  └─ Action items created (see below)
└─ Duration: ~30 min

T+2h: Detailed RCA Begins
├─ Release engineer analyzes v1.3.0 code changes
├─ Finds: New ORM query in dashboards feature
├─ Issue: .forEach(item → database.load(item)) (N+1 query)
├─ Expected: 100 items, 1 query (bulk load)
├─ Actual: 100 items, 100 individual queries
├─ Impact: Database connection pool exhaustion after ~5 min of traffic
└─ Fix: One-line change (use bulk_load instead of loop)

T+next day: Action Items
1. IMMEDIATE (Fix forward):
   ├─ Deploy v1.3.1 with N+1 query fix
   └─ Code review: Add database query count assertion to integration tests

2. SHORT-TERM (1 week):
   ├─ Add database connection pool monitoring (alert if ≥80%)
   ├─ Add high database query volume detection
   └─ Increase staging load test traffic (simulate production load)

3. MEDIUM-TERM (1 month):
   ├─ Implement automatic query logging (N+1 detection)
   ├─ Enforce database query budgets per endpoint (max queries)
   └─ Training: ORM best practices (batch loading, eager loading)

4. POST-MORTEM REPORT:
   ├─ Title: API v1.3.0 Deployment Incident (Feb 16, 2026)
   ├─ Impact: 10-minute service degradation
   ├─ Root Cause: N+1 database query pattern in dashboard feature
   ├─ Detection: 5 minutes (monitoring alert)
   ├─ Response: 10 minutes (rollback)
   ├─ Recovery: 10 minutes (verification + customer notification)
   ├─ Severity: P1 (resolved in 20 min)
   └─ Prevention: 4 action items tracked in Jira
```

### 6. Metrics & Continuous Improvement

**Incident Metrics (Monthly):**

```
January 2026 Incident Summary:
├─ P1 Incidents: 1 (v1.3.0 N+1 query issue)
├─ P2 Incidents: 3 (API timeouts, slow reports, data sync lag)
├─ P3 Incidents: 8 (UI glitches, missing features)
├─ P4 Incidents: 15 (typos, log messages)
├─ Total MTTR (mean time to resolve): 25 min
├─ Total MTTD (mean time to detect): 8 min
├─ Rollback count: 1 (v1.3.0 required rollback)
├─ Rollback success rate: 100% (1/1 successful)
└─ Rollback time (average): 4.2 min

TRENDS (Last 3 Months):
├─ P1 incidents: 3 → 2 → 1 ✓ (improving)
├─ MTTR: 35min → 28min → 25min ✓ (improving)
├─ Detection → Resolution: 30min → 20min → 20min (stable)
├─ Action items from post-mortems: 12 → 10 → 8 (backlog shrinking) ✓
└─ Production releases: 12 → 14 → 16 (increasing velocity safely)

GOAL: Zero P1 incidents; <10 min MTTR for P2
```

---

## Control Mapping

| EATGF Control       | ISO 27001:2022         | NIST SSDF      | COBIT 2019   | OWASP   |
| ------------------- | ---------------------- | -------------- | ------------ | ------- |
| Incident Response   | A.5.26, A.6.10, A.16.1 | PO.1.2, PO.3.2 | DSS06, MEA01 | SAMM IM |
| Business Continuity | A.8.36, A.8.37         | N/A            | BAI04.05     | SAMM IM |
| Change Recovery     | A.8.32                 | PW.5           | BAI07        | SAMM IM |
| Metrics & Reporting | A.8.17, A.6.7          | N/A            | MEA01        | SAMM IM |

---

## Developer Checklist

- [ ] Understand incident severity levels (P1-P4) and escalation procedures
- [ ] Pre-deployment: Verify rollback procedure in staging environment
- [ ] Pre-deployment: Run rollback script; confirm success (<5 min, zero data loss)
- [ ] Production deployment: Have rollback script available; one-command execution
- [ ] During incident: Know decision criteria (rollback vs forward fix)
- [ ] After rollback: Participate in root-cause analysis meeting
- [ ] After incident: Help implement action items from post-mortem
- [ ] Monitoring: Set up alerts for P1/P2 incident detection
- [ ] On-call: Understand escalation and communication procedures
- [ ] Metrics: Track MTTR, MTTD, and improvement trends monthly

---

## Governance Implications

**Risk if not implemented:**

- Long incident recovery times; customers frustrated
- No rollback procedure → extended outages
- Repeated incidents; same root causes not fixed
- Compliance violations (incidents not documented)

**Operational impact:**

- Rapid recovery minimizes customer impact
- On-call team clear on procedures; less chaos
- Post-mortems drive continuous improvement
- Metrics guide investment in monitoring/automation

**Audit consequences:**

- External auditors verify incident response procedures
- Post-mortems demonstrate root-cause analysis discipline
- Rollback readiness verifiable through testing records
- Incident metrics show maturity and improvement

**Cross-team dependencies:**

- **Engineering:** Develop rollback scripts; participate in post-mortems
- **Operations:** Execute rollback; monitor during incidents
- **Product:** Communicate with customers; product decisions from incidents
- **Customer Success:** Manage customer communication; gather feedback from incidents
- **Executive:** P1 incidents escalated; board-level decisions may be needed

---

## Official References

- **NIST SP 800-34:** Contingency Planning Guide
- **ISO 27001:2022 Annex A.5.26-27:** Incident management
- **NIST SSDF PO.1.2:** Establish and maintain a plan for incident handling
- **COBIT 2019 DSS06:** Manage IT incident and security events

---

## Version History

| Version | Date         | Change Type | Notes                                                                                                                  |
| ------- | ------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Feb 16, 2026 | Major       | Initial release; incident severity P1-P4, automated rollback scripts, decision matrix, post-mortem procedures, metrics |

---

_Last Updated: February 16, 2026_
_EATGF v1.0-Foundation: Rollback and Incident Response Standard_
