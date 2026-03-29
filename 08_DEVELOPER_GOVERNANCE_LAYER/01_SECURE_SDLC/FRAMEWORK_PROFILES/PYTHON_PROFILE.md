# Python Secure SDLC Framework Profile

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Framework:** Python (3.8+)
**Applicable To:** Django, FastAPI, Flask, Starlette, and all Python web applications
**Reference:** SECURE_SDLC_GOVERNANCE_STANDARD.md
**Framework Profiles Directory:** 01_SECURE_SDLC/FRAMEWORK_PROFILES/

---

## Authority Notice

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 01_SECURE_SDLC  
**Governance Scope:** Implementation Standard  
**Control Authority:** Defines controls for Python development lifecycle

---

## Governance Principles

- **Single Source of Truth:** Python security requirements defined in SECURE_SDLC_GOVERNANCE_STANDARD.md
- **Developer-Operational Alignment:** Developers implement controls, operations audit compliance
- **Security-by-Design:** All Python projects must accept security review before code merge
- **Audit Traceability:** GitHub Actions logs all SAST/DAST/dependency scan results
- **Control-Centric Architecture:** Each Python application must satisfy 8 control families

---

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF v1.1 | OWASP | COBIT 2019 |
|---|---|---|---|---|
| Python Secure Coding | A.14.1, A.14.2 | PO3.1, PO3.2 | Top 10 | BAI01 |
| Dependency Management | A.8.8 | PO3.3 | A06:2021 | BAI02 |
| SAST/Linting | A.12.6.1 | PO5.2 | ASPM | BAI04 |
| Secrets Management | A.8.23 | PS2.3 | A02:2021 | DSS05 |
| CI/CD Pipeline | A.14.2.1 | PO5.1 | A09:2021 | BAI01 |
| Vulnerability Response | A.8.16 | RV.1 | A06:2021 | DSS07 |
| Supply Chain | A.8.28 | S1.2 | A08:2021 | BAI03 |
| Code Review | A.14.2.5 | PW5.1 | N/A | BAI06 |

---

## Developer Checklist

- [ ] All Python code commits must pass Black formatter check (line-length=100)
- [ ] Security linting enabled (bandit, semgrep) - zero HIGH/CRITICAL findings before merge
- [ ] Dependency scanning (safety, pip-audit) - no known vulnerabilities
- [ ] SAST enabled in CI/CD (SonarQube minimum) - coverage >80%
- [ ] Secrets detection active (detect-secrets, git-secrets) - no credentials committed
- [ ] Type checking (mypy strict mode) on all public APIs
- [ ] Unit tests >70% coverage with security test cases
- [ ] Code review completed by peer + security team for P1/P2 features
- [ ] OWASP Top 10 checklist completed before production deployment
- [ ] Changelog updated with security-relevant modifications

---

## Purpose

This profile operationalizes Secure SDLC requirements specifically for **Python** development environments and web frameworks.

It provides:

- Python-specific secure coding guidelines
- Recommended security tools and configurations
- Production-grade CI/CD pipeline examples
- Common misconfigurations and remediation
- Dependency and supply chain security practices

---

## Architectural Position

**Applicability:** All Python applications (web, API, microservices, CI/CD automation)

**Profile Classification:** Developer Governance Framework Profile

**Enforcement Level:**

- **Enterprise:** MANDATORY
- **SaaS:** MANDATORY
- **Startup:** RECOMMENDED
- **Individual Developer:** RECOMMENDED

---

## 1. Security Requirements Integration (Python)

### Required Controls

**Severity: MANDATORY**

Python-specific security requirements must be captured in backlog:

```yaml
Labels:
  - security-requirement
  - framework:python

Title: "Validate user input on all API endpoints – Python validation"

Description: |
  Implement Pydantic BaseModel validation for all request parameters.
  No raw request.args or request.json access in route handlers.

Acceptance Criteria:
  - All FastAPI endpoints use Pydantic models
  - All request data validated before processing
  - Type checking enforced (mypy --strict)
  - Integration tests verify validation boundaries

Security Acceptance:
  - OWASP ASVS V5.1.1 (input validation)
  - CWE-20 (improper input validation)
  - PEP 20 (explicit is better than implicit)
```

### Tools for Requirements Tracking

- **Jira / Linear:** Security labels and custom fields
- **GitHub Projects:** Security columns in board view
- **Repository:** SECURITY_REQUIREMENTS.md checklist

---

## 2. Design & Threat Modeling (Python)

### Architecture Diagram Template

```
┌─────────────────────────────────────────────┐
│         Client (Browser / Mobile)           │
└──────────────┬──────────────────────────────┘
               │ HTTPS/TLS 1.3
               ▼
┌─────────────────────────────────────────────┐
│  API Gateway / Load Balancer                │
│  - Rate limiting                            │
│  - Request validation                       │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴───────┐
       ▼               ▼
  ┌─────────┐    ┌──────────────┐
  │ FastAPI │    │ Middleware   │
  │ Service │    │ (Auth/CORS)  │
  └─────┬───┘    └──────────────┘
        │
    ┌───┴────────┬───────────┬──────────────┐
    ▼            ▼           ▼              ▼
┌────────┐ ┌──────────┐ ┌────────┐ ┌──────────────┐
│ SQLAlch│ │  Redis   │ │ Celery │ │ External API │
│ (RDS)  │ │ (Cache)  │ │ (Jobs) │ │ (HTTPS Only) │
└────────┘ └──────────┘ └────────┘ └──────────────┘

Trust Boundaries:
[Client] ← → [API Gateway] ← → [Service] ← → [Data Layer]
```

### Threat Model Template (Python)

```
Threat Model – FastAPI User Authentication Service

High-Risk Components:
1. Password hashing (bcrypt usage)
2. JWT token generation and validation
3. Database connection with credentials
4. External OAuth provider integration

Threats:
- SQL injection via ORM misuse
- Authentication bypass via JWT manipulation
- Plaintext password logging
- Database credentials in environment

Mitigations:
- Use SQLAlchemy ORM with parameterized queries
- Validate JWT signature and expiration
- Never log passwords; use structured logging
- Vault-managed database credentials
```

---

## 3. Secure Coding Practices (Python)

### Anti-Pattern 1: SQL Injection

```python
# ✗ WRONG: String concatenation (vulnerable)
user_id = request.query_params.get("id")
query = f"SELECT * FROM users WHERE id = {user_id}"
result = db.execute(query)

# ✓ CORRECT: SQLAlchemy ORM (parameterized)
from sqlalchemy import select, Table, Column, Integer, String

users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

query = select(users_table).where(users_table.c.id == user_id)
result = db.execute(query)

# ✓ CORRECT: Using Pydantic + async
from fastapi import FastAPI
from sqlalchemy import select

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # User_id is validated as int by FastAPI
    query = select(User).where(User.id == user_id)
    user = await db.execute(query)
    return user
```

### Anti-Pattern 2: Hard-Coded Secrets

```python
# ✗ WRONG: Secrets in code
DATABASE_URL = "postgresql://user:password123@localhost/mydb"
SECRET_KEY = "super-secret-key-12345"
API_KEY = "sk_test_1234567890"

# ✓ CORRECT: Environment variables with Pydantic
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = os.environ.get("DATABASE_URL")
    secret_key: str = os.environ.get("SECRET_KEY")
    api_key: str = os.environ.get("API_KEY")

    class Config:
        env_file = ".env.local"  # Never commit .env files

# Validate at startup
settings = Settings()
if not settings.database_url:
    raise ValueError("DATABASE_URL environment variable not set")

# ✓ CORRECT: Using Vault client
from hvac import Client as VaultClient

vault = VaultClient(url="https://vault.internal:8200")
secrets = vault.secrets.kv.v2.read_secret_version(path="prod/database")
db_url = secrets['data']['data']['url']
```

### Anti-Pattern 3: Unvalidated Input

```python
# ✗ WRONG: No input validation
from fastapi import FastAPI
from typing import Optional

@app.post("/users/")
async def create_user(email: Optional[str], age: Optional[int]):
    # Email could be anything, age could be -100
    user = User(email=email, age=age)
    db.add(user)
    return user

# ✓ CORRECT: Pydantic validation
from pydantic import BaseModel, EmailStr, ValidationError, field_validator
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr  # Built-in email validation
    age: int
    name: str = None

    @field_validator('age')
    @classmethod
    def age_must_be_positive(cls, v):
        if v < 0 or v > 150:
            raise ValueError('Age must be between 0 and 150')
        return v

    @field_validator('name')
    @classmethod
    def name_length(cls, v):
        if v and len(v) > 255:
            raise ValueError('Name too long')
        return v

@app.post("/users/")
async def create_user(user_data: UserCreate):
    # user_data is guaranteed to be valid
    user = User(**user_data.dict())
    db.add(user)
    return user
```

### Anti-Pattern 4: Information Disclosure via Exceptions

```python
# ✗ WRONG: Returning raw exception details (exposes DB structure)
from fastapi import FastAPI

@app.get("/data/{item_id}")
async def get_data(item_id: int):
    try:
        result = db.query(Data).filter(Data.id == item_id).first()
        return result
    except Exception as e:
        return {"error": str(e)}  # Leaks implementation details

# ✓ CORRECT: Generic error response with logging
import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)

@app.get("/data/{item_id}")
async def get_data(item_id: int):
    try:
        result = db.query(Data).filter(Data.id == item_id).first()
        if not result:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    except Exception as e:
        # Log full details internally
        logger.error(f"Database error: {str(e)}", exc_info=True)
        # Return generic error to client
        raise HTTPException(status_code=500, detail="Internal server error")
```

### Anti-Pattern 5: Insecure Cryptography

```python
# ✗ WRONG: Using hashlib for passwords
import hashlib

password_hash = hashlib.sha256(password.encode()).hexdigest()

# ✗ WRONG: Using simple base64 encoding for secrets
import base64
encoded = base64.b64encode(api_key.encode())

# ✓ CORRECT: Using bcrypt for passwords
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed_password = pwd_context.hash(password)
is_valid = pwd_context.verify(password, hashed_password)

# ✓ CORRECT: Using cryptography for encryption
from cryptography.fernet import Fernet

key = Fernet.generate_key()  # Store in vault
cipher = Fernet(key)
encrypted = cipher.encrypt(secret_data.encode())
decrypted = cipher.decrypt(encrypted).decode()
```

---

## 4. Code Review Checklist (Python)

Security reviewers must verify:

- [ ] All inputs validated using Pydantic (web) or similar
- [ ] No hardcoded secrets (API keys, database URLs, tokens)
- [ ] SQLAlchemy ORM used; raw SQL queries approved by security
- [ ] No SQL query construction via f-strings or string concatenation
- [ ] Exception handling doesn't leak internal details
- [ ] Logging doesn't capture sensitive data (passwords, tokens, PII)
- [ ] External API calls use HTTPS only
- [ ] Database connections use SSL/TLS
- [ ] Authentication uses strong algorithms (bcrypt, Argon2)
- [ ] CORS configured correctly (no `allow_origin="*"` in production)
- [ ] Rate limiting configured on public endpoints
- [ ] No debug mode in production
- [ ] Dependency versions pinned (not `>=`)

---

## 5. Dependency & Supply Chain Security (Python)

### Dependency Management Tools

| Tool              | Purpose                          | Command                               |
| ----------------- | -------------------------------- | ------------------------------------- |
| **pip-audit**     | Find vulnerable dependencies     | `pip-audit --desc`                    |
| **safety**        | Safety DB vulnerability scanning | `safety check`                        |
| **cyclonedx-bom** | Generate SBOM                    | `cyclonedx-bom -o sbom.xml`           |
| **bandit**        | Find common security issues      | `bandit -r . --severity-level medium` |
| **pip-compile**   | Lock dependency versions         | `pip-compile -o requirements.txt`     |

### Secure Dependency Workflow

```bash
#!/bin/bash
# secure-dependencies.sh

# 1. Audit for known vulnerabilities
echo "Auditing dependencies..."
pip-audit --desc --exit-code 1

# 2. Generate SBOM
echo "Generating SBOM..."
cyclonedx-bom -o sbom.xml

# 3. Lock versions
echo "Locking versions..."
pip-compile --generate-hashes requirements.in

# 4. Create reproducible build
pip install --require-hashes -r requirements.txt
```

### requirements.txt Best Practices

```
# ✓ CORRECT: Pinned versions with hashes
Django==4.2.0 \
    --hash=sha256:abc123...
djangorestframework==3.14.0 \
    --hash=sha256:def456...
psycopg2-binary==2.9.6 \
    --hash=sha256:ghi789...

# ✓ CORRECT: Transitive dependencies resolved
# (Use pip-compile to generate from requirements.in)

# ✗ WRONG: Unpinned versions
Django>=4.0
djangorestframework

# ✗ WRONG: Comments with sensitive info
# Database password: postgresql://user:password@host/db
```

---

## 6. CI/CD Pipeline (Python)

### GitHub Actions Secure Pipeline

```yaml
name: Python Secure SDLC Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  security-checks:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # Type checking
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install mypy bandit pip-audit cyclonedx-bom

      # Type checking (mypy)
      - name: Run mypy (type checking)
        run: mypy . --strict --ignore-missing-imports
        continue-on-error: false

      # SAST: Bandit
      - name: Run Bandit (SAST)
        run: |
          bandit -r . -f json -o bandit-report.json
          bandit -r . -f txt -o bandit-report.txt

      # Upload SAST results
      - name: Upload Bandit results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: bandit-report.json
        if: always()

      # SCA: Dependency vulnerability scanning
      - name: Audit dependencies
        run: |
          pip-audit --desc --output text > pip-audit-report.txt
          pip-audit --exit-code 1
        continue-on-error: false

      # Secrets detection
      - name: Detect secrets
        run: |
          pip install truffleHog3
          truffleHog filesystem . --json --fail > /dev/null
        continue-on-error: true

      # SBOM generation
      - name: Generate SBOM
        run: cyclonedx-bom -o sbom.xml

      # Upload artifacts
      - name: Upload security reports
        uses: actions/upload-artifact@v3
        with:
          name: security-reports
          path: |
            bandit-report.txt
            bandit-report.json
            pip-audit-report.txt
            sbom.xml

      # Build and unit tests
      - name: Run unit tests
        run: pytest --cov=. --cov-report=xml

      # Upload coverage
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml

  deployment-gate:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    needs: security-checks

    steps:
      - uses: actions/checkout@v4

      - name: Security gates passed
        run: echo "All security checks passed. Ready for deployment"

      - name: Create release
        run: |
          VERSION=$(git describe --tags --always)
          echo "Release: $VERSION"
```

---

## 7. Secrets Management (Python)

### Environment Variable Pattern (Development)

```bash
# .env.local (NEVER commit to Git)
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
REDIS_URL="redis://localhost:6379"
SECRET_KEY="dev-key-only-12345"
JWT_SECRET="dev-jwt-secret"

# .gitignore
.env
.env.local
*.key
*.pem
```

### Vault Integration (Production)

```python
# vault_client.py
import hvac
import os

class VaultSecretsManager:
    def __init__(self):
        self.client = hvac.Client(
            url=os.environ["VAULT_ADDR"],
            token=os.environ["VAULT_TOKEN"]
        )

    def get_db_credentials(self):
        """Fetch database credentials from Vault"""
        response = self.client.secrets.kv.v2.read_secret_version(
            path="prod/database"
        )
        return response['data']['data']

    def get_api_keys(self):
        """Fetch API keys from Vault"""
        response = self.client.secrets.kv.v2.read_secret_version(
            path="prod/external-apis"
        )
        return response['data']['data']

# Usage in FastAPI startup
from fastapi import FastAPI

app = FastAPI()

vault = VaultSecretsManager()

@app.on_event("startup")
async def startup():
    db_creds = vault.get_db_credentials()
    os.environ["DATABASE_URL"] = db_creds["url"]
```

---

## 8. Security Logging (Python)

### Structured Logging Pattern

```python
# logging_config.py
import json
import logging
from logging import LogRecord
from datetime import datetime

class SecurityLogFormatter(logging.Formatter):
    """Format security events as structured JSON"""

    def format(self, record: LogRecord) -> str:
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "event_type": getattr(record, "event_type", "unknown"),
            "user_id": getattr(record, "user_id", None),
            "action": getattr(record, "action", None),
            "result": getattr(record, "result", None),
            "source_ip": getattr(record, "source_ip", None),
            "details": getattr(record, "details", {}),
        }
        return json.dumps(event)

# Usage
import logging

logger = logging.getLogger("security")
handler = logging.StreamHandler()
handler.setFormatter(SecurityLogFormatter())
logger.addHandler(handler)

def log_authentication_attempt(user_id, result, source_ip):
    logger.warning(
        "Authentication attempt",
        extra={
            "event_type": "authentication",
            "user_id": user_id,
            "action": "login",
            "result": result,
            "source_ip": source_ip,
        }
    )

# Output:
# {"timestamp": "2026-02-14T...", "event_type": "authentication", ...}
```

---

## 9. Runtime Hardening (Python)

### ASGI Server Security

```python
# main.py – FastAPI with Uvicorn security settings
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI(
    title="Secure API",
    docs_url=None if os.environ["ENVIRONMENT"] == "production" else "/docs",
    redoc_url=None if os.environ["ENVIRONMENT"] == "production" else "/redoc",
)

# Trust only specific hosts
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["api.example.com", "localhost"]
)

# CORS: Restrict origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.example.com"],  # Specific origin, not "*"
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=600,
)

# Run with Uvicorn
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        ssl_keyfile="/etc/certs/key.pem" if os.environ["ENVIRONMENT"] == "production" else None,
        ssl_certfile="/etc/certs/cert.pem" if os.environ["ENVIRONMENT"] == "production" else None,
        log_level="info",
    )
```

---

## 10. Common Misconfigurations

| Misconfiguration              | Risk                   | Fix                                          |
| ----------------------------- | ---------------------- | -------------------------------------------- |
| `debug=True` in production    | Information disclosure | Set `debug=False` in prod settings           |
| `ALLOWED_HOSTS=["*"]`         | CSRF vulnerability     | Use specific domains                         |
| `CORS allow_origin="*"`       | Credential theft       | Use specific origins                         |
| `SECRET_KEY` in code          | Credential compromise  | Use environment variable                     |
| Plaintext database in URI     | Credential exposure    | Use vault or env var                         |
| `session.cookie_secure=False` | Session hijacking      | Set to `True` in production                  |
| Unvalidated file uploads      | RCE, DoS               | Validate file type/size                      |
| SQL ORM queries in loops      | N+1 query performance  | Use `select_related()`, `prefetch_related()` |

---

## 11. Django-Specific Security

### Django Security Middleware

```python
# settings.py – Django security hardening

# Force HTTPS
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# HSTS (Strict-Transport-Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# XSS Protection
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Content Security Policy
SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
    "script-src": ("'self'", "cdn.example.com"),
    "style-src": ("'self'", "'unsafe-inline'"),
    "img-src": ("'self'", "data:", "https:"),
}

# CSRF token in forms
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

# Session security
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Strict"

# Allowed hosts (production)
ALLOWED_HOSTS = ["api.example.com"]

# Debug mode
DEBUG = False
```

---

## Framework Profile Checklist

For Python projects, confirm:

- [ ] All external inputs validated with Pydantic or similar
- [ ] No hardcoded secrets (use environment variables or vault)
- [ ] SQLAlchemy ORM used; no raw SQL concatenation
- [ ] Parameterized queries for all database access
- [ ] Exception handling doesn't leak internal details
- [ ] Logging configured; doesn't capture sensitive data
- [ ] CORS configured for production (specific origins)
- [ ] HTTPS enforced in production
- [ ] Dependencies audited and locked with hashes
- [ ] SAST (Bandit) and SCA (pip-audit) in CI/CD
- [ ] Pre-commit hooks for secret detection
- [ ] Secrets managed via vault or secure env vars
- [ ] Rate limiting configured on public endpoints
- [ ] Debug mode disabled in production

---

## Official References

**Python Official Documentation:**
- Python Security Documentation: https://docs.python.org/3/library/security_warnings.html
- Virtual Environments: https://docs.python.org/3/tutorial/venv.html

**Framework-Specific Security Guides:**
- Django Security: https://docs.djangoproject.com/en/stable/topics/security/
- FastAPI Security: https://fastapi.tiangolo.com/tutorial/security/
- Flask Best Practices: https://flask.palletsprojects.com/en/latest/security/

**Dependency Management:**
- pip-audit: https://github.com/pypa/pip-audit
- Safety: https://safetycli.com/
- Poetry Lock Files: https://python-poetry.org/docs/dependency-specification/

**SAST & Linting Tools:**
- Bandit (Security Linting): https://bandit.readthedocs.io/
- Semgrep (SAST): https://semgrep.dev/
- Black (Code Formatting): https://github.com/psf/black

**Secrets Management:**
- Python-dotenv: https://github.com/theskumar/python-dotenv
- Hashicorp Vault: https://www.vaultproject.io/docs/auth/jwt
- AWS Secrets Manager: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html

**Authoritative Standards:**
- OWASP Top 10 (A02:2021 Cryptographic Failures): https://owasp.org/Top10/
- OWASP ASVS (Application Security Verification Standard): https://owasp.org/www-project-application-security-verification-standard/
- NIST SP 800-53 (Security Controls): https://csrc.nist.gov/publications/detail/sp/800-53/rev-5
- ISO 27001:2022 Compliance: https://www.iso.org/standard/27001

---

## Version History

| Version | Date       | Change Type | Description                                                                                      |
| ------- | ---------- | ----------- | ------------------------------------------------------------------------------------------------ |
| 1.0     | 2026-02-14 | Major       | Initial Python Framework Profile with SAST, SCA, secure coding patterns, Django/FastAPI guidance |
