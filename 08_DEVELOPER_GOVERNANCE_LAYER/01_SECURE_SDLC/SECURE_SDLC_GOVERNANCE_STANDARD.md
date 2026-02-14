# Secure Software Development Lifecycle Governance Standard

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Change Type:** Major  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Domain:** 01_SECURE_SDLC  
**Classification:** Developer Governance Standard  
**Governance Scope:** Standard, Policy, Architecture  
**Control Authority Relationship:** Implements controls from ISO 27001, NIST SSDF, OWASP SAMM, COBIT

---

## Purpose

This standard defines the governance model for Secure Software Development Lifecycle (SDLC) within the EATGF Developer Governance Layer.

It establishes mandatory security controls for enterprise environments and recommended practices for startups and individual developers.

The objective is to integrate security, quality, compliance, and traceability into every phase of software delivery—from planning through retirement.

---

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER

**Domain:** 01_SECURE_SDLC

**Classification:** Developer Governance Standard

**Scope:** All software delivery models—web applications, APIs, SaaS platforms, mobile apps, microservices, containerized workloads

**Control Authority Relationship:** Implements controls from:

- Layer 02_CONTROL_ARCHITECTURE: Secure Development Controls
- Layer 04_POLICY_LAYER: Information Security Policy
- MASTER_CONTROL_MATRIX (Layer 00_FOUNDATION)

**Authority Relationship:**

- This standard operationalizes NIST SSDF (SP 800-218) inside development workflows
- Connects ISO 27001 Annex A controls to engineering practice
- Aligns with OWASP secure development principles
- Supports DevSecOps maturity scaling
- Does NOT replace enterprise governance controls—it operationalizes them at the developer level

---

## Governance Principles

Applicable EATGF Principles:

1. **Security-by-Design:** Security requirements must be defined before coding begins
2. **Shift-Left Enforcement:** Controls must be embedded into pipelines and tooling, not post-deployment
3. **Control-Centric Architecture:** Every control maps to authoritative frameworks (ISO, NIST, OWASP)
4. **Developer-Operational Alignment:** Clear roles, responsibilities, and automation boundaries
5. **Audit Traceability:** All security activities must be auditable and evidence-based
6. **Severity-Based Enforcement:** Controls classified by mandatory, recommended, optional levels
7. **Maturity Scaling:** Framework supports organizations from startup to enterprise

---

## Severity Model

Each requirement is classified by enforcement level:

### MANDATORY

- **Definition:** Required for all production systems. Non-compliance blocks deployment.
- **Applicability:** Enterprise, SaaS platforms, payment/healthcare systems
- **Evidence:** Required in audit trails
- **Exception:** Requires formal exception request and risk acceptance

### RECOMMENDED

- **Definition:** Required for systems handling sensitive data or customer-facing functionality.
- **Applicability:** Startups, mid-market SaaS, open-source projects
- **Evidence:** Compliance tracked but not blocking
- **Exception:** Can be deferred based on risk assessment

### OPTIONAL

- **Definition:** Enhancement for defense-in-depth; implement based on risk profile.
- **Applicability:** Non-critical services, experimental projects
- **Evidence:** Tracked for maturity reporting
- **Exception:** Can be excluded based on risk profile

---

## Applicability Model

Secure SDLC requirements are tiered by organization profile:

| Profile                  | Organization Type                          | Secure SDLC Requirement | Threat Modeling | Artifact Signing | SBOM Mandatory |
| ------------------------ | ------------------------------------------ | ----------------------- | --------------- | ---------------- | -------------- |
| **Enterprise**           | Large organizations, regulated industries  | MANDATORY               | MANDATORY       | MANDATORY        | MANDATORY      |
| **SaaS**                 | Commercial platforms, customer data        | MANDATORY               | MANDATORY       | RECOMMENDED      | MANDATORY      |
| **Startup**              | Early-stage, venture-backed                | RECOMMENDED             | RECOMMENDED     | RECOMMENDED      | RECOMMENDED    |
| **Individual Developer** | Open-source maintainers, personal projects | RECOMMENDED             | OPTIONAL        | OPTIONAL         | OPTIONAL       |

---

## Secure Development Lifecycle – Six-Phase Model

Security governance is enforced across six interconnected phases:

### Phase 1: Planning & Requirements

**Objectives:**

- Identify security requirements before development
- Classify data sensitivity
- Define regulatory constraints

**Key Activities:**

- Create security requirement tickets
- Perform risk classification
- Document compliance impacts

**Severity: MANDATORY**

---

### Phase 2: Design & Threat Modeling

**Objectives:**

- Design systems with security in mind
- Identify threats and attack vectors
- Document security architectures

**Key Activities:**

- Conduct threat modeling (STRIDE/PASTA)
- Design authentication/authorization flows
- Create trust boundary diagrams
- Approve design before implementation

**Severity: MANDATORY**

**Guidance:** See ANNEX_A_THREAT_MODELING_STANDARD.md

---

### Phase 3: Development & Secure Coding

**Objectives:**

- Write secure, testable code
- Prevent common vulnerabilities
- Enforce secure patterns

**Key Activities:**

- Follow language-specific secure coding guidelines
- Implement input validation and output encoding
- Use parameterized queries (prevent SQL injection)
- Externalize secrets (no hard-coded credentials)
- Document architectural security decisions

**Severity: MANDATORY**

**Guidance:** See ANNEX_B_SECURE_CODING_STANDARD.md

---

### Phase 4: CI/CD & Build Pipeline Security

**Objectives:**

- Automate security testing
- Enforce controls through pipelines
- Produce signed, verifiable artifacts

**Key Activities:**

- Integrate SAST (Static Application Security Testing)
- Run dependency scanning (SCA)
- Scan container images for vulnerabilities
- Sign release artifacts
- Generate SBOM (Software Bill of Materials)

**Severity: MANDATORY**

**Guidance:** See ANNEX_C_SECURE_PIPELINE_STANDARD.md

---

### Phase 5: Testing & Verification

**Objectives:**

- Verify security controls function correctly
- Discover vulnerabilities before production
- Document test coverage

**Key Activities:**

- Execute dynamic security testing (DAST)
- Perform fuzz testing on API inputs
- Conduct security code review
- Validate authentication/authorization
- Execute penetration testing for critical systems

**Severity: MANDATORY**

**Guidance:** See ANNEX_F_SECURITY_TESTING_STANDARD.md

---

### Phase 6: Deployment & Runtime Security

**Objectives:**

- Deploy securely to production
- Protect runtime environment
- Enable security monitoring

**Key Activities:**

- Isolate production infrastructure
- Manage secrets with vault/managed services
- Enable comprehensive logging
- Configure security monitoring and alerts
- Implement runtime threat protection

**Severity: MANDATORY**

**Guidance:** See ANNEX_E_RUNTIME_SECURITY_STANDARD.md

---

## Technical Implementation – Core Controls

### Control 1: Security Requirements Integration

**Severity:** MANDATORY

**Requirement:**
Security requirements must be captured as first-class backlog items in planning phase.

**Developer Actions:**

- Create security requirement tickets with control references
- Include acceptance criteria for security
- Link to threat model and risk assessment
- Assign security owner (tech lead or security champion)

**Example (Jira Security Requirement):**

```yaml
Type: Story - Security Requirement
Epic: Authentication System Hardening
Title: Enforce TLS 1.3 on all external API endpoints
Severity: High
Control Reference: EATGF-DEV-SDLC-SEC-001
Description: >
  Implement TLS 1.3 enforcement across all public-facing API endpoints
  to prevent downgrade attacks and ensure modern cryptographic standards.

Acceptance Criteria:
  - TLS 1.3 configured as minimum version
  - TLS 1.0, 1.1, 1.2 disabled in production
  - Certificate rotation automated quarterly
  - Compliance audit shows 100% TLS 1.3 adoption

Security Acceptance:
  - NIST SP 800-52 compliance verified
  - OWASP ASVS V6.1.1 satisfied
  - Penetration testing confirms configuration
```

---

### Control 2: CI/CD Security Gate Implementation

**Severity:** MANDATORY

**Requirement:**
All code repositories must have automated security scanning in CI/CD pipelines.

**Developer Actions:**

- Integrate SAST (Static Application Security Testing)
- Run Software Composition Analysis (SCA) on dependencies
- Scan container images for vulnerabilities
- Block builds with critical vulnerabilities
- Generate and retain scan reports for audit

**CI/CD Pipeline Example (GitHub Actions):**

```yaml
name: Secure-SDLC-Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  security-checks:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # SAST: Static Application Security Testing
      - name: Run Bandit (Python SAST)
        run: |
          pip install bandit[sarif]
          bandit -r . -f sarif -o bandit-report.sarif

      # Upload SAST results
      - name: Upload Bandit Results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: bandit-report.sarif

      # SCA: Software Composition Analysis
      - name: Run Trivy (Dependency Scanning)
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: "fs"
          scan-ref: "."
          exit-code: "1"
          severity: "CRITICAL,HIGH"
          format: "sarif"
          output: "trivy-results.sarif"

      # SBOM generation
      - name: Generate SBOM (CycloneDX)
        run: |
          pip install cyclonedx-bom
          cyclonedx-bom -o sbom.xml

      # Upload SBOM as artifact
      - name: Upload SBOM
        uses: actions/upload-artifact@v3
        with:
          name: sbom
          path: sbom.xml

      # Enforce: Block if critical vulnerabilities
      - name: Security Gate - Fail on Critical
        run: |
          if grep -q "CRITICAL" trivy-results.sarif; then
            echo "CRITICAL vulnerabilities detected. Build blocked."
            exit 1
          fi

  code-review-gate:
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'

    steps:
      - name: Require Code Review
        run: |
          echo "Pull request requires minimum 1 approval before merge"
          # GitHub branch protection will enforce this
```

---

### Control 3: Threat Modeling Execution

**Severity:** MANDATORY

**Requirement:**
Threat models must exist for new services, major rewrites, and systems handling sensitive data.

**Developer Actions:**

- Use STRIDE or PASTA methodology
- Identify threats, vulnerabilities, and mitigations
- Document trust boundaries and data flows
- Review and approve threat model before implementation
- Update threat model on significant architectural changes

**Threat Modeling Governance:**

Threat model is MANDATORY for:

- Public APIs and web services
- Payment processing systems
- Authentication/authorization systems
- Systems processing PII (Personally Identifiable Information)
- AI/ML models handling sensitive data

Threat model is RECOMMENDED for:

- Internal services handling business-critical data
- Microservices with cross-service communication

**Guidance:** See ANNEX_A_THREAT_MODELING_STANDARD.md

---

### Control 4: Secure Code Review Enforcement

**Severity:** MANDATORY

**Requirement:**
No code merges to production without peer review and approval.

**Developer Actions:**

- Enable branch protection on main/stable branches
- Require minimum 1 independent reviewer for general code
- Require 2 reviewers for security-sensitive changes:
  - Authentication/authorization logic
  - Cryptographic implementations
  - Database access layers
  - Secrets handling
- Require signed commits (GPG or SSH)
- Pull requests must reference related issue/requirement

**Review Checklist:**

Reviewers must verify:

- [ ] Secure coding practices followed (no SQL injection, XSS, etc.)
- [ ] Input validation present on all external inputs
- [ ] Secrets not hard-coded
- [ ] Error handling doesn't leak sensitive information
- [ ] No new dependencies without security review
- [ ] Test coverage adequate for security-critical paths
- [ ] Logging and monitoring configured

**Guidance:** See CODE_REVIEW_GOVERNANCE_STANDARD.md (existing)

---

### Control 5: Dependency & Supply Chain Security

**Severity:** MANDATORY

**Requirement:**
All software dependencies must be inventoried, scanned, and kept current.

**Developer Actions:**

- Run SCA (Software Composition Analysis) on every build
- Block builds with critical or high-severity vulnerabilities
- Maintain Software Bill of Materials (SBOM) for all releases
- Subscribe to security advisories for all dependencies
- Patch critical vulnerabilities within 7 days
- Patch high-severity vulnerabilities within 30 days
- Document remediation in issue tracker

**Dependency Scanning Example (Python):**

```bash
# Install auditing tools
pip install pip-audit safety
pip install cyclonedx-bom

# Audit dependencies
pip-audit --desc

# Generate SBOM
cyclonedx-bom -o dependencies.xml

# Review and remediate
pip install --upgrade vulnerable-package==secure-version
```

**Guidance:** See ANNEX_D_SUPPLY_CHAIN_SECURITY_STANDARD.md

---

### Control 6: Secrets Management & Externalization

**Severity:** MANDATORY

**Requirement:**
Secrets (API keys, database credentials, certificates) must never be hard-coded. All secrets must be externalized.

**Developer Actions:**

- Use secret vaults (HashiCorp Vault, AWS Secrets Manager, Azure KeyVault, 1Password)
- Load secrets from environment variables or secret management service
- Pre-commit hooks to scan for committed secrets
- Rotate secrets on regular basis (minimum quarterly)
- Audit all secret access

**Secrets Anti-Patterns (Never Do This):**

```python
# WRONG: Hard-coded API key
API_KEY = "sk-1234567890abcdef"

# WRONG: Committed to git
config = {
    "db_password": "production_password_123"
}

# WRONG: In environment file committed to git
DATABASE_PASSWORD=secret123
```

**Correct Pattern:**

```python
# CORRECT: Load from environment (injected at runtime)
import os

API_KEY = os.environ.get('API_KEY')
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD')

if not API_KEY:
    raise ValueError("API_KEY environment variable not set")

# CORRECT: Use Pydantic for validation
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    db_password: str

    class Config:
        env_file = ".env.local"  # Never commit .env files

settings = Settings()
```

**Pre-commit Hook (Prevent Secret Commits):**

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Scanning for secrets..."
truffleHog filesystem . --json --fail > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Secrets detected! Commit aborted."
    exit 1
fi
```

**Guidance:** See ANNEX_G_SECRETS_MANAGEMENT_STANDARD.md

---

### Control 7: Logging & Monitoring for Security

**Severity:** MANDATORY

**Requirement:**
Security-relevant events must be logged and monitored.

**Developer Actions:**

- Log all authentication/authorization failures
- Log all data access/modifications involving sensitive data
- Include context (user ID, timestamp, action, result, source IP)
- Forward logs to centralized SIEM/aggregation service
- Configure alerts for critical security events
- Retain logs for minimum 90 days

**Security Logging Example (Python):**

```python
import logging
import json
from datetime import datetime
from functools import wraps

logger = logging.getLogger("security_events")

def log_security_event(event_type: str, user_id: str, action: str,
                       result: str, details: dict = None, severity: str = "WARNING"):
    """Log security-relevant events with structured formatting"""
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "user_id": user_id,
        "action": action,
        "result": result,
        "severity": severity,
        "details": details or {}
    }
    log_level = getattr(logging, severity.upper(), logging.WARNING)
    logger.log(log_level, json.dumps(event))

# Usage: Authentication failure
log_security_event(
    event_type="authentication_failure",
    user_id="user123",
    action="login_attempt",
    result="failed",
    severity="WARNING",
    details={
        "reason": "invalid_password",
        "ip_address": "192.168.1.1",
        "attempt_count": 3
    }
)

# Usage: Sensitive data access
log_security_event(
    event_type="data_access",
    user_id="admin456",
    action="export_pii",
    result="success",
    severity="CRITICAL",
    details={
        "resource": "customers_table",
        "record_count": 10000,
        "export_format": "csv"
    }
)
```

**Guidance:** See ANNEX_E_RUNTIME_SECURITY_STANDARD.md

---

### Control 8: Release Artifact Integrity

**Severity:** RECOMMENDED

**Requirement:**
Production artifacts must be signed, versioned, and verifiable.

**Developer Actions:**

- Sign all release artifacts with organizational signing key
- Generate SBOM in SPDX or CycloneDX format
- Tag releases with semantic version and commit hash
- Maintain artifact metadata (builder identity, build timestamp)
- Store artifacts in secure, audited repository

**Release Process Example:**

```bash
#!/bin/bash
# Build and sign release artifact

VERSION="1.0.0"
COMMIT_HASH=$(git rev-parse --short HEAD)

# Build application
npm run build

# Generate SBOM
cyclonedx-npm -o sbom.xml

# Create release archive
tar -czf app-${VERSION}-${COMMIT_HASH}.tar.gz dist/ sbom.xml

# Sign artifact
gpg --sign --armor app-${VERSION}-${COMMIT_HASH}.tar.gz

# Upload to secure repository
aws s3 cp app-${VERSION}-${COMMIT_HASH}.tar.gz.asc \
  s3://secure-releases/app/ \
  --sse AES256

echo "Release ${VERSION} signed and published"
```

---

## Framework Profiles

Framework Profiles define Secure SDLC requirements specific to each technology stack.

Each profile includes:

- Required security controls
- Secure configuration guidance
- Recommended tools and integrations
- Common misconfigurations and anti-patterns
- Production-ready CI/CD snippets
- Runtime hardening notes

### Available Profiles:

| Profile               | Type                    | Status         |
| --------------------- | ----------------------- | -------------- |
| PYTHON_PROFILE.md     | Backend                 | In Development |
| DJANGO_PROFILE.md     | Web Framework           | In Development |
| FASTAPI_PROFILE.md    | Web Framework           | In Development |
| NODE_PROFILE.md       | Backend Runtime         | In Development |
| REACT_PROFILE.md      | Frontend Framework      | In Development |
| NEXTJS_PROFILE.md     | Full-Stack Framework    | In Development |
| DOCKER_K8S_PROFILE.md | Container/Orchestration | In Development |

**See:** FRAMEWORK_PROFILES/ directory

---

## Maturity Model

Secure SDLC maturity is measured across 5 levels. Organizations can be at different maturity levels for different controls.

### Level 1: Ad Hoc

**Characteristics:**

- Manual, inconsistent security enforcement
- No automated controls
- Security reviews are reactive, not preventive
- Vulnerabilities discovered in production

**Controls:**

- Manual code review (optional)
- Sporadic dependency checking
- No threat modeling
- Minimal logging

**Tools:** None required; manual processes

---

### Level 2: Defined

**Characteristics:**

- Security standards documented
- Processes partially automated
- Threat models exist for critical systems
- Security reviews before release

**Controls:**

- Code review required before merge
- SAST tools integrated in CI (not blocking)
- Dependency scanning available
- Threat modeling documented
- Security requirements tracked

**Tools:**

- Bandit (Python SAST)
- npm audit / pip-audit
- GitHub branch protection
- Jira for issue tracking

---

### Level 3: Managed

**Characteristics:**

- Automated security controls in CI/CD
- Compliance enforcement via pipelines
- Security outcomes measured and tracked
- Vulnerabilities discovered before production

**Controls:**

- SAST/DAST integrated and blocking
- Dependency scanning with policy enforcement
- Threat modeling required for new services
- Code review with security focus
- Signed commits and releases
- SBOM generated for all releases
- Vulnerability response SLAs defined

**Tools:**

- SonarQube or CodeQL (SAST)
- Trivy (dependency scanning)
- OWASP ZAP (DAST)
- HashiCorp Vault (secrets)
- Artifact signing infrastructure

---

### Level 4: Integrated

**Characteristics:**

- Security metrics integrated into governance reporting
- Risk-based prioritization of controls
- Automated remediation for common issues
- Runtime security monitoring

**Controls:**

- All Level 3 controls plus:
- Runtime threat protection
- Centralized logging and SIEM integration
- Security metrics dashboard for leadership
- Automated dependency updates (with testing)
- Policy-as-code for security configuration

**Tools:**

- Falco (runtime security)
- Splunk / ELK Stack (SIEM)
- Datadog / New Relic (monitoring)
- Dependabot / Renovate (automated updates)
- HashiCorp Sentinel (policy-as-code)

---

### Level 5: Optimized

**Characteristics:**

- Continuous improvement driven by risk data
- Proactive threat hunting and red teaming
- AI-powered vulnerability prediction
- Security embedded in organizational culture

**Controls:**

- All Level 4 controls plus:
- Regular penetration testing and red team exercises
- Threat modeling updated continuously
- ML-based anomaly detection
- Security training and awareness program
- Bug bounty program
- Regular security architecture reviews

**Tools:**

- Custom threat intel integration
- Advanced SOAR (Security Orchestration, Automation, Response)
- ML-based security analytics
- Internal red team tools

---

## Control Mapping

| EATGF Context         | ISO 27001:2022 | NIST SSDF  | OWASP SAMM                    | COBIT 2019 | NIST 800-53 |
| --------------------- | -------------- | ---------- | ----------------------------- | ---------- | ----------- |
| Security Requirements | A.8.1, A.8.28  | PW.1       | Governance-Strategy           | BAI03.01   | SA-3        |
| Threat Modeling       | A.8.25         | PO.1       | Design-Threat Assessment      | BAI03.05   | SA-11       |
| Secure Coding         | A.8.28, A.8.29 | PS.2, PO.2 | Implementation-Code Review    | BAI06.01   | SA-11       |
| Code Review           | A.8.28, A.8.29 | PS.1, PO.4 | Implementation-Code Review    | BAI03.10   | SA-3        |
| SAST/Dependency       | A.8.31         | PO.3, RV.1 | Verification-Security Testing | BAI06.01   | SA-11       |
| Supply Chain          | A.8.31         | RV.1       | Governance-Threat Model       | DSS06.01   | SA-12       |
| Secrets Management    | A.8.2, A.8.3   | PS.3, PS.2 | Implementation-Configuration  | BAI02.01   | IA-4, SC-7  |
| Logging/Monitoring    | A.8.15, A.8.16 | RV.1, RV.2 | Verification-Security Testing | DSS01.03   | AU-12       |
| Artifact Integrity    | A.8.32         | PO.2       | Release-Build                 | BAI01.03   | CA-7        |

---

## Developer Checklist

### Pre-Development

- [ ] Security requirements captured in backlog
- [ ] Risk classification assigned
- [ ] Compliance impact assessed
- [ ] Data sensitivity classification defined

### Design Phase

- [ ] Threat model created and approved
- [ ] Trust boundaries documented
- [ ] Authentication/authorization flows designed
- [ ] Architecture security review completed
- [ ] Encryption requirements defined

### Development Phase

- [ ] Secure coding standard followed
- [ ] No hard-coded secrets or credentials
- [ ] Input validation implemented on all external inputs
- [ ] Output encoding applied to prevent injection
- [ ] Parameterized queries used (all database access)
- [ ] Error handling doesn't leak sensitive data
- [ ] Logging configured for security events

### Code Review Phase

- [ ] Minimum 1 independent reviewer assigned
- [ ] Security checklist items verified
- [ ] No new high-risk dependencies introduced
- [ ] Secrets management verified
- [ ] Testing coverage adequate

### CI/CD Phase

- [ ] SAST scan passes with no critical issues
- [ ] Dependency scanning passes
- [ ] Container image scan passes (if applicable)
- [ ] Build artifacts signed
- [ ] SBOM generated and retained

### Testing Phase

- [ ] Dynamic security testing completed
- [ ] Fuzz testing on public APIs
- [ ] Authentication/authorization tested
- [ ] Injection vulnerabilities tested
- [ ] Penetration testing completed (critical systems)

### Deployment Phase

- [ ] Production environment isolated
- [ ] Secrets stored in vault (not in code/config)
- [ ] Secrets rotated according to policy
- [ ] Logging and monitoring configured
- [ ] Security alerts configured
- [ ] Post-deployment verification completed

---

## Governance Implications

### Risk if not implemented:

- **Vulnerability Introduction:** Exploitable vulnerabilities in production systems
- **Supply Chain Attacks:** Compromised dependencies and transitive vulnerabilities
- **Regulatory Non-Compliance:** Violations of PCI-DSS, SOC 2, HIPAA, GDPR, ISO 27001
- **Data Breaches:** Unauthorized access to customer data and PII
- **Business Impact:** Operational disruption, financial loss, reputation damage

### Operational impact:

- **Early Vulnerability Detection:** Reduces remediation cost by 10-100x vs. post-production discovery
- **Automation:** Reduces manual security review time by 70-80%
- **Time-to-Market:** Clear standards reduce architectural rework
- **Developer Onboarding:** Well-documented standards reduce onboarding from weeks to days
- **Organizational Learning:** Centralized secure coding practices shared across teams

### Audit consequences:

- **Compliance Audits:** NIST SSDF compliance required for government contracts (FedRAMP, etc.)
- **Certification Impact:** ISO 27001, SOC 2, and PCI-DSS audits require evidence of secure SDLC
- **Exception Process:** Non-compliance triggers formal exception request and risk acceptance
- **Regulatory Fines:** Failure to implement baseline controls can result in significant penalties

### Cross-team dependencies:

- **Security Team:** Threat modeling review, security training, policy guidance, incident response
- **Platform/DevOps Team:** CI/CD infrastructure, secret management tooling, container registry
- **Audit Team:** Evidence collection, compliance validation, exception tracking
- **Architecture Team:** Design security review, technology evaluation, standards governance

---

## Authority Hierarchy

If conflict exists, resolution order:

1. **MASTER_CONTROL_MATRIX** (Layer 00_FOUNDATION)
2. **Information Security Policy** (Layer 04_POLICY_LAYER)
3. **Secure SDLC Governance Standard** (this document)
4. **Annex Standards** (A-G)
5. **Framework Profiles**

---

## Exception & Variance Process

**When can an organization NOT follow this standard?**

1. **Risk-Based Exception:** Organization documents risk and accepts in writing
2. **Maturity-Based Variance:** Startup/individual developer may implement Level 1 practices
3. **Regulatory Exemption:** Regulatory body explicitly exempts certain controls

**Exception Request Process:**

1. Engineering lead documents business justification
2. Security team reviews risk impact
3. Risk owner (CTO/CISO) approves in writing
4. Exception recorded in governance repository
5. Exception reviewed quarterly for expiration

---

## Related Documents

**Governance Standards:**

- ENFORCEMENT_MATRIX.md (Enforcement model by organization profile)
- CONTROL_MAPPING_APPENDIX.md (Detailed framework mapping)

**Annex Standards:**

- ANNEX_A_THREAT_MODELING_STANDARD.md
- ANNEX_B_SECURE_CODING_STANDARD.md
- ANNEX_C_SECURE_PIPELINE_STANDARD.md
- ANNEX_D_SUPPLY_CHAIN_SECURITY_STANDARD.md
- ANNEX_E_RUNTIME_SECURITY_STANDARD.md
- ANNEX_F_SECURITY_TESTING_STANDARD.md
- ANNEX_G_SECRETS_MANAGEMENT_STANDARD.md

**Framework Profiles:**

- See FRAMEWORK_PROFILES/ directory

**Legacy References:**

- NIST_SSDF_DEVELOPER_IMPLEMENTATION.md (v1.0, superseded)
- SECURE_CODING_STANDARD.md (now ANNEX_B)
- CODE_REVIEW_GOVERNANCE_STANDARD.md (now part of Phase 3)
- THREAT_MODELING_GUIDELINE.md (now ANNEX_A)

---

## Official References

**Primary Standards:**

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [ISO/IEC 27001:2022 Information Security Management Systems](https://www.iso.org/standard/27001)
- [OWASP Application Security Verification Standard (ASVS) v4.x](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Software Assurance Maturity Model (SAMM)](https://owaspsamm.org/)
- [COBIT 2019 – Governance Framework for Enterprise IT](https://www.isaca.org/resources/frameworks/cobit)
- [NIST SP 800-53 Rev. 5: Security and Privacy Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

**Supplementary References:**

- CWE Top 25 Most Dangerous Software Weaknesses
- OWASP Top 10 Web Application Security Risks
- SANS Top 25 Software Errors
- NIST SP 800-52 Rev. 2: Guidelines for TLS Implementations

---

## Version History

| Version | Date       | Change Type | Description                                                                                                                                                                |
| ------- | ---------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-02-14 | Major       | Authoritative Secure SDLC Governance Standard v1.0; consolidates DevOps governance with maturity model, framework profiles, and pragmatic severity-based enforcement model |
