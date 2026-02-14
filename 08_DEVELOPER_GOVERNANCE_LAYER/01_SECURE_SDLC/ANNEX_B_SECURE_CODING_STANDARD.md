# Secure Coding Governance Standard

## Purpose

This document defines the mandatory secure coding requirements within the EATGF Developer Governance Layer.

It establishes enforceable coding rules that reduce exploitable vulnerabilities at source level.
Secure coding under this Annex is not advisory guidance. It is a governance-controlled engineering obligation.

This standard applies to backend services, APIs, web applications, mobile backends, and microservices.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Domain: 01_SECURE_SDLC
Authority: Subordinate to SECURE_SDLC_GOVERNANCE_STANDARD.md
Control Reference: SDLC-SC-02

This Annex operationalizes:

- Secure SDLC Phase: Implementation
- Enforcement: Pre-Merge & Pre-Release Gate
- Severity: MANDATORY for Enterprise & SaaS
- Applicability: Enterprise / SaaS / Startup / Developer

Integrated With:

- ENFORCEMENT_MATRIX.md
- CONTROL_MAPPING_APPENDIX.md
- ANNEX_A_THREAT_MODELING_STANDARD.md

## Governance Principles

- All input is untrusted until validated.

## Technical Implementationn source code.

- Error handling must not expose internal state.
- Logging must be structured and sanitized.
- Cryptography must rely on approved libraries only.

---

## Core Secure Coding Requirements

### 1. Input Validation (MANDATORY)

**Requirement:** All external inputs validated before processing.

All external input must be validated using allow-lists.

Example – FastAPI with Pydantic

```python
from fastapi import FastAPI
from pydantic import BaseModel, constr

app = FastAPI()

class UserInput(BaseModel):
    username: constr(min_length=3, max_length=20, regex="^[a-zA-Z0-9_]+$")
    age: int

@app.post("/users")
def create_user(data: UserInput):
    return {"status": "validated"}
```

No manual string parsing allowed for structured data.

\*\*RequiSQL Injection Protection (MANDATORY)

Raw query string concatenation is prohibited.

Correct Example – SQLAlchemy

```python
from sqlalchemy import select
from models import User

def get_user(session, username):
    stmt = select(User).where(User.username == username)
    return session.execute(stmt).scalar_one_or_none()
```

**Requirement:** All database queries use parameterized statements.

**CWE Mapping:** CWE-89 (SQL Injection)

**Anti-Pattern:**

```python
# WRONG
query = f"SELECT * FROM users WHERE id = {user_id}"
```

**Correct Pattern:**

```python
# Correct - Parameterized query
query = "SELECT * FROM users WHERE id = ?"
result = db.execute(query, (user_id,))
```

### 4. Authentication & Session Management (MANDATORY)

**Requirements:**

- Strong password hashing (bcrypt, Argon2 – minimum 10 rounds)
- Secure session tokens (cryptographically random, 128+ bits)
- Session expiration (maximum 8 hours for sensitive operations)
- Secure cookies (HttpOnly, Secure, SameSite flags)

**Anti-Pattern:**

```python
# WRONG
password_hash = hashlib.sha256(password.encode()).hexdigest()
```

**Correct Pattern:**

```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed = pwd_context.hash(password)
```

### 5. Cryptographic Controls (MANDATORY)

**Requirements:**

- Use platform-provided cryptography libraries only
- Use algorithms certified by NIST (AES-256, SHA-256+)
- Key management via vault, never hardcoded
- Never use deprecated algorithms (MD5, SHA1, DES)

**Approved Algorithms:**

| Use Case             | Algorithms         |
| -------------------- | ------------------ |
| Symmetric Encryption | AES-256 (GCM mode) |
| Hashing              | SHA-256, SHA-3     |
| Password Hashing     | bcrypt, Argon2     |
| Digital Signatures   | ECDSA, RSA-2048+   |

### 6. Error Handling & Logging (MANDATORY)

**Requirements:**

- Never expose system details in error messages to users
- Log full error details internally for debugging
- Mask sensitive data (passwords, tokens, PII) in all logs
- Include context (user ID, timestamp, action) in logs

**Anti-Pattern:**

```python
try:
    result = db.query(...)
except Exception as e:
    return {"error": str(e)}  # Exposes DB schema
```

**Correct Pattern:**

```python
try:
    result = db.query(...)
except Exception as e:
    logger.error(f"Database error: {str(e)}", exc_info=True)
    return {"error": "Internal server error"}  # Generic to client
```

### 7. Deserialization Controls (MANDATORY)

**Requirement:** Never deserialize untrusted data using unsafe methods.

**CWE Mapping:** CWE-502 (Deserialization of Untrusted Data)

**Anti-Pattern:**

```python
# WRONG – Allows arbitrary code execution
import pickle
data = pickle.loads(untrusted_data)
```

**Correct Pattern:**

```python
import json
# Safe – Only JSON data, no code execution
data = json.loads(untrusted_data)
# With validation
from pydantic import BaseModel
validated_data = MyModel(**data)
```

### 8. Security Headers (MANDATORY for Web Applications)

| Header                    | Value                             | Purpose                  |
| ------------------------- | --------------------------------- | ------------------------ |
| Content-Security-Policy   | `default-src 'self'`              | Prevent XSS              |
| X-Frame-Options           | `DENY`                            | Prevent clickjacking     |
| X-Content-Type-Options    | `nosniff`                         | Prevent MIME sniffing    |
| Strict-Transport-Security | `max-age=31536000`                | Enforce HTTPS            |
| Referrer-Policy           | `strict-origin-when-cross-origin` | Control referrer leakage |

## Framework-Specific Patterns

### Python (Pydantic + FastAPI)

```python
from pydantic import BaseModel, EmailStr, validator
from fastapi import FastAPI

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    age: int

    @validator('username')
    def username_valid(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid username')
        return v

    @validator('age')
    def age_valid(cls, v):
        if not (0 < v < 150):
            raise ValueError('Invalid age')
        return v

app = FastAPI()

@app.post("/users")
async def create_user(user: UserCreate):
    # user is guaranteed valid
    pass
```

### JavaScript/Node.js (Express + Joi)

```javascript
const express = require("express");
const Joi = require("joi");

const userSchema = Joi.object({
  email: Joi.string().email().required(),
  username: Joi.string().alphanum().max(255).required(),
  age: Joi.number().integer().min(1).max(150).required(),
});

app.post("/users", (req, res) => {
  const { error, value } = userSchema.validate(req.body);
  if (error) {
    return res.status(400).json({ error: error.details });
  }
  // value is validated
});
```

---

## Control Mapping

| Framework            | Mapping                                |
| -------------------- | -------------------------------------- |
| ISO 27001:2022       | Annex A 8.28 Secure Coding             |
| NIST SSDF SP 800-218 | PW.5 Implement Secure Coding Practices |
| OWASP ASVS v4        | V5 Validation, V4 Access Control       |
| OWASP SAMM           | Implementation → Secure Coding         |
| COBIT 2019           | BAI03 Manage Solutions Build           |
| NIST SP 800-53 Rev.5 | SA-11 Developer Testing                |

## Developer Checklist

Before merge:

- Input validation implemented
- ORM or parameterized queries used
- RBAC enforced per endpoint
- No secrets in repository
- Logs structured and sanitized
- Error handling sanitized
- Approved crypto only
- Dependency versions locked
- Code scanned via SAST
- Code reviewed by peer
- CI gate passed

## Governance Implications

Risk Exposure:
Insecure coding introduces exploitable vulnerabilities.

Operational Cost:
Post-production fixes cost significantly more than pre-merge enforcement.

Audit Impact:
Failure to enforce secure coding may invalidate ISO 27001 secure development compliance.

Cultural Impact:
Secure coding must become engineering baseline, not optional discipline.

## Official References

- NIST SP 800-218 Secure Software Development Framework
- ISO/IEC 27001:2022
- OWASP ASVS v4
- OWASP SAMM v2
- NIST SP 800-53 Rev.5
- COBIT 2019

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Classification: Public Governance Standard
