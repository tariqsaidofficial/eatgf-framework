# Code Review Governance Standard

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 01_SECURE_SDLC  
**Governance Scope:** Implementation Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 01_SECURE_SDLC

**Governance Scope:** Code review requirements, approval workflows, and security review criteria.

**Control Authority Relationship:** Implements:
- Layer 02: Change Management Controls
- Layer 04: Information Security Policy
- NIST SSDF PS.2 (Perform peer review)

## Purpose

This standard defines mandatory code review practices to ensure code quality, security, and compliance. It covers:

- Peer review requirements
- Security-focused review criteria
- Approval workflows and authority
- Review tool configuration
- Metrics and compliance tracking

## Governance Principles

- **Control-Centric Architecture:** Reviews enforce security and quality controls
- **Security-by-Design:** Security assessed before code is merged
- **Audit Traceability:** All reviews documented and logged
- **Developer-Operational Alignment:** Efficient review process without compromising security

## Code Review Requirements

### Peer Review Mandate

**Requirement:** All code changes must be reviewed before merging to protected branches.

**Developer Requirements:**
- Minimum of 1 peer review approval required for standard changes
- Minimum of 2 peer review approvals for high-risk changes
- Security champion review required for security-sensitive code
- Reviewers must not be the author of the code

**High-Risk Changes Definition:**
- Changes to authentication or authorization logic
- Changes to cryptographic implementations
- Changes to data validation or encoding
- Changes to API contracts or database schemas
- Infrastructure-as-code changes affecting production

### Review Scope

**Requirement:** Reviews must assess code for functionality, security, and best practices.

**Reviewer Checklist:**
- [ ] Code implements the intended functionality
- [ ] No introduction of security vulnerabilities
- [ ] Input validation and output encoding applied
- [ ] Error handling implemented correctly
- [ ] No hard-coded credentials or secrets
- [ ] Code follows organizational coding standards
- [ ] Automated tests included and passing
- [ ] No exposed sensitive data in logs or error messages

### Security Review Criteria

**Requirement:** Reviewers must specifically assess security implications.

**Security Review Checklist:**
- [ ] OWASP Top 10 vulnerabilities considered
- [ ] Threat model updated if architecture changed
- [ ] Dependency changes reviewed for known vulnerabilities
- [ ] Authentication and authorization logic correct
- [ ] Data classification and handling appropriate
- [ ] Logging and monitoring implemented for security events

### Automated Code Review

**Requirement:** Automated checks must pass before human review.

**Automated Checks:**
- SAST (Static Application Security Testing) scan
- SCA (Software Composition Analysis) for dependencies
- Code coverage minimum threshold (80%)
- Linting and code style checks
- Unit and integration tests

**Blocking Criteria:**
- Critical or high-severity SAST findings block merge
- Critical or high-severity SCA findings block merge
- Code coverage below minimum threshold blocks merge
- Failed unit or integration tests block merge

### Review Response Time

**Requirement:** Reviews must be completed within defined timeframes.

**Service Level Targets:**
- Standard changes: Review within 1 business day
- High-risk changes: Review within 2 business days
- Hotfix changes: Review within 4 hours

**Escalation:**
- If review not completed within SLA, escalate to engineering manager

### Documentation Requirements

**Requirement:** Review comments and approvals must be documented.

**Developer Requirements:**
- All review comments addressed before merge
- Reviewer explicitly approves with "LGTM" (Looks Good To Me) or equivalent
- Review discussion retained for audit purposes
- Security decisions documented in code comments or architecture docs

### Branch Protection Configuration

**Requirement:** Repository branch protection enforces review requirements.

**Configuration Requirements:**
- Require pull request before merging
- Require approvals (1 for standard, 2 for high-risk)
- Dismiss stale approvals when new commits pushed
- Require status checks to pass before merging
- Require signed commits
- Restrict who can push to protected branches

### Security Champion Review

**Requirement:** Security-sensitive changes require security champion approval.

**Security Champion Responsibilities:**
- Review authentication, authorization, and cryptography changes
- Assess threat modeling implications
- Validate security control implementation
- Escalate to security team when necessary

**Security Champion Criteria:**
- Completed advanced security training
- 2+ years software development experience
- Demonstrated security knowledge

### Metrics and Reporting

**Requirement:** Code review metrics tracked and reported monthly.

**Tracked Metrics:**
- Average review cycle time
- Percentage of reviews completed within SLA
- Number of security findings identified in review
- Code coverage trends
- SAST/SCA finding trends

**Reporting:**
- Monthly dashboard shared with engineering leadership
- Quarterly review of process effectiveness
- Continuous improvement based on metrics

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Peer Review | A.8.26 | PS.2 | SAMM Verification | BAI03 |
| Security Review | A.8.25 | PO.1, RV.1 | ASVS | BAI03 |
| Branch Protection | A.8.3 | PS.1 | - | DSS05 |
| Metrics | A.5.37 | PO.5 | SAMM Measurement | MEA01 |

## Developer Checklist

Before requesting code review:

- [ ] All automated checks passing (SAST, SCA, tests, linting)
- [ ] Self-review completed for security issues
- [ ] Threat model updated if architecture changed
- [ ] Security-sensitive changes flagged for security champion review
- [ ] Meaningful commit messages and pull request description
- [ ] Documentation updated if needed

## Governance Implications

**Risk if not implemented:**
- Introduction of vulnerabilities into production code
- Non-compliance with separation of duties requirements
- Lack of audit trail for code changes
- Knowledge silos within engineering teams

**Operational impact:**
- Improved code quality and reduced defects
- Knowledge sharing across engineering team
- Early detection of security issues (lower remediation cost)
- Compliance with regulatory requirements (e.g., SOC 2, PCI-DSS)

**Audit consequences:**
- Code review process is standard audit requirement
- Lack of documented reviews results in audit findings
- Demonstrates due diligence and security culture

**Cross-team dependencies:**
- Security team provides security champion training
- Engineering managers enforce review SLAs
- DevOps team configures branch protection and automated checks

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. Code Review Governance Standard

## References

- NIST SP 800-218 (SSDF Practice PS.2)
- ISO/IEC 27034 (Application Security)
- OWASP Code Review Guide (https://owasp.org/www-project-code-review-guide/)
- Google Engineering Practices (Code Review) (https://google.github.io/eng-practices/review/)
- CERT Secure Coding Standards

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial code review governance standard |
