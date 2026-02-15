# Cloud Runtime Governance Profile

**Version:** 1.0  
**Status:** Active  
**Last Updated:** 2026-02-15

## Authority Notice

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME  
**Governance Scope:** Implementation Standard  
**Control Authority:** Implements controls for cloud-native deployment governance  
**Authority Type:** DRI (Designated Responsible Individual) - Infrastructure Leadership

---

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
- **Governance Scope:** Implementation Standard
- **Control Authority:** Implements controls from API_GOVERNANCE_STANDARD

---

## Governance Principles

This profile enforces:

- **Security-by-Design:** Environment isolation, secrets injection at runtime
- **Control-Centric Architecture:** 8 mandatory controls + deployment approval
- **Versioned Governance:** Deployment versioning by git SHA, rollback capability
- **Developer-Operational Alignment:** Infrastructure-as-Code deployments, GitOps
- **Audit Traceability:** Deployment logs, actor tracking, change history
- **Single Source of Truth:** Configuration from version control, no manual changes

---

## Control Mapping

| EATGF Control | ISO 27001:2022 | NIST SSDF | OWASP SAMM | COBIT |
|---|---|---|---|---|
| Authentication (API Token) | A.8.2 | PW.4 | ASVS V1 | APO13 |
| Authorization (Scoped Perms) | A.8.2 | PW.4 | ASVS V4 | APO13 |
| Deployment Versioning | A.8.22 | PW.8 | Build.1 | DSS05 |
| Environment Validation | A.8.9 | PW.8 | ASVS V5 | CM-6 |
| Approval Gates | A.8.22 | PW.8 | Build.2 | DSS05 |
| Secrets Management | A.8.24 | PW.4 | ASVS V6 | IA-5 |
| Deployment Traceability | A.8.15 | RV.1 | Verify.1 | MEA01 |
| Rollback Procedures | A.8.13 | PW.8 | Verify.2 | CM-3 |

---

## Purpose

Define governance controls for deploying containerized applications to cloud platforms (Vercel, Railway, Heroku, fly.io, AWS ECS) with deployment traceability, approval gates, and rollback capabilities.

**Applies to:**

- Serverless platforms (Vercel, Netlify)
- Container platforms (Railway, Fly.io, Render)
- Platform-as-a-Service (Heroku)
- Managed Kubernetes (ECS, GKE, AKS)
- All production application deployments

---

## Technical Implementation

### Environment Isolation via Terraform

```hcl
# ✅ COMPLIANT: Separate projects/regions per environment
variable "environment" {
  type = string
  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production."
  }
}

locals {
  env_config = {
    dev = {
      region         = "us-west-2"
      instance_type  = "t3.small"
      db_size        = "db.t3.micro"
      memory_limit   = "512MB"
      log_retention  = 7  # days
    }
    staging = {
      region         = "us-east-1"
      instance_type  = "t3.medium"
      db_size        = "db.t3.small"
      memory_limit   = "1GB"
      log_retention  = 30
    }
    production = {
      region         = "us-east-1"
      instance_type  = "t3.large"
      db_size        = "db.t3.medium"
      memory_limit   = "2GB"
      log_retention  = 365
      multi_az       = true
      backup_window  = "03:00-04:00"
    }
  }
}
```

### Deployment Metadata & Traceability

```yaml
# ✅ COMPLIANT: Deployment record with git SHA + actor
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-deployment-metadata
  namespace: production
data:
  git_sha: "a3f5b8c1e2d9f4a6c7b8e9f0d1a2b3c4"
  git_branch: "main"
  git_author: "user@example.com"
  deployment_timestamp: "2026-02-15T14:23:45Z"
  ci_build_url: "https://github.com/org/repo/actions/runs/123456789"
  image_tag: "v1.2.3-a3f5b8c"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  namespace: production
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
        version: v1.2.3
      annotations:
        deployment.kubernetes.io/revision: "42"
        deployment-timestamp: "2026-02-15T14:23:45Z"
    spec:
      securityContext:
        runAsNonRoot: true
      containers:
      - name: api
        image: registry.example.com/app:v1.2.3@sha256:abc123...
        imagePullPolicy: Always
        env:
        - name: APP_ENV
          value: "production"
        - name: LOG_LEVEL
          value: "info"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
```

### Pre-Deployment Validation

```bash
#!/bin/bash
# ✅ COMPLIANT: Deployment gate validations

set -e

echo "=== Pre-Deployment Validation Gate ==="

# 1. Verify environment
if [[ "$ENVIRONMENT" != "production" ]] && [[ "$ENVIRONMENT" != "staging" ]]; then
  echo "ERROR: Invalid environment: $ENVIRONMENT"
  exit 1
fi

# 2. Check git branch (only main/release branches for prod)
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$ENVIRONMENT" == "production" ]] && [[ "$BRANCH" != "main" ]]; then
  echo "ERROR: Production deployments only from main branch. Current: $BRANCH"
  exit 1
fi

# 3. Verify Docker image exists and is signed
IMAGE_DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' "$IMAGE:$VERSION")
if ! cosign verify "$IMAGE_DIGEST" --key cosign.pub > /dev/null 2>&1; then
  echo "ERROR: Image not signed: $IMAGE_DIGEST"
  exit 1
fi

# 4. Run smoke tests
echo "Running smoke tests..."
docker run --rm \
  --env-file .env.test \
  "$IMAGE:$VERSION" \
  npm run test:smoke

# 5. Validate Kubernetes manifests
echo "Validating Kubernetes manifests..."
kubectl apply -f k8s/ --dry-run=client --validate=true

# 6. Check resource quotas
echo "Checking resource quotas..."
kubectl get quota -n "$NAMESPACE" -o json | \
  jq '.items[].status.used' | \
  jq 'to_entries | map(select(.value > 0.8))'

echo "✅ All validation gates passed. Ready for deployment approval."
```

### Approval & Rollback

```yaml
# ✅ COMPLIANT: Manual approval gate + automatic rollback
name: Deploy to Production
on:
  workflow_dispatch:
    inputs:
      version:
        required: true
        description: "Semver version (e.g., v1.2.3)"

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Pre-deployment validation
        run: |
          ./scripts/deploy/pre-deployment-check.sh \
            --environment production \
            --version ${{ github.event.inputs.version }}

  approval:
    needs: validate
    runs-on: ubuntu-latest
    environment:
      name: production
      # GitHub required approval from CODEOWNERS
    steps:
      - name: Approval gate
        run: |
          echo "Deployment approved by: $(git log -1 --format='%an <%ae>')"

  deploy:
    needs: approval
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to production
        run: |
          kubectl set image deployment/api \
            api=registry.example.com/app:${{ github.event.inputs.version }} \
            -n production

  rollback:
    if: failure()  # Automatic rollback on deploy failure
    needs: deploy
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Rollback to previous release
        run: |
          PREV_VERSION=$(kubectl get deployment api -n production \
            -o jsonpath='{.spec.template.spec.containers[0].image}' \
            | sed 's/.*://')

          kubectl rollout undo deployment/api -n production
          echo "Rolled back from $VERSION to $PREV_VERSION"
```

---

## Developer Checklist

- [ ] Deployment version matches git SHA or semantic version tag
- [ ] Environment variables injected at runtime (not in container)
- [ ] Secrets sourced from external vault (not in code)
- [ ] Database migrations run before application deployment
- [ ] Pre-deployment validation script passes (smoke tests)
- [ ] Health checks configured (readiness + liveness probes)
- [ ] Rollback procedure tested (previous version available)
- [ ] Deployment logs captured (actor, timestamp, version)
- [ ] Resource limits set (memory, CPU, disk space)
- [ ] Log retention policy enforced per environment
- [ ] Approval gate enforced for production (multi-approver)
- [ ] Deployment monitoring alerts configured (error rates, latency)
- [ ] Traffic policies defined (canary vs blue-green vs rolling)
- [ ] Cost governance applied (instance sizing, reserved capacity)
- [ ] Incident response playbook available (runbook)

---

## Governance Implications

### Risk if Not Implemented

- **Uncontrolled Deployments:** No approval gate → developers deploy directly
- **Configuration Drift:** Environment-specific config leads to inconsistency
- **Lost Deployment History:** No traceability → cannot audit who deployed what
- **Irreversible Failures:** No rollback procedure → outage becomes permanent
- **Secret Exposure:** Hardcoded secrets in deployment config → compromise

### Operational Impact

- Deployment failure without rollback capability → extended outage
- Inconsistent environments (dev ≠ staging ≠ prod) → works locally only
- Resource exhaustion → OOM kills/crashes, unplanned restarts
- Cost overruns → over-provisioned instances, unused resources

### Audit Consequences

- **ISO 27001 A.8.22:** Configuration management failure
- **SOC2 CC7.1:** Change management not enforced
- **PCI-DSS 6.5.10:** Broken access control (no deployment approval)

### Cross-Team Dependencies

- Platform team: Must operate approval workflow, monitor deployments
- Security team: Must define approval policy, secrets rotation schedule
- DevOps team: Must maintain rollback procedures, monitor health
- Development team: Must follow deployment gates, test rollbacks

---

## Official References

- GitHub Actions: <https://docs.github.com/en/actions/>
- GitLab CI/CD: <https://docs.gitlab.com/ee/ci/>
- NIST SP 800-218: Secure Software Development Framework
- Kubernetes Deployment: <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>
- Heroku Platform API: <https://devcenter.heroku.com/articles/platform-api-reference>

---

## Version Information

- **Version:** 1.0
- **Change Type:** Major (Initial Release)
- **Date:** 2026-02-15
- **Status:** Published
- **Target Audience:** DevOps engineers, platform teams, release managers
- **Platforms:** Vercel, Railway, Heroku, Fly.io, Render, ECS, GKE, AKS

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)
