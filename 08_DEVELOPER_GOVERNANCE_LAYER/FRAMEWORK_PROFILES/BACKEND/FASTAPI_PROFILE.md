# FastAPI Framework Governance Profile

> **Authority Notice:** This profile implements EATGF controls for FastAPI-based backend systems. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW FastAPI applications satisfy Secure SDLC (Layer 01), API Governance (Layer 05), and DevSecOps (Layer 03) requirements.

## Purpose

This document defines the governance conformance model for FastAPI-based backend systems operating under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It translates EATGF Secure SDLC, API Governance, DevSecOps, and Runtime Security controls into enforceable technical requirements for high-performance async REST APIs.

This profile applies to:

- API-first SaaS platforms
- Microservices architectures
- Internal service layers
- High-throughput async backends
- Real-time data streaming APIs

## Architectural Position

**EATGF Layer:**

- Primary: `08_DEVELOPER_GOVERNANCE_LAYER` → `FRAMEWORK_PROFILES` → `BACKEND`
- References: Layer 01 (Secure SDLC), Layer 05 (API Governance), Layer 03 (DevSecOps)

**Scope:**
FastAPI acts as:

- HTTP boundary enforcement layer
- API contract generator (OpenAPI)
- Input validation enforcement surface
- Token validation control point
- Multi-tenant context propagator

**FastAPI Classification:**

- API-native enforcement framework
- Automatic OpenAPI schema generation
- Type-safe via Pydantic validation
- Async-first runtime model
- Application security boundary

**Conformance Obligations:**

- ✅ 01_SECURE_SDLC standards
- ✅ 02_API_GOVERNANCE standards (REST-specific controls)
- ✅ 03_DEVSECOPS standards
- ✅ 04_CLOUD standards (if deployed in SaaS context)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

FastAPI profiles enforce:

- **Dependency scanning:** `pip-audit`, `bandit` in CI/CD pipeline
- **SAST rules:** Bandit plugin for Python security checks
- **Type checking:** `mypy` with strict mode for type safety
- **Test coverage requirement:** Minimum 80% unit + integration test coverage

### Layer 03: DevSecOps Governance

FastAPI profiles reference:

- **Container security:** `docker/Dockerfile` multi-stage builds
- **CI/CD pipeline gates:** Pre-merge, pre-release, pre-production stages
- **Secrets management:** Environment variables from HashiCorp Vault or AWS Secrets Manager
- **Image scanning:** Trivy/Grype vulnerability scanning + SBOM generation

### Layer 05: Domain Frameworks

FastAPI profiles implement API Governance controls:

- **Authentication:** JWT/OIDC via `fastapi.security` (not session-based)
- **Authorization:** Dependency injection + custom permission classes
- **Rate Limiting:** `slowapi` decorator-based approach
- **OpenAPI/Swagger:** Automatic generation with Pydantic models
- **Versioning:** URL-based versioning (`/api/v1/`, `/api/v2/`)

### Layer 04: Cloud Governance (Conditional)

If deployed in cloud infrastructure:

- **HTTPS enforcement:** SSL/TLS termination at load balancer
- **Environment config:** CloudFormation/Terraform for reproducibility
- **Database encryption:** RDS/CloudSQL encryption at rest + TLS in transit
- **IAM scoping:** Service-specific IAM roles for FastAPI instances

## Governance Principles

### 1. Type-Enforced Input Validation (Mandatory)

All request and response bodies must use explicit Pydantic models.

```python
from pydantic import BaseModel, Field

class InvoiceCreateRequest(BaseModel):
    amount: float = Field(gt=0, description="Invoice amount in cents")
    currency: str = Field(min_length=3, max_length=3)
    tenant_id: str

    class Config:
        json_schema_extra = {
            "example": {
                "amount": 9999,
                "currency": "USD",
                "tenant_id": "tenant-123"
            }
        }
```

**Constraint:** Unvalidated dict payload usage is a governance violation

### 2. Explicit Authentication Enforcement

Session-based authentication is prohibited for API deployments.

JWT or OIDC required.

```python
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = jwt.decode(token, SECRET_KEY, algorithms=["RS256"], audience="https://api.example.com")
    return payload
```

**Token must include:**

- `exp` (expiration)
- `sub` (subject/user ID)
- `tenant_id` (tenant scope)
- `aud` (audience)
- `iat` (issued at)

### 3. Tenant Context Isolation

All queries must be scoped to tenant context derived from token.

```python
async def get_current_user(token: str = Depends(verify_token)):
    return {
        "user_id": token["sub"],
        "tenant_id": token["tenant_id"],
    }

@app.get("/api/v1/invoices")
async def list_invoices(
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_db)
):
    # Tenant filtering enforced at query layer
    result = await session.execute(
        select(Invoice).filter(Invoice.tenant_id == current_user["tenant_id"])
    )
    return result.scalars().all()
```

**Constraint:** Cross-tenant leakage classified as critical severity

### 4. Secure-by-Default App Initialization

```python
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI(
    title="Enterprise API",
    description="EATGF-compliant API",
    version="1.0.0",
    docs_url=None,  # Disable Swagger in production
    redoc_url=None,
    openapi_url="/api/v1/openapi.json",  # Protected endpoint
)

# Only trust specific hosts
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["api.example.com", "api-backup.example.com"]
)
```

**Constraint:** Swagger UI must not be exposed publicly without access control

### 5. Secrets Isolation

Secrets must originate from managed secret store.

```python
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = os.environ["DATABASE_URL"]
    jwt_public_key: str = os.environ["JWT_PUBLIC_KEY"]
    api_key: str = os.environ["API_KEY"]

    class Config:
        env_file = ".env.production"  # Only for staging/local

settings = Settings()
```

**Constraint:** Hardcoded secrets are MANDATORY violation

### 6. Structured Logging with Correlation IDs

```python
import logging
import json
from contextvars import ContextVar

correlation_id_var: ContextVar[str] = ContextVar("correlation_id", default="")

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": self.formatTime(record),
            "correlation_id": correlation_id_var.get(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        return json.dumps(log_entry)

logger = logging.getLogger("security")
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    import uuid
    correlation_id_var.set(str(uuid.uuid4()))
    response = await call_next(request)
    return response
```

**Logs must support:**

- Correlation ID (request tracing)
- Tenant ID (multi-tenant audit)
- Request path (endpoint tracking)
- Response status (outcome tracking)
- Latency (performance monitoring)

## Governance Conformance

This section maps the 8 mandatory controls from Layer 05 (API Governance) to FastAPI-specific implementation patterns.

### Control 1: Authentication

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Use `fastapi.security.HTTPBearer` or `HTTPAuthorizationCredentials` for JWT
- Validate token signature against IdP public keys (cached)
- Enforce token expiry; refresh tokens rotated server-side
- Reject sessions for API endpoints; use JWT only

**Compliant Example:**

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            settings.JWT_PUBLIC_KEY,
            algorithms=["RS256"],
            audience="https://api.example.com",
            options={"verify_exp": True}
        )
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/api/v1/me")
async def get_user(token: dict = Depends(verify_token)):
    return {"user_id": token["sub"], "tenant_id": token["tenant_id"]}
```

**Non-Compliant Example:**

```python
# ❌ Session authentication for API
@app.get("/api/v1/me")
async def get_user(request: Request):
    user = request.session.get("user")  # Vulnerable
    return {"user": user}
```

### Control 2: Authorization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Define custom permission dependency injector functions
- Enforce tenant scoping at query layer
- Use FastAPI `Depends()` for permission composition
- Deny by default; explicitly grant scopes

**Compliant Example:**

```python
async def check_invoice_ownership(
    invoice_id: int,
    current_user: dict = Depends(verify_token),
    session: AsyncSession = Depends(get_db)
):
    invoice = await session.get(Invoice, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404)
    if invoice.tenant_id != current_user["tenant_id"] or \
       invoice.user_id != current_user["sub"]:
        raise HTTPException(status_code=403, detail="Forbidden")
    return invoice

@app.get("/api/v1/invoices/{invoice_id}")
async def get_invoice(invoice: Invoice = Depends(check_invoice_ownership)):
    return invoice
```

**Non-Compliant Example:**

```python
# ❌ No object-level permission check
@app.get("/api/v1/invoices/{invoice_id}")
async def get_invoice(
    invoice_id: int,
    session: AsyncSession = Depends(get_db),
    current_user: dict = Depends(verify_token)
):
    invoice = await session.get(Invoice, invoice_id)
    return invoice  # Missing tenant/ownership check
```

### Control 3: API Versioning

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Use URL-based versioning: `/api/v1/`, `/api/v2/`
- Maintain backward compatibility for 12 months
- Deprecate old versions with HTTP `Sunset` header
- Document breaking changes in CHANGELOG

**Compliant Example:**

```python
from fastapi import APIRouter

router_v1 = APIRouter(prefix="/api/v1", tags=["invoices"])
router_v2 = APIRouter(prefix="/api/v2", tags=["invoices"])

@router_v1.get("/invoices")
async def list_invoices_v1(session: AsyncSession = Depends(get_db)):
    # Legacy response format
    return {"invoices": [...], "count": 10}

@router_v2.get("/invoices")
async def list_invoices_v2(
    session: AsyncSession = Depends(get_db),
    response: Response
):
    # New response format with additional fields
    response.headers["Sunset"] = "Sun, 31 Dec 2026 23:59:59 GMT"
    return {"data": [...], "pagination": {"count": 10, "page": 1}}

app.include_router(router_v1)
app.include_router(router_v2)
```

**Non-Compliant Example:**

```python
# ❌ No versioning; breaking changes in place
@app.get("/api/invoices")
async def list_invoices(session: AsyncSession = Depends(get_db)):
    # Breaking change: removed `count` field
    return {"data": [...]}
```

### Control 4: Input Validation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Use Pydantic models with strict type validation
- Implement custom validators for business logic
- Reject unknown fields: `model_config = ConfigDict(extra="forbid")`
- Sanitize/validate before database queries

**Compliant Example:**

```python
from pydantic import BaseModel, Field, field_validator, ConfigDict

class InvoiceCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")  # Reject unknown fields

    amount: float = Field(gt=0, le=999999.99, description="Amount in cents")
    currency: str = Field(min_length=3, max_length=3, pattern="^[A-Z]{3}$")
    description: str = Field(min_length=1, max_length=500)
    tenant_id: str = Field(min_length=1, max_length=255)

    @field_validator("currency")
    @classmethod
    def validate_currency(cls, v):
        allowed = ["USD", "EUR", "GBP"]
        if v not in allowed:
            raise ValueError(f"Currency must be one of {allowed}")
        return v

@app.post("/api/v1/invoices")
async def create_invoice(
    invoice: InvoiceCreate,
    current_user: dict = Depends(verify_token),
    session: AsyncSession = Depends(get_db)
):
    # Pydantic validation already passed; safe to use
    new_invoice = Invoice(**invoice.model_dump())
    session.add(new_invoice)
    await session.commit()
    return new_invoice
```

**Non-Compliant Example:**

```python
# ❌ No Pydantic validation; dict payload
@app.post("/api/v1/invoices")
async def create_invoice(
    invoice: dict,  # Unvalidated dict
    session: AsyncSession = Depends(get_db)
):
    new_invoice = Invoice(**invoice)  # Injection risk
    session.add(new_invoice)
    await session.commit()
    return new_invoice
```

### Control 5: Rate Limiting

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Use `slowapi` library for decorator-based rate limiting
- Enforce per-IP, per-user-tier limits
- Return 429 status with `Retry-After` header
- Log all rate limit hits for abuse detection

**Compliant Example:**

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

class RateLimitConfig:
    FREE_TIER = "10/minute"
    STANDARD_TIER = "100/minute"
    PREMIUM_TIER = "10000/minute"

@app.get("/api/v1/invoices")
@limiter.limit(RateLimitConfig.STANDARD_TIER)
async def list_invoices(
    request: Request,
    current_user: dict = Depends(verify_token),
    session: AsyncSession = Depends(get_db)
):
    # Get user tier from JWT claims
    tier = current_user.get("tier", "standard")
    # Rate limit applied by @limiter decorator
    return await session.execute(
        select(Invoice).filter(Invoice.tenant_id == current_user["tenant_id"])
    )
```

**Non-Compliant Example:**

```python
# ❌ No rate limiting; open to DoS
@app.get("/api/v1/invoices")
async def list_invoices(current_user: dict = Depends(verify_token)):
    # No rate limit protection
    return [...]
```

### Control 6: Testing & Documentation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Unit tests ≥80% code coverage
- Integration tests for all API endpoints
- OpenAPI schema auto-generated and validated
- Document all breaking changes in CHANGELOG.md

**Compliant Example:**

```python
# tests/test_invoices.py
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_token():
    return jwt.encode(
        {"sub": "user-123", "tenant_id": "tenant-1"},
        settings.JWT_SECRET,
        algorithm="RS256"
    )

def test_list_invoices_auth_required(client):
    response = client.get("/api/v1/invoices")
    assert response.status_code == 403

def test_list_invoices_tenant_filtered(client, auth_token):
    response = client.get(
        "/api/v1/invoices",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert all(inv["tenant_id"] == "tenant-1" for inv in response.json())

def test_list_invoices_cross_tenant_access_denied(client, auth_token):
    # Create invoice for different tenant
    other_invoice = Invoice(tenant_id="tenant-2")
    session.add(other_invoice)
    session.commit()

    response = client.get(
        f"/api/v1/invoices/{other_invoice.id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 403

# OpenAPI schema validation
def test_openapi_schema_valid(client):
    response = client.get("/api/v1/openapi.json")
    schema = response.json()
    assert "openapi" in schema
    assert schema["info"]["version"] == "1.0.0"
```

**Non-Compliant Example:**

```python
# ❌ No tests; no OpenAPI schema validation
# No explicit tests
# No schema coverage
```

### Control 7: Logging & Observability

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Structured JSON logging for all security events
- Include correlation_id, user_id, tenant_id, action, result
- Retain logs for ≥90 days
- Real-time alerting on 5xx errors, auth failures

**Compliant Example:**

```python
import logging
import json
from datetime import datetime

logger = logging.getLogger("security")

@app.middleware("http")
async def log_security_events(request: Request, call_next):
    import uuid
    correlation_id = str(uuid.uuid4())

    # Log request
    response = await call_next(request)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "correlation_id": correlation_id,
        "user_id": request.scope.get("user_id"),
        "tenant_id": request.scope.get("tenant_id"),
        "method": request.method,
        "path": request.url.path,
        "status": response.status_code,
        "latency_ms": response.headers.get("X-Process-Time", 0),
        "result": "ALLOW" if response.status_code < 400 else "DENY",
    }

    logger.info(json.dumps(log_entry))
    response.headers["X-Correlation-ID"] = correlation_id
    return response
```

**Non-Compliant Example:**

```python
# ❌ No structured logging; text-only format
logger.info(f"User {user_id} accessed {path}")
```

### Control 8: Zero Trust Networking

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**FastAPI Implementation Pattern:**

- Enforce HTTPS only (SSL/TLS at load balancer or Uvicorn)
- Implement CORS headers (whitelist only trusted origins)
- Validate JWT `aud` (audience) claim
- Optional: mTLS for service-to-service communication

**Compliant Example:**

```python
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# HTTPS enforcement
app.add_middleware(HTTPSRedirectMiddleware)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://app.example.com",
        "https://admin.example.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type", "X-Correlation-ID"],
    max_age=3600,
)

# JWT validation with audience
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = jwt.decode(
        credentials.credentials,
        settings.JWT_PUBLIC_KEY,
        algorithms=["RS256"],
        audience="https://api.example.com",  # Strict audience validation
    )
    return payload
```

**Non-Compliant Example:**

```python
# ❌ CORS wide open; HTTP allowed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dangerous
    allow_methods=["*"],
)
# No HTTPS enforcement
```

## Multi-Tenancy Controls

### Tenant Context Propagation

- User authentication includes tenant ID claim in JWT
- Dependency injection functions extract tenant ID from token
- Tenant ID propagated to all database queries via SQLAlchemy filters

```python
async def get_tenant_id(current_user: dict = Depends(verify_token)) -> str:
    return current_user["tenant_id"]

@app.get("/api/v1/invoices")
async def list_invoices(
    tenant_id: str = Depends(get_tenant_id),
    session: AsyncSession = Depends(get_db)
):
    result = await session.execute(
        select(Invoice).filter(Invoice.tenant_id == tenant_id)
    )
    return result.scalars().all()
```

### Resource Isolation Verification

- Every route enforces `tenant_id == current_user.tenant_id` check
- SQLAlchemy queries use `.filter()` for tenant scoping
- Cross-tenant resource access returns 403 Forbidden

### Audit Trail Isolation

- Logs include tenant_id for all operations
- Tenant-specific log export available only to tenant admins
- Compliance audit trails stored separately per tenant with 90-day minimum retention

## Dependency & Supply Chain Governance

### Dependency Declaration

FastAPI applications declare all dependencies using `poetry` or `pip-tools`:

```toml
[tool.poetry.dependencies]
python = "^3.11"
fastapi = "0.115.0"
uvicorn = "0.30.0"
pydantic = "2.9.0"
pydantic-settings = "2.3.0"
sqlalchemy = "2.0.31"
asyncpg = "0.29.0"
python-jose = "3.3.0"
python-multipart = "0.0.6"
slowapi = "0.1.9"
```

### Vulnerability Scanning

CI/CD pipeline runs:

```bash
pip install bandit pip-audit
bandit -r .
pip-audit --desc
```

- HIGH severity findings block merge
- MEDIUM findings require documented mitigation
- Security patches deployed within 7 days of CVE publication

### Transitive Dependency Management

- Lock files (`poetry.lock`) pinned for reproducibility
- Dependency updates reviewed monthly with 30-day testing window
- Abandoned dependencies replaced immediately

### License Compliance

Approved licenses:

- MIT
- Apache 2.0
- BSD (2-Clause, 3-Clause)
- ISC

Forbidden licenses:

- GPL 2.0 (without SaaS exemption)
- AGPL (no SaaS deployment)

SBOM generated via `cyclonedx-py -o sbom.json`

## Logging & Observability

### Structured Logging Format

All requests logged in JSON:

```json
{
  "timestamp": "2026-02-14T10:00:00Z",
  "correlation_id": "corr-xyz789",
  "user_id": "user-456",
  "tenant_id": "tenant-789",
  "method": "GET",
  "path": "/api/v1/invoices",
  "query_params": { "limit": 10 },
  "status": 200,
  "latency_ms": 45,
  "action": "READ",
  "result": "ALLOW"
}
```

### Retention & Indexing

- Logs retained 90 days minimum
- Indexed by: correlation_id, user_id, tenant_id, status
- Enables: user activity history, error trend analysis, intrusion detection

### Real-Time Alerting

- Alert on 5xx error rate > 5% per minute
- Alert on failed auth > 10/minute from same IP
- Alert on 403 denials > 100/hour (possible permission brute-force)

## CI/CD Integration

### Pre-Merge Gate

```yaml
name: Pre-Merge Security Gate

on:
  pull_request:
    branches:
      - main

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Secrets Detection
        run: |
          pip install detect-secrets
          detect-secrets scan --all-files --force-use-all-plugins

      - name: SAST (Bandit)
        run: |
          pip install bandit
          bandit -r . -f json -o bandit-report.json
          if grep -q '"severity": "HIGH"' bandit-report.json; then exit 1; fi

      - name: Type Checking
        run: |
          pip install mypy types-all
          mypy . --strict

      - name: Unit Tests
        run: |
          pip install pytest pytest-asyncio pytest-cov
          pytest --cov --cov-fail-under=80

      - name: OpenAPI Validation
        run: |
          python -c "from main import app; import json; schema = app.openapi(); assert schema; print('Schema valid')"
```

### Pre-Release Gate

- Integration tests passing (100% pass rate)
- Load test: p99 latency < 500ms for 100 RPS
- API schema stable (no breaking changes)
- Database migrations tested on staging

### Pre-Production Gate

- Dependency audit passes: `pip-audit --desc` with no HIGH findings
- Secrets validation: no credentials in production config
- Canary deployment to 5% traffic; monitor error rates for 15 minutes
- Health endpoint responding within 100ms

## Implementation Risk Notes

### Deployment Risks

**Breaking async changes:**

- Risk: Async context lost between request/response handlers
- Mitigation: Store correlation_id in ContextVar, use proper dependency injection

**Database connection pool exhaustion:**

- Risk: Async concurrency causes connection leak
- Mitigation: Configure pool size correctly, use `sqlalchemy.pool.QueuePool`

**Performance degradation with large responses:**

- Risk: JSON serialization becomes bottleneck
- Mitigation: Implement pagination, use jsonencode caching

### Performance Impact

- Token validation: ~20ms (JWT signature check + cache lookup)
- Pydantic validation: ~5ms (type conversion + field validation)
- Structured logging: ~2ms (JSON serialization per request)
- **Total:** ~27ms overhead acceptable for enterprise SaaS (p99 <500ms)

### Operational Burden

- **Async debugging:** Requires proper correlation ID tracking
- **Rate limit tuning:** Monitor 429 error rates; adjust per-tier
- **Dependency updates:** Monthly security patch cycle

### Testing Gaps

- Hard to test connection pool exhaustion without load testing
- Async error handling edge cases require complex fixtures
- IdP failover scenarios need staging integration

## Control Mapping

| EATGF Control         | ISO 27001:2022 | NIST SSDF | OWASP ASVS | NIST 800-53 | COBIT 2019 |
| --------------------- | -------------- | --------- | ---------- | ----------- | ---------- |
| Input Validation      | A.8.9          | PW.7      | V5         | SI-10       | DSS05.04   |
| Authentication        | A.8.5          | PW.2      | V2         | IA-2        | DSS05.03   |
| Tenant Isolation      | A.8.21         | PW.1      | V1.2       | AC-3        | APO13.01   |
| Logging               | A.8.15         | RV.1      | V15        | AU-2        | MEA01      |
| Dependency Governance | A.8.28         | PW.4      | V14        | SI-7        | BAI09      |
| Authorization         | A.8.35         | PW.3      | V4         | AC-2        | APO13.02   |
| Rate Limiting         | A.8.22         | PW.6      | V5         | SC-7        | DSS05.03   |
| Zero Trust            | A.8.23         | PW.7      | V1.1       | AC-4        | APO13.03   |

## Developer Checklist

Before production deployment:

- [ ] **All endpoints use Pydantic models** (no raw dict payloads)
- [ ] **JWT/OIDC validation enabled** (not sessions)
- [ ] **Tenant context enforced** on all queries
- [ ] **Dependencies locked** in poetry.lock or requirements.lock
- [ ] **pip-audit passes** (no HIGH severity findings)
- [ ] **Rate limiting enabled** (`slowapi` decorators)
- [ ] **CORS restricted** (whitelist only trusted origins)
- [ ] **Structured logging enabled** (JSON format with correlation IDs)
- [ ] **Swagger protected or disabled** (no public schema in production)
- [ ] **No debug mode** (FASTAPI_ENV=production)
- [ ] **Health endpoints protected** or rate-limited
- [ ] **Type checking passes** (mypy --strict)
- [ ] **Unit test coverage ≥80%** (pytest-cov)
- [ ] **Integration tests passing** (multi-tenant scenarios)
- [ ] **Load test** completes p99 < 500ms
- [ ] **Uvicorn workers** ≥2 (no single-worker deployment)

**Deployment blocked if any MANDATORY item fails.**

## Governance Implications

### If Not Implemented

**Injection vulnerabilities:**

- Risk: SQL injection, NoSQL injection via unvalidated input
- Impact: Data breach, RCE, compliance failure
- Audit finding: OWASP ASVS V5 (Input Validation) violation

**Cross-tenant exposure:**

- Risk: Customer A queries Customer B data
- Impact: GDPR/CCPA violations, contract breach
- Audit finding: ISO 27001 A.8.21 violation

**API abuse (DoS):**

- Risk: Malicious users exhaust resources
- Impact: Service outage, reputation damage
- Audit finding: NIST 800-53 SC-7 violation

**Certification audit failures:**

- FastAPI without governance = non-compliant under EATGF
- SOC2 Type II certification blocked
- PCI-DSS development control failure

**Non-conformance consequences:**

- Audit findings escalate to board level
- Customer SLAs violated
- Financial penalties if data breach occurs

## Official References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [ISO/IEC 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security Top 10 (2023)](https://owasp.org/www-project-api-security/)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [COBIT 2019 Governance Framework](https://www.isaca.org/resources/cobit)
- [RFC 6749: OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
- [FastAPI Security Documentation](https://fastapi.tiangolo.com/tutorial/security/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## Version Information

| Field              | Value                           |
| ------------------ | ------------------------------- |
| **Version**        | 1.0                             |
| **Release Date**   | 2026-02-14                      |
| **Change Type**    | Major (First Release)           |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)    |
| **Next Review**    | Q2 2026 (FastAPI 1.0 release)   |
| **Author**         | EATGF Governance Council        |
| **Status**         | Ready for Enterprise Deployment |
