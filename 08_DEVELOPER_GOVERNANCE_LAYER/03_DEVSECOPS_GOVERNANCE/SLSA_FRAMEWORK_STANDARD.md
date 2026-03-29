# SLSA Framework Implementation Standard

| Field          | Value                                                   |
| -------------- | ------------------------------------------------------- |
| Document Type  | Implementation Standard                                 |
| Version        | 1.0                                                     |
| Classification | Controlled                                              |
| Effective Date | 2026-02-16                                              |
| Authority      | Chief Information Security Officer                      |
| EATGF Layer    | 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE |
| MCM Reference  | EATGF-DEV-SUP-01                                        |

---

## Purpose

Implement SLSA (Supply chain Levels for Software Artifacts) framework to increase supply chain integrity, protect against artifact tampering and unauthorized modification, and enable verifiable provenance.

**Scope:** All software artifacts deployed to production.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

- **Upstream dependency:** Supply Chain Security Standard, CI/CD Security Architecture
- **Downstream usage:** SLSA provenance attestations created during builds; verified at deployment
- **Cross-layer reference:** Maps to NIST SSDF PW/RV layers; aligns with in-toto provenance framework

## Governance Principles

1. **Verifiable Provenance** – Complete artifact history and builder identity cryptographically verified
2. **Build System Security** – Build platform isolation, access control, audit logging per NIST SP 800-218
3. **Tamper-Proof Artifacts** – Cryptographic signatures prevent unauthorized modification
4. **Progressive Levels** – SLSA 1-4 maturity progression; target SLSA 3+ for regulated environments

## Technical Implementation

### SLSA Levels Progression

| Level | Code Controls  | Build Requirements   | Provenance               | Deployment               |
| ----- | -------------- | -------------------- | ------------------------ | ------------------------ |
| **1** | VCS + review   | Automated builds     | Basic provenance         | Manual verification      |
| **2** | Signed commits | Isolated build       | Signed provenance        | Manual + signature check |
| **3** | Hardened CI    | Hermetic builds      | Hardened provenance      | Automated verification   |
| **4** | Full hardening | Multi-party approval | Cryptographic provenance | Complete automation      |

**Target:** SLSA 3 for all production software.

### SLSA 1: Version Control + Builds

**Requirements:**

- Code in version control (Git)
- Commit review and approval
- Runs automated builds
- Builds produce verifiable artifacts

```yaml
# Simple build workflow
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build
        run: |
          npm install
          npm run build
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist/
```

### SLSA 2: Signed Commits + Isolated Builds

**Requirements:**

- Commits must be signed (GPG/SSH)
- Branch protection enforced
- Builds run in isolated containers
- Build secrets managed in vault
- Build logs retained

```yaml
# SLSA 2 workflow
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: ubuntu:22.04
      options: "--network isolated"
    steps:
      - uses: actions/checkout@v3
      - name: Verify commit signature
        run: git verify-commit HEAD || exit 1

      - name: Build
        env:
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: |
          npm ci --prefer-offline
          npm run build

      - name: Sign artifact
        run: |
          cosign sign-blob \
            --key /var/run/secrets/signing-key \
            dist/app.js > dist/app.js.sig

      - name: Generate SLSA provenance (L2)
        uses: slsa-framework/github-action-slsa-provenance@v1
        with:
          artifact_list: dist/app.js.sig
```

### SLSA 3: Hardened Build System

**Build System Hardening:**

```dockerfile
# Hardened builder image
FROM ubuntu:22.04 as builder

# Minimal OS
RUN apt-get update && apt-get install --no-install-recommends \
    ca-certificates git curl \
    && rm -rf /var/lib/apt/lists/*

# Non-root user
RUN useradd -m -s /sbin/nologin builder
USER builder

# Immutable filesystem
RUN chmod 000 /root

# Network isolation enforced at runtime
```

**Build Isolation:**

```yaml
# GitHub Actions: SLSA 3 with hermetic builds
jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write # For OIDC token
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0 # Full history for verification

      # Verify repository state
      - name: Verify repo state
        run: |
          # No uncommitted changes
          [ -z "$(git status --porcelain)" ] || exit 1

          # Commits signed
          for commit in $(git rev-list HEAD~10..HEAD); do
            git verify-commit $commit || exit 1
          done

      # Hermetic build: no network except to allowed registries
      - name: Build hermetically
        run: |
          npm ci --prefer-offline --no-audit
          npm run build

      # Generate SLSA 3 provenance
      - uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3@v1
        with:
          base64-subjects: "${{ steps.hash.outputs.hashes }}"
          upload-assets: true
```

### SLSA 4: Supply Chain Attack Resilience

**SLSA 4 Requirements:**

- Hermetic builds (reproducible)
- Distributed builds (no single point of compromise)
- Hardware-backed key signing
- Multi-party approval for production deployments

```yaml
# SLSA 4: High-security deployment
on:
  repository_dispatch:
    types: [deploy-production]

jobs:
  slsa-4-deploy:
    runs-on: ubuntu-latest
    environment:
      name: production-slsa4
      approval-required: true # Requires manual approval

    steps:
      # Verify SLSA provenance before deployment
      - name: Verify SLSA attestation
        run: |
          cosign verify-attestation \
            --predicate-type slsaprovenance \
            --key=${{ secrets.SIGNINGKEY_PUBLIC }} \
            ${{ env.ARTIFACT_URI }}

      # Verify provenance meets SLSA 4
      - name: Validate SLSA level
        run: |
          # Check provenance claims
          # - Builder identity matches allowed builders
          # - Build environment hermetic
          # - All dependencies listed
          # - Build reproducible

      - name: Deploy with multi-party approval
        run: |
          # Deploy only after approval
          kubectl apply -f deployment.yaml --record
```

### Provenance Verification

**Cosign + In-Toto Provenance:**

```bash
# Generate provenance during build
cosign attest --predicate provenance.json \
  --key=hsm://key-id \
  ghcr.io/company/app:v1.2.3

# Verify provenance at deployment
cosign verify-attestation \
  --type=slsaprovenance \
  --key=cosign.pub \
  ghcr.io/company/app:v1.2.3 | jq '.

# Extract builder information
cosign verify-attestation ... | jq '.payload | @base64d | fromjson | .predicate | {builder, buildConfig, invocation}'
```

**Provenance Content:**

```json
{
  "predicate": {
    "builder": {
      "id": "https://github.com/slsa-framework/slsa-github-generator@v1"
    },
    "sourceRepository": "https://github.com/company/app",
    "invocation": {
      "configSource": {
        "uri": "git+https://github.com/company/app@12345",
        "digest": { "sha1": "abc123" },
        "entryPoint": ".github/workflows/build.yaml"
      },
      "parameters": {},
      "environment": {
        "github_actor": "ci-system",
        "github_run_attempt": "1"
      }
    },
    "buildConfig": {
      "steps": [
        { "command": ["npm", "ci"], "env": ["NPM_TOKEN"] },
        { "command": ["npm", "run", "build"] },
        { "command": ["npm", "run", "test"] }
      ]
    },
    "materials": [
      {
        "uri": "git+https://github.com/company/app@12345",
        "digest": { "sha1": "abc123" }
      }
    ],
    "completeness": {
      "parameters": true,
      "environment": true,
      "materials": true
    },
    "reproducible": true
  }
}
```

## Control Mapping

| EATGF Context       | ISO 27001:2022 | NIST SSDF      | COBIT |
| ------------------- | -------------- | -------------- | ----- |
| SLSA 3+             | A.8.30, A.8.31 | PW.4, PW.5, RV | BAI07 |
| Artifact provenance | A.8.30, A.12.7 | RV.1, RV.2     | MEA02 |

## Developer Checklist

- [ ] SLSA target level defined (recommend SLSA 3+)
- [ ] Cosign installed and configured
- [ ] Build workflow generates SLSA provenance
- [ ] Deployment verifies SLSA attestation
- [ ] Builder identity pinned in deployment
- [ ] Hermetic build environment confirmed
- [ ] Reproducible builds validated
- [ ] Multi-party approval for SLSA 4
- [ ] Provenance audit logging enabled

## Governance Implications

**Risk if Not Implemented:**
- Without SLSA attestation, deployed artifacts lack verifiable provenance, enabling supply chain attacks through tampered binaries, compromised build systems, or unauthorized modifications
- Organizations without SLSA compliance cannot demonstrate software integrity to auditors or regulatory bodies

**Operational Impact:**
- All production deployments must include SLSA provenance attestation at Level 2 minimum; regulated environments require Level 3+
- Build systems must generate signed provenance automatically; manual attestation is prohibited
- Deployment pipelines must verify provenance before releasing to production; verification failures block deployment

**Audit Consequences:**
- SLSA compliance audited as part of EATGF-DEV-SUP-01 (Software Supply Chain & SBOM Management)
- Missing or invalid provenance attestations constitute a High-severity audit finding
- Build system access logs and signing key management are mandatory audit evidence

**Cross-Team Dependencies:**
- Platform Engineering: Configures hermetic build environments and provenance generation
- Security: Manages signing keys (Cosign/Sigstore) and validates attestation integrity
- DevOps: Integrates provenance verification into CI/CD deployment gates
- Audit: Reviews provenance chain completeness during annual control assessments

## Official References

- SLSA Specification v1.0 (https://slsa.dev/spec/v1.0/)
- NIST SP 800-218 (Secure Software Development Framework)
- NIST SP 800-161 Rev. 1 (Cybersecurity Supply Chain Risk Management)
- in-toto Attestation Framework (https://in-toto.io/)
- Sigstore/Cosign Documentation (https://docs.sigstore.dev/)

## Version History

| Version | Date       | Change Type | Description                                    |
| ------- | ---------- | ----------- | ---------------------------------------------- |
| 1.0     | 2026-02-16 | Major       | Initial SLSA framework implementation standard |
