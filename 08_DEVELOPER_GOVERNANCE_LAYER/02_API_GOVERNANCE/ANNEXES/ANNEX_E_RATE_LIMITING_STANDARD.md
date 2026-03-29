# Rate Limiting & Quota Governance Standard

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Purpose

Defines rate limiting policies to prevent resource exhaustion and DoS attacks.

Ensures API availability through traffic shaping and quota enforcement.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Subordinate to API_GOVERNANCE_STANDARD.md
Control Reference: SDLC-RATELIMIT-05

## Governance Principles

- Rate limiting mandatory for all public APIs
- Per-IP limits for unauthenticated endpoints
- Per-token quotas for authenticated endpoints
- Burst allowance for legitimate traffic
- Dynamic limits based on tier/plan

## Technical Implementation

### 1. IP-Based Rate Limiting (MANDATORY for public APIs)

```nginx
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;

server {
    location /api/ {
        limit_req zone=api_limit burst=20 nodelay;
    }
}
```

### 2. Token-Based Quota (MANDATORY for authenticated APIs)

```python
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.util import get_request_identifier

@app.get("/api/v1/users")
@FastAPILimiter.limit("100/minute")
async def list_users():
    return {"users": []}
```

### 3. Tiered Rate Limits

| Plan         | Requests/Minute | Burst Allowance | Monthly Quota |
| ------------ | --------------- | --------------- | ------------- |
| Free         | 10              | 15              | 10,000        |
| Startup      | 100             | 200             | 500,000       |
| Professional | 1,000           | 2,000           | 10,000,000    |
| Enterprise   | Unlimited       | Custom          | Unlimited     |

### 4. Rate Limit Headers (MANDATORY)

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 75
X-RateLimit-Reset: 1634567890
RateLimit-Limit: 100
RateLimit-Remaining: 75
RateLimit-Reset: 1634567890
```

### 5. 429 Too Many Requests Response

```json
HTTP/1.1 429 Too Many Requests
Content-Type: application/json
Retry-After: 60

{
  "error": "rate_limit_exceeded",
  "message": "Too many requests",
  "retry_after_seconds": 60,
  "reset_time": "2024-02-14T12:00:00Z"
}
```

### 6. Dynamic Rate Limiting (RECOMMENDED)

```python
def get_rate_limit(user_id: str, tier: str) -> int:
    base_limit = TIER_LIMITS.get(tier, 10)

    # Adjust based on historical usage
    usage_score = calculate_usage_pattern(user_id)
    if usage_score > 0.9:  # Consistently high usage
        return base_limit * 1.5
    elif usage_score < 0.2:  # Inactive user
        return base_limit * 0.5

    return base_limit
```

## Quota Enforcement Strategy

```
Sliding Window:
├── Per-minute: Real-time limit
├── Per-hour: Aggregated metric
└── Per-day: Calendar-based reset

Fixed Window:
├── Reset at midnight UTC
├── Simple to implement
└── Vulnerable to burst attacks
```

## Control Mapping

| Framework        | Reference                                |
| ---------------- | ---------------------------------------- |
| ISO 27001:2022   | A.8.30 (DoS protection)                  |
| NIST SSDF        | RV.1 (Monitor)                           |
| OWASP API Top 10 | API4 (Unrestricted Resource Consumption) |
| NIST 800-53      | SC-5 (DoS protection)                    |

## Developer Checklist

- Rate limiting configured at gateway
- Per-IP and per-token limits defined
- Rate limit headers returned
- 429 response format standardized
- Burst allowance configured
- Quota persistence (database/cache)
- Monitoring/alerting on exceeded quotas
- Tier-based scaling implemented

## Governance Implications

Unprotected APIs can be exhausted by single malicious actor.
Resource exhaustion = service unavailability = SLA breach.

## Official References

- IETF RFC 6585 (Additional HTTP Status Codes)
- OWASP API Top 10 (API4)
- NIST SP 800-53 (SC-5)

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
