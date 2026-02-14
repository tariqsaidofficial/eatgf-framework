# Change Approval Model

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 05_APPLICATION_LIFECYCLE_GOVERNANCE
**Governance Scope:** Process Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 05_APPLICATION_LIFECYCLE_GOVERNANCE

**Governance Scope:** Change classification, approval workflows, and emergency change procedures.

**Control Authority Relationship:** Implements:

- Layer 02: Change Management Controls
- Layer 04: Governance Charter
- ITIL Change Management

## Purpose

Defines change approval requirements based on risk level including classification criteria, approval authorities, and emergency procedures.

## Governance Principles

- **Control-Centric Architecture:** Risk-based approval gates
- **Developer-Operational Alignment:** Fast approvals for low-risk changes
- **Audit Traceability:** All changes logged and approved
- **Single Source of Truth:** Centralized change tracking

## Change Classification

**Requirement:** Classify all changes by risk level.

**Change Categories:**

| Category      | Risk Level | Examples                                       | Approval Required                     |
| ------------- | ---------- | ---------------------------------------------- | ------------------------------------- |
| **Standard**  | Low        | Bug fixes, minor updates, config changes       | Engineering Lead                      |
| **Normal**    | Medium     | New features, refactoring, dependency updates  | Engineering Lead + Security Champion  |
| **Major**     | High       | Architecture changes, breaking API changes     | Engineering Lead + Security + Product |
| **Emergency** | Variable   | Critical security patch, production outage fix | Post-implementation review            |

**Classification Criteria:**

**Standard Change:**

- Well-understood, low-risk
- No impact on API contracts or data schema
- Fully tested and reviewed

**Normal Change:**

- Introduces new functionality
- Moderate complexity
- Requires cross-team coordination

**Major Change:**

- Significant architecture impact
- Breaking changes to APIs or integrations
- High complexity or risk
- Regulatory implications

**Emergency Change:**

- Addresses critical production issue
- Security vulnerability requiring urgent patch
- Requires immediate action to restore service

## Approval Workflows

### Standard Change

**Approval Authority:** Engineering Lead

**Process:**

1. Developer creates pull request
2. Automated tests pass
3. Peer review approval
4. Engineering lead approval
5. Merge to main branch
6. Automated deployment to staging
7. Manual approval for production

**Approval Timeline:** Same day

### Normal Change

**Approval Authority:** Engineering Lead + Security Champion

**Process:**

1. Developer creates pull request with design document
2. Automated tests and security scans pass
3. Peer review approval
4. Security champion review (if security-relevant)
5. Engineering lead approval
6. Merge and deploy to staging
7. Integration testing in staging
8. Engineering lead approves production deployment

**Approval Timeline:** 1-2 business days

### Major Change

**Approval Authority:** Engineering Lead + Security Champion + Product Owner

**Process:**

1. Design document and architecture review
2. Impact assessment (API consumers, dependencies, data migration)
3. Pull request with implementation
4. Security review and threat modeling update
5. Engineering lead approval
6. Product owner approval (business impact)
7. Staged rollout (canary or feature flag)
8. Post-deployment validation

**Approval Timeline:** 1 week

### Emergency Change

**Approval Authority:** Engineering Lead (with post-implementation review)

**Process:**

1. Incident declared
2. Emergency change documented in incident channel
3. Engineering lead provides verbal approval
4. Change implemented with peer present (if possible)
5. Deployment to production
6. Post-implementation review within 24 hours
7. Formal change request created retrospectively

**Approval Timeline:** Minutes to hours

## Change Advisory Board (CAB)

**Requirement:** CAB reviews major changes and oversees change governance.

**CAB Composition:**

- Engineering Manager (chair)
- Security Lead
- Product Lead
- DevOps Lead
- Senior Engineer representatives

**Meeting Cadence:** Weekly

**Responsibilities:**

- Review major change requests
- Assess risk and approve/deny
- Monitor change success metrics
- Review emergency changes
- Continuous improvement of change process

## Change Documentation

**Requirement:** Document all changes in change management system.

**Required Information:**

- Change requestor and implementation team
- Change classification
- Description of change and business justification
- Risk assessment and rollback plan
- Testing and validation plan
- Approvers and approval timestamp
- Deployment schedule
- Post-implementation validation results

**Change Management Tools:**

- Jira / Linear / Azure DevOps
- ServiceNow (for enterprise)
- GitHub/GitLab issue tracking

## Metrics and Reporting

**Requirement:** Track change metrics for continuous improvement.

**Tracked Metrics:**

- Change success rate (% of changes without rollback)
- Change approval cycle time
- Emergency change frequency
- Change-related incidents
- Mean time to approve (by category)

**Monthly Report:**

- Number of changes by category
- Success/failure rate
- Trends and improvement opportunities

## Control Mapping

| EATGF Context         | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
| --------------------- | -------------- | --------- | ----- | ----- |
| Change Classification | A.8.32         | PS.3      | -     | BAI06 |
| Approval Workflow     | A.5.22         | PO.1      | -     | BAI06 |
| Emergency Changes     | A.5.26         | RV.2      | -     | DSS02 |
| Metrics               | A.5.37         | PO.5      | -     | MEA01 |

## Developer Checklist

For every change:

- [ ] Change classified (Standard, Normal, Major, Emergency)
- [ ] Change documented in tracking system
- [ ] Risk assessment completed
- [ ] Rollback plan documented
- [ ] Appropriate approvals obtained
- [ ] Test evidence provided

## References

- ITIL 4: Change Enablement
- ISO/IEC 20000-1: Service Management
- COBIT 2019: BAI06 (Manage Changes)

## Version History

| Version | Date       | Change Type | Description                   |
| ------- | ---------- | ----------- | ----------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial change approval model |
