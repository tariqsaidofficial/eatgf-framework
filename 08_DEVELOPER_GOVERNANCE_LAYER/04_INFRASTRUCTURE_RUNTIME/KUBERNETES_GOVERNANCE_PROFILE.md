# Kubernetes Governance Profile
## Enterprise Orchestration Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Infrastructure Runtime - Orchestration Layer)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → 04_INFRASTRUCTURE_RUNTIME → ORCHESTRATION_LAYER

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** orchestration security controls from [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **extends** DOCKER_GOVERNANCE_PROFILE.md (container runtime upstream)
- This profile **defines** cluster, namespace, pod, and network isolation requirements
- This profile **coordinates** with TERRAFORM_GOVERNANCE_PROFILE.md (cluster provisioning)
- This profile **does not** manage cloud infrastructure (see CLOUD_RUNTIME_GOVERNANCE_PROFILE.md)

**COMPLIANCE STATEMENT:** Kubernetes represents the **ORCHESTRATION_LAYER** where containers scale, communicate, and persist. Non-conformance results in:

- Pod-to-pod lateral movement (no network policy)
- Privilege escalation via unconstrained RBAC
- Cross-tenant namespace access
- Credential leakage via secret exposure in logs/etcd
- Resource exhaustion attacks (no limits)

Every Kubernetes cluster must enforce this profile.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Kubernetes clusters hosting backend applications under EATGF.

**Scope:** Kubernetes API server configuration, pod security policies/standards, network policies, RBAC, secrets management, resource limits, cluster-wide controls

**Non-Scope:** Container image security (see Docker profile), Cloud infrastructure provisioning (see Terraform profile), Application configuration management

**Kubernetes Versions:** 1.24+ (Pod Security Admission GA)

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES (Application Layer)
│   ├── BACKEND (Django, FastAPI, Node.js, Spring Boot)
│   └── FRONTEND (8 frameworks)
└── 04_INFRASTRUCTURE_RUNTIME (Container + Orchestration)
    ├── DOCKER_GOVERNANCE (Container Layer)
    ├── KUBERNETES_GOVERNANCE (Orchestration Layer) ← THIS PROFILE
    ├── DATABASE_GOVERNANCE (Data Layer)
    ├── TERRAFORM_GOVERNANCE (Infrastructure as Code)
    └── CLOUD_RUNTIME_GOVERNANCE (Cloud Controls)
```

**Kubernetes operates as:**

- Scheduler of container workloads across nodes
- Network policy enforcer (pod-to-pod communication)
- Secret/config management (etcd-backed, encrypted)
- RBAC enforcer (API server access control)
- Volume orchestrator (persistent data, pod ephemeral storage)

**Critical Principle:** Zero-trust cluster. All communication denied by default, explicit allow-rules only.

---

## 3. Governance Principles

### Principle 1: Pod Security & Reduced Capabilities (MANDATORY)

Pods must run with minimal Linux capabilities, no privileged mode.

```yaml
# ❌ PROHIBITED: Privileged pod
apiVersion: v1
kind: Pod
metadata:
  name: vulnerable-pod
spec:
  containers:
  - name: app
    image: myapp:v1
    securityContext:
      privileged: true  # Can escape to host OS

# ✅ COMPLIANT: Restricted pod
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:v1
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
        add:
        - NET_BIND_SERVICE  # Only required capability
      readOnlyRootFilesystem: true
    volumeMounts:
    - name: tmp
      mountPath: /tmp
  volumes:
  - name: tmp
    emptyDir: {}
```

---

### Principle 2: Network Policy Default Deny (MANDATORY)

All inter-pod traffic denied by default. Explicit allow-rules only.

```yaml
# ✅ COMPLIANT: Default deny ingress & egress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: tenant-abc
spec:
  podSelector: {} # Applies to all pods
  policyTypes:
    - Ingress
    - Egress

---
# ✅ COMPLIANT: Allow specific traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-to-db
  namespace: tenant-abc
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: api
      ports:
        - protocol: TCP
          port: 5432

# ❌ PROHIBITED: No network policy (allow-all)
# Pods communicate freely (violates zero-trust)
```

---

### Principle 3: RBAC Least Privilege (MANDATORY)

All service accounts have minimal permissions. No cluster-admin for applications.

```yaml
# ✅ COMPLIANT: Minimal role for app
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-app
  namespace: tenant-abc

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: api-app-role
  namespace: tenant-abc
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list"] # Only read config
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"] # Only read secret names (not values)

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: api-app-binding
  namespace: tenant-abc
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: api-app-role
subjects:
  - kind: ServiceAccount
    name: api-app
    namespace: tenant-abc

# ❌ PROHIBITED: Cluster-admin for app
# apiVersion: rbac.authorization.k8s.io/v1
# kind: ClusterRoleBinding
# metadata:
#   name: app-admin
# roleRef:
#   apiGroup: rbac.authorization.k8s.io
#   kind: ClusterRole
#   name: cluster-admin
# subjects:
# - kind: ServiceAccount
#   name: api-app
#   namespace: tenant-abc
```

---

### Principle 4: Secret Management Without Exposure (MANDATORY)

Secrets stored in Kubernetes Secrets (encrypted etcd), not in Deployments/logs.

```yaml
# ✅ COMPLIANT: Secret separated from deployment
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: tenant-abc
type: Opaque
stringData:
  database-url: "postgres://..."
  jwt-secret: "..." # Only in Secret, not in code/manifest

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  namespace: tenant-abc
spec:
  template:
    spec:
      containers:
        - name: app
          image: myapp:v1
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: app-secrets
                  key: database-url
            - name: JWT_SECRET
              valueFrom:
                secretKeyRef:
                  name: app-secrets
                  key: jwt-secret

# ❌ PROHIBITED: Secret in deployment
# env:
# - name: DATABASE_URL
#   value: "postgres://user:password@host/db"  # Visible in manifest
#
# ❌ PROHIBITED: Secret in logs
# RUN echo $DATABASE_URL > /var/log/config  # Leaks in container logs
```

---

### Principle 5: Resource Limits & Quotas (MANDATORY)

All pods have CPU/memory limits. Namespaces have aggregate quotas.

```yaml
# ✅ COMPLIANT: Pod resource limits
apiVersion: v1
kind: Pod
metadata:
  name: api-pod
spec:
  containers:
    - name: app
      image: myapp:v1
      resources:
        requests: # Scheduler reserve this amount
          memory: "256Mi"
          cpu: "500m"
        limits: # Pod capped at this amount
          memory: "512Mi"
          cpu: "1000m"

---
# ✅ COMPLIANT: Namespace quota
apiVersion: v1
kind: ResourceQuota
metadata:
  name: tenant-abc-quota
  namespace: tenant-abc
spec:
  hard:
    requests.cpu: "10" # Max 10 CPU cores total
    requests.memory: "40Gi" # Max 40GB RAM total
    pods: "300" # Max 300 pods

---
# ✅ COMPLIANT: Pod disruption budget
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: api-pdb
  namespace: tenant-abc
spec:
  minAvailable: 2 # Always keep 2 replicas available
  selector:
    matchLabels:
      app: api
```

---

### Principle 6: Multi-Tenancy Namespace Isolation (MANDATORY)

Each tenant gets isolated namespace, RBAC enforces access.

```yaml
# ✅ COMPLIANT: Per-tenant namespace
apiVersion: v1
kind: Namespace
metadata:
  name: tenant-abc
  labels:
    tenant: abc
    data-classification: confidential

---
# ✅ COMPLIANT: Tenant admin RBAC
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: tenant-admin
rules:
  - apiGroups: ["apps", "batch", ""]
    resources: ["*"]
    verbs: ["*"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: tenant-abc-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: tenant-admin
subjects:
  - kind: User
    name: "tenant-abc-admin@example.com"

# ❌ PROHIBITED: Cross-namespace pod communication
# Without NetworkPolicy, pods in tenant-abc can reach tenant-xyz pods
```

---

### Principle 7: Audit & Compliance Logging (MANDATORY)

All API server authentication, authorization, and configuration changes logged.

```yaml
# ✅ COMPLIANT: Audit policy (apiserver config)
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  - level: RequestResponse
    omitStages:
      - RequestReceived
    resources:
      - group: ""
        resources: ["secrets"] # Log all secret access
    namespaces: ["*"]
  - level: Metadata
    resources:
      - group: "rbac.authorization.k8s.io"
        resources: ["roles", "rolebindings"] # Log RBAC changes
  - level: Metadata
    verbs: ["create", "update", "patch", "delete"] # Log modifications
  - level: RequestResponse
    omitStages:
      - RequestReceived
    users: ["system:unauthenticated"] # Log all anonymous requests
  - level: Metadata
    omitStages:
      - RequestReceived
    resources:
      - group: ""
        resources: ["*"]

# ❌ PROHIBITED: No audit logging
# Cannot trace who accessed secrets, modified RBAC
```

---

### Principle 8: Secure Control Plane (MANDATORY)

API server, etcd, scheduler, controller-manager hardened.

```yaml
# ✅ COMPLIANT: Secure kubeadm configuration
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
etcd:
  local:
    dataDir: /var/lib/etcd
    extraArgs:
      cipher-suites: "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
      client-auto-tls: "false"
apiServer:
  extraArgs:
    # Disable anonymous access
    anonymous-auth: "false"
    # Enforce API server authentication
    basic-auth-file: "" # Don't use basic auth
    # Enable audit logging
    audit-policy-file: /etc/kubernetes/audit-policy.yaml
    audit-log-maxage: "7"
    # Enable RBAC
    authorization-mode: "RBAC"
    # Enforce encryption at rest
    encryption-provider-config: /etc/kubernetes/encryption-config.yaml
    # TLS version
    tls-min-version: "VersionTLS12"
controllerManager:
  extraArgs:
    # Feature gates for security
    feature-gates: "PodSecurityPolicy=true,LegacyServiceAccount=false"
scheduler:
  extraArgs:
    feature-gates: "PodSecurityPolicy=true"
```

---

## 4. Control 1: Authentication (API Server Access)

**Objective:** Authenticate all API server access, audit failed attempts.

### Requirement

- All requests authenticated (no anonymous)
- Service accounts for pod-to-API communication
- Human users via OIDC or certificates

### Compliant Implementation

```bash
# ✅ COMPLIANT: Create service account for app
kubectl create serviceaccount api-app -n tenant-abc

# ✅ COMPLIANT: Verify service account has token
kubectl get secret -n tenant-abc \
  $(kubectl get secret -n tenant-abc | grep api-app-token | awk '{print $1}')

# ✅ COMPLIANT: Disable anonymous access
kubectl apply -f - <<EOF
apiVersion: v1
kind: ConfigMap
metadata:
  name: kube-apiserver-audit
  namespace: kube-system
data:
  anonymous-auth: "false"
EOF

# ❌ PROHIBITED: Anonymous API access
# curl -k https://cluster-ip:443/api/v1/secrets  # No authentication
```

---

## 5. Control 2: Authorization (RBAC)

**Objective:** Role-based access control for API operations.

### Requirement

- Minimal permissions per service account
- No cluster-admin for applications
- Deny-all default policy

### Compliant Implementation

```bash
# ✅ COMPLIANT: List roles available
kubectl get roles -A

# ✅ COMPLIANT: Verify pod service account permissions
kubectl auth can-i get secrets --as=system:serviceaccount:tenant-abc:api-app -n tenant-abc
# should output: no (because of explicit deny-all role)

# ✅ COMPLIANT: Create restricted role
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: api-reader
  namespace: tenant-abc
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
EOF

# ❌ PROHIBITED: Granting cluster-admin to namespace
# kubectl create clusterrolebinding app-admin \
#   --clusterrole=cluster-admin \
#   --serviceaccount=tenant-abc:api-app
```

---

## 6. Control 3: Versioning (API Server, etcd, kubelet)

**Objective:** Track and enforce consistent cluster versions.

### Requirement

- Single control plane version
- All nodes within N-2 minor version skew
- etcd version matches apiserver

### Compliant Implementation

```bash
# ✅ COMPLIANT: Check cluster version
kubectl version --short
# Server Version: v1.28.3
# All nodes should be within N-2: 1.26.x, 1.27.x, 1.28.x

# ✅ COMPLIANT: Verify node versions
kubectl get nodes -o wide
NAME             VERSION
worker-001       v1.28.3
worker-002       v1.28.3

# ❌ PROHIBITED: Skewed versions
# Control plane: v1.28
# Node 1: v1.25 (too old, N-3)
```

---

## 7. Control 4: Input Validation (Pod/Deployment Specs)

**Objective:** Validate all pod specifications against security policies.

### Requirement

- Pod Security Standards enforced
- Admission webhooks validate configs
- No privileged, hostNetwork, hostPID pods

### Compliant Implementation

```yaml
# ✅ COMPLIANT: Pod Security Policy / Pod Security Admission
apiVersion: policy.k8s.io/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
  - ALL
  volumes:
  - 'configMap'
  - 'emptyDir'
  - 'projected'
  - 'secret'
  - 'downwardAPI'
  - 'persistentVolumeClaim'
  hostNetwork: false
  hostIPC: false
  hostPID: false
  runAsUser:
    rule: 'MustRunAsNonRoot'
  seLinux:
    rule: 'MustRunAs'
  fsGroup:
    rule: 'MustRunAs'
  readOnlyRootFilesystem: true

# ❌ PROHIBITED: Unvalidated pod spec
apiVersion: v1
kind: Pod
metadata:
  name: bad-pod
spec:
  hostNetwork: true  # Uses host network (security violation)
  containers:
  - name: app
    image: myapp:v1
    securityContext:
      privileged: true  # Violates policy
```

---

## 8. Control 5: Rate Limiting (API Server Throttling)

**Objective:** Prevent API server denial-of-service.

### Requirement

- API server request throttling enabled
- Per-namespace resource quotas
- Eviction policies on resource pressure

### Compliant Implementation

```yaml
# ✅ COMPLIANT: API server rate limiting
apiVersion: v1
kind: ConfigMap
metadata:
  name: kube-apiserver-config
  namespace: kube-system
data:
  rate-limit-config: |
    --max-requests-inflight=400
    --max-mutating-requests-inflight=200

---
# ✅ COMPLIANT: Namespace quota (limits request rate indirectly)
apiVersion: v1
kind: ResourceQuota
metadata:
  name: tenant-abc-quota
  namespace: tenant-abc
spec:
  hard:
    pods: "300"
    services: "10"
    persistentvolumeclaims: "10"

---
# ✅ COMPLIANT: Eviction policy
apiVersion: v1
kind: ConfigMap
metadata:
  name: kubelet-eviction
  namespace: kube-system
data:
  eviction-policy: |
    --eviction-hard=memory.available<100Mi,nodefs.available<10%
    --eviction-soft=memory.available<500Mi
    --eviction-soft-grace-period=memory.available=5m
```

---

## 9. Control 6: Testing & Policy Validation

**Objective:** Test cluster compliance before deployment.

### Requirement

- Pod security scanning (kubesec, kube-bench)
- Policy validation in CI/CD
- Admission webhooks reject violations

### Compliant Implementation

```bash
# ✅ COMPLIANT: Scan Kubernetes manifest
kubesec scan deployment.yaml
# Output: Advises on security improvements, fails on critical issues

# ✅ COMPLIANT: Run kube-bench
kube-bench run --targets master,node
# CIS Kubernetes Benchmark compliance check

# ✅ COMPLIANT: Validating admission webhook
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: pod-security-webhook
webhooks:
- name: pod-security.k8s.io
  rules:
  - operations: ["CREATE", "UPDATE"]
    apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods"]
  clientConfig:
    service:
      name: admission-webhook
      namespace: kube-system
      path: "/validate"
    caBundle: LS0tLS1CRUd...
  sideEffects: None
  admissionReviewVersions: ["v1"]
  clientConfig:
    timeoutSeconds: 3
```

---

## 10. Control 7: Logging & Audit Trail

**Objective:** Audit all secret access, RBAC changes, authentication events.

### Requirement

- API audit logging enabled
- Secret access logged
- Failed authentication attempts captured

### Compliant Implementation

```bash
# ✅ COMPLIANT: Query audit logs
kubectl logs -n kube-system -l component=kube-apiserver | grep audit

# Sample audit log entry (JSON):
{
  "level": "RequestResponse",
  "auditID": "abc-123",
  "stage": "ResponseComplete",
  "requestObject": {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {
      "name": "db-password",
      "namespace": "tenant-abc"
    }
  },
  "user": {
    "username": "system:serviceaccount:tenant-abc:api-app",
    "uid": "...",
    "groups": ["system:serviceaccounts", "system:serviceaccounts:tenant-abc"]
  },
  "verb": "get",
  "requestReceivedTimestamp": "2026-02-15T10:30:00Z",
  "responseStatus": {
    "code": 200
  }
}

# ❌ PROHIBITED: No audit logging
# Secret access invisible, cannot trace data access
```

---

## 11. Control 8: Zero Trust Network Policy

**Objective:** Enforce network isolation between pods/namespaces.

### Requirement

- Default deny network policies
- Explicit allow-rules only
- Namespace isolation
- Egress filtering to external networks

### Compliant Implementation

```yaml
# ✅ COMPLIANT: Deny all ingress & egress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: tenant-abc
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress

---
# ✅ COMPLIANT: Allow ingress from load balancer
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ingress-from-lb
  namespace: tenant-abc
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - protocol: TCP
          port: 8000

---
# ✅ COMPLIANT: Allow egress to DNS & external API
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-egress-dns-api
  namespace: tenant-abc
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Egress
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              name: kube-system
      ports:
        - protocol: UDP
          port: 53 # DNS
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - protocol: TCP
          port: 5432 # PostgreSQL


# ❌ PROHIBITED: No network policy = allow-all
# Pods communicate laterally, cross-tenant movement possible
```

---

## 12. Multi-Tenancy Controls

**Objective:** Namespace isolation, separate RBAC, network policies per tenant.

### Requirement

- Separate namespace per tenant
- RBAC prevents cross-namespace access
- Network policies limit tenant-to-tenant communication

### Compliant Implementation

```yaml
# ✅ COMPLIANT: Multi-tenant cluster setup
---
# Tenant A
apiVersion: v1
kind: Namespace
metadata:
  name: tenant-a
  labels:
    tenant: a

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: tenant-a-admin
  namespace: tenant-a
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: edit
subjects:
  - kind: User
    name: "tenant-a-admin@example.com"

---
# Tenant B (isolated)
apiVersion: v1
kind: Namespace
metadata:
  name: tenant-b
  labels:
    tenant: b

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: tenant-b-admin
  namespace: tenant-b
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: edit
subjects:
  - kind: User
    name: "tenant-b-admin@example.com"

---
# Deny cross-tenant communication
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-from-other-tenants
  namespace: tenant-a
spec:
  podSelector: {}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector: {} # Only from same namespace
          namespaceSelector:
            matchLabels:
              tenant: a
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** Container images verified before pod creation, signed images only.

### Requirement

- Image pull policy: always pull
- Signed images verified (cosign, notation)
- Registry enforces signature verification

### Compliant Implementation

```yaml
# ✅ COMPLIANT: Always pull with signature verification
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  namespace: tenant-abc
spec:
  template:
    spec:
      imagePullPolicy: Always # Re-verify on every pod start
      containers:
        - name: app
          image: registry.example.com/myapp:v1@sha256:abc123...
          # Digest pin ensures immutability

---
# ✅ COMPLIANT: Image signature verification webhook
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: image-signature-verification
webhooks:
  - name: verify-image-signature.example.com
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
    clientConfig:
      service:
        name: image-verification
        namespace: kube-system
    sideEffects: None

# ❌ PROHIBITED: Unsigned image pull
# image: registry.example.com/untrusted:latest
# No signature verification, malicious image possible
```

---

## 14. Control Mapping

| EATGF Control        | ISO 27001:2022 | NIST SSDF 1.1 | OWASP SAMM   | NIST 800-53 | COBIT 2019 |
| -------------------- | -------------- | ------------- | ------------ | ----------- | ---------- |
| API Authentication   | A.8.2, A.8.5   | AS.1          | Governance.1 | AC-2        | DSS05.01   |
| RBAC Authorization   | A.8.5, A.8.9   | AS.1, AS.2    | Governance.2 | AC-3, AC-6  | DSS05.03   |
| Version Control      | A.8.28         | PO.3          | Build.1      | CM-3        | BAI09.02   |
| Pod Input Validation | A.8.22         | PW.8          | Build.2      | CM-5        | DSS05.04   |
| Rate Limiting        | A.8.22         | PW.8          | Verify.1     | SC-5        | DSS01.05   |
| Admission Testing    | A.8.28         | PO.2          | Build.3      | SA-3        | BAI03.07   |
| Audit Logging        | A.8.15, A.8.23 | RV.1          | Verify.3     | AU-2        | MEA01.02   |
| Network Policy       | A.8.1, A.8.9   | PW.1          | Verify.1     | SC-7        | DSS05.02   |

---

## 15. Developer Checklist

Before deploying to production Kubernetes cluster:

- [ ] Namespace created with tenant label
- [ ] Network policy: default deny-all ingress/egress
- [ ] Network policy: explicit allow for application traffic
- [ ] Service account created with minimal RBAC role
- [ ] Deployment uses non-root user (runAsNonRoot: true)
- [ ] All containers have resource requests/limits set
- [ ] Pod security context: dropped capabilities, read-only filesystem
- [ ] Secrets managed via Kubernetes Secrets (not ConfigMaps)
- [ ] Audit logging configured and captured
- [ ] Pod Disruption Budget defined (for high-availability)
- [ ] Health checks: liveness and readiness probes configured
- [ ] Container image uses digest pin (immutable)
- [ ] Image signature verification enabled
- [ ] No hostPath volumes, no privileged mounts
- [ ] Cluster has encryption at rest enabled (etcd)
- [ ] API server has anonymous-auth: false

---

## 16. Governance Implications

**Risk if not implemented:**

- **Lateral Movement:** No network policy → pod-to-pod compromise spreads to all pods
- **Privilege Escalation:** RBAC misconfiguration → app gains cluster-admin
- **Secret Exposure:** Secrets in etcd → data breach on node compromise
- **Cross-Tenant Access:** RBAC violation → tenant A accesses tenant B data
- **API Abuse:** No rate limit → DDoS on API server

**SOC2/ISO 27001 Impact:**

- **SOC2 CC6.1:** Network policies enforce logical access controls
- **SOC2 CC6.2:** Audit logging satisfies change management requirements
- **ISO 27001 A.8.22:** Input validation prevents container escape
- **ISO 27001 A.8.9:** RBAC enforces access control

**Operational Impact:**

- Compromised pod → can access other pods' secrets if no network policy
- RBAC error → application gains unintended permissions

---

## 17. Implementation Risks

| Risk                     | Severity | Mitigation                                  |
| ------------------------ | -------- | ------------------------------------------- |
| No network policy        | CRITICAL | Default deny-all; explicit allow rules      |
| RBAC overpermission      | CRITICAL | Audit pod service account permissions       |
| Secrets in logs          | HIGH     | Log redaction; secure audit storage         |
| Unencrypted etcd         | HIGH     | Enable EncryptionConfiguration in apiserver |
| No pod disruption budget | MEDIUM   | Define PDB for high-availability            |
| Unvalidated pod specs    | MEDIUM   | ValidatingWebhook + PodSecurityPolicy       |

---

## 18. Official References

**Normative (Governance):**

- NIST SP 800-218: Secure Software Development Framework (SSDF)
- ISO/IEC 27001:2022 Annex A: Control Objectives
- NIST SP 800-53 Rev. 5: Security & Privacy Controls

**Informative (Kubernetes Security):**

- CIS Kubernetes Benchmark v1.8.0
- NIST Application Container Security Guide (SP 800-190)
- Kubernetes Security Best Practices Documentation
- PodSecurityPolicy (deprecated) → Pod Security Admission (1.24+)
- OWASP Container Security Top 10

**Tools & Standards:**

- Kubernetes Official Documentation
- kubesec: <https://kubesec.io/>
- kube-bench: <https://github.com/aquasecurity/kube-bench>
- Falco: Runtime security
- Cilium: eBPF-based networking & security

---

## 19. Version Information

| Field                  | Value                                  |
| ---------------------- | -------------------------------------- |
| **Document Version**   | 1.0                                    |
| **Change Type**        | Major (Initial Release)                |
| **Issue Date**         | February 15, 2026                      |
| **EATGF Baseline**     | v1.0 (Layer 08 Infrastructure Runtime) |
| **Kubernetes Version** | 1.24+ (Pod Security Admission GA)      |
| **Target Audience**    | Platform engineers, DevSecOps, SREs    |

**Compliance Statement:** This profile is 100% conformant to EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md and enforces all governance principles at Layer 08, Infrastructure Runtime → Orchestration tier.

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)

**Supersedes:** N/A (new document)
**Superseded By:** None (active)
