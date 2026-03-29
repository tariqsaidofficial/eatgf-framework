# Zero Trust API Governance Standard

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Purpose

Defines Zero Trust architecture principles applied to API security.

Implements "never trust, always verify" at every API boundary.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Subordinate to API_GOVERNANCE_STANDARD.md
Control Reference: SDLC-ZTRUST-07

## Governance Principles

- No implicit trust based on network location
- Every request authenticated and authorized
- Deny-by-default access model
- Explicit allow lists only
- Continuous verification required
- Microsegmentation at API boundary
- Minimum privilege enforcement

## Technical Implementation

### 1. mTLS Everywhere (Service-to-Service) (MANDATORY)

```python
import ssl
import certifi

# Client certificate authentication
ssl_context = ssl.create_default_context()
ssl_context.load_cert_chain(
    certfile="/etc/ssl/certs/client.crt",
    keyfile="/etc/ssl/private/client.key"
)

response = requests.get(
    "https://internal-api.example.com/data",
    cert=("/etc/ssl/certs/client.crt", "/etc/ssl/private/client.key"),
    verify=certifi.where()
)
```

### 2. Bearer Token Validation (MANDATORY for each request)

```python
from fastapi import Depends, HTTPException, Header

async def verify_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401)

    token = authorization[7:]
    try:
        payload = verify_jwt(token)
        return payload
    except:
        raise HTTPException(status_code=403, detail="Invalid token")
```

### 3. Deny-by-Default Authorization (MANDATORY)

```python
ALLOWED_ROUTES = {
    "/api/v1/users": ["admin", "user"],
    "/api/v1/admin": ["admin"],
    "/api/v1/public": ["*"],
}

async def check_route_access(path: str, user_role: str):
    allowed_roles = ALLOWED_ROUTES.get(path)

    if allowed_roles is None:
        raise HTTPException(status_code=403, detail="Route not allowed")

    if "*" not in allowed_roles and user_role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Insufficient permissions")
```

### 4. Continuous Token Validation (MANDATORY)

```python
import time
from functools import wraps

def validate_token_freshness(max_age_seconds: int = 3600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            token_payload = get_current_token()

            # Check token hasn't expired
            if token_payload['exp'] < time.time():
                raise HTTPException(status_code=401, detail="Token expired")

            # Check token age for sensitive operations
            token_age = time.time() - token_payload['iat']
            if token_age > max_age_seconds:
                raise HTTPException(status_code=401, detail="Token too old")

            return await func(*args, **kwargs)
        return wrapper
    return decorator
```

### 5. Device & Context Verification (RECOMMENDED for Enterprise)

```python
def verify_device_context(current_user: dict, request):
    # Verify device ID hasn't changed
    device_id = request.headers.get("X-Device-ID")
    if device_id != current_user.get("device_id"):
        # Device fingerprint / location changed
        log_suspicious_activity(current_user["id"], request.client.host)
        raise HTTPException(status_code=403, detail="Unrecognized device")

    # Verify geo-location (optional)
    location = extract_geolocation(request.client.host)
    expected_location = current_user.get("expected_location")
    if location != expected_location:
        # User accessing from unexpected location
        require_additional_verification(current_user["id"])
```

### 6. Request Signing & Mutual Authentication

```python
import hmac
import hashlib
from datetime import datetime

# Client signs request
def sign_request(method: str, path: str, body: str, secret: str):
    timestamp = datetime.utcnow().isoformat()
    message = f"{method}\n{path}\n{body}\n{timestamp}"
    signature = hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    return signature, timestamp

# Server verifies signature
def verify_request_signature(request, secret: str):
    signature = request.headers.get("X-Signature")
    timestamp = request.headers.get("X-Timestamp")

    # Replay protection
    request_age = (datetime.utcnow() - datetime.fromisoformat(timestamp)).seconds
    if request_age > 300:  # 5 minutes
        raise HTTPException(status_code=401, detail="Request too old")

    # Verify signature matches
    expected_sig, _ = sign_request(request.method, request.url.path, request.body, secret)
    if not hmac.compare_digest(expected_sig, signature):
        raise HTTPException(status_code=403, detail="Invalid signature")
```

## Zero Trust Implementation Layers

```
Layer 1: User Identity
├── Multi-factor authentication
├── Context-aware verification
└── Behavioral analysis

Layer 2: Device Trust
├── Device fingerprinting
├── Geolocation verification
└── Device certificate validation

Layer 3: API Endpoint
├── mTLS between services
├── Request signing
└── Token validation

Layer 4: Application Logic
├── Resource ownership checks
├── Attribute-based access
└── Audit logging
```

## Control Mapping

| Framework | Reference |
| --- | --- |
| ISO 27001:2022 | A.8.20, A.8.21, A.8.23 |
| NIST SSDF | PS.1, PS.2 |
| NIST 800-53 | AC-2, AC-3, AC-5, AC-6 |
| NIST 800-207 | Zero Trust Architecture |

## Developer Checklist

- mTLS configured for service-to-service communication
- Bearer token validation on every request
- Deny-by-default authorization model
- Token freshness check implemented
- Device context verification (if enterprise)
- Request signing implemented (if sensitive)
- Continuous monitoring active
- Anomaly detection alerting enabled

## Governance Implications

Zero Trust prevents lateral movement after breach.
Breach containment reduces incident impact.

## Official References

- NIST SP 800-207 (Zero Trust Architecture)
- NIST SP 800-53 (Access Control)
- Google BeyondCorp Architecture
- OAuth 2.0 Proof Key for Public Clients (PKCE)

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
