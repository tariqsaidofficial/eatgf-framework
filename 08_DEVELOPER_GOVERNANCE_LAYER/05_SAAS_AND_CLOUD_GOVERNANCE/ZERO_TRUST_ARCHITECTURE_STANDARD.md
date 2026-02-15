# Infrastructure Zero Trust Architecture Standard

| Field | Value |
|-------|-------|
| Document Type | Implementation Standard |
| Version | 1.0 |
| Classification | Controlled |
| Effective Date | 2026-02-16 |
| Authority | Chief Information Security Officer |
| EATGF Layer | 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE |
| MCM Reference | EATGF-CLOUD-ZERO-TRUST-01 |

---

## Purpose

Implement Zero Trust architecture for cloud infrastructure: assume breach, verify every access, enforce cryptographic identity, limit lateral movement, and provide complete auditability.

**Mandatory for:** All cloud infrastructure hosting sensitive data or services.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE

- **Upstream dependency:** Layer 04 Information Security Policy; Layer 02 Control Objectives (network security, authentication)
- **Downstream usage:** Enforces Zero Trust throughout networking, compute, storage, and data layers
- **Cross-layer reference:** Maps to NIST CSF PR.AC, NIST SP 800-207 (Zero Trust Architecture)

## Governance Principles

1. **Never Trust, Always Verify** – Every connection verified cryptographically; no implicit trust
2. **Least Privilege Access** – Every principal (user, service, device) receives minimum necessary permissions
3. **Assume Breach** – Architecture designed to contain compromise; lateral movement prevented
4. **Complete Observability** – All traffic logged and analyzable; no blind spots

## Technical Implementation

### Perimeter Elimination

**Traditional vs. Zero Trust:**

| Traditional | Zero Trust |
|-------------|-----------|
| Network perimeter (DMZ) | No perimeter; cryptographic identity |
| VPN access | VPN + device posture + user verification |
| Private DNS | Private DNS + cryptographic validation |
| Security groups (source IP) | mTLS identity + RBAC policies |

**Zero Trust Network Architecture:**

```yaml
# AWS example: Zero Trust ingress
Application Load Balancer:
  - HTTPS only (TLS 1.3)
  - Client cert verification (mutual TLS)
  - Certificate pinning for known clients
  - WAF rules: rate limiting, IP reputation
  
Service Mesh (Istio/Linkerd):
  - mTLS between all services
  - Service identity via Kubernetes SPIFFE/SVID certificates
  - Automatic certificate rotation (24-hour TTL)
  - Network policies: allow-list model (default deny)
  
Database Access:
  - No direct internet-facing endpoints
  - Bastion host + hardware key for access
  - Encryption in transit (TLS 1.3) + at rest (AES-256)
  - Row-level security + audit logging
```

### Identity and Access Management

**Cryptographic Identity:**

```yaml
# Kubernetes: SPIFFE certificate-based identity
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT  # All traffic must be mTLS

---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: api-policy
spec:
  selector:
    matchLabels:
      app: api-server
  rules:
  - from:
    - source:
        principals:
        - cluster.local/ns/default/sa/web-frontend
    to:
    - operation:
        methods: ["GET", "POST"]
        paths: ["/api/v1/*"]
```

**Service-to-Service Identity:**

```javascript
// Node.js microservice with mTLS
const fs = require('fs');
const https = require('https');

const options = {
  key: fs.readFileSync('/var/run/secrets/tls/key.pem'),
  cert: fs.readFileSync('/var/run/secrets/tls/cert.pem'),
  ca: fs.readFileSync('/var/run/secrets/tls/ca.pem'),
  rejectUnauthorized: true  // Verify server certificate
};

const agent = new https.Agent(options);

// Request includes client certificate
https.get('https://api-service:443/data', { agent }, (res) => {
  // Both client and server authenticated
});
```

**User Identity (Zero Trust VPN):**

```yaml
# Tailscale / Wireguard Zero Trust VPN
# - User device authenticates with OIDC provider (Okta/Azure AD)
# - Device posture verified (EDR agent running, disk encrypted, OS patched)
# - User-device certificate generated (short-lived, device-bound)
# - Access policy: user role + device posture + destination
# - All traffic encrypted end-to-end
# - Certificate revoked if device compromised or user deactivated
```

### Network Segmentation

**Micro-segmentation with Network Policies:**

```yaml
# Kubernetes NetworkPolicy: allow-list model
# Default: deny all ingress/egress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress

---
# Allow specific: web → api
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web-to-api
spec:
  podSelector:
    matchLabels:
      tier: api
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: web
    ports:
    - protocol: TCP
      port: 443  # HTTPS only

---
# Allow specific: api → database
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-to-db
spec:
  podSelector:
    matchLabels:
      tier: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: api
    ports:
    - protocol: TCP
      port: 5432
```

### Principle of Least Privilege

**RBAC for Kubernetes:**

```yaml
# Minimal permissions per service
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-service

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: api-service-role
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  resourceNames: ["api-config"]  # Only specific configmap
  verbs: ["get"]
- apiGroups: [""]
  resources: ["secrets"]
  resourceNames: ["api-tls-cert"]  # Only TLS secret
  verbs: ["get"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: api-service-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: api-service-role
subjects:
- kind: ServiceAccount
  name: api-service
```

**Cloud IAM (AWS/GCP example):**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::prod-data/app-123/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["10.0.0.0/8"]
        },
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

### Continuous Verification

**Device Posture Verification:**

```yaml
# Device must pass checks before access granted
device_requirements:
  - os_version: minimum 12.0 (macOS) / 21H2 (Windows) / 22.04 (Ubuntu)
  - disk_encryption: enabled (FileVault / BitLocker / LUKS)
  - antivirus: active (EDR agent running, signatures current)
  - firewall: enabled and managed by organization
  - auto_updates: enabled
  - screen_lock: 5 minute timeout
  - full_disk_access_recovery: disabled (prevents bypass)
```

**Continuous Authentication:**

```javascript
// Re-verify identity every 30 minutes for sensitive operations
async function verifyIdentity(req, res, next) {
  const tokenAge = Date.now() - req.session.issued_at;
  
  if (tokenAge > 30 * 60 * 1000) {  // 30 minutes
    // Re-authenticate
    const verified = await oidc.verify(req.session.id_token);
    if (!verified) {
      return res.status(403).send('Session re-verification failed');
    }
    req.session.last_verified = Date.now();
  }
  
  next();
}
```

### Logging and Monitoring

**Complete Observability:**

```yaml
# All connections logged
logging:
  network_events:
    - source_identity (certificate CN)
    - destination_identity
    - action (allow/deny)
    - timestamp
    - request_id (for tracing)
  
  access_events:
    - principal_identity
    - resource_accessed
    - action
    - result (success/failure)
    - timestamp
  
  data_events:
    - who accessed what data
    - when
    - what operations
    - result

# Real-time anomaly detection
alerts:
  - access_from_new_location (>500 miles from last location in 1 hour)
  - privilege_escalation_attempt (unexpected admin access)
  - data_exfiltration (unusual volume/velocity of data access)
  - certificate_verification_failure
```

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST | COBIT |
|---|---|---|---|
| Zero Trust architecture | A.8.2, A.8.3, A.9.1 | CSF PR.AC, SP 800-207 | BAI10 |
| Network segmentation | A.8.2 | CSF PR.AC | DSS05 |
| Continuous verification | A.8.19, A.12.4 | CSF DE.AE | MEA02 |

## Developer Checklist

- [ ] Remove all public endpoints (except API Gateway / ALB)
- [ ] Implement mTLS between all services
- [ ] Kubernetes SPIFFE certificates configured
- [ ] NetworkPolicy allow-list model enforced
- [ ] Device posture verification configured
- [ ] OIDC provider integration completed
- [ ] Least privilege IAM roles assigned
- [ ] All access audited and logged
- [ ] Real-time monitoring alerts configured
- [ ] Zero Trust architecture diagram documented

## Version History

| Version | Date | Change Type | Description |
|---------|------|-------------|-------------|
| 1.0 | 2026-02-16 | Major | Initial Zero Trust architecture standard |
