# API Versioning Governance Standard

## Purpose

Defines versioning strategies, deprecation policies, and backward compatibility requirements.

Ensures APIs can evolve without breaking existing clients.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Subordinate to API_GOVERNANCE_STANDARD.md
Control Reference: SDLC-VERSION-03

## Governance Principles

- Explicit versioning required (no unversioned APIs in production)
- Semantic versioning for internal tracking
- Minimum 6-month deprecation window
- Deprecation headers required (RFC 8594)
- Backward compatibility maintained for 12+ months
- Breaking changes only on major version bumps

## Technical Implementation

### 1. URI Versioning (MANDATORY)

```
GET /api/v1/users          → Current version
GET /api/v2/users          → Next generation
GET /api/v1-beta/users     → Pre-release
```

Latest version never: `/api/latest/users` (tie to specific version instead)

### 2. Semantic Versioning

```
v1.2.3
├── 1 = MAJOR (breaking changes)
├── 2 = MINOR (backward-compatible features)
└── 3 = PATCH (bug fixes)
```

### 3. Deprecation Headers (MANDATORY)

```http
HTTP/1.1 200 OK
Deprecation: true
Sunset: Wed, 31 Dec 2026 23:59:59 GMT
Link: <https://docs.example.com/migration>; rel="deprecation"
X-API-Warn: "v1 endpoint deprecated; migrate to v2"
```

### 4. Version Support Lifecycle

```
v1 Released:       Jan 2024
v2 Released:       Jan 2025 (v1 enters deprecation)
v1 Sunset Notice:  Jul 2025 (6-month notice)
v1 Sunset Date:    Jan 2026 (end of support)
v2 Sunset Notice:  Jul 2026
v2 Sunset Date:    Jan 2027
```

### 5. Breaking Change Policy

| Change Type          | Backward Compatible | Requires New Version |
| -------------------- | ------------------- | -------------------- |
| New field (optional) | Yes                 | No (v1.1)            |
| New endpoint         | Yes                 | No (v1.1)            |
| Field renamed        | No                  | Yes (v2)             |
| Field removed        | No                  | Yes (v2)             |
| Field type changed   | No                  | Yes (v2)             |
| Required field added | No                  | Yes (v2)             |

## Version Migration Path

```python
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/api/v1/users")
async def get_users_v1():
    return {"version": 1, "users": []}

@app.get("/api/v2/users")
async def get_users_v2():
    return {"version": 2, "users": [], "metadata": {}}

@app.get("/api/users")
async def get_users_header(api_version: str = Header("1")):
    if api_version == "1":
        return await get_users_v1()
    elif api_version == "2":
        return await get_users_v2()
    else:
        raise HTTPException(status_code=400, detail="Unsupported version")
```

## Deprecation Lifecycle

```
Phase 1: Announcement (Month 1)
├── Deprecation header added
├── Blog post published
├── Client notifications sent
└── Migration guide released

Phase 2: Support (Months 2-6)
├── Both versions fully supported
├── Bug fixes applied to both
├── Performance parity maintained
└── Support tickets prioritized

Phase 3: Sunset Notice (Month 7)
├── Email reminders sent
├── Documentation highlights migration
├── No new features for old version
└── Bug fixes only

Phase 4: End of Life (Month 13+)
├── Endpoint disabled
├── 404 redirects to docs
└── Incident response plan activated
```

## Control Mapping

| Framework        | Reference                              |
| ---------------- | -------------------------------------- |
| ISO 27001:2022   | A.8.31 (Supplier interface management) |
| NIST SSDF        | PO.3 (Change control)                  |
| OWASP API Top 10 | API7 (Security misconfiguration)       |
| COBIT 2019       | BAI06 (Change management)              |

## Developer Checklist

- Version declared in URI or header
- Semantic versioning used for tracking
- Deprecation headers implemented
- Migration guide published
- 6-month deprecation window enforced
- Backward compatibility tested
- Sunset date documented
- Client notification procedure defined

## Governance Implications

Unmanaged API versioning breaks integrations.
Broken integrations = support incidents = operational cost.

## Official References

- RFC 8594 (The Sunset HTTP Header Field)
- RFC 7231 (HTTP/1.1 Semantics and Content)
- Semantic Versioning 2.0.0
- OpenAPI 3.0 Specification
- OWASP API Top 10

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
