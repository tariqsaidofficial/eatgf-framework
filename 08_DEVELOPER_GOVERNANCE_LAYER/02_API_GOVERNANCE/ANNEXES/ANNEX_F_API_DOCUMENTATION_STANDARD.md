# API Documentation & Specification Standard

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Purpose

Defines requirements for API documentation, specification formats, and developer experience.

Ensures APIs are discoverable, understandable, and implementable.

## Architectural Position

Layer: 08_DEVELOPER_GOVERNANCE_LAYER
Sub-Layer: 02_API_GOVERNANCE
Authority: Subordinate to API_GOVERNANCE_STANDARD.md
Control Reference: SDLC-DOCS-06

## Governance Principles

- OpenAPI 3.0+ specification mandatory
- Machine-readable format (YAML / JSON)
- Every endpoint documented
- Error responses documented
- Authentication scheme documented
- Rate limits documented
- Deprecation notices visible
- SDK generation automated

## Technical Implementation

### 1. OpenAPI 3.0 Specification (MANDATORY)

```yaml
openapi: 3.0.3
info:
  title: User API
  version: 1.0.0
  description: Manage user accounts
  x-logo: https://example.com/logo.png

servers:
  - url: https://api.example.com/v1
    description: Production

paths:
  /users:
    get:
      summary: List all users
      operationId: listUsers
      parameters:
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            default: 10
      responses:
        "200":
          description: List of users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/User"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "429":
          $ref: "#/components/responses/RateLimitError"

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
          format: email
        created_at:
          type: string
          format: date-time
      required:
        - id
        - email

  responses:
    UnauthorizedError:
      description: Authentication required
    RateLimitError:
      description: Rate limit exceeded
      headers:
        X-RateLimit-Reset:
          schema:
            type: integer
```

### 2. AsyncAPI for Event APIs (if applicable)

```yaml
asyncapi: 2.0.0
info:
  title: User Events
  version: 1.0.0

channels:
  user/events:
    publish:
      message:
        $ref: "#/components/messages/UserEvent"

components:
  messages:
    UserEvent:
      payload:
        type: object
        properties:
          event:
            type: string
            enum: [created, updated, deleted]
          user_id:
            type: string
```

### 3. Protobuf for gRPC Services (if applicable)

```protobuf
syntax = "proto3";

package user.v1;

service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(ListUsersRequest) returns (UserList);
}

message User {
  string id = 1;
  string email = 2;
  int64 created_at = 3;
}
```

### 4. Changelog / Release Notes (MANDATORY)

```markdown
# Changelog

## v2.0.0 - 2024-02-14

### Added

- OIDC authentication support
- Webhook events for user lifecycle

### Changed

- `/users/{id}` response includes `last_login` field
- Rate limits increased to 1000/min for Professional tier

### Deprecated

- API key authentication (use OAuth2 instead)
- `/v1/users/search` endpoint (use `/v2/users?q=...`)

### Removed

- Legacy XML response format

### Fixed

- Fixed race condition in concurrent updates
```

### 5. Code Examples (MANDATORY)

```python
# Example: Creating a user
import requests

response = requests.post(
    "https://api.example.com/v1/users",
    headers={"Authorization": "Bearer YOUR_TOKEN"},
    json={"email": "user@example.com"}
)

user = response.json()
print(f"Created user: {user['id']}")
```

## Documentation Checklist

- [ ] OpenAPI 3.0+ specification
- [ ] JSON & YAML formats
- [ ] Every endpoint documented
- [ ] Every error response documented
- [ ] Authentication scheme documented
- [ ] Rate limit tiers documented
- [ ] Code examples in 2+ languages
- [ ] Changelog up-to-date
- [ ] Deprecation notices clear
- [ ] SDK auto-generated

## Control Mapping

| Framework        | Reference                         |
| ---------------- | --------------------------------- |
| ISO 27001:2022   | A.8.29 (Testing)                  |
| NIST SSDF        | PO.5 (Requirements documentation) |
| OWASP API Top 10 | API9 (Improper inventory)         |

## Developer Checklist

- OpenAPI spec committed to repo
- Spec validates against standard
- Spec linked in README
- Auto-generated docs deployed
- SDK generation automated
- Changelog updated per release
- API portal accessible
- Developer guide published

## Governance Implications

Poor documentation = support burden.
Undocumented APIs = adoption failures.

## Official References

- OpenAPI 3.0 Specification
- AsyncAPI 2.0 Specification
- Protocol Buffers 3
- RFC 3986 (URI Standard)

## Version

Version: 1.0
Status: Authoritative Annex
Layer: 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
Classification: Public Governance Standard
