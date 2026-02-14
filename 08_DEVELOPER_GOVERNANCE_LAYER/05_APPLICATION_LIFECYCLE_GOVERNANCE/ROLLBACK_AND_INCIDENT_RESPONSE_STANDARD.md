# Rollback and Incident Response Standard

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 05_APPLICATION_LIFECYCLE_GOVERNANCE
**Governance Scope:** Operational Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 05_APPLICATION_LIFECYCLE_GOVERNANCE

**Governance Scope:** Rollback procedures, incident classification, and incident response for application deployments.

**Control Authority Relationship:** Implements:

- Layer 02: Incident Management Controls
- Layer 04: Information Security Policy
- NIST SSDF RV.2 (Respond to vulnerabilities)

## Purpose

Defines procedures for application rollback and incident response including incident classification, escalation, rollback execution, and post-incident review.

## Governance Principles

- **Control-Centric Architecture:** Automated rollback mechanisms
- **Developer-Operational Alignment:** Fast incident response
- **Audit Traceability:** Full incident documentation
- **Security-by-Design:** Security incident escalation

## Incident Classification

**Requirement:** Classify incidents by severity.

**Severity Levels:**

| Severity | Impact | Response Time | Examples |
|---|---|---|---|
| **P0 (Critical)** | Complete service outage | 15 minutes | Database down, authentication broken |
| **P1 (High)** | Major functionality degraded | 1 hour | Slow API response, partial feature failure |
| **P2 (Medium)** | Minor functionality impaired | 4 hours | Non-critical feature broken, UI glitch |
| **P3 (Low)** | Minimal impact | 1 business day | Cosmetic issues, minor bugs |

## Incident Response Roles

**Incident Commander:** Coordinates response, makes rollback/escalation decisions.

**Engineering On-Call:** Investigates and implements fixes or rollbacks.

**Communications Lead:** Updates stakeholders and customers.

**Subject Matter Experts:** Provide domain expertise as needed.

## Rollback Decision Criteria

**Requirement:** Execute rollback if incident meets rollback criteria.

**Rollback Triggers:**

- Service availability <99% (P0 incident)
- Error rate >5% (P1 incident)
- Security vulnerability introduced (any severity)
- Data corruption or loss detected
- Incident root cause unknown and fix not immediately available

**Rollback Authority:**

- P0/P1 incidents: Incident Commander or Engineering On-Call
- P2/P3 incidents: Engineering Lead

## Rollback Procedures

### Blue/Green Deployment Rollback

**Procedure:**

1. Switch traffic back to previous (blue) environment
2. Validate service restored
3. Communicate rollback to team
4. Investigate root cause

**Execution Time:** <5 minutes

### Canary Deployment Rollback

**Procedure:**

1. Stop canary rollout
2. Route all traffic to stable version
3. Validate service restored
4. Investigate root cause

**Execution Time:** <10 minutes

### Rolling Deployment Rollback

**Procedure:**

1. Halt ongoing deployment
2. Redeploy previous version to all instances
3. Validate service restored
4. Investigate root cause

**Execution Time:** 10-30 minutes (depends on number of instances)

### Database Migration Rollback

**Requirement:** All database migrations must be reversible.

**Procedure:**

1. Execute rollback migration script
2. Validate data integrity
3. Redeploy previous application version
4. Validate application functionality

**Execution Time:** Variable (15 minutes to several hours)

**Prevention:** Test migrations in staging, use backward-compatible migrations where possible.

## Incident Response Workflow

**Phase 1: Detection and Triage (0-5 minutes)**

1. Incident detected (monitoring alert, user report)
2. On-call engineer acknowledges
3. Assess severity and classify
4. Declare incident in incident channel

**Phase 2: Incident Response (5-30 minutes)**

1. Assemble incident response team
2. Investigate root cause
3. Decide: Fix forward or rollback
4. Execute rollback if necessary
5. Validate service restoration

**Phase 3: Communication**

1. Update internal stakeholders
2. Update status page for customers
3. Provide ETA for resolution

**Phase 4: Resolution**

1. Implement permanent fix
2. Deploy fix to production
3. Validate resolution
4. Close incident

**Phase 5: Post-Incident Review (within 48 hours)**

1. Conduct blameless post-mortem
2. Document timeline and root cause
3. Identify action items for prevention
4. Assign owners and due dates
5. Follow up on action items

## Incident Communication

**Requirement:** Communicate incident status regularly.

**Internal Communication:**

- Incident channel (Slack, Teams) for real-time updates
- Status updates every 30 minutes during active incident
- Executive summary for P0/P1 incidents

**External Communication (Customers):**

- Update status page within 30 minutes of P0/P1 incident
- Provide status updates until resolution
- Publish post-incident report (for P0 incidents)

## Post-Incident Review (PIR)

**Requirement:** Conduct PIR for all P0 and P1 incidents.

**PIR Template:**

- **Incident Summary:** What happened, when, impact
- **Timeline:** Detailed sequence of events
- **Root Cause:** Technical root cause and contributing factors
- **Resolution:** How was it resolved
- **Action Items:** What will prevent recurrence
- **Lessons Learned:** What went well, what to improve

**PIR Distribution:**

- Engineering team review (all P0/P1 incidents)
- Leadership review (P0 incidents)
- Customer communication (P0 incidents with customer impact)

## Testing and Preparedness

**Requirement:** Test rollback procedures quarterly.

**Testing Activities:**

- **Game Days:** Simulate production incident and practice rollback
- **Chaos Engineering:** Intentionally introduce failures in staging
- **Tabletop Exercises:** Walk through incident response scenarios
- **Rollback Drills:** Practice rollback on non-critical deployment

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Incident Classification | A.5.26 | RV.2 | - | DSS02 |
| Rollback Procedures | A.5.27 | RV.2 | - | DSS02 |
| Post-Incident Review | A.5.28 | RV.3 | - | DSS03 |

## Developer Checklist

For every deployment:

- [ ] Rollback procedure documented and tested
- [ ] Incident response team identified
- [ ] Monitoring and alerting configured
- [ ] Status page updated if customer-facing
- [ ] Post-deployment validation plan ready

## References

- NIST SP 800-218 (SSDF Practice RV.2)
- ISO/IEC 27035: Incident Management
- Site Reliability Engineering, Google
- PagerDuty Incident Response Guide

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial rollback and incident response standard |
