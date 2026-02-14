# Zero Trust API Architecture

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 02_API_GOVERNANCE
**Governance Scope:** Architecture Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE

**Governance Scope:** Zero Trust security model for API architecture, authentication flows, and authorization enforcement.

**Control Authority Relationship:** Implements:

- Layer 02: Information Security Controls
- Layer 04: Information Security Policy
- NIST Zero Trust Architecture (SP 800-207)

## Purpose

This standard defines Zero Trust principles for API security architecture. It covers:

- "Never trust, always verify" authentication model
- Fine-grained authorization (RBAC, ABAC)
- Mutual TLS (mTLS) for service-to-service communication
- API gateway architecture
- Least privilege access enforcement
- Continuous verification and monitoring

## Governance Principles

- **Security-by-Design:** Zero Trust embedded in API architecture
- **Control-Centric Architecture:** Every API call authenticated and authorized
- **Developer-Operational Alignment:** Secure-by-default API design
- **Audit Traceability:** All access attempts logged

## Zero Trust Core Principles

### Principle 1: Verify Explicitly

**Requirement:** Authenticate and authorize every API request using all available data points.

**Developer Requirements:**

- Verify identity on every API call (no implicit trust)
- Use strong authentication (OAuth 2.0, OpenID Connect, mTLS)
- Validate authorization using current access policies
- Consider contextual signals: user location, device posture, risk score

**No Implicit Trust:**

- Network location does not grant access (internal vs. external network irrelevant)
- Previous authentication does not grant future access (re-verify each request)

### Principle 2: Use Least Privilege Access

**Requirement:** Grant minimum necessary permissions for each API consumer.

**Developer Requirements:**

- Implement fine-grained authorization (per-resource, per-action)
- Use short-lived access tokens (15 minutes recommended)
- Scope tokens to specific resources and operations
- Deny by default (explicit allow required)

### Principle 3: Assume Breach

**Requirement:** Design APIs assuming attackers may already be inside the network.

**Developer Requirements:**

- Encrypt all data in transit (TLS 1.3)
- Encrypt sensitive data at rest
- Segment access (lateral movement prevention)
- Monitor for anomalous behavior
- Implement rate limiting and DDoS protection

## Zero Trust API Architecture

### API Gateway

**Requirement:** Route all API traffic through centralized API gateway.

**API Gateway Responsibilities:**

- Authentication and authorization enforcement
- Rate limiting and throttling
- Request/response logging
- TLS termination
- DDoS protection
- API versioning and routing

**Recommended Solutions:**

- Kong Gateway
- Apigee
- AWS API Gateway
- Azure API Management
- Traefik

**Developer Requirements:**

- Do not bypass API gateway (no direct service access)
- Configure gateway with security policies
- Use gateway for centralized logging and monitoring

### Service Mesh (for Microservices)

**Requirement:** Use service mesh for service-to-service communication.

**Service Mesh Responsibilities:**

- Mutual TLS (mTLS) for service-to-service encryption
- Service identity and authentication
- Traffic management and load balancing
- Observability (distributed tracing)

**Recommended Solutions:**

- Istio
- Linkerd
- Consul Connect

**Developer Requirements:**

- Enable mTLS for all service-to-service communication
- Use service identities (e.g., SPIFFE/SPIRE)
- Enforce authorization policies at service mesh layer

## Authentication

### OAuth 2.0 and OpenID Connect (REQUIRED)

**Requirement:** Use OAuth 2.0 for authorization and OIDC for authentication.

**OAuth 2.0 Flows:**

| Flow | Use Case | Security Level |
|---|---|---|
| Authorization Code + PKCE | Web and mobile apps | High |
| Client Credentials | Service-to-service | High |
| Device Code | IoT and limited-input devices | Medium |

**Prohibited Flows:**

- Implicit Flow (deprecated, insecure)
- Resource Owner Password Credentials (anti-pattern)

**Developer Requirements:**

- Use Authorization Code flow with PKCE for user-facing applications
- Use Client Credentials flow for service-to-service communication
- Validate tokens on every API request (do not trust client-provided claims)
- Use short-lived access tokens (15 minutes)
- Use refresh tokens for long-lived sessions (with rotation)

### Mutual TLS (mTLS) for Service-to-Service

**Requirement:** Use mTLS for authentication between internal services.

**Developer Requirements:**

- Each service has unique X.509 certificate
- Services verify peer certificates on connection
- Use short-lived certificates (e.g., 24 hours) with automated rotation
- Use service mesh or sidecar proxy to manage mTLS

**Benefits:**

- Strong service identity
- Encrypted communication
- Prevents service impersonation

### API Key (LIMITED USE)

**Requirement:** Use API keys only for public, read-only APIs.

**Developer Requirements:**

- API keys for identification, not authentication
- Combine API keys with other authentication (e.g., OAuth)
- Rotate API keys regularly
- Never embed API keys in client-side code
- Monitor API key usage for anomalies

**Prohibited Use:**

- API keys for write operations
- API keys for accessing sensitive data
- Long-lived API keys without rotation

## Authorization

### Role-Based Access Control (RBAC)

**Requirement:** Implement RBAC for coarse-grained access control.

**Developer Requirements:**

- Define roles based on job functions (e.g., Admin, Editor, Viewer)
- Assign permissions to roles, not individual users
- Users inherit permissions from assigned roles
- Enforce role checks on every API endpoint

**Example RBAC:**

| Role | Permissions |
|---|---|
| Admin | read:*, write:*, delete:* |
| Editor | read:*, write:* |
| Viewer | read:* |

### Attribute-Based Access Control (ABAC)

**Requirement:** Implement ABAC for fine-grained, context-aware access control.

**Developer Requirements:**

- Define policies using attributes (user, resource, action, environment)
- Evaluate policies at runtime for each request
- Use policy decision point (PDP) and policy enforcement point (PEP) pattern
- Use standard policy language (e.g., Open Policy Agent / Rego, XACML)

**Example ABAC Policy:**

```rego
# Allow read access if user is owner or resource is public
allow {
    input.action == "read"
    input.resource.owner == input.user.id
}

allow {
    input.action == "read"
    input.resource.visibility == "public"
}
```

**Benefits:**

- Fine-grained access control (per-resource, per-action)
- Context-aware decisions (time, location, device)
- Dynamic policies without code changes

### Policy Enforcement

**Requirement:** Enforce authorization at API gateway and service level.

**Defense in Depth:**

1. **API Gateway:** Coarse-grained authorization (e.g., role-based)
2. **Service Layer:** Fine-grained authorization (e.g., resource ownership)

**Developer Requirements:**

- Verify authorization on every API endpoint
- Deny by default (explicit allow required)
- Use centralized policy decision point (e.g., OPA)
- Log all authorization decisions

## Token Security

### Access Token Requirements

**Requirement:** Use JWT (JSON Web Tokens) for access tokens.

**Developer Requirements:**

- Sign tokens using RS256 or ES256 (asymmetric algorithms)
- Do not use HS256 for distributed systems (shared secret vulnerability)
- Include standard claims: `iss`, `sub`, `aud`, `exp`, `iat`
- Include custom claims for authorization: `roles`, `scopes`, `permissions`
- Set short expiration (15 minutes recommended)

**Token Validation:**

- Verify signature using issuer's public key
- Verify `iss` (issuer) matches expected authority
- Verify `aud` (audience) matches API
- Verify `exp` (expiration) is in the future
- Verify token has required scopes/permissions

### Refresh Token Security

**Requirement:** Use refresh tokens with rotation for long-lived sessions.

**Developer Requirements:**

- Store refresh tokens securely (HttpOnly, Secure cookies or secure storage)
- Use refresh token rotation (issue new refresh token on each use)
- Invalidate old refresh token after new one issued
- Implement refresh token expiration (e.g., 30 days)
- Revoke refresh tokens on logout or suspicious activity

### Token Storage

**Requirement:** Store tokens securely on client side.

**Web Applications:**

- Store in HttpOnly, Secure, SameSite cookies (preferred)
- Or use browser memory (sessionStorage / in-memory variable)
- Do not store in localStorage (vulnerable to XSS)

**Mobile Applications:**

- Use platform-specific secure storage (Keychain on iOS, Keystore on Android)

**Single Page Applications (SPA):**

- Use Authorization Code flow with PKCE
- Use BFF (Backend-for-Frontend) pattern to handle tokens server-side

## Network Security

### TLS Requirements

**Requirement:** Enforce TLS 1.3 or TLS 1.2 for all API communication.

**Developer Requirements:**

- Disable TLS 1.0 and TLS 1.1 (deprecated)
- Use strong cipher suites (AEAD ciphers: AES-GCM, ChaCha20-Poly1305)
- Implement certificate pinning for mobile apps
- Use valid certificates from trusted CA (no self-signed in production)

### DDoS Protection

**Requirement:** Implement DDoS protection at edge and API gateway.

**Developer Requirements:**

- Use CDN with DDoS protection (e.g., Cloudflare, Akamai)
- Implement rate limiting at API gateway
- Use CAPTCHA or challenge for suspicious traffic
- Monitor for traffic anomalies and auto-scale infrastructure

## Monitoring and Logging

**Requirement:** Log all API access attempts and authorization decisions.

**Developer Requirements:**

- Log: timestamp, user ID, IP address, endpoint, HTTP method, status code, response time
- Log authorization decisions: allowed or denied, policy evaluated
- Do not log sensitive data (tokens, passwords, PII)
- Implement real-time monitoring and alerting
- Use SIEM for security event correlation

**Anomaly Detection:**

- Sudden spike in failed authentication attempts
- Access from unusual geographic locations
- High volume of requests from single IP
- Access to sensitive endpoints outside business hours

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Authentication | A.5.17, A.5.18 | PS.1 | API2:2023 | DSS05 |
| Authorization | A.5.15 | PO.1 | API5:2023 | DSS05 |
| Encryption | A.8.24 | PS.2 | API8:2023 | DSS05 |
| Monitoring | A.8.15, A.8.16 | RV.1 | API10:2023 | DSS05 |

## Developer Checklist

For Zero Trust API implementation:

- [ ] All API traffic routed through API gateway
- [ ] OAuth 2.0 / OIDC implemented for user authentication
- [ ] mTLS implemented for service-to-service communication
- [ ] Fine-grained authorization (RBAC or ABAC) enforced
- [ ] Short-lived access tokens (15 minutes)
- [ ] TLS 1.3 or TLS 1.2 enforced
- [ ] Rate limiting and DDoS protection configured
- [ ] Comprehensive logging and monitoring implemented
- [ ] Security policies centralized (e.g., OPA)

## Governance Implications

**Risk if not implemented:**

- Unauthorized access to APIs and data
- Lateral movement in case of breach
- Insufficient audit trail for compliance

**Operational impact:**

- Centralized security controls reduce configuration drift
- Automated policy enforcement reduces human error
- Improved incident detection and response

**Audit consequences:**

- Zero Trust demonstrates defense-in-depth
- Comprehensive logging supports compliance audits
- Fine-grained authorization demonstrates least privilege

**Cross-team dependencies:**

- Security team defines authentication and authorization policies
- DevOps team configures API gateway and service mesh
- Monitoring team sets up alerting and SIEM integration

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. API Governance Framework (Layer 05)
4. Zero Trust API Architecture

## References

- NIST SP 800-207: Zero Trust Architecture (<https://csrc.nist.gov/publications/detail/sp/800-207/final>)
- OAuth 2.0 (RFC 6749)
- OpenID Connect Core 1.0
- OWASP API Security Top 10 (<https://owasp.org/www-project-api-security/>)
- Open Policy Agent (<https://www.openpolicyagent.org/>)
- SPIFFE/SPIRE (<https://spiffe.io/>)

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial Zero Trust API architecture standard |
