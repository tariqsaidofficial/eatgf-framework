# API_GOVERNANCE_FRAMEWORK

| Field | Value |
|-------|-------|
| Document Type | Domain Framework |
| Version | 2.0 |
| Classification | Controlled |
| Effective Date | 2026-02-14 |
| Authority | API Governance Lead |
| EATGF Layer | 05_DOMAIN_FRAMEWORKS |
| MCM Reference | EATGF-API-SEC-01, EATGF-API-LC-01 |
| Standards | OWASP API Security Top 10:2023, OpenAPI 3.0 Specification |

---

## Purpose

This framework establishes governance standards for all APIs created, acquired, or operated by the organization. It covers API design through documentation, security and threat prevention, lifecycle management, performance monitoring, and reliability. All organizational APIs must comply with this framework; API deployments without governance compliance are subject to immediate takedown and deployment privilege suspension.

## Architectural Position

This framework operates within **05_DOMAIN_FRAMEWORKS** as the specialized API domain extension.

- **Upstream dependency:** Governance Charter (04_POLICY_LAYER) establishes authority structure; Information Security Policy provides encryption and access control foundation
- **Downstream usage:** Operationalized through API security procedures, lifecycle procedures, API catalog management, and monitoring/operations procedures
- **Cross-layer reference:** Maps to EATGF API domain controls (API-SEC-01 security, API-LC-01 lifecycle) in Layer 02; implements Layer 03 governance models through API governance maturity assessment; aligned with OWASP Top 10 security controls in Layer 02

## Governance Principles

1. **Contract-First Design** – APIs are contracts between services; design documented in OpenAPI/Swagger specifications before implementation begins
2. **Security by Default** – Authentication, authorization, and encryption required for all APIs without exception; security reviews mandatory before production
3. **Versioning and Stability** – Backward compatibility maintained; breaking changes require major version increment with 6-month migration period
4. **Observability and Monitoring** – All APIs monitored for performance, security posture, and business metrics; dashboards provide real-time visibility
5. **Developer Experience** – Clear documentation, SDKs, sandbox environments, and support channels provided for all APIs

## Technical Implementation

### API Lifecycle: Seven-Stage Framework

**Stage 1: Planning & Design**

**Design Gate Checklist:**

- [ ] API purpose and intended use cases documented
- [ ] API consumers identified and documented
- [ ] OpenAPI 3.0 specification started (contract-first)
- [ ] Resource modeling completed
- [ ] Error handling and error code strategy defined
- [ ] Security model identified (OAuth 2.0, mTLS, API Key)
- [ ] Rate limiting strategy defined with tier levels
- [ ] Versioning strategy chosen per semantic versioning

**OpenAPI Specification (Mandatory Minimum):**

```yaml
openapi: 3.0.0
info:
  title: API Name
  version: 1.0.0
  description: Clear description of API purpose
servers:
  - url: https://api.enterprise.com/v1
paths:
  /resources:
    get:
      summary: Get resources
      operationId: getResources
      security:
        - bearerAuth: []
      responses:
        200:
          description: Success
        401:
          description: Unauthorized
        429:
          description: Rate limit exceeded
```

**Security Model Selection:**

| Use Case | API Type | Authentication | Authorization |
|---|---|---|---|
| Internal service-to-service | Internal | mTLS | RBAC via certificate |
| Public third-party | Public | OAuth 2.0 | Scopes + RBAC |
| Partner integration | Partner | API Key + mTLS | Custom roles |
| Mobile application | Public | OAuth 2.0 + PKCE | Device-scoped tokens |

**Owner:** API Product Manager
**Review Timeline:** 1 week
**Approval Gate:** Architecture Review Board sign-off required

---

**Stage 2: Development & Documentation**

**Development Requirements:**

- [ ] OpenAPI specification follows enterprise naming conventions
- [ ] Code generated from OpenAPI (contract-first approach)
- [ ] Unit tests cover happy path and error cases
- [ ] Security tests validate OWASP Top 10 controls
- [ ] Performance tests validate latency targets (<200ms p95)
- [ ] API documentation auto-generated from OpenAPI
- [ ] OpenAPI spec matches implementation (no drift)

**API Documentation Must Include:**

- Business use cases and workflow scenarios
- Authentication flow diagrams with sequence diagrams
- Rate limit policies and behavior on limit exceeding
- Error responses with real examples
- Versioning and deprecation policy enforcement
- SLA and performance expectations
- Code samples in multiple languages
- SDKs availability
- Break-glass procedures (emergency access)

**API Catalog Registration Entry:**

- [ ] API registered in centralized API catalog within 1 week
- [ ] Owner team assigned and primary contact designated
- [ ] Classification assigned (Internal/Partner/Public)
- [ ] Maturity level assigned (Alpha/Beta/Stable/Deprecated)
- [ ] OpenAPI spec linked and version tracked

**Owner:** API Development Team
**Review Timeline:** 1-2 weeks (code review + security review)

---

**Stage 3: Security & Compliance Review**

**OWASP API Security Top 10:2023 Controls:**

| OWASP Category | Requirement | Validation Method |
|---|---|---|
| **API1: Broken Object Level Authorization** | Resource access validated at object ID | Code review + penetration test |
| **API2: Broken Authentication** | OAuth 2.0 or mTLS enforced | Security review + automated scan |
| **API3: Broken Object Property Level Authorization** | Field-level access control enforced | Penetration testing |
| **API4: Unrestricted Resource Consumption** | Rate limiting and quotas configured | Load testing validation |
| **API5: Broken Function Level Authorization** | Endpoint-level access control checks | Code review and testing |
| **API6: Unrestricted Access to Sensitive Flows** | Business logic threats mitigated | Threat modeling assessment |
| **API7: Server-Side Request Forgery (SSRF)** | Input validation and allowlists | Security testing |
| **API8: Security Misconfiguration** | Hardened defaults applied enterprise-wide | Configuration audit |
| **API9: Improper Inventory Management** | All APIs registered in catalog | API audit process |
| **API10: Unsafe Consumption of APIs** | Third-party API security validated | Vendor assessment |

**Security Review Outputs:**

- [ ] Threat model documented (STRIDE methodology)
- [ ] Security assessment report completed
- [ ] Remediation plan for any findings (with timeline)
- [ ] CISO office sign-off obtained before Stage 4

**Owner:** Application Security Team
**Timeline:** 2 weeks (expedited: 1 week for low-risk internal APIs)

---

**Stage 4: Testing & Validation**

**Comprehensive Testing Requirements:**

| Test Type | Scope | Pass Criteria | Owner |
|---|---|---|---|
| **Functional** | All user stories, happy path, error cases | 100% story coverage | QA Team |
| **Performance** | Load test (1000 RPS minimum) | <200ms p95 latency | Performance Team |
| **Security** | OWASP Top 10 controls | No critical findings | Security Team |
| **Integration** | Upstream and downstream systems | All integrations tested | Integration Team |
| **Regression** | All existing API versions | Backward compatibility confirmed | Release Team |

**Test Environment Setup:**

- [ ] Staging environment with production-like data volume
- [ ] Production-grade network topology mirrored
- [ ] Test data set prepared (no PII, compliance verified)
- [ ] Monitoring and logging configured
- [ ] Performance baseline established from requirements

**Owner:** QA and Testing Team
**Timeline:** 1-2 weeks

---

**Stage 5: Release & Operations**

**Pre-Release Checklist:**

- [ ] All testing phases completed with pass criteria met
- [ ] Security review approved by CISO office
- [ ] Documentation complete and published to developer portal
- [ ] Monitoring dashboards created and tested
- [ ] Operational runbooks created for incident response
- [ ] Customer communication plan developed and ready
- [ ] Rollback/fallback plans prepared and tested
- [ ] Executive release signoff obtained

**Release Deployment Phases:**

1. **Phase 1: Canary (1-5% traffic)** – 3-7 days of monitoring; watch for errors, latency spikes
2. **Phase 2: Early Adopters (10-25% traffic)** – 1-2 weeks; gather feedback from launch partners
3. **Phase 3: Standard (50% traffic)** – Monitor for stability
4. **Phase 4: General Availability (100% traffic)** – Full production deployment

**Release Authority:** API Platform Team (with on-call engineering readiness)

---

**Stage 6: Operations & Optimization**

**Continuous Operational Monitoring:**

| Metric | Monitoring Frequency | Alert Threshold | Owner |
|---|---|---|---|
| Error Rate (4xx/5xx) | Real-time | >1% of requests | On-call engineer |
| Latency (p95) | Real-time | >500ms response time | On-call engineer |
| Rate Limit Violations | Hourly | >5% of requests rejected | Product team |
| Unused Endpoints | Monthly | Not called in 30 days | Product team |
| API Schema Drift | Monthly | Implementation ≠ OpenAPI spec | Architecture team |
| Security Incidents | Real-time | Any unauthorized access | Security team |

**Monthly Operations Review:**

- [ ] Performance vs. SLA comparison (uptime %, latency)
- [ ] Error analysis identifying top 10 error patterns
- [ ] Security incidents or issues reported
- [ ] Usage trends and customer feedback
- [ ] Cost analysis and optimization opportunities

**Quarterly Comprehensive Assessment:**

- [ ] Comprehensive performance audit vs. targets
- [ ] Security reassessment including vulnerability scan
- [ ] Deprecation opportunity identification
- [ ] Optimization recommendations (caching, batching, etc.)
- [ ] Stakeholder review and satisfaction

**Owner:** API Operations Team

---

**Stage 7: Deprecation & Sunset**

**Deprecation Lifecycle Timeline:**

- **Month 1:** Announce sunset date (6-month minimum notice)
- **Month 2-5:** Migration support period; migration guide published
- **Month 6:** Redirect all traffic to successor version
- **Month 9:** Final version sunset; decommissioning

**Deprecation Communication:**

- [ ] Email notification sent to all API consumers with migration path
- [ ] Migration guide published in developer documentation
- [ ] Support team briefed on migration assistance
- [ ] Dashboard shows pending deprecations and timelines

**Owner:** API Product Manager

### API Authentication and Authorization

**Authentication Mechanisms:**

**Internal Service-to-Service APIs (mTLS):**

- Mutual TLS with certificate validation
- Client certificate provisioning and lifecycle management
- Certificate rotation annually minimum
- Certificate revocation procedures documented
- Certificate expiration monitoring automated

**Public APIs (OAuth 2.0 Authorization Code Flow):**

- User authenticates via browser
- OAuth provider requests authorization; user grants
- Authorization code issued (short-lived, 10 minutes)
- Code exchanged for access token (server-to-server)
- API called with Bearer token in Authorization header

**Authorization Token Requirements:**

- Token expiration: 1 hour maximum
- Refresh tokens: 30-day lifetime
- Scope-based permissions enforced at API gateway
- No hardcoded credentials or tokens

**Partner APIs (API Key + mTLS + IP Allowlist):**

- Asymmetric security model combining multiple controls
- API keys revocable on-demand with immediate effect
- IP whitelisting enforced for known partner networks
- mTLS as secondary authentication
- Rate limiting enforced per key
- Monthly access review with partner

### Authorization Models

**Role-Based Access Control (RBAC):**

```
User → Assigned Role → Role Has Permissions → Can Perform Action
```

**Example RBAC Scopes:**

- `api:read` – Read-only access to all endpoints
- `api:write` – Create and update access
- `api:admin` – Full access including deletion and configuration
- `api:support` – Support team limited access (read + special endpoints)

**Enforcement:** API gateway validates token scopes before routing to backend service; scope mismatch returns 403 Forbidden.

**Attribute-Based Access Control (ABAC):**
For complex authorization (e.g., "allow access if user's organization matches resource's organization"):

```
User Attributes: org_id, role, team, department
Resource Attributes: org_id, visibility, owner, classification
Authorization Decision: user.org_id == resource.org_id AND user.role in ['admin', 'owner']?
```

### Rate Limiting Strategy

**Standard Tier (Public API):**

- 100 requests per minute per API key
- Burst allowance: 20 requests (temporary spike tolerance)
- Over-limit response: `429 Too Many Requests`
- Retry-After header indicates wait time

**Premium Tier (Paid Partners):**

- 1,000 requests per minute
- Burst allowance: 100 requests

**Internal Tier (Service-to-Service):**

- Rate limiting disabled (mTLS only)
- Network-level DDoS protection applied at infrastructure layer

**Implementation:**

- Token bucket algorithm (distributed across regions)
- Redis-backed counters for consistency
- Response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

### API Registry and Inventory

**Mandatory API Registration:**
All APIs must be registered within 1 week of production deployment.

**API Catalog Fields:**

```
API ID: [UUID]
Name: [Human-readable name]
Owner: [Team/Department]
Version: [Semantic version, e.g., 1.0.0]
Maturity: [Alpha / Beta / Stable / Deprecated]
Classification: [Internal / Partner / Public]
Endpoint: https://api.enterprise.com/[path]
OpenAPI Spec: [Link to latest specification]
Documentation: [Link to developer documentation]
Support: [Email and/or Slack channel]
SLA: [Expected availability percentage]
Last Audit: [Date of most recent security audit]
Next Audit: [Scheduled audit date]
Status: [Active / Sunset Pending / Deprecated]
Contact: [Primary and secondary contacts]
```

### API Versioning Strategy

**Semantic Versioning: MAJOR.MINOR.PATCH**

| Version Type | When to Increment | Example Transition |
|---|---|---|
| MAJOR | Breaking changes | 1.0.0 → 2.0.0 |
| MINOR | Backward-compatible new features | 1.0.0 → 1.1.0 |
| PATCH | Bug fixes | 1.0.0 → 1.0.1 |

**URL Versioning Schema:**

```
/api/v1/users     // Version 1 (stable)
/api/v2/users     // Version 2 (major breaking change)
/api/v2.1/users   // Not allowed; use v2 + query params for variations
```

**Backward Compatibility Requirements:**

- Support last 2 major versions in production simultaneously
- Deprecate oldest version with 6-month notice
- Timeline: v1 active → v2 active → v3 introduced → v1 sunset

### API Governance Maturity Model

| Maturity Level | Design | Testing | Security | Monitoring |
|---|---|---|---|---|
| **1 - Prototype** | Informal documentation | Manual testing | Ad-hoc review | Basic logging |
| **2 - Early** | OpenAPI partially defined | Scripted tests | Security scan | Log aggregation |
| **3 - Growing** | Full OpenAPI spec | Comprehensive test suite | Security gates in CI/CD | Dashboards and KPIs |
| **4 - Stable** | Best practices documented | 100% test coverage | Automated security scanning | Full observability and alerting |
| **5 - Optimized** | API platform/standards | Continuous testing | AI-based threat detection | Predictive analytics |

**Current Organizational Target:** Level 3-4 by Q3 2026

### Common API Failure Modes and Mitigations

**Failure Mode 1: Unauthorized Access (Data Breach Risk)**

- **Symptom:** Any user can call API and access resources
- **Root Cause:** Missing or insufficient authorization checks
- **Mitigation:**

```
if (!request.user.scopes.contains("api:write")) {
  return 401 Unauthorized;
}
```

**Failure Mode 2: Slow API (Performance Degradation)**

- **Symptom:** API latency exceeds 500ms p95
- **Root Cause:** N+1 query problem; large response payload; missing caching
- **Mitigation:**
  - Batch database queries
  - Implement pagination (default 20 items per page)
  - Add Redis caching for frequently accessed data

**Failure Mode 3: Data Leakage (Privacy Risk)**

- **Symptom:** API response includes unintended fields
- **Root Cause:** No field-level authorization
- **Mitigation:**

```
response = {
  id, name, email,        // Public fields
  // salary, ssn omitted   // Private fields
}
```

## Control Mapping

### OWASP API Security Alignment

Framework aligns with OWASP API Security Top 10:2023:

- **API1-API3** – Authentication and authorization controls
- **API4-API5** – Resource consumption and function authorization
- **API6-API7** – Business logic and SSRF protection
- **API8-API10** – Configuration, inventory, and consumption security

### OpenAPI 3.0 Specification

Framework uses OpenAPI 3.0 standard for API contract definition:

- Schema validation and documentation
- Security scheme definitions
- Rate limit constraints documentation
- Standard error response formats

### ISO 27001:2022 Alignment

Framework implements ISO 27001 controls:

- **A.6.2** – API access management and RBAC
- **A.6.3** – API password management policies
- **A.9.4** – API encryption in transit (TLS)
- **A.9.5** – API confidentiality and integrity controls

## Developer Checklist

Before deploying API:

- [ ] Business use case and value proposition documented
- [ ] API consumers identified
- [ ] OpenAPI 3.0 specification written and reviewed
- [ ] Security model selected (OAuth 2.0, mTLS, API Key)
- [ ] Resource model and data models defined
- [ ] Error handling strategy documented with error codes
- [ ] Rate limiting policy defined with tier levels
- [ ] Versioning strategy chosen per semantic versioning
- [ ] Development completed with unit tests
- [ ] Security testing completed; OWASP Top 10 verified
- [ ] Performance testing completed; latency targets met (<200ms p95)
- [ ] Penetration testing by security team completed
- [ ] API documentation complete and published
- [ ] Monitoring dashboards and alerts configured
- [ ] Operational runbooks created for incidents
- [ ] API registered in catalog with all metadata
- [ ] Customer communication plan developed
- [ ] Rollback procedures tested and documented
- [ ] Executive release signoff obtained before Stage 5

## Governance Implications

### API Governance Authority

- **API Governance Lead:** API governance policy ownership; API system exception authority; strategic API initiatives
- **Architecture Review Board:** Quarterly review of all API deployments; design standard approval authority
- **Security Team:** Security approval authority; incident response for security breaches
- **API Platform Team:** Operational authority; release scheduling; deprecation authority

### Non-Compliance and Enforcement

- APIs deployed without governance approval subject to immediate takedown
- Redeployment requires compliance with all governance gates
- Security violations escalate per incident response procedures
- Repeated violations result in deployment privilege suspension for development team

### API Security Governance

- Security vulnerabilities in APIs escalate to CISO office immediately
- Rate limiting violations investigated for potential DDoS attacks
- Unauthorized access attempts trigger security incident procedures
- Regular security audits (minimum annual) for all production APIs

### API Lifecycle Governance

- All APIs follow standardized 7-stage lifecycle
- Stage gates require formal approvals before advancement
- Deprecation decisions require API Governance Lead approval
- Sunset dates communicated 6 months in advance minimum

## Official References

- **OWASP API Security Top 10** – API security controls (OWASP, 2023)
- **OpenAPI 3.0 Specification** – API contract documentation standard (OpenAPI Initiative, 2021)
- **RFC 6749** – The OAuth 2.0 Authorization Framework (IETF, 2012)
- **RFC 8446** – The Transport Layer Security (TLS) Protocol Version 1.3 (IETF, 2018)
- **ISO/IEC 27001:2022** – Information Security Management Systems (ISO, 2022)

**Design Gate Checklist:**

- [ ] API purpose & use cases documented
- [ ] API consumers identified
- [ ] OpenAPI 3.0 specification started
- [ ] Resource modeling complete
- [ ] Error handling strategy defined
- [ ] Security model identified (OAuth 2.0, etc.)
- [ ] Rate limiting strategy defined
- [ ] Versioning strategy chosen

**OpenAPI Specification (Minimum):**

```yaml
openapi: 3.0.0
info:
  title: Example API
  version: 1.0.0
  description: Clear description
servers:
  - url: https://api.enterprise.com/v1
paths:
  /resources:
    get:
      summary: List resources
      security:
        - bearerAuth: []
      responses:
        200:
          description: Success
        401:
          description: Unauthorized
```

**Security Model Selection:**

| Use Case | Authentication | Authorization |
|----------|----------------|---------------|
| Internal service-to-service | mTLS | RBAC |
| Public API | OAuth 2.0 | Scopes + RBAC |
| Partner API | API Key + mTLS | Custom roles |
| Mobile App | OAuth 2.0 + PKCE | Device-scoped tokens |

**Owner:** API Product Manager
**Review Timeline:** 1 week
**Approval Gate:** Architecture Review Board

---

### Stage 2: Development & Documentation

**Development Standards:**

- [ ] OpenAPI spec follows enterprise conventions
- [ ] Code generated from OpenAPI (contract-first)
- [ ] Unit tests cover happy path + error cases
- [ ] Security tests for OWASP Top 10
- [ ] Performance tests for load targets
- [ ] API documentation generated (auto-generated from OpenAPI)

**API Documentation Must Include:**

- [ ] Use cases and workflows
- [ ] Authentication flow diagrams
- [ ] Rate limit policies
- [ ] Error responses with examples
- [ ] Versioning and deprecation policy
- [ ] SLA/performance expectations
- [ ] Samples and SDKs
- [ ] Break glass procedures (emergency access)

**API Catalog Entry:**

- [ ] API registered in central catalog
- [ ] Owner and team assigned
- [ ] Classification (Internal/Partner/Public)
- [ ] Maturity level assigned

**Owner:** API Development Team
**Review Timeline:** Code review + security review (1-2 weeks)

---

### Stage 3: Security & Compliance Review

**Security Checklist (OWASP API):**

| OWASP Category | Requirement | Validation |
|---------------|------------|-----------|
| API1: Broken Object Level Authorization | Path/ID validation | Code review + test |
| API2: Broken Authentication | OAuth 2.0 + MFA | Security review + scan |
| API3: Broken Object Property Level Authorization | Field-level RBAC | Penetration test |
| API4: Unrestricted Resource Consumption | Rate limiting + quotas | Load test |
| API5: Broken Function Level Authorization | Endpoint-level checks | Code review |
| API6: Unrestricted Access to Sensitive Flows | Business logic protection | Threat modeling |
| API7: Server-Side Request Forgery | Input validation + allowlists | Security test |
| API8: Security Misconfiguration | Hardened defaults | Config review |
| API9: Improper Inventory Management | Catalog accuracy | API audit |
| API10: Unsafe Consumption of APIs | Third-party validation | Review + testing |

**Security Review Outputs:**

- [ ] Threat model documented
- [ ] Security assessment report
- [ ] Remediation plan (if issues found)
- [ ] Sign-off from CISO office

**Owner:** Security Team
**Timeline:** 2 weeks (expedited: 1 week for low-risk)

---

### Stage 4: Testing & Validation

**Testing Requirements:**

| Test Type | Scope | Pass Criteria |
|-----------|-------|---------------|
| Functional | Happy path + error cases | 100% user stories covered |
| Performance | Load test (1000 RPS) | <200ms p95 latency |
| Security | OWASP Top 10 | No critical findings |
| Integration | Upstream/downstream systems | All integrations tested |
| Regression | Existing API versions | Backward compat confirmed |

**Test Environment:**

- [ ] Staging environment with production-like data
- [ ] Test data set prepared (no PII)
- [ ] Monitoring & logging configured
- [ ] Performance baseline established

**Owner:** QA Team
**Timeline:** 1-2 weeks

---

### Stage 5: Release & Operations

**Pre-Release Checklist:**

- [ ] All tests passed
- [ ] Security review approved
- [ ] Documentation complete & published
- [ ] Monitoring dashboards created
- [ ] Runbooks created (incident response)
- [ ] Customer communication plan ready
- [ ] Rollback plan prepared

**Release Phases:**

1. **Canary (1-5% traffic)** - 3-7 days
2. **Early adopters (25% traffic)** - 1-2 weeks
3. **General availability (100%)** - Rolling out

**Release Owner:** API Platform Team

---

### Stage 6: Operations & Optimization

**Operational Monitoring:**

| Metric | Cadence | Alert Threshold | Owner |
|--------|---------|-----------------|-------|
| Error rate (4xx/5xx) | Real-time | >1% errors | On-call engineer |
| Latency (p95) | Real-time | >500ms | On-call engineer |
| Rate limit violations | Hourly | >5% over limit | Product |
| Unused endpoints | Monthly | Not called in 30d | Product |
| API schema drift | Monthly | Spec != implementation | Architecture |

**Monthly Review:**

- [ ] Performance vs. SLA
- [ ] Error analysis (top 10 errors)
- [ ] Security incidents/breaches
- [ ] Usage trends
- [ ] Customer feedback

**Quarterly Assessment:**

- [ ] Comprehensive performance audit
- [ ] Security reassessment
- [ ] Deprecation opportunities
- [ ] Optimization recommendations

**Owner:** API Operations Team

---

### Stage 7: Deprecation & Sunset

**Deprecation Timeline:**

- **Month 1:** Announce sunset (6-month notice minimum)
- **Month 2-5:** Migration support period
- **Month 6:** Redirect to new version
- **Month 9:** Sunset final version

**Deprecation Communication:**

- [ ] Email sent to all API consumers
- [ ] Migration guide published
- [ ] Support team briefed
- [ ] Dashboard shows pending sunsets

**Owner:** API Product Manager

---

## 4. API SECURITY FRAMEWORK

### Authentication Mechanisms

#### 4.1 Service-to-Service (Internal APIs)

**Mechanism:** mTLS (Mutual TLS)

**Implementation:**

```
Client (with cert) → TLS handshake → Server (with cert)
Both verify each other's certificates
```

**Requirements:**

- [ ] Client certificate provisioning
- [ ] Certificate rotation (annually)
- [ ] Certificate revocation process
- [ ] Monitoring of cert expirations

---

#### 4.2 Public APIs (Third-party Access)

**Mechanism:** OAuth 2.0 Authorization Code Flow

**Flow:**

1. User logs in via browser
2. OAuth provider requests authorization
3. Authorization code granted (short-lived)
4. Code exchanged for access token
5. API called with access token

**Requirements:**

- [ ] Client secret managed securely
- [ ] PKCE for mobile apps
- [ ] Token expiration: 1 hour
- [ ] Refresh tokens: 30 days
- [ ] Scope-based permissions

---

#### 4.3 Partner APIs

**Mechanism:** API Key + IP Whitelisting + mTLS

**Requirement:**

- Asymmetric security model
- API key revocable on-demand
- IP whitelisting enforced
- Rate limiting enforced
- Monthly review of access

---

### Authorization Models

#### 4.4 Role-Based Access Control (RBAC)

**Implementation:**

```
User → Has Role → Role Has Permissions → Can Do Action
```

**Example Roles:**

- `api:read` - Read-only access
- `api:write` - Create/update access
- `api:admin` - Full access including deletion
- `api:support` - Support team access

**Enforcement Point:** API Gateway checks token scopes before routing to service.

---

#### 4.5 Attribute-Based Access Control (ABAC)

**For complex scenarios** (e.g., "allow if user is in same org as resource"):

```
User Attributes: org_id, role, team
Resource Attributes: org_id, visibility, owner
Decision: User org_id == Resource org_id?
```

---

### Rate Limiting Strategy

**Tier 1: Standard (Public API):**

- 100 requests per minute per API key
- Burst allowance: 20 requests
- Response: `429 Too Many Requests` with retry-after

**Tier 2: Premium (Paid Partners):**

- 1,000 requests per minute
- Burst allowance: 100 requests

**Tier 3: Internal (Service-to-Service):**

- Rate limiting disabled (mTLS only)
- Network-level DDoS protection applied

**Implementation:**

- Token bucket algorithm
- Redis-backed (distributed)
- Headers returned: `X-RateLimit-Remaining`, `X-RateLimit-Reset`

---

## 5. API INVENTORY & GOVERNANCE

### API Registry

**Mandatory Registration:**
All APIs must be registered in the API catalog within 1 week of deployment.

**Catalog Fields:**

```
API ID: [UUID]
Name: [Human-readable name]
Owner: [Team]
Version: [1.0.0]
Maturity: [Alpha/Beta/Stable/Deprecated]
Classification: [Internal/Partner/Public]
Endpoint: https://api.enterprise.com/[path]
OpenAPI Spec: [Link to spec]
Documentation: [Link to docs]
Support: [Email/Slack channel]
SLA: [Availability target]
Last Audit: [Date]
Next Audit: [Date]
Status: [Active/Sunset Pending/Deprecated]
```

### Versioning Strategy

**Semantic Versioning: MAJOR.MINOR.PATCH**

| Version Type | When | Example |
|-------------|------|---------|
| MAJOR | Breaking changes | 1.0.0 → 2.0.0 |
| MINOR | Backward-compat new features | 1.0.0 → 1.1.0 |
| PATCH | Bug fixes | 1.0.0 → 1.0.1 |

**URL Versioning:**

```
/api/v1/users → Version 1
/api/v2/users → Version 2 (breaking change)
```

**Backward Compatibility:**

- Support last 2 major versions
- Deprecate with 6-month notice
- v1 sunset → v2 active → v3 released

---

## 6. API GOVERNANCE ROLES

| Role | Responsibility | Authority |
|------|----------------|-----------|
| **API Product Manager** | Business case, roadmap, deprecation | Prioritization |
| **API Architect** | Design standards, patterns | Tech decisions |
| **API Developer** | Implementation, documentation | Code quality |
| **Security Officer** | Threat modeling, security review | Approve/reject |
| **Ops/DevOps** | Deployment, monitoring, SLAs | Operational decisions |
| **Data Manager** | Data governance, privacy | Data access decisions |

---

## 7. API MATURITY MODEL

| Level | Design | Tests | Security | Monitoring |
|-------|--------|-------|----------|-----------|
| **1 - Prototype** | Informal | Manual | Ad-hoc | Minimal |
| **2 - Early** | OpenAPI started | Basic tests | Security review | Logs only |
| **3 - Growing** | Full OpenAPI | Comprehensive | Security gates | Dashboards |
| **4 - Stable** | Best practices | 100% coverage | Automated scanning | Full observability |
| **5 - Optimized** | API platform | Continuous | AI-based threat detection | Predictive |

**Current Target:** Level 3-4

---

## 8. COMMON API FAILURE MODES

### Problem: Unauthorized Access

**Symptom:** Anyone can call API regardless of permissions
**Root Cause:** Missing authorization checks
**Fix:**

```
if (!user.scopes.contains("api:write")) {
  return 401 Unauthorized;
}
```

### Problem: Slow API

**Symptom:** API latency > 500ms
**Root Cause:** N+1 query problem, large response
**Fix:**

- Batch database queries
- Implement pagination (default 20 items/page)
- Add caching (Redis)

### Problem: Data Leakage

**Symptom:** API returns unintended fields
**Root Cause:** No field-level authorization
**Fix:**

```
user_response = {
  id, name, email (public)
  // salary, ssn removed (private)
}
```

---

## 9. API COMPLIANCE CHECKLIST

### Design Phase

- [ ] OpenAPI specification complete
- [ ] Security model defined
- [ ] Rate limiting strategy
- [ ] Error handling documented
- [ ] Versioning planned

### Implementation Phase

- [ ] Code follows enterprise standards
- [ ] Unit tests written
- [ ] Documentation complete
- [ ] Logging/monitoring configured
- [ ] Secrets secured (no hardcoding)

### Security Phase

- [ ] OWASP Top 10 verified
- [ ] Penetration testing done
- [ ] Security scan passed
- [ ] CISO approval obtained

### Production Phase

- [ ] All tests passed
- [ ] Monitoring live
- [ ] Runbooks created
- [ ] Customer communication sent
- [ ] API registered in catalog

---

## 10. Contact and Escalation

Refer to the Governance Contact Directory in the Governance Charter for escalation procedures.

---

**Next Review:** August 2026
