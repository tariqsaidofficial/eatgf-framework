# Supply Chain Governance Profile

> **Authority Notice:** This profile implements EATGF controls for software supply chain security, artifact provenance, SBOM generation, and Software Supply-chain Levels for Software Artifacts (SLSA) compliance. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW organizations satisfy Secure SDLC (Layer 01), DevSecOps (Layer 03), and Supply Chain Security requirements per ISO 27001 A.8.28 and NIST SSDF PW.4/PW.7.

## Purpose

Define governance controls for end-to-end software supply chain security, including dependency management, artifact integrity, provenance verification, and regulatory compliance to prevent supply chain compromise, malicious dependencies, and unauthorized modifications.

**Applies to:**

- Source code repositories
- Build artifact generation (containers, binaries, wheels, JARs)
- Package publishing and distribution
- Dependency tracking and vulnerability management
- Deployment artifact verification
- Third-party software integration

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME (Primary) + Layer 01 (Secure SDLC) + Layer 03 (DevSecOps)
- **Governance Scope:** Supply Chain Security, Artifact Integrity, Provenance Tracking, Vulnerability Management
- **Control Authority:** Implements controls from MASTER_CONTROL_MATRIX for supply chain security (ISO 27001 A.8.28, NIST SSDF PW.4/PW.7)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

Supply Chain profiles enforce:

- **Dependency scanning:** SCA tools (OWASP Dependency-Check, Snyk, GitHub Dependabot) in CI/CD
- **Source tracking:** Git revision/DAGhashes captured in artifact metadata
- **Code provenance:** Commit signing (GPG/SSO) mandatory before merge
- **Build attestation:** Signed SLSA provenance for each artifact

### Layer 03: DevSecOps Governance

Supply Chain profiles reference:

- **Artifact registry security:** Private registries with access control + encryption
- **CI/CD audit logging:** Complete build-to-deployment pipeline traceability
- **Policy enforcement:** Automated scanning gates for dependencies + SBOM generation
- **Incident response:** Rapid artifact revocation capability on CVE discovery

### Layer 04: Infrastructure Runtime

Supply Chain profiles implement:

- **Runtime verification:** Admit only signed/verified artifacts at deployment time
- **Image verification:** Kubernetes admission controllers validate signatures (Portieris, Kyverno, OPA)
- **Deployment attestation:** Track deployed artifact digest + responsible actor

## Governance Principles

### 1. Single Source of Truth for Dependencies

All dependencies (direct + transitive) tracked centrally with exact versions pinned.

```bash
#  COMPLIANT: Exact versions pinned, lock file committed
# Python: requirements.txt with ==, poetry.lock, or Pipfile.lock
numpy==1.24.3
pandas==2.0.2
requests==2.31.0

# Node.js: package-lock.json committed (not just package.json)
npm ci  # Install exact versions from lock file

# Ruby: Gemfile.lock committed
bundle install --frozen

# Java: maven.lock or build.gradle.lock
maven dependency:resolve -DoutputFile=deps.txt
```

**Violation:** Floating versions in production (numpy>=1.24, @latest) = MANDATORY failure

### 2. Incident Disclosure: Known Vulnerable Dependencies Immediately Remediated

When CVE detected in dependency, MUST be patched within SLA:

- Critical/High: 24 hours
- Medium: 7 days
- Low: 30 days

```bash
# Automated scanning catches new CVEs
dependabot scan  # Alerts on new vuln in deps
snyk test        # Fail CI/CD if HIGH+ CVE detected
pip-audit        # Python dependency audit
npm audit        # Node.js audit
```

### 3. SLSA Compliance: Immutable Build Records & Provenance

Every artifact originates from auditable, reproducible build with cryptographic proof.

**SLSA Levels:**

```
Level 1: Version control + source is version-controlled
Level 2: Signed provenance + build on hosted platform
Level 3: Ephemeral build environment + provenance signed by build service
Level 4: Hermetic builds + reproducible + hardened distributor (not typical for 2026)
```

### 4. Attestation & Verification at Deploy Time

Deployment must verify artifact authenticity before admitting to production.

```bash
# Build time: generate attestation
cosign attest --predicate provenance.json --key cosign.key image:tag

# Deploy time: verify before admit
cosign verify-attestation --key cosign.pub image:tag
kyverno apply policy.yaml  # Pod admission control
```

### 5. Supply Chain Bill of Materials (SBOM)

Comprehensive inventory of all software components, versions, licenses, and known vulnerabilities.

```bash
# Generate SBOM
syft packages docker:myimage:v1.0 -o cyclonedx > sbom.xml
syft packages './app' -o spdx > sbom.spdx.json

# Publish with artifact
cosign attach sbom --sbom sbom.json image:tag

# Distribute in package registry
curl -X POST -H "Content-Type: multipart/form-data" \
  -F "sbom=@sbom.json" \
  https://sbom-repo.example.com/api/upload
```

### 6. Provenance Immutability: Artifacts Cannot Be Rewritten

Once published, artifact digest is permanent. Retagging old versions tracked with timestamp.

```yaml
# Kubernetes deployment spec: immutable reference
spec:
  containers:
    - name: app
      image: gcr.io/prod/app@sha256:abc123def456... # Digest, not tag
      # NOT: image: gcr.io/prod/app:v1.0 (mutable)
```

**Violation:** Pushing new content to existing tag = MANDATORY failure

## Governance Conformance

### Control 1: Dependency Management & SCA

**Root Standard:** NIST SSDF PW.4 (Secure Software Supply Chain)

**Implementation Pattern:**

- Catalog all direct dependencies with exact versions
- Run SCA scanners on every commit + PR
- Block merge if HIGH/CRITICAL CVE detected
- Maintain updated advisories database

**Compliant Example:**

```bash
# .github/workflows/supply-chain.yml
- name: Scan dependencies
  run: |
    pip install pip-audit bandit safety
    pip-audit --desc
    bandit -r .
    safety check -r requirements.txt

# Python: pyproject.toml with locked dependencies
# Node: npm ci --prefer-offline --no-audit (in CI)
# Java: mvn dependency:check -DfailOnWarning

- name: Check for new CVEs
  run: npm audit --severity=moderate
  continue-on-error: false
```

### Control 2: Source Integrity & Commit Verification

**Root Standard:** NIST SSDF PW.7 (Secure Provisioning)

**Implementation Pattern:**

- Enforce signed commits (GPG, SSH keys)
- Require commit verification in branch protection
- Maintain commit audit trail for all changes
- Attribute changes to verified identity

**Compliant Example:**

```bash
# Configure Git to require signatures
git config --global commit.gpgsign true
git config --global tag.gpgsign true

# Generate GPG key
gpg --gen-key
git config --global user.signingkey <keyid>

# Verify commits
git log --verify-signatures

# GitHub branch protection: require signed commits
# Settings → Branches → Require signed commits
```

### Control 3: Build Provenance & SLSA Generation

**Root Standard:** NIST SSDF PW.7 (Secure Provisioning)

**Implementation Pattern:**

- Generate signed provenance for each build artifact
- Include build environment, source revision, builder identity
- Sign provenance with service keychain
- Verify provenance at deployment

**Compliant Example:**

```yaml
# .github/workflows/build.yml - Generate SLSA provenance
- name: Build and sign artifact
  uses: slsa-framework/slsa-github-generator/actions/docker-publish@v1
  with:
    image: gcr.io/prod/appimage:${{ github.sha }}
    registry-username: ${{ secrets.DOCKER_USERNAME }}
    registry-password: ${{ secrets.DOCKER_TOKEN }}

# Output: signed provenance at gcr.io/prod/appimage:$sha.attestation

- name: Publish SBOM
  run: |
    syft packages docker:gcr.io/prod/app:$GITHUB_SHA -o json > sbom.json
    cosign attach sbom --sbom sbom.json gcr.io/prod/app:$GITHUB_SHA
```

### Control 4: SBOM Generation & Distribution

**Root Standard:** ISO 27001 A.8.28 (Supply Chain Management)

**Implementation Pattern:**

- Generate SBOM in CycloneDX or SPDX format
- Include all dependencies (direct + transitive)
- Publish SBOM alongside artifact
- Update SBOM on vulnerability discovery

**Compliant Example:**

```bash
# Generate SBOM from container image
syft packages docker:gcr.io/prod/app:v1.2.3 \
  -o cyclonedx-json > app-v1.2.3.sbom.json

# Generate SBOM from source tree
syft packages './' -o spdx > app-source.sbom.json

# Attach SBOM to container registry
cosign attach sbom --sbom app-v1.2.3.sbom.json \
  gcr.io/prod/app:v1.2.3

# Retrieve SBOM later
cosign download sbom gcr.io/prod/app:v1.2.3
```

### Control 5: Artifact Signing & Verification

**Root Standard:** NIST SSDF PS.2 (Authorization & Access Control)

**Implementation Pattern:**

- Sign all publishable artifacts (containers, binaries, packages)
- Use keyless signing where possible (Sigstore)
- Distribute public keys securely
- Verify signatures before deployment

**Compliant Example:**

```bash
# Install cosign + keyless setup
cosign initialize  # Uses OIDC provider (GitHub, Google, etc)

# Sign container image (keyless)
cosign sign gcr.io/prod/app:v1.2.3

# Sign binary with key
cosign sign --key cosign.key binary.tar.gz

# Verify signature at deployment
cosign verify gcr.io/prod/app:v1.2.3 \
  --certificate-identity https://github.com/org/repo/.github/workflows/build.yml@refs/tags/v1.2.3 \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

# Kubernetes admission policy
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: ConstraintTemplate
metadata:
  name: signedimage
spec:
  crd:
    spec:
      names:
        - Signature
      validation:
        openAPIV3Schema:
          properties:
            publicKey:
              type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        violation[{"msg": msg}] {
          not signed(input.review.object)
          msg := "Image must be signed"
        }
        signed(obj) {
          # Cosign verification logic
        }
```

### Control 6: Transitive Dependency Risk Assessment

**Root Standard:** NIST SSDF PW.4 (Secure Software Supply Chain)

**Implementation Pattern:**

- Track all transitive dependencies (not just direct)
- Assess risk of each dependency (vendor reputation, maintenance, vulnerabilities)
- Block high-risk dependencies or isolate in separate artifact
- Monitor dependency updates for breaking changes

**Compliant Example:**

```bash
# Generate dependency tree with vulns
pip-audit --desc --format json > deps-audit.json
npm ls --depth=all --json | jq . > npm-tree.json

# Analyze transitive risk
safety check -r requirements.txt --json > safety-report.json

# Isolate high-risk dependencies
# Option 1: Use separate build stage (vendor-isolated container)
# Option 2: Fork/mirror risky packages internally

# Monitor for maintainer abandonment
curl https://api.github.com/repos/owner/repo \
  | jq '.updated_at, .pushed_at'  # Last update within 6 months?
```

### Control 7: Incident Response: CVE-Driven Rebuild & Revocation

**Root Standard:** NIST SSDF PW.4 (Rapid Response)

**Implementation Pattern:**

- On CVE discovery in dependency, trigger automatic rebuild
- Re-scan with SCA tools
- If still vulnerable, revoke old artifact from distribution
- Push patched version with new digest

**Compliant Example:**

```bash
# Automated CVE response workflow
# .github/workflows/cve-response.yml

on:
  schedule:
    - cron: '0 * * * *'  # Hourly check for new CVEs
  workflow_dispatch:

jobs:
  cve-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Check for new CVEs
        run: |
          pip install pip-audit
          pip-audit --desc --format json > audit-current.json

          # Compare with last known-good audit
          if diff audit-current.json audit-known-good.json > /dev/null; then
            echo "No new CVEs"
            exit 0
          else
            echo "New CVEs detected!"
            exit 1
          fi

      - name: Trigger rebuild if CVE found
        run: |
          # Trigger rebuild workflow
          gh workflow run build.yml \
            -f reason="automatic-cve-response" \
            -f severity="high"

      - name: Revoke affected artifacts
        run: |
          cosign delete gcr.io/prod/app:v1.0.0 --force
          cosign delete gcr.io/prod/app:v1.0.1 --force
```

### Control 8: Supply Chain Auditability & Forensics

**Root Standard:** ISO 27001 A.8.15 (Monitoring & Logging)

**Implementation Pattern:**

- Log all artifact operations (build, sign, publish, revoke, deploy)
- Maintain immutable audit trail
- Enable forensic analysis on security incidents
- Track builder identity + signing keychain access

**Compliant Example:**

```json
{
  "audit_log_entry": {
    "timestamp": "2026-02-15T10:30:45Z",
    "event": "artifact_build",
    "artifact_id": "sha256:abc123...",
    "artifact_name": "gcr.io/prod/app:v1.2.3",
    "builder_identity": "oidc://https://token.actions.githubusercontent.com:github.com:org:repo",
    "build_trigger": "push:refs/tags/v1.2.3",
    "source_revision": "git:4a7b2c3d9e1f...",
    "signing_key_id": "keyless:cosign",
    "sbom_generated": true,
    "sbom_hash": "sha256:sbom123...",
    "vulnerability_scan": {
      "scanner": "trivy",
      "timestamp": "2026-02-15T10:31:00Z",
      "critical_count": 0,
      "high_count": 2,
      "medium_count": 15
    },
    "attestation_generated": true,
    "attestation_signature": "sig_mocked_...",
    "publication_attempt": {
      "registry": "gcr.io",
      "status": "success",
      "timestamp": "2026-02-15T10:32:00Z"
    },
    "deployment_events": [
      {
        "cluster": "prod-us-east",
        "namespace": "default",
        "timestamp": "2026-02-15T11:00:00Z",
        "verifier": "kyverno-policy",
        "signature_valid": true
      }
    ]
  }
}
```

## SLSA Framework Integration

### SLSA Level 1: Version Control

**Requirements:**

- Source code in version control (Git, GitHub, GitLab)
- Commits have metadata (author, date, message)
- Artifacts traceable to source revision

**Implementation:**

```bash
git log --format=fuller  # Author + verifier
git tag -v v1.2.3        # Signed tags
```

### SLSA Level 2: Hosted Build Platform + Signed Provenance

**Requirements:**

- Build on hosted platform (GitHub Actions, GitLab CI, Google Cloud Build)
- Provenance signed by build service
- Ephemeral build environment

**Implementation:**

```yaml
# .github/workflows/build.yml
- uses: slsa-framework/slsa-github-generator/actions/generator@v1
  with:
    provenance-filename: provenance.json
```

### SLSA Level 3: Hermetic Build + Dependency Pinning

**Requirements:**

- Build environment isolated (no network access except build cache)
- All dependencies pinned (no latest-version fetching)
- Provenance includes full build configuration
- Build service key protected

**Implementation:**

```dockerfile
# Hermetic Dockerfile: all deps pinned
FROM python:3.12@sha256:abc123...
RUN pip install --no-index --find-links /cache numpy==1.24.3
```

### SLSA Level 4: Reproducible Builds

**Requirements:**

- Same source + build config → same artifact digest
- Distributed build verification (multiple builders)
- No secrets in build logs

**Note:** Level 4 rarely achievable in 2026 due to system state complexity. Most organizations target Level 2/3.

## Multi-Tenancy Supply Chain Isolation

### Tenant Artifact Isolation

- Each tenant's artifacts published to isolated registry namespace
- Cross-tenant artifact access returns 403 Forbidden
- Tenant-specific signing keys per environment

```bash
#  COMPLIANT: Tenant-specific registries
gcr.io/tenant-a/app:v1.0  # Tenant A artifacts only
gcr.io/tenant-b/app:v1.0  # Tenant B artifacts only

# RBAC on registry push/pull
gcloud container images add-iam-policy-binding \
  gcr.io/tenant-a/app:v1.0 \
  --member=serviceAccount:tenant-a-ci@project.iam.gserviceaccount.com \
  --role=roles/storage.admin
```

### Transitive Dependency Risk by Tenant

- Assess dependency risk per tenant (not global)
- Tenant-specific vulnerability policies
- Tenant-specific incident response SLA

```yaml
# Tenant-A: conservative (no experimental packages)
policies:
  - name: no-experimental
    source: registry  # Only official registries
    min-stars: 100
    max-age-days: 180
    excluded-licenses: [GPL-3.0]

# Tenant-B: permissive (accepts more risk)
policies:
  - name: flexible
    excluded-licenses: []
    min-stars: 1
```

## CI/CD Integration Gates

### Pre-Build Gate

```bash
- [ ] Dependencies listed in requirements.txt/package.json/Gemfile
- [ ] .lock file present and committed
- [ ] Dependency audit passes (no unpatched vulns > threshold)
- [ ] Source code committed + signed (git verify-commit)
- [ ] version is semantically versioned (v1.2.3)
```

### Pre-Publish Gate

```bash
- [ ] Build artifact scanned (Trivy/Grype) - no CRITICAL findings
- [ ] SBOM generated and valid (CycloneDX/SPDX schema)
- [ ] Artifact digest recorded (immutable reference)
- [ ] Provenance generated and signed
- [ ] All signable artifacts signed (container, binary)
```

### Pre-Deploy Gate

```bash
- [ ] Artifact signature verified before admission
- [ ] SBOM available and documented
- [ ] Provenance chain verified (source → build → artifact)
- [ ] Deployment actor recorded in audit log
- [ ] Cluster admission policy enforces signature check (Kyverno/Portieris)
```

### Post-Deployment Gate

```bash
- [ ] Runtime image matches deployed artifact (no substitution)
- [ ] Audit log captures deployment actor + source
- [ ] CVE scan repeated at deployment (runtime vulneabilities)
- [ ] Active monitoring for configuration drift
```

## Dependency & Supply Chain Governance

### Direct Dependencies

```python
#  COMPLIANT: Explicit, pinned versions
# requirements-prod.txt
Django==4.2.7
PostgreSQL==15.1
requests==2.31.0
boto3==1.28.85

# Lock file committed
# requirements.lock-prod.txt (generated by pip-compile)
```

### Transitive Dependency Management

```bash
# Show all transitive dependencies
pip show numpy  # Includes dependencies
npm ls --depth=all

# Manage transitive vulns
pip-audit --show-deps
npm audit --depth=all
```

### Vendor Risk Assessment

```python
# Evaluate vendor credibility:
# 1. Maintenance frequency: commits > once/month?
# 2. Community size: GitHub stars > threshold?
# 3. Security: Has SECURITY.md? Signs releases?
# 4. License: Acceptable for commercial use?
# 5. CVE history: Responded to disclosures within SLA?
```

## Developer Checklist

Before publishing artifact:

- [ ] **All dependencies from official registries** (PyPI, npm, Maven Central, RubyGems)
- [ ] **requirements.txt/Gemfile/package.json + lock file committed** (exact versions)
- [ ] **SCA scan passes** (pip-audit, npm audit, bundler-audit - no HIGH+ vulns)
- [ ] **Vulnerability scan passes** (Trivy/Grype on container - no CRITICAL findings)
- [ ] **SBOM generated** (syft with CycloneDX or SPDX format)
- [ ] **Artifact tagged with exact version** (v1.2.3, not latest)
- [ ] **Commit signed** (git commit -S)
- [ ] **Tag signed** (git tag -s v1.2.3)
- [ ] **Artifact digest recorded** (immutable sha256 reference)
- [ ] **Provenance generated** (SLSA level 2+ attestation)
- [ ] **Artifact signed** (cosign sign with keyless or key)
- [ ] **SBOM attached to registry** (cosign attach sbom)
- [ ] **Deployment verification policy configured** (Kyverno/Portieris)
- [ ] **Audit log captures builder identity** (GitHub Actions OIDC token)
- [ ] **Incident response tested** (mock CVE revocation)

**Deployment blocked if any MANDATORY item fails.**

## Control Mapping

| EATGF Control          | ISO 27001:2022 | NIST SSDF | OWASP SAMM | NIST 800-53 | COBIT 2019 |
| ---------------------- | -------------- | --------- | ---------- | ----------- | ---------- |
| Dependency Management  | A.8.28         | PW.4      | Build.1    | SI-4        | BAI09      |
| Source Integrity       | A.8.5          | PW.7      | Source.1   | IA-4        | APO13      |
| Build Provenance       | A.8.24         | PW.7      | Build.3    | CM-8        | BAI10      |
| SBOM Generation        | A.8.28         | PS.1      | Verify.3   | SI-4        | BAI06      |
| Artifact Signing       | A.8.24         | PS.2      | Build.1    | AC-4        | DSS05      |
| Vulnerability Tracking | A.8.15         | RV.1      | Verify.2   | CA-7        | MEA01      |
| Incident Response      | A.8.16         | RV.2      | Verify.1   | IR-1        | MEA03      |
| Auditability           | A.8.15         | RV.1      | Verify.1   | AU-2        | MEA01      |

## Governance Implications

### If Not Implemented

**Untracked Malicious Dependencies:**

- Risk: npm package with 10 million downloads contains backdoor
- Impact: RCE deployed to production via transitive dependency
- Audit finding: ISO 27001 A.8.28 (Supply chain management) violation

**Build Tampering:**

- Risk: CI/CD artifact replaced after build (artifact substitution attack)
- Impact: Backdoored container deployed to production
- Audit finding: NIST SSDF PW.7 (Secure provisioning) violation

**No Provenance:**

- Risk: Deployment uses unverified artifact (no attestation)
- Impact: Cannot trace incident source; forensics impossible
- Audit finding: ISO 27001 A.8.15 (Logging) violation

**Unmanaged CVE Response:**

- Risk: Known CVE in dependency deployed for months (log4j CVE)
- Impact: Complete system compromise
- Audit finding: NIST SSDF PW.4 (Rapid response) violation

**Transitive Dependency Blind Spot:**

- Risk: Attacker compromises deep transitive dependency (1000+ levels down)
- Impact: Silent compromise across all dependent artifacts
- Audit finding: ISO 27001 A.8.28 + NIST SSDF PW.4 violation

### Operational Impact

- Supply chain incident requires artifact revocation + emergency rebuild
- No SBOM → cannot trace incident blast radius
- No provenance → cannot identify root cause
- No audit trail → compliance audit failure

### Audit Consequences

- **SOC2 CC4.1:** Risk assessment for supply chain compromises
- **ISO 27001 A.8.28:** Supply chain management and security obligation
- **PCI-DSS 6.3.2:** Third-party software review (dependencies)
- **GDPR Article 32:** Security of processing (artifact integrity)

## Official References

- [NIST SP 800-218: Secure Software Development Framework (SSDF)](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [SLSA Framework: Supply-chain Levels for Software Artifacts](https://slsa.dev)
- [ISO/IEC 27001:2022 Annex A.8.28: Supply Chain Management](https://www.iso.org/standard/27001)
- [NIST SP 800-53 Rev 5: SI-4 (Information System Monitoring)](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/publications/detail/sp/800-92/final)
- [Sigstore: Keyless Signing Infrastructure](https://docs.sigstore.dev)
- [Syft: SBOM Generation](https://github.com/anchore/syft)
- [Cosign: Container Signing and Verification](https://docs.sigstore.dev/cosign/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [Snyk: Developer-first dependency security](https://snyk.io)

## Version Information

| Field              | Value                                    |
| ------------------ | ---------------------------------------- |
| **Version**        | 1.0                                      |
| **Release Date**   | 2026-02-15                               |
| **Change Type**    | Major (First Release)                    |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)             |
| **Next Review**    | Q2 2026 (SLSA v1.1 finalization)         |
| **Author**         | EATGF Governance Council                 |
| **Status**         | Ready for Enterprise Deployment          |
| **SLSA Target**    | Level 2 (immediate), Level 3 (12 months) |
| **Audit Scope**    | ISO 27001 + NIST SSDF + PCI-DSS          |
