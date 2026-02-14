# SAST, DAST, and SCA Policy

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 03_DEVSECOPS_GOVERNANCE  
**Governance Scope:** Policy Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

**Governance Scope:** Security testing requirements for static, dynamic, and composition analysis.

**Control Authority Relationship:** Implements:

- Layer 02: Security Testing Controls
- Layer 04: Information Security Policy
- NIST SSDF RV.1 (Review code)

## Purpose

This policy defines mandatory security testing practices using:

- **SAST** (Static Application Security Testing)
- **DAST** (Dynamic Application Security Testing)
- **SCA** (Software Composition Analysis)

## Governance Principles

- **Security-by-Design:** Testing integrated into development workflow
- **Control-Centric Architecture:** Automated enforcement of security quality gates
- **Developer-Operational Alignment:** Actionable findings with remediation guidance
- **Audit Traceability:** All scan results retained for compliance

## Static Application Security Testing (SAST)

### SAST Requirements

**Requirement:** Run SAST on every commit and pull request.

**Developer Requirements:**

- Integrate SAST tool in CI/CD pipeline
- Scan all code changes before merge
- Fail build on critical or high-severity findings
- Provide scan results in pull request comments

**Recommended SAST Tools:**

- SonarQube (multi-language)
- Semgrep (open-source, customizable rules)
- CodeQL (advanced semantic analysis)
- Checkmarx / Veracode (enterprise solutions)

### SAST Configuration

**Requirement:** Configure SAST with appropriate rulesets and thresholds.

**Developer Requirements:**

- Enable OWASP Top 10 and CWE Top 25 rules
- Configure language-specific rules
- Set quality gate thresholds:
  - **Critical findings:** 0 allowed
  - **High findings:** 0 allowed
  - **Medium findings:** Track trend, no regression
- Suppress false positives with documented justification

### SAST Remediation

**Requirement:** Address SAST findings according to severity SLA.

**Remediation SLA:**

| Severity | Remediation Timeline         | Action                                        |
| -------- | ---------------------------- | --------------------------------------------- |
| Critical | Immediate (block deployment) | Fix before merge                              |
| High     | Within 7 days                | Create tracking issue, fix in current sprint  |
| Medium   | Within 30 days               | Create tracking issue, fix in current release |
| Low      | Backlog                      | Address during refactoring or as time permits |

**Developer Requirements:**

- Do not suppress findings without security review
- Document remediation or accepted risk in issue tracker

## Dynamic Application Security Testing (DAST)

### DAST Requirements

**Requirement:** Run DAST in staging environment before production deployment.

**Developer Requirements:**

- Deploy application to staging environment
- Run automated DAST scan
- Fail deployment pipeline on critical findings
- Run authenticated scans (test protected endpoints)
- Schedule regular DAST scans in production (weekly or monthly)

**Recommended DAST Tools:**

- OWASP ZAP (open-source)
- Burp Suite Professional
- Acunetix
- Rapid7 InsightAppSec

### DAST Configuration

**Requirement:** Configure comprehensive DAST scanning.

**Scan Configuration:**

- Crawl all application routes (provide sitemap or OpenAPI spec)
- Test all HTTP methods (GET, POST, PUT, DELETE, etc.)
- Test authenticated and unauthenticated endpoints
- Test for OWASP Top 10 vulnerabilities
- Configure rate limiting to avoid overwhelming application

### DAST Remediation

**Requirement:** Address DAST findings before production deployment.

**Remediation SLA:**

| Severity | Remediation Timeline                   | Action                                        |
| -------- | -------------------------------------- | --------------------------------------------- |
| Critical | Block deployment until remediated      | Fix immediately                               |
| High     | Within 7 days (can deploy with waiver) | Require security team approval for deployment |
| Medium   | Within 30 days                         | Track in issue tracker                        |
| Low      | Backlog                                | Address as time permits                       |

## Software Composition Analysis (SCA)

### SCA Requirements

**Requirement:** Scan all dependencies for known vulnerabilities on every build.

**Developer Requirements:**

- Integrate SCA tool in CI/CD pipeline
- Scan both direct and transitive dependencies
- Fail build on critical or high-severity vulnerabilities
- Generate and review SBOM (Software Bill of Materials)
- Monitor for new vulnerabilities in production dependencies

**Recommended SCA Tools:**

- Snyk (developer-friendly, auto-remediation)
- OWASP Dependency-Check (open-source)
- Dependabot (GitHub native)
- Mend (formerly WhiteSource)
- Sonatype Nexus Lifecycle

### SCA Configuration

**Requirement:** Configure SCA with vulnerability database and policies.

**Developer Requirements:**

- Use up-to-date vulnerability databases (CVE, NVD, GitHub Advisory)
- Set quality gate thresholds:
  - **Critical vulnerabilities:** 0 allowed
  - **High vulnerabilities:** 0 allowed
  - **Medium vulnerabilities:** Track and remediate within 30 days
- Configure license compliance policy (block GPL, AGPL if proprietary)

### SCA Remediation

**Requirement:** Update vulnerable dependencies according to severity SLA.

**Remediation SLA:**

| Severity                 | Remediation Timeline | Action                            |
| ------------------------ | -------------------- | --------------------------------- |
| Critical (CVSS 9.0-10.0) | Within 7 days        | Emergency patch                   |
| High (CVSS 7.0-8.9)      | Within 30 days       | Patch in next release             |
| Medium (CVSS 4.0-6.9)    | Within 90 days       | Track and remediate               |
| Low (CVSS 0.1-3.9)       | Backlog              | Address during dependency updates |

**Developer Requirements:**

- Update to patched version if available
- If no patch available, assess exploitability and apply compensating controls
- Document accepted risk if remediation deferred

### Dependency Approval

**Requirement:** Review and approve new dependencies before introduction.

**Developer Requirements:**

- Run SCA scan on new dependencies
- Check for known vulnerabilities
- Review dependency maintainership and update frequency
- Check license compatibility
- Document approval in pull request

## Tool Integration

### CI/CD Integration

**Requirement:** Integrate all security testing tools in CI/CD pipeline.

**Pipeline Stages:**

```
1. Source Code Checkout
2. SAST Scan (parallel with build)
3. Build Application
4. SCA Scan (dependency check)
5. Unit Tests
6. Deploy to Staging
7. DAST Scan
8. Integration Tests
9. Manual Approval (if security gates passed)
10. Deploy to Production
```

**Developer Requirements:**

- Security scans run automatically on every build
- Build fails if security gates not met
- Scan results visible in CI/CD dashboard
- Alerts sent to team channel on failures

### Developer IDE Integration

**Requirement:** Provide security scanning feedback in developer IDE.

**Developer Requirements:**

- Install IDE plugins for SAST (e.g., SonarLint, Semgrep)
- Enable real-time security feedback while coding
- Fix issues before committing code

## Metrics and Reporting

**Requirement:** Track and report security testing metrics.

**Tracked Metrics:**

- Number of findings by severity (SAST, DAST, SCA)
- Mean time to remediation (MTTR) by severity
- Percentage of builds passing security gates
- Trends over time (improving or regressing)

**Reporting:**

- Weekly dashboard shared with engineering team
- Monthly report to security and engineering leadership
- Quarterly review of security testing effectiveness

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF  | OWASP             | COBIT |
| ------------- | -------------- | ---------- | ----------------- | ----- |
| SAST          | A.8.26         | RV.1       | SAMM Verification | BAI03 |
| DAST          | A.8.29         | RV.1       | ASVS V1           | BAI07 |
| SCA           | A.8.31         | PO.3, RV.1 | Dependency-Check  | BAI07 |
| Remediation   | A.8.8          | RV.2       | -                 | DSS02 |

## Developer Checklist

Before deploying to production:

- [ ] SAST scan passed (0 critical/high findings)
- [ ] SCA scan passed (no vulnerable dependencies)
- [ ] DAST scan completed in staging
- [ ] All critical findings remediated
- [ ] High findings have remediation plan or waiver
- [ ] Security testing results documented

## Governance Implications

**Risk if not implemented:**

- Vulnerabilities deployed to production
- Compliance failures (PCI-DSS, HIPAA require security testing)
- Data breaches from exploitable vulnerabilities

**Operational impact:**

- Early detection reduces remediation cost
- Automated testing reduces manual security review burden
- Developer-friendly tools improve security culture

**Audit consequences:**

- Security testing results demonstrate proactive risk management
- Compliance with secure development lifecycle requirements

**Cross-team dependencies:**

- Security team defines security testing policies
- DevOps team integrates tools in CI/CD
- Engineering managers enforce remediation SLAs

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. SAST/DAST/SCA Policy

## References

- NIST SP 800-218 (SSDF Practice RV.1)
- OWASP Testing Guide (https://owasp.org/www-project-web-security-testing-guide/)
- OWASP Dependency-Check (https://owasp.org/www-project-dependency-check/)
- OWASP ZAP (https://www.zaproxy.org/)
- Semgrep (https://semgrep.dev/)

## Version History

| Version | Date       | Change Type | Description                  |
| ------- | ---------- | ----------- | ---------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial SAST/DAST/SCA policy |
