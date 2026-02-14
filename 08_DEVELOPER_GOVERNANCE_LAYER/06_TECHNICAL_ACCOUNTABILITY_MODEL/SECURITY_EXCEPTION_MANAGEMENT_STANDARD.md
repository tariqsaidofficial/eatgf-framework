# Security Exception Management Standard

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 06_TECHNICAL_ACCOUNTABILITY_MODEL
**Governance Scope:** Exception Process
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 06_TECHNICAL_ACCOUNTABILITY_MODEL

**Governance Scope:** Security exception request, approval, tracking, and remediation process.

**Control Authority Relationship:** Implements:

- Layer 02: Risk Management Controls
- Layer 04: Information Security Policy
- Exception handling framework

## Purpose

Defines process for requesting, approving, and managing security exceptions when compliance with security standards is not feasible.

## Governance Principles

- **Control-Centric Architecture:** Exceptions tracked and time-limited
- **Security-by-Design:** Exceptions are rare, with compensating controls
- **Audit Traceability:** All exceptions documented and auditable
- **Developer-Operational Alignment:** Clear exception process without blocking work

## Exception Definition

**Security Exception:** Temporary or permanent waiver of security requirement due to:

- Technical limitations
- Business constraints
- Legacy system constraints
- Cost-benefit analysis

**Not Exceptions (Use Normal Process):**

- False positive security findings (use suppression with justification)
- Interpretative differences (resolve via security champion or policy clarification)

## When to Request Exception

**Valid Exception Reasons:**

- **Technical Limitation:** Technology does not support required control (e.g., legacy OS cannot be patched)
- **Business Deadline:** Critical business deadline cannot be met with full compliance (time-limited exception)
- **Cost Prohibitive:** Cost of compliance far exceeds risk (rare, requires executive approval)
- **Third-Party Dependency:** Vendor system does not meet requirement and no alternative exists

**Invalid Exception Reasons:**

- Convenience or developer preference
- Lack of knowledge or training
- "It's too hard"
- Insufficient time due to poor planning

## Exception Classification

**Requirement:** Classify exceptions by risk level.

**Exception Risk Levels:**

| Risk Level   | Description                                             | Approval Authority          | Max Duration | Examples                                                    |
| ------------ | ------------------------------------------------------- | --------------------------- | ------------ | ----------------------------------------------------------- |
| **Low**      | Minimal security impact                                 | Security Champion           | 6 months     | Old dependency with no critical vulns, non-standard logging |
| **Medium**   | Moderate security risk with compensating controls       | Security Team               | 3 months     | Delayed patching, limited encryption scope                  |
| **High**     | Significant risk requiring strong compensating controls | Security Team + Eng Manager | 1 month      | Production deploy without full security testing             |
| **Critical** | Unacceptable risk without executive approval            | CISO + CTO                  | 2 weeks      | Production system with critical vulnerability               |

## Exception Request Process

**Requirement:** Submit formal exception request for approval.

**Exception Request Contents:**

**1. Exception Details**

- Requirement being waived (reference policy section)
- System/application affected
- Duration requested (start and end date)

**2. Risk Assessment**

- Description of security risk
- Risk level (Low, Medium, High, Critical)
- Affected assets and data classification
- Potential impact of exploitation

**3. Justification**

- Business or technical justification
- Why compliance is not feasible
- Alternative approaches considered and rejected

**4. Compensating Controls**

- Mitigations to reduce risk
- Additional monitoring or detection measures
- Access restrictions
- Incident response preparedness

**5. Remediation Plan**

- How will compliance be achieved (if temporary exception)
- Target remediation date
- Resources required
- Dependencies

**Exception Request Template:**

```markdown
# Security Exception Request: [Short Description]

**Submitted By:** [Name, Team]
**Date:** [YYYY-MM-DD]
**Risk Level:** [Low/Medium/High/Critical]

## Requirement Being Waived

[Policy reference and specific requirement]

## System/Application Affected

[System name, environment, data classification]

## Requested Duration

**Start Date:** [YYYY-MM-DD]
**End Date:** [YYYY-MM-DD] (Max: per risk level)

## Risk Assessment

**Security Risk:** [Description of risk]
**Affected Assets:** [Data, systems, credentials]
**Impact if Exploited:** [Confidentiality, Integrity, Availability impact]

## Justification

**Why is compliance not feasible?**

[Detailed explanation]

**Alternative Approaches Considered:**

1. [Option 1] - [Why rejected]
2. [Option 2] - [Why rejected]

## Compensating Controls

1. [Control 1]
2. [Control 2]
3. [Control 3]

## Remediation Plan (for temporary exceptions)

**Remediation Action:** [Description]
**Target Date:** [YYYY-MM-DD]
**Owner:** [Name]
**Resources Required:** [Budget, people, tools]

## Approvals

**Security Champion:** [Approve/Deny] [Date]
**Security Team:** [Approve/Deny] [Date]
**Engineering Manager:** [Approve/Deny] [Date]
```

## Approval Workflow

### Low-Risk Exception

**Approver:** Security Champion

**Timeline:** 2 business days

**Process:**

1. Submit exception request
2. Security champion reviews
3. Approval or denial with feedback
4. If approved, log in exception tracking system

### Medium-Risk Exception

**Approvers:** Security Team + Security Champion

**Timeline:** 1 week

**Process:**

1. Submit exception request
2. Security champion preliminary review
3. Security team detailed review
4. Approval or denial with feedback
5. If approved, log in exception tracking system

### High-Risk Exception

**Approvers:** Security Team + Engineering Manager

**Timeline:** 2 weeks

**Process:**

1. Submit exception request
2. Security team review and risk assessment
3. Engineering manager approval (acknowledges business risk)
4. Document in security exception register
5. Monthly reporting to leadership

### Critical-Risk Exception

**Approvers:** CISO + CTO (or VP Engineering)

**Timeline:** Expedited (same day to 3 days)

**Process:**

1. Submit exception request with executive summary
2. CISO review and risk assessment
3. CTO approval (acknowledges organizational risk)
4. Document in security exception register
5. Immediate reporting to executive leadership
6. Weekly review until remediated

## Exception Tracking

**Requirement:** Maintain central exception register.

**Exception Register Contents:**

| Field                 | Description                          |
| --------------------- | ------------------------------------ |
| Exception ID          | Unique identifier                    |
| Submitted By          | Requestor name and team              |
| Submission Date       | Request date                         |
| Requirement Waived    | Policy reference                     |
| System Affected       | Application or infrastructure        |
| Risk Level            | Low, Medium, High, Critical          |
| Approval Date         | When approved                        |
| Approved By           | Approver names                       |
| Start Date            | Exception effective date             |
| End Date              | Exception expiration date            |
| Status                | Active, Expired, Remediated, Revoked |
| Compensating Controls | Mitigations in place                 |
| Remediation Plan      | How compliance will be achieved      |

**Exception Tracking Tool:**

- Jira / ServiceNow / Compliance Management System
- Searchable and auditable
- Automated expiration alerts

## Exception Monitoring and Review

**Requirement:** Monitor exceptions and enforce expiration.

**Monitoring Activities:**

**Weekly:**

- Review exceptions expiring within 30 days
- Send reminders to exception owners

**Monthly:**

- Report active exceptions to security and engineering leadership
- Review high/critical exceptions with remediation plans

**Quarterly:**

- Audit all active exceptions for continued validity
- Revoke exceptions no longer necessary
- Extend exceptions if justified (requires re-approval)

**Annually:**

- Comprehensive review of exception process effectiveness
- Update exception policy based on lessons learned

## Exception Expiration and Renewal

**Requirement:** Exceptions expire automatically at end date.

**Expiration Process:**

1. 30 days before expiration: Alert to exception owner
2. 7 days before expiration: Escalation to engineering manager
3. Expiration date: Exception automatically revoked
4. Post-expiration: Security control must be complied with or new exception requested

**Renewal Process:**

- Owner submits new exception request
- Cannot extend existing exception without re-approval
- Renewal requires same approval process as original request
- Frequent renewals trigger escalation (why is remediation not progressing?)

## Exception Revocation

**Requirement:** Revoke exceptions immediately if risk changes.

**Revocation Triggers:**

- **Exploited Vulnerability:** If weakness waived by exception is exploited
- **Threat Intelligence:** New threat makes exception too risky
- **Compliance Audit:** Auditor or regulator rejects exception
- **Business Risk Change:** Risk appetite or business context changes

**Revocation Process:**

1. Security team or CISO issues revocation notice
2. Exception owner notified immediately
3. Remediation required within defined timeframe (e.g., 7 days)
4. Escalation if not remediated

## Reporting and Metrics

**Requirement:** Track and report exception metrics.

**Tracked Metrics:**

- Number of active exceptions (by risk level)
- Exception approval/denial rate
- Average exception duration
- Exceptions expired vs. remediated
- Exception recidivism (same issue, multiple exceptions)

**Monthly Dashboard:**

- Active exceptions by team
- Expiring exceptions (next 30 days)
- Overdue remediations
- High/critical exceptions

## Control Mapping

| EATGF Context         | ISO 27001:2022 | NIST SSDF  | OWASP | COBIT |
| --------------------- | -------------- | ---------- | ----- | ----- |
| Exception Management  | A.5.22         | PO.1       | -     | APO12 |
| Risk Acceptance       | A.5.8          | PO.1       | -     | APO12 |
| Compensating Controls | A.5.9          | PO.1, PS.1 | -     | APO13 |

## Developer Checklist

When requesting exception:

- [ ] Confirmed exception is necessary (no alternative)
- [ ] Identified compensating controls
- [ ] Documented remediation plan (if temporary)
- [ ] Submitted exception request with all required fields
- [ ] Obtained appropriate approval
- [ ] Exception logged in tracking system
- [ ] Calendar reminder set for expiration date

## References

- ISO/IEC 27001:2022 (Controls A.5.8, A.5.22)
- NIST SP 800-53: Compensating Security Controls
- COBIT 2019: APO12 (Manage Risk)

## Version History

| Version | Date       | Change Type | Description                                    |
| ------- | ---------- | ----------- | ---------------------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial security exception management standard |
