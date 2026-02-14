# REST API Governance Profile

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Profile Description

Enterprise AI-Aligned Technical Governance Framework (EATGF)
Version: 1.0
Layer: 08_DEVELOPER_GOVERNANCE_LAYER → 02_API_GOVERNANCE
Profile Type: REST Architecture Implementation
Status: Authoritative Implementation Profile

## Purpose

Define enforceable governance standards for RESTful APIs within enterprise, SaaS, startup, and developer environments.

This profile operationalizes the [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md) specifically for REST-based systems and ensures:

- Protocol correctness alignment with RFC 9110
- Secure implementation patterns preventing OWASP API top 10 risks
- Version discipline preventing breaking changes
- Audit traceability for regulatory compliance
- Deployment gating before production release

**This is an enforcement profile, not a REST tutorial.**

## Architectural Position

- **Parent Standard:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **Enforcement Model:** [API_ENFORCEMENT_MATRIX.md](../API_ENFORCEMENT_MATRIX.md)
- **Mapping Authority:** [API_CONTROL_MAPPING_APPENDIX.md](../API_CONTROL_MAPPING_APPENDIX.md)
- **Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
- **Control Authority Relationship:** Implements root standard controls using REST-specific patterns

**Applies to:**

- Public APIs (web, mobile, partner)
- Internal microservices
- Partner integrations
- Mobile backend APIs
- SaaS multi-tenant REST APIs

**Mandatory for all HTTP-based production APIs.**

## Governance Principles

- **RFC Compliance:** All REST APIs must follow RFC 9110 HTTP semantics and RFC 3986 URI standards
- **Explicit Authentication:** Authentication must be expressed in every request; no implicit trust
- **Resource Authorization:** Authorization must be enforced at resource level (not just endpoint level)
- **Version Discipline:** Breaking changes prohibited without major version increment and deprecation window
- **Observable & Auditable:** All requests must be loggable, traceable, and auditable with correlation IDs
- **Deployment Gating:** Deployment without governance validation gates is non-compliant
- **No API Mutation Hiding:** Business logic cannot be hidden behind misleading status codes or response patterns

## REST Governance Requirements

### 1. HTTP Semantics (MANDATORY)

Correct HTTP verbs must map to operations:

| Method      | Operation               | Response Codes          | Idempotent | Use Case                                       |
| ----------- | ----------------------- | ----------------------- | ---------- | ---------------------------------------------- |
| **GET**     | Read resource           | 200, 404, 401, 403      | Yes        | Retrieve data without modification             |
| **POST**    | Create resource         | 201, 400, 401, 409      | No         | Create new resource; may return created object |
| **PUT**     | Replace entire resource | 200, 204, 400, 401, 404 | Yes        | Full resource replacement                      |
| **PATCH**   | Partial update          | 200, 204, 400, 401, 404 | No         | Partial fields only                            |
| **DELETE**  | Remove resource         | 204, 400, 401, 404      | Yes        | Permanent deletion                             |
| **HEAD**    | Read headers only       | 200, 404, 401           | Yes        | Like GET but no body                           |
| **OPTIONS** | Describe method options | 200, 404                | Yes        | CORS preflight; allowed methods                |

**Status codes must be meaningful:**

| Category | Code          | When to Use                                             |
| -------- | ------------- | ------------------------------------------------------- |
| **1xx**  | Informational | Rarely used in REST APIs                                |
| **2xx**  | Success       | Request succeeded as intended                           |
| **3xx**  | Redirect      | Resource moved; client should follow Location header    |
| **4xx**  | Client Error  | Bad request, auth failure, permission denial, not found |
| **5xx**  | Server Error  | Internal error, service unavailable, timeout            |

**Example (Compliant):**

```http
GET /api/v1/users/123 HTTP/1.1
Authorization: Bearer <token>

HTTP/1.1 200 OK
Content-Type: application/json

{"id": 123, "email": "user@example.com"}
```

```http
DELETE /api/v1/users/123 HTTP/1.1
Authorization: Bearer <token>

HTTP/1.1 204 No Content
```

**Example (Non-Compliant - Prohibited):**

```http
POST /deleteUser HTTP/1.1

HTTP/1.1 200 OK
{"status": "deleted"}  # Wrong: business logic hidden behind POST

GET /api/users/123 HTTP/1.1

HTTP/1.1 200 OK
{"error": "user not found"}  # Wrong: resource doesn't exist but returns 200
```

### 2. Authentication (MANDATORY)

**Approved mechanisms:**

- OAuth 2.0 (RFC 6749) - Recommended for public APIs
- OpenID Connect (RFC 6749 + identity) - Recommended for multi-user SaaS
- Mutual TLS (RFC 8705) - Recommended for service-to-service
- JWT (RFC 7519) - Must include RS256/ES256 signature, never plaintext
- API Keys - Internal only; not for public APIs

**Authentication must be:**

- Explicit in every request (Authorization header or equivalent)
- Validated before processing any business logic
- Token expiration enforced (max 1 hour for access tokens)
- Token freshness verified (not issued in future)

**Example (FastAPI with OAuth2):**

```python
from fastapi import Depends, HTTPException
from jose import jwt
from datetime import datetime

def verify_bearer_token(token: str):
    """Validate JWT token with expiration check"""
    try:
        # Decode with RS256 public key
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])

        # Verify expiration
        exp = payload.get("exp")
        if exp is None:
            raise HTTPException(status_code=401, detail="Token missing expiration")
        if datetime.fromtimestamp(exp) < datetime.utcnow():
            raise HTTPException(status_code=401, detail="Token expired")

        # Verify issued-at (nbf) not in future
        nbf = payload.get("nbf", 0)
        if datetime.fromtimestamp(nbf) > datetime.utcnow():
            raise HTTPException(status_code=401, detail="Token not yet valid")

        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/api/v1/users/{user_id}")
def get_user(user_id: int, token: dict = Depends(verify_bearer_token)):
    user_id_claim = token.get("sub")
    # Verify user can access this resource
    return get_user_data(user_id)
```

**Non-Compliant Examples (Prohibited):**

```python
# Wrong: No authentication validation
@app.get("/users/{user_id}")
def get_user_insecure(user_id: int):
    return get_user_data(user_id)  # Any caller can access

# Wrong: Plaintext token
@app.post("/api/users")
def create_user(password: str):  # Password in plaintext response/request
    return {"token": password}  # Token not encrypted

# Wrong: No expiration check
def verify_token_bad(token: str):
    payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
    return payload  # Doesn't check exp, nbf, iat
```

### 3. Authorization (MANDATORY)

**Must enforce:**

- **RBAC (Role-Based Access Control):** User has role → Role has permissions → Endpoint/resource requires permission
- **ABAC (Attribute-Based Access Control):** Decisions based on user attributes, resource attributes, environment (for SaaS multi-tenancy)
- **Resource-Level Authorization:** Verify user can access specific resource instance (not just endpoint)
- **Tenant Isolation (SaaS):** User from Tenant A cannot access Tenant B data
- **No Implicit Trust:** Absence of deny = don't assume allow

**Example (Resource-Level RBAC):**

```python
from fastapi import Depends, HTTPException

def authorize_resource_access(user: dict, tenant_id: int, resource_id: int):
    """Enforce resource-level authorization"""

    # 1. Check user belongs to tenant
    if user["tenant_id"] != tenant_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    # 2. Check user has role with permission
    if "viewer" not in user["roles"] and "editor" not in user["roles"]:
        raise HTTPException(status_code=403, detail="Forbidden")

    # 3. Verify resource exists in this tenant
    resource = db.get_resource(resource_id)
    if resource.tenant_id != tenant_id:
        raise HTTPException(status_code=404, detail="Not found")

    # 4. Check edit permission if needed
    if editing and "editor" not in user["roles"]:
        raise HTTPException(status_code=403, detail="Forbidden")

    return resource

@app.get("/api/v1/tenants/{tenant_id}/resources/{resource_id}")
def get_resource(
    tenant_id: int,
    resource_id: int,
    user: dict = Depends(get_current_user)
):
    resource = authorize_resource_access(user, tenant_id, resource_id)
    return resource
```

**Non-Compliant Examples (Prohibited):**

```python
# Wrong: BOLA - broken object-level authorization
@app.get("/users/{user_id}")
def get_user_bola(user_id: int, current_user: dict = Depends(get_current_user)):
    return db.get_user(user_id)  # No check if current_user can access user_id

# Wrong: No tenant isolation
@app.get("/resources/{resource_id}")
def get_resource_no_tenant(resource_id: int):
    return db.get_resource(resource_id)  # Any user can access any resource

# Wrong: Implicit trust
@app.post("/admin/settings")
def update_settings(settings: dict, user: dict = Depends(get_current_user)):
    # Assumes if we got here, user is admin (wrong!)
    db.update_settings(settings)
```

### 4. Input Validation (MANDATORY)

**All payloads must be validated against schema:**

- Enforce strict typing
- Reject unknown fields
- Validate ranges, formats, lengths
- Sanitize strings before storage
- Prevent injection attack vectors

**Example (Pydantic schemas):**

```python
from pydantic import BaseModel, EmailStr, Field

class CreateUserRequest(BaseModel):
    email: EmailStr  # Validates email format
    password: str = Field(min_length=12, max_length=256)
    age: int = Field(ge=0, le=150)

    class Config:
        extra = "forbid"  # Reject unknown fields

class Config:
    json_schema_extra = {
        "example": {
            "email": "user@example.com",
            "password": "SecurePassword123!",
            "age": 30
        }
    }

@app.post("/api/v1/users")
def create_user(request: CreateUserRequest):
    # Pydantic automatically validates before function called
    db.create_user(request.email, request.password, request.age)
```

**Example OpenAPI Schema Validation:**

```yaml
components:
  schemas:
    CreateUser:
      type: object
      required:
        - email
        - password
      properties:
        email:
          type: string
          format: email
        password:
          type: string
          minLength: 12
          maxLength: 256
        age:
          type: integer
          minimum: 0
          maximum: 150
      additionalProperties: false # Reject unknown fields
```

**Non-Compliant Examples (Prohibited):**

```python
# Wrong: No schema validation
@app.post("/users")
def create_user_unvalidated(request: dict):
    db.create_user(request)  # No type checking, length checking

# Wrong: No length/format constraints
@app.post("/users")
def create_user_unconstrained(name: str, age: int):
    db.create_user(name, age)  # age could be -999; name could be 10MB string

# Wrong: Accepts unknown fields
class UserBad(BaseModel):
    email: str
    # Missing: class Config: extra = "forbid"
```

### 5. Rate Limiting (MANDATORY for Public APIs)

**Protect against:**

- Abuse (resource exhaustion)
- DDoS amplification
- Enumeration attacks (password guessing, user ID enumeration)
- Resource starvation

**Rate limit tiers:**

| Tier           | Rate Limit    | Use Case                      | Response Code               |
| -------------- | ------------- | ----------------------------- | --------------------------- |
| **Free**       | 10 req/min    | Public, unauthenticated       | 429 Too Many Requests       |
| **Startup**    | 100 req/min   | Early customers               | 429 with Retry-After header |
| **Pro**        | 1,000 req/min | Standard SaaS customers       | 429 with Retry-After header |
| **Enterprise** | Unlimited     | Large customers with contract | No limit; monitored         |

**Example (Nginx configuration):**

```nginx
limit_req_zone $binary_remote_addr zone=api_free:10m rate=10r/m;
limit_req_zone $http_x_api_key zone=api_authenticated:10m rate=1000r/m;

server {
    location /api/v1/ {
        # Unauthenticated: 10 req/min per IP
        limit_req zone=api_free burst=5 nodelay;

        # Authenticated: 1000 req/min per API key
        limit_req zone=api_authenticated burst=50 nodelay;

        # Return 429 with Retry-After
        error_page 429 = @rate_limit_exceeded;
    }

    location @rate_limit_exceeded {
        default_type application/json;
        return 429 '{"error": "Rate limit exceeded"}';
        add_header Retry-After 60;
    }
}
```

**Example (FastAPI):**

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/v1/users")
@limiter.limit("100/minute")
def create_user(request: Request):
    # FastAPI SlowAPI automatically enforces and returns 429
    pass
```

### 6. API Versioning (MANDATORY)

**Versioning prevents breaking changes:**

- Semantic Versioning (MAJOR.MINOR.PATCH)
- MAJOR = breaking changes
- MINOR = backward-compatible features
- PATCH = backward-compatible fixes

**Approved strategies:**

**Option A: URI Versioning (Recommended)**

```http
GET /api/v1/users/123         # Version 1
GET /api/v2/users/123         # Version 2 (breaking changes)
```

**Breaking changes in v2:**

- Different request/response schema
- Different auth mechanism
- Different status code meanings

**Deprecation for v1:**

- Announce deprecation (email, API notification)
- Support for minimum 6 months
- Return Deprecation and Sunset headers

```http
GET /api/v1/users HTTP/1.1

HTTP/1.1 200 OK
Deprecation: true
Sunset: Wed, 31 Dec 2024 23:59:59 GMT
Link: </api/v2/users>; rel="successor-version"

{"id": 123, "email": "user@example.com"}
```

**Option B: Header-Based Versioning**

```http
GET /api/users/123 HTTP/1.1
Accept: application/vnd.myapi.v1+json

HTTP/1.1 200 OK
Content-Type: application/vnd.myapi.v1+json
```

**OpenAPI Versioning:**

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 2.0.0 # Semantic version

paths:
  /api/v2/users:
    get:
      deprecated: true
      x-sunset-date: "2024-12-31"
```

**Non-Compliant (Prohibited):**

```http
# Wrong: No versioning
GET /api/users/123

# Wrong: Breaking change without major version
GET /api/v1/users/123
# Response changed from {"id": 123} to {"userId": 123}
# Without /v2/, causes client breakage
```

### 7. Logging & Observability (MANDATORY)

**Must log:**

- **Request ID** / **Correlation ID** (UUID; persisted across services)
- **User ID** (who made the request)
- **Endpoint** (GET /api/v1/users)
- **HTTP Verb & Status** (POST 201, GET 404, PUT 403)
- **Execution Time** (duration in ms)
- **Error Details** (stack trace for 5xx; NOT sensitive data)

**Must NOT log:**

- Passwords
- API keys, tokens, credentials
- PII (unless required; must be encrypted at rest)
- Credit card numbers
- Social security numbers

**Example (Structured JSON logging):**

```python
import json
import uuid
from datetime import datetime

def log_request(request, response, duration_ms):
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "correlation_id": correlation_id,
        "user_id": request.user_id,  # From JWT
        "method": request.method,
        "endpoint": request.url.path,
        "status_code": response.status_code,
        "duration_ms": duration_ms,
        "client_ip": request.client.host,
        "error": response.get("error") if response.status_code >= 400 else None
    }

    logger.info(json.dumps(log_entry))  # Structured JSON
    return correlation_id

@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start) * 1000

    log_request(request, response, duration_ms)
    response.headers["X-Correlation-ID"] = correlation_id

    return response
```

### 8. OpenAPI Specification (MANDATORY)

**All production APIs must publish machine-readable OpenAPI spec:**

**Spec must include:**

- Title, description, version
- All endpoints with methods
- Request/response schemas
- Authentication scheme
- Status codes
- Rate limit information (x-rate-limit)

**Example (FastAPI auto-generates OpenAPI):**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="User API",
    description="Manages user accounts",
    version="2.0.0"
)

class User(BaseModel):
    id: int
    email: str
    created_at: str

@app.get(
    "/api/v2/users/{user_id}",
    response_model=User,
    responses={
        404: {"description": "User not found"},
        401: {"description": "Unauthorized"}
    }
)
def get_user(user_id: int):
    """Retrieve user by ID"""
    return {"id": user_id, "email": "user@example.com"}

# Generates: /openapi.json (machine readable)
```

**OpenAPI 3.0 YAML Example:**

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 2.0.0

servers:
  - url: https://api.example.com
    description: Production

paths:
  /api/v2/users/{user_id}:
    get:
      operationId: getUser
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        "200":
          description: User found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/User"
        "404":
          description: User not found
        "401":
          description: Unauthorized

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        email:
          type: string
          format: email
        created_at:
          type: string
          format: date-time
```

### 9. CI/CD Security Gate (MANDATORY)

**Deployment pipeline must include gates:**

| Gate                  | Tool                    | Pass Criteria             | Failure Behavior    |
| --------------------- | ----------------------- | ------------------------- | ------------------- |
| **Secrets Scan**      | GitLeaks, TruffleHog    | No hardcoded credentials  | BLOCK deployment    |
| **SAST**              | Bandit (Python), CodeQL | No HIGH/CRITICAL findings | BLOCK deployment    |
| **Dependency**        | pip-audit, Snyk         | No CVE in dependencies    | WARN (can override) |
| **Schema Validation** | OpenAPI Validator       | OpenAPI spec valid        | BLOCK deployment    |
| **Unit Tests**        | pytest, jest            | 80%+ code coverage        | BLOCK deployment    |
| **Type Checking**     | mypy (Python)           | No type errors            | WARN (can override) |

**Example (GitHub Actions):**

```yaml
name: API Security Check

on:
  pull_request:
    paths:
      - "api/**"
  push:
    branches:
      - main

jobs:
  security-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Secrets Detection
        uses: gitleaks/gitleaks-action@v2
        with:
          fail: true

      - name: SAST Scan (Bandit)
        run: |
          pip install bandit
          bandit -r api/ -f json -o bandit-report.json
          if grep -q '"severity": "HIGH"' bandit-report.json; then
            echo "SAST findings detected"
            exit 1
          fi

      - name: OpenAPI Validation
        run: |
          npm install -g @stoplight/spectral-cli
          spectral lint api/openapi.yaml --ruleset https://unpkg.com/@stoplight/spectral-rulesets@latest/dist/oas.mjs

      - name: Dependency Audit
        run: |
          pip install pip-audit
          pip-audit --desc

      - name: Unit Tests
        run: |
          pip install pytest pytest-cov
          pytest api/ --cov=api --cov-fail-under=80
```

## Severity & Maturity

**Severity Model and Maturity Progression are defined in [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md) and apply uniformly across all architecture profiles.**

REST APIs inherit the standard 5-level maturity model and organizational profile severity escalation (Enterprise → SaaS → Startup → Developer).

## Control Mapping

| EATGF Control        | ISO 27001:2022 | NIST SSDF | OWASP API | COBIT 2019 |
| -------------------- | -------------- | --------- | --------- | ---------- |
| **Authentication**   | A.8.2          | PW.1      | API2      | EDM03      |
| **Authorization**    | A.8.2, A.8.5   | PW.4      | API1      | DSS05      |
| **Input Validation** | A.8.22         | PW.5      | API3      | BAI03      |
| **Rate Limiting**    | A.8.30         | RV.1      | API4      | DSS02      |
| **Logging**          | A.8.15, A.8.16 | RV.2      | API10     | MEA01      |
| **Versioning**       | A.8.31         | PO.3      | API7      | BAI07      |
| **OpenAPI Spec**     | A.8.29         | PW.3      | API9      | BAI01      |

## Developer Checklist

Before submitting REST API for deployment:

- [ ] **HTTP Semantics:** Correct verbs (GET, POST, PUT, PATCH, DELETE); meaningful status codes
- [ ] **Authentication:** OAuth2/OIDC/mTLS implemented; tokens validated on every request
- [ ] **Authorization:** RBAC/ABAC defined; resource-level checks enforced; no BOLA vulnerabilities
- [ ] **Input Validation:** Pydantic/JSON Schema validation; unknown fields rejected; no injection patterns
- [ ] **Rate Limiting:** Configured per tier (Free/Startup/Pro/Enterprise); 429 responses working
- [ ] **Versioning:** Semantic version enforced; deprecation window documented; Sunset headers present
- [ ] **OpenAPI Spec:** 3.0+ spec complete; validated with Spectral; matches implementation
- [ ] **Logging:** JSON structured; correlation IDs present; no sensitive data leaked
- [ ] **CI/CD Gates:** SAST passed; dependencies audited; tests passing (80%+ coverage)
- [ ] **Documentation:** README with examples; error codes documented; version migration guide provided

**Deployment without checklist completion is non-compliant.**

## Governance Implications

### Risk If Not Enforced

- **Authentication Bypass:** Attackers gain access without credentials (OWASP API2)
- **Broken Object Access:** Users access other users' data (OWASP API1 - BOLA)
- **Input Injection:** SQL injection, NoSQL injection, OS command injection via unvalidated inputs
- **DDoS Vulnerability:** Missing rate limiting enables resource exhaustion attacks
- **Silent Breaking Changes:** API versions change without client notification; mobile/SaaS integrations break
- **Audit Gap:** Missing correlation IDs prevent incident investigation and regulatory compliance

### Operational Impact

- **Developers:** Must implement 9 mandatory controls; estimated 2-3 weeks per API
- **QA/Testing:** SAST scanning, rate limit testing, security regression testing required
- **Operations:** Logs must be structured, searchable, retained 90+ days
- **Security:** Incident response accelerated with correlation IDs; forensics enabled

### Audit Consequences

- **ISO 27001:** A.8.2 (Authentication), A.8.5 (Access Control), A.8.15 (Logging) certification findings
- **SOC 2 Type II:** CC6 (Logical Access), CC7 (System Monitoring) require evidencing control implementation
- **PCI-DSS:** Requirements 2 (Auth), 6 (Input Validation), 8 (Access Control) depend on REST governance
- **GDPR:** Article 32 (Technical Measures) requires encryption, authentication, logging
- **Incident Response:** 72-hour breach notification requires immediate access to audit logs

### Compliance Risk

Absence of REST governance exposes organization to:

- Regulatory fines (GDPR €20M, HIPAA $1.5M/violation)
- Customer data breaches
- Certification audit failures
- Reputational damage
- M&A diligence failures

## Official References

- **Root Authority:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **Enforcement:** [API_ENFORCEMENT_MATRIX.md](../API_ENFORCEMENT_MATRIX.md)
- **Framework Mapping:** [API_CONTROL_MAPPING_APPENDIX.md](../API_CONTROL_MAPPING_APPENDIX.md)
- **ISO/IEC 27001:2022:** Annex A (Information Security Controls)
- **NIST SP 800-218:** Secure Software Development Framework
- **OWASP API Security Top 10 2023:** <https://owasp.org/www-project-api-security>
- **COBIT 2019:** Process Reference Guide (ISACA)
- **RFC 9110:** HTTP Semantics and Connection Management
- **RFC 6749:** OAuth 2.0 Authorization Framework
- **RFC 7519:** JSON Web Token (JWT)
- **RFC 8705:** OAuth 2.0 Mutual-TLS Client Authentication
- **RFC 8594:** The Sunset HTTP Header Field

## Version Information

| Element                                | Value                                                                                               |
| -------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Document Version**                   | 1.0 (Initial Release)                                                                               |
| **Change Type**                        | Major (new framework profile for REST APIs)                                                         |
| **Issue Date**                         | 2024-Q1                                                                                             |
| **Profile Type**                       | REST Architecture Implementation                                                                    |
| **Relation to EATGF**                  | Implements EATGF Layer 08, Domain 02; operationalizes API_GOVERNANCE_STANDARD for HTTP/REST systems |
| **Applicable Organizational Profiles** | Enterprise, SaaS, Startup, Developer (severity escalation per profile)                              |
| **Next Review**                        | Q2 2024 (align with emerging REST standards, HTTP/3 adoption)                                       |
