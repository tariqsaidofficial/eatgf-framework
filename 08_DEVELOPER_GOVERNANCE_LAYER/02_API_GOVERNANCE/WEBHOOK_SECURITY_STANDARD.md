# Webhook Security Standard

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 02_API_GOVERNANCE
**Governance Scope:** Implementation Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE

**Governance Scope:** Security requirements for webhook implementation, signature verification, and delivery guarantees.

**Control Authority Relationship:** Implements:

- Layer 02: API Security Controls
- Layer 04: Information Security Policy
- OWASP API Security Top 10

## Purpose

This standard defines mandatory security requirements for webhooks (event-driven HTTP callbacks). It covers:

- Webhook signature verification
- Replay attack prevention
- Idempotency and retry logic
- Webhook endpoint security
- Monitoring and logging

## Governance Principles

- **Security-by-Design:** Webhooks implement authentication and integrity controls
- **Control-Centric Architecture:** Prevents spoofing, replay, and tampering
- **Developer-Operational Alignment:** Clear implementation guidance
- **Audit Traceability:** All webhook deliveries logged

## Webhook Signature Verification

### HMAC Signature (REQUIRED)

**Requirement:** All webhook payloads must be signed using HMAC-SHA256.

**Developer Requirements (Webhook Provider):**

- Generate HMAC signature of webhook payload using shared secret
- Include signature in HTTP header: `X-Webhook-Signature` or `X-Hub-Signature-256`
- Include timestamp in header: `X-Webhook-Timestamp`
- Use secure random string as webhook secret (minimum 32 bytes)

**Signature Generation Algorithm:**

```
timestamp = current_unix_timestamp
payload_string = timestamp + "." + json_payload
signature = HMAC_SHA256(secret, payload_string)
header_value = "t=" + timestamp + ",v1=" + signature
```

**Example Header:**

```
X-Webhook-Signature: t=1707906000,v1=a3b2c1d4e5f6...
```

**Developer Requirements (Webhook Consumer):**

- Extract signature and timestamp from header
- Recompute HMAC using same algorithm
- Compare computed signature with received signature (constant-time comparison)
- Reject webhook if signatures do not match
- Reject webhook if timestamp is older than tolerance window (e.g., 5 minutes)

**Signature Verification Pseudocode:**

```python
def verify_webhook(payload, signature_header, secret):
    parts = signature_header.split(',')
    timestamp = extract_timestamp(parts)
    signature = extract_signature(parts)

    # Check timestamp freshness
    if current_time - timestamp > 300:  # 5 minutes
        raise WebhookError("Timestamp too old")

    # Recompute signature
    payload_string = f"{timestamp}.{payload}"
    expected_signature = hmac.new(secret, payload_string, hashlib.sha256).hexdigest()

    # Constant-time comparison
    if not hmac.compare_digest(signature, expected_signature):
        raise WebhookError("Invalid signature")

    return True
```

### Timestamp Validation (REQUIRED)

**Requirement:** Reject webhooks with stale timestamps to prevent replay attacks.

**Developer Requirements:**

- Include current Unix timestamp in webhook signature
- Consumer validates timestamp is within acceptable window (5 minutes recommended)
- Reject webhooks with timestamps in the future
- Reject webhooks with timestamps older than tolerance

**Rationale:** Even if attacker captures valid signed webhook, they cannot replay it after tolerance window expires.

## Webhook Secret Management

**Requirement:** Webhook secrets must be securely generated, stored, and rotated.

**Developer Requirements (Webhook Provider):**

- Generate cryptographically random secrets (minimum 256 bits / 32 bytes)
- Use separate secret per webhook consumer
- Store secrets in secret management system (e.g., AWS Secrets Manager, HashiCorp Vault)
- Never log or expose secrets in API responses
- Support secret rotation without service disruption

**Secret Rotation Process:**

1. Generate new secret
2. Provide new secret to consumer via secure channel
3. Sign webhooks with both old and new secrets during transition period (e.g., 7 days)
4. Consumer updates to new secret
5. Provider stops using old secret after transition period

**Developer Requirements (Webhook Consumer):**

- Store webhook secret in environment variables or secret management system
- Never hard-code secrets in source code
- Rotate secrets on defined schedule (e.g., every 90 days)

## Idempotency and Retry Logic

### Idempotency (REQUIRED)

**Requirement:** Webhook consumers must handle duplicate deliveries idempotently.

**Developer Requirements:**

- Use unique webhook event ID for deduplication
- Store processed event IDs in database with TTL (e.g., 7 days)
- If event ID already exists, acknowledge without reprocessing
- Design webhook handlers to be idempotent (safe to execute multiple times)

**Deduplication Pseudocode:**

```python
def handle_webhook(event_id, payload):
    if already_processed(event_id):
        return 200  # Already processed, acknowledge success

    process_webhook(payload)
    mark_as_processed(event_id)
    return 200
```

### Retry Logic (REQUIRED)

**Requirement:** Webhook providers must implement exponential backoff retry logic.

**Developer Requirements (Webhook Provider):**

- Retry failed deliveries with exponential backoff
- Maximum retry attempts: 3-5
- Backoff schedule: 1 minute, 5 minutes, 30 minutes
- Stop retrying after final attempt
- Provide webhook delivery status dashboard for monitoring
- Allow manual retry via dashboard or API

**Retry Decision:**

- Retry on network errors (connection timeout, DNS failure)
- Retry on HTTP 5xx errors
- Do not retry on HTTP 4xx errors (except 429 Too Many Requests)
- Do not retry if consumer returns 410 Gone (endpoint permanently disabled)

**Developer Requirements (Webhook Consumer):**

- Return `200 OK` only after successful processing
- Return `500 Internal Server Error` for transient failures (will be retried)
- Return `400 Bad Request` for malformed payload (will not be retried)
- Return `410 Gone` to disable webhook permanently

## Webhook Endpoint Security

**Requirement:** Webhook endpoints must be secured and validated.

**Developer Requirements (Webhook Consumer):**

- Use HTTPS for all webhook endpoints (TLS 1.2 or higher)
- Implement signature verification before processing payload
- Apply rate limiting to prevent abuse
- Validate payload structure and data types
- Implement authentication if supported by provider
- Use dedicated webhook endpoint (do not reuse user-facing APIs)

**Endpoint Configuration:**

- URL format: `https://api.example.com/webhooks/{provider}/{event-type}`
- Accept only POST requests
- Reject requests with missing or invalid signatures
- Return appropriate HTTP status codes

## Webhook Payload Security

**Requirement:** Minimize sensitive data in webhook payloads.

**Developer Requirements (Webhook Provider):**

- Include only necessary data in webhook payload
- Use resource identifiers instead of full objects where possible
- Do not include credentials, API keys, or tokens
- Consider encrypting sensitive fields (e.g., PII)
- Log payload delivery but redact sensitive fields

**Example Minimal Payload:**

```json
{
  "event_id": "evt_1234567890",
  "event_type": "user.created",
  "timestamp": 1707906000,
  "data": {
    "user_id": "usr_abcdef123456",
    "resource_url": "https://api.example.com/v1/users/usr_abcdef123456"
  }
}
```

**Rationale:** Consumer fetches full resource via API using authenticated request.

## Monitoring and Logging

**Requirement:** Log all webhook deliveries and failures.

**Developer Requirements (Webhook Provider):**

- Log: event ID, timestamp, target URL, HTTP status, response time, retry count
- Do not log: full payloads with sensitive data, webhook secrets
- Alert on high failure rates (e.g., >10% failed deliveries)
- Provide webhook delivery dashboard with filtering and search

**Developer Requirements (Webhook Consumer):**

- Log: event ID, timestamp, signature verification result, processing result
- Do not log: webhook secrets
- Monitor for signature verification failures (potential attack indicator)
- Alert on processing errors

## Webhook Registration and Management

**Requirement:** Provide secure webhook registration and management interface.

**Developer Requirements (Webhook Provider):**

- Allow consumers to register webhook URLs via authenticated API or dashboard
- Validate webhook URL format (must be HTTPS)
- Support webhook URL verification (e.g., send challenge request)
- Allow consumers to configure event subscriptions (specific event types)
- Provide webhook secret rotation interface
- Allow consumers to disable or delete webhooks

**Webhook Verification (Challenge-Response):**

When registering webhook:

1. Provider sends POST request to webhook URL with challenge token
2. Consumer responds with challenge token in response body
3. Provider confirms webhook URL is controlled by consumer

## Control Mapping

| EATGF Context          | ISO 27001:2022 | NIST SSDF | OWASP      | COBIT |
| ---------------------- | -------------- | --------- | ---------- | ----- |
| Signature Verification | A.8.24         | PS.1      | API2:2023  | DSS05 |
| Replay Prevention      | A.8.26         | PO.1      | API4:2023  | DSS05 |
| Secret Management      | A.8.24         | PS.2      | API2:2023  | DSS05 |
| Logging                | A.8.15         | RV.1      | API10:2023 | DSS05 |

## Developer Checklist

Before deploying webhooks:

**Webhook Provider:**

- [ ] HMAC-SHA256 signature implemented
- [ ] Timestamp included in signature
- [ ] Webhook secrets securely generated and stored
- [ ] Retry logic with exponential backoff implemented
- [ ] Webhook delivery logging implemented
- [ ] Webhook registration requires HTTPS URLs

**Webhook Consumer:**

- [ ] Signature verification implemented (constant-time comparison)
- [ ] Timestamp validation implemented (5-minute window)
- [ ] Idempotency using event ID deduplication
- [ ] Webhook endpoint uses HTTPS
- [ ] Rate limiting applied to webhook endpoint
- [ ] Webhook secret stored securely (not in code)

## Governance Implications

**Risk if not implemented:**

- Webhook spoofing (attacker sends fake events)
- Replay attacks (old webhooks replayed)
- Webhook secret exposure leading to unauthorized events
- Duplicate processing causing data inconsistencies

**Operational impact:**

- Signature verification prevents spoofing
- Idempotency prevents duplicate processing
- Retry logic ensures reliable delivery

**Audit consequences:**

- Webhook logs provide audit trail for event-driven actions
- Signature verification demonstrates authentication controls

**Cross-team dependencies:**

- Security team reviews webhook security architecture
- DevOps team configures webhook endpoints and secrets
- Monitoring team sets up alerting for webhook failures

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. API Governance Framework (Layer 05)
3. Information Security Policy (Layer 04)
4. Webhook Security Standard

## References

- OWASP API Security Top 10 (<https://owasp.org/www-project-api-security/>)
- GitHub Webhook Security (<https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries>)
- Stripe Webhook Security (<https://stripe.com/docs/webhooks/signatures>)
- NIST SP 800-107: Recommendation for Applications Using Approved Hash Algorithms

## Version History

| Version | Date       | Change Type | Description                       |
| ------- | ---------- | ----------- | --------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial webhook security standard |
