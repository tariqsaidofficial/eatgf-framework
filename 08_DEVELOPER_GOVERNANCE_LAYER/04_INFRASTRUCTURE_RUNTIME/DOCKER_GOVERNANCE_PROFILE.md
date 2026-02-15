# Docker Governance Profile

## Enterprise Container Runtime Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Infrastructure Runtime)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → 04_INFRASTRUCTURE_RUNTIME → CONTAINER_LAYER

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** container security controls from [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **extends** BACKEND framework profiles (Django, FastAPI, Node.js, Spring Boot) to production runtime
- This profile **defines** immutable infrastructure expectations
- This profile **does not** supersede networking/orchestration (see Kubernetes profile)

**COMPLIANCE STATEMENT:** This profile enforces mandatory controls for Docker image lifecycle, supply chain integrity, and runtime hardening. Non-conformance results in:

- Container breakout and privilege escalation
- Supply chain compromise via unsigned/unscanned images
- Cross-tenant data exposure via shared filesystem mounts
- Registry poisoning via unsigned artifact push
- Runtime isolation bypass via privileged containers

Docker represents the **CONTAINER_LAYER** where application code meets host OS. Security boundary must be enforced.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Docker containers supporting backend applications operating under EATGF.

**Scope:** Docker images, Dockerfile standards, image build pipelines, container registry operations, runtime container execution

**Non-Scope:** Docker Compose (single-host orchestration), Docker Swarm, proprietary container runtimes

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES (Application Layer)
│   ├── BACKEND (Django, FastAPI, Node.js, Spring Boot)
│   └── FRONTEND (8 frameworks)
└── 04_INFRASTRUCTURE_RUNTIME (Container + Orchestration)
    ├── DOCKER_GOVERNANCE (Container Layer) ← THIS PROFILE
    ├── KUBERNETES_GOVERNANCE (Orchestration Layer)
    ├── DATABASE_GOVERNANCE (Data Layer)
    ├── TERRAFORM_GOVERNANCE (Infrastructure as Code)
    └── CLOUD_RUNTIME_GOVERNANCE (Cloud Controls)
```

**Docker operates as:**

- Container image builder (Dockerfile-driven)
- Runtime enforcement boundary (user isolation, filesystem controls)
- Supply chain artifact (signed, scanned, versioned)
- Deployment unit (immutable from build → production)

**Critical Principle:** Immutable infrastructure. Containers built once, never modified post-build. All changes require rebuild.

---

## 3. Governance Principles

### Principle 1: Immutable Infrastructure (MANDATORY)

Containers must never be modified at runtime. Changes require rebuild.

```dockerfile
# ❌ PROHIBITED: Installation in running container
docker exec app apt-get install -y package

# ✅ COMPLIANT: Rebuild for any change
FROM python:3.12-slim

RUN pip install --no-cache-dir -r requirements.txt

# Rebuild and deploy: docker build -t app:v2 .
```

**Enforcement:**

- No `docker exec` write operations in production
- Filesystem mounted read-only by default
- Configuration via environment variables only
- Secrets injected at runtime (not built-in)

---

### Principle 2: Least Privilege Runtime User (MANDATORY)

Containers must not run as root. Non-root user required.

```dockerfile
# ❌ PROHIBITED: Root user
FROM python:3.12-slim
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
# Runs as root (UID 0)

# ✅ COMPLIANT: Non-root user
FROM python:3.12-slim

# Create user during build
RUN addgroup --system appgroup && \
    adduser --system appuser --ingroup appgroup

WORKDIR /app
COPY --chown=appuser:appgroup . .

# Switch to non-root
USER appuser

CMD ["python", "app.py"]
# Runs as appuser (UID > 1000)
```

**Enforcement:**

- USER directive mandatory in all Dockerfiles
- UID must be >= 1000 (non-system user)
- Verify at build-time: `docker inspect app:v1 | grep User`

---

### Principle 3: Minimal Base Images (MANDATORY)

Use minimal base images (`-slim`, `-alpine`, distroless).

```dockerfile
# ❌ NOT COMPLIANT: Unnecessary tools
FROM ubuntu:22.04  # ~77 MB, includes apt, systemd, etc.

# ✅ COMPLIANT: Minimal image
FROM python:3.12-slim  # ~125 MB, reduced attack surface
FROM gcr.io/distroless/python3  # ~68 MB, no shell

# Distroless best practice (if python not needed):
FROM gcr.io/distroless/base-debian12  # ~20 MB, only libc
```

**Attack Surface Reduction:**

- Remove curl, wget, netcat (command-line tools)
- Remove package managers (apt, yum)
- Remove shells (no `/bin/sh` in distroless)
- Each MB = potential vulnerability surface

---

### Principle 4: Supply Chain Integrity (MANDATORY)

Every image must be vulnerability-scanned, SBOM-generated, and cryptographically signed.

```bash
# ✅ COMPLIANT Build Pipeline
# 1. Build image
docker build -t myapp:${SHA} .

# 2. Scan for vulnerabilities (Trivy)
trivy image --severity CRITICAL,HIGH myapp:${SHA}
# ↑ Fails build if high-severity vulnerability found

# 3. Generate SBOM
syft packages docker:myapp:${SHA} -o json > sbom.json

# 4. Sign image with cosign
cosign sign --key cosign.key myapp:${SHA}

# 5. Push signed image to registry
docker push myapp:${SHA}
# ↑ Registry verifies signature before acceptance

# ❌ PROHIBITED: Unsigned push
docker push untrusted:latest  # No signature, no scan
```

**Enforcement:**

- CI/CD pipeline fails if scan detects high/critical CVE
- Unsigned images rejected by registry policy
- SBOM stored with artifact metadata

---

### Principle 5: Runtime Isolation Hardening (MANDATORY)

No container may:

- Run with `--privileged` flag
- Share Docker socket (`-v /var/run/docker.sock`)
- Use host network mode (`--net=host`)
- Mount host filesystem uncontrolled

```bash
# ❌ PROHIBITED: Privileged mode
docker run --privileged app  # Can escape to host

# ❌ PROHIBITED: Docker socket access
docker run -v /var/run/docker.sock:/var/run/docker.sock app
# Container becomes container manager (privilege escalation)

# ❌ PROHIBITED: Host network mode
docker run --net=host app  # No network isolation

# ✅ COMPLIANT: Default isolation
docker run \
  --read-only \
  --security-opt=no-new-privileges:true \
  --cap-drop=ALL \
  --cap-add=NET_BIND_SERVICE \
  myapp:v1

# ✅ COMPLIANT: Read-only root filesystem
docker run --read-only --tmpfs /tmp myapp:v1
# Only /tmp writable, everything else immutable
```

---

### Principle 6: Resource Limits (MANDATORY)

Every container must have CPU and memory limits defined.

```bash
# ❌ PROHIBITED: No limits
docker run app  # Can consume all host resources

# ✅ COMPLIANT: Resource limits
docker run \
  --memory=512m \
  --memswap=512m \
  --cpus=1.0 \
  --pids-limit=100 \
  app:v1

# Dockerfile equivalent (for Kubernetes)
# (See Kubernetes profile for pod resource requests)
```

---

### Principle 7: Health Checks & Observability (MANDATORY)

Containers must expose health status and metrics.

```dockerfile
# ✅ COMPLIANT: Built-in healthcheck
FROM python:3.12-slim

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:8000/health || exit 1

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

---

### Principle 8: Deterministic, Reproducible Builds (MANDATORY)

Builds must produce identical artifacts when source is identical.

```dockerfile
# ❌ NON-DETERMINISTIC: Latest dependencies
FROM python:3.12-slim
RUN pip install -r requirements.txt  # Latest versions installs

# ✅ COMPLIANT: Pinned dependencies
FROM python:3.12-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# requirements.txt contains exact versions:
# requests==2.31.0
# flask==3.0.0

# ✅ COMPLIANCE: Reproducible base image
FROM python:3.12.1-slim@sha256:abc123...
# Use digest pin, not tag, for immutability
```

---

## 4. Control 1: Authentication (Container Build)

**Objective:** Authenticate image builder, track image lineage.

### Requirement

- Build signed with developer identity (GIT_AUTHOR_NAME)
- Image tagged with build metadata
- Audit trail of who built which image

### Compliant Implementation

```bash
# ✅ COMPLIANT: Build with metadata
docker build \
  --label "maintainer=platform-security@example.com" \
  --label "build.date=$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
  --label "vcs.ref=${GITHUB_SHA}" \
  --label "vcs.url=${GITHUB_REPOSITORY}" \
  -t myapp:${GITHUB_SHA} \
  .

# Verify labels
docker inspect myapp:${GITHUB_SHA} | grep -A 20 Labels
```

### Non-Compliant Example

```bash
# ❌ VIOLATION: No build provenance
docker build -t app:latest .
# No metadata, unclear who built, when, from what source
```

---

## 5. Control 2: Authorization (Registry Access)

**Objective:** Control who can push/pull images from registry.

### Requirement

- Role-based access control (RBAC) on registry
- Only CI/CD service account can push
- Pull requires authentication

### Compliant Implementation

```bash
# ✅ COMPLIANT: Docker login with service account token
echo "${DOCKER_REGISTRY_TOKEN}" | docker login \
  -u ${DOCKER_REGISTRY_USER} \
  --password-stdin registry.example.com

# Push only via CI/CD authenticated session
docker push registry.example.com/myapp:${SHA}

# ✅ Restricted access: Only pushing from CI/CD IP
# Registry policy: Allow push only from CI IP 203.0.113.0/24
```

### Non-Compliant Example

```bash
# ❌ VIOLATION: Pushing without authentication
docker push untrusted.registry.io/malicious:latest

# ❌ VIOLATION: Hardcoded credentials
docker login -u admin -p hardcoded_password
echo "$DOCKER_PASSWORD" | docker login  # Plain text in logs
```

---

## 6. Control 3: Versioning

**Objective:** Immutable versioning scheme for images.

### Requirement

- Images tagged with git SHA (immutable)
- Semantic versioning for releases (v1.2.3)
- Digest-based pinning for reproducibility

### Compliant Implementation

```bash
# ✅ COMPLIANT: Git SHA tagging
docker build -t myapp:${GITHUB_SHA} .  # e.g., myapp:abc123def456

# ✅ COMPLIANT: Release versioning
docker tag myapp:${GITHUB_SHA} myapp:v1.2.3
docker tag myapp:${GITHUB_SHA} myapp:v1.2
docker tag myapp:${GITHUB_SHA} myapp:v1
docker tag myapp:${GITHUB_SHA} myapp:latest

# ✅ COMPLIANT: Digest-based deployment
docker pull myapp@sha256:abc123...  # Immutable by content hash
```

### Non-Compliant Example

```bash
# ❌ VIOLATION: Floating latest tag
docker tag local:builds myapp:latest
docker push myapp:latest
# Unclear which code version deployed, unpredictable behavior
```

---

## 7. Control 4: Input Validation (Configuration)

**Objective:** Validate environment variables and secrets injected at runtime.

### Requirement

- Runtime config validated against schema
- Secrets never hardcoded in image
- Environment variables sanitized

### Compliant Implementation

```dockerfile
# ✅ COMPLIANT: Expect env vars, no defaults for secrets
FROM python:3.12-slim

ENV DATABASE_URL=${DATABASE_URL:?DATABASE_URL required}
ENV JWT_SECRET=${JWT_SECRET:?JWT_SECRET required}

# Validate on startup
RUN --mount=type=secret,id=docker_config \
    echo "Secrets provided dynamically at runtime"
```

```bash
# ✅ COMPLIANT: Inject secrets at runtime
docker run \
  -e DATABASE_URL="postgres://..." \
  -e JWT_SECRET="$(aws secretsmanager get-secret-value ...)" \
  myapp:v1

# ✅ COMPLIANT: Docker secrets (Swarm/Kubernetes)
docker secret create db_password db_password.txt
docker service create \
  --secret db_password \
  -e DATABASE_PASSWORD_FILE=/run/secrets/db_password \
  myapp:v1
```

### Non-Compliant Example

```dockerfile
# ❌ VIOLATION: Hardcoded secrets
ENV JWT_SECRET="super-secret-key"
RUN echo "DB_PASSWORD=admin123" >> /etc/app/config

# Secrets exposed in image layers, accessible to all who pull
```

---

## 8. Control 5: Rate Limiting (Image Layer)

**Objective:** Control image build frequency, scan rate limits.

### Requirement

- Registry has rate limits enforced
- Scan operations throttled
- Pull rate limits per image

### Compliant Implementation

```bash
# ✅ COMPLIANT: Registry rate limiting configured
# Docker Hub limits: 100 pulls/6hr for anonymous, 200 for authenticated

# ✅ COMPLIANT: Respect limits in CI/CD
docker pull --retry-max=3 myapp:v1
# Backoff on rate limit (429 response)

# ✅ COMPLIANT: Cache images locally
docker pull myapp:v1
docker tag myapp:v1 local-registry/myapp:v1
# Reuse local copy to avoid repeated pulls
```

---

## 9. Control 6: Testing & Documentation

**Objective:** Test security and functionality of image.

### Requirement

- Image security tests (container escape, privilege checks)
- Functionality tests (app responds to health check)
- Documentation of image purpose and usage

### Compliant Implementation

```bash
# ✅ COMPLIANT: Functional testing
docker run myapp:test /bin/sh -c "python -m pytest tests/"

# ✅ COMPLIANT: Security testing
docker run myapp:test /bin/sh -c "
  # Verify non-root
  [ \$(id -u) -gt 0 ] || exit 1

  # Verify no dangerous tools
  ! which nc && \
  ! which curl && \
  ! which apt-get || exit 1
"

# ✅ COMPLIANT: Health check verification
docker run --health-cmd="curl localhost:8000/health" myapp:test
sleep 5
docker ps --filter "health=healthy" | grep myapp || exit 1
```

### Documentation

```dockerfile
# Dockerfile best practice
# Usage: docker build -t myapp:v1 .
# Run: docker run --rm --read-only myapp:v1
# Health: /health endpoint (port 8000)
# Logs: stdout (capture with docker logs)
# Config: DATABASE_URL, JWT_SECRET env vars
```

---

## 10. Control 7: Logging & Observability

**Objective:** Capture container lifecycle events and logs.

### Requirement

- Container logs streamed to stdout/stderr (Docker standard)
- Image metadata includes log format
- Build events logged with metadata

### Compliant Implementation

```dockerfile
# ✅ COMPLIANT: All logs to stdout
FROM python:3.12-slim

# Don't write to /var/log, write to stdout
CMD ["python", "-u", "app.py"]
# -u: unbuffered output to stdout

# Logging format (structured)
# {"timestamp": "2026-02-15T10:30:00Z", "level": "INFO", "message": "..."}
```

```bash
# ✅ Capture logs
docker logs myapp:v1

# ✅ Stream to logging infrastructure
docker run --log-driver=splunk myapp:v1
docker run --log-driver=awslogs myapp:v1
```

---

## 11. Control 8: Zero Trust Networking

**Objective:** Containers isolated by default, explicit network access.

### Requirement

- No inter-container communication by default
- Explicit port exposure only
- Network policies enforced at orchestration layer

### Compliant Implementation

```bash
# ✅ COMPLIANT: Minimal port exposure
docker run \
  -p 8000:8000 \  # Only expose application port
  --expose 8000 \
  myapp:v1

# ❌ PROHIBITED: Exposing all ports
docker run -P myapp:v1  # Exposes all EXPOSE ports unpredictably

# ✅ COMPLIANT: Custom bridge network isolation
docker network create app-network
docker run --network app-network --name api myapp:v1
docker run --network app-network --name worker myapp:v1
# Only api and worker can communicate, isolated from host
```

---

## 12. Multi-Tenancy Controls

**Objective:** Tenant data never leaks between container instances.

### Requirement

- Each tenant gets isolated container instance (or namespace)
- Secrets per-tenant injected separately
- Filesystem isolation at container boundary

### Compliant Implementation

```bash
# ✅ COMPLIANT: Per-tenant container instance
export TENANT_ID="tenant-abc"

docker run \
  -e TENANT_ID="${TENANT_ID}" \
  -e DATABASE_URL="postgres://tenant-abc-db" \
  -e JWT_SECRET="$(aws secrets tenant-${TENANT_ID}/jwt-key)" \
  --name "api-${TENANT_ID}" \
  myapp:v1

# Kubernetes equivalent (see Kubernetes profile):
# Each namespace gets separate container instance
# RBAC enforces tenant isolation
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** Base image and dependency integrity.

### Requirement

- Base images from trusted sources (official Docker, distroless)
- Platform-scans all dependencies
- SBOM tracks all transitive dependencies

### Compliant Implementation

```dockerfile
# ✅ COMPLIANT: Trusted base with digest pin
FROM python:3.12.1-slim@sha256:abc123def456...
# Pinned to specific digest (immutable by content)

# ✅ COMPLIANT: Example with distroless
FROM gcr.io/distroless/python3:nonroot@sha256:xyz789...

# ✅ COMPLIANT: Build with SBOM
FROM python:3.12-slim@sha256:...
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# SBOM generated in CI: syft packages docker:myapp:v1
```

```bash
# ❌ PROHIBITED: Floating base image tags
FROM ubuntu:latest  # Tag changes, unpredictable
FROM python:3.12   # Minor updates, unexpected dependency changes
```

---

## 14. Control Mapping

| EATGF Control            | ISO 27001:2022 | NIST SSDF 1.1 | OWASP SAMM   | NIST 800-53 | COBIT 2019 |
| ------------------------ | -------------- | ------------- | ------------ | ----------- | ---------- |
| Build Authentication     | A.8.2, A.8.5   | PS.2.1        | Build.1      | AC-2        | DSS05.02   |
| Registry Authorization   | A.8.5, A.8.9   | AS.1          | Build.3      | AC-3        | DSS05.03   |
| Image Versioning         | A.8.28         | PO.3, PO.4    | Build.2      | CM-3        | BAI09.02   |
| Configuration Validation | A.8.22         | PW.8          | Build.1      | CM-5        | DSS05.04   |
| Rate Limiting            | A.8.22         | PW.8          | Deprecated.1 | AC-6        | DSS01.05   |
| Testing                  | A.8.28         | PO.2, PO.3    | Build.2      | SA-3        | BAI03.07   |
| Logging                  | A.8.15, A.8.23 | RV.1          | Verify.2     | AU-2        | MEA01.02   |
| Zero Trust Network       | A.8.1, A.8.9   | PW.1          | Build.1      | SC-7        | DSS05.01   |

---

## 15. Developer Checklist

Before pushing Docker image to registry:

- [ ] Base image from trusted source (official or distroless)
- [ ] Base image pinned to digest (not floating tag)
- [ ] Non-root user created and used (USER directive)
- [ ] Minimal base image (`-slim`, `-alpine`, distroless)
- [ ] Trivy scan passes (no critical/high vulnerabilities)
- [ ] SBOM generated and stored with artifact
- [ ] Image signed with cosign/notation
- [ ] Healthcheck implemented (/health endpoint or process check)
- [ ] Resource limits documented (memory, CPU for Kubernetes)
- [ ] No hardcoded secrets in Dockerfile
- [ ] Read-only root filesystem compatible (--read-only flag)
- [ ] Build metadata: date, git SHA, maintainer labels
- [ ] Documentation: how to run, required env vars, port exposure
- [ ] Multi-stage build (if applicable) to minimize image size
- [ ] Deterministic build (pinned dependencies in requirements.txt)

---

## 16. Governance Implications

**Risk if not implemented:**

- **Supply Chain Compromise:** Unsigned/unscanned images → malicious code in production
- **Container Breakout:** Privileged containers → host OS compromise
- **Privilege Escalation:** Root user in container → escape to host with full permissions
- **Cross-Tenant Data Leak:** Shared filesystem mount → tenant data exposed
- **Audit Trail Loss:** No build metadata → cannot track who deployed what

**SOC2/ISO 27001 Impact:**

- **SOC2 CC6.1:** (Logical & Physical Access Controls) Registry must enforce authentication/RBAC
- **SOC2 CC6.2:** (Change Management) All image changes require rebuild, not runtime modification
- **ISO 27001 A.8.28:** (Supply Chain Management) SBOM, scanning, signing mandatory
- **ISO 27001 A.8.2:** (Privileged Access Rights) No root containers

**Operational Impact:**

- Container escape → complete host compromise
- Malicious artifact in registry → silent deployment of trojan
- Privilege escalation → lateral movement to other containers on same host

---

## 17. Implementation Risks

| Risk                    | Severity | Mitigation                                                  |
| ----------------------- | -------- | ----------------------------------------------------------- |
| Unsigned image deployed | CRITICAL | CI/CD rejects unsigned images; cosign verify on pull        |
| Running as root         | CRITICAL | USER directive non-negotiable; validate at scan-time        |
| Unscanned CVE           | HIGH     | Trivy scan fails build; waiver approval required            |
| Hardcoded secrets       | CRITICAL | Environment variable injection; secret scanning in CI       |
| No healthcheck          | MEDIUM   | Kubernetes liveness probe; automated restart on failure     |
| No resource limits      | MEDIUM   | Docker/Kubernetes resource requests; node pressure eviction |

---

## 18. Official References

**Normative (Governance):**

- NIST SP 800-218: Secure Software Development Framework (SSDF)
- ISO/IEC 27001:2022 Annex A: Control Objectives
- NIST SP 800-53 Rev. 5: Security & Privacy Controls

**Informative (Container Security):**

- CIS Docker Benchmark v1.7.0
- NIST Application Container Security Guide (SP 800-190)
- OCI Image Spec: <https://github.com/opencontainers/image-spec>
- Sigstore Cosign: <https://github.com/sigstore/cosign>
- Aquasecurity Trivy: <https://github.com/aquasecurity/trivy>
- SPDX SBOM Specification: <https://spdx.dev>

**Tools & Standards:**

- Docker Official Documentation
- Container Security Best Practices (SANS, Cloud Security Alliance)
- Supply Chain Levels for Software Artifacts (SLSA) Framework

---

## 19. Version Information

| Field                      | Value                                         |
| -------------------------- | --------------------------------------------- |
| **Document Version**       | 1.0                                           |
| **Change Type**            | Major (Initial Release)                       |
| **Issue Date**             | February 15, 2026                             |
| **EATGF Baseline**         | v1.0 (Layer 08 Infrastructure Runtime)        |
| **Docker Version**         | 24.0+ (moby engine)                           |
| **Kubernetes Requirement** | 1.24+ (for pod security standards)            |
| **Target Audience**        | DevSecOps engineers, platform engineers, SREs |

**Compliance Statement:** This profile is 100% conformant to EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md and enforces all governance principles at Layer 08, Infrastructure Runtime tier.

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)

**Supersedes:** N/A (new document)
**Superseded By:** None (active)
