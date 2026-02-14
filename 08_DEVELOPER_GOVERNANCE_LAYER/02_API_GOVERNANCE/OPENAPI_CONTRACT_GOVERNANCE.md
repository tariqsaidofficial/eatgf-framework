# OpenAPI Contract Governance

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 02_API_GOVERNANCE
**Governance Scope:** Implementation Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE

**Governance Scope:** OpenAPI specification standards, contract-first development, and validation.

**Control Authority Relationship:** Implements:

- Layer 02: API Security Controls
- Layer 04: Information Security Policy
- OpenAPI Specification 3.1

## Purpose

This standard defines mandatory requirements for OpenAPI contract definition, versioning, and validation. It covers:

- Contract-first API development
- OpenAPI specification requirements
- Schema validation and linting
- Contract testing and enforcement
- Documentation generation

## Governance Principles

- **Control-Centric Architecture:** API contracts enforce security and data validation controls
- **Security-by-Design:** Security requirements defined in contract
- **Developer-Operational Alignment:** Contracts facilitate client-server agreement
- **Audit Traceability:** Contracts version-controlled and reviewed

## Contract-First Development

**Requirement:** API contracts must be defined before implementation.

**Developer Requirements:**

- Define OpenAPI specification before writing code
- Review and approve specification with stakeholders
- Use specification to generate server stubs or client SDKs
- Validate implementation against specification using automated testing

**Benefits:**

- Clear contract between API provider and consumers
- Early identification of design issues
- Automated validation of implementation
- Auto-generated documentation

## OpenAPI Specification Requirements

### Mandatory Metadata

**Requirement:** All OpenAPI specifications must include complete metadata.

**Required Fields:**

```yaml
openapi: 3.1.0
info:
  title: User Management API
  version: 1.0.0
  description: API for managing user accounts and profiles
  contact:
    name: API Support
    email: api-support@example.com
    url: https://example.com/support
  license:
    name: Proprietary
servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://api-staging.example.com/v1
    description: Staging
```

### Security Schemes

**Requirement:** All authentication mechanisms must be documented in `securitySchemes`.

**Example:**

```yaml
components:
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.example.com/oauth/authorize
          tokenUrl: https://auth.example.com/oauth/token
          scopes:
            read:users: Read user information
            write:users: Modify user information
            admin: Administrative access
security:
  - OAuth2:
      - read:users
```

**Developer Requirements:**

- Define all security schemes used by the API
- Apply global or endpoint-level security requirements
- Document required scopes or permissions

### Schema Definitions

**Requirement:** All request and response bodies must reference defined schemas.

**Developer Requirements:**

- Define reusable schemas in `components/schemas`
- Use strong typing (avoid `type: object` without properties)
- Define validation constraints (minLength, maxLength, pattern, enum)
- Use `required` fields appropriately
- Include examples for complex schemas

**Example Schema:**

```yaml
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
        - username
      properties:
        id:
          type: string
          format: uuid
          example: "a1b2c3d4-e5f6-7890-abcd-1234567890ab"
        email:
          type: string
          format: email
          example: "user@example.com"
        username:
          type: string
          minLength: 3
          maxLength: 20
          pattern: "^[a-zA-Z0-9_-]+$"
          example: "john_doe"
        createdAt:
          type: string
          format: date-time
          example: "2026-02-14T12:34:56Z"
```

### Error Responses

**Requirement:** All error responses must be documented.

**Developer Requirements:**

- Document all possible HTTP status codes per endpoint
- Define error response schema (RFC 7807 recommended)
- Include examples of error responses

**Example:**

```yaml
paths:
  /users/{userId}:
    get:
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
```

### Request and Response Examples

**Requirement:** Provide examples for all requests and responses.

**Developer Requirements:**

- Include realistic examples that could be used for testing
- Cover both success and error scenarios
- Examples should match the defined schema

## OpenAPI Linting and Validation

**Requirement:** All OpenAPI specifications must pass validation and linting.

**Developer Requirements:**

- Use Spectral or equivalent linter
- Enforce organizational ruleset
- Integrate linting into CI/CD pipeline
- Block merges if linting fails

**Linting Rules:**

- No empty descriptions
- All operations have operationId
- All paths have summaries
- All schemas have examples
- No unused schemas
- Security schemes defined for protected endpoints

**Validation:**

- Specification must be valid OpenAPI 3.x
- All `$ref` references resolve correctly
- No circular dependencies in schemas

## Contract Testing

**Requirement:** Validate API implementation against OpenAPI contract.

**Developer Requirements:**

- Use contract testing tools (e.g., Prism, Dredd, Schemathesis)
- Run contract tests in CI/CD pipeline
- Fail build if implementation deviates from contract
- Test both request validation and response validation

**Contract Testing Tools:**

- **Prism:** Mock server and validation proxy
- **Dredd:** HTTP API testing framework
- **Schemathesis:** Property-based testing from OpenAPI specs

## Breaking Change Detection

**Requirement:** Detect and prevent unintentional breaking changes.

**Developer Requirements:**

- Use API diff tools (e.g., openapi-diff, oasdiff)
- Compare new spec against previous version
- Flag breaking changes in code review
- Require version bump for breaking changes

**Breaking Changes:**

- Removing an endpoint
- Removing a required field from request
- Adding a required field to request
- Changing response structure
- Removing or renaming enum values

## Documentation Generation

**Requirement:** Generate API documentation from OpenAPI specification.

**Developer Requirements:**

- Use documentation generators (Swagger UI, Redoc, RapiDoc)
- Host documentation publicly for external APIs, internally for internal APIs
- Keep documentation in sync with specification (auto-generated)
- Include "Try it out" functionality for interactive testing

**Documentation Hosting:**

- Production API docs: `https://api.example.com/docs`
- Staging API docs: `https://api-staging.example.com/docs`

## Specification Storage and Version Control

**Requirement:** OpenAPI specifications must be version-controlled.

**Developer Requirements:**

- Store specification in Git repository alongside code
- Use conventional file naming: `openapi.yaml` or `openapi.json`
- Version specification using semantic versioning
- Tag releases with Git tags

**Repository Structure:**

```
/api
  /openapi
    openapi.yaml
  /src
    ...
```

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Contract Definition | A.8.26 | PO.1 | ASVS V13 | BAI03 |
| Schema Validation | A.8.26 | RV.1 | API4:2023 | BAI03 |
| Contract Testing | A.8.29 | RV.1 | ASVS V13 | BAI07 |
| Documentation | A.5.37 | PO.3 | - | MEA01 |

## Developer Checklist

Before implementing an API:

- [ ] OpenAPI 3.1 specification created
- [ ] All endpoints documented with request/response schemas
- [ ] Security schemes defined
- [ ] Error responses documented
- [ ] Examples provided for all schemas
- [ ] Specification passes linting validation
- [ ] Contract tests configured in CI/CD
- [ ] API documentation generated and hosted

## Governance Implications

**Risk if not implemented:**

- API contract violations leading to client failures
- Undocumented breaking changes causing integration issues
- Lack of input validation leading to security vulnerabilities
- Poor API discoverability and developer experience

**Operational impact:**

- Contract-first development reduces rework
- Automated contract testing catches bugs early
- Auto-generated docs reduce documentation drift

**Audit consequences:**

- OpenAPI contracts provide audit trail for API changes
- Demonstrates structured change management

**Cross-team dependencies:**

- API consumers rely on accurate contracts
- QA team uses contracts for test generation
- Security team reviews contracts for security requirements

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. API Governance Framework (Layer 05)
3. API Governance Implementation Standard
4. OpenAPI Contract Governance

## References

- OpenAPI Specification 3.1 (<https://spec.openapis.org/oas/latest.html>)
- Spectral OpenAPI Linter (<https://stoplight.io/open-source/spectral>)
- Swagger UI (<https://swagger.io/tools/swagger-ui/>)
- Redoc (<https://redocly.com/>)
- RFC 7807: Problem Details for HTTP APIs

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial OpenAPI contract governance standard |
