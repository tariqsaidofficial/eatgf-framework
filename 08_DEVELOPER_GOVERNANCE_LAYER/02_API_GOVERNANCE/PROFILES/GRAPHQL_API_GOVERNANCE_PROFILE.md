# GraphQL API Governance Profile

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Profile Description

Enterprise AI-Aligned Technical Governance Framework (EATGF)
Version: 1.0
Layer: 08_DEVELOPER_GOVERNANCE_LAYER → 02_API_GOVERNANCE
Profile Type: GraphQL Architecture Implementation
Status: Authoritative Implementation Profile

## Purpose

Define enforceable governance standards for GraphQL APIs within enterprise, SaaS, startup, and developer environments.

This profile operationalizes the [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md) specifically for GraphQL-based systems and ensures:

- Query complexity control preventing resource exhaustion
- Field-level authorization preventing data leakage
- Secure subscription management for real-time APIs
- Introspection lockdown preventing reconnaissance attacks
- Audit traceability for regulatory compliance
- Deployment gating before production release

**This is an enforcement profile, not a GraphQL tutorial.**

## Architectural Position

- **Parent Standard:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **Enforcement Model:** [API_ENFORCEMENT_MATRIX.md](../API_ENFORCEMENT_MATRIX.md)
- **Mapping Authority:** [API_CONTROL_MAPPING_APPENDIX.md](../API_CONTROL_MAPPING_APPENDIX.md)
- **Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
- **Control Authority Relationship:** Implements root standard controls using GraphQL-specific patterns

**Applies to:**

- GraphQL public endpoints
- Internal data graphs
- Federation (Apollo Federation, Schema stitching)
- Real-time subscriptions
- SaaS multi-tenant GraphQL APIs

**Mandatory for all GraphQL production APIs.**

## Relationship to EATGF Layers

This profile implements controls from:

- **Layer 08 - Developer Governance Layer**
  - Domain 02: API Governance (primary - root authority)
  - Domain 01: Secure SDLC (field-level authorization, query validation patterns)
  - Domain 03: DevSecOps Governance (schema scanning, complexity analyzers, dependency management)

- **Layer 05 - Domain Frameworks**
  - API Governance Framework (control definitions apply universally)

- **Layer 03 - Governance Models**
  - Maturity Model (5-level progression from Ad Hoc to Optimized)
  - Performance Model (authorization policy effectiveness)

**Integration Points:**

- GraphQL field authorization enforces Secure SDLC authorization policies (Layer 08.01)
- Schema validation gates enforced by DevSecOps Governance CI/CD rules (Layer 08.03)
- Query complexity control tied to maturity progression (Layer 03)
- GraphQL threat model mapped to OWASP controls (Layer 05)

## Governance Principles

- **Query Complexity Limits:** Unbounded queries prohibited; depth + breadth limits enforced
- **Field-Level Authorization:** Every field must verify user access; no implicit trust
- **Subscription Security:** Real-time subscriptions must authenticate, authorize, rate-limit
- **Introspection Control:** Production introspection disabled; sensitive schema hidden
- **Error Information Leakage:** Error messages must never expose schema/implementation details
- **Batch Query Protection:** Prevent resource exhaustion via query batching
- **Dependency Tracking:** Document field-to-field authorization dependencies
- **Deployment Gating:** Deployment without governance validation gates is non-compliant

## Governance Conformance

This section demonstrates how GraphQL APIs implement each mandatory control from [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md). No new controls are defined here; this profile clarifies GraphQL-specific implementation patterns only.

### Control 1: Authentication (MANDATORY)

**Root Standard Requirement:**
> All APIs must explicitly authenticate every request using OAuth 2.0, OpenID Connect, mTLS, or equivalent.

**GraphQL Implementation Pattern:**
GraphQL queries are HTTP POST requests; authentication follows HTTP standards via Authorization header:

- Bearer token: `Authorization: Bearer <JWT>`
- JWT must include subject (`sub`) claiming user identity
- Subscriptions (WebSocket): Token passed in connection init message
- Gateway enforces authentication before query reaches GraphQL resolver

**Compliant Pattern:**

```graphql
POST /graphql HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInN1YiI6InVzZXItNDU2In0...
Content-Type: application/json

query {
  viewer {
    id
    email
  }
}
```

---

### Control 2: Authorization - Field-Level MANDATORY

**Root Standard Requirement:**
> Enforce authorization at resource level. Verify every request has permission to access specific data.

**GraphQL Implementation Pattern:**
GraphQL requires field-level authorization because queries can request any combination of fields:

- Resolver-level checks: Each field resolver verifies user can access this field
- Parent context: Authorization depends on parent object ownership
- Directives: `@auth`, `@requires` directives enforce policy
- Scopes: OAuth2 scopes limit available fields/mutations

**Compliant Pattern:**

```graphql
type Query {
  viewer: User @auth(requires: "authenticated")
}

type User {
  id: ID! @auth(requires: "authenticated")
  email: String! @auth(requires: "self_or_admin") # Only user or admin
  ssn: String! @auth(requires: "admin") # Admin only
  salary: Float! @auth(requires: "admin") # Admin only
}

# Resolve only grants email/ssn/salary if authorization check passes
```

---

### Control 3: Query Complexity & Rate Limiting (MANDATORY)

**Root Standard Requirement:**
> Enforce per-tier rate limits. Prevent resource exhaustion attacks.

**GraphQL Implementation Pattern:**
GraphQL needs depth/breadth/complexity limits because queries can be exponentially expensive:

- Depth limit: Max nesting level (e.g., depth ≤ 10)
- Breadth limit: Max fields per level (e.g., first: 50)
- Complexity score: Sum of field costs; max threshold per query
- Subscription limits: Max active subscriptions per user (e.g., 10)

**Compliant Pattern:**

```graphql
query {
  viewer {                      # Depth 1
    friends(first: 50) {        # Depth 2, breadth 50
      posts(first: 10) {        # Depth 3, breadth 10
        comments(first: 5) {    # Depth 4, breadth 5
          author { name }       # Depth 5
        }
      }
    }
  }
}
# Complexity score calculated; if > limit → 429 Too Many Requests
```

---

### Control 4: Introspection Control (MANDATORY)

**Root Standard Requirement:**
> Prevent reconnaissance attacks. Sensitive schema details must not be exposed.

**GraphQL Implementation Pattern:**

- Production introspection disabled: `introspectionFromSchema` returns empty
- Admin-only introspection: Behind authentication + authorization
- Schema documentation: Published separately via website/PDF
- Error messages: Never reveal type names or fields in error responses

**Compliant Pattern:**

```graphql
# Production: introspection query blocked
query IntrospectionQuery {
  __schema {
    types {
      name
    }
  }
}
# Response: { errors: [{ message: "Introspection disabled" }] }

# Development/Admin: introspection allowed
Authorization: Bearer <admin_token>
# Response: Full schema returned
```

---

### Control 5: Input Validation & Mutation Protection (MANDATORY)

**Root Standard Requirement:**
> Validate all inputs against declared schema. Reject requests with unknown fields or type mismatches.

**GraphQL Implementation Pattern:**

- GraphQL schema enforces type safety: `String!`, `Int!`, enums, custom scalars
- Custom scalars: Email, DateTime, UUID with format validation
- Input object validation: Required fields checked, unknown fields rejected
- Mutation-level guards: Mutations require explicit scopes/permissions

**Compliant Pattern:**

```graphql
input CreateUserInput {
  email: Email! @email # Custom scalar with format validation
  age: Int! @range(min: 0, max: 150)
  role: UserRole! # Enum: restricted set of values
}

type Mutation {
  createUser(input: CreateUserInput!): User @auth(requires: "admin")
}
```

---

### Control 6: Logging & Error Handling (MANDATORY)

**Root Standard Requirement:**
> Log all requests with correlation IDs, user ID, resource access, and authorization decisions.

**GraphQL Implementation Pattern:**

- Request ID: Passed through HTTP header, included in all logs
- Operation audit: Log query operation name, user, variables (sanitized)
- Authorization audit: Every field resolution logged (ALLOW/DENY)
- Error responses: Generic messages; detailed errors logged server-side only

**Compliant Pattern - Audit Log:**

```json
{
  "timestamp": "2024-02-14T10:00:00Z",
  "correlation_id": "corr-xyz789",
  "user_id": "user-456",
  "operation": "GetUserProfile",
  "fields_requested": ["id", "email", "posts"],
  "fields_granted": ["id", "email"],
  "fields_denied": [],
  "status": "PARTIAL_SUCCESS"
}
```

---

### Control 7: Schema Versioning (MANDATORY)

**Root Standard Requirement:**
> Breaking API changes prohibited without major version increment. Deprecated fields must have sunset dates.

**GraphQL Implementation Pattern:**

- Deprecation directive: `@deprecated(reason: "Use newField instead", version: "2.0")`
- Schema versioning: Versioned endpoint `/graphql/v1`, `/graphql/v2`
- SDL versioning: OpenAPI-like approach with `version` metadata
- Breaking change detection: CI/CD scans for breaking changes

**Compliant Pattern:**

```graphql
type User {
  id: ID!
  email: String!
  phone: String @deprecated(reason: "Use phoneNumbers field", version: "2.0")
  phone Numbers: [PhoneNumber!]! # New field for multi-phone support
}
```

---

### Control 8: Federation & Service Authorization (MANDATORY)

**Root Standard Requirement:**
> Service-to-service requires mutual TLS. No implicit trust between services.

**GraphQL Implementation Pattern:**

- Apollo Federation: Sub-graphs must validate requests come from authenticated gateways
- Service account validation: Each sub-graph verifies gateway identity via mTLS
- Cross-graph authorization: Federation routing respects authorization boundaries
- Token propagation: User context passed to sub-graphs; sub-graphs re-validate

**Compliant Pattern:**

```graphql
# Sub-graph never trusts gateway context implicitly
type Query {
  user(id: ID!): User @authenticated @requiresMTLS
}

# Resolver re-validates user ID from JWT token, not gateway assertion
```

---

## GraphQL Governance Requirements

### 1. Query Complexity Analysis (MANDATORY)

**Unbounded queries can exhaust resources:**

```graphql
# DoS Attack: Exponential query depth
{
  viewer {
    friends {
      friends {
        friends {
          friends {
            friends {
              profile {
                name
              }
            }
          }
        }
      }
    }
  }
}
```

**Mitigation:**

- Maximum query depth: 10 levels
- Maximum query breadth: 50 fields per level
- Complexity score per query: derived function of depth × breadth
- Mutations limited to 5 per request

**Example (Apollo GraphQL with complexity analysis):**

```javascript
const { graphqlHTTP } = require("express-graphql");
const depthLimit = require("graphql-depth-limit");
const { costAnalysis } = require("graphql-cost-analysis");

app.use(
  "/graphql",
  graphqlHTTP({
    schema: schema,
    rootValue: resolvers,

    // Query depth limit (max 10 levels)
    validationRules: [depthLimit(10)],

    // Query complexity scoring
    customValidationRules: [
      costAnalysis({
        variables: req.body.variables,
        complexity: {
          User: { complexity: 2 },
          friends: { complexity: 3 },
          profile: { complexity: 1 },
          posts: { args: { limit: "complexity" } },
        },
        defaultComplexity: 1,
        maximumComplexity: 500, // Max score per query
      }),
    ],
  }),
);
```

**Validated Example (Compliant):**

```graphql
{
  viewer {
    friends(first: 10) {
      # Limited
      edges {
        node {
          id
          name
        }
      }
    }
  }
}
```

### 2. Field-Level Authorization (MANDATORY)

**Every field must enforce authorization:**

```graphql
type User {
  id: ID! # Public
  name: String! # Public
  email: String! # RESTRICTED: requires viewer to be self or admin
  taxId: String! # RESTRICTED: tax-officer role only
  medicalHistory: [String] # RESTRICTED: medical-staff role only
}
```

**Example (Apollo authorization middleware):**

```javascript
const { mapSchema, getDirective, MapperKind } = require("@graphql-tools/utils");
const { defaultFieldResolver } = require("graphql");

function authDirectiveTransformer(schema) {
  return mapSchema(schema, {
    [MapperKind.OBJECT_FIELD]: (fieldConfig, fieldName, typeName) => {
      const authDirective = getDirective(schema, fieldConfig, "auth");
      if (authDirective) {
        const { requires } = authDirective;
        const originalResolve = fieldConfig.resolve || defaultFieldResolver;

        fieldConfig.resolve = async (source, args, context, info) => {
          // Check user role
          if (!context.user.roles.includes(requires)) {
            throw new Error(`Unauthorized: requires ${requires} role`);
          }
          return originalResolve(source, args, context, info);
        };
      }
      return fieldConfig;
    },
  });
}
```

**Schema with auth directives:**

```graphql
directive @auth(requires: String!) on FIELD_DEFINITION

type User {
  id: ID!
  name: String!
  email: String @auth(requires: "self_or_admin")
  taxId: String @auth(requires: "tax_officer")
  medicalRecords: [String] @auth(requires: "medical_staff")
}
```

### 3. Subscription Security (MANDATORY)

**Real-time subscriptions must be secured:**

```graphql
subscription onUserUpdated($userId: ID!) {
  userUpdated(id: $userId) {
    id
    name
    lastSeen
  }
}
```

**Mitigation:**

- Authentication required (same as queries/mutations)
- User can only subscribe to own resources
- Rate limiting per subscription (max 10 concurrent)
- Idle timeout after 5 minutes of no activity

**Example (Secure subscription resolver):**

```javascript
subscriptions: {
  userUpdated: {
    subscribe: (parent, { userId }, context, info) => {
      // 1. Verify authentication
      if (!context.user) {
        throw new Error("Authentication required");
      }

      // 2. Verify user can access this userId
      if (context.user.id !== userId && !context.user.isAdmin) {
        throw new Error("Unauthorized");
      }

      // 3. Rate limit subscriptions
      if (context.user.activeSubscriptions >= 10) {
        throw new Error("Too many active subscriptions");
      }

      // 4. Return subscription iterator
      return pubsub.asyncIterator([`USER_UPDATED_${userId}`]);
    };
  }
}
```

### 4. Introspection Control (MANDATORY)

**Production must disable introspection:**

```graphql
# This exposes entire schema; disabled in production
{
  __schema {
    types {
      name
      fields {
        name
      }
    }
  }
}
```

**Mitigation:**

- Introspection disabled in production
- Introspection enabled only for authenticated API consumers
- Disabled for unauthenticated clients
- Schema documentation provided via separate channel (OpenAPI export, documentation site)

**Example (Disable introspection):**

```javascript
const { NoSchemaIntrospectionCustomRule } = require("graphql");

app.use(
  "/graphql",
  graphqlHTTP({
    schema: schema,
    validationRules:
      process.env.NODE_ENV === "production"
        ? [NoSchemaIntrospectionCustomRule]
        : [],

    // OR per-user basis
    validationRules: context.user.isInternal
      ? []
      : [NoSchemaIntrospectionCustomRule],
  }),
);
```

### 5. Error Information Leakage (MANDATORY)

**Errors must never expose schema/implementation:**

```graphql
# WRONG: Exposes field names
{
  "errors": [{
    "message": "Cannot query field \"taxId\" on type \"User\"",
    "extensions": {
      "code": "GRAPHQL_PARSE_FAILED"
    }
  }]
}

# CORRECT: Generic error
{
  "errors": [{
    "message": "Invalid query",
    "extensions": {
      "code": "INVALID_REQUEST"
    }
  }]
}
```

**Mitigation:**

- Sanitize error messages in production
- Hide field names in validation errors
- Log full error server-side; return generic message to client
- Never expose stack traces

**Example:**

```javascript
app.use(
  "/graphql",
  graphqlHTTP({
    schema: schema,
    customFormatErrorFn: (error, context) => {
      if (process.env.NODE_ENV === "production") {
        // Log full error server-side
        logger.error({
          message: error.message,
          stack: error.stack,
          query: context.request.body,
        });

        // Return generic message to client
        return { message: "Internal server error" };
      }
      return error;
    },
  }),
);
```

### 6. Batch Query Protection (MANDATORY)

**Prevent resource exhaustion via batching:**

```javascript
// ATTACK: Send 100 queries at once
POST /graphql
[
  { query: "{ user { id name } }" },
  { query: "{ user { id name } }" },
  // ... x98 more
]
```

**Mitigation:**

- Maximum 5 queries per batch request
- Rate limiting applies to entire batch
- Total complexity score for batch cannot exceed limit

**Example:**

```javascript
app.post("/graphql", (req, res, next) => {
  const queries = Array.isArray(req.body) ? req.body : [req.body];

  // 1. Limit batch size
  if (queries.length > 5) {
    return res.status(400).json({
      error: "Maximum 5 queries per batch request",
    });
  }

  // 2. Validate complexity for entire batch
  let totalComplexity = 0;
  for (const query of queries) {
    totalComplexity += calculateComplexity(query);
  }
  if (totalComplexity > 1000) {
    return res.status(400).json({
      error: "Batch complexity exceeds limit",
    });
  }

  next();
});
```

### 7. Logging & Observability (MANDATORY)

**Must log all GraphQL operations:**

```json
{
  "timestamp": "2024-01-15T10:30:45Z",
  "correlation_id": "uuid",
  "user_id": "user123",
  "operation": "query|mutation|subscription",
  "operation_name": "GetUser",
  "query_complexity": 15,
  "fields_accessed": ["user.id", "user.name", "user.friends"],
  "execution_time_ms": 45,
  "status": "success|error",
  "error": null
}
```

**Example:**

```javascript
const logGraphQLOperation = (req, res, next) => {
  const startTime = Date.now();
  const correlationId = req.headers["x-correlation-id"] || uuid();

  res.on("finish", () => {
    const duration = Date.now() - startTime;
    const { query, variables, operationName } = req.body;

    logger.info({
      timestamp: new Date().toISOString(),
      correlation_id: correlationId,
      user_id: req.user?.id,
      operation_name: operationName,
      query_complexity: calculateComplexity(query),
      execution_time_ms: duration,
      status: res.statusCode < 400 ? "success" : "error",
    });
  });

  next();
};
```

### 8. Apollo Federation Security (MANDATORY for federated schemas)

**Sub-graph authorization must be enforced:**

```graphql
# Main gateway validates user
type User @key(fields: "id") {
  id: ID!
  name: String!
}

# Sub-graph enforces field-level auth
extend type User {
  orders: [Order] @auth(requires: "customer")
  medicalHistory: [String] @auth(requires: "medical")
}
```

**Mitigation:**

- Gateway validates authentication
- Gateway forwards user context to sub-graphs
- Sub-graphs re-validate authorization per field
- Sub-graphs never trust gateway context alone

## Severity & Maturity

**Severity Model and Maturity Progression are defined in [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md) and apply uniformly across all architecture profiles.**

GraphQL APIs inherit the standard 5-level maturity model and organizational profile severity escalation (Enterprise → SaaS → Startup → Developer).

## Control Mapping

**Framework mapping for GraphQL API controls is maintained in [API_CONTROL_MAPPING_APPENDIX.md](../API_CONTROL_MAPPING_APPENDIX.md). Do not duplicate mappings in architecture-specific profiles.**

## Developer Checklist

Before submitting GraphQL API for deployment:

- [ ] **Query Complexity:** Depth limit 10, breadth limit 50, complexity score < 500
- [ ] **Field Authorization:** Every protected field has @auth directive
- [ ] **Subscriptions:** Authentication, authorization, rate limiting (max 10 concurrent)
- [ ] **Introspection:** Disabled in production; enabled only for authenticated
- [ ] **Error Handling:** No field names in error messages; stack traces server-logged only
- [ ] **Batch Queries:** Max 5 queries per batch; total complexity validated
- [ ] **Logging:** JSON structured logs with correlation IDs; operation names recorded
- [ ] **Federation:** Sub-graphs re-validate user context; no implicit trust
- [ ] **Documentation:** Schema documentation published separate from introspection
- [ ] **CI/CD Gates:** Schema validation passed; complexity analyzer running

**Deployment without checklist completion is non-compliant.**

## Governance Implications

### Risk If Not Enforced

- **Query Complexity Attacks:** Unbounded queries exhaust database/compute resources (DoS)
- **Field-Level Breaches:** Users access fields they shouldn't (data leakage)
- **Subscription Abuse:** Millions of subscriptions exhaust memory
- **Schema Reconnaissance:** Introspection enables targeted attacks
- **Error Leakage:** Field names exposed in error messages enable enumeration

### Operational Impact

- **Developers:** Must add @auth directives to all sensitive fields (2–3 weeks per schema)
- **QA/Testing:** Query complexity testing, authorization matrix validation
- **Operations:** Monitor query complexity scores, subscription counts
- **Security:** Incident response enabled via correlation IDs

### Audit Consequences

- **ISO 27001:** A.8.2 authorization controls require field-level enforcement
- **SOC 2:** CC6 logical access requires field-level audit evidence
- **Data Protection:** GDPR Article 32 requires field-level encryption/access control

## Official References

- **Root Authority:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **Enforcement:** [<https://spec.graphql.org/>](../API_ENFORCEMENT_MATRIX.md)
- **GraphQL Spec:** <ht<https://www.apollographql.com/docs/apollo-server/security/>
- **Apollo Security:** <https://www.apollographql.com/docs/apollo-server/security/>
- **OWASP:** OWASP GraphQL Cheat Sheet
- **ISO/IEC 27001:2022:** Annex A

## Version Information

| Element               | Value                                              |
| --------------------- | -------------------------------------------------- |
| **Document Version**  | 1.0 (Initial Release)                              |
| **Issue Date**        | 2024-Q1                                            |
| **Profile Type**      | GraphQL Architecture Implementation                |
| **Relation to EATGF** | Implements Layer 08, Domain 02 for GraphQL systems |
| **Next Review**       | Q2 2024                                            |
