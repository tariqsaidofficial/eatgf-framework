# CI/CD Security Architecture Standard

| Field | Value |
|-------|-------|
| Document Type | Implementation Standard |
| Version | 1.0 |
| Classification | Controlled |
| Effective Date | 2026-02-16 |
| Authority | Chief Security Officer and Platform Engineering Lead |
| EATGF Layer | 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE |
| MCM Reference | EATGF-PW-CD-01, EATGF-RV-CD-01 |

---

## Purpose

This standard defines security architecture requirements for all CI/CD pipelines. It ensures that code builds, tests, and deployments occur in secure, auditable environments with cryptographic integrity verification and unauthorized change prevention.

**Mandatory for:** All code deployments to production, staging, or regulated environments.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

- **Upstream dependency:** Layer 02 Control Objectives (change management, code integrity, audit traceability); Layer 04 Information Security Policy (authentication, encryption)
- **Downstream usage:** Enforces security controls throughout artifact lifecycle from source code through deployment
- **Cross-layer reference:** Maps to NIST SSDF PW.4 (artifact handling), PW.5 (build platform), RV.1 (static testing)

## Governance Principles

1. **Zero-Trust Pipeline Architecture** – All pipeline stages assume compromise; each stage cryptographically verifies prior stages
2. **Immutable Artifacts** – Build outputs are immutable after creation; modification requires full rebuild and audit
3. **Cryptographic Integrity** – All artifacts signed with hardware-backed keys; signatures verified at deployment
4. **Auditability by Design** – Every pipeline action logged with actor identity, timestamp, input/output hashes
5. **Least Privilege Compute** – Pipeline runners operate with minimal permissions; elevated privileges require approval

## Technical Implementation

### CI/CD Pipeline Architecture

**Five-Layer Security Model:**

**Layer 1: Source Control Security**
- Code repository authentication via public key infrastructure or SSO
- Commit signing required (GPG or similar); unsigned commits blocked
- Branch protection rules: code review + CI pass required before merge
- Audit trail retention: minimum 7 years for production code changes
- Secret scanning: automated detection of credentials in source code; commits rejected if secrets detected
- Example platforms: GitHub, GitLab, Gitea

**Layer 2: Build Isolation and Sandboxing**
- Build execution in containerized environment; no shared compute
- Build containers based on hardened base images; weekly vulnerability scanning
- Network isolation: build environment cannot access production credentials
- Filesystem ephemeral: build artifacts written to temporary storage; cleaned after completion
- Resource limits: CPU/memory throttling to prevent resource exhaustion
- Example platforms: GitHub Actions, GitLab CI, CircleCI, Jenkins with container agents

**Layer 3: Artifact Signing and Provenance**
- All build artifacts cryptographically signed with hardware security module (HSM) key
- Signature includes: build environment fingerprint, builder identity, timestamp, artifact hash
- Artifact provenance recorded in Software Bill of Materials (SBOM) format
- Signature verification mandatory at deployment stage; deployment fails if signature invalid
- Key rotation: HSM keys rotated annually; old keys retained but marked deprecated
- Example standards: Sigstore, in-toto, SLSA framework

**Layer 4: Deployment Security**
- Deployment credentials stored in hardware-backed vault (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault)
- Deployment credentials rotated on every successful deployment (one-time-use tokens)
- Deployment approval: critical/production deployments require manual approval from authorized deployer
- Deployment audit: all deployment actions logged including deployer, target environment, artifact version
- Rollback capability: previous artifact versions retained and deployable; rollback audited
- Example platforms: ArgoCD, Spinnaker, AWS CodeDeploy

**Layer 5: Monitoring and Response**
- Pipeline execution monitoring: real-time alerts for failed builds, unsigned artifacts, unapproved deployments
- SIEM integration: pipeline events streamed to security information and event management system
- Incident response: failed deployment security checks trigger automatic rollback and security team notification
- Compliance dashboard: real-time view of build security posture (% signed artifacts, % passing security gates)

### CI/CD Platform Selection

**Required Security Capabilities:**

| Capability | Requirement | Verification |
|------------|-------------|----------------|
| Secret Management | Secrets never logged or exposed in build logs | Log file audit sampling |
| Build Isolation | Each build in separate ephemeral environment | Platform documentation + test |
| Audit Logging | All pipeline actions logged with identity | Log retention verification |
| Access Control | Role-based access to pipeline configuration | Access control audit |
| Artifact Repository | Credentials-based access control; repository scan for vulnerabilities | Repository audit |
| Deployment Approval | Manual approval gate for critical environments | Configuration review |

**Tested Platforms:**
- GitHub Actions (GitHub Enterprise Cloud with advanced security)
- GitLab CI (self-hosted with elevated privileges)
- CircleCI (with private runners and vault integration)
- Jenkins (with agent segregation and Groovy sandboxing)

**Prohibited Platforms:**
- Shared hosted build agents without network isolation
- Pipeline systems without cryptographic artifact signing
- Platforms without audit logging

### Enforced Security Gates

**Build Pipeline Security Gates:**

1. **Code Quality Gate** – SonarQube or equivalent; code fails build if quality metrics below threshold
   - Blockers: Critical security issues, code duplications >20%, coverage <60%
   - Critical failures trigger automatic notification to code owner

2. **Dependency Analysis Gate** – OWASP Dependency-Check or Snyk; fails if high-risk vulnerabilities detected
   - Known vulnerabilities: CVSS >7 blocks build; CVSS 5-7 requires manual exception
   - Transitive dependencies scanned; supply chain risk assessed

3. **Secret Detection Gate** – TruffleHog, git-secrets, or GitGuardian; fails if credentials detected
   - Regular expressions match API keys, credentials, private key formats
   - False positives require maintainer override with documented exception

4. **Container Image Scan Gate** – Trivy or Qualys; fails if critical vulnerabilities in base image
   - Base image scanned for known CVEs from NVD database
   - CVSS >8.9 blocks deployment; lower scores trigger risk assessment

5. **Artifact Signing Gate** – Cosign or TUF; fails if artifact not cryptographically signed
   - Signature verified against public key pinned in deployment environment
   - Key rotation tracked; old keys verified before signing verification

6. **Compliance Gate** – Custom policy engine (OPA/Rego or Kyverno); fails if policy violations detected
   - Policy examples: Kubernetes resource quotas, image registry whitelisting, RBAC requirements
   - Policy violations trigger exception workflow with security review

**Gate Bypass Procedure:**

- Bypass only allowed via explicit override by security lead
- Override requires: business justification, risk assessment, 30-day remediation deadline
- Override recorded in audit log with approver identity and justification
- Exceptions reviewed monthly; outstanding exceptions escalated monthly

### Build Environment Hardening

**Build Runner Base Image Requirements:**

```dockerfile
# Minimal Linux base: Alpine or Distroless
FROM alpine:3.19

# Security hardening
RUN apk add --no-cache \
    ca-certificates \
    git \
    python3 \
    && rm -rf /var/cache/apk/*

# Run as non-root
RUN addgroup -g 1000 builder && adduser -D -u 1000 -G builder builder
USER builder:builder

# Immutable filesystem
RUN echo "tmpfs /tmp tmpfs defaults,rw,nosuid,nodev,noexec 0 0" >> /etc/fstab
```

**Build Runner Network Requirements:**
- Outbound: Package registries (PyPI, npm, Maven Central), Git hosting, Docker registries only
- Inbound: Blocked except for pipeline control messages
- DNS: Resolved through internal DNS forwarder; external resolution blocked
- No external load balancer access; builds triggered only via pipeline service

**Build Runner Resource Limits:**
- CPU: 2 cores maximum per build
- Memory: 4 GB maximum per build
- Disk: 50 GB temporary storage (cleaned after build)
- Build timeout: 60 minutes (enforcement at platform level)

### Artifact Repository Security

**Repository Access Control:**
- Read access: Restricted to deployment systems and authorized developers
- Write access: Restricted to build pipeline only
- Admin access: CISO approval required; actions logged with hardware key signing
- Access tokens: Rotated every 90 days minimum
- Credential storage: Stored in hardware security module (HSM); never in plaintext

**Repository Vulnerability Scanning:**
- All uploaded artifacts scanned within 1 hour of upload
- Vulnerability scan results attached to artifact metadata; available at deployment time
- High-risk artifacts (CVSS >8.9) quarantined; deployment rejected unless explicitly approved
- Scan results retained for minimum 7 years per audit requirements

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Build isolation | A.8.25, A.8.26 | PW.4.1, PW.5 | SAMM-AM | BAI03.10 |
| Artifact signing | A.8.30, A.8.31 | PW.4.2, RV.1.2 | SLSA | BAI07.02 |
| Secret management | A.8.24, A.7.2 | PO.5.1, PW.3 | SecureCodeDox | BAI04.02 |
| Compliance gates | A.8.19, A.8.20 | PW.6, PO.3 | ASVS | DSS05.06 |
| Access control | A.9.2, A.9.4 | PO.1, PO.2 | AuthN/Z | APO01.03 |

## Developer Checklist

Before implementing CI/CD security architecture:

- [ ] CI/CD platform selected from approved list (GitHub Actions, GitLab CI, CircleCI, Jenkins)
- [ ] Build isolation verified: each build runs in separate ephemeral container
- [ ] Artifact signing configured: cryptographic signing with HSM-backed keys
- [ ] Six security gates implemented: code quality, dependencies, secrets, container scan, signing, compliance
- [ ] Secret detection enabled: TruffleHog or GitGuardian scanning on every commit
- [ ] Build logs verified: no credentials exposed; logs retained 90 days
- [ ] Build approval workflows: manual approval for critical/production deployments
- [ ] Deployment credentials rotated: one-time-use tokens or automatic rotation on every deployment
- [ ] Artifact repository access restricted: CI/CD system only for write access
- [ ] Audit logging verified: all pipeline actions logged with actor identity and timestamp
- [ ] Monitoring dashboards configured: security gate failures trigger alerts
- [ ] Incident response procedures: rollback procedures documented and tested
- [ ] Hardware security module (HSM) provisioned: signing keys protected with FIPS 140-2 compliance
- [ ] Compliance audits: quarterly review of security gate bypass exceptions

## Governance Implications

**Risk if not implemented:**

- Compromised build pipelines inject malware into production code
- Unsigned artifacts allow unauthorized deployment of untrusted code
- Plaintext build credentials captured and used for lateral movement
- Unauditable deployments prevent forensic investigation of security incidents
- Supply chain attacks through transitive dependency vulnerabilities go undetected

**Operational impact:**

- Build failure rates initially increase (10-20% during hardening phase)
- Build time increases 15-30% due to security scanning and approval workflows
- Infrastructure cost increases for separate build environments and HSM hardware
- Security incident detection and response time decreases dramatically

**Audit consequences:**

- CI/CD security gaps result in audit findings under ISO 27001 A.8.25-26 (change management)
- Unsigned artifacts indicate non-compliance with artifact integrity controls
- Build logs provide primary audit evidence for deployment traceability
- Missing security gates indicate control deficiency in NIST SSDF PW layer

**Cross-team dependencies:**

- Platform Engineering: infrastructure provisioning for build runners, artifact repositories, HSM
- Security: approval workflows, monitoring dashboards, incident response procedures
- Development: understanding of security gates, exception procedures, remediation timelines
- Audit: log retention, compliance verification, periodic security gate exception review

## Official References

- **NIST SP 800-218** – Secure Software Development Framework (PW.4, PW.5, RV.1)
- **NIST SP 800-46 Revision 2** – Security for Specialized Information Systems
- **SLSA Framework** – Supply chain Levels for Software Artifacts (slsa.dev)
- **ISO/IEC 27001:2022** – Information Security Management Systems
- **Sigstore Documentation** – keyless signing for software artifacts (sigstore.dev)
- **in-toto Framework** – Secure software supply chain (in-toto.io)
- **OWASP SAMM** – Software Assurance Maturity Model
- **COBIT 2019** – Domains BAI03, BAI07, DSS05

## Version History

| Version | Date | Change Type | Description |
|---------|------|-------------|-------------|
| 1.0 | 2026-02-16 | Major | Initial CI/CD security architecture standard for Layer 08 |
