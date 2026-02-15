# Supply Chain Security Standard

| Field | Value |
|-------|-------|
| Document Type | Implementation Standard |
| Version | 1.0 |
| Classification | Controlled |
| Effective Date | 2026-02-16 |
| Authority | Chief Security Officer and Chief Technology Officer |
| EATGF Layer | 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE |
| MCM Reference | EATGF-PW-SUPPLY-01, EATGF-RV-SUPPLY-01 |

---

## Purpose

This standard protects against software supply chain attacks by ensuring integrity of build tools, dependencies, build infrastructure, and deployed artifacts throughout delivery pipelines.

**Mandatory for:** All code, binaries, and containers deployed to production.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

- **Upstream dependency:** Layer 02 Control Objectives (supply chain risk); Layer 04 Information Security Policy (vendor management, third-party risk)
- **Downstream usage:** Prevents compromise at every stage: code → build → artifact → deployment
- **Cross-layer reference:** Maps to NIST SSDF PW.4 (artifact handling), PW.5 (build platform), RV.1-RV.2 (testing), SLSA framework verification

## Governance Principles

1. **Trust Verification at Every Stage** – No trust in intermediaries; cryptographic verification at each pipeline stage
2. **Artifact Provenance Tracking** – Complete history of who built what, when, and with which tools
3. **Dependency Transparency** – SBOM required for all deployments; no opaque dependencies
4. **Tool Integrity** – Build tools and CI/CD platform patched within 7 days of security advisory

## Technical Implementation

### Supply Chain Layers

**Layer 1: Developer Machine Security**

Requirements for developer machines:
- Operating system: macOS 13+, Ubuntu 22.04+, Windows 11 with TPM 2.0
- Disk encryption: BitLocker (Windows), FileVault (macOS), LUKS (Linux)
- Antivirus: Endpoint Detection and Response (EDR) agent deployed
- Mobile device management: Approved devices only; wipe on termination
- VPN: All development over organization VPN or zero-trust network access

Developer machine security audit:
```bash
# macOS check script
security find-certificate -a -c "developer" > /dev/null
if ! defaults read -g com.apple.keylockd >/dev/null 2>&1; then
  echo "FAIL: FileVault not enabled"
  exit 1
fi

# Check for EDR agent
if ! launchctl list | grep -q "com.company.edragent"; then
  echo "FAIL: EDR agent not running"
  exit 1
fi
```

**Layer 2: Source Code Repository Security**

Requirements:
- Repository: GitHub Enterprise / GitLab self-hosted / Gitea with RBAC
- Authentication: Public key infrastructure (SSH or WebAuthn); no password auth
- Branch protection: Code review + CI pass required; no force-push to main
- Commit signing: GitHub/GitLab enforces GPG signatures
- Access audit: Quarterly review of repository access, delete unused keys

Protected branch rules:
```yaml
main:
  require_code_review: 1
  require_ci_pass: true
  require_commit_signing: true
  require_status_checks:
    - security/sast
    - security/sca
    - build/integrity
  force_push: false
  admin_override: false
```

**Layer 3: Build Tool Supply Chain**

Build tool integrity verification:
- All build tools (npm, Maven, Gradle, PIP, Go) downloaded via checksum verification
- Build tool vulnerabilities tracked; updates applied within 7 days

```bash
# npm example: verify integrity
npm ci --prefer-offline --no-audit  # Use lockfile, not package.json
npm audit --audit-level=moderate    # Fail on medium+ vulnerabilities

# Maven example: verify build tool version
mvn --version
# Compare SHA256 against Maven archive site

# Python example: verify pip integrity
python -m pip install --require-hashes -r requirements.txt
```

**Layer 4: Build Infrastructure Security**

Build runner security requirements:
- Build runners in isolated network segment; no internet access except to package registries
- Build runners ephemeral; destroyed after each build
- Build logs encrypted; retention 90 days then deleted
- Build runner images hardened: minimal packages, no development tools, readonly filesystem
- Hardware security: Build runner hosts protected by hardware TPM 2.0

```dockerfile
# Hardened build runner image (Alpine minimal)
FROM alpine:3.19

# Minimize image
RUN apk add --no-cache git openssh-client curl ca-certificates

# Create non-root builder user
RUN addgroup -g 1000 builder && adduser -D -u 1000 -G builder builder
USER builder:builder

# Read-only filesystem (enforced at runtime)
USER builder
WORKDIR /build
ENTRYPOINT ["sh", "-c"]

# Immutable volumes configuration
# - /build: tmpfs (non-persistent)
# - /: read-only except /tmp, /var/tmp
```

**Layer 5: Artifact Signing and Provenance**

All artifacts signed and verified:
- **Code signing:** Developer signs commit with GPG key
- **Build artifact signing:** Artifact signed immediately after build with HSM-backed key
- **Container signing:** Container image signed after push to registry (Cosign)
- **Binary signature:** Executable signed with organization certificate

Artifact provenance includes:
- Builder identity (certificate CN)
- Build timestamp
- Build environment fingerprint (OS, build tool versions)
- Input artifact hashes (source code, dependencies)
- Build command and parameters

```yaml
# Cosign example: sign container after build
cosign sign --key=hsm://pkcs11/token/key-label \
  ghcr.io/company/app:v1.2.3

# Verify signature at deployment time
cosign verify --key=cosign.pub \
  ghcr.io/company/app:v1.2.3

# in-toto provenance example
{
  "_type": "link",
  "signed": {
    "command": ["make", "build"],
    "environment": {
      "os": "linux",
      "go_version": "1.20.3"
    },
    "materials": {
      "src/main.go": {
        "sha256": "abc123def456..."
      }
    },
    "products": {
      "bin/app": {
        "sha256": "xyz789uvw012..."
      }
    },
    "byproducts": {
      "user": "builder@build.example.com",
      "timestamp": "2024-02-16T10:30:00Z"
    }
  },
  "signatures": [
    {
      "keyid": "...",
      "sig": "..."
    }
  ]
}
```

**Layer 6: Container Registry Security**

Registry requirements:
- Registry: Private container registry (not public Docker Hub)
- Access control: Role-based authentication; MFA for administrative access
- Image scanning: All images scanned for vulnerabilities before storage; critical images blocked
- Immutability: Images immutable after push; re-tag forces rebuild
- Retention: Images older than 90 days without deployment deleted

Registry policy:
```yaml
# Registry access policy
registries:
  gcr.io/company:
    pull_allowed: true
    push_allowed: only_ci_system
    image_scan_required: true
    vulnerability_threshold: CVSS 7.0
    
  docker.io:
    pull_allowed: false  # No public Docker Hub
    push_allowed: false
```

**Layer 7: Deployment Verification**

Deployment-time verification:
- Artifact signature verified against trusted key
- SBOM verified against expected dependencies
- Container image scanned for runtime vulnerabilities
- Deployment approval: manual gate for production

Deployment checklist:
```bash
# Pre-deployment verification script
#!/bin/bash

IMAGE=$1
MANIFEST=$2

# Verify image signature
cosign verify --key=cosign.pub "$IMAGE" || exit 1

# Verify SBOM
syft "$IMAGE" > actual-sbom.json
diff expected-sbom.json actual-sbom.json || exit 1

# Scan image
trivy image --severity HIGH,CRITICAL "$IMAGE" || exit 1

# Verify build audit trail
docker inspect "$IMAGE" --format='{{.Config.Labels.build_id}}'
# Cross-check against build system audit log

echo "All verification passed; deployment approved"
```

### Threat Scenarios and Mitigations

| Threat | Attack Vector | Mitigation | Detection |
|--------|---------------|-----------|-----------|
| Compromised developer machine | Malware injects code at commit time | Endpoint detection + code signing | Code review + signature verification |
| Compromised build tool | npm/Maven/PIP infected malware | Tool verification + isolated network | SAST scanning + provenance check |
| Compromised build infrastructure | Build runner access by attacker | Network isolation + runner ephemeral | Access logs + artifact signature verification |
| Typosquatting attack | Attacker publishes similarly-named package | Dependency allow-list + SCA scanning | SCA tool alerts + manual verification |
| Compromised CI/CD platform | Attacker gains pipeline access | Access control + audit logging | Anomalous build patterns + signature verification |
| Dependency version pinning | Attacker publishes malicious update to used version | Automatic SCA alerts + manual update review | Dependency-Check + license scanning |
| Container registry compromise | Attacker modifies stored image | Registry access control + signature verification | Image signature validation at deployment |

### Supply Chain Continuous Monitoring

**Monitoring dashboard (real-time):**

```yaml
metrics:
  - unverified_artifacts: 0  # All artifacts must have valid signature
  - unsigned_commits: 0
  - sast_findings_critical: 0
  - sca_vulnerabilities_high: <5
  - build_failures_security: 0
  - outdated_build_tools: 0
  - unsigned_deployments: 0
```

**Alerts:**
- Any new unverified artifact → immediate investigation
- Build tool update available → patch within 7 days
- Anomalous build pattern (different builder, unusual dependencies) → escalate
- Signature verification failure at deployment → block deployment

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Supply chain verification | A.8.19, A.8.31 | PW.4, PW.5 | SAMM | BAI07 |
| Provenance tracking | A.8.30, A.12.7 | RV.1, RV.2 | - | MEA02, MEA03 |
| Dependency management | A.8.31 | PW.4.1 | Dependency Check | BAI07.02 |

## Developer Checklist

Before implementing supply chain security:

- [ ] Developer machine security baseline deployed
- [ ] Source repository with branch protection configured
- [ ] Commit signing enforced (GPG/WebAuthn)
- [ ] Build tool verification implemented (npm ci, Maven checksum)
- [ ] Build infrastructure hardened and isolated
- [ ] Artifact signing with HSM keys configured
- [ ] Container registry secured with access control
- [ ] SBOM generation automated and stored
- [ ] Provenance tracking enabled (in-toto or equivalent)
- [ ] Deployment verification checklist created
- [ ] Supply chain monitoring dashboard configured
- [ ] Incident response for compromised artifacts documented

## Governance Implications

**Risk if not implemented:**
- Compromised developer machine = malware in production
- Unsigned build artifacts = unverifiable deployments
- Missing SBOM = unknown dependencies = undetectable supply chain attacks
- Unverified deployments = attacker-modified code in production

**Operational impact:**
- Build complexity increases initially (tool verification, signing)
- Deployment velocity decreases (manual verification gates)
- Incident response time decreases (automated verification catch compromises)
- Audit efficiency increases (provenance trail for investigation)

**Audit consequences:**
- Missing supply chain controls = NIST SSDF PW/RV findings
- No SBOM = non-compliance with NTIA minimum requirements
- Unverified artifacts = audit finding for change management

**Cross-team dependencies:**
- Development: commit signing, local machine security
- Platform: build infrastructure, artifact repository
- Security: supply chain monitoring, incident response
- Audit: provenance verification, exception approval

## Official References

- **NIST SP 800-218** – Secure Software Development Framework (PW, RV layers)
- **SLSA Framework** – Supply chain Levels for Software Artifacts (slsa.dev)
- **in-toto Framework** – Secure software supply chain (in-toto.io)
- **Sigstore Project** – Keyless code signing (sigstore.dev)
- **NTIA Minimum Elements** – Software Bill of Materials (SBOM)
- **ISO/IEC 27001:2022** – Information Security Management

## Version History

| Version | Date | Change Type | Description |
|---------|------|-------------|-------------|
| 1.0 | 2026-02-16 | Major | Initial supply chain security standard for Layer 08 |
