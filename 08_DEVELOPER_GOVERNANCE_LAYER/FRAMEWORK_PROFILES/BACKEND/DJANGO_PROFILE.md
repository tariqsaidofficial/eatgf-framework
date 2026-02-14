# Django Framework Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Django-based backend systems. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Django applications satisfy Secure SDLC (Layer 01), API Governance (Layer 05), and DevSecOps (Layer 03) requirements.

## Purpose

This document defines the governance conformance model for Django-based backend systems operating under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It translates EATGF Secure SDLC, API Governance, DevSecOps, and Runtime Security standards into enforceable implementation controls for enterprise Django applications.

This profile applies to:

- Enterprise web applications
- Multi-tenant SaaS platforms
- Internal enterprise systems
- API-first backend services

## Architectural Position

**EATGF Layer:**
- Primary: `08_DEVELOPER_GOVERNANCE_LAYER` → `FRAMEWORK_PROFILES` → `BACKEND`
- References: Layer 01 (Secure SDLC), Layer 05 (API Governance), Layer 03 (DevSecOps)

**Scope:**
Backend application layer responsible for:
- HTTP request/response handling
- ORM-based data access
- Authentication and authorization
- Multi-tenancy enforcement
- API exposure
- Session and token management

**Django Classification:**
- REST-capable backend framework
- Policy enforcement boundary
- Data protection control surface
- Application security boundary

**Conformance Obligations:**
- ✅ 01_SECURE_SDLC standards
- ✅ 02_API_GOVERNANCE standards (REST-specific controls)
- ✅ 03_DEVSECOPS standards
- ✅ 04_CLOUD standards (if deployed in SaaS context)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC
Django profiles enforce:
- **Dependency scanning:** `pip-audit`, `bandit` in CI/CD pipeline
- **SAST rules:** Bandit plugin for Django security checks
- **Code review workflow:** PR-based gate with security checklist
- **Test coverage requirement:** Minimum 80% unit + integration test coverage

### Layer 03: DevSecOps Governance
Django profiles reference:
- **Container security:** `docker/Dockerfile` multi-stage builds with non-root user
- **CI/CD pipeline gates:** Pre-merge, pre-release, pre-production stages
- **Secrets management:** HashiCorp Vault integration or AWS Secrets Manager
- **Image scanning:** Trivy/Grype vulnerability scanning in build pipeline

### Layer 05: Domain Frameworks
Django profiles implement API Governance controls:
- **Authentication:** JWT/OIDC (not session-based for APIs)
- **Authorization:** Object-level permission checks
- **Rate Limiting:** Per-IP, per-user tier enforcement
- **OpenAPI/Swagger:** Automated schema generation via `drf-spectacular`
- **Versioning:** URL-based API versioning (`/api/v1/`, `/api/v2/`)

### Layer 04: Cloud Governance (Conditional)
If deployed in cloud infrastructure:
- **HTTPS enforcement:** HSTS headers, secure redirects
- **Environment config:** CloudFormation or Terraform for reproducibility
- **Database encryption:** RDS encryption at rest + TLS in transit
- **IAM scoping:** Service-specific IAM roles for production Django instances

## Governance Principles

### 1. Secure-by-Default Configuration

Production environments must never rely on default settings.

```python
# settings/production.py
DEBUG = False
ALLOWED_HOSTS = ["api.example.com"]
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

**Failure to enforce:** MANDATORY violation

### 2. Tenant Isolation as a First-Class Control

All database queries must be tenant-scoped.

```python
class InvoiceViewSet(ModelViewSet):
    def get_queryset(self):
        return Invoice.objects.filter(
            tenant_id=self.request.user.tenant_id
        )
```

**Cross-tenant leakage:** Classified as critical governance breach

### 3. Authentication Boundary Hardening

Django must not rely on session authentication for APIs.

Enterprise profile requires:
- JWT or OIDC
- Audience validation
- Token expiry enforcement
- Optional mTLS for internal APIs

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
}
```

### 4. Object-Level Authorization Enforcement

```python
from rest_framework.permissions import BasePermission

class IsTenantOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.tenant_id == request.user.tenant_id
```

**Authorization scope:** Must not rely solely on route-level checks

### 5. Secrets Governance

Secrets must not exist in source code or committed `.env` files.

**Acceptable patterns:**
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- GCP Secret Manager

```python
import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
```

**Static hardcoded keys:** MANDATORY violation

### 6. Structured Logging & Auditability

All security-relevant events must be logged in structured JSON format.

```python
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": '{"level":"%(levelname)s","message":"%(message)s","tenant":"%(tenant)s"}'
        }
    },
    "handlers": {
        "security": {
            "class": "logging.StreamHandler",
            "formatter": "json"
        }
    },
    "loggers": {
        "django.security": {
            "handlers": ["security"],
            "level": "INFO",
            "propagate": False,
        }
    }
}
```

**Constraint:** Logs must exclude PII unless legally justified

## Governance Conformance

This section maps the 8 mandatory controls from Layer 05 (API Governance) to Django-specific implementation patterns.

### Control 1: Authentication

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-1-authentication)

**Django Implementation Pattern:**
- Use `rest_framework_simplejwt` or `authlib` for JWT/OIDC
- Validate token signature against IdP public keys (cached)
- Enforce token expiry; refresh tokens rotated server-side
- Reject sessions for API endpoints

**Compliant Example:**
```python
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.user is populated from JWT claims
        return Response({"user": request.user.id})
```

**Non-Compliant Example:**
```python
# ❌ Session authentication for API
class LegacyView(APIView):
    authentication_classes = [SessionAuthentication]  # Vulnerable
    
    def get(self, request):
        return Response({"user": request.user.id})
```

### Control 2: Authorization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-2-authorization)

**Django Implementation Pattern:**
- Define custom permission classes for resource-level checks
- Enforce tenant scoping at query layer
- Use Django `@permission_required` decorators
- Deny by default; explicitly grant scopes

**Compliant Example:**
```python
class IsResourceOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id and \
               obj.tenant_id == request.user.tenant_id

class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsResourceOwner]
    queryset = Document.objects.all()
```

**Non-Compliant Example:**
```python
# ❌ No object-level permission check
class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  # Missing object check
    queryset = Document.objects.all()
```

### Control 3: API Versioning

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-3-versioning)

**Django Implementation Pattern:**
- Use URL-based versioning: `/api/v1/`, `/api/v2/`
- Maintain backward compatibility for 12 months
- Deprecate old versions with HTTP `Sunset` header
- Document breaking changes in migration guide

**Compliant Example:**
```python
# urls.py
urlpatterns = [
    path('api/v1/users/', UsersListV1View.as_view(), name='users-v1'),
    path('api/v2/users/', UsersListV2View.as_view(), name='users-v2'),
]

# views.py
class UsersListV2View(APIView):
    def get(self, request):
        response = Response(data)
        response['Sunset'] = 'Sun, 31 Dec 2025 23:59:59 GMT'
        return response
```

**Non-Compliant Example:**
```python
# ❌ No versioning; breaking changes in production
urlpatterns = [
    path('api/users/', UsersListView.as_view()),  # v1 → v2 breaking change
]
```

### Control 4: Input Validation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-4-input-validation)

**Django Implementation Pattern:**
- Use Django REST Framework serializers with strict validation
- Reject extra fields: `extra = "forbid"` in serializers
- Validate field types and ranges
- Sanitize inputs before database queries

**Compliant Example:**
```python
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']
        extra_kwargs = {
            'email': {'validators': [UniqueValidator(queryset=User.objects.all())]},
        }

    def validate_email(self, value):
        if '@' not in value:
            raise ValidationError("Invalid email")
        return value
```

**Non-Compliant Example:**
```python
# ❌ No validation; accepts arbitrary input
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Exposes internal fields
```

### Control 5: Rate Limiting

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-5-rate-limiting)

**Django Implementation Pattern:**
- Use `django-ratelimit` or `rest-framework-throttle`
- Enforce per-IP, per-user-tier limits
- Return 429 with `Retry-After` header
- Log all rate limit hits for abuse detection

**Compliant Example:**
```python
from rest_framework.throttling import UserRateThrottle

class StandardUserThrottle(UserRateThrottle):
    scope = 'standard'

class PROMiumUserThrottle(UserRateThrottle):
    scope = 'premium'

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'api.throttles.StandardUserThrottle',
        'api.throttles.PROMMiumUserThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'standard': '100/hour',
        'premium': '10000/hour',
    }
}
```

**Non-Compliant Example:**
```python
# ❌ No rate limiting; open to DoS
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': []  # Disabled
}
```

### Control 6: Testing & Documentation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-6-testing)

**Django Implementation Pattern:**
- Unit tests ≥80% code coverage
- Integration tests for all API endpoints
- Auto-generate OpenAPI schema with `drf-spectacular`
- Document all breaking changes in CHANGELOG.md

**Compliant Example:**
```python
# tests/test_users_api.py
class UsersAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            tenant_id='tenant-1'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_users_filtered_by_tenant(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            all(u['tenant_id'] == 'tenant-1' for u in response.data)
        )

    def test_cross_tenant_access_denied(self):
        other_user = User.objects.create_user(
            email='other@example.com',
            tenant_id='tenant-2'
        )
        response = self.client.get(f'/api/v1/users/{other_user.id}/')
        self.assertEqual(response.status_code, 403)
```

**Non-Compliant Example:**
```python
# ❌ No tests; no documentation
# No test coverage
# No OpenAPI schema
```

### Control 7: Logging & Observability

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-7-logging)

**Django Implementation Pattern:**
- Structured JSON logging for all security events
- Include correlation_id, user_id, tenant_id, action, result
- Retain logs for ≥90 days
- Real-time alerting on 5xx errors, auth failures

**Compliant Example:**
```python
import logging
import json
from django.http import HttpResponse
from django.utils.decorators import decorator_from_middleware_with_args

logger = logging.getLogger('django.security')

class SecurityLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'correlation_id': request.META.get('HTTP_X_CORRELATION_ID'),
            'user_id': request.user.id if request.user.is_authenticated else None,
            'tenant_id': request.user.tenant_id if request.user.is_authenticated else None,
            'method': request.method,
            'path': request.path,
            'status': response.status_code,
            'result': 'ALLOW' if response.status_code < 400 else 'DENY',
        }
        
        logger.info(json.dumps(log_entry))
        return response
```

**Non-Compliant Example:**
```python
# ❌ No structured logging; text-only format
logger.info(f"User {request.user} accessed {request.path}")
```

### Control 8: Zero Trust Networking

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-8-zero-trust)

**Django Implementation Pattern:**
- Require mTLS for inter-service communication
- Implement CORS headers (whitelist only trusted origins)
- Force HTTPS; disable HTTP
- Validate JWT `aud` (audience) claim

**Compliant Example:**
```python
# settings/production.py
CORS_ALLOWED_ORIGINS = [
    "https://app.example.com",
    "https://admin.example.com",
]
CORS_ALLOW_CREDENTIALS = True
SECURE_SSL_REDIRECT = True

# JWT validation
SIMPLE_JWT = {
    'ALGORITHM': 'RS256',
    'VERIFY_EXPIRATION': True,
    'VERIFY_AUD': True,  # Audience validation
    '__JWT_AUDIENCE__': 'https://api.example.com',
}
```

**Non-Compliant Example:**
```python
# ❌ CORS wide open; HTTP allowed
CORS_ALLOWED_ORIGINS = ["*"]
SECURE_SSL_REDIRECT = False
```

## Multi-Tenancy Controls

### Tenant Context Propagation

- User authentication includes tenant ID claim
- Middleware extracts tenant ID from JWT claim or request header
- Tenant ID propagated to all ORM queries

```python
class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.tenant_id = request.user.tenant_id
        return self.get_response(request)
```

### Resource Isolation Verification

- Every ViewSet filter enforces `tenant_id == request.user.tenant_id`
- ORM queries use `.select_related()` and `.prefetch_related()` for tenant context
- Cross-tenant resource access returns 403 Forbidden

```python
class BaseTenanntViewSet(ModelViewSet):
    def get_queryset(self):
        return self.queryset.filter(tenant_id=self.request.tenant_id)
```

### Audit Trail Isolation

- Logs include tenant_id for all operations
- Tenant-specific log export available only to tenant admins
- Compliance audit trails stored separately per tenant with 90-day minimum retention

## Dependency & Supply Chain Governance

### Dependency Declaration

Django APIs declare all dependencies in `requirements.txt` or `pyproject.toml`:

```
Django==5.0.7
djangorestframework==3.15.1
djangorestframework-simplejwt==5.3.1
psycopg2-binary==2.9.9
django-cors-headers==4.3.1
python-decouple==3.8
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

- Lock files (`requirements.lock`) pinned for reproducibility
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

SBOM generated via `pip install cyclonedx-bom && cyclonedx-bom -o sbom.json`

## Logging & Observability

### Structured Logging Format

All requests logged in JSON:

```json
{
  "timestamp": "2026-02-14T10:00:00Z",
  "correlation_id": "corr-abc123",
  "user_id": "user-456",
  "tenant_id": "tenant-789",
  "method": "GET",
  "path": "/api/v1/invoices/",
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
- Alert on 403 denials > 100/hour (possible brute-force of permissions)

## CI/CD Integration

### Pre-Merge Gate

```yaml
name: Pre-Merge Security Gate

on:
  pull_request:
    branches:
      - main

jobs:
  security-checks:
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
          pip install mypy django-stubs
          mypy .

      - name: Unit Tests
        run: |
          pip install pytest pytest-django pytest-cov
          pytest --cov --cov-fail-under=80

      - name: OpenAPI Validation
        run: |
          pip install drf-spectacular
          python manage.py spectacular --no-serve --file schema.yaml
```

### Pre-Release Gate

- Integration tests passing (100% pass rate)
- Load test: p99 latency < 500ms for 100 RPS
- API schema stable (no breaking changes from v1.0)
- Database migrations tested on staging

### Pre-Production Gate

- Dependency audit passes: `pip-audit --desc` with no HIGH findings
- Secrets in production config validated (not in code)
- Canary deployment to 5% traffic; monitor error rates for 15 minutes
- Feature flags disabled for untested features

## Implementation Risk Notes

### Deployment Risks

**Breaking API changes:**
- Risk: Clients using old endpoints fail silently
- Mitigation: Semantic versioning (v1 → v2 separate endpoints), 6+ month deprecation window

**Database migration failures:**
- Risk: Locks production database during upgrade
- Mitigation: Test migrations on production-like staging; have automated rollback

**Token validation latency:**
- Risk: IdP becomes bottleneck; fails open (accepts invalid tokens)
- Mitigation: Cache public keys; implement timeout with fallback

### Performance Impact

- Authentication adds ~20ms per request (token validation + cache lookup)
- Authorization checks add ~5ms per request (permission check)
- Structured logging adds ~2ms per request (JSON serialization)
- **Total:** ~27ms overhead on typical request
- Acceptable for enterprise SaaS (p99 latency <500ms achievable)

### Operational Burden

- **RBAC/ABAC maintenance:** Quarterly governance review of permissions
- **Rate limit tuning:** Monitor 429 error rates; adjust per-tier if complaints spike
- **Dependency updates:** Monthly security patch cycle with 30-day testing

### Testing Gaps

- Hard to test cross-tenant isolation without multiple staging tenants
- Rate limit exhaustion testing requires load testing infrastructure
- IdP failover scenarios require staging IdP integration

## Control Mapping

| EATGF Control | ISO 27001:2022 | NIST SSDF | OWASP ASVS | NIST 800-53 | COBIT 2019 |
|---|---|---|---|---|---|
| Secure Config | A.8.9 | PW.8 | V14 | CM-6 | DSS05.04 |
| Authentication | A.8.5 | PW.2 | V2 | IA-2 | DSS05.03 |
| Tenant Isolation | A.8.21 | PW.1 | V1.2 | AC-3 | APO13.01 |
| Logging | A.8.15 | RV.1 | V15 | AU-2 | MEA01 |
| Dependency Governance | A.8.28 | PW.4 | V14 | SI-7 | BAI09 |
| Authorization | A.8.35 | PW.3 | V4 | AC-2 | APO13.02 |
| Rate Limiting | A.8.22 | PW.6 | V5 | SC-7 | DSS05.03 |
| Zero Trust | A.8.23 | PW.7 | V1.1 | AC-4 | APO13.03 |

## Developer Checklist

Before production deployment:

- [ ] **DEBUG=False** in production settings
- [ ] **SECRET_KEY** sourced from vault (not code)
- [ ] **ALLOWED_HOSTS** explicitly defined (not `*`)
- [ ] **HTTPS enforced** (SECURE_SSL_REDIRECT=True)
- [ ] **JWT/OIDC enabled** (not session auth for APIs)
- [ ] **Object-level permissions** enforced on all ViewSets
- [ ] **Tenant scoping** implemented on all queries
- [ ] **Dependencies pinned** in requirements.txt
- [ ] **pip-audit passes** (no HIGH severity findings)
- [ ] **Structured logging** enabled (JSON format)
- [ ] **CSP headers** configured (Content-Security-Policy)
- [ ] **manage.py check --deploy** passes (0 errors)
- [ ] **Unit test coverage ≥80%** (pytest-cov report)
- [ ] **Integration tests passing** for multi-tenant scenarios
- [ ] **Load test** completes with p99 < 500ms
- [ ] **Database migrations** tested on staging replica

**Deployment blocked if any MANDATORY item fails.**

## Governance Implications

### If Not Implemented

**Cross-tenant data exposure:**
- Risk: Customer A queries Customer B data
- Impact: GDPR/CCPA violations, contract breach, reputation damage
- Audit finding: ISO 27001 A.8.21 (Access control) violation

**Token misuse:**
- Risk: Stale tokens accepted; compromised credentials reused
- Impact: Account takeover, fraud, compliance failure
- Audit finding: NIST 800-53 IA-2 (Authentication) violation

**Supply chain compromise:**
- Risk: Vulnerable dependency deployed to production
- Impact: RCE, data breach, ransomware
- Audit finding: NIST SSDF PW.4 (Dependency management) violation

**PII exposure in logs:**
- Risk: Customer data in plain-text logs
- Impact: GDPR Article 32 violation, SOC2 Type I failure
- Audit finding: ISO 27001 A.8.15 (Logging) violation

**Audit failure:**
- Django without governance = non-compliant under EATGF
- SOC2 Type II certification blocked
- PCI-DSS development control failure (missing code review, testing, logging)

## Official References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [ISO/IEC 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security Top 10 (2023)](https://owasp.org/www-project-api-security/)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [COBIT 2019 Governance Framework](https://www.isaca.org/resources/cobit)
- [RFC 6749: OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)

## Version Information

| Field | Value |
|---|---|
| **Version** | 1.0 |
| **Release Date** | 2026-02-14 |
| **Change Type** | Major (First Release) |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete) |
| **Next Review** | Q2 2026 (Django 6.0 LTS release) |
| **Author** | EATGF Governance Council |
| **Status** | Ready for Enterprise Deployment |
