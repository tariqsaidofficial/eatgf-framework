# Software Bill of Materials (SBOM) Governance Standard

| Field          | Value                                                   |
| -------------- | ------------------------------------------------------- |
| Document Type  | Implementation Standard                                 |
| Version        | 1.0                                                     |
| Classification | Controlled                                              |
| Effective Date | 2026-02-16                                              |
| Authority      | Chief Security Officer and Chief Technology Officer     |
| EATGF Layer    | 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE |
| MCM Reference  | EATGF-DEV-SUP-01                                        |

---

## Purpose

This standard mandates Software Bill of Materials (SBOM) creation, validation, and continuous monitoring for all applications and container images. SBOM provides complete component transparency for vulnerability management, license compliance, and supply chain traceability.

**Mandatory for:** All production applications, container images, and libraries.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

- **Upstream dependency:** NIST SSDF RV.1 (artifact documentation); NTIA minimum elements for SBOM
- **Downstream usage:** SBOM used at deployment for vulnerability scanning, compliance verification, license audit
- **Cross-layer reference:** Maps to supply chain security (03_DEVSECOPS_GOVERNANCE), API governance (02_API_GOVERNANCE) for API SBOM, cloud governance (05_SAAS_AND_CLOUD_GOVERNANCE) for infrastructure SBOMs

## Governance Principles

1. **Transparency by Default** – All components and dependencies documented in standard format
2. **Continuous Generation** – SBOM generated automatically during build; no manual creation
3. **Format Independence** – Support multiple formats (SPDX, CycloneDX, SWID) for tool flexibility
4. **Compliance Alignment** – SBOM complies with NTIA minimum elements and NIST recommendations

## Technical Implementation

### SBOM Standards and Formats

**Recommended Standards:**

| Standard                              | Format            | Use Case                                               | Tool                                |
| ------------------------------------- | ----------------- | ------------------------------------------------------ | ----------------------------------- |
| SPDX (Software Package Data Exchange) | JSON/XML/tagvalue | Industry standard; compliance reporting                | syft, cyclonedx-maven-plugin        |
| CycloneDX                             | JSON/XML          | Container/application focus; vulnerability correlation | syft, trivy, grype                  |
| SWID (Software Identification)        | XML               | Legacy/commercial software; licensing                  | Microsoft SBOM tool                 |
| Package URL (purl)                    | Text              | Dependency reference standard                          | syft, grype, OWASP Dependency-Check |

### SBOM Generation

**Application SBOM (Language-Specific):**

```yaml
# Python application - Syft
syft packages . -o cyclonedx-json > sbom.cyclonedx.json

# JavaScript/Node.js
syft packages . -o spdx-json > sbom.spdx.json
npm ls --all --json > npm-tree.json

# Java (Maven)
cyclonedx:makeBom
# Generates sbom.cyclonedx.xml

# Go (using Syft)
syft ./... -o github-json > sbom.github.json

# Container image
syft ghcr.io/company/app:v1.2.3 -o cyclonedx-json > container-sbom.json
```

**SBOM Required Fields (NTIA Minimum Elements):**

```json
{
  "bom-version": 1,
  "components": [
    {
      "type": "library",
      "name": "express",
      "version": "4.18.2",
      "purl": "pkg:npm/express@4.18.2",
      "licenses": [
        {
          "license": {
            "name": "MIT"
          }
        }
      ],
      "supplier": {
        "name": "npm registry"
      },
      "hashes": [
        {
          "alg": "SHA-256",
          "content": "abc123..."
        }
      ]
    }
  ],
  "metadata": {
    "timestamp": "2024-02-16T15:30:00Z",
    "tools": [
      {
        "vendor": "Syft",
        "name": "syft",
        "version": "0.75.0"
      }
    ]
  }
}
```

### SBOM Storage and Distribution

**SBOM Storage:**

| Artifact             | Storage Location                             | Retention            |
| -------------------- | -------------------------------------------- | -------------------- |
| Container image SBOM | In-toto attestation (inside registry)        | Lifetime of image    |
| Application SBOM     | Artifact repository alongside application    | 7 years minimum      |
| Dependency lockfile  | Git repository                               | Lifetime of release  |
| Library SBOM         | Published with artifact (npm, Maven Central) | Per package lifetime |

**Container Image Example (in-toto attestation):**

```bash
# Generate SBOM and sign as attestation
syft ghcr.io/company/app:v1.2.3 -o cyclonedx-json \
  > sbom.cyclonedx.json

# Create in-toto attestation
cosign attest --predicate sbom.cyclonedx.json \
  --key=hsm://pkcs11/token/key-label \
  ghcr.io/company/app:v1.2.3

# Verify SBOM attestation at deployment
cosign verify-attestation \
  --type=cyclonedx \
  --key=cosign.pub \
  ghcr.io/company/app:v1.2.3
```

**CLI Tool Integration:**

```bash
# Grype: Vulnerability scanner with SBOM generation
grype ghcr.io/company/app:v1.2.3 \
  -o cyclonedx-json \
  --fail-on high

# Trivy: SBOM + vulnerability scanning
trivy image \
  --format cyclonedx \
  --output sbom.cyclonedx.json \
  ghcr.io/company/app:v1.2.3
```

### SBOM Validation

**Validation Checklist:**

```python
def validate_sbom(sbom_path):
    """Verify SBOM completeness and compliance"""
    with open(sbom_path) as f:
        sbom = json.load(f)

    # Check NTIA minimum elements
    assert sbom.get('specVersion'), "Missing specVersion"
    assert sbom.get('version'), "Missing SBOM version"
    assert sbom.get('metadata', {}).get('timestamp'), "Missing timestamp"
    assert sbom.get('metadata', {}).get('tools'), "Missing tool info"

    # Validate components
    for component in sbom.get('components', []):
        assert component.get('name'), "Component missing name"
        assert component.get('version'), "Component missing version"
        assert component.get('purl'), "Component missing purl"

        # Verify hash for integrity
        if not component.get('hashes'):
            warnings.append(f"Component {component['name']} missing hash")

    # Check license information
    for component in sbom.get('components', []):
        if not component.get('licenses'):
            warnings.append(f"Component {component['name']} missing license")

    return True, warnings
```

**SBOM CI/CD Gate:**

```yaml
# GitHub Actions example
- name: Validate SBOM
  run: |
    syft packages . -o cyclonedx-json > sbom.json

    # Verify SBOM valid JSON
    jq . sbom.json > /dev/null || exit 1

    # Count components
    COMPONENTS=$(jq '.components | length' sbom.json)
    echo "SBOM contains $COMPONENTS components"

    # Check for required fields
    jq '.components[] | select(.purl == null)' sbom.json | \
      wc -l | grep -q '^0$' || exit 1

    echo "SBOM validation passed"
```

### SBOM Vulnerability Correlation

**Vulnerability Matching:**

```yaml
# Grype uses SBOM to correlate vulnerabilities
grype sbom:sbom.cyclonedx.json -o table --fail-on high

# Output example:
NAME            VERSION   VULNERABILITY   SEVERITY   EPSS
vulnerable-lib  1.0.0     CVE-2024-1234   High       0.95
```

**Automated Vulnerability Response:**

```python
def handle_sbom_vulnerability(sbom_path, cve_id, severity):
    """Automated response to SBOM vulnerability"""
    sbom = load_sbom(sbom_path)
    affected_component = find_component_by_cve(sbom, cve_id)

    if severity >= 8.0:
        # Critical: immediate remediation
        create_urgent_patch(affected_component)
        notify_team_channels(affected_component, cve_id)
        trigger_emergency_release_planning()

    elif severity >= 5.0:
        # Medium-High: planned update
        create_github_issue(affected_component, cve_id)
        assign_to_team(affected_component)
        set_deadline(30_days)
```

### SBOM Types

**Application SBOM (contains all dependencies):**

Generated during application build for deployment.

```
myapp-1.0.0.sbom.json
├── express (4.18.2)
├── mongoose (6.8.0)
├── async (3.2.4)
├── lodash (4.17.21)
└── ... (100+ dependencies)
```

**Container Image SBOM (OS packages + application dependencies):**

Generated when building container image.

```
app-v1.2.3-container.sbom.json
├── [OS Packages]
│   ├── libc (2.36)
│   ├── openssl (3.0.8)
│   └── ...
├── [Application Dependencies]
│   ├── express (4.18.2)
│   └── ...
```

**Infrastructure SBOM (IaC components):**

For infrastructure-as-code (Terraform, CloudFormation).

```
infrastructure-prod.sbom.json
├── AWS::S3::Bucket (prod-data)
├── AWS::RDS::DBInstance (postgres-prod)
├── AWS::Lambda::Function (async-worker)
└── ...
```

**API SBOM (API dependencies):**

For microservices-based systems.

```
api-gateway-sbom.json
├── [Direct Dependencies]
├── [Backend Services]
│   ├── User Service (v2.1.0)
│   ├── Payment Service (v1.8.0)
│   └── ...
├── [External APIs]
│   ├── Stripe API (v5.0)
│   └── SendGrid API (v5.8)
```

### SBOM Reporting and Monitoring

**Weekly SBOM Report:**

```yaml
metrics:
  - total_sboms_generated: 142
  - sboms_with_vulnerabilities: 28
  - critical_vulnerabilities: 2
  - acknowledged_but_unpatched: 8
  - components_updated_this_week: 12

trending:
  - sbom_generation_compliance: 100%
  - vulnerability_remediation_time: 10 days avg
  - license_compliance_violations: 0
```

**License Audit Report:**

```yaml
licenses_used:
  MIT: 412 components (45%)
  Apache-2.0: 198 components (22%)
  BSD-3-Clause: 154 components (17%)
  ISC: 89 components (10%)
  GPL: 12 components (1.3%) # Flagged for review

prohibited_licenses:
  AGPL: 0
  GPL-3.0: 0
```

## Control Mapping

| EATGF Context          | ISO 27001:2022 | NIST SSDF  | OWASP            | COBIT    |
| ---------------------- | -------------- | ---------- | ---------------- | -------- |
| SBOM generation        | A.8.30, A.8.31 | RV.1, RV.2 | -                | BAI07    |
| Vulnerability tracking | A.8.31         | RV.1.2     | Dependency Check | BAI07.02 |
| License compliance     | A.8.18         | PO.1       | OSS License      | APO07    |

## Developer Checklist

Before implementing SBOM governance:

- [ ] SBOM generation tool selected (Syft, CycloneDX, Trivy)
- [ ] SBOM generation automated in build pipeline
- [ ] SBOM format standardized (CycloneDX recommended)
- [ ] SBOM storage configured (artifact repository)
- [ ] SBOM validation gate implemented in CI/CD
- [ ] Vulnerability correlation configured (Grype/Trivy)
- [ ] License scanning configured with approved/prohibited lists
- [ ] SBOM signing configured (in-toto attestation for containers)
- [ ] Weekly SBOM compliance reporting dashboard created
- [ ] Development team trained on SBOM review

## Governance Implications

**Risk if not implemented:**

- Unknown dependencies = vulnerability blindness
- License violations = legal liability
- Untracked supply chain = undetectable compromise

**Operational impact:**

- SBOM generation adds <1 minute to build
- Vulnerability alerting enables proactive patching
- License tracking prevents compliance violations

**Audit consequences:**

- SBOM required for NIST SSDF compliance
- SBOM demonstrates supply chain control
- Vulnerability tracking = incident investigation evidence

**Cross-team dependencies:**

- Development: SBOM review, dependency updates
- Security: vulnerability monitoring, license policy
- Compliance: license tracking, audit evidence

## Official References

- **NTIA Minimum Elements for SBOM** – NIST/OMB requirement
- **SPDX Standard** – Software Package Data Exchange (spdx.org)
- **CycloneDX** – OWASP component analysis format
- **Trivy Documentation** – Container/artifact scanning
- **NIST SP 800-218** – SSDF PW.4, RV.1-RV.2

## Version History

| Version | Date       | Change Type | Description                                   |
| ------- | ---------- | ----------- | --------------------------------------------- |
| 1.0     | 2026-02-16 | Major       | Initial SBOM governance standard for Layer 08 |
