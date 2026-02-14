# API Versioning Standard

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 02_API_GOVERNANCE  
**Governance Scope:** Implementation Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE

**Governance Scope:** API versioning strategy, deprecation policy, and backward compatibility requirements.

**Control Authority Relationship:** Implements:

- Layer 02: Change Management Controls
- Layer 04: Version Governance Policy
- Layer 05: API Governance Framework

## Purpose

This standard defines mandatory requirements for API versioning, backward compatibility, and deprecation. It covers:

- Versioning strategy (URI, header, or content negotiation)
- Semantic versioning for APIs
- Breaking vs. non-breaking changes
- Deprecation and sunset policy
- Version support lifecycle

## Governance Principles

- **Control-Centric Architecture:** Versioning prevents breaking changes to API consumers
- **Developer-Operational Alignment:** Clear versioning strategy reduces integration issues
- **Audit Traceability:** Version changes tracked and documented
- **Single Source of Truth:** One active version per major release

## API Versioning Strategy

### URI-Based Versioning (RECOMMENDED)

**Requirement:** Use major version in URI path.

**Format:** `https://api.example.com/v{major}/resource`

**Example:**

- `https://api.example.com/v1/users`
- `https://api.example.com/v2/users`

**Rationale:**

- Simple and explicit
- Easy to test and debug
- Clear separation between versions
- Browser-friendly (no special headers required)

**Developer Requirements:**

- Include major version number in base path
- Do not include minor or patch versions in URI
- Each major version is independently deployable

### Header-Based Versioning (ALTERNATIVE)

**Requirement:** Use custom header or Accept header for versioning.

**Custom Header Example:**

```
GET /users
API-Version: 2
```

**Accept Header Example:**

```
GET /users
Accept: application/vnd.example.v2+json
```

**Use Cases:**

- Complex content negotiation requirements
- Multiple representation formats per version

**Developer Requirements:**

- Default to latest stable version if header omitted
- Validate version header and return `400 Bad Request` for unsupported versions
- Document required headers in OpenAPI specification

## Semantic Versioning for APIs

**Requirement:** Use semantic versioning format: `MAJOR.MINOR.PATCH`

**Version Components:**

- **MAJOR** – Breaking changes (requires client updates)
- **MINOR** – New features (backward compatible)
- **PATCH** – Bug fixes (backward compatible)

**Examples:**

- `1.0.0` – Initial release
- `1.1.0` – Added new endpoint (backward compatible)
- `1.1.1` – Fixed bug in existing endpoint
- `2.0.0` – Removed deprecated endpoint (breaking change)

### Breaking Changes (Increment MAJOR)

**Breaking Change Definition:**
A change that requires API consumers to modify their integration.

**Examples of Breaking Changes:**

- Removing an endpoint
- Removing a field from response
- Adding a required field to request
- Changing data type of existing field
- Changing authentication mechanism
- Renaming fields or endpoints
- Changing error response format

**Developer Requirements:**

- Increment major version for breaking changes
- Support previous major version for minimum 12 months
- Provide migration guide for breaking changes

### Non-Breaking Changes (Increment MINOR or PATCH)

**Non-Breaking Change Definition:**
A change that does not require API consumers to modify their integration.

**Examples of Non-Breaking Changes:**

- Adding a new endpoint
- Adding an optional field to request
- Adding a new field to response
- Adding a new HTTP method to existing endpoint
- Bug fixes that do not change contract

**Developer Requirements:**

- Increment minor version for new features
- Increment patch version for bug fixes
- Ensure existing clients continue to function unchanged

## Version Support Lifecycle

**Requirement:** Define and communicate version support policy.

**Support Tiers:**

| Tier           | Support Level                    | SLA          | Duration                      |
| -------------- | -------------------------------- | ------------ | ----------------------------- |
| **Current**    | Full support, active development | 99.9% uptime | Until next major version      |
| **Maintained** | Security and critical bug fixes  | 99.5% uptime | 12 months after deprecation   |
| **Deprecated** | Security fixes only              | 99% uptime   | 6 months notice before sunset |
| **Sunset**     | No support                       | N/A          | Version disabled              |

**Lifecycle Example:**

1. **v2.0.0 released** – v1 moves to "Maintained" tier
2. **v1 deprecated (12 months later)** – v1 moves to "Deprecated" tier
3. **v1 sunset (6 months later)** – v1 disabled

**Developer Requirements:**

- Clearly document support tier for each version
- Provide deprecation notices at least 6 months before sunset
- Monitor usage of deprecated versions
- Notify consumers via email, changelog, and API response headers

## Deprecation Policy

**Requirement:** Follow structured deprecation process.

### Step 1: Announce Deprecation

**Developer Requirements:**

- Publish deprecation notice in API changelog
- Update API documentation with deprecation warnings
- Email all registered API consumers
- Add deprecation headers to API responses:

```
Deprecation: true
Sunset: Sat, 31 Dec 2026 23:59:59 GMT
Link: <https://api.example.com/docs/migration-guide>; rel="deprecation"
```

### Step 2: Monitor Usage

**Developer Requirements:**

- Track usage metrics for deprecated endpoints
- Identify and contact high-volume consumers
- Offer migration support to large consumers

### Step 3: Sunset

**Developer Requirements:**

- Return `410 Gone` for sunset endpoints
- Provide clear error message with migration instructions
- Redirect to migration guide documentation

**Sunset Response Example:**

```json
{
  "error": "API version sunset",
  "message": "API v1 is no longer supported. Please migrate to v2.",
  "migrationGuide": "https://api.example.com/docs/v1-to-v2-migration",
  "supportContact": "api-support@example.com"
}
```

## Backward Compatibility Requirements

**Requirement:** Maintain backward compatibility within major versions.

**Developer Requirements:**

- Do not remove or rename existing fields
- Do not change data types of existing fields
- Do not make optional fields required
- Add new fields as optional
- Ensure clients ignoring new fields continue to function

**Tolerance for Change:**
API clients must:

- Ignore unknown fields in responses (forward compatibility)
- Accept new optional fields in requests

API providers must:

- Accept requests missing newly added optional fields
- Continue to return all previously documented fields

## Version Documentation

**Requirement:** Document all version changes in changelog.

**Changelog Format:**

```markdown
# API Changelog

## [2.0.0] - 2026-02-14

### Breaking Changes

- Removed deprecated `/users/legacy` endpoint
- Changed authentication from API key to OAuth 2.0
- Renamed `user_id` field to `userId` for consistency

### Migration Guide

See [v1 to v2 migration guide](./migration-v1-to-v2.md)

## [1.2.0] - 2025-11-01

### Added

- New `/users/{id}/preferences` endpoint
- Support for filtering users by creation date

### Fixed

- Fixed pagination bug in `/users` endpoint
```

**Developer Requirements:**

- Maintain CHANGELOG.md in repository
- Link changelogs from API documentation
- Use semantic versioning tags in Git

## Multi-Version Deployment Strategy

**Requirement:** Deploy multiple API versions independently.

**Deployment Options:**

### Option 1: Path-Based Routing

```
/v1 → Service v1
/v2 → Service v2
```

**Pros:** Simple, clear separation  
**Cons:** Requires routing configuration

### Option 2: Subdomain Routing

```
v1.api.example.com → Service v1
v2.api.example.com → Service v2
```

**Pros:** DNS-based routing, independent scaling  
**Cons:** Certificate and DNS management complexity

### Option 3: Header-Based Routing

```
API-Version: 1 → Service v1
API-Version: 2 → Service v2
```

**Pros:** Single endpoint  
**Cons:** More complex routing logic

**Developer Requirements:**

- Choose one strategy consistently across organization
- Document routing strategy in API documentation
- Test routing configuration in CI/CD pipeline

## Control Mapping

| EATGF Context     | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
| ----------------- | -------------- | --------- | ----- | ----- |
| Version Control   | A.8.19         | PS.3      | -     | BAI06 |
| Change Management | A.8.32         | PO.1      | -     | BAI06 |
| Deprecation       | A.5.30         | PO.3      | -     | BAI06 |
| Documentation     | A.5.37         | PO.3      | -     | MEA01 |

## Developer Checklist

Before releasing a new API version:

- [ ] Version number follows semantic versioning
- [ ] Breaking changes documented in migration guide
- [ ] Deprecation notices added for sunset features
- [ ] OpenAPI specification includes version metadata
- [ ] Changelog updated with release notes
- [ ] Previous version support policy communicated
- [ ] Routing configuration tested

## Governance Implications

**Risk if not implemented:**

- Breaking changes cause client application failures
- Lack of migration path frustrates API consumers
- Unsupported versions create security vulnerabilities

**Operational impact:**

- Clear versioning reduces support burden
- Structured deprecation allows planned migrations
- Version metrics inform infrastructure capacity planning

**Audit consequences:**

- Version history demonstrates change control discipline
- Deprecation policy shows responsible sunset management

**Cross-team dependencies:**

- DevOps team manages multi-version deployments
- Support team communicates deprecation to customers
- Security team ensures deprecated versions receive security patches

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Version Governance Policy (Layer 04)
3. API Governance Framework (Layer 05)
4. API Versioning Standard

## References

- Semantic Versioning 2.0.0 (https://semver.org/)
- RFC 8594: Sunset HTTP Header
- Stripe API Versioning (https://stripe.com/docs/api/versioning)
- Microsoft REST API Guidelines (Versioning)
- Roy Fielding, "REST APIs must be hypertext-driven"

## Version History

| Version | Date       | Change Type | Description                     |
| ------- | ---------- | ----------- | ------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial API versioning standard |
