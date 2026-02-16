# Docker Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Container building, scanning, signing, and supply chain integrity. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Docker/OCI containers satisfy DevSecOps (Layer 03), Infrastructure Runtime (Layer 04), and Supply Chain Security requirements.

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME (Primary) + Layer 03 (DevSecOps) + Layer 01 (Secure SDLC)
- **Governance Scope:** Implementation Standard for Container Supply Chain Security
- **Control Authority:** Implements controls from MASTER_CONTROL_MATRIX via Secure SDLC, DevSecOps, and Supply Chain Governance standards

---

## Governance Principles

This profile enforces:

- **Security-by-Design:** Container immutability, zero privilege runtime
- **Control-Centric Architecture:** 8 mandatory controls + supply chain governance
- **Versioned Governance:** Image tagging by git SHA, digest pinning
- **Developer-Operational Alignment:** Dockerfile standards + CI/CD scanning
- **Audit Traceability:** Image metadata, SBOM generation, signing verification
- **Single Source of Truth:** Official base images, no local builds

---

## Control Mapping

| EATGF Control              | ISO 27001:2022 | NIST SSDF | OWASP SAMM | COBIT |
| -------------------------- | -------------- | --------- | ---------- | ----- |
| Image Scanning             | A.8.8          | RV.1      | Verify.1   | APO13 |
| Image Signing              | A.8.24         | PS.2      | Build.1    | DSS05 |
| Least Privilege (non-root) | A.8.2          | PW.4      | ASVS V1    | APO13 |
| Runtime Hardening          | A.8.9          | PW.8      | ASVS V14   | CM-6  |
| Supply Chain Integrity     | A.8.28         | PS.1      | Build.2    | BAI09 |
| Dependency Governance      | A.8.15         | RV.1      | Verify.2   | MEA01 |
| Configuration Management   | A.8.22         | PW.8      | Build.1    | DSS05 |
| Secrets Exclusion          | A.8.12         | PW.4      | ASVS V6    | IA-5  |

---

## Purpose

Define governance controls for building, scanning, signing, and deploying Docker containers to ensure runtime integrity, immutability, and supply chain trust in production environments.

**Applies to:**

- REST APIs
- Microservices
- Background workers
- CI/CD agents
- All containerized workloads

---

## Technical Implementation

### Secure Dockerfile Standard

```dockerfile
#  COMPLIANT: Minimal base, non-root user
FROM python:3.12-slim@sha256:abc123...

RUN addgroup --system appgroup && \
    adduser --system appuser --ingroup appgroup

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER appuser

EXPOSE 8000
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

### CI/CD Scanning Pipeline

```bash
# Build with metadata
docker build -t app:$GITHUB_SHA \
  --label "vcs.ref=$GITHUB_SHA" \
  --label "maintainer=security@example.com" .

# Scan with Trivy (fail on HIGH/CRITICAL)
trivy image --severity CRITICAL,HIGH app:$GITHUB_SHA

# Generate SBOM
syft packages docker:app:$GITHUB_SHA -o json > sbom.json

# Sign image
cosign sign --key cosign.key app:$GITHUB_SHA

# Push signed image
docker push app:$GITHUB_SHA
```

### Runtime Hardening

```bash
#  COMPLIANT: Container execution
docker run \
  --user 1000:1000 \
  --read-only \
  --tmpfs /tmp \
  --cap-drop=ALL \
  --cap-add=NET_BIND_SERVICE \
  --memory=512m \
  --cpus=1.0 \
  --health-cmd="curl localhost:8000/health" \
  app:v1
```

---

## Developer Checklist

- [ ] Dockerfile uses minimal base image (slim, alpine, distroless)
- [ ] Non-root user created and set (USER directive)
- [ ] Base image pinned to digest (@sha256:...), not floating tag
- [ ] All dependencies pinned to exact versions (no ^ or ~)
- [ ] Trivy vulnerability scan passes (no CRITICAL/HIGH CVEs)
- [ ] SBOM generated and stored with artifact
- [ ] Image signed with cosign before registry push
- [ ] No hardcoded secrets in Dockerfile or image layers
- [ ] Read-only root filesystem compatible (--read-only flag tested)
- [ ] Healthcheck endpoint implemented (/health or equivalent)
- [ ] Resource limits documented (memory, CPU)
- [ ] Image build metadata included (labels)
- [ ] No curl, wget, shell in final image (if distroless)
- [ ] Multi-stage build used to minimize layer count
- [ ] CI/CD pipeline enforces all scanning checks before push

---

## Governance Implications

### Risk if Not Implemented

- **Supply Chain Compromise:** Unsigned/unscanned images → malicious code in production
- **Container Breakout:** Root user or privileged mode → host OS compromise
- **Dependency Vulnerability:** Outdated packages in image → known CVE exploitation
- **Audit Trail Loss:** No metadata → cannot trace who built image when

### Operational Impact

- Image escape → lateral movement to host and other containers
- Runtime privilege escalation → data breach of all container secrets
- Uncontrolled resource usage → node exhaustion, cluster instability

### Audit Consequences

- **ISO 27001 A.8.28:** Supply chain management failure
- **SOC2 CC6.1:** Access control violation (privileges not minimal)
- **PCI-DSS 6.5:** Vulnerability management failure

### Cross-Team Dependencies

- Security team: Must define acceptable CVE severity thresholds
- DevOps team: Must operate container registry with policy enforcement
- Development team: Must maintain Dockerfile standards and pass scans

---

## Official References

- NIST SP 800-218: Secure Software Development Framework (SSDF)
- ISO/IEC 27001:2022 Annex A: Control Objectives & Guidance
- NIST SP 800-53 Rev.5: Security & Privacy Controls for Information Systems
- CIS Docker Benchmark v1.7.0
- OWASP Container Security Top 10
- Sigstore Cosign Documentation: <https://docs.sigstore.dev/cosign/>
- Aquasecurity Trivy: <https://github.com/aquasecurity/trivy>

---

## Version Information

- **Version:** 1.0
- **Change Type:** Major (Initial Release)
- **Date:** 2026-02-15
- **Status:** Published
- **Target Audience:** DevSecOps engineers, platform teams, SREs
- **Docker Version:** 24.0+ (moby engine)
- **Kubernetes Version:** 1.24+ (if using K8s admission controllers)

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)
