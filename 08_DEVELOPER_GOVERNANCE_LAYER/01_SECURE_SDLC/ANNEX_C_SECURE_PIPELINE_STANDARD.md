# Secure CI/CD Pipeline Governance Standard

## Purpose

Defines mandatory security controls for CI/CD pipelines to prevent supply chain compromise, unauthorized deployments, and insecure builds.

This Annex governs build automation, artifact integrity, deployment gating, and pipeline trust boundaries.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Domain: 01_SECURE_SDLC
Authority: Subordinate to SECURE_SDLC_GOVERNANCE_STANDARD.md
Control Reference: SDLC-PIPE-03

Enforced via ENFORCEMENT_MATRIX.md pre-release gate.

## Governance Principles

- Pipelines are production systems.
- Builds must be deterministic and reproducible.
- Artifacts must be signed.
- No direct production deployment from local machines.
- Pipeline configuration is code (Pipeline-as-Code).
- Secrets must never reside in CI variables unencrypted.

## Technical Implementation

### 1. Pipeline as Code (MANDATORY)

```yaml
# .github/workflows/build.yml
name: Secure Build

on:
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run SAST
        run: bandit -r .

      - name: Build Artifact
        run: docker build -t app:${{ github.sha }} .
```

### 2. Artifact Signing (MANDATORY)

```bash
cosign sign --key cosign.key myregistry/app:latest
```

Unsigned artifacts must be rejected at deployment.

### 3. Branch Protection (MANDATORY)

- Required PR review
- Required status checks
- No force push
- No direct push to main

### 4. Dependency & Image Scanning (MANDATORY)

```bash
trivy image myregistry/app:latest
```

Fail pipeline if HIGH/CRITICAL vulnerabilities exist.

## Control Mapping

| Framework      | Mapping                           |
| -------------- | --------------------------------- |
| ISO 27001:2022 | A.8.28 Secure development         |
| NIST SSDF      | PW.6 Secure build process         |
| OWASP SAMM     | Deployment Security               |
| COBIT 2019     | BAI06 Manage Changes              |
| NIST 800-53    | CM-3 Configuration Change Control |

## Developer Checklist

- Pipeline as code committed
- Branch protection enabled
- SAST executed
- Dependency scanning enforced
- Artifact signed
- No plaintext secrets
- Deployment gated
- Immutable artifact tags used

## Governance Implications

Pipeline compromise equals total system compromise.
Secure pipelines are non-negotiable for SaaS and Enterprise.

## Official References

- NIST SP 800-218
- ISO/IEC 27001:2022
- OWASP SAMM
- COBIT 2019
- NIST SP 800-53 Rev.5

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Classification: Public Governance Standard
