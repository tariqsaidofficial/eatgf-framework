# Webhook Security Governance Standard

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Purpose

Defines security requirements for webhook delivery and reception.

Ensures webhook payloads are authenticated and cannot be replayed.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Subordinate to API_GOVERNANCE_STANDARD.md
Control Reference: SDLC-WEBHOOK-04

## Governance Principles

- All webhooks require HMAC signature verification
- Timestamp validation prevents replay attacks
- Request signing mandatory for producer
- Signature verification mandatory for consumer
- Retry policy with exponential backoff required
- Webhook events must be idempotent

## Technical Implementation

### 1. HMAC-SHA256 Signature (MANDATORY)

Producer (generating signature):

```python
import hmac
import hashlib
import json
import time

def sign_webhook(payload: dict, secret: str) -> str:
    timestamp = str(int(time.time()))
    payload_json = json.dumps(payload, sort_keys=True)

    message = f"{timestamp}.{payload_json}"
    signature = hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    return f"v1,{signature}", timestamp
```

Consumer (verifying signature):

```python
def verify_webhook_signature(
    payload_body: bytes,
    signature_header: str,
    secret: str,
    timestamp_header: str,
    max_age_seconds: int = 300
) -> bool:
    # Verify timestamp
    try:
        timestamp = int(timestamp_header)
    except ValueError:
        return False

    if abs(time.time() - timestamp) > max_age_seconds:
        return False  # Replay protection

    # Verify signature
    message = f"{timestamp}.{payload_body.decode()}"
    expected = hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected, signature_header.split(",")[1])
```

### 2. Webhook Headers (MANDATORY)

```http
POST /webhooks/events HTTP/1.1
Host: api.example.com
Content-Type: application/json
X-Webhook-Signature: v1,a1b2c3d4e5f6g7h8i9j0
X-Webhook-Timestamp: 1634567890
X-Webhook-ID: evt_123456789
X-Webhook-Delivery-Attempt: 1

{"event": "order.created", "order_id": "12345"}
```

### 3. Idempotency (MANDATORY for safety)

```python
from functools import wraps
import hashlib

SEEN_EVENTS = {}  # Or use Redis for distributed systems

def idempotent_webhook(func):
    @wraps(func)
    def wrapper(event_id: str, payload: dict):
        if event_id in SEEN_EVENTS:
            return {"status": "already_processed"}

        result = func(event_id, payload)
        SEEN_EVENTS[event_id] = True
        return result

    return wrapper

@app.post("/webhooks/events")
@idempotent_webhook
async def handle_webhook(event_id: str, payload: dict):
    # Process event only once
    return {"processed": event_id}
```

### 4. Retry Policy with Exponential Backoff (MANDATORY)

```yaml
# Retry Configuration
max_retries: 5
initial_backoff_seconds: 5
max_backoff_seconds: 3600  # 1 hour
backoff_multiplier: 2

# Retry Schedule:
# Attempt 1: Immediate
# Attempt 2: 5 seconds later
# Attempt 3: 10 seconds later
# Attempt 4: 20 seconds later
# Attempt 5: 40 seconds later
```

### 5. Status Code Expectations

```
200-299: Success (stop retrying)
400-499: Client error (stop retrying)
401/403: Auth error (stop; alert webhook owner)
500-599: Server error (retry according to policy)
Timeout: Retry
```

## Webhook Event Schema

```json
{
  "id": "evt_123456789",
  "timestamp": 1634567890,
  "event": "order.created",
  "version": "v1",
  "data": {
    "order_id": "ord_987654321",
    "amount": 99.99,
    "currency": "USD"
  }
}
```

## Control Mapping

| Framework | Reference |
| --- | --- |
| ISO 27001:2022 | A.8.15 (Data integrity) |
| NIST SSDF | PS.2 (Protect secrets) |
| OWASP API Top 10 | API5 (Broken access control) |
| NIST 800-53 | SI-7 (Information integrity) |

## Developer Checklist

- HMAC-SHA256 signature implemented
- Timestamp validation enforced
- Replay protection configured
- Idempotency keys used
- Retry policy with backoff implemented
- Webhook events logged
- Signature header format documented
- Error handling tested

## Governance Implications

Unsigned webhooks can be forged, leading to data corruption.
Replay attacks can cause duplicate transactions.

## Official References

- RFC 3610 (HMAC and AEAD)
- RFC 7231 (HTTP/1.1)
- OWASP Webhook Security Guide
- IETF Draft (Signed HTTP Messages)

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
