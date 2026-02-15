# Policy-as-Code Profile (OPA/Kyverno)

> **Authority Notice:** This profile implements EATGF controls for declarative policy enforcement, compliance automation, and governance at admission/deployment time. It does NOT define new controls, redefine policies, or override standards. This profile clarifies HOW organizations satisfy Container Security (Layer 03), Governance Models (Layer 03), and compliance requirements per ISO 27001 A.8.1 and Kubernetes Network Policies.

## Purpose

Define governance controls for policy-as-code deployment, enabling declarative enforcement of security, compliance, and operational standards across CI/CD pipelines, container registries, and Kubernetes clusters without manual approval bottlenecks.

**Applies to:**

- Container image admission (signature verification, registry whitelisting)
- Pod security admission (privileged execution, volume mounts)
- Network policies (ingress/egress controls)
- Resource quotas and limits
- RBAC policy enforcement
- Configuration compliance (infrastructure code)
- Compliance audit automation

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME (Primary) + Layer 01 (Secure SDLC) + Layer 03 (DevSecOps)
- **Governance Scope:** Policy Declaration, Enforcement Engines, Compliance Automation, Admission Control
- **Control Authority:** Implements controls from MASTER_CONTROL_MATRIX for governance automation (ISO 27001 A.8.1, Kubernetes security hardening, CIS Kubernetes Benchmarks)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

Policy-as-Code profiles enforce:

- **Build-time policies:** Container registry scanning before push
- **Artifact signing:** Only signed images admitted to cluster
- **Dependency policies:** No images with CRITICAL vulnerabilities

### Layer 03: DevSecOps Governance

Policy-as-Code profiles reference:

- **Runtime policies:** Pod security standards (restricted, baseline, privileged)
- **Network policies:** Zero-trust segmentation
- **RBAC policies:** Least privilege service accounts
- **Configuration drift detection:** Declarative state management

### Layer 04: Infrastructure Runtime

Policy-as-Code profiles implement:

- **Admission webhooks:** Kyverno/OPA intercept pod creation
- **Policy repository:** Git-stored policies as source of truth
- **Audit logging:** Policy violations tracked with context

## Governance Principles

### 1. Declarative Policy as Source of Truth

All policies stored as code in version control, not on cluster.

```yaml
# ✅ COMPLIANT: Git-stored policy (Kyverno ClusterPolicy)
---
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-image-signature
  namespace: kyverno
spec:
  validationFailureAction: audit # block on production
  webhookTimeoutSeconds: 30
  failurePolicy: fail
  rules:
    - name: verify-cosign-signature
      match:
        resources:
          kinds:
            - Pod
            - Deployment
            - StatefulSet
      verifyImages:
        - imageReferences:
            - "gcr.io/prod/*"
          attestors:
            - name: verify-signature
              entries:
                - keys:
                    publicKeys: |
                      -----BEGIN PUBLIC KEY-----
                      MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE...
                      -----END PUBLIC KEY-----
                    signatureAlgorithm: sha256
                  conditions:
                    - key: "{{ signerProvider }}"
                      operator: Equals
                      value: "cosign"
```

**Violation:** Policies configured manually on cluster = MANDATORY failure

### 2. Multi-Engine Policy Coverage

Policies enforced at multiple points (registry, admission, runtime).

```bash
# ✅ COMPLIANT: Multi-layer enforcement
# Layer 1: Registry (Container scanning)
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image --severity CRITICAL,HIGH app:v1.0

# Layer 2: CI/CD (Signature verification)
cosign verify gcr.io/prod/app:v1.0

# Layer 3: Admission Control (Pod policy)
kubectl apply -f pod.yaml  # Kyverno/OPA validates

# Layer 4: Runtime (Network policies)
# Network policy: deny-all ingress, explicit allow rules
```

### 3. Compliance-Driven Policy

Policies directly reference compliance standards.

```yaml
# ✅ COMPLIANT: Compliance-mapped policy
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: enforce-pod-security-restricted
  labels:
    compliance: pci-dss
    control: "PCI-DSS Requirement 1.2"
    standard: "CIS Kubernetes 5.1"
spec:
  validationFailureAction: block
  rules:
    - name: restrict-running-as-root
      match:
        resources:
          kinds:
            - Pod
      validate:
        message: >-
          Running as root is not permitted.
          PCI-DSS 1.2: Establish and implement firewall and router
          standards to protect cardholder data. CIS K8s 5.1.1
        pattern:
          spec:
            securityContext:
              runAsNonRoot: true
              runAsUser: "!= 0"
```

### 4. Audit Trail for Policy Violations

All policy violations logged for forensics.

```json
{
  "audit_event": {
    "timestamp": "2026-02-15T10:30:00Z",
    "event_type": "POLICY_VIOLATION",
    "policy_name": "require-image-signature",
    "violating_resource": {
      "kind": "Pod",
      "namespace": "production",
      "name": "app-pod-xyz"
    },
    "violation_detail": {
      "rule_violated": "verify-cosign-signature",
      "reason": "image_signature_verification_failed",
      "image": "docker.io/app:unverified"
    },
    "enforcement_action": "blocked",
    "user": "deployment-service",
    "remediation": {
      "required_action": "use_signed_image_from_gcr.io/prod",
      "documentation": "https://wiki.org/signed-images"
    }
  }
}
```

### 5. Policy Exception Management

Exceptions tracked with expiration dates, not permanent.

```yaml
# ✅ COMPLIANT: Temporary exception with expiration
apiVersion: kyverno.io/v1
kind: ClusterPolicyException
metadata:
  name: legacy-app-temporary-exception
  namespace: kyverno
spec:
  exceptions:
    - ruleNames:
        - "require-image-signature"
      resources:
        selector:
          matchLabels:
            app: legacy-auth-service
  expirationTime: "2026-03-15T23:59:59Z" # Auto-revoke after expiration
  justification: "Legacy app requires 1-month remediation time per Risk Board"
  owner: "security@org"
  tracking_issue: "https://github.com/org/repo/issues/12345"
```

### 6. Automated Remediation

Policies can auto-remediate violations (e.g., add missing labels).

```yaml
# ✅ COMPLIANT: Mutating policy (auto-remediate)
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: add-security-labels
spec:
  validationFailureAction: audit
  rules:
    - name: add-compliance-labels
      match:
        resources:
          kinds:
            - Pod
      mutate:
        patchStrategicMerge:
          metadata:
            labels:
              compliance: "true"
              audit-date: "{{ now }}"
              policy-version: "v1.0"
        patchesJson6902:
          - op: add
            path: "/spec/securityContext/runAsNonRoot"
            value: true
```

## Governance Conformance

### Control 1: Declarative Policy Repository

**Root Standard:** ISO 27001 A.8.1 (Information security policies)

**Implementation Pattern:**

- All policies stored in Git repository
- Branch protection enforces peer review
- Policy changes audited via commit history
- Policy version tagged with release versions

**Compliant Example:**

```bash
# Git-based policy management
mkdir -p policies/security policies/compliance policies/operational

# Security policies
cat > policies/security/require-image-signature.yaml << 'EOF'
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-image-signature
spec:
  validationFailureAction: block
  rules:
  - name: check-image-signature
    match:
      resources:
        kinds:
        - Pod
    verifyImages:
    - imageReferences:
      - "gcr.io/prod/*"
      attestors:
      - name: check-cosign
        entries:
        - keys:
            publicKeys: |
              [PUBLIC_KEY_HERE]
            signatureAlgorithm: sha256
EOF

# Version control
git add policies/
git commit -m "Security: Add image signature verification policy (ISO-27001-A.8.1)"
git tag policy-v1.0.0

# Enforce policy changes via GitOps
kubectl apply -k policies/
```

### Control 2: Multi-Registry Image Admission

**Root Standard:** NIST SP 800-53 AC-2 (Account Management)

**Implementation Pattern:**

- Whitelist trusted registries (gcr.io, ECR, etc)
- Block images from untrusted registries
- OPA Rego enforces registry allowlist
- Exception process for temporary third-party images

**Compliant Example:**

```rego
# OPA/Rego policy: Registry Allowlist

package kubernetes.admission

import data.lib

deny[msg] {
    input.request.kind.kind == "Pod"
    image := input.request.object.spec.containers[_].image
    not registry_allowed(image)
    msg := sprintf("Image registry not whitelisted: %v", [image])
}

registry_allowed(image) {
    # Approved registries
    image_registry := split(image, "/")[0]
    registry := data.config.approved_registries[_]
    image_registry == registry
}

# Configuration (ConfigMap)
data.config.approved_registries = [
    "gcr.io",
    "us-docker.pkg.dev",
    "753453431143.dkr.ecr.us-east-1.amazonaws.com"
]
```

### Control 3: Pod Security Standard Enforcement

**Root Standard:** CIS Kubernetes Benchmarks 5.1+

**Implementation Pattern:**

- Kubernetes PSA (Pod Security Admission) configured
- Restricted/baseline/privileged labels on namespaces
- Kyverno policies enforce CIS benchmarks
- Runtime enforcement with audit logging

**Compliant Example:**

```yaml
# Kyverno policy: CIS 5.1.1 - RunAsNonRoot
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: cis-5-1-1-require-non-root
  labels:
    cis: "5.1.1"
spec:
  validationFailureAction: block
  rules:
    - name: check-runAsNonRoot
      match:
        resources:
          kinds:
            - Pod
            - Deployment
            - StatefulSet
            - DaemonSet
            - Job
      validate:
        message: "CIS 5.1.1: Pods must run as non-root user"
        pattern:
          spec:
            securityContext:
              runAsNonRoot: true
```

### Control 4: Network Policy Enforcement

**Root Standard:** ISO 27001 A.8.22 (Access Control)

**Implementation Pattern:**

- Deny-all ingress by default
- Explicit allow rules for known traffic
- DNS policy controls (CoreDNS access)
- Kyverno/Calico enforces policies

**Compliant Example:**

```yaml
# Default deny all ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress

---
# Explicit allow: frontend → backend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              tier: frontend
      ports:
        - protocol: TCP
          port: 8080

---
# Kyverno: Require NetworkPolicy on all namespaces
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-network-policy
spec:
  validationFailureAction: audit
  rules:
    - name: check-network-policy
      match:
        resources:
          kinds:
            - Namespace
      validate:
        message: >-
          Network policy required for security isolation.
          ISO-27001 A.8.22
        pattern:
          metadata:
            labels:
              network-policy: "enforced"
```

### Control 5: RBAC Policy Enforcement

**Root Standard:** ISO 27001 A.8.21 (Access Control)

**Implementation Pattern:**

- Least privilege service accounts (minimal permissions)
- Deny use of default service account
- Kyverno enforces RBAC policy
- Service account token restrictions

**Compliant Example:**

```yaml
# Kyverno: Least privilege RBAC
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: restrict-default-service-account
spec:
  validationFailureAction: block
  rules:
    - name: pod-spec-serviceaccount
      match:
        resources:
          kinds:
            - Pod
            - Deployment
            - StatefulSet
      validate:
        message: "Use of default service account is prohibited"
        pattern:
          spec:
            serviceAccountName: "!default"
            automountServiceAccountToken: false

---
# RBAC: Least privilege for application
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-service-account
  namespace: production

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-minimal-role
  namespace: production
rules:
  # Only required APIs
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list"]
    resourceNames: ["app-config"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]
    resourceNames: ["app-secrets"]
```

### Control 6: Configuration Drift Detection

**Root Standard:** ISO 27001 A.8.22 (Change Management)

**Implementation Pattern:**

- Continuous reconciliation (GitOps)
- Audit logging for manual changes (detected via webhooks)
- Policy drift triggers remediation
- Immutable configuration reference (Git SHA)

**Compliant Example:**

```yaml
# ArgoCD: Continuous deployment & drift detection
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: app-production
  namespace: argocd
spec:
  project: production
  source:
    repoURL: https://github.com/org/infrastructure
    targetRevision: main
    path: k8s/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true

---
# Kyverno: Detect manual changes
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: audit-manual-changes
spec:
  validationFailureAction: audit
  rules:
    - name: track-all-deployments
      match:
        resources:
          kinds:
            - Deployment
            - StatefulSet
            - DaemonSet
      validate:
        message: "Deployment changed manually (not via GitOps)"
        pattern:
          metadata:
            labels:
              "git-commit-sha": "?*"
```

### Control 7: Compliance Audit Automation

**Root Standard:** ISO 27001 A.8.15 (Monitoring & Logging)

**Implementation Pattern:**

- Monthly compliance report generated automatically
- Policy violations tied to compliance frameworks
- Remediation status tracked per control
- Audit trail exported for external auditors

**Compliant Example:**

```yaml
# Kyverno: Compliance audit policy
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: compliance-audit-check
  labels:
    compliance: all-frameworks
spec:
  validationFailureAction: audit
  rules:
    - name: cis-benchmark-check
      match:
        resources:
          kinds:
            - Pod
            - Deployment
            - Role
            - RoleBinding
            - ClusterRole
            - ClusterRoleBinding
      validate:
        message: |
          CIS Kubernetes Benchmark check: https://www.cisecurity.org/kubernetes
          This resource does not conform to CIS security controls.
        pattern:
          metadata:
            labels:
              "cis-compliance": "v1.6.0"
```

### Control 8: Exception Management Automation

**Root Standard:** ISO 27001 A.8.14 (Exception Process)

**Implementation Pattern:**

- Exceptions tracked in Git (merged PR = approved exception)
- Exception expiration enforced automatically
- Remediation tracked until exception expires
- Post-expiration: policy re-enforced automatically

**Compliant Example:**

```yaml
# ClusterPolicyException: Temporary override
apiVersion: kyverno.io/v1
kind: ClusterPolicyException
metadata:
  name: legacy-privileged-container-exception
  namespace: kyverno
spec:
  exceptions:
    - ruleNames:
        - "restrict-privileged-container"
      resources:
        selector:
          matchLabels:
            app: legacy-system
  expirationTime: "2026-04-15T23:59:59Z" # Must remediate by this date
  justification: >-
    Legacy system requires privileged capabilities.
    Remediation plan: Refactor to run unprivileged by Q2 2026.
    Risk accepted until 2026-04-15 by: CISO@org
  owner: "infrastructure-team@org"
  tracking_issue: "https://github.com/org/infrastructure/issues/5678"

---
# Kyverno: Auto-revoke expired exceptions
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: enforce-exception-expiration
spec:
  background: true
  validationFailureAction: block
  rules:
    - name: check-exception-not-expired
      match:
        resources:
          kinds:
            - ClusterPolicyException
      validate:
        message: >-
          Policy exception has expired.
          Reapply the policy or request new exception.
        pattern:
          spec:
            expirationTime: ">= {{ now }}"
```

## CI/CD Integration Gates

### Pre-Build Gate

```bash
- [ ] Policy repository cloned locally
- [ ] Policy syntax validated (kyverno apply --dry-run)
- [ ] Policy conflicts detected (overlapping rules)
```

### Build Gate

```bash
- [ ] Policy tests pass (unit tests for OPA/Kyverno)
- [ ] Policy rendered correctly (no template errors)
- [ ] Policy audit logging configured
```

### Pre-Deploy Gate

```bash
- [ ] Policy dry-run on test cluster (no violations)
- [ ] Exceptions reviewed and approved
- [ ] Policy version matches code release tag
```

### Deploy Gate

```bash
- [ ] Policies deployed before workloads
- [ ] Admission webhooks responding
- [ ] Policy violations captured (audit log streaming)
```

## Developer Checklist

Before deploying policy changes:

- [ ] **Policy syntax validated** (kyverno validate -f policy.yaml)
- [ ] **Policy conflicts resolved** (no overlapping deny/allow rules)
- [ ] **Compliance mapping documented** (which control addresses)
- [ ] **Exception expiration set** (no permanent exceptions)
- [ ] **Audit logging configured** (violations captured)
- [ ] **Tests written** (OPA test cases pass)
- [ ] **Dry-run on staging** (no unexpected denials)
- [ ] **Remediation time estimated** (time needed to comply)
- [ ] **Documentation updated** (developer guidance)
- [ ] **Emergency runbook prepared** (disable policy if broken)
- [ ] **Compliance scope verified** (applies to all namespaces)
- [ ] **Exception approval obtained** (Risk Board if temporary exception)

**Deployment blocked if any MANDATORY item fails.**

## Control Mapping

| EATGF Control                     | ISO 27001:2022 | NIST SSDF | OWASP SAMM | COBIT 2019 |
| --------------------------------- | -------------- | --------- | ---------- | ---------- |
| Declarative Policy Repository     | A.8.1          | PS.1      | Build.1    | BAI01      |
| Multi-Registry Image Admission    | A.8.21         | PS.2      | Build.2    | DSS05      |
| Pod Security Standard Enforcement | A.8.21         | RV.2      | Verify.1   | DSS01      |
| Network Policy Enforcement        | A.8.22         | RV.2      | Verify.1   | DSS05      |
| RBAC Policy Enforcement           | A.8.21         | PS.1      | Verify.1   | DSS01      |
| Configuration Drift Detection     | A.8.22         | RV.1      | Verify.2   | BAI09      |
| Compliance Audit Automation       | A.8.15         | RV.1      | Verify.3   | MEA02      |
| Exception Management Automation   | A.8.14         | RV.1      | Verify.1   | MEA01      |

## Governance Implications

### If Not Implemented

**Inconsistent Security Posture:**

- Risk: Pods run privileged on some clusters, restricted on others
- Impact: Attacker targets weakest cluster
- Audit finding: ISO 27001 A.8.21 (Access control) violation

**Manual Policy Bottleneck:**

- Risk: Security team approves policies manually (slow)
- Impact: Teams circumvent controls (shadow IT)
- Audit finding: A.8.1 (Policy effectiveness) violation

**No Compliance Automation:**

- Risk: Cannot prove compliance at audit time
- Impact: Audit failures, regulatory findings
- Audit finding: No compliance audit trail

**Configuration Drift:**

- Risk: Manual changes override policy
- Impact: Policy allows X, but manual config allows Y
- Audit finding: A.8.22 (Change management) violation

## Official References

- [OPA/Rego Documentation](https://www.openpolicyagent.org)
- [Kyverno Documentation](https://kyverno.io)
- [Kubernetes Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
- [CIS Kubernetes Benchmarks](https://www.cisecurity.org/benchmark/kubernetes)
- [ISO/IEC 27001:2022 A.8.1: Information Security Policies](https://www.iso.org/standard/27001)
- [NIST SP 800-53 AC-2: Account Management](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5)
- [Kubernetes RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

## Version Information

| Field              | Value                                |
| ------------------ | ------------------------------------ |
| **Version**        | 1.0                                  |
| **Release Date**   | 2026-02-15                           |
| **Change Type**    | Major (First Release)                |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)         |
| **Next Review**    | Q3 2026 (Kyverno v2.0 release)       |
| **Author**         | EATGF Governance Council             |
| **Status**         | Ready for Enterprise Deployment      |
| **Policy Engines** | OPA/Rego (v0.58+) + Kyverno (v1.10+) |
| **Audit Scope**    | ISO 27001 + CIS K8s + NIST SSDF      |
