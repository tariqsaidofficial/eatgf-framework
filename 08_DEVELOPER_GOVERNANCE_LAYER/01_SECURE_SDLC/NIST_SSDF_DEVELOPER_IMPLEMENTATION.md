# NIST SSDF Developer Implementation Standard

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 01_SECURE_SDLC  
**Governance Scope:** Implementation Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 01_SECURE_SDLC

**Governance Scope:** Developer-facing implementation of NIST SP 800-218 Secure Software Development Framework.

**Control Authority Relationship:** Implements:
- Layer 02: Secure Development Controls
- Layer 04: Information Security Policy
- NIST SSDF Practices (PW, PS, PO, RV)

## Purpose

This standard translates NIST SSDF practices into actionable engineering requirements. It defines:

- Development environment security controls
- Secure coding practices enforcement
- Dependency and supply chain validation
- Code review and testing requirements
- Vulnerability response procedures

## Governance Principles

- **Security-by-Design:** Security controls integrated into development workflow
- **Control-Centric Architecture:** Mapped to NIST SSDF practices
- **Developer-Operational Alignment:** Written for software engineers
- **Audit Traceability:** All activities produce verifiable evidence

## NIST SSDF Practice Mapping

### PW: Prepare the Workforce

**PW.1 – Establish secure development training**

**Developer Requirements:**
- Complete secure coding training within 30 days of onboarding
- Annual refresher on OWASP Top 10 and CWE Top 25
- Role-specific training (e.g., DevSecOps, API security)

**Evidence:**
- Training completion certificates
- Internal knowledge assessments

### PW.2 – Security champion program**

**Developer Requirements:**
- Each engineering team designates a security champion
- Champions receive advanced security training
- Champions participate in threat modeling reviews

### PS: Protect the Software

**PS.1 – Protect code repositories**

**Developer Requirements:**
- Enable branch protection on main/production branches
- Require signed commits (GPG/SSH)
- Enforce multi-factor authentication for repository access
- No credentials or secrets in version control

**Evidence:**
- Git repository configuration audit logs
- Pre-commit hook enforcement logs

**PS.2 – Secure development environment**

**Developer Requirements:**
- Use hardened development workstations
- Enable full-disk encryption
- Install endpoint protection (EDR)
- Use containerized development environments where possible

**PS.3 – Secure CI/CD pipelines**

**Developer Requirements:**
- CI/CD systems protected by RBAC
- Pipeline definitions stored in version control
- Build artifacts signed and verified
- No long-lived credentials in pipelines (use OIDC or short-lived tokens)

### PO: Produce Well-Secured Software

**PO.1 – Threat modeling**

**Developer Requirements:**
- Conduct threat modeling for new features or microservices
- Use STRIDE or PASTA methodology
- Document threat model in repository (THREAT_MODEL.md)

**Evidence:**
- Threat model artifacts in repository
- Threat modeling review meeting notes

**PO.3 – Review and analyze dependencies**

**Developer Requirements:**
- Run Software Composition Analysis (SCA) on every build
- Block builds with critical or high-severity vulnerabilities
- Maintain dependency inventory (SBOM)
- Review new dependencies before introduction

**Evidence:**
- SCA scan results in CI/CD pipeline
- SBOM files (SPDX or CycloneDX format)

**PO.5 – Automated testing**

**Developer Requirements:**
- Maintain minimum 80% code coverage for unit tests
- Run integration tests in CI/CD pipeline
- Perform security-specific tests (SAST, DAST, API fuzzing)

### RV: Respond to Vulnerabilities

**RV.1 – Vulnerability disclosure and response**

**Developer Requirements:**
- Subscribe to security advisories for all dependencies
- Patch critical vulnerabilities within 7 days
- Patch high-severity vulnerabilities within 30 days
- Document remediation in issue tracker

**Evidence:**
- Vulnerability tracking tickets
- Patch deployment logs

**RV.2 – Analyze and fix root causes**

**Developer Requirements:**
- Conduct root cause analysis for security incidents
- Update threat models based on findings
- Share lessons learned with engineering teams

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Training | A.6.3 | PW.1, PW.2 | SAMM Training | APO07 |
| Repository Security | A.8.3 | PS.1 | - | DSS05 |
| Threat Modeling | A.8.25 | PO.1 | SAMM Design | BAI03 |
| Dependency Management | A.8.31 | PO.3 | Dependency Check | BAI07 |
| Vulnerability Response | A.8.8 | RV.1, RV.2 | - | DSS02 |

## Developer Checklist

For every new project or feature:

- [ ] Complete threat modeling exercise
- [ ] Enable branch protection and signed commits
- [ ] Configure SCA scanning in CI/CD pipeline
- [ ] Establish minimum test coverage requirements
- [ ] Subscribe to security advisories for dependencies
- [ ] Document security architecture decisions

## Governance Implications

**Risk if not implemented:**
- Introduction of exploitable vulnerabilities
- Supply chain attacks via compromised dependencies
- Non-compliance with regulatory requirements (e.g., PCI-DSS, GDPR)

**Operational impact:**
- Early detection of vulnerabilities reduces remediation cost
- Automated controls reduce manual security reviews
- Clear standards reduce onboarding time for new developers

**Audit consequences:**
- NIST SSDF compliance is increasingly required by government contracts
- Non-compliance may result in failed security audits

**Cross-team dependencies:**
- Security team provides training and advisory support
- Platform team provides CI/CD infrastructure and tooling
- Audit team validates compliance and evidence collection

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. NIST SSDF Developer Implementation Standard

## References

- NIST SP 800-218: Secure Software Development Framework (https://csrc.nist.gov/publications/detail/sp/800-218/final)
- OWASP Software Assurance Maturity Model (https://owaspsamm.org/)
- ISO/IEC 27034-1: Application Security
- CWE Top 25 Most Dangerous Software Weaknesses (https://cwe.mitre.org/top25/)

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial NIST SSDF developer implementation standard |
