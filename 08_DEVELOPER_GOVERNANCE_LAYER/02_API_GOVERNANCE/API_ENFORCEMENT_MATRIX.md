# API Governance Enforcement Matrix

## Purpose

Operationalizes API governance controls through mandatory deployment gates, architectural verification checkpoints, and profile-based enforcement thresholds.

Transforms abstract API_GOVERNANCE_STANDARD principles into concrete, machine-verifiable compliance criteria that prevent non-compliant APIs from reaching production.

## Architectural Position

- **Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
- **Domain:** 02_API_GOVERNANCE
- **Authority Source:** API_GOVERNANCE_STANDARD.md (root authority)
- **Operational Scope:** Pre-merge, pre-release, canary, and production deployment gates
- **Control Authority Relationship:** Implements controls defined in root standard

## Governance Principles

The enforcement matrix operates under these mandatory principles:

- **Mandatory Blocking:** MANDATORY controls block deployment; non-compliance generates automated failure
- **Profile-Based Escalation:** Enterprise enforces stricter gates than Startup/Developer; organizational profile determines applicable control set
- **Sensitive Data Elevation:** APIs handling PII/PHI/financial data automatically escalate to Enterprise controls regardless of organizational profile
- **Exception Documentation:** All exceptions require written justification, security review approval, and time-bound remediation dates
- **Automation-First:** All gates must be automatable in CI/CD; manual-only gates permitted only with documented exception
- **Audit Traceability:** Every gate result logged with decision timestamp, approver identity, and compliance evidence artifacts

## Organization Profiles

| Profile        | Use Case                                                       | Control Baseline                                         | Deployment Risk Tolerance                                             |
| -------------- | -------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| **Enterprise** | Organizations with 500+ developers, multi-tenancy, 24/7 SLAs   | All MANDATORY controls                                   | Zero tolerance; any MANDATORY failure blocks production               |
| **SaaS**       | Platform companies, 100–500 developers, customer data handling | All MANDATORY controls                                   | Zero tolerance; sensitive data elevation mandatory                    |
| **Startup**    | <100 developers, non-regulated data                            | MANDATORY only if sensitive data; RECOMMENDED for others | Medium tolerance; can proceed with RECOMMENDED waiver + documentation |
| **Developer**  | Open source, internal tools, hackathons                        | OPTIONAL for public APIs; RECOMMENDED minimum            | High tolerance; RECOMMENDED gates informational only                  |

## Control Severity Model

| Severity        | Definition                                                                              | Enforcement         | Gate Behavior                                                      | Exception Process                                                                    |
| --------------- | --------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **MANDATORY**   | Control is legally/operationally non-negotiable; failure indicates security breach risk | Deploy immediately  | **BLOCKS deployment** without exception approval                   | Requires: VP-level security approval + risk acknowledgment + 30-day remediation plan |
| **RECOMMENDED** | Best practice; strongly suggested but operational workarounds exist                     | Deploy with warning | **Warning logged** but deployment proceeds; appears in audit trail | Self-documented in PR; requires senior engineer review                               |
| **OPTIONAL**    | Enhancement for defense-in-depth; informational                                         | Deploy with note    | **Informational only**; no blocking; logged for maturity tracking  | No exception required; tracked for future enforcement                                |

## Enforcement Matrix: Control × Profile × Severity

| Control                               | Enterprise | SaaS        | Startup                    | Developer | Technical Gate                                                   |
| ------------------------------------- | ---------- | ----------- | -------------------------- | --------- | ---------------------------------------------------------------- |
| **Authentication (OAuth2/OIDC)**      | MANDATORY  | MANDATORY   | MANDATORY if auth required | OPTIONAL  | Pre-Merge: Static code analysis for token validation patterns    |
| **Authorization (RBAC/ABAC)**         | MANDATORY  | MANDATORY   | RECOMMENDED if multi-user  | OPTIONAL  | Pre-Release: API spec review for resource ownership checks       |
| **API Versioning**                    | MANDATORY  | MANDATORY   | RECOMMENDED                | OPTIONAL  | Pre-Merge: Git lint for /v1/ or header versioning                |
| **Input Validation**                  | MANDATORY  | MANDATORY   | RECOMMENDED                | OPTIONAL  | Pre-Merge: Bandit/CodeQL for schema validation patterns          |
| **Rate Limiting**                     | MANDATORY  | MANDATORY   | RECOMMENDED                | OPTIONAL  | Pre-Release: Load test configuration file presence               |
| **Logging & Observability**           | MANDATORY  | MANDATORY   | RECOMMENDED                | OPTIONAL  | Pre-Release: JSON structured logging config verification         |
| **Webhook Security (HMAC/Timestamp)** | MANDATORY  | MANDATORY   | RECOMMENDED                | OPTIONAL  | Pre-Release: Manual security review of webhook handler code      |
| **API Documentation (OpenAPI 3.0+)**  | MANDATORY  | MANDATORY   | RECOMMENDED                | OPTIONAL  | Pre-Release: OpenAPI spec linting and schema validation          |
| **Secrets Management**                | MANDATORY  | MANDATORY   | RECOMMENDED                | OPTIONAL  | Pre-Merge: Pre-commit hook detection of hardcoded secrets        |
| **Zero Trust (mTLS/Bearer)**          | MANDATORY  | RECOMMENDED | OPTIONAL                   | OPTIONAL  | Pre-Release: Certificate chain validation for service-to-service |

## Deployment Gate Logic

APIs proceed through three sequential gates before production release:

### Gate 1: Security Gate (Pre-Merge)

**Triggered for:** All PRs modifying API endpoints

**Automated Checks (PASS/FAIL):**

- ✓ No hardcoded secrets (pre-commit hook + git-secrets scan)
- ✓ Input validation schema present (Pydantic, JSON Schema, OpenAPI)
- ✓ Authentication mechanism declared (OAuth2/OIDC/mTLS/API key)
- ✓ No SQL/NoSQL injection patterns (Bandit, CodeQL)
- ✓ HTTPS/TLS enforcement declared (no plaintext HTTP)

**Failure Action:** PR blocked automatically; author receives detailed error report with remediation steps

**Override:** VP Security approval required; override logged with business justification

### Gate 2: Architecture Gate (Pre-Release)

**Triggered for:** All code entering staging environment

**Verification Checks (PASS/FAIL/REVIEW):**

- ✓ Authorization matrix documented (RBAC/ABAC definition)
- ✓ Rate limiting configured per tier (free/startup/pro/enterprise)
- ✓ API versioning strategy defined (/v1/, header-based, GraphQL versioning)
- ✓ OpenAPI 3.0+ specification complete and validated
- ✓ Webhook security (HMAC-SHA256 + timestamp validation) if async
- ✓ Logging includes correlation IDs for request traceability

**Failure Action:** Automated notification to API owner; manual review required

**Override:** VP Engineering + VP Security joint approval; override logged with architectural justification

### Gate 3: Compliance Gate (Pre-Release → Canary)

**Triggered for:** All code entering canary/production environments

**Verification Checks (PASS/FAIL/AUDIT):**

- ✓ SOC 2 evidence present (logging retention ≥90 days)
- ✓ Secrets encrypted at rest + in transit (HashiCorp Vault, AWS Secrets Manager)
- ✓ Rate limiting functional verification (stress test confirms enforcement)
- ✓ mTLS certificates valid (if service-to-service)
- ✓ Sensitive data classification documented (PII/PHI/payment card/regulated)
- ✓ Data residency constraints honored (EU, US, compliance-specific geography)
- ✓ GDPR/CCPA capability audit completed (if handling customer data)

**Failure Action:** Canary deployment rejected; issue escalated to Compliance team

**Override:** Chief Information Security Officer (CISO) + Chief Compliance Officer (CCO) joint approval required

## Risk-Based Escalation

Gates automatically escalate based on detected risk factors:

### Risk Level: RED (Critical - Deploy Blocked)

**Triggers:**

- MANDATORY control completely absent (e.g., no authentication mechanism)
- Known CVE in dependency with CVSS ≥ 9.0
- Secrets detected in code repository
- SQL injection vulnerability confirmed
- Cross-tenant data access possible (multi-tenancy systems)

**Required Actions:**

1. Automated deployment block (all gates fail)
2. Automatic ticket creation for VP Security + assigned team
3. VP Security + VP Engineering joint review required
4. No deployment permitted until both parties approve
5. Remediation tracking with hard stop at 72-hour mark

**Audit Trail:** RED escalation logged with affected control, detected risk, approvers, and timeline

### Risk Level: ORANGE (High - Conditional Proceed)

**Triggers:**

- RECOMMENDED control missing (e.g., rate limiting not configured)
- Medium-severity CVE (CVSS 7.0–8.9) in non-critical dependency
- Sensitive data classification unclear
- Documentation incomplete but functional tests pass

**Required Actions:**

1. Automated warning issued; deployment proceeds if within profile tolerance
2. Engineering team lead + Security team review optional but logged
3. Issue tracked for remediation within 30 days
4. Escalates to RED if not resolved before next release cycle

**Audit Trail:** ORANGE escalation logged with conditional approval conditions and remediation deadline

### Risk Level: YELLOW (Low - Informational)

**Triggers:**

- OPTIONAL controls missing (e.g., advanced caching strategies)
- Minor lint violations (whitespace, naming)
- Documentation could be enhanced (non-blocking improvements)

**Required Actions:**

1. Informational logging only; deployment not affected
2. Tracked for maturity progression discussion
3. No remediation deadline

**Audit Trail:** YELLOW logged as informational for trend analysis

## CI/CD Integration

### GitHub Actions Integration Example

```yaml
name: API Governance Enforcement

on:
  pull_request:
    paths:
      - "api/**"
  push:
    branches:
      - staging
      - main

jobs:
  security-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Detect Secrets
        uses: gitleaks/gitleaks-action@v2
        with:
          fail: true
      - name: SAST Scan (Bandit)
        run: |
          pip install bandit
          bandit -r api/ -f json -o bandit-report.json
          if grep -q '"severity": "HIGH"' bandit-report.json; then
            echo "High-severity SAST findings detected"
            exit 1
          fi
      - name: Input Validation Schema Check
        run: |
          python scripts/validate_schemas.py api/
          if [ $? -ne 0 ]; then
            echo "Schema validation failed"
            exit 1
          fi
      - name: Authentication Pattern Check
        run: |
          grep -r "oauth2\|oidc\|mTLS" api/auth/ || {
            echo "No authentication mechanism detected"
            exit 1
          }

  architecture-gate:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/staging'
    needs: security-gate
    steps:
      - uses: actions/checkout@v3
      - name: OpenAPI Validation
        run: |
          npm install @stoplight/spectral-cli
          spectral lint api/openapi.yaml --ruleset .spectral.json
      - name: Rate Limiting Config Check
        run: |
          python scripts/check_rate_limits.py
      - name: Logging Configuration Audit
        run: |
          grep -r "json\|correlation_id\|request_id" api/logging/ || {
            echo "JSON structured logging not detected"
            exit 1
          }

  compliance-gate:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: architecture-gate
    steps:
      - uses: actions/checkout@v3
      - name: Secrets Encryption Audit
        run: |
          python scripts/audit_secrets.py --vault HashiCorp
      - name: mTLS Certificate Validation
        run: |
          openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt certificates/*.crt
      - name: GDPR/CCPA Capability Assessment
        run: |
          python scripts/gdpr_ccpa_audit.py api/
      - name: Comment on PR
        if: always()
        uses: actions/github-script@v6
        with:
          script: |
            const status = '${{ job.status }}'
            if (status === 'failure') {
              github.rest.issues.createComment({
                issue_number: context.issue.number,
                owner: context.repo.owner,
                repo: context.repo.repo,
                body: '⚠️ **Compliance Gate Failed**: A mandatory control is missing. Contact API Governance team.'
              })
            }
```

## Exception Process

### When Exceptions Are Permitted

1. **Documented Risk:** Business case explains why control cannot be implemented immediately
2. **Scoped to Time:** Remediation date set; exception auto-expires
3. **Approved Dual Authority:** Both engineering and security leadership sign off
4. **Audit-Track Enabled:** All production traffic logged and monitored during exception period

### Exception Approval Workflow

| Step | Actor               | Action                                                           | Artifact                   | Duration        |
| ---- | ------------------- | ---------------------------------------------------------------- | -------------------------- | --------------- |
| 1    | PR Author           | Submit exception request with business justification             | `EXCEPTION.md` in PR       | N/A             |
| 2    | API Governance Lead | Verify exception scope; confirm no sensitive data affected       | Automated checklist review | ≤ 4 hours       |
| 3    | VP Security         | Risk assessment; set monitoring requirements                     | Signed exception memo      | ≤ 24 hours      |
| 4    | VP Engineering      | Deployment authorization; confirm remediation plan               | Engineering sign-off       | ≤ 24 hours      |
| 5    | Audit System        | Auto-monitor exception until expiry; escalate if deadline missed | Dashboard tracking         | Until exp. date |

### Exception Template

```markdown
## Exception Request: [Control Name]

**Requested By:** [Engineer Name]
**Affected API:** [API Endpoint]
**Control:** [MANDATORY/RECOMMENDED control]

**Business Justification:**
[Explain why control cannot be implemented; estimate effort required]

**Risk Assessment:**

- Sensitive data affected: [YES/NO]
- Customer-facing: [YES/NO]
- Revenue impact: [Description]

**Monitoring Plan:** [How will we observe adverse effects during exception?]

**Remediation Plan:** Complete by [DATE - max 30 days for MANDATORY]

**Approvals:**

- VP Security: **\_** Date: **\_**
- VP Engineering: **\_** Date: **\_**
```

## Audit Evidence Requirements

### What Auditors Require

| Control              | Audit Question                                | Evidence Type                         | Retention |
| -------------------- | --------------------------------------------- | ------------------------------------- | --------- |
| **Authentication**   | Is every API call authenticated?              | Gateway logs, token validation traces | 90 days   |
| **Authorization**    | Can users access only their own data?         | RBAC policy file, access control logs | 90 days   |
| **Versioning**       | Do deprecated APIs have sunset dates?         | versioning.yaml, API changelog        | Permanent |
| **Input Validation** | Are all inputs validated before processing?   | Schema definitions, SAST reports      | 30 days   |
| **Rate Limiting**    | Are quotas enforced per client?               | Rate limit config, traffic logs       | 90 days   |
| **Logging**          | Are all requests logged with correlation IDs? | Structured log samples, JSON schema   | 90 days   |
| **Webhook Security** | Do webhooks verify authenticity?              | HMAC validation code, test results    | 30 days   |
| **Documentation**    | Is API specification machine-readable?        | OpenAPI spec, spec validation reports | Permanent |

### Evidence Collection Automation

```bash
#!/bin/bash
# Collect audit evidence for API governance compliance

AUDIT_REPORT="API_AUDIT_EVIDENCE_$(date +%Y%m%d).tar.gz"

# Authentication evidence
find api/auth -name "*.json" -o -name "*.yaml" | \
  tar czf /tmp/auth_evidence.tar.gz -T -

# Authorization RBAC
grep -r "roles:\|permissions:" api/ > /tmp/rbac_audit.txt

# Versioning strategy
git log --oneline --all -- api/versioning.md > /tmp/version_history.txt

# Rate limiting configuration
find . -name "*rate*" -o -name "*quota*" | \
  tar czf /tmp/rate_limit_evidence.tar.gz -T -

# Structured logging samples (last 1000 requests)
kubectl logs -n api-production deployment/api-gateway --tail=1000 > /tmp/logging_samples.json

echo "Audit evidence collected to $AUDIT_REPORT"
```

## Control Mapping

| EATGF Control ID      | ISO 27001:2022 | NIST SSDF | OWASP Category              | COBIT 2019 |
| --------------------- | -------------- | --------- | --------------------------- | ---------- |
| SDLC-API-AUTH-01      | A.8.2          | PS.2      | API2 (Broken Auth)          | EDM03      |
| SDLC-API-AUTHZ-01     | A.8.2, A.8.5   | PW.4      | API1 (Broken OLBA)          | DSS05      |
| SDLC-API-VERSION-01   | A.8.31         | PO.3      | API7 (Misconfiguration)     | BAI07      |
| SDLC-API-INPUT-01     | A.8.22         | PW.5      | API3 (Broken PLBA)          | DSS06      |
| SDLC-API-RATELIMIT-01 | A.8.30         | RV.1      | API4 (Resource Consumption) | DSS02      |
| SDLC-API-LOGGING-01   | A.8.15, A.8.16 | RV.2      | N/A                         | MEA02      |
| SDLC-API-WEBHOOK-01   | A.8.28         | PW.4      | API6 (Weak Access Control)  | DSS05      |
| SDLC-API-DOCS-01      | A.8.29         | PO.5      | API9 (Weak Inventory)       | MEA01      |

## Developer Checklist

Before submitting API for enforcement gates:

- [ ] **Security Gate:** Secrets scan passed; no hardcoded credentials
- [ ] **Security Gate:** Input validation schema defined (JSON Schema, Pydantic, OpenAPI)
- [ ] **Security Gate:** Authentication mechanism selected (OAuth2/OIDC/mTLS/API key)
- [ ] **Security Gate:** SAST tools (Bandit, CodeQL) executed; no HIGH severity findings
- [ ] **Architecture Gate:** Authorization model documented (resource ownership checks, tenant boundaries)
- [ ] **Architecture Gate:** Rate limiting tiers configured per organization profile
- [ ] **Architecture Gate:** API versioning strategy defined and implemented (/v1/, header, or compatible)
- [ ] **Architecture Gate:** OpenAPI 3.0+ specification complete and validated
- [ ] **Compliance Gate:** Webhook security HMAC + timestamp validation implemented (if applicable)
- [ ] **Compliance Gate:** Structured JSON logging configured with correlation/request IDs
- [ ] **Compliance Gate:** Sensitive data classification documented (PII, PHI, payment card, regulated)
- [ ] **Compliance Gate:** Data residency constraints declared (geographic, sovereignty)

## Governance Implications

### Risk If Not Enforced

- **Security:** Non-compliant APIs expose authentication/authorization bypasses to production (OWASP API1, API2)
- **Operational:** API sprawl without versioning creates downstream breakage for mobile/SaaS clients
- **Audit:** Cannot demonstrate control compliance to external auditors; SOC 2, ISO 27001 certification at risk
- **Compliance:** Unversioned rate-limit violate SLA commitments; customer billing disputes
- **Data:** Unlogged API traffic prevents incident investigation; GDPR/CCPA breach response compromised

### Operational Impact

- **Developers:** 24–48 hour delays if gates block production deployment; emphasis on pre-merge compliance checks
- **Security Team:** Reduction in run-time incident response; shift-left enables proactive detection
- **Compliance/Audit:** Automated evidence collection reduces manual audit cycles from quarterly to monthly
- **Operations:** Rate limiting gates prevent unintended resource exhaustion during traffic spikes

### Audit Consequences

- **Certification:** ISO 27001, SOC 2 Type II, PCI-DSS require documented API access controls; gates provide defensible evidence
- **Regulatory:** GDPR/CCPA audits require logging evidence; structured JSON logging fulfills data processing audit trail
- **Forensics:** Correlation IDs enable attack reconstruction; compliance gates ensure capability exists before incident
- **Trends:** Repeated exceptions flag systemic governance gaps requiring policy review

### Cross-Team Dependencies

- **API Governance + Platform Engineering:** Platform team provides CI/CD integration; API team maintains standard definitions
- **Security + Engineering:** Joint approval on RED-level escalations; enables rapid security-aware deployment
- **Compliance + Operations:** Compliance defines logging/retention; Operations implements monitoring infrastructure
- **Product + API Governance:** Product sets organizational profile (Startup vs. Enterprise); governance maps to enforcement gates

## Official References

- **EATGF Foundation:** `eatgf-framework/00_FOUNDATION/MASTER_CONTROL_MATRIX.md`
- **Root Authority:** `API_GOVERNANCE_STANDARD.md`
- **Framework Alignment:** `API_CONTROL_MAPPING_APPENDIX.md`
- **ISO 27001:2022:** Annex A, Section A.8 (Implementation of cryptography, A.8.15–A.8.31)
- **NIST SP 800-218:** PW.2 (Protect secrets), PW.4 (Perform secure SDLC practices), PW.5 (Implement secure coding)
- **OWASP API Top 10 2023:** API1–API10 with API governance mappings

## Version Information

| Element               | Value                                                                             |
| --------------------- | --------------------------------------------------------------------------------- |
| **Document Version**  | 2.0 (Refined Operational)                                                         |
| **Change Type**       | Major (enforcement gateway logic + escalation procedures)                         |
| **Issue Date**        | 2024-Q1                                                                           |
| **Supersedes**        | API_ENFORCEMENT_MATRIX v1.0                                                       |
| **Relation to EATGF** | Implements EATGF Layer 08, Domain 02; subordinate to API_GOVERNANCE_STANDARD v2.0 |
| **Next Review**       | Q3 2024 (align with organizational profile evolution)                             |
