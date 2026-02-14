# Webhook & Event-Driven API Governance Profile

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Profile Description

Enterprise AI-Aligned Technical Governance Framework (EATGF)
Version: 1.0
Layer: 08_DEVELOPER_GOVERNANCE_LAYER → 02_API_GOVERNANCE
Profile Type: Webhook & Event-Driven Architecture Implementation
Status: Authoritative Implementation Profile

## Purpose

Define enforceable governance standards for webhook and event-driven APIs within enterprise, SaaS, startup, and developer environments.

This profile operationalizes the [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md) specifically for asynchronous event systems and ensures:

- Event signature verification preventing forged webhooks
- Delivery reliability with idempotency guarantees
- Subscriber authorization for sensitive events
- Audit traceability for regulatory compliance
- Deployment gating before production release

**This is an enforcement profile, not an event systems tutorial.**

## Architectural Position

- **Parent Standard:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **Enforcement Model:** [API_ENFORCEMENT_MATRIX.md](../API_ENFORCEMENT_MATRIX.md)
- **Mapping Authority:** [API_CONTROL_MAPPING_APPENDIX.md](../API_CONTROL_MAPPING_APPENDIX.md)
- **Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
- **Control Authority Relationship:** Implements root standard controls using webhook patterns

**Applies to:**

- Webhook delivery systems
- Event notification APIs
- Async event processing
- Message brokers (Kafka, RabbitMQ, SQS)
- Real-time data pipelines
- SaaS subscription events

**Mandatory for all webhook production systems.**

## Governance Principles

- **Signature Verification:** Every webhook must include HMAC signature; receiver must validate
- **Delivery Reliability:** Events must be delivered at-least-once with idempotency support
- **Subscriber Authorization:** Webhook endpoints must be registered and approved before events sent
- **Audit Trail:** Every webhook event logged with delivery status, retries, errors
- **Event Schema:** Events must conform to published schema; unknown fields handled gracefully
- **Timeout Enforcement:** Webhook handlers must respond within SLA (3 seconds default)
- **Deployment Gating:** Deployment without governance validation gates is non-compliant

## Webhook & Event-Driven Governance Requirements

### 1. Webhook Signature Verification (MANDATORY)

**Every webhook must include HMAC-SHA256 signature:**

```http
POST https://customer.example.com/webhooks/payment HTTP/1.1
Content-Type: application/json
Svix-ID: msg_123456
Svix-Signature: v1,ivmLMHJ7zNk6RY3e32JaUTVqErGa9bJc8a3c+4MF1qI=
Svix-Timestamp: 1614613200

{
  "type": "payment.completed",
  "data": {
    "payment_id": "pay_123",
    "amount": 10000,
    "currency": "USD"
  }
}
```

**Signature format:** `v1,<base64(HMAC-SHA256(secret, timestamp.payload))>`

**Example (Node.js verification):**

```javascript
const crypto = require("crypto");

function verifyWebhookSignature(req, webhookSecret) {
  const timestamp = req.headers["svix-timestamp"];
  const signature = req.headers["svix-signature"];
  const body = req.rawBody; // Raw bytes before JSON parsing

  // 1. Verify timestamp (prevent replay: max 5 min old)
  const now = Math.floor(Date.now() / 1000);
  if (Math.abs(now - parseInt(timestamp)) > 300) {
    throw new Error("Timestamp too old; possible replay attack");
  }

  // 2. Verify signature
  const signedContent = `${timestamp}.${body}`;
  const hmac = crypto
    .createHmac("sha256", webhookSecret)
    .update(signedContent)
    .digest("base64");

  const expectedSignature = `v1,${hmac}`;
  if (!crypto.timingSafeEqual(signature, expectedSignature)) {
    throw new Error("Invalid signature; webhook forged");
  }

  return true;
}

app.post(
  "/webhooks/payment",
  express.raw({ type: "application/json" }),
  (req, res) => {
    try {
      verifyWebhookSignature(req, process.env.WEBHOOK_SECRET);
      const event = JSON.parse(req.body);

      // Process event
      res.status(200).send({ success: true });
    } catch (err) {
      res.status(403).send({ error: "Webhook verification failed" });
    }
  },
);
```

**Python verification:**

```python
import hmac
import hashlib
from datetime import datetime, timedelta

def verify_webhook_signature(headers, body_bytes, webhook_secret):
    timestamp = headers.get('svix-timestamp')
    signature = headers.get('svix-signature')

    # 1. Verify timestamp
    msg_timestamp = int(timestamp)
    now = int(datetime.now().timestamp())
    if abs(now - msg_timestamp) > 300:  # 5 minutes
        raise ValueError('Timestamp too old')

    # 2. Verify signature
    signed_content = f"{timestamp}.{body_bytes.decode()}"
    hmac_object = hmac.new(
        webhook_secret.encode(),
        signed_content.encode(),
        hashlib.sha256
    )
    expected_signature = f"v1,{hmac_object.digest().hex()}"

    if not hmac.compare_digest(signature, expected_signature):
        raise ValueError('Invalid signature')

    return True
```

### 2. Delivery Reliability & Idempotency (MANDATORY)

**Webhooks must be delivered at-least-once with idempotency:**

```javascript
// Producer: Send webhook with idempotency key
const webhookId = crypto.randomUUID(); // Unique per event
const idempotencyKey = `event_${webhookId}`;

await sendWebhook({
  url: subscriberUrl,
  body: event,
  headers: {
    "idempotency-key": idempotencyKey,
    "svix-id": webhookId,
  },
});

// Consumer: Handle idempotent delivery
async function handleWebhook(req, res) {
  const idempotencyKey = req.headers["idempotency-key"];

  // 1. Check if already processed
  const existingResult = await db.getWebhookResult(idempotencyKey);
  if (existingResult) {
    return res.status(200).json(existingResult); // Return cached result
  }

  // 2. Process webhook (first time)
  const result = await processEvent(req.body);

  // 3. Cache result
  await db.cacheWebhookResult(idempotencyKey, result);

  res.status(200).json(result);
}
```

**Retry policy (exponential backoff):**

```
Attempt 1: immediate
Attempt 2: 5 seconds later
Attempt 3: 30 seconds later
Attempt 4: 2 minutes later
Attempt 5: 10 minutes later
Max: 5 retries over ~13 minutes
```

**HTTP status code expectations:**

| Status           | Meaning                         | Retry? |
| ---------------- | ------------------------------- | ------ |
| 2xx              | Success; stop retrying          | No     |
| 4xx (except 408) | Client error; permanent failure | No     |
| 408              | Timeout; retry                  | Yes    |
| 5xx              | Server error; retry             | Yes    |
| No response      | Network error; retry            | Yes    |

### 3. Subscriber Authorization (MANDATORY)

**Webhook endpoints must be registered and approved:**

```javascript
// 1. Subscriber registers webhook
POST /webhooks HTTP/1.1
{
  "url": "https://customer.example.com/webhooks/payment",
  "events": ["payment.completed", "payment.failed"],
  "description": "Payment notifications"
}

// 2. System sends verification challenge
POST https://customer.example.com/webhooks/payment HTTP/1.1
{
  "type": "webhook.verify",
  "challenge": "verify_abc123xyz"
}

// 3. Subscriber must echo challenge to complete registration
POST /webhooks/verify HTTP/1.1
{
  "challenge": "verify_abc123xyz"
}

// 4. Webhook endpoint approved and marked as active
```

**Example (Verification handling):**

```javascript
app.post("/webhooks/payment", async (req, res) => {
  const event = req.body;

  // Handle verification challenge
  if (event.type === "webhook.verify") {
    return res.status(200).json({ challenge: event.challenge });
  }

  // Handle actual events
  if (event.type === "payment.completed") {
    // Process payment
    return res.status(200).json({ success: true });
  }

  // Unknown event type
  res.status(400).json({ error: "Unknown event type" });
});
```

**Event filters per subscriber:**

```javascript
// Subscriber registers only for specific events
{
  "url": "https://customer.example.com/webhooks/payment",
  "events": ["payment.completed"],  // Only this event
  "filters": {
    "currency": "USD",              // Only USD payments
    "amount_gte": 1000              // Only amounts >= $1000
  }
}
```

### 4. Event Schema & Versioning (MANDATORY)

**All events must conform to published schema:**

```json
{
  "type": "payment.completed",
  "id": "evt_123456",
  "created": "2024-01-15T10:30:45Z",
  "data": {
    "payment_id": "pay_123",
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_123"
  },
  "metadata": {
    "version": "1.0",
    "source": "payment-service",
    "trace_id": "trace_abc123"
  }
}
```

**Schema definition (JSONSchema):**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PaymentCompleted Event",
  "type": "object",
  "required": ["type", "id", "created", "data"],
  "properties": {
    "type": {
      "enum": ["payment.completed"]
    },
    "id": {
      "type": "string",
      "pattern": "^evt_[a-z0-9]{20}$"
    },
    "created": {
      "type": "string",
      "format": "date-time"
    },
    "data": {
      "type": "object",
      "required": ["payment_id", "amount", "currency"],
      "properties": {
        "payment_id": { "type": "string" },
        "amount": { "type": "integer", "minimum": 0 },
        "currency": { "type": "string", "pattern": "^[A-Z]{3}$" },
        "customer_id": { "type": "string" }
      },
      "additionalProperties": false // Reject unknown fields
    }
  }
}
```

**Versioning:**

```
v1 (Current): {"type": "payment.completed", "data": {...}}
v2 (New):     {"type": "payment.completed", "spec_version": "2.0", "data": {...}}

Deprecation: v1 supported until 2024-12-31
Migration: Customers must update subscribers by deprecation date
```

### 5. Event Logging & Audit Trail (MANDATORY)

**Every webhook event must be logged:**

```json
{
  "timestamp": "2024-01-15T10:30:45Z",
  "event_id": "evt_123456",
  "event_type": "payment.completed",
  "subscriber_url": "https://customer.example.com/webhooks/payment",
  "subscriber_id": "sub_123",
  "delivery_status": "success|failed|retrying",
  "http_status": 200,
  "attempt": 1,
  "duration_ms": 245,
  "error": null
}
```

**Webhook dashboard showing:**

- Event delivery status per subscriber
- Retry history
- Error details (HTTP status, timeout, network error)
- Manual retry capability
- Event payload inspection (for debugging)

### 6. Timeout Enforcement (MANDATORY)

**Webhook handlers must respond within SLA:**

```
Default SLA: 3 seconds
Maximum SLA: 30 seconds
Below SLA: Treated as timeout; triggers retry
```

**Example (Node.js with timeout):**

```javascript
async function deliverWebhook(url, payload, timeout = 3000) {
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify(payload),
      headers: { "Content-Type": "application/json" },
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (response.ok) {
      return { status: "delivered" };
    } else if (response.status >= 500) {
      return { status: "retry", reason: "server_error" };
    } else {
      return { status: "failed", reason: "client_error" };
    }
  } catch (err) {
    if (err.name === "AbortError") {
      return { status: "retry", reason: "timeout" };
    }
    return { status: "retry", reason: "network_error" };
  }
}
```

### 7. Event Rate Limiting (RECOMMENDED)

**Prevent subscriber exhaustion:**

```
Free Tier: 100 events/hour
Pro Tier: 10,000 events/hour
Enterprise: Unlimited
```

**Example:**

```javascript
async function sendWebhook(subscriberId, event) {
  const subscriber = await db.getSubscriber(subscriberId);
  const rateLimit = getRateLimit(subscriber.plan);

  const eventCountLastHour = await redis.get(`webhooks:${subscriberId}:hour`);

  if (eventCountLastHour >= rateLimit.max_events) {
    return { status: "rate_limited" };
  }

  await redis.incr(`webhooks:${subscriberId}:hour`);
  await redis.expire(`webhooks:${subscriberId}:hour`, 3600);

  // Deliver webhook...
}
```

## Severity Model

| Control                      | Severity    | Enforcement       |
| ---------------------------- | ----------- | ----------------- |
| **Signature Verification**   | MANDATORY   | BLOCKS deployment |
| **Idempotency**              | MANDATORY   | BLOCKS deployment |
| **Subscriber Authorization** | MANDATORY   | BLOCKS deployment |
| **Event Schema**             | MANDATORY   | BLOCKS deployment |
| **Logging**                  | MANDATORY   | BLOCKS deployment |
| **Timeout Enforcement**      | MANDATORY   | BLOCKS deployment |
| **Rate Limiting**            | RECOMMENDED | Warning logged    |

## Developer Checklist

Before deploying webhook system:

- [ ] **Signatures:** HMAC-SHA256 generated and validated on every webhook
- [ ] **Timestamp Validation:** Replay protection on all webhooks (max 5 min old)
- [ ] **Idempotency:** Idempotency key cached; duplicate events handled gracefully
- [ ] **Subscriber Registration:** Verification challenge required before activation
- [ ] **Event Schema:** Published schema; validation on send and receive
- [ ] **Logging:** JSON logs with event ID, status, duration, errors
- [ ] **Timeouts:** 3-second default SLA enforced; no hanging requests
- [ ] **Retry Policy:** Exponential backoff up to 5 retries over ~13 minutes
- [ ] **Dashboard:** Webhook delivery status visible to subscribers
- [ ] **CI/CD Gates:** Schema validation passed; signature tests passing

**Deployment without checklist completion is non-compliant.**

## Governance Implications

### Risk If Not Enforced

- **Forged Webhooks:** Without signature verification, attackers send fake events
- **Data Loss:** Without idempotency, events silently lost on retries
- **Unauthorized Subscribers:** Webhooks sent to unverified endpoints
- **Audit Gap:** Without logging, breach investigation impossible
- **System Overload:** Rate limiting prevents resource exhaustion

### Operational Impact

- **Developers:** 1-2 weeks to implement signature verification and idempotency
- **Operations:** Webhook delivery monitoring; dashboard support
- **Support:** Customer debugging via webhook inspection

## Official References

- **Root Authority:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **Webhook Security:** https://svix.com/docs/
- **AWS SNS:** https://docs.aws.amazon.com/sns/
- **CloudEvents:** https://cloudevents.io/ (event format standard)

## Version Information

| Element               | Value                                            |
| --------------------- | ------------------------------------------------ |
| **Document Version**  | 1.0 (Initial Release)                            |
| **Issue Date**        | 2024-Q1                                          |
| **Profile Type**      | Webhook & Event-Driven Architecture              |
| **Relation to EATGF** | Implements Layer 08, Domain 02 for async systems |
| **Next Review**       | Q2 2024                                          |
