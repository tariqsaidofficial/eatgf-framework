# Application Lifecycle Governance Standard

**Version:** 2.0-COMPREHENSIVE
**Status:** Active
**Authority:** EATGF Layer 08 (Developer Governance) - Domain 06
**Effective Date:** 2026-02-15
**Classification:** Internal - Governance & Operations

---

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / Domain 06_APPLICATION_LIFECYCLE_GOVERNANCE

**Document Authority:** Implements BAI and DSS domain controls related to application release, change management, and incident response:

- EATGF-BAI-REL-01: Release Management & Change Approval
- EATGF-DSS-INC-01: Incident Response & Rollback Procedures
- EATGF-DSS-EOL-01: Application End-of-Life Governance
- EATGF-DSS-OPS-01: Production Operations & Monitoring

**Relationship to EATGF:** Derivative document - operationalizes BAI/DSS controls with implementation standards for safe, auditable application lifecycle management.

---

## Governance Principles

1. **Changeability with Safety** -- All production changes follow approval gates; emergency patches documented post-incident with audit trail intact
2. **Rollback Capability** -- Every deployment maintains rollback capability; tested quarterly and documented in runbooks
3. **Observability by Default** -- All changes logged in centralized system (Git, deployment platform, monitoring); searchable audit trail persists 12 months
4. **Incident Transparency** -- Incidents classified, root causes documented, postmortems blameless; metrics tracked (MTTR, resolution rate)
5. **End-of-Life Clarity** -- Applications reach EOL with defined timeline (90-day notice); data retention policy per control; no orphaned systems
6. **Cross-Functional Alignment** -- Release decisions include security, operations, and business perspectives; no unilateral deployment decisions

---

## Control 1: Release Management & Change Approval (EATGF-BAI-REL-01)

### Purpose

Organization establishes formal release process with approval gates, preventing unauthorized or untested changes from reaching production, while enabling rapid, safe deployments.

### Release Classification

**Three-Tier Release Models:**

```
Tier 1: Hotfix (Emergency Patches)
├─ Trigger: Security vulnerability, data corruption, production outage
├─ Approval: CEO (or designated emergency authority) + Security + Ops Lead
├─ Timeline: 30min approval, documentation post-deployment
├─ Testing: Hotspot testing only (no full regression)
└─ Post-Incident: RCA within 24hrs; controls review 72hrs post-deployment

Tier 2: Minor Release (Bug fixes, patches, config changes)
├─ Trigger: Scheduled maintenance, non-critical bugfixes
├─ Approval: Product Lead + Tech Lead + Security + Ops
├─ Timeline: 2-week release cycle (first/third Monday of month)
├─ Testing: Full QA, smoke tests passing, 48hrs in staging
└─ Change Advisory Board (CAB) review required

Tier 3: Major Release (Features, architecture changes)
├─ Trigger: New features, infrastructure upgrades, frameworks
├─ Approval: Executive sponsor + Architects + Full CAB + Security
├─ Timeline: 4-week planning, 2-week staging, 1-week post-deployment support
├─ Testing: Full regression, load testing, security scan pass
└─ Feature flag deployment recommended (dark launch)
```

### Release Gates (Non-Waivable)

| Gate               | Stage  | Check                             | Owner           | Failure Action |
| ------------------ | ------ | --------------------------------- | --------------- | -------------- |
| **Code Quality**   | Build  | SonarQube score >80%              | Dev Lead        | BLOCK          |
| **Security Scan**  | Build  | SAST/DAST pass; no critical vulns | Security        | BLOCK          |
| **Test Coverage**  | Build  | >80% code coverage                | QA              | BLOCK          |
| **Staging Deploy** | Test   | App health checks pass (5min)     | DevOps          | BLOCK          |
| **Smoke Tests**    | Test   | Core workflows validated          | QA              | BLOCK          |
| **Performance**    | Test   | p99 latency <200ms; no regression | Ops             | BLOCK          |
| **Approval**       | Deploy | CAB signed off                    | Release Manager | BLOCK          |
| **Backup**         | Deploy | Pre-production backup completed   | DevOps          | BLOCK          |

**Zero Waivers Policy:** No gates can be bypassed except by emergency executive authorization (logged immediately).

### Change Approval Board (CAB) Process

**Quarterly Membership:**

- Product Manager (chairs)
- Tech Lead / Architect
- Security Officer
- Operations Lead
- Customer Success (for SaaS)

**Meeting Cadence:** Weekly (30min)

**Agenda:**

1. Proposed releases (5 min review)
2. Roll-out schedule (staging → production)
3. Rollback procedures (documented & tested)
4. Known risks & mitigation
5. Post-deployment support plan

**Documentation Requirements:**

- Release notes (features, bugfixes, security updates)
- Known issues (bugs still present, planned for future release)
- Rollback procedure (steps, estimated time, validation tests)
- Support runbook (troubleshooting, escalation)

### Deployment Process

**Pre-Deployment (Staging):**

```
1. Deploy to staging environment (identical prod config)
2. Run full regression test suite (automated)
3. Execute smoke tests (manual critical paths)
4. Performance validation (load test, latency < 200ms p99)
5. Security validation (no new vulnerabilities, OWASP pass)
6. Backup production database (point-in-time)
7. Notify on-call team (pagerduty alert)
8. Get CAB sign-off (async approval or meeting consensus)
```

**Deployment (Production):**

```
1. Blue-green deployment (new version in parallel)
2. Health checks passing (5 min timeout; rollback if fail)
3. Gradual traffic shift (5% → 25% → 50% → 100% over 15 min)
4. Monitor error rates (alert if >0.5% deviation)
5. Complete traffic shift OR immediate rollback
6. Sign-off by Ops Lead
```

**Post-Deployment (48 hours):**

```
1. Monitor metrics (error rates, latency, CPU, memory)
2. Alert on any anomalies (auto-rollback if >5% error spike)
3. Customer feedback review (support tickets, user reports)
4. Release sign-off document completed
5. Post-deployment support team on standby (phone/slack accessible)
```

### Evidence Checklist

- [ ] Release classification documented (Tier 1/2/3)
- [ ] All release gates passing (quality, security, tests, approval)
- [ ] CAB approval documented and signed
- [ ] Staging deployment successful; smoke tests pass
- [ ] Rollback procedure documented and tested
- [ ] Pre-production backup completed and verified
- [ ] Post-deployment monitoring alerts configured
- [ ] On-call team notified 24hrs prior to deployment

---

## Control 2: Incident Response & Rollback Procedures (EATGF-DSS-INC-01)

### Purpose

Organization responds to production incidents with defined escalation, communication, and rollback procedures, enabling rapid recovery with full audit trail.

### Incident Classification

**Severity Levels:**

| Level        | Downtime    | Impact                                | Response Time | Example                                       |
| ------------ | ----------- | ------------------------------------- | ------------- | --------------------------------------------- |
| **Critical** | >30 min     | All users/features affected           | <15 min       | Data loss, auth broken, API down              |
| **High**     | 5-30 min    | Major feature/region down             | <1 hour       | Payment processing failed, SaaS region down   |
| **Medium**   | <5 min      | Small feature or user subset affected | <4 hours      | Report page slow, single region latency spike |
| **Low**      | No downtime | Performance degradation, warnings     | <24 hours     | Disk space warning, deprecated API usage      |

### Incident Response Runbook

**Critical Incident (Production Down):**

```
┌─────────────────────────────────────────────────────┐
│ STEP 1: DECLARE INCIDENT (< 2 min)                 │
├─────────────────────────────────────────────────────┤
│ Action:                                             │
│  1. On-call engineer opens incident in PagerDuty   │
│  2. Set severity: CRITICAL                         │
│  3. Notified: CTO, VP Engineering, Product Lead   │
│  4. Slack channel #incident-war-room created       │
│  5. Zoom call started (recording enabled)          │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│ STEP 2: TRIAGE & DIAGNOSIS (< 5 min)              │
├─────────────────────────────────────────────────────┤
│ Questions:                                          │
│  • What is down? (API, web, database, all?)        │
│  • When did it start? (exact time)                 │
│  • What changed? (recent deploys, config, alert?) │
│  • How many users affected? (% of traffic)         │
│ Actions:                                            │
│  • Check deployment log (revert if <2hrs old)     │
│  • Check monitoring (errors, CPU, memory)          │
│  • Check database replication lag                  │
│  • Check external dependencies (API, ISP down?)   │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│ STEP 3: EXECUTE ROLLBACK (if recent deploy)       │
├─────────────────────────────────────────────────────┤
│ Decision point:                                     │
│  IF recent deploy (< 2 hours) + app causing issue  │
│    → EXECUTE ROLLBACK (< 5 min)                    │
│  ELSE                                               │
│    → INVESTIGATE DATABASE / INFRASTRUCTURE         │
│ Rollback procedure:                                 │
│  1. git log --oneline (last 5 commits)            │
│  2. kubectl rollout undo deployment/myapp          │
│  3. Wait 2min; validate health checks              │
│  4. Disable traffic shift (revert to 100% old)    │
│  5. Monitor error rates (30sec check)              │
│  6. SUCCESS → document root cause                  │
│     FAILURE → continue investigation               │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│ STEP 4: RECOVERY & VALIDATION                      │
├─────────────────────────────────────────────────────┤
│ Metrics to verify:                                  │
│  • API response time < 200ms p99                   │
│  • Error rate < 0.1%                              │
│  • Database replication lag < 1s                   │
│  • User reports: no new errors in support          │
│ Sign-off: Ops Lead confirms system healthy         │
│ Timeline: +15 min from rollback start               │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│ STEP 5: COMMUNICATE & DOCUMENT                     │
├─────────────────────────────────────────────────────┤
│ Communications:                                     │
│  • Slack #announcements: "Resolved, root cause:"  │
│  • Customer status page: mark incident resolved   │
│  • Email notification to affected customers       │
│ Documentation:                                      │
│  • Timeline: exact start/end times                 │
│  • Root cause: (deploy, config, dependency, etc.)  │
│  • Actions taken: (rollback, restart, etc.)        │
│  • RCA scheduled: within 24 hours                  │
│  • Ticket created for fix: in backlog             │
└─────────────────────────────────────────────────────┘
```

### Rollback Procedure (Tested Quarterly)

**Blue-Green Rollback (Zero-Downtime):**

```
Before Rollback:
  Blue (Old):   60% traffic → v1.2.3 (stable)
  Green (New):  40% traffic → v1.3.0 (issues)

Decision: Rollback detected

Execution (< 2 min):
  1. kubectl set image deployment/app app=app:v1.2.3
  2. kubectl rollout status deployment/app (wait for complete)
  3. Traffic routing: revert 100% → v1.2.3
  4. Verify health: GET /-/health (200 OK)
  5. Error rate check: <0.1% for 30sec

After Rollback:
  Blue (Old):   100% traffic → v1.2.3 (healthy)
  Green (New):  Offline pending investigation
```

**Quarterly Rollback Test:**

- Schedule: First Wednesday of quarter (Jan 4, Apr 3, Jul 2, Oct 1)
- Procedure: Execute full rollback in production (within maintenance window)
- Validation: All health checks pass; no customer impact
- Documentation: Test results in audit log (Jira ticket Auto-created)

### Incident Post-Mortem

**Within 24 Hours:**

1. **Root Cause Analysis (RCA)**
   - What happened? (timeline of events)
   - Why did it happen? (root cause, not symptoms)
   - What prevented earlier detection? (monitoring gaps)

2. **5 Whys Analysis**

   ```
   Issue: Payment API timeout
   Why 1: Database connection pool exhausted
   Why 2: Query N+1 in new code change
   Why 3: Code review missed query optimization
   Why 4: Load test only used 100 concurrent users
   Why 5: Capacity planning used old traffic metrics

   Root Cause: Load test insufficient; using stale metrics
   ```

3. **Action Items (Blameless Culture)**
   - [ ] Deploy database connection limit alert (Ops)
   - [ ] Add N+1 query detection to SAST (Security)
   - [ ] Update load test to 50K concurrent users (QA)
   - [ ] Quarterly capacity review process (Product)
   - Owner & deadline assigned to each item

4. **Metrics Captured**
   - Time to detect: 5 min
   - Time to respond: 3 min
   - Time to resolve (TTR): 8 min total (within 15min target)
   - Customer impact: 2,500 users; 2% transaction failure

### Evidence Checklist

- [ ] Critical incident declared and escalation initiated (<2 min)
- [ ] Triage completed; root cause identified or rollback executed
- [ ] Rollback procedure executed successfully or issue contained
- [ ] Recovery validated (health checks, metrics normal)
- [ ] Status page / customer communications sent
- [ ] Post-mortem completed within 24 hours
- [ ] RCA documented (5 Whys analysis completed)
- [ ] Action items assigned with deadlines
- [ ] Quarterly rollback test scheduled and documented

---

## Control 3: Application End-of-Life Governance (EATGF-DSS-EOL-01)

### Purpose

Organization manages application sunset with defined decommissioning procedures, data retention, and customer notification timelines, preventing orphaned systems.

### End-of-Life Timeline

**Phase 1: Announcement (Months 1-2)**

- Executive decision to sunset application
- End-of-Support (EOS) date announced: 90-day minimum notice
- Migration path documented (alternative service or data export)
- Support plan: what happens during EOL window

Example announcement:

```
"Application X reaches End-of-Support on June 30, 2026.

Timeline:
- April 1, 2026: New features frozen (security patches only)
- May 15, 2026: Last login period starts; data export available
- June 30, 2026: Application shut down; all data deleted

Migration: Export your data via [Settings > Export] or contact support@company.com"
```

**Phase 2: Maintenance Mode (Month 2-3)**

- No new features developed
- Critical security patches only
- All new usage redirected to replacement service
- Data export functionality enabled
- Migration tools provided or manual export documented

**Phase 3: Final Support (Final 30 days)**

- Reminder emails to all active users (weekly)
- Support team on standby (escalation only)
- Technical blog post: "Migrating from Application X"
- Decommissioning checklist reviewed with Ops

**Phase 4: Decommissioning (Final day)**

### Decommissioning Checklist

**72 Hours Before Shutdown:**

- [ ] Final backup of application database
- [ ] Data retention verification (what stays, what deletes)
- [ ] Customer support contact confirmation (who handles questions)
- [ ] Monitoring alerts disabled (prevent false positives)

**24 Hours Before Shutdown:**

- [ ] Final reminder emails sent to all users
- [ ] Read-only mode activated (no new data accepted)
- [ ] Redirect page prepared (link to replacement service)
- [ ] On-call team briefed (escalation route)

**Shutdown Hour (T-0:00 to T+1:00):**

```
T-0:30:  Final application health check OK
T-0:15:  Load balancer drains connections (graceful shutdown)
T-0:00:  Application stops accepting requests
T+0:05:  Database connections terminated
T+0:10:  DNS record updated (point to redirect page)
T+0:15:  Final verification: application unreachable
T+0:30:  Archive database to cold storage (AWS S3 Glacier)
T+0:45:  Infrastructure de-provisioned (servers, containers removed)
T+1:00:  Webhook notifications sent (customer integrations informed)
```

**After Shutdown:**

- [ ] Incident report closed (if any issues encountered)
- [ ] Post-mortem: lessons learned documented
- [ ] Customer feedback collected (migration smooth? issues?)
- [ ] Data retention audit (verify old data archived correctly)
- [ ] Cost savings calculated and reported

### Data Retention Policy

| Data Category        | Retention Period  | Storage Destination                | Deletion Authority             |
| -------------------- | ----------------- | ---------------------------------- | ------------------------------ |
| **Customer Data**    | 30 days after EOL | Encrypted archive (S3 Glacier)     | Customer request or 1-year max |
| **Audit Logs**       | 12 months         | Archive (cold storage)             | Compliance requirement         |
| **Application Code** | Indefinite        | Git repository (archived branch)   | Engineering decision           |
| **Performance Data** | 90 days           | Monitoring system (time-series db) | Metrics retention policy       |
| **Configuration**    | 12 months         | Backup (encrypted)                 | Disaster recovery requirement  |

### Evidence Checklist

- [ ] End-of-Support date announced 90+ days in advance
- [ ] Migration path documented and communicated
- [ ] Application in maintenance mode (no new features)
- [ ] Data export functionality enabled and tested
- [ ] Final backup completed and verified
- [ ] Decommissioning checklist completed
- [ ] DNS/redirect page prepared and tested
- [ ] Data retention audit completed (archived data verified)
- [ ] Customer feedback collected post-decommissioning

---

## Control 4: Production Operations & Monitoring (EATGF-DSS-OPS-01)

### Purpose

Organization maintains production system health through continuous monitoring, alerting, and operational discipline, ensuring rapid problem detection and response.

### Production Monitoring Standards

**Core Metrics (Real-time Dashboard):**

| Metric                     | Type         | Target    | Alert Threshold        | Owner |
| -------------------------- | ------------ | --------- | ---------------------- | ----- |
| **API Latency (p99)**      | Performance  | <200ms    | >500ms                 | Ops   |
| **Error Rate**             | Reliability  | <0.1%     | >1%                    | Ops   |
| **Uptime**                 | Availability | 99.95%    | <99.9% (ongoing month) | Ops   |
| **Database Response Time** | Performance  | <20ms     | >100ms                 | DBA   |
| **CPU Utilization**        | Capacity     | <70%      | >80%                   | Ops   |
| **Memory Utilization**     | Capacity     | <80%      | >90%                   | Ops   |
| **Disk Space**             | Capacity     | <80%      | >90%                   | Ops   |
| **Active Connections**     | Capacity     | <80% pool | >95% pool              | DBA   |

**Dashboard Tools:** Datadog, New Relic, or Grafana (updated every 60 seconds)

### On-Call Rotation

**Coverage Requirements:**

- 24/7 on-call rotation (1 primary, 1 secondary)
- On-call weeks: 1 per 4-week rotation (e.g., Jan 1-7, Jan 29-Feb 4)
- Response time: <15 min for critical, <1 hour for high
- Acknowledgement required within 5 min or escalation triggered

**On-Call Responsibilities:**

1. Receive PagerDuty alert (sms + phone call)
2. Acknowledge within 5 min (confirm receipt)
3. Assess incident severity (critical/high/medium/low)
4. For critical: execute incident response procedures
5. For medium/low: create ticket; handle next business day

### Operational Runbooks

Runbook locations: `/docs/operations/runbooks/`

**Required Runbooks:**

- Database failover (cross-AZ switchover)
- Cache invalidation (Redis flush procedure)
- DNS update (pointing to backup service)
- SSL certificate renewal (before expiration)
- Disk cleanup (old logs, temp files)
- Secrets rotation (API keys, passwords)

**Runbook Template:**

```
# Runbook: [Title]

**Severity:** [Critical/High/Medium/Low]
**Estimated Time:** [5min / 30min / 2hr]

## Prerequisites
- [ ] Step 1
- [ ] Step 2

## Execution
1. Step A (command / action)
2. Step B
3. Verification: Check output

## Rollback
If something goes wrong:
- Action: Undo step
- Verify: Health check passed
```

### Change Log & Audit Trail

**All changes logged in:**

- Git (application code)
- Infrastructure-as-Code repo (Terraform / CloudFormation)
- Configuration management (Ansible, Chef)
- DNS registrar
- Monitoring tools (alert threshold changes)

**Searchable audit trail:**

- Query: "who changed X?" → Git blamed; author identified
- Query: "when was X changed?" → Commit timestamp
- Query: "why was X changed?" → Commit message / ticket link
- Retention: 12 months minimum

### Evidence Checklist

- [ ] Production monitoring dashboard live (all core metrics visible)
- [ ] Alert thresholds configured per metric
- [ ] On-call rotation schedule published
- [ ] Runbooks written and tested (all critical procedures covered)
- [ ] Post-incident monitoring verified (alerts trigger within 30sec)
- [ ] On-call team trained on incident procedures
- [ ] Quarterly drill: simulate critical incident; execute procedures
- [ ] Audit log searchable; retention verified (12+ months)

---

## Compliance Alignment

| EATGF Control | ISO 27001:2022 | NIST 800-53 | COBIT 2019   |
| ------------- | -------------- | ----------- | ------------ |
| BAI-REL-01    | 8.34, 5.37     | CM-3, SA-10 | BAI03        |
| DSS-INC-01    | 7.3, A.16      | IR-4, CP-2  | DSS02, MEA01 |
| DSS-EOL-01    | 8.26, 5.36     | CM-2, CP-4  | DSS03        |
| DSS-OPS-01    | 9.1, 9.2       | AU-6, SI-4  | DSS01, MEA01 |

### Governance Implications

**Risk if Not Implemented:**

- Uncontrolled changes; production outages from untested code
- No incident diagnosis capability; slow mean-time-to-recovery
- Orphaned applications; security risks from unsupported software
- Operational blindness; no monitoring of system health

**Operational Impact:**

- Faster releases with confidence (gates prevent failures)
- Rapid incident response (documented procedures, practiced quarterly)
- Technical debt decreases (EOL process forces cleanup)
- Team autonomy increases (clear authority model, runbooks)

**Audit Consequences:**

- SOC 2 Type II: Requires change control, incident response procedures, monitoring
- ISO 27001: Change management, incident response, asset retirement required
- PCI-DSS: Change approval, audit logging, incident documentation required

---

## Version & Authority

| Field           | Value                                                                  |
| --------------- | ---------------------------------------------------------------------- |
| **Version**     | 2.0-COMPREHENSIVE                                                      |
| **Date Issued** | 2026-02-15                                                             |
| **Change Type** | Major (placeholder → comprehensive)                                    |
| **Related MCM** | EATGF-BAI-REL-01, EATGF-DSS-INC-01, EATGF-DSS-EOL-01, EATGF-DSS-OPS-01 |
| **Next Review** | 2026-08-15                                                             |

**Classification:** Internal - Governance
**Authority:** EATGF Layer 08, Domain 06
**Distribution:** Release Managers, DevOps, SREs, On-Call Team, Product Leads
