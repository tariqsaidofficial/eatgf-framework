# SAST, DAST, and SCA Testing Policy

| Field | Value |
|-------|-------|
| Document Type | Implementation Standard |
| Version | 1.0 |
| Classification | Controlled |
| Effective Date | 2026-02-16 |
| Authority | Chief Security Officer and Development Lead |
| EATGF Layer | 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE |
| MCM Reference | EATGF-DEV-SCAN-01 |

---

## Purpose

This policy mandates static application security testing (SAST), dynamic application security testing (DAST), and software composition analysis (SCA) in all development pipelines to detect security defects before production deployment.

**Mandatory for:** All code deployments; all third-party libraries and dependencies.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

- **Upstream dependency:** Layer 02 Control Objectives (vulnerability management, code quality); Layer 04 Information Security Policy (security testing requirements)
- **Downstream usage:** Enforces detection of security defects throughout development lifecycle from code through dependency analysis
- **Cross-layer reference:** Maps to NIST SSDF RV.1 (static testing), RV.2 (dynamic testing), PW.4 (code review)

## Governance Principles

1. **Early Detection** – Security defects detected as early as code check-in, not production deployment
2. **Layered Testing** – SAST (design/architecture), DAST (deployment), SCA (supply chain) provide complementary coverage
3. **Automated Enforcement** – Tools run automatically in CI/CD; violations block deployment without override approval
4. **Developer Experience** – Tools provide actionable feedback with remediation guidance
5. **Continuous Improvement** – Tool configurations evolve based on vulnerability trends and false positive reduction

## Technical Implementation

### Static Application Security Testing (SAST)

**SAST Purpose:** Analyze source code without execution to detect design flaws, injection vulnerabilities, insecure API usage, hardcoded credentials, and configuration errors.

**Mandatory SAST Scanning:**

| Language | Tool | Tier | Cadence |
|----------|------|------|---------|
| Python | Bandit + Semgrep | Tier 1 | Per commit |
| JavaScript/TypeScript | ESLint + Semgrep | Tier 1 | Per commit |
| Java | SonarQube (community) + SpotBugs | Tier 1 | Per commit |
| Go | gosec + Semgrep | Tier 1 | Per commit |
| C/C++ | Clang Static Analyzer + Cppcheck | Tier 1 | Per commit |
| Generic | Semgrep (multi-language) | Core | Per commit |

**SAST Vulnerability Severity Classification:**

| Severity | CVSS | Response | Timeline |
|----------|------|----------|----------|
| Critical | 9.0-10.0 | Block deployment; immediate remediation | 24 hours |
| High | 7.0-8.9 | Block deployment; remediation required before release | 7 days |
| Medium | 4.0-6.9 | Requires risk assessment; default block unless approved | 30 days |
| Low | 0.1-3.9 | Informational; tracked for improvement | No deadline |

**SAST Tool Configuration Examples:**

```yaml
# Semgrep configuration (.semgrep.yml)
rules:
  - id: hardcoded-secrets
    pattern: |
      password = "..."
    message: "Hardcoded credentials detected"
    languages: [python, javascript]
    severity: CRITICAL

  - id: sql-injection
    pattern: |
      execute($SQL)
    message: "SQL injection vulnerability"
    languages: [java, python]
    severity: HIGH
```

**SAST False Positive Handling:**


- False positives tracked in tool configuration
- Suppression comments require justification: `// NOSONAR: reason`
- Suppressed findings reviewed monthly; persistent suppressions escalated
- Suppression trends analyzed to improve tool configuration

### Dynamic Application Security Testing (DAST)

**DAST Purpose:** Test running application to detect runtime vulnerabilities: authentication bypass, authorization flaws, injection attacks, sensitive data exposure, business logic flaws.

**DAST Environment Requirements:**

- **Staging Environment:** Exact replica of production with test data (no production data)
- **Network Isolation:** DAST tool cannot access production systems; separate network segment
- **Test Data:** Sensitive test data masked or synthetic; data retention 30 days post-test
- **API Endpoints:** API contract documented in OpenAPI format for comprehensive testing
- **User Accounts:** Test accounts with various privilege levels; reset after each run

**Mandatory DAST Scanning:**

| API Type | Tool | Cadence | Scope |
|----------|------|---------|-------|
| REST APIs | OWASP ZAP (active) | Pre-release | All endpoints |
| GraphQL APIs | Wunderbucket or custom tooling | Pre-release | Schema + queries |
| Web Applications | BurpSuite Community (active scan) | Pre-release | All web forms |
| Microservices | Postman + Newman for API chains | Per deployment | Service boundaries |

**DAST Vulnerability Severity Classification:**

| Severity | Impact | Response | Example |
|----------|--------|----------|---------|
| Critical | Data breach / account takeover | Block deployment; fix before release | Authentication bypass |
| High | Privilege escalation / sensitive exposure | Block deployment (7-day remediation) | Unauthorized data access |
| Medium | Targeted attack possible | Risk assessment required | Weak password policy |
| Low | Theoretical risk under specific conditions | Documented for future improvement | Cache header missing |

**DAST Test Checklist:**

- [ ] OWASP Top 10 coverage (injection, broken auth, XSS, CSRF, etc.)
- [ ] API fuzzing with negative payloads
- [ ] Session management testing (timeout, fixation, hijacking)
- [ ] Business logic testing (authorization across user roles)
- [ ] Data validation testing (type enforcement, boundaries)
- [ ] Error handling testing (information disclosure through errors)
- [ ] TLS/SSL testing (certificate validity, cipher strength)

### Software Composition Analysis (SCA)

**SCA Purpose:** Analyze dependencies (direct and transitive) to identify known vulnerabilities, license compliance issues, and outdated libraries.

**SCA Vulnerability Sources:**

| Source | Tool | Cadence | Update Frequency |
|--------|------|---------|------------------|
| National Vulnerability Database (NVD) | Dependency-Check | Per build | Daily |
| GitHub Advisory Database | Dependabot / GitHub Advanced Security | Per build | Real-time |
| npm Security Advisory | npm audit | Per build | Real-time |
| Open Source Advisory Database | Sonatype OSS Index | Per build | Real-time |
| Proprietary Database | Snyk Intelligence | On-demand | Real-time |

**Transitive Dependency Analysis:**

```
Application
  ├── Framework A (v2.0)
  │     └── Utility Library B (v1.0)  ← VULNERABLE: CVE-2024-1234, CVSS 8.5
  ├── ORM Library C (v1.5)
  │     └── Connection Pool D (v0.9)
  └── Cache Library E (v3.0)
```

**SCA Vulnerability Response:**

| CVSS Score | Response | Timeline | Escalation |
|-----------|----------|----------|------------|
| 9.0-10.0 | Block build; immediate patching | 24 hours | CISO/CTO |
| 7.0-8.9 | Block build; urgent patching | 7 days | Security lead |
| 5.0-6.9 | Risk assessment; patch within 30 days | 30 days | Development lead |
| 0-4.9 | Tracked in backlog; patch when convenient | 90 days | Development team |

**Dependency Upgrade Strategy:**

- **Security patches:** Applied immediately; automatic PR creation by Dependabot
- **Minor updates:** Applied weekly; tested in separate branch
- **Major updates:** Quarterly review; compatibility assessment required
- **Deprecated libraries:** End-of-life tracking; migration plan required if still in use

**License Compliance Scanning:**

```
Prohibited Licenses (Copyleft):
- GPL v2/v3
- AGPL
- Affero GPL

Restricted Licenses (Review Required):
- LGPL
- MPL (Mozilla Public License)

Approved Licenses:
- MIT
- Apache 2.0
- BSD (2-Clause, 3-Clause)
- ISC
- CC0 (public domain)
```


**License Violation Handling:**

- GPL dependency detected → trigger replacement/exemption process
- No new GPL dependencies added → enforced in SCA gate
- Existing GPL dependencies → document in SBOM with exemption justification

### Integrated Testing Pipeline


**Stage 1: Commit → SAST (Immediate)**

```
git push → pre-commit hook
  ├─ Semgrep on changed files
  ├─ ESLint/Bandit/gosec
  └─ Fail if Critical/High found

```

**Stage 2: Build → SCA (Minutes)**

```
Pull Request Created → Build CI
  ├─ Dependency-Check on all libs
  ├─ License scanning
  ├─ npm audit / pip audit

  └─ Fail if CVSS > 7.0
```

**Stage 3: Release → DAST (Hours)**

```
Pre-release (manual trigger) → Test Environment
  ├─ Deploy to staging
  ├─ OWASP ZAP active scan
  ├─ API fuzzing

  ├─ Coverage report
  └─ Fail if Critical found
```

**Stage 4: Production → Monitoring (Continuous)**

```
Post-release → Production Monitoring
  ├─ Runtime error tracking
  ├─ Security event logging
  ├─ Vulnerability advisories watch

  └─ Automatic patch PR if CVE discovered
```

### Tool Exception Workflow

**Exception Criteria (Valid Reasons):**

- False positive with documented analysis
- Business risk accepted with explicit approval
- Remediation timeline documented with milestone dates
- Mitigation controls implemented (e.g., firewall rule, rate limiting)

**Exception Process:**


1. Developer submits exception via tool UI with justification
2. Security lead reviews (24-hour SLA)
3. If approved: exception recorded with expiration date (max 30 days)
4. If denied: developer remediates or escalates to CISO

**Denied Exception Escalation:**


- CISO reviews; may override with documented business risk acceptance
- Override recorded in audit log; reviewed quarterly
- Trend analysis: frequent overrides indicate tool misconfiguration

### Monitoring and Reporting


**Weekly Reports:**

- Total findings by severity
- True positive vs. false positive ratio
- Exception count and age

- Remediation SLA compliance

**Monthly Reports:**

- Trending analysis (improving or worsening?)
- Top vulnerable libraries company-wide
- Compliance with testing mandate (% of commits scanned)
- Tool effectiveness metrics

**Quarterly Executive Review:**

- Critical findings and incident correlation
- Security posture trend
- Recommended tool updates
- Budget allocation for tool improvements

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| SAST testing | A.8.25, A.8.26 | RV.1.1, RV.1.2 | SAMM-ST | BAI03, BAI07 |
| DAST testing | A.8.25, A.8.26 | RV.2.1, RV.2.2 | ASVS | DSS05.06 |
| SCA analysis | A.8.19, A.8.20 | PW.4.1 | Dependency Check | APO07.02 |
| License compliance | A.8.18 | PO.1 | OSS License | BAI06 |

## Developer Checklist

Before implementing SAST/DAST/SCA testing:

- [ ] SAST tools installed and configured (Bandit/Semgrep/SonarQube)
- [ ] Secrets scanning integrated (TruffleHog/GitGuardian)
- [ ] SCA tool configured with automatic updates (Dependency-Check/Snyk)
- [ ] License scanning enabled with approved/prohibited lists
- [ ] DAST environment prepared (staging replica with test data)

- [ ] OWASP ZAP configured for API/web testing
- [ ] Severity classification matrix documented
- [ ] False positive suppression guidelines established
- [ ] Exception approval workflow implemented
- [ ] Weekly/monthly reporting dashboards configured
- [ ] Developer training on tool outputs and remediation

- [ ] Tool updates scheduled (weekly for vulnerability data)

## Governance Implications

**Risk if not implemented:**


- Vulnerable code reaches production; exploit path discovered in production
- Third-party libraries with known exploits deployed; incident inevitable
- License violations expose organization to legal liability
- Security defects embedded in architecture; expensive to remediate post-deployment

**Operational impact:**


- Build times increase 5-10 minutes for scanning
- False positive rate initially high (requires tuning)
- Development velocity decreases during vulnerability backlog remediation
- Security incident response time decreases dramatically

**Audit consequences:**

- SAST/DAST evidence directly supports NIST RV layer compliance
- Missing SAST scanning indicates deficiency in PW.4 (code review)
- Undetected vulnerabilities in DAST indicate RV.2 control failure
- License violations result in compliance findings

**Cross-team dependencies:**

- Development: tool integration into workflows, vulnerability remediation
- Security: threshold configuration, exception review, vulnerability trending
- Platform: tool infrastructure, artifact scanning integration
- Audit: control evidence collection, exception documentation

## Official References

- **NIST SP 800-218** – Secure Software Development Framework (RV.1, RV.2, PW.4)
- **OWASP Top 10** – Most Critical Web Application Security Risks
- **OWASP SAMM** – Software Assurance Maturity Model (Verification & Validation)
- **CWE Top 25** – Most Dangerous Software Weaknesses (cwe.mitre.org)
- **CVE/NVD** – Common Vulnerability Enumeration (nvd.nist.gov)
- **SBOM Standards** – SPDX, CycloneDX, SWID
- **ISO/IEC 27001:2022** – Information Security Management

## Version History

| Version | Date | Change Type | Description |
|---------|------|-------------|-------------|
| 1.0 | 2026-02-16 | Major | Initial SAST/DAST/SCA testing policy for Layer 08 |
