# Security Testing Governance Standard

## Purpose

Defines governance for SAST, DAST, and penetration testing.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Control Reference: SDLC-TEST-06

## Governance Principles

- Testing must be automated.
- Testing must be repeatable.
- Critical findings block release.

## Technical Implementation

### 1. SAST (Mandatory)

```bash
bandit -r .
```

### 2. DAST (Mandatory)

```bash
zap-baseline.py -t https://staging.example.com
```

### 3. Penetration Testing (Mandatory)

- Annual for Enterprise.
- Pre-major-release for SaaS.

## Control Mapping

| Framework   | Mapping                         |
| ----------- | ------------------------------- |
| ISO 27001   | A.8.29 Testing                  |
| NIST SSDF   | RV.3 Security testing           |
| OWASP       | ASVS verification               |
| COBIT       | MEA01 Performance & conformance |
| NIST 800-53 | CA-8 Penetration Testing        |

## Developer Checklist

- SAST integrated
- DAST executed
- Critical vulnerabilities resolved
- False positives documented
- Test reports archived

## Governance Implications

Security testing provides measurable compliance evidence.

## Official References

- NIST SP 800-218
- ISO/IEC 27001:2022
- OWASP ASVS
- COBIT 2019

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Classification: Public Governance Standard
