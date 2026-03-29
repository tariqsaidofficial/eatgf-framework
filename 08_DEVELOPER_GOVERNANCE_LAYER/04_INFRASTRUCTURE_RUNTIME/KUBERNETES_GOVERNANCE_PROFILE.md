# Kubernetes Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Container Orchestration runtime security. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Kubernetes deployments satisfy DevSecOps (Layer 03), Infrastructure Runtime (Layer 04), and Zero-Trust security requirements.

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME (Primary) + Layer 03 (DevSecOps) + Layer 01 (Secure SDLC)
- **Governance Scope:** Implementation Standard for Container Orchestration Security
- **Control Authority:** Implements controls from MASTER_CONTROL_MATRIX via Secure SDLC, DevSecOps, and Zero-Trust Networking standards

---

## Governance Principles

This profile enforces:

- **Security-by-Design:** Zero-trust networking, pod security standards
- **Control-Centric Architecture:** 8 mandatory controls + cluster audit logging
- **Versioned Governance:** Cluster version N-2 enforcement, deprecation tracking
- **Developer-Operational Alignment:** RBAC least privilege, admission webhooks
- **Audit Traceability:** Kubernetes audit logging with secret access tracking
- **Single Source of Truth:** Declarative infrastructure via GitOps

---

## Control Mapping

| EATGF Control          | ISO 27001:2022 | NIST SSDF | OWASP SAMM | COBIT |
| ---------------------- | -------------- | --------- | ---------- | ----- |
| Service Account RBAC   | A.8.2          | PW.4      | ASVS V1    | APO13 |
| Network Policies       | A.8.9          | PW.8      | ASVS V14   | CM-6  |
| Pod Security Standards | A.8.22         | PW.8      | ASVS V5    | DSS05 |
| Secrets Management     | A.8.12         | PW.4      | ASVS V6    | IA-5  |
| Audit Logging          | A.8.15         | RV.1      | Verify.1   | MEA01 |
| Resource Quotas        | A.8.9          | PW.8      | ASVS V14   | CM-3  |
| Admission Controllers  | A.8.22         | PW.8      | Build.2    | DSS05 |
| RBAC Enforcement       | A.8.2          | PW.4      | ASVS V1    | APO13 |

---

## Purpose

Define governance controls for Kubernetes cluster security, pod isolation, network policies, and RBAC to ensure zero-trust container orchestration in production environments.

**Applies to:**

- Multi-tenant clusters
- Stateless workloads
- Microservices
- Data processing pipelines
- All production-grade K8s deployments

---

## Technical Implementation

### Service Account & RBAC

```yaml
#  COMPLIANT: Minimal service account, no cluster-admin
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: production

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-role
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]
    resourceNames: ["app-secret"] # Read only specific secret
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get"]
    resourceNames: ["app-config"]
  - apiGroups: [""]
    resources: ["services"]
    verbs: ["get", "list"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-rolebinding
  namespace: production
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: app-role
subjects:
  - kind: ServiceAccount
    name: app-sa
    namespace: production
```

### Network Policy (Zero-Trust)

```yaml
#  COMPLIANT: Deny-all default with explicit allows
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-allow-ingress
  namespace: production
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
              name: production
        - podSelector:
            matchLabels:
              app: web
      ports:
        - protocol: TCP
          port: 8000

    - from:
        - namespaceSelector:
            matchLabels:
              name: monitoring
      ports:
        - protocol: TCP
          port: 9090 # Prometheus metrics only
```

### Pod Security & Secrets

```yaml
#  COMPLIANT: Read-only filesystem, drop capabilities
---
apiVersion: v1
kind: Pod
metadata:
  name: api-pod
  namespace: production
spec:
  serviceAccountName: app-sa
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault

  containers:
    - name: api
      image: app:v1.2.3@sha256:abc123...
      imagePullPolicy: Always
      ports:
        - containerPort: 8000
          name: http

      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
          add:
            - NET_BIND_SERVICE

      resources:
        requests:
          memory: "256Mi"
          cpu: "100m"
        limits:
          memory: "512Mi"
          cpu: "500m"

      volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: app-secret
          mountPath: /var/secrets/app
          readOnly: true

      env:
        - name: APP_SECRET
          valueFrom:
            secretKeyRef:
              name: app-secret
              key: db-password

  volumes:
    - name: tmp
      emptyDir: {}
    - name: app-secret
      secret:
        secretName: app-secret
        defaultMode: 0400
```

### Audit Logging Configuration

```yaml
#  COMPLIANT: Capture secret access, RBAC denials
---
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # Log all secret reads
  - level: RequestResponse
    verbs: ["get", "list", "watch"]
    resources:
      - group: ""
        resources: ["secrets"]
    omitStages:
      - RequestReceived

  # Log all RBAC denials
  - level: Metadata
    userGroups: ["system:unauthenticated"]
    omitStages:
      - RequestReceived

  # Log pod exec
  - level: Metadata
    verbs: ["create"]
    resources:
      - group: ""
        resources: ["pods/exec"]

  # Everything else at Metadata level
  - level: Metadata
    omitStages:
      - RequestReceived
```

---

## Developer Checklist

- [ ] Service account created (no `default` SA used)
- [ ] Role/RoleBinding establish least-privilege access
- [ ] No ClusterRole used (using Role + RoleBinding per namespace)
- [ ] Network policies: default deny-all + explicit allow rules
- [ ] Pod SecurityContext: runAsNonRoot=true, readOnlyRootFilesystem=true
- [ ] Capabilities dropped (ALL) and only NET_BIND_SERVICE added
- [ ] Resource requests AND limits defined for all containers
- [ ] Secrets mounted as volumes (read-only, 0400 permissions)
- [ ] Image pulls use imagePullPolicy: Always + digest pinning (@sha256)
- [ ] No hostPath volumes (use emptyDir or projected volumes)
- [ ] Audit logging enabled and monitoring secret access
- [ ] PSA (Pod Security Admission) set to restricted/baseline per namespace
- [ ] Network policies tested with `kubectl exec` + curl verification
- [ ] All pod labels include app=, version=, tier= for policy selectors
- [ ] Admission webhooks validate policy compliance before pod creation

---

## Governance Implications

### Risk if Not Implemented

- **Lateral Movement:** Pod without network policy → unrestricted East-West communication
- **Privilege Escalation:** root container or privileged pod → node OS compromise
- **Secret Breach:** Secrets in environment variables (not mounted) → process inspection attack
- **Audit Blind Spot:** Secret access logging disabled → cannot detect breaches

### Operational Impact

- Cluster-wide network accessibility → DOS between pods
- Pod-to-host escape via privileged container → all node data exposed
- Unquota workloads → node resource starvation, eviction cascade
- Audit log data loss → no forensic evidence for compliance

### Audit Consequences

- **ISO 27001 A.8.2:** Access control not minimal
- **SOC2 CC6.1:** Privilege management failure
- **PCI-DSS 6.5.1:** Weak RBAC enforcement

### Cross-Team Dependencies

- Platform team: Must operate K8s cluster with audit logging enabled
- Security team: Must review and approve network policies per team
- DevOps team: Must enforce admission webhooks in CI/CD pipeline

---

## Official References

- Kubernetes Official: https://kubernetes.io/docs/concepts/security/
- NIST SP 800-218: Secure Software Development Framework (SSDF)
- CIS Kubernetes Benchmark v1.8.0
- NSA/CISA Kubernetes Hardening Guidance (2021)
- OWASP Container Security Top 10

---

## Version Information

- **Version:** 1.0
- **Change Type:** Major (Initial Release)
- **Date:** 2026-02-15
- **Status:** Published
- **Target Audience:** Platform engineers, SREs, cluster admins
- **Kubernetes Version:** 1.24+ (PSA/audit v1 stable)

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)
