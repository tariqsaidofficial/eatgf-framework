# API Authentication Governance Standard

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Purpose

Defines mandatory authentication mechanisms for API endpoints.

Ensures all APIs verify caller identity before granting access.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Subordinate to API_GOVERNANCE_STANDARD.md
Control Reference: SDLC-AUTH-01

## Governance Principles

- Authentication mandatory for all production APIs
- OAuth 2.1 preferred over custom implementations
- OpenID Connect required for user identity
- mTLS required for service-to-service
- Public APIs must provide API key mechanism
- Token expiration mandatory (max 1 hour for sessions)
- No API credential hardcoding permitted

## Technical Implementation

### 1. OAuth 2.1 (Public & SaaS APIs) (MANDATORY)

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id
```

### 2. OpenID Connect (User identity) (MANDATORY for SaaS)

```yaml
# OIDC Configuration
issuer: https://auth.example.com
client_id: api-client-123
client_secret: (from vault)
scopes:
  - openid
  - profile
  - email
redirect_uri: https://api.example.com/callback
```

### 3. mTLS (Service-to-Service) (MANDATORY for internal APIs)

```nginx
# NGINX mTLS configuration
server {
    listen 443 ssl;
    server_name internal-api.example.com;

    ssl_certificate /etc/ssl/certs/server.crt;
    ssl_certificate_key /etc/ssl/private/server.key;
    ssl_client_certificate /etc/ssl/certs/ca.crt;
    ssl_verify_client required;
}
```

### 4. API Keys (Legacy/Public APIs) (CONDITIONAL)

```python
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return x_api_key
```

### 5. JWT Validation (MANDATORY)

```python
import jwt
from cryptography.jwk import RSAKey
from cryptography.hazmat.backends import default_backend

PUBLIC_KEY = RSAKey.from_json(JWKS_ENDPOINT)

def verify_jwt(token: str):
    try:
        payload = jwt.decode(
            token,
            PUBLIC_KEY,
            algorithms=["RS256", "ES256"]  # Only modern algorithms
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
```

## Token Lifecycle

| Stage         | Duration         | Action                         |
| ------------- | ---------------- | ------------------------------ |
| Issued        | T=0              | Token generated with exp claim |
| Valid         | T < exp          | Token accepted for requests    |
| Expiring Soon | 5 min before exp | Refresh token advised          |
| Expired       | T >= exp         | Request rejected, 401 response |
| Revoked       | On demand        | Token blacklisted immediately  |

## Control Mapping

| Framework        | Reference                    |
| ---------------- | ---------------------------- |
| ISO 27001:2022   | A.8.20 (Authentication)      |
| NIST SSDF        | PS.2 (Protect secrets)       |
| OWASP API Top 10 | API2 (Broken Authentication) |
| NIST 800-53      | IA-2, IA-5                   |

## Developer Checklist

- Authentication mechanism selected (OAuth2/OIDC/mTLS/API key)
- Token validation implemented
- Expiration enforced
- Secrets masked in logs
- HTTPS/TLS required
- Public key rotation plan defined
- Token revocation procedure documented
- Rate limiting on authentication endpoint

## Governance Implications

Broken authentication is #2 in OWASP API Top 10.
Weak authentication leads to account takeover and privilege escalation.

## Official References

- IETF RFC 6749 (OAuth 2.0 Authorization Framework)
- IETF RFC 6750 (OAuth 2.0 Bearer Token Usage)
- IETF RFC 7519 (JSON Web Token - JWT)
- IETF RFC 8252 (OAuth 2.0 for Native Apps)
- OpenID Connect Core 1.0
- OWASP API Top 10

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
