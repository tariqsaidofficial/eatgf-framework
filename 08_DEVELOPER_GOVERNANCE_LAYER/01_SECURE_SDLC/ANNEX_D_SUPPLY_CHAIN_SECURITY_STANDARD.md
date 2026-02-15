# Software Supply Chain Security Standard

## Purpose

Defines governance controls for dependency integrity, SBOM, third-party risk, and artifact provenance.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Domain: 01_SECURE_SDLC
Control Reference: SDLC-SUP-04

## Governance Principles

- All dependencies are potential attack vectors.
- SBOM must be generated for each release.
- External components must be traceable.
- Third-party code requires risk evaluation.

## Technical Implementation

### 1. SBOM Generation (MANDATORY)

```bash
cyclonedx-py -r -o sbom.json
```

### 2. Dependency Pinning (MANDATORY)

```
fastapi==0.110.0
pydantic==2.6.1
```

No floating versions.

### 3. Dependency Scanning (MANDATORY)

```bash
pip-audit
```

Fail if HIGH vulnerabilities unresolved.

### 4. Third-Party Review

- License review
- Maintenance activity check
- Security advisory review

## Control Mapping

| Framework   | Mapping                                             |
| ----------- | --------------------------------------------------- |
| ISO 27001   | **A.8.28** Supply chain management (PRIMARY)       |
| ISO 27001   | A.5.19 Supplier relationships                     |
| NIST SSDF   | PS.3 Manage third-party software                   |
| OWASP       | Dependency management                              |
| COBIT       | APO10 Manage Suppliers                             |
| NIST 800-53 | SA-12 Supply Chain Protection                     |

## Developer Checklist

- SBOM generated
- Versions pinned
- Dependencies scanned
- License reviewed
- Advisory monitoring active
- Artifact provenance verified

## Governance Implications

Supply chain attacks bypass perimeter security.
Governance must extend to external code.

## Official References

- NIST SP 800-218
- ISO/IEC 27001:2022
- NIST SP 800-53
- COBIT 2019

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Classification: Public Governance Standard
