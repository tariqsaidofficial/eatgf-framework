# API Authorization Governance Standard

## Purpose

Defines mandatory access control policies for API resources.

Ensures authenticated users only access resources they are authorized for.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Subordinate to API_GOVERNANCE_STANDARD.md
Control Reference: SDLC-AUTHZ-02

## Governance Principles

- Authorization required after successful authentication
- Explicit whitelist model (deny by default)
- Resource ownership verified per request
- Role-based (RBAC) or Attribute-based (ABAC)
- Tenant isolation for multi-tenant systems
- Regular access review and revocation

## Technical Implementation

### 1. Role-Based Access Control (RBAC) (MANDATORY)

```python
from fastapi import Depends, HTTPException

ROLES = {
    "admin": ["read", "write", "delete"],
    "user": ["read", "write"],
    "viewer": ["read"]
}

def require_role(required_role: str):
    def check_role(current_user: dict = Depends(get_current_user)):
        user_role = current_user.get("role")
        if user_role not in ROLES or required_role not in ROLES[user_role]:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return check_role

@app.delete("/users/{user_id}")
async def delete_user(user_id: str, current_user = Depends(require_role("admin"))):
    return {"deleted": user_id}
```

### 2. Attribute-Based Access Control (ABAC) (RECOMMENDED for SaaS)

```python
def require_abac_permission(required_action: str):
    def check_permission(current_user: dict = Depends(get_current_user)):
        user_attrs = {
            "user_id": current_user.get("sub"),
            "tenant_id": current_user.get("tenant_id"),
            "department": current_user.get("department"),
            "clearance": current_user.get("clearance_level")
        }

        allowed = evaluate_policy(user_attrs, required_action)
        if not allowed:
            raise HTTPException(status_code=403, detail="Access denied")
        return current_user
    return check_permission
```

### 3. Resource Ownership Verification (MANDATORY)

```python
@app.get("/api/v1/users/{user_id}/profile")
async def get_user_profile(user_id: str, current_user = Depends(get_current_user)):
    # Broken Object Level Authorization (BOLA) prevention
    if current_user["sub"] != user_id and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access denied")

    return get_profile(user_id)
```

### 4. Tenant Isolation (MANDATORY for Multi-Tenant)

```python
@app.get("/api/v1/organizations/{org_id}/users")
async def list_org_users(org_id: str, current_user = Depends(get_current_user)):
    # Tenant boundary enforcement
    user_org = current_user.get("org_id")
    if user_org != org_id:
        raise HTTPException(status_code=403, detail="Cross-tenant access denied")

    return get_users_for_org(org_id)
```

### 5. Authorization Cache (Performance)

```python
from functools import lru_cache

@lru_cache(maxsize=10000)
def check_authorization(user_id: str, resource_id: str, action: str) -> bool:
    # Cache authorization decisions for 5 minutes
    policy = get_policy(user_id)
    return action in policy.get(resource_id, [])
```

## Authorization Matrix Template

| Role | GET | POST | PUT | DELETE | Admin |
| --- | --- | --- | --- | --- | --- |
| admin | ✓ | ✓ | ✓ | ✓ | ✓ |
| user | ✓ | ✓ | own | - | - |
| viewer | ✓ | - | - | - | - |
| guest | public | - | - | - | - |

## Control Mapping

| Framework | Reference |
| --- | --- |
| ISO 27001:2022 | A.8.20, A.8.23 (Access Control) |
| NIST SSDF | PW.4 (Access Control) |
| OWASP API Top 10 | API1 (Broken Object Level Authorization) |
| NIST 800-53 | AC-3 (Enforcement) |

## Developer Checklist

- Authorization logic separate from business logic
- Resource ownership verified per request
- Role/attribute decisions logged
- Deny-by-default model implemented
- Multi-tenant boundary tested
- Authorization cache implemented (if performance-critical)
- Emergency access revocation procedure documented

## Governance Implications

Broken Object Level Authorization (BOLA) is #1 in OWASP API Top 10.
Authorization bypass bypasses all upstream controls.

## Official References

- OWASP ASVS v4.0 (V4 Access Control)
- OWASP API Top 10 (API1, API5)
- NIST SP 800-53 (AC-3, AC-5)
- NIST SP 800-192 (Access Control Guide)

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
