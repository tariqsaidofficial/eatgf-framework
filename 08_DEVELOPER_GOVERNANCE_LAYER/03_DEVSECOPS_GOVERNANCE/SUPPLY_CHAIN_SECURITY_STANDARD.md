# Supply Chain Security Standard

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 03_DEVSECOPS_GOVERNANCE  
**Governance Scope:** Implementation Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

**Governance Scope:** Software supply chain security controls, dependency verification, and build provenance.

**Control Authority Relationship:** Implements:

- Layer 02: Supply Chain Controls
- Layer 04: Information Security Policy
- NIST SSDF PO.3 (Protect code integrity), SLSA Framework

## Purpose

This standard defines security controls for the software supply chain to prevent:

- Dependency confusion attacks
- Malicious package injection
- Compromised build environments
- Artifact tampering

It covers:

- Dependency verification and approval
- Build provenance and attestation
- SBOM (Software Bill of Materials) requirements
- Artifact signing and verification

## Governance Principles

- **Security-by-Design:** Supply chain security embedded in development process
- **Control-Centric Architecture:** Preventive and detective controls at each step
- **Developer-Operational Alignment:** Secure supply chain without developer friction
- **Audit Traceability:** Full provenance from source to deployment

## Dependency Management

### Approved Package Registries

**Requirement:** Use only approved package registries.

**Approved Registries:**

- Internal artifact repository (Artifactory, Nexus, Azure Artifacts)
- Public registries via internal proxy/mirror

**Developer Requirements:**

- Configure package managers to use internal registry first
- Internal registry proxies and caches approved packages from public registries
- Block direct access to public registries from production build environment
- Scan packages in internal registry for vulnerabilities

### Dependency Verification

**Requirement:** Verify integrity of all downloaded dependencies.

**Developer Requirements:**

- Verify package checksums (SHA-256 minimum)
- Verify package signatures where available (e.g., npm signatures, Python wheels)
- Use lock files to pin exact versions (package-lock.json, Gemfile.lock, poetry.lock)
- Fail build if checksum mismatch detected

**Lock File Requirements:**

- Commit lock files to version control
- Review lock file changes in code review
- Regenerate lock files only when intentionally updating dependencies

### Dependency Approval Process

**Requirement:** Review and approve new dependencies before introduction.

**Approval Workflow:**

1. Developer proposes new dependency in pull request
2. Automated SCA scan checks for known vulnerabilities
3. Security champion reviews:
   - Dependency necessity and alternatives
   - Maintainer reputation and activity
   - License compatibility
   - Supply chain risk (number of transitive dependencies)
4. Approval documented in pull request
5. Dependency added to approved list

**Approval Criteria:**

- No known critical or high-severity vulnerabilities
- Active maintenance (commits within last 6 months)
- Reputable maintainer or organization
- Compatible license
- Minimal transitive dependencies (reduce attack surface)

### Dependency Updates

**Requirement:** Regularly update dependencies to address vulnerabilities.

**Update Policy:**

- Security patches: Apply within 7-30 days depending on severity
- Minor version updates: Quarterly review
- Major version updates: Planned with testing

**Developer Requirements:**

- Enable automated dependency update PRs (Dependabot, Renovate)
- Review and test dependency updates before merging
- Monitor for breaking changes in release notes

## Build Provenance

### Build Attestation

**Requirement:** Generate cryptographically signed attestation for every build.

**Attestation Contents:**

- Source repository and commit hash
- Build command and parameters
- Build environment (OS, tools, versions)
- Build timestamp
- Builder identity (CI/CD system, service account)
- Output artifacts (hash, location)

**Developer Requirements:**

- Use SLSA Build Level 2+ provenance format
- Sign attestation using ephemeral key or workload identity
- Store attestation alongside artifacts in artifact repository
- Use tools like Sigstore/Cosign or in-toto

**Example (Sigstore Cosign):**

```bash
# Sign container image and generate attestation
cosign sign --key cosign.key myregistry.com/myapp:v1.0.0

# Generate SLSA provenance
cosign attest --key cosign.key \
  --predicate slsa-provenance.json \
  myregistry.com/myapp:v1.0.0
```

### Reproducible Builds

**Requirement:** Strive for reproducible builds (same source produces same artifact).

**Developer Requirements:**

- Use fixed versions of build tools
- Avoid embedding timestamps or build machine details in artifacts
- Use containerized build environments for consistency
- Document build process for manual verification

**Benefits:**

- Artifact tampering detectable (hash mismatch)
- Independent verification possible
- Increased confidence in build integrity

## Software Bill of Materials (SBOM)

### SBOM Generation

**Requirement:** Generate SBOM for every build in standard format.

**Supported Formats:**

- **SPDX** (Software Package Data Exchange) – ISO/IEC standard
- **CycloneDX** – OWASP standard

**Developer Requirements:**

- Generate SBOM automatically in CI/CD pipeline
- Include all direct and transitive dependencies
- Include component licenses
- Store SBOM in artifact repository alongside artifacts
- Make SBOM available to customers (if distributing software)

**SBOM Tools:**

- Syft (container and filesystem SBOM generation)
- CycloneDX CLI
- SPDX SBOM Generator
- Cloud provider tools (AWS Inspector, Azure Defender)

**Example (Syft):**

```bash
# Generate SBOM for container image
syft myregistry.com/myapp:v1.0.0 -o spdx-json > sbom.spdx.json

# Generate SBOM for local directory
syft dir:. -o cyclonedx-json > sbom.cdx.json
```

### SBOM Consumption

**Requirement:** Use SBOM for vulnerability tracking and compliance.

**Use Cases:**

- Continuous monitoring for new vulnerabilities in production components
- License compliance verification
- Customer transparency (if distributing software)
- Incident response (quickly identify affected systems)

**Developer Requirements:**

- Ingest SBOM into vulnerability management system
- Alert on new vulnerabilities in SBOM components
- Update SBOM when components are updated

## Artifact Signing and Verification

### Artifact Signing

**Requirement:** Sign all release artifacts.

**Artifact Types:**

- Container images
- Binary executables
- Library packages (JAR, npm, wheel)
- Deployment manifests (Kubernetes YAML, Terraform)

**Developer Requirements:**

- Sign artifacts using private key or keyless signing (Sigstore)
- Use separate signing keys per artifact type or environment
- Automate signing in CI/CD pipeline
- Store signatures in artifact repository

**Signing Methods:**

| Method            | Use Case               | Security                   | Complexity |
| ----------------- | ---------------------- | -------------------------- | ---------- |
| GPG/PGP           | Traditional packages   | High (with key management) | High       |
| Cosign (keyless)  | Container images       | High (OIDC-based)          | Low        |
| Code Signing Cert | Windows/macOS binaries | High                       | Medium     |

### Artifact Verification

**Requirement:** Verify artifact signatures before deployment.

**Developer Requirements:**

- Verify signature using trusted public key or CA
- Fail deployment if signature invalid or missing
- Enforce signature verification in deployment tool (Kubernetes admission controller, CD pipeline)

**Kubernetes Example (Cosign Admission Controller):**

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: cosign-webhook
webhooks:
  - name: cosign.sigstore.dev
    rules:
      - operations: ["CREATE", "UPDATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
    # Verify all images are signed before allowing pod creation
```

## Supply Chain Levels for Software Artifacts (SLSA)

### SLSA Compliance

**Requirement:** Achieve SLSA Build Level 2 minimum, target Level 3.

**SLSA Levels:**

| Level      | Requirements                                      | Benefits           |
| ---------- | ------------------------------------------------- | ------------------ |
| **SLSA 1** | Build process documented                          | Basic transparency |
| **SLSA 2** | Build service generates provenance                | Verifiable build   |
| **SLSA 3** | Build service hardened, source integrity verified | Tamper-resistant   |
| **SLSA 4** | Two-party review of changes                       | Highest assurance  |

**Developer Requirements (SLSA 2):**

- Use hosted build service (GitHub Actions, GitLab CI, Cloud Build)
- Build service generates signed provenance
- Source repository enforces branch protection

**Developer Requirements (SLSA 3):**

- Build service runs on ephemeral, isolated environment
- Provenance includes source repository and commit hash
- All dependencies verified before build

## Dependency Confusion Prevention

### Private Package Naming

**Requirement:** Use unique naming for internal packages to prevent dependency confusion.

**Developer Requirements:**

- Use organization-specific namespace or prefix (e.g., `@mycompany/package-name`)
- Register internal package names in public registries (reserve name, mark as private)
- Configure package manager to prioritize internal registry

**Example (npm scoped packages):**

```json
{
  "name": "@mycompany/internal-api-client",
  "private": true
}
```

**Example (.npmrc):**

```
@mycompany:registry=https://internal-registry.mycompany.com
```

### Registry Priority Configuration

**Requirement:** Configure package managers to use internal registry first.

**Developer Requirements:**

- Internal registry configured as primary source
- Public registries as fallback (with SCA scanning)
- Block resolution if package found in both internal and public registry (require manual review)

## Incident Response

### Supply Chain Compromise Detection

**Requirement:** Monitor for supply chain attack indicators.

**Monitored Signals:**

- Unexpected changes to dependency checksums
- New maintainers added to critical dependencies
- Sudden increase in transitive dependencies
- Vulnerabilities introduced in dependency updates
- Unusual network connections during build

**Developer Requirements:**

- Subscribe to security advisories for critical dependencies
- Enable alerts for dependency changes
- Review release notes before updating dependencies

### Supply Chain Incident Response

**Requirement:** Have documented response plan for supply chain compromise.

**Response Steps:**

1. Identify compromised component and affected systems
2. Use SBOM to locate all instances of component
3. Isolate affected systems
4. Assess compromise scope and impact
5. Roll back or patch affected systems
6. Conduct forensic analysis
7. Document lessons learned and improve controls

## Control Mapping

| EATGF Context           | ISO 27001:2022 | NIST SSDF  | OWASP            | COBIT |
| ----------------------- | -------------- | ---------- | ---------------- | ----- |
| Dependency Verification | A.8.31         | PO.3       | Dependency-Check | BAI07 |
| Build Provenance        | A.8.26         | PS.2       | SLSA             | BAI03 |
| SBOM                    | A.8.30         | PO.3, RV.1 | CycloneDX        | BAI07 |
| Artifact Signing        | A.8.24         | PS.2       | Sigstore         | DSS05 |

## Developer Checklist

For every release:

- [ ] All dependencies resolved from approved registries
- [ ] Dependency checksums verified
- [ ] New dependencies approved by security champion
- [ ] Build provenance generated and signed
- [ ] SBOM generated in SPDX or CycloneDX format
- [ ] Artifacts signed using Cosign or equivalent
- [ ] Signature verification enforced in deployment pipeline

## Governance Implications

**Risk if not implemented:**

- Supply chain attacks (malicious dependencies)
- Dependency confusion attacks
- Artifact tampering
- Unable to track vulnerabilities in production components

**Operational impact:**

- SBOM enables rapid vulnerability response
- Artifact signing prevents tampering
- Build provenance supports incident investigation

**Audit consequences:**

- SBOM required for compliance (EO 14028, NTIA guidance)
- Supply chain security demonstrates risk management
- Provenance provides audit trail

**Cross-team dependencies:**

- Security team defines supply chain policies
- DevOps team configures artifact repository and signing
- Engineering teams implement SBOM generation

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. Supply Chain Security Standard

## References

- NIST SP 800-218 (SSDF Practice PO.3)
- SLSA Framework (https://slsa.dev/)
- Sigstore (https://www.sigstore.dev/)
- SPDX Specification (https://spdx.dev/)
- CycloneDX (https://cyclonedx.org/)
- CISA Software Supply Chain Best Practices
- Executive Order 14028: Improving the Nation's Cybersecurity

## Version History

| Version | Date       | Change Type | Description                            |
| ------- | ---------- | ----------- | -------------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial supply chain security standard |
