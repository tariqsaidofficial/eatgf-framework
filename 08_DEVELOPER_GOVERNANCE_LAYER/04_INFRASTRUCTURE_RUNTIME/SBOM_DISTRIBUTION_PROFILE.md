# SBOM Distribution Profile

> **Authority Notice:** This profile implements EATGF controls for Software Bill of Materials (SBOM) generation, publishing, distribution, and consumption. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW organizations satisfy Supply Chain Security (Layer 04), DevSecOps (Layer 03), and compliance requirements per ISO 27001 A.8.28 and CycloneDX/SPDX standards.

## Purpose

Define governance controls for SBOM lifecycle management, ensuring every software artifact is accompanied by a comprehensive, cryptographically signed SBOM that enables supply chain transparency, vulnerability tracking, and compliance audit across the organization.

**Applies to:**

- Container images (OCI/Docker)
- Binary distributions (executables, libraries)
- Package publications (PyPI, npm, Maven Central, RubyGems)
- SaaS application builds
- Third-party dependency inventory
- Compliance reporting (NTIA SBOM mandates)

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME (Primary) + Layer 01 (Secure SDLC) + Layer 03 (DevSecOps)
- **Governance Scope:** SBOM Generation, Format Standardization, Publication, Distribution, Consumption
- **Control Authority:** Implements controls from MASTER_CONTROL_MATRIX for supply chain transparency (ISO 27001 A.8.28, NTIA SBOM Guidelines, CycloneDX/SPDX standards)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

SBOM Distribution profiles enforce:

- **Dependency capture:** All direct + transitive dependencies captured at build time
- **Format compliance:** SBOM generated in approved formats (CycloneDX, SPDX)
- **Metadata inclusion:** License, version, source, vulnerability data included
- **Signature verification:** SBOM signed by builder, verified by consumers

### Layer 03: DevSecOps Governance

SBOM Distribution profiles reference:

- **CI/CD automation:** SBOM generated automatically on every build
- **Registry integration:** SBOM published alongside artifact in registry
- **Scanning integration:** SBOM consumed by vulnerability scanners
- **Audit trail:** SBOM change history tracked with commit/build correlation

### Layer 04: Infrastructure Runtime

SBOM Distribution profiles implement:

- **Deployment verification:** SBOM available before pod admission
- **Runtime scanning:** SBOM used for runtime vulnerability detection
- **Incident forensics:** SBOM enables rapid blast radius assessment

## Governance Principles

### 1. Universal SBOM Generation

Every publishable artifact automatically generates an SBOM at build time.

```bash
# ✅ COMPLIANT: SBOM generated for every artifact
# Build pipeline
docker build -t app:v1.0 .
syft packages docker:app:v1.0 -o cyclonedx-json > sbom.json
syft packages docker:app:v1.0 -o spdx > sbom.spdx.json

# Publish to registry with SBOM attached
docker push app:v1.0
cosign attach sbom --sbom sbom.json app:v1.0
```

**Violation:** No SBOM generated = MANDATORY failure

### 2. Standardized SBOM Formats

SBOM published in industry-standard formats for interoperability.

```json
// ✅ COMPLIANT: CycloneDX format (NTIA-approved)
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "version": 1,
  "metadata": {
    "timestamp": "2026-02-15T10:30:00Z",
    "tools": [
      {
        "vendor": "anchore",
        "name": "syft",
        "version": "0.75.0"
      }
    ],
    "component": {
      "bom-ref": "app-v1.0",
      "type": "application",
      "name": "app",
      "version": "1.0"
    }
  },
  "components": [
    {
      "bom-ref": "pkg:python/requests@2.31.0",
      "type": "library",
      "name": "requests",
      "version": "2.31.0",
      "purl": "pkg:python/requests@2.31.0",
      "licenses": [
        {
          "license": {
            "name": "Apache-2.0"
          }
        }
      ],
      "externalReferences": [
        {
          "type": "security-advisory",
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2023-32681"
        }
      ]
    }
  ]
}
```

**Dual format support:** CycloneDX (security-focused) + SPDX (license-focused)

### 3. SBOM Registry Integration

SBOM published as first-class artifact alongside binary/image.

```bash
# Registry attachment patterns

# OCI Image Registry (Docker Hub, GCR, ECR, etc)
cosign attach sbom --sbom sbom.json gcr.io/prod/app:v1.0
# Retrieved via: cosign download sbom gcr.io/prod/app:v1.0

# Package Registry (PyPI, npm, Maven Central)
curl -X POST https://repo.maven.apache.org/api/sbom \
  -F "sbom=@sbom.json" \
  -F "artifact=com.example:app:1.0"

# OCI Artifact Registry (ORAS)
oras attach app:v1.0 sbom.json:application/vnd.cyclonedx+json
```

### 4. Signed & Verifiable SBOM

SBOM cryptographically signed to prove integrity.

```bash
# ✅ COMPLIANT: SBOM signed with artifact
cosign sign-sbom --sbom sbom.json gcr.io/prod/app:v1.0
cosign verify-sbom gcr.io/prod/app:v1.0 \
  --certificate-identity https://github.com/org/repo/.github/workflows/build.yml \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

### 5. SBOM Context: Build Environment Metadata

SBOM includes full build context for reproducibility.

```json
{
  "metadata": {
    "timestamp": "2026-02-15T10:30:00Z",
    "build": {
      "id": "github-actions-run-123456",
      "system": "GitHub Actions",
      "environment": "ubuntu-latest",
      "trigger": "push:refs/tags/v1.0"
    },
    "source": {
      "vcs": "git",
      "repository": "https://github.com/org/repo",
      "revision": "abc123def456...",
      "branch": "main",
      "tag": "v1.0"
    },
    "builder": {
      "identity": "https://github.com/org/repo",
      "signature_tool": "cosign",
      "signature_algorithm": "ecdsa"
    }
  }
}
```

### 6. SBOM Consumption: Automated Vulnerability Correlation

SBOM consumed by vulnerability scanners for real-time risk assessment.

```bash
# ✅ COMPLIANT: SBOM fed to multiple scanners
cosign download sbom gcr.io/prod/app:v1.0 | \
  grype --file - --output json > vulns.json

# Correlation with NVD/GitHub Security Advisories
cyclonedx-npm generate --output-file sbom.json
cyclonedx validate --input-format json sbom.json
```

## Governance Conformance

### Control 1: SBOM Generation at Build Time

**Root Standard:** ISO 27001 A.8.28 (Supply Chain Management)

**Implementation Pattern:**

- SCA tools (Syft, SPDX Maven Plugin, npm SBOM) integrated into CI/CD
- SBOM generated for every artifact (not optional)
- Both CycloneDX and SPDX formats supported
- SBOM includes all dependencies (direct + transitive)

**Compliant Example:**

```yaml
# .github/workflows/build.yml
- name: Generate SBOM
  run: |
    # Install syft
    curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

    # Generate SBOM for container
    syft packages docker:gcr.io/prod/app:$GITHUB_SHA \
      -o cyclonedx-json > sbom-cyclonedx.json
    syft packages docker:gcr.io/prod/app:$GITHUB_SHA \
      -o spdx > sbom-spdx.spdx.json

    # Validate SBOM format
    cyclonedx validate --exit-code --input-format json sbom-cyclonedx.json

- name: Attach SBOM to Registry
  run: |
    cosign attach sbom --sbom sbom-cyclonedx.json \
      gcr.io/prod/app:$GITHUB_SHA
    cosign attach sbom --sbom sbom-spdx.spdx.json \
      gcr.io/prod/app:$GITHUB_SHA-spdx
```

### Control 2: SBOM Publication & Registry Integration

**Root Standard:** NTIA SBOM Guidelines + CycloneDX/SPDX Standards

**Implementation Pattern:**

- SBOM published as OCI artifact alongside container image
- SBOM discoverable via registry API
- Multiple format support (CycloneDX, SPDX, JSON, XML, YAML)
- SBOM versioning aligned with artifact version

**Compliant Example:**

```bash
# Publish SBOM to multiple registries
# Docker Registry
cosign attach sbom --sbom sbom.json gcr.io/prod/app:v1.0

# OCI Artifact Store
oras attach --artifact-type application/vnd.sbom.v1 \
  gcr.io/prod/app:v1.0 sbom.json

# Package Repository
# Maven
mvn deploy:deploy-file \
  -Dfile=sbom.json \
  -DgroupId=com.example \
  -DartifactId=app \
  -Dversion=1.0 \
  -Dclassifier=sbom \
  -DrepositoryId=central

# npm
npm publish --sbom sbom.json

# Retrieve SBOM from registry
cosign download sbom gcr.io/prod/app:v1.0
oras pull gcr.io/prod/app:v1.0:sbom sbom.json
```

### Control 3: SBOM Signature & Verification

**Root Standard:** NIST SP 800-53 SC-7 (Boundary Protection)

**Implementation Pattern:**

- SBOM signed with same key as artifact
- Signature verifiable at download time
- Keyless signing supported (Sigstore/Cosign)
- Signature timestamp included (Timestamp Authority)

**Compliant Example:**

```bash
# Sign SBOM with artifact
cosign sign-sbom --key cosign.key sbom.json gcr.io/prod/app:v1.0

# Verify SBOM signature
cosign verify-sbom gcr.io/prod/app:v1.0 \
  --key cosign.pub

# Keyless verification (GitHub Actions)
cosign verify-sbom gcr.io/prod/app:v1.0 \
  --certificate-identity https://github.com/org/repo/.github/workflows/build.yml@refs/tags/v1.0 \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

### Control 4: SBOM Consumption for Vulnerability Detection

**Root Standard:** ISO 27001 A.8.8 (Malware Protection)

**Implementation Pattern:**

- SBOM consumed by vulnerability scanners (Grype, Trivy, OSV)
- Automatic correlation with NVD/GitHub Security Advisories
- Vulnerability alerts integrated into incident workflow
- Risk scoring based on SBOM component severity

**Compliant Example:**

```bash
# Download SBOM from registry
cosign download sbom gcr.io/prod/app:v1.0 > sbom.json

# Scan SBOM for vulnerabilities
grype --file sbom.json --output json > vulns.json

# Post-process vulnerability findings
cat vulns.json | jq '.matches[] | select(.vulnerability.severity == "CRITICAL")'

# Trigger incident response on CRITICAL findings
if grep -q '"severity":"CRITICAL"' vulns.json; then
  echo "CRITICAL vulnerabilities found!"
  # Alert security team
  # Trigger automated remediation
  exit 1
fi
```

### Control 5: SBOM Compliance Reporting

**Root Standard:** ISO 27001 A.8.28 + NTIA SBOM Mandate

**Implementation Pattern:**

- SBOM aggregated for organization-wide inventory
- License compliance analysis (GPL, MIT, Apache, etc)
- Regulatory reporting (NTIA, CFAA, Executive Order requirements)
- Audit trail maintained for compliance audits

**Compliant Example:**

```bash
# SBOM Aggregation Query
curl https://registry.gcr.io/v2/prod/app/manifests \
  -H "Authorization: Bearer $TOKEN" | \
  jq -r '.sbom' | \
  > organization-sbom-inventory.json

# License Compliance Report
cat organization-sbom-inventory.json | \
  jq '.components[].licenses[].name' | \
  sort | uniq -c | \
  tee license-report.txt

# NTIA SBOM Requirement Validation
cyclonedx-cli validate --input-format json sbom.json \
  --input-version v1_5 --output report.txt
```

### Control 6: Multi-Tenancy SBOM Isolation

**Root Standard:** ISO 27001 A.8.21 (Access Control)

**Implementation Pattern:**

- Tenant-specific SBOM namespacing in registry
- Cross-tenant SBOM access prevented via IAM
- Tenant-specific vulnerability policies
- Separate audit logs per tenant

**Compliant Example:**

```bash
# Tenant-A SBOM registry path
gcr.io/tenant-a/app:v1.0
# SBOM accessible only to tenant-a-ci service account

# Tenant-B SBOM registry path
gcr.io/tenant-b/app:v1.0
# SBOM accessible only to tenant-b-ci service account

# Registry IAM Policy
gcloud container images add-iam-policy-binding \
  gcr.io/tenant-a/app:sbom \
  --member=serviceAccount:tenant-a-ci@project.iam.gserviceaccount.com \
  --role=roles/storage.objectViewer
```

### Control 7: SBOM Versioning & Change Tracking

**Root Standard:** ISO 27001 A.8.22 (Change Management)

**Implementation Pattern:**

- SBOM version tracked alongside artifact version
- SBOM change history maintained (git commits)
- Detection of component additions/removals
- Audit trail for dependency changes

**Compliant Example:**

```json
{
  "metadata": {
    "version": 2,
    "previous_version": 1,
    "changes": [
      {
        "timestamp": "2026-02-15T10:30:00Z",
        "type": "component_added",
        "component": "pkg:python/numpy@1.24.3",
        "reason": "Feature implementation"
      },
      {
        "timestamp": "2026-02-15T10:35:00Z",
        "type": "component_removed",
        "component": "pkg:python/deprecated-lib@1.0",
        "reason": "CVE remediation"
      },
      {
        "timestamp": "2026-02-15T10:40:00Z",
        "type": "component_updated",
        "component": "pkg:python/requests@2.31.0",
        "from_version": "2.30.0",
        "reason": "Security patch"
      }
    ]
  }
}
```

### Control 8: SBOM Auditability & Forensics

**Root Standard:** ISO 27001 A.8.15 (Monitoring & Logging)

**Implementation Pattern:**

- SBOM access logged (who downloaded, when, from where)
- SBOM modification history tracked
- Builder identity included in SBOM metadata
- Incident forensics enabled via SBOM audit trail

**Compliant Example:**

```json
{
  "audit_log": {
    "sbom_publication": {
      "timestamp": "2026-02-15T10:30:00Z",
      "artifact_id": "gcr.io/prod/app:v1.0",
      "sbom_hash": "sha256:abc123...",
      "publisher_identity": "github-actions-bot",
      "signature_algorithm": "cosign-ecdsa",
      "registry": "gcr.io"
    },
    "sbom_access": [
      {
        "timestamp": "2026-02-15T10:31:00Z",
        "accessor": "security-scanner-bot",
        "action": "download",
        "purpose": "vulnerability_scan",
        "destination": "grype-engine"
      },
      {
        "timestamp": "2026-02-15T10:32:00Z",
        "accessor": "deployment-service",
        "action": "verify",
        "signature_valid": true
      }
    ]
  }
}
```

## CI/CD Integration Gates

### Pre-Build Gate

```bash
- [ ] Dependency list available (requirements.txt, package.json, Gemfile)
- [ ] Lock file generated and committed
- [ ] SCA baseline established (baseline-sbom.json)
```

### Build Gate

```bash
- [ ] SBOM generated automatically (syft/cyclonedx-maven/npm)
- [ ] SBOM format validated (CycloneDX/SPDX schema)
- [ ] SBOM signed with builder key
- [ ] SBOM digest recorded (immutable reference)
```

### Pre-Publish Gate

```bash
- [ ] SBOM signature verified
- [ ] SBOM component count matches artifact dependencies
- [ ] No untracked transitive dependencies
- [ ] License compliance checked (no forbidden licenses)
```

### Deploy Gate

```bash
- [ ] SBOM downloaded and verified at deployment
- [ ] SBOM used by admission controller (Kyverno/OPA)
- [ ] Runtime vulnerability scan triggered
- [ ] Audit log captures SBOM version deployed
```

## Developer Checklist

Before publishing artifact with SBOM:

- [ ] **SBOM generated from artifact build** (syft/cyclonedx auto-detection)
- [ ] **SBOM in CycloneDX format** (v1.5+) for NTIA compliance
- [ ] **SBOM in SPDX format** (v2.3+) for license tracking
- [ ] **All dependencies listed** (direct + transitive, exact versions)
- [ ] **License information included** for each component
- [ ] **Vulnerability references included** (CVE, GHSA, OSV)
- [ ] **Build metadata included** (source revision, builder identity)
- [ ] **SBOM signature generated** (cosign sign-sbom)
- [ ] **SBOM published to registry** (cosign attach sbom)
- [ ] **SBOM discoverable via registry API** (oras pull works)
- [ ] **SBOM validated against schema** (cyclonedx validate)
- [ ] **Change tracking enabled** (SBOM version management)
- [ ] **Audit log captures publication** (who, when, signature)
- [ ] **Consumption enabled** (scanners can download & verify)

**Deployment blocked if any MANDATORY item fails.**

## Control Mapping

| EATGF Control          | ISO 27001:2022 | NIST SSDF | OWASP SAMM | COBIT 2019 |
| ---------------------- | -------------- | --------- | ---------- | ---------- |
| SBOM Generation        | A.8.28         | PW.4      | Build.1    | BAI09      |
| Format Standardization | A.8.28         | PW.4      | Build.1    | BAI06      |
| Registry Integration   | A.8.24         | PS.2      | Build.3    | DSS05      |
| Signature & Verify     | A.8.24         | PS.2      | Build.1    | DSS05      |
| Vulnerability Scan     | A.8.15         | RV.1      | Verify.2   | MEA01      |
| Compliance Reporting   | A.8.28         | RV.1      | Verify.3   | MEA02      |
| Versioning             | A.8.22         | PW.8      | Build.2    | DSS05      |
| Auditability           | A.8.15         | RV.1      | Verify.1   | MEA01      |

## Governance Implications

### If Not Implemented

**Blind Supply Chain:**

- Risk: Cannot identify which components in deployment
- Impact: CVE discovered, cannot assess blast radius
- Audit finding: ISO 27001 A.8.28 (Supply chain) violation

**Unverified Dependencies:**

- Risk: SBOM without signatures, could be manipulated
- Impact: Injected malicious dependency goes undetected
- Audit finding: NIST SSDF PS.2 (Artifact integrity) violation

**License Compliance Failure:**

- Risk: GPL software deployed in proprietary product
- Impact: Legal liability, product recall
- Audit finding: NTIA SBOM mandate violation

**Incident Forensics Impossible:**

- Risk: CVE in transitive dependency, cannot trace impact
- Impact: cannot contain incident, organization-wide compromise
- Audit finding: ISO 27001 A.8.15 (Logging) violation

## Official References

- [NTIA SBOM Examples & Guidance](https://www.cisa.gov/sbom)
- [CycloneDX Specification v1.5](https://cyclonedx.org)
- [SPDX Specification v2.3](https://spdx.dev)
- [ISO/IEC 27001:2022 A.8.28: Supply Chain Management](https://www.iso.org/standard/27001)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [Anchore Syft: SBOM Generation](https://github.com/anchore/syft)
- [Sigstore Cosign: Artifact Signing](https://docs.sigstore.dev/cosign/)

## Version Information

| Field               | Value                             |
| ------------------- | --------------------------------- |
| **Version**         | 1.0                               |
| **Release Date**    | 2026-02-15                        |
| **Change Type**     | Major (First Release)             |
| **EATGF Baseline**  | v1.0 (Phases 12a-b Complete)      |
| **Next Review**     | Q2 2026 (CycloneDX v1.6 release)  |
| **Author**          | EATGF Governance Council          |
| **Status**          | Ready for Enterprise Deployment   |
| **NTIA Compliance** | v1.5 (Immediate), v1.6 (Q2 2026)  |
| **Audit Scope**     | ISO 27001 + NIST SSDF + NTIA SBOM |
