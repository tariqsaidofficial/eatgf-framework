# API Gateway Governance Standard

## Purpose

API Gateways function as unified entry points for all service-to-service and client-to-service communication. This standard establishes mandatory governance controls ensuring that gateways enforce authentication, authorization, rate limiting, request validation, and audit logging before traffic reaches backend services. Gateways serve as the primary enforcement checkpoint for API governance policies.

---

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Governance Scope:** 02_API_GOVERNANCE
**Document Type:** Root Authority Standard
**Control Authority Relationship:** Defines mandatory gateway controls that all API proxies must implement
**Applicable Profiles:** Enterprise, SaaS, Startup, Developer

---

## Governance Principles

- **Defense in Depth:** API Gateway enforces controls before backend exposure; services assume gateway validation
- **Centralized Policy:** All gateway policies auditable, versioned, and managed through GitOps
- **Control-Centric Architecture:** Every gateway control maps to specific SDLC/API security requirements
- **Zero Trust at Entry:** Gateways verify ALL requests (no implicit trust) regardless of source network
- **Audit Traceability:** All gateway decisions (accept/reject/modify) logged with full context
- **Developer Experience:** Policy enforcement transparent; developers understand failure reasons

---

## Mandatory Gateway Controls

### 1. Request Validation & Transformation

**Requirement:** API Gateway must validate all incoming requests against declared schemas before forwarding to backend services.

**Control Elements:**

- Request body schema validation (JSON/XML/Protocol Buffers)
- Header validation (required headers, type constraints)
- Query parameter validation with bounds checking
- Path parameter type enforcement (integers, UUIDs, enums)
- Request size limits (prevent DoS via oversized payloads)
- Content-type restrictions based on endpoint definition

**Production Example - Kong with Schema Enforcement:**

```lua
-- Kong Request Validation Plugin
local plugin = {
  name = "request-validation",
  handler = {
    access = function(self)
      local content_type = ngx.var.content_type
      local body = ngx.req.get_body_data()

      -- Schema validation
      if not self:validate_json_schema(body, self.config.schema) then
        return ngx.exit(ngx.HTTP_BAD_REQUEST)
      end

      -- Size enforcement
      local content_length = tonumber(ngx.var.content_length) or 0
      if content_length > self.config.max_body_size then
        ngx.log(ngx.ERR, "Request exceeds max size: " .. content_length)
        return ngx.exit(ngx.HTTP_REQUEST_ENTITY_TOO_LARGE)
      end
    end
  }
}
```

**Audit Evidence:**

- Schema validation rules stored in service definitions
- Rejected request counts per endpoint per day
- Sample rejected requests (sanitized, no PII)

---

### 2. Authentication Enforcement

**Requirement:** API Gateway must authenticate all inbound requests using declared credential types before allowing backend communication.

**Control Elements:**

- Multiple authentication method support (API keys, OAuth 2.0, mTLS, JWT)
- Credential extraction and validation (headers, cookies, query params forbidden)
- Token/credential format validation
- Invalid credential rejection with audit logging
- Authentication method routing per endpoint
- Credential refresh coordination (prevent expired token forwarding)

**Production Example - Istio Authorization Policy with OIDC:**

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: api-gateway-authn
  namespace: api-gateway
spec:
  rules:
    - from:
        - source:
            requestPrincipals: ["*"]
      to:
        - operation:
            methods: ["GET", "POST", "PUT", "DELETE"]
            paths: ["/api/v1/*"]
  provider:
    name: "oidc"
---
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: gateway-oidc
  namespace: api-gateway
spec:
  jwtRules:
    - issuer: "https://auth.company.com"
      jwksUri: "https://auth.company.com/.well-known/jwks.json"
      audiences: "api-gateway"
      forwardOriginalToken: true
```

**Audit Evidence:**

- Authentication method per endpoint (enforced in gateway config)
- Failed authentication attempt counts (timestamp, endpoint, credential type)
- Authentication latency percentiles (P50, P95, P99)

---

### 3. Authorization & Access Control

**Requirement:** API Gateway must enforce fine-grained authorization, ensuring authenticated identities have permission to access requested resources.

**Control Elements:**

- Role-based access control (RBAC) per endpoint/resource
- Attribute-based access control (ABAC) for dynamic validation
- Resource ownership verification (user can only access own resources)
- Scope validation (OAuth scope claims vs. endpoint requirements)
- Authorization decision logging with decision rationale
- Graceful denial with 403 Forbidden + audit trail

**Production Example - AWS API Gateway with Lambda Authorizer:**

```python
# Lambda Authorizer for fine-grained authz
import json
import jwt
import boto3

def lambda_handler(event, context):
    token = event['authorizationToken']
    method_arn = event['methodArn']

    try:
        # Decode JWT
        payload = jwt.decode(token, algorithms=['RS256'],
                           options={"verify_signature": False})

        user_id = payload['sub']
        scopes = payload.get('scope', '').split()

        # Extract resource from ARN
        arn_parts = method_arn.split(':')
        resource_id = arn_parts[-1].split('/')[-1]

        # Verify ownership
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('api_resources')
        response = table.get_item(Key={'id': resource_id})

        if response.get('Item', {}).get('owner_id') != user_id:
            raise Exception('Unauthorized')

        # Verify scope
        required_scope = 'api:write' if method_arn.endswith('POST') else 'api:read'
        if required_scope not in scopes:
            raise Exception('Insufficient scope')

        return generate_policy(user_id, 'Allow', method_arn)

    except Exception as e:
        return generate_policy('user', 'Deny', method_arn)

def generate_policy(principal_id, effect, resource):
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': resource
            }]
        }
    }
```

**Audit Evidence:**

- Authorization rules per endpoint (stored in gateway configuration)
- Access denial counts (timestamp, user, endpoint, reason)
- Permission change audit trail (who granted/revoked, when, why)

---

### 4. Rate Limiting & Quota Management

**Requirement:** API Gateway must enforce rate limits and quotas per client/user/API plan to prevent resource exhaustion and ensure fair resource allocation.

**Control Elements:**

- Per-client rate limiting (API key, OAuth client, IP)
- Per-user rate limiting (authenticated identity)
- Distributed rate limiting (across gateway instances)
- Quota management (daily/monthly limits)
- Burst allowance with backoff
- Graceful degradation (429 Too Many Requests with Retry-After)
- Rate limit headers in responses (X-RateLimit-\*)

**Production Example - Kong Rate Limiting with Redis:**

```yaml
# Kong Rate Limiting Configuration
_format_version: "3.0"
services:
  - name: api-backend
    host: backend.internal
    port: 8080
    routes:
      - name: api-v1
        paths:
          - /api/v1
        plugins:
          - name: rate-limiting
            config:
              minute: 1000
              hour: 50000
              day: 500000
              policy: redis
              redis_host: redis-cluster.internal
              redis_port: 6379
              fault_tolerant: true
              hide_client_headers: false
          - name: response-ratelimit-headers
            config:
              header_name: X-RateLimit-Limit
              limit_by: consumer

      # Quota tracking for OAuth scopes
      - name: quota-enforcement
        paths:
          - /api/v1/premium
        plugins:
          - name: rate-limiting
            config:
              minute: 5000
              policy: redis
              break_on_exceed: true
```

**Audit Evidence:**

- Rate limit configuration per API/endpoint (with effective dates)
- Rate limit exceeding incidents (counts per client, timestamp)
- Quota utilization trends (peak usage, daily patterns)

---

### 5. Request/Response Logging & Audit Trail

**Requirement:** API Gateway must log all request decisions, authentication/authorization outcomes, rate limit violations, and responses for audit and troubleshooting.

**Control Elements:**

- Complete request logging (method, path, headers subset, timestamp)
- Authentication outcome logging (success/failure reason)
- Authorization logging (decision, required vs. granted permissions)
- Response status and latency logging
- Sensitive data sanitization (no passwords, API keys, PII in logs)
- Structured logging (JSON) for automated analysis
- Log retention per organizational requirements
- Correlation ID propagation for distributed tracing

**Production Example - Fluent Bit to Elasticsearch:**

```yaml
# Fluent Bit: Gateway to Elasticsearch
[SERVICE]
  Flush         5
  Daemon        off
  Log_Level     info

[INPUT]
  Name              systemd
  Tag               gateway.access
  Read_From_Tail    On
  Strip_Underscores On

[FILTER]
  Name                modify
  Match               gateway.access
  Add                 environment prod
  Copy                _HOSTNAME gateway_instance

[FILTER]
  Name                parser
  Match               gateway.access
  Key_Name            MESSAGE
  Parser              gateway_json
  Preserve_Key        On

[PARSER]
  Name        gateway_json
  Format      json
  Time_Key    timestamp
  Time_Format %Y-%m-%dT%H:%M:%S.%LZ

[OUTPUT]
  Name            es
  Match           gateway.*
  Host            elasticsearch.internal
  Port            9200
  HTTP_User       gateway_user
  HTTP_Passwd     ${ELASTICSEARCH_PASSWORD}
  Index           gateway-access-%Y.%m.%d
  Type            _doc
  Retry_Limit     5
  Trace_Error     On
```

**Sanitization Rules (Python):**

```python
def sanitize_log_entry(entry):
    """Remove sensitive data from gateway logs"""
    sensitive_headers = [
        'authorization', 'x-api-key', 'cookie', 'x-auth-token',
        'x-api-secret', 'x-access-token'
    ]

    # Sanitize headers
    for header in sensitive_headers:
        if header in entry.get('headers', {}):
            entry['headers'][header] = '***REDACTED***'

    # Sanitize token claims (log hash, not value)
    if 'jwt_claims' in entry:
        entry['jwt_claims_hash'] = hashlib.sha256(
            json.dumps(entry['jwt_claims']).encode()
        ).hexdigest()
        del entry['jwt_claims']

    # Redact query params containing sensitive keywords
    if 'query_params' in entry:
        for key in entry['query_params']:
            if any(kw in key.lower() for kw in ['password', 'secret', 'key', 'token']):
                entry['query_params'][key] = '***REDACTED***'

    return entry
```

**Audit Evidence:**

- Gateway access logs (retained per compliance policy: 90 days minimum)
- Authentication failure logs with reason (invalid format, expired, blacklisted)
- Authorization denial logs (resource, required scope, granted scope)
- Rate limit violation logs (client, endpoint, count)

---

### 6. Circuit Breaking & Fault Tolerance

**Requirement:** API Gateway must detect and isolate unhealthy backend services to prevent cascading failures and improve user experience during partial outages.

**Control Elements:**

- Automatic health checking (endpoint-specific, configurable interval)
- Circuit breaker state machine (Closed → Open → Half-Open)
- Failure threshold configuration (consecutive failures or error rate)
- Fast failover detection (configurable timeout)
- Graceful degradation (cached responses, fallbacks where applicable)
- Circuit state visibility in monitoring/dashboards
- Circuit state change logging

**Production Example - Istio Destination Rule with Circuit Breaking:**

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: backend-circuit-breaker
  namespace: api-gateway
spec:
  host: backend.api.svc.cluster.local
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 50
        maxRequestsPerConnection: 2
        h2UpgradePolicy: UPGRADE
    outlierDetection:
      consecutiveErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
      minRequestVolume: 10
      splitExternalLocalOriginErrors: true

      # Enhanced detection for specific error types
      consecutiveGatewayErrors: 3
      consecutiveLocalOriginFailures: 2

  # Per-subset circuit breaking (canary deployments)
  subsets:
    - name: stable
      labels:
        version: v1
      trafficPolicy:
        outlierDetection:
          consecutiveErrors: 5

    - name: canary
      labels:
        version: v2
      trafficPolicy:
        outlierDetection:
          consecutiveErrors: 2 # More aggressive for canary
```

**Health Check Configuration:**

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: backend-routing
spec:
  hosts:
    - backend.api.svc.cluster.local
  http:
    # Health checks before routing
    - match:
        - uri:
            prefix: /health
      route:
        - destination:
            host: backend.api.svc.cluster.local
            port:
              number: 8080
          timeout: 2s

    # Normal traffic with circuit breaker
    - route:
        - destination:
            host: backend.api.svc.cluster.local
            subset: stable
            port:
              number: 8080
          timeout: 30s
      retries:
        attempts: 3
        perTryTimeout: 10s
```

**Audit Evidence:**

- Circuit state transitions (timestamp, backend, trigger reason)
- Health check results (successful/failed, latency)
- Failover activation (backend, traffic redirected to)
- Circuit recovery events (backend brought back online)

---

### 7. Security Policy Enforcement

**Requirement:** API Gateway must enforce security policies including CORS, CSP, TLS version enforcement, and request/response headers that prevent common web vulnerabilities.

**Control Elements:**

- CORS policy management (allowed origins, methods, headers)
- TLS version enforcement (TLS 1.2+ only)
- Certificate validation for backend connections
- HTTP security headers (HSTS, X-Content-Type-Options, X-Frame-Options)
- Request/response header filtering
- SSL/TLS cipher suite enforcement
- HTTPS redirection enforcement

**Production Example - Traefik Security Middlewares:**

```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: api-gateway-security
spec:
  # TLS version enforcement
  plugin:
    apigateway-tls:
      minVersion: "1.2"
      cipherSuites:
        - TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        - TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305
        - TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305

  # CORS configuration
  headers:
    accessControlAllowOriginList:
      - https://app.company.com
      - https://admin.company.com
    accessControlAllowMethods:
      - GET
      - POST
      - PUT
      - DELETE
      - OPTIONS
    accessControlAllowHeaders:
      - Content-Type
      - Authorization
      - X-Requested-With
    accessControlMaxAge: 3600
    accessControlAllowCredentials: true

  # Security headers
  customResponseHeaders:
    X-Content-Type-Options: nosniff
    X-Frame-Options: DENY
    X-XSS-Protection: 1; mode=block
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
    Content-Security-Policy: "default-src 'self'; script-src 'self' trusted.cdn.com"
    Referrer-Policy: strict-origin-when-cross-origin

---
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: header-filtering
spec:
  plugin:
    header-filter:
      # Remove sensitive headers from requests
      removeHeaders:
        - X-Original-Authorization
        - X-Internal-Service-Key
      # Add security headers to responses
      addHeaders:
        X-API-Version: "1.0"
        X-Content-Type-Options: "nosniff"
```

**Audit Evidence:**

- CORS policy (effective dates, allowed origins)
- TLS certificate deployment (issuer, expiration, deployment date)
- Security header compliance (percentage of responses with required headers)
- Policy violations (blocked requests due to security policies)

---

### 8. Traffic Management & Routing

**Requirement:** API Gateway must intelligently route traffic based on declared policies, enabling canary deployments, A/B testing, and service migration.

**Control Elements:**

- Version-based routing (v1, v2, v3 concurrent support)
- Canary deployment routing (weighted traffic to new version)
- Blue-green deployment support
- Header-based routing (route based on User-Agent, custom headers)
- Geographic routing (geolocation-aware backend selection)
- Failure-based routing (fallback to alternate backends)
- Traffic mirroring for low-risk testing

**Production Example - Istio VirtualService with Canary:**

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api-v2-canary
  namespace: api-gateway
spec:
  hosts:
    - api.company.com
  http:
    # Route /api/v2 traffic with canary strategy
    - match:
        - uri:
            prefix: /api/v2
      route:
        - destination:
            host: api-backend-v2.internal
            subset: canary
            port:
              number: 8080
          weight: 10 # 10% to canary
        - destination:
            host: api-backend-v1.internal
            subset: stable
            port:
              number: 8080
          weight: 90 # 90% to stable
      timeout: 30s
      retries:
        attempts: 3

    # Mirror traffic for testing new version
    - match:
        - uri:
            prefix: /api/v1
      route:
        - destination:
            host: api-backend-v1.internal
            subset: stable
            port:
              number: 8080
      mirror:
        host: api-backend-v2.internal
        subset: canary
        port:
          number: 8080
      mirrorPercent: 5
      timeout: 30s

---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: api-backend-subsets
spec:
  host: api-backend-v1.internal
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 50
  subsets:
    - name: stable
      labels:
        version: v1
      trafficPolicy:
        loadBalancer:
          simple: ROUND_ROBIN
    - name: canary
      labels:
        version: v2-canary
      trafficPolicy:
        loadBalancer:
          simple: LEAST_REQUEST
```

**Audit Evidence:**

- Traffic routing rules (effective dates, canary percentages)
- Version migration schedule (when traffic shifted between versions)
- Canary success metrics (deployment date, error rate, latency impact)

---

## Organizational Profile Escalation

### Enterprise (Mandatory Controls: 1-8)

**Implemented:** All mandatory controls + circuit breaking + traffic management
**Additional Requirements:**

- Multi-region gateway deployment
- Active-active failover
- Rate limiting per customer organization
- Advanced ABAC with external policy engine
- Real-time threat detection and automatic mitigation
- Quarterly penetration testing of gateway policies

### SaaS (Mandatory Controls: 1-7)

**Implemented:** All mandatory controls except advanced traffic management
**Additional Requirements:**

- Multi-tenancy isolation enforcement
- Per-tenant rate limiting
- Per-tenant authentication method customization
- Audit logging with tenant segregation
- Monthly security policy review

### Startup (Mandatory Controls: 1-5)

**Implemented:** Request validation, authentication, authorization, rate limiting, logging
**Additional Requirements:**

- API-key based authentication (OAuth optional)
- Basic rate limiting per API key
- Weekly log analysis for security incidents

### Developer (Mandatory Controls: 1-4)

**Implemented:** Request validation, authentication, authorization, logging
**Additional Requirements:**

- Simplified gateway setup (cloud provider managed service)
- JWT token validation only
- Basic rate limiting

---

## Control Mapping to External Frameworks

| EATGF Control                      | ISO 27001:2022   | NIST SSDF | OWASP API Top 10                         | COBIT 2019 | NIST 800-53                           |
| ---------------------------------- | ---------------- | --------- | ---------------------------------------- | ---------- | ------------------------------------- |
| Request Validation                 | A.14.2.1         | PO2.2     | API5 (Broken Function Level AuthZ)       | DSS05.01   | SI-10 (Information System Monitoring) |
| Authentication Enforcement         | A.9.2.1, A.9.4.2 | PO4.1     | API6 (Broken Object Level AuthZ)         | DSS05.02   | AC-2 (Account Management)             |
| Authorization & Access Control     | A.9.2.5, A.9.4.3 | PO4.1     | API1 (Broken Object Level AuthZ)         | DSS05.03   | AC-3 (Access Enforcement)             |
| Rate Limiting & Quota              | A.12.6.1         | PO2.2     | API4 (Unrestricted Resource Consumption) | DSS05.04   | SI-4 (System Monitoring)              |
| Request/Response Logging           | A.12.4.1         | PO3.2     | API9 (Improper Inventory Management)     | MEA02.01   | AU-2 (Audit Events)                   |
| Circuit Breaking & Fault Tolerance | A.12.3.1         | PO2.2     | -                                        | DSS04.08   | SC-7 (Boundary Protection)            |
| Security Policy Enforcement        | A.13.1.1         | PO4.1     | API2 (Broken Authentication)             | DSS05.05   | AC-4 (Information Flow Enforcement)   |
| Traffic Management & Routing       | A.12.3.1         | PO2.2     | -                                        | DSS04.01   | SC-7 (Boundary Protection)            |

---

## Developer Checklist

- [ ] **Declare Gateway Technology:** Specify API Gateway platform (Kong, AWS API Gateway, Istio, Traefik, Azure API Management)
- [ ] **Request Validation Schema:** Create JSON Schema for all request body, query params, headers per endpoint
- [ ] **Authentication Configuration:** Specify credential type (API key, OAuth, mTLS, JWT) per endpoint; coordinate with OAuth/Identity profile
- [ ] **Authorization Rules:** Define RBAC/ABAC rules; verify token claims provide required attributes
- [ ] **Rate Limit Quotas:** Set minute/hour/day limits per API plan; coordinate with SLA documentation
- [ ] **Logging Configuration:** Verify logs forwarded to central system (Elasticsearch, CloudWatch, Stackdriver); confirm log retention policy
- [ ] **Circuit Breaker Configuration:** Set failure thresholds and timeout values; test with chaos engineering
- [ ] **Security Headers:** Verify all security headers present in responses (HSTS, CSP, X-Frame-Options)
- [ ] **TLS Configuration:** Verify TLS 1.2+ enforced; confirm certificate authority and renewal process
- [ ] **Health Check Endpoints:** Define health check paths; verify gateway queries them at configured interval
- [ ] **Canary Deployment Plan:** If rolling out new API version, define canary percentage and success metrics
- [ ] **Gateway Configuration Testing:** Validate test suite covers: auth success/failure, invalid input rejection, rate limit enforcement, security header presence
- [ ] **Runbook Documentation:** Create gateway incident response procedures (circuit breaker tripping, health check failures, authentication service outages)
- [ ] **Monitoring Dashboard:** Configure gateway metrics (request rate, authentication failures, authorization denials, latency percentiles)

---

## Governance Implications

**Risk if Not Implemented:**

- Unvalidated requests reach backend services → application crashes, data corruption
- Missing authentication enforcement → unauthorized access, data breaches
- No rate limiting → resource exhaustion, service denial of attack
- Missing audit logs → cannot detect intrusions or respond to incidents
- No circuit breaking → cascading failures across service mesh

**Operational Impact:**

- Gateway configuration changes require testing (impact on production traffic)
- High observability required (dashboard, alerting) to detect gateway issues early
- Incident response playbooks needed for circuit breaker activation
- Cross-team coordination: gateway team + backend teams + security team + identity team

**Audit Consequences:**

- Gateway configuration reviewed during ISO 27001 audits (Annex A.9, A.12, A.14 controls)
- Audit logs examined for evidence of access control enforcement
- Gateway health/reliability examined for business continuity assessment
- Traffic routing decisions auditable (especially for regulated compliance)

**Cross-Team Dependencies:**

- **Identity Team:** Coordinate OAuth provider deployment, token format, scope definitions
- **Backend Teams:** Coordinate health check endpoints, expected request formats, timeout values
- **Security Team:** Review rate limiting strategy, security header configuration, threat detection rules
- **SRE Team:** Monitor gateway performance, manage autoscaling policies, incident response

---

## References

- NIST SP 800-218: Secure Software Development Framework (SSDF) - Practice PO4.1, PO2.2
- OWASP API Top 10 2023: `https://owasp.org/www-project-api-security/`
- ISO/IEC 27001:2022 - Information Security Management Systems
- Kong API Gateway: `https://docs.konghq.com/`
- Istio: `https://istio.io/latest/docs/`
- COBIT 2019 - Framework for IT Governance - DSS04, DSS05, MEA02 domains

---

## Version & Authority

**Document Title:** API Gateway Governance Standard
**Version:** 1.0
**Release Date:** 2026-02-14
**Change Type:** Major (First Release)
**EATGF Baseline:** Block 2 API Governance Module
**Authority:** API Governance Root Authority
**Next Review Date:** 2026-05-14
**Compliance Status:** EATGF Signature Template Compliant ✅
