# OAuth 2.0 & Identity Governance Profile

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Purpose

OAuth 2.0 and OpenID Connect provide standardized mechanisms for authentication and authorization delegation. This profile establishes governance requirements for identity provider integration, token validation, scope enforcement, and identity lifecycle management across all APIs. OAuth serves as the cross-cutting authentication layer enabling secure API access by external applications and users.

---

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Governance Scope:** 02_API_GOVERNANCE / Implementation Profile
**Document Type:** Authentication & Delegation Profile
**Applicable Standards:** OAuth 2.0 (RFC 6749), OpenID Connect 1.0, PKCE (RFC 7636)
**Integration Points:** API Gateway, Service Mesh, API Security Controls
**Organizational Profiles:** Enterprise, SaaS, Startup, Developer

---

## Relationship to EATGF Layers

This profile implements controls from:

- **Layer 08 - Developer Governance Layer**
  - Domain 02: API Governance (primary - identity control root)
  - Domain 01: Secure SDLC (credential issuance, token lifecycle, MFA integration)
  - Domain 03: DevSecOps Governance (token validation, IdP endpoint hardening, secret rotation automation)

- **Layer 05 - Domain Frameworks**
  - API Governance Framework (authentication/authorization for all service types)

- **Layer 03 - Governance Models**
  - Maturity Model (identity infrastructure capability levels)
  - Performance Model (token issuance latency, identity provider availability)

**Integration Points:**

- OAuth2/OIDC token format and validation enforces Secure SDLC requirements (Layer 08.01)
- IdP failover and token refresh policies enforced by DevSecOps (Layer 08.03)
- MFA requirements scale with organizational profile (Layer 03)
- Identity threat landscape mapped to OWASP authentication controls (Layer 05)

## Governance Principles

- **Delegated Authorization:** Users grant consent; identity provider issues fine-grained tokens
- **Token-Based Auth:** Services validate tokens without querying identity provider on every request
- **Scope Limitation:** Each token grants minimal required permissions; principle of least privilege
- **Token Lifecycle Management:** Automatic refresh, revocation, expiration enforcement
- **Secure Token Storage:** Tokens protected in transit (TLS) and at rest (encrypted storage)
- **Audit Trail:** All authentication/authorization decisions logged for compliance
- **Multi-Factor Authentication:** Integration with MFA providers for high-security contexts

---

## Governance Conformance

This section demonstrates how OAuth 2.0/OIDC identity profiles implement each mandatory control from [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md). No new controls are defined here; this profile clarifies identity-specific patterns only.

### Control 1: OAuth2 Token-Based Authentication (MANDATORY)

**Root Standard Requirement:** All APIs must authenticate using OAuth 2.0, OIDC, or equivalent.

**OAuth Implementation:** User authenticates with IdP. IdP issues access token (JWT). API validates signature using IdP's public key. Token contains user identity and scopes.

### Control 2: Scope-Based Authorization (MANDATORY)

**Root Standard Requirement:** Enforce fine-grained authorization. Verify user has permission for specific resource.

**OAuth Implementation:** Scopes define permissions. Token includes granted scopes. API checks scopes before allowing action. Resource ownership verified.

### Control 3: Token Refresh & Expiration (MANDATORY)

**Root Standard Requirement:** Enforce token expiration. Enable revocation and credential rotation.

**OAuth Implementation:** Access tokens expire in 1 hour max. Refresh tokens expire in 30 days. Revocation immediately invalidates both tokens.

### Control 4: Token Signature Validation (MANDATORY)

**Root Standard Requirement:** Verify token authenticity and integrity. Prevent token forgery.

**OAuth Implementation:** IdP signs with RS256 (asymmetric). API caches public key. Signature validated before accepting. Token exp claim validated.

### Control 5: PKCE for Public Clients (MANDATORY)

**Root Standard Requirement:** Protect against authorization code interception attacks.

**OAuth Implementation:** Public clients use PKCE. Client generates code_challenge. Auth server returns auth code. Client exchanges code + code_verifier for token.

### Control 6: MFA Integration (MANDATORY for Sensitive Operations)

**Root Standard Requirement:** High-security operations require multi-factor authentication.

**OAuth Implementation:** IdP supports MFA. APIs with sensitive scopes require MFA. Token includes `acr` claim indicating MFA completion.

### Control 7: Token Revocation (MANDATORY)

**Root Standard Requirement:** Enable logout and credential invalidation on compromise.

**OAuth Implementation:** IdP provides revocation endpoint. Client can revoke tokens. API checks revocation blocklist (refreshed every 5 minutes).

### Control 8: Cross-Tenant Isolation (MANDATORY for SaaS)

**Root Standard Requirement:** Multi-tenant systems must isolate data per tenant.

**OAuth Implementation:** Token includes tenant ID. APIs verify tenant matches resource. IdP enforces tenant context—no cross-tenant access.

---

## Mandatory OAuth & Identity Requirements

### 1. Identity Provider Selection & Certification

**Requirement:** Organizations must select certified identity providers meeting security and compliance criteria.

**Control Elements:**

- Identity provider evaluation criteria (security certifications, compliance, SLA)
- OAuth 2.0 & OpenID Connect compliance verification
- MTLS support for token endpoint (or equivalent security)
- Token signing algorithm support (RS256, ES256 minimum)
- Token revocation endpoint support
- User audit log retention (180+ days minimum)
- SLA compliance (uptime guarantee 99.9%+)
- Incident response procedures (published SLA)

**Approved Providers Evaluation Matrix:**

| Provider               | OAuth 2.0 | OIDC | mTLS | Token Revocation | Audit Logs | SOC 2  | ISO 27001 | FedRAMP | Recommended For    |
| ---------------------- | --------- | ---- | ---- | ---------------- | ---------- | ------ | --------- | ------- | ------------------ |
| Auth0                  | ✅        | ✅   | ✅   | ✅               | ✅         | ✅     | ✅        | -       | Enterprise, SaaS   |
| Keycloak (Self-hosted) | ✅        | ✅   | ✅   | ✅               | ✅         | Custom | Custom    | Custom  | All (On-premises)  |
| Azure AD / Entra       | ✅        | ✅   | ✅   | ✅               | ✅         | ✅     | ✅        | ✅      | Enterprise (Azure) |
| AWS Cognito            | ✅        | ✅   | ✅   | ✅               | ✅         | ✅     | ✅        | ✅      | Enterprise (AWS)   |
| Okta                   | ✅        | ✅   | ✅   | ✅               | ✅         | ✅     | ✅        | ✅      | Enterprise, SaaS   |
| Google Cloud Identity  | ✅        | ✅   | ✅   | ✅               | ✅         | ✅     | ✅        | -       | Enterprise (GCP)   |

**Audit Evidence:**

- Identity provider selection decision (approved list, decision date)
- Certification validation records (latest security audit, compliance certificates)
- SLA compliance tracking (uptime %, incident response times)
- Provider incident notifications received

---

### 2. Token Validation & Signature Verification

**Requirement:** All APIs must validate OAuth tokens, verifying signature, issuer, audience, and expiration before allowing access.

**Control Elements:**

- Token signature verification (asymmetric key validation)
- Token issuer validation (must match expected OIDC provider)
- Token audience validation (aud claim must match API)
- Token expiration validation (exp claim checked)
- Token blacklist/revocation checking (if immediately revocable)
- Key rotation handling (multiple key IDs supported)
- Token introspection endpoint support (fallback validation method)

**Production Example - FastAPI with OIDC Token Validation:**

```python
# FastAPI OAuth 2.0 Token Validation
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
import jwt
from jwt import PyJWKClient
from datetime import datetime
import httpx
import logging

logger = logging.getLogger(__name__)

class OAuthValidator:
    def __init__(self,
                 oidc_issuer: str,
                 api_audience: str,
                 algorithms: list = ["RS256"]):
        self.oidc_issuer = oidc_issuer
        self.api_audience = api_audience
        self.algorithms = algorithms

        # Fetch JWKS from well-known endpoint
        self.jwks_client = PyJWKClient(
            f"{oidc_issuer}/.well-known/jwks.json",
            cache_keys=True
        )

    async def validate_token(self, credentials: HTTPAuthCredentials) -> dict:
        """Validate OAuth token and return claims"""
        token = credentials.credentials

        try:
            # Get signing key from JWKS endpoint
            signing_key = self.jwks_client.get_signing_key_from_jwt(token)

            # Verify and decode token
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=self.algorithms,
                audience=self.api_audience,
                issuer=self.oidc_issuer,
                options={
                    "verify_exp": True,
                    "verify_aud": True,
                    "verify_iss": True
                }
            )

            # Additional custom validations
            self._validate_token_claims(payload)

            logger.info(f"Token validated for user: {payload.get('sub')}")
            return payload

        except jwt.ExpiredSignatureError:
            logger.warning(f"Expired token: {credentials.credentials[:20]}...")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.InvalidTokenError as e:
            logger.warning(f"Invalid token: {str(e)[:50]}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def _validate_token_claims(self, payload: dict) -> None:
        """Validate custom token claims"""
        # Verify token not revoked (if revocation list maintained)
        if 'jti' in payload:
            if self._is_token_revoked(payload['jti']):
                raise jwt.InvalidTokenError("Token has been revoked")

        # Verify token issued after last password change
        if 'iat' in payload and 'password_changed_at' in payload:
            iat_time = datetime.fromtimestamp(payload['iat'])
            pwd_changed_time = datetime.fromtimestamp(
                payload['password_changed_at']
            )
            if iat_time < pwd_changed_time:
                raise jwt.InvalidTokenError(
                    "Token issued before password change"
                )

    def _is_token_revoked(self, token_id: str) -> bool:
        """Check if token JTI is in revocation list"""
        # Implementation: Check Redis cache or database
        # For high-performance, keep revocation list in cache
        pass

# API setup
app = FastAPI()
security = HTTPBearer()

validator = OAuthValidator(
    oidc_issuer="https://auth.company.com",
    api_audience="api-backend"
)

@app.get("/api/v1/protected")
async def protected_endpoint(
    credentials: HTTPAuthCredentials = Depends(security)
) -> dict:
    """Endpoint requiring valid OAuth token"""
    claims = await validator.validate_token(credentials)

    return {
        "message": "Access granted",
        "user_id": claims.get('sub'),
        "email": claims.get('email'),
        "scope": claims.get('scope')
    }

@app.get("/api/v1/health")
async def health_check() -> dict:
    """Health check endpoint (no auth required)"""
    return {"status": "healthy"}
```

**Audit Evidence:**

- Token validation configuration (OIDC issuer, audience, algorithms)
- Token validation success/failure logs (count, timestamp, user_id)
- Signature validation failures (timestamp, token issuer, reason)
- Key rotation events (old key retired, new key activated)

---

### 3. Scope Management & Permission Validation

**Requirement:** OAuth scopes must be defined granularly, enforced at API level, and validated against token grants.

**Control Elements:**

- Scope definition (granular permissions, documented purpose)
- Scope request validation (API specifies required scopes)
- Token scope claim validation (requested scope must be in token scopes)
- Insufficient scope error handling (403 Forbidden, WWW-Authenticate header)
- Scope-to-resource mapping (which scopes allow which API operations)
- Scope consent UI (users understand what they're granting)

**Production Example - OAuth Scope Management:**

```python
# Define scopes per API resource
SCOPE_DEFINITIONS = {
    "api:read": {
        "description": "Read public API data",
        "resources": ["GET /api/v1/*"],
        "risk_level": "low"
    },
    "api:write": {
        "description": "Create and modify API data",
        "resources": ["POST /api/v1/*", "PUT /api/v1/*", "PATCH /api/v1/*"],
        "risk_level": "medium"
    },
    "api:delete": {
        "description": "Delete API data (irreversible)",
        "resources": ["DELETE /api/v1/*"],
        "risk_level": "high"
    },
    "admin:manage-users": {
        "description": "Manage user access and permissions",
        "resources": ["GET /admin/users", "POST /admin/users", "DELETE /admin/users"],
        "risk_level": "critical"
    }
}

# Scope enforcement middleware
from fastapi import Request
from typing import List

class ScopeValidator:
    def __init__(self, required_scopes: List[str]):
        self.required_scopes = required_scopes

    async def __call__(self, request: Request, claims: dict) -> None:
        """Validate token scopes before allowing access"""
        token_scopes = claims.get('scope', '').split()

        # Check if token has required scope
        if not any(scope in token_scopes for scope in self.required_scopes):
            missing_scopes = set(self.required_scopes) - set(token_scopes)

            # Log insufficient scope attempt
            logger.warning(
                f"Insufficient scope: user={claims.get('sub')}, "
                f"required={self.required_scopes}, "
                f"granted={token_scopes}"
            )

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient scope. Required: {', '.join(missing_scopes)}",
                headers={
                    "WWW-Authenticate": f'Bearer scope="{" ".join(missing_scopes)}"'
                }
            )

# Endpoint with scope requirement
scope_validator = ScopeValidator(required_scopes=["api:write"])

@app.post("/api/v1/resources")
async def create_resource(
    resource_data: dict,
    credentials: HTTPAuthCredentials = Depends(security),
    _: None = Depends(scope_validator)
) -> dict:
    """Create resource - requires api:write scope"""
    claims = await validator.validate_token(credentials)
    return {"id": "new-resource-id", "owner": claims.get('sub')}
```

**Audit Evidence:**

- Scope definition document (approved scopes per API)
- Scope grant audit log (user consent, timestamp, granted scopes)
- Scope validation failures (timestamp, user, required scope, granted scope)
- Scope change history (new scope added, deprecation notices for old scopes)

---

### 4. Refresh Token & Token Lifecycle Management

**Requirement:** Tokens must have limited lifetime; refresh tokens enable obtaining new tokens without user interaction.

**Control Elements:**

- Access token lifetime (15-60 minutes typical)
- Refresh token lifetime (days/weeks/months depending on usage)
- Refresh token rotation (issue new refresh token on current token use)
- Refresh request validation (client authentication, grant_type validation)
- Refresh token revocation capability
- Automatic token refresh before expiration
- Offline access scope for long-running processes

**Production Example - OAuth Token Refresh Pattern:**

```python
# Token refresh endpoint integration
from datetime import datetime, timedelta

class TokenRefreshManager:
    """Manage token refresh lifecycle"""

    async def refresh_access_token(
        self,
        refresh_token: str,
        client_id: str,
        client_secret: str
    ) -> dict:
        """Exchange refresh token for new access token"""

        # Validate refresh token (similar to access token validation)
        try:
            payload = jwt.decode(
                refresh_token,
                algorithms=["RS256"],
                options={"verify_exp": True}
            )
        except jwt.ExpiredSignatureError:
            logger.warning(f"Expired refresh token for client: {client_id}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Refresh token expired"
            )

        # Validate client credentials
        if not await self._validate_client(client_id, client_secret):
            logger.warning(f"Invalid client credentials: {client_id}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid client credentials"
            )

        # Verify refresh token was issued to this client
        if payload.get('client_id') != client_id:
            logger.warning(
                f"Refresh token client mismatch: token={payload.get('client_id')}, "
                f"request={client_id}"
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid refresh token"
            )

        # Issue new access token
        new_access_token = self._generate_access_token(payload)

        # Optionally rotate refresh token (issue new refresh token)
        new_refresh_token = self._generate_refresh_token(payload)

        logger.info(
            f"Token refreshed for client: {client_id}, "
            f"user: {payload.get('sub')}"
        )

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,  # 1 hour
            "scope": payload.get('scope')
        }

    def _generate_access_token(self, original_payload: dict) -> str:
        """Generate new access token with original claims"""
        now = datetime.utcnow()
        expiry = now + timedelta(hours=1)

        payload = {
            "sub": original_payload.get('sub'),
            "email": original_payload.get('email'),
            "scope": original_payload.get('scope'),
            "iat": int(now.timestamp()),
            "exp": int(expiry.timestamp()),
            "iss": "https://auth.company.com",
            "aud": "api-backend"
        }

        return jwt.encode(payload, private_key, algorithm="RS256")

    def _generate_refresh_token(self, original_payload: dict) -> str:
        """Generate new refresh token (long lifetime)"""
        now = datetime.utcnow()
        expiry = now + timedelta(days=30)  # 30-day refresh token

        payload = {
            "sub": original_payload.get('sub'),
            "client_id": original_payload.get('client_id'),
            "iat": int(now.timestamp()),
            "exp": int(expiry.timestamp()),
            "iss": "https://auth.company.com",
            "jti": str(uuid.uuid4())  # Token ID for revocation
        }

        return jwt.encode(payload, private_key, algorithm="RS256")

# API endpoint for token refresh
@app.post("/oauth/token")
async def refresh_token_endpoint(
    grant_type: str,
    refresh_token: str,
    client_id: str,
    client_secret: str
) -> dict:
    """OAuth 2.0 Token Refresh endpoint"""

    if grant_type != "refresh_token":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported grant_type: {grant_type}"
        )

    manager = TokenRefreshManager()
    return await manager.refresh_access_token(
        refresh_token, client_id, client_secret
    )
```

**Audit Evidence:**

- Token generation audit log (timestamp, user, client, granted scope)
- Token refresh audit log (timestamp, user, client, reason)
- Token revocation requests (timestamp, token_id, requester)
- Long-lived token usage (offline_access scope grants)

---

### 5. Logout & Token Revocation

**Requirement:** Users must be able to explicitly revoke OAuth tokens; logout must invalidate all tokens for that session.

**Control Elements:**

- Logout endpoint implementation
- Access token revocation
- Refresh token revocation (primary revocation point)
- Session termination across all applications
- Optional: Immediate revocation support (via revocation endpoint)
- Token revocation audit logging
- Revocation list maintenance (if revocation check required)

**Production Example - Logout & Revocation:**

```python
# Logout endpoint - revokes all user tokens
@app.post("/oauth/logout")
async def logout_endpoint(
    credentials: HTTPAuthCredentials = Depends(security),
    request: Request = None
) -> dict:
    """Logout endpoint - revoke all tokens for user"""

    claims = await validator.validate_token(credentials)
    user_id = claims.get('sub')

    # Revoke all refresh tokens for this user
    revoked_count = await revoke_user_tokens(user_id)

    logger.info(f"User logout: user={user_id}, revoked_tokens={revoked_count}")

    return {
        "message": "Successfully logged out",
        "tokens_revoked": revoked_count
    }

# Token revocation endpoint (RFC 7009)
@app.post("/oauth/revoke")
async def revoke_token_endpoint(
    token: str,
    token_type_hint: str = "access_token",  # Optional hint
    client_id: str = None,
    client_secret: str = None
) -> dict:
    """RFC 7009 Token Revocation endpoint"""

    # Validate client credentials
    if not await validate_client(client_id, client_secret):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid client credentials"
        )

    try:
        # Decode token to get JTI (token ID)
        payload = jwt.decode(
            token,
            algorithms=["RS256"],
            options={"verify_signature": True, "verify_exp": False}
        )
        token_jti = payload.get('jti')

        # Add to revocation list
        await add_to_revocation_list(token_jti, datetime.utcnow())

        # Also revoke related tokens (if refresh token, revoke all related access tokens)
        if token_type_hint == "refresh_token":
            await revoke_related_access_tokens(token_jti)

        logger.info(f"Token revoked: jti={token_jti}, type={token_type_hint}")

    except jwt.DecodeError:
        # Token already invalid; per RFC 7009, return 200 anyway
        logger.warning(f"Revoke called with invalid token")

    # Always return 200 (RFC 7009 requirement)
    return {"status": "revoked"}

# Revocation list implementation (Redis for performance)
async def add_to_revocation_list(token_jti: str, revoked_at: datetime) -> None:
    """Add token JTI to revocation list"""
    redis = await get_redis()

    # Store with TTL = token expiration time
    revocation_key = f"revoked_token:{token_jti}"
    await redis.set(revocation_key, "revoked", ex=86400)  # 24 hours

    logger.debug(f"Token added to revocation list: {token_jti}")
```

**Audit Evidence:**

- Logout audit log (timestamp, user, reason)
- Token revocation log (timestamp, token_jti, requester, reason)
- Session termination records (user, all devices/applications logged out)
- Revocation reason classification (user-initiated, admin-initiated, security reasons)

---

### 6. Multi-Factor Authentication Integration

**Requirement:** APIs must support multi-factor authentication, particularly for sensitive operations and high-risk users.

**Control Elements:**

- MFA method support (TOTP, SMS, email OTP, hardware keys)
- MFA claim in token (indicates authentication strength)
- Step-up authentication (re-authenticate for sensitive operations)
- MFA enforcement per user/application risk level
- MFA bypass policies (emergency access, trusted devices)
- MFA recovery procedure (backup codes, device recovery)

**Production Example - MFA-Protected API Access:**

```python
# MFA claim validation
class MFAValidator:
    """Validate MFA requirements"""

    def __init__(self, identity_provider_client):
        self.idp = identity_provider_client

    async def verify_mfa_requirement(
        self,
        claims: dict,
        operation_risk_level: str  # "low", "medium", "high", "critical"
    ) -> bool:
        """Check if MFA requirement satisfied for operation"""

        user_risk_profile = await self.get_user_risk_profile(claims.get('sub'))
        mfa_methods_used = claims.get('amr', [])  # Authentication Methods References

        # Determine MFA requirement based on operation + user risk
        mfa_required = self._should_require_mfa(
            operation_risk_level,
            user_risk_profile
        )

        if not mfa_required:
            return True

        # Check if MFA was used in this authentication
        if 'mfa' in mfa_methods_used or 'totp' in mfa_methods_used:
            # Verify MFA timestamp recent (< 15 minutes)
            mfa_timestamp = claims.get('auth_time', 0)
            if self._is_recent(mfa_timestamp, minutes=15):
                logger.info(f"MFA verified for user: {claims.get('sub')}")
                return True

        logger.warning(
            f"MFA required but not satisfied: "
            f"user={claims.get('sub')}, operation={operation_risk_level}"
        )
        return False

    def _should_require_mfa(self, operation_risk: str, user_risk: str) -> bool:
        """Determine if MFA required based on risk levels"""
        risk_matrix = {
            ("critical", "high"): True,
            ("critical", "medium"): True,
            ("high", "high"): True,
            ("high", "medium"): True,
            ("medium", "high"): True,
        }
        return risk_matrix.get((operation_risk, user_risk), False)

    def _is_recent(self, timestamp: int, minutes: int) -> bool:
        """Check if timestamp is within N minutes"""
        now = datetime.utcnow()
        auth_time = datetime.fromtimestamp(timestamp)
        return (now - auth_time).total_seconds() < (minutes * 60)

    async def get_user_risk_profile(self, user_id: str) -> str:
        """Get user risk classification"""
        # Implementation: Check user profile, location, device, etc.
        pass

# API endpoint requiring MFA for sensitive operation
mfa_validator = MFAValidator(idp_client)

@app.delete("/api/v1/sensitive-resource/{resource_id}")
async def delete_sensitive_resource(
    resource_id: str,
    credentials: HTTPAuthCredentials = Depends(security)
) -> dict:
    """Delete sensitive resource - requires MFA"""

    claims = await validator.validate_token(credentials)

    # Verify MFA for this high-risk operation
    if not await mfa_validator.verify_mfa_requirement(claims, "critical"):
        logger.warning(
            f"MFA step-up required: user={claims.get('sub')}, "
            f"operation=delete_sensitive"
        )
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Multi-factor authentication required for this operation"
        )

    # Proceed with deletion
    await delete_resource(resource_id)
    return {"status": "deleted"}

# Step-up authentication endpoint
@app.post("/oauth/step-up-authentication")
async def step_up_authentication(
    credentials: HTTPAuthCredentials = Depends(security),
    mfa_method: str = "totp"
) -> dict:
    """Request step-up authentication for sensitive operation"""

    claims = await validator.validate_token(credentials)
    user_id = claims.get('sub')

    # Generate MFA challenge
    challenge = await idp.initiate_mfa(user_id, mfa_method)

    return {
        "challenge_id": challenge.id,
        "mfa_method": mfa_method,
        "expires_in": 300  # 5 minutes to complete
    }
```

**Audit Evidence:**

- MFA enrollment audit log (user, method, date)
- MFA verification log (successful/failed, method, timestamp)
- Step-up authentication requests (operation, user, result)
- MFA bypass records (user, reason, approver, timestamp)

---

### 7. Client Credential Grant & Service-to-Service Auth

**Requirement:** Service-to-service communication must use Client Credentials grant type with mTLS for highest security.

**Control Elements:**

- Client ID & secret management (secure storage, rotation)
- mTLS certificate verification (supplementary to credentials)
- Token lifetime enforcement (short-lived for service-to-service)
- Client scope restrictions (minimum required scopes per client)
- Client revocation capability
- Client usage monitoring (anomaly detection)

**Production Example - Service-to-Service OAuth:**

```python
# Service-to-Service OAuth Client Credentials
class ClientCredentialsGrantHandler:
    """Handle OAuth 2.0 Client Credentials grant"""

    async def issue_token(
        self,
        client_id: str,
        client_secret: str,
        scope: str,
        mtls_cert: str = None  # Optional but recommended
    ) -> dict:
        """Issue access token using Client Credentials grant"""

        # Authenticate client
        client = await self._authenticate_client(client_id, client_secret)

        if not client:
            logger.warning(f"Client authentication failed: {client_id}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid client credentials"
            )

        # Validate mTLS certificate (if provided)
        if mtls_cert:
            if not self._verify_mtls_certificate(client_id, mtls_cert):
                logger.warning(f"mTLS certificate mismatch: {client_id}")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="mTLS certificate invalid"
                )

        # Validate requested scopes
        requested_scopes = scope.split()
        allowed_scopes = client.get('allowed_scopes', [])

        invalid_scopes = set(requested_scopes) - set(allowed_scopes)
        if invalid_scopes:
            logger.warning(
                f"Client requested unauthorized scope: "
                f"client={client_id}, requested={invalid_scopes}"
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid scope: {', '.join(invalid_scopes)}"
            )

        # Issue short-lived access token
        access_token = self._generate_service_token(
            client_id,
            requested_scopes,
            lifetime_seconds=900  # 15 minutes for service-to-service
        )

        logger.info(
            f"Service token issued: client={client_id}, scopes={requested_scopes}"
        )

        return {
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_in": 900,
            "scope": scope
        }

    async def _authenticate_client(
        self,
        client_id: str,
        client_secret: str
    ) -> dict:
        """Authenticate OAuth client"""

        # Fetch client from secure store
        client = await self._get_client(client_id)

        if not client:
            return None

        # Verify client secret
        if not await bcrypt.verify(client_secret, client['secret_hash']):
            return None

        # Check if client active
        if not client.get('active', False):
            return None

        return client

    def _verify_mtls_certificate(
        self,
        client_id: str,
        certificate: str
    ) -> bool:
        """Verify mTLS certificate matches client"""
        # Implementation: Verify certificate CN matches client_id
        # Verify certificate signed by trusted CA
        pass

# API endpoint for service-to-service token
@app.post("/oauth/token")
async def token_endpoint(
    grant_type: str,
    client_id: str,
    client_secret: str,
    scope: str = "",
    request: Request = None
) -> dict:
    """OAuth 2.0 Token endpoint"""

    if grant_type == "client_credentials":
        handler = ClientCredentialsGrantHandler()

        # Extract mTLS cert if presented
        mtls_cert = request.client.certificate if hasattr(request, 'client') else None

        return await handler.issue_token(
            client_id, client_secret, scope, mtls_cert
        )

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported grant_type: {grant_type}"
        )
```

**Audit Evidence:**

- Client registration audit log (client_id, created_by, creation_date)
- Client secret rotation log (old secret retired, new secret issued)
- Token issuance log (client_id, scope, issued_at, expires_at)
- Failed authentication attempts (client_id, timestamp, reason)

---

### 8. PKCE for Public Clients

**Requirement:** Native applications and SPAs must use Proof Key for Code Exchange (PKCE) to protect against authorization code interception.

**Control Elements:**

- PKCE enforcement for public clients (native apps, SPAs)
- S256 code challenge method (SHA-256 hashing required)
- Code challenge & code verifier validation
- PKCE optional but recommended for confidential clients
- Code parameter validation (single-use, short-lived)

**Production Example - PKCE Flow Implementation:**

```python
# PKCE implementation
import secrets
import hashlib
import base64

class PKCEValidator:
    """Validate Proof Key for Code Exchange"""

    @staticmethod
    def generate_code_challenge() -> tuple:
        """Generate PKCE code challenge and verifier"""

        # Generate random code verifier (43-128 characters)
        code_verifier = base64.urlsafe_b64encode(
            secrets.token_bytes(32)
        ).decode('utf-8').rstrip('=')

        # Generate code challenge (S256: SHA256 hash)
        code_challenge = base64.urlsafe_b64encode(
            hashlib.sha256(code_verifier.encode('utf-8')).digest()
        ).decode('utf-8').rstrip('=')

        return code_verifier, code_challenge

    @staticmethod
    async def validate_pkce(
        authorization_code: str,
        code_verifier: str,
        challenge_method: str = "S256"
    ) -> bool:
        """Validate PKCE code verifier"""

        # Retrieve stored code challenge
        stored_challenge = await AuthorizationCodeStore.get_challenge(
            authorization_code
        )

        if not stored_challenge:
            logger.warning(f"Code challenge not found: {authorization_code}")
            return False

        # Compute challenge from verifier
        if challenge_method == "S256":
            computed_challenge = base64.urlsafe_b64encode(
                hashlib.sha256(code_verifier.encode('utf-8')).digest()
            ).decode('utf-8').rstrip('=')
        else:
            # Plain method (not recommended)
            computed_challenge = code_verifier

        # Verify challenge matches
        if computed_challenge != stored_challenge:
            logger.warning(
                f"PKCE challenge mismatch for code: {authorization_code}"
            )
            return False

        return True

# Authorization endpoint with PKCE
@app.get("/oauth/authorize")
async def authorize_endpoint(
    response_type: str,
    client_id: str,
    redirect_uri: str,
    scope: str,
    state: str,
    code_challenge: str = None,
    code_challenge_method: str = "S256"
) -> RedirectResponse:
    """OAuth 2.0 Authorization endpoint with PKCE"""

    # Validate client
    client = await validate_client_redirect_uri(client_id, redirect_uri)
    if not client:
        raise HTTPException(status_code=400, detail="Invalid client")

    # PKCE requirement for public clients
    if client.get('is_public') and not code_challenge:
        raise HTTPException(
            status_code=400,
            detail="PKCE code_challenge required for public clients"
        )

    # Generate authorization code
    auth_code = secrets.token_urlsafe(32)

    # Store code + PKCE challenge
    await AuthorizationCodeStore.save(
        code=auth_code,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        code_challenge=code_challenge,
        challenge_method=code_challenge_method,
        expires_at=datetime.utcnow() + timedelta(minutes=10)
    )

    # Redirect back to client with code
    params = {
        'code': auth_code,
        'state': state
    }
    return RedirectResponse(
        url=f"{redirect_uri}?{'&'.join([f'{k}={v}' for k,v in params.items()])}"
    )

# Token endpoint validating PKCE
@app.post("/oauth/token")
async def token_endpoint_pkce(
    grant_type: str,
    code: str,
    client_id: str,
    redirect_uri: str,
    code_verifier: str = None
) -> dict:
    """Token endpoint with PKCE validation"""

    if grant_type != "authorization_code":
        raise HTTPException(status_code=400, detail="Invalid grant_type")

    # Get authorization code details
    auth_code_data = await AuthorizationCodeStore.get(code)

    if not auth_code_data:
        raise HTTPException(status_code=400, detail="Invalid authorization code")

    # Validate PKCE
    if auth_code_data.get('code_challenge'):
        if not code_verifier:
            raise HTTPException(status_code=400, detail="code_verifier required")

        if not await PKCEValidator.validate_pkce(
            code,
            code_verifier,
            auth_code_data.get('challenge_method', 'S256')
        ):
            raise HTTPException(status_code=400, detail="Invalid code_verifier")

    # Issue access token
    access_token = generate_access_token(
        auth_code_data.get('client_id'),
        auth_code_data.get('scope')
    )

    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": auth_code_data.get('scope')
    }
```

**Audit Evidence:**

- PKCE code challenge submission (client_id, timestamp)
- PKCE verification result (successful/failed, timestamp)
- Public client configuration (which clients require PKCE)

---

## Severity & Maturity

**Severity Model and Maturity Progression are defined in [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md) and apply uniformly across all architecture profiles.**

OAuth 2.0 & Identity deployments inherit the standard 5-level maturity model and organizational profile severity escalation (Enterprise → SaaS → Startup → Developer).

## Developer Checklist

- [ ] **Select Identity Provider:** Choose certified provider (Auth0, Keycloak, Azure AD, AWS Cognito, Okta, Google Cloud)
- [ ] **Configure OIDC Discovery:** Verify `.well-known/openid-configuration` endpoint returns correct metadata
- [ ] **Implement Token Validation:** Deploy JWT signature verification, issuer validation, audience validation, expiration check
- [ ] **Define Scopes:** Document granular scopes per API resource; get security approval
- [ ] **Implement Scope Enforcement:** Verify token claims include required scopes before allowing operation
- [ ] **Configure Token Refresh:** Set access token lifetime (1 hour default), refresh token lifetime (30 days default)
- [ ] **Implement Logout:** Create logout endpoint that revokes user tokens across all applications
- [ ] **Enable Audit Logging:** Log all authentication, authorization, token refresh, token revocation events
- [ ] **Implement PKCE:** For native applications and SPAs, enforce PKCE authorization code grant
- [ ] **Configure MFA:** For sensitive operations, require multi-factor authentication step-up
- [ ] **Test Authorization Failures:** Verify invalid tokens rejected with 401; insufficient scope returns 403
- [ ] **Monitor Identity Provider:** Set up alerts for provider outages, certificate expiration, suspicious activity
- [ ] **Document Authorization Flow:** Create runbook describing OAuth flow for application developers

---

## Control Mapping to External Frameworks

**Framework mapping for OAuth & Identity controls is maintained in [API_CONTROL_MAPPING_APPENDIX.md](../API_CONTROL_MAPPING_APPENDIX.md). Do not duplicate mappings in architecture-specific profiles.**

---

## Governance Implications

**Risk if Not Implemented:**

- No OAuth/OIDC → custom token implementation → security vulnerabilities
- Missing token validation → unauthorized access to protected resources
- Insufficient scope enforcement → privilege escalation
- No token revocation → cannot respond to compromised credentials

**Operational Impact:**

- Identity provider outages impact all API access
- Token lifetime tuning affects security vs. UX tradeoff
- MFA requirements may reduce developer convenience (acceptable for sensitive operations)
- Audit logging volume high (all token requests logged)

**Audit Consequences:**

- OAuth compliance reviewed in ISO 27001/SOC 2 audits
- Token validation implementation verified
- MFA enforcement verified for sensitive operations
- Audit logs examined for suspicious authentication patterns

**Cross-Team Dependencies:**

- **Identity Team:** Manage identity provider, issue credentials, incident response
- **API Teams:** Implement token validation, scope enforcement
- **Security Team:** Define scope hierarchy, approve MFA requirements
- **Observability Team:** Collect authentication metrics, build dashboards

---

## References

- OAuth 2.0 Authorization Framework - RFC 6749: `https://tools.ietf.org/html/rfc6749`
- OpenID Connect Core 1.0: `https://openid.net/specs/openid-connect-core-1_0.html`
- Proof Key for Code Exchange (PKCE) - RFC 7636: `https://tools.ietf.org/html/rfc7636`
- OAuth 2.0 Token Revocation - RFC 7009: `https://tools.ietf.org/html/rfc7009`
- NIST SP 800-63B - Authentication and Lifecycle Management
- Auth0 - OAuth 2.0 & OIDC Implementation Guide: `https://auth0.com/docs/`
- OWASP - OAuth 2.0 Security: `https://cheatsheetseries.owasp.org/cheatsheets/OAuth_2_0_Cheat_Sheet.html`

---

## Version & Authority

**Document Title:** OAuth 2.0 & Identity Governance Profile
**Version:** 1.0
**Release Date:** 2026-02-14
**Change Type:** Major (First Release)
**EATGF Baseline:** Block 2 API Governance Module
**Authority:** API Governance Implementation Profile
**Next Review Date:** 2026-05-14
**Compliance Status:** EATGF Signature Template Compliant ✅
