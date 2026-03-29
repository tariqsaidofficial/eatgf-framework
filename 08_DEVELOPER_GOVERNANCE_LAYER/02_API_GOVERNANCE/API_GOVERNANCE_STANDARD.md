# API Governance Standard

Enterprise AI-Aligned Technical Governance Framework (EATGF)

> **Authority Notice:** This document is the authoritative governance definition. Annexes and Profiles are derivative and must not redefine controls.

## Purpose

Define mandatory governance controls for designing, building, securing, versioning, operating, and decommissioning APIs across Web, Mobile, SaaS, and Enterprise systems.

This standard ensures APIs are:

- Secure by design
- Consistently documented
- Backward compatible
- Auditable
- Compliant with international security standards

This document operationalizes API-related controls from the EATGF Master Control Matrix and Developer Governance Layer.

## Architectural Position

EATGF Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Root Authority for API Governance Domain
Control Reference: SDLC-API-01

Scope:

- REST APIs
- GraphQL APIs
- gRPC services
- Webhooks
- Internal microservice APIs
- Public external APIs

Authority Level:

- Mandatory for Enterprise and SaaS
- Mandatory for Startup handling sensitive data
- Recommended for individual developers

Integrated With:

- SECURE_SDLC_GOVERNANCE_STANDARD.md (parent)
- ANNEX_B_SECURE_CODING_STANDARD.md (input validation)
- ANNEX_C_SECURE_PIPELINE_STANDARD.md (artifact integrity)
- ANNEX_G_SECRETS_MANAGEMENT_STANDARD.md (credential protection)

## Governance Principles

- API-First Architecture – APIs are primary security boundary
- Contract-Driven Development – OpenAPI / AsyncAPI / Protobuf baseline
- Security-By-Default – No anonymous production APIs permitted
- Backward Compatibility Discipline – Explicit versioning required
- Zero Trust Access Model – Authentication + authorization mandatory
- Observability Required – All API calls auditable
- Formal Deprecation Lifecycle – Minimum 6-month notice period

## Technical Implementation

### Control 1: Authentication

Allowed mechanisms:

- OAuth 2.1 (authorization code flow)
- OpenID Connect (identity verification)
- mTLS (service-to-service)
- Signed JWT (RS256 / ES256 only)

Example – FastAPI + OAuth2:

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
```

No API endpoint may bypass authentication in production.

### Control 2: Authorization

Authorization must be:

- Role-Based (RBAC) or
- Attribute-Based (ABAC)

Authorization must be evaluated at:

- Endpoint level
- Resource ownership level
- Tenant boundary (for SaaS)

### Control 3: Versioning

Versioning strategies:

- URI Versioning (/v1/)
- Header-based versioning
- Semantic versioning policy required

Example:

```
GET /api/v1/users
```

Deprecation Policy:

- Minimum 6-month support window
- Deprecation notice header required:

```
Deprecation: true
Sunset: Tue, 31 Dec 2026 23:59:59 GMT
```

### Control 4: Rate Limiting

Minimum controls:

- IP throttling
- Token-based quotas
- Burst limits

Example – NGINX:

```nginx
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;

server {
    location /api/ {
        limit_req zone=api_limit burst=20 nodelay;
    }
}
```

### Control 5: Input Validation

- Schema validation required
- Reject unknown fields
- Enforce type strictness

Example – Pydantic:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    age: int
```

### Control 6: Logging and Observability

APIs must log:

- Request ID
- User ID (if authenticated)
- Response code
- Latency
- Correlation ID

Structured JSON logging required.

### Control 7: Webhook Security

Webhooks must:

- Use HMAC signatures
- Validate timestamp tolerance
- Support replay protection

Example:

```python
import hmac
import hashlib

def verify_signature(payload, signature, secret):
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
```

### Control 8: API Documentation

Every API must publish:

- OpenAPI 3.0+
- Error schema definitions
- Authentication scheme
- Version information
- Deprecation notices

## Control Mapping

| Framework                 | Reference              |
| ------------------------- | ---------------------- |
| ISO 27001:2022            | A.8.20, A.8.23, A.8.28 |
| NIST SSDF (SP 800-218)    | PW.4, RV.1, PO.3       |
| OWASP API Security Top 10 | API1, API2, API3, API8 |
| COBIT 2019                | DSS05, APO13           |
| NIST SP 800-53 Rev.5      | AC-3, SC-12, SI-10     |

## Developer Checklist

Before production deployment:

- Authentication enforced
- Authorization policy tested
- Rate limiting configured
- OpenAPI spec updated
- Input validation strict
- Logging structured
- Version declared
- Deprecation policy documented
- Security testing completed
- OWASP API Top 10 reviewed
- Webhook signature verification implemented (if applicable)

## Governance Implications

**Risk Mitigation:**

- Prevent broken object level authorization (OWASP API1)
- Prevent mass assignment (OWASP API2)
- Prevent credential exposure in requests/responses
- Prevent resource exhaustion via rate limiting

**Operational Impact:**

- Requires API Gateway (Kong, AWS API Gateway, etc.)
- Requires logging infrastructure (ELK, Datadog)
- Requires CI security scanning

**Audit Readiness:**

- OpenAPI documentation serves as control evidence
- Versioning records serve as change control evidence
- Gateway logs serve as audit logs

## Official References

- NIST SP 800-218 (Secure Software Development Framework)
- ISO/IEC 27001:2022
- OWASP API Security Top 10
- NIST SP 800-53 Rev.5
- COBIT 2019 (ISACA)
- IETF RFC 6749 (OAuth 2.0)
- IETF RFC 7519 (JWT)
- OpenAPI Specification 3.0
- RFC 7234 (HTTP Caching)

## Version

Version: 1.0
Status: Authoritative Root Authority
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
