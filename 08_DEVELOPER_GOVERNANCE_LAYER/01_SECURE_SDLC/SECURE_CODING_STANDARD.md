# Secure Coding Standard

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 01_SECURE_SDLC  
**Governance Scope:** Implementation Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 01_SECURE_SDLC

**Governance Scope:** Language-agnostic secure coding requirements and vulnerability prevention standards.

**Control Authority Relationship:** Implements:
- Layer 02: Application Security Controls
- Layer 04: Information Security Policy
- OWASP ASVS and CWE Top 25

## Purpose

This standard defines mandatory secure coding practices to prevent common vulnerabilities. It covers:

- Input validation and output encoding
- Authentication and session management
- Cryptographic requirements
- Error handling and logging
- Secure configuration management

## Governance Principles

- **Security-by-Design:** Security controls embedded at code level
- **Control-Centric Architecture:** Prevents CWE Top 25 weaknesses
- **Developer-Operational Alignment:** Language-specific guidance provided
- **Audit Traceability:** SAST tools validate compliance

## Secure Coding Requirements

### Input Validation

**Requirement:** All external input must be validated before processing.

**Developer Requirements:**
- Use allowlist validation (define what is permitted, reject everything else)
- Validate data type, length, format, and range
- Reject input that fails validation (do not attempt to sanitize)
- Validate on the server side, even if client-side validation exists

**Prohibited Practices:**
- Relying solely on client-side validation
- Blacklist-based validation
- Attempting to "fix" invalid input

**Evidence:**
- SAST findings showing input validation on all external entry points

### Output Encoding

**Requirement:** Encode all dynamic output to prevent injection attacks.

**Developer Requirements:**
- Use context-aware output encoding (HTML, JavaScript, SQL, OS command)
- Use established encoding libraries (do not implement custom encoding)
- Apply encoding at the last moment before output

**Prohibited Practices:**
- Directly embedding user input in HTML, SQL, or OS commands
- Using string concatenation for dynamic SQL queries

### Authentication and Session Management

**Requirement:** Implement secure authentication and session handling.

**Developer Requirements:**
- Use industry-standard authentication libraries (OAuth 2.0, OIDC, SAML)
- Enforce multi-factor authentication for high-privilege accounts
- Generate cryptographically random session tokens (minimum 128 bits)
- Set session timeout (30 minutes for standard users, 15 minutes for privileged)
- Invalidate sessions on logout
- Use secure and HttpOnly flags on session cookies

**Prohibited Practices:**
- Implementing custom authentication schemes
- Storing passwords in plain text or using weak hashing (e.g., MD5, SHA-1)
- Including session tokens in URLs

**Password Requirements:**
- Minimum length: 12 characters
- Use bcrypt, scrypt, or Argon2 for password hashing
- Implement account lockout after 5 failed login attempts

### Cryptography

**Requirement:** Use approved cryptographic algorithms and key management.

**Developer Requirements:**
- Use TLS 1.3 or TLS 1.2 for data in transit
- Use AES-256 for data at rest
- Use cryptographically secure random number generators
- Never hard-code cryptographic keys in source code
- Rotate encryption keys according to organizational policy

**Prohibited Practices:**
- Using deprecated algorithms (DES, 3DES, RC4, MD5, SHA-1)
- Implementing custom cryptographic algorithms
- Storing encryption keys in version control

### Error Handling and Logging

**Requirement:** Handle errors securely and log security-relevant events.

**Developer Requirements:**
- Display generic error messages to users
- Log detailed error information for developers (but do not log sensitive data)
- Log authentication attempts, authorization failures, and security events
- Ensure log entries include timestamp, user ID, source IP, and action

**Prohibited Practices:**
- Displaying stack traces or database errors to end users
- Logging passwords, session tokens, or credit card numbers
- Suppressing errors without logging

### Secure Configuration

**Requirement:** Follow secure-by-default configuration practices.

**Developer Requirements:**
- Disable unnecessary features and services
- Remove default accounts and credentials
- Use environment variables or secret management systems for sensitive configuration
- Implement principle of least privilege for application accounts

**Prohibited Practices:**
- Committing configuration files with production credentials to version control
- Using default or weak credentials (e.g., admin/admin)

### Authorization

**Requirement:** Enforce access control on all protected resources.

**Developer Requirements:**
- Implement role-based access control (RBAC) or attribute-based access control (ABAC)
- Perform authorization checks on the server side
- Deny access by default (fail securely)
- Verify authorization on every request (do not rely on client-side checks)

**Prohibited Practices:**
- Relying on hidden URLs or client-side access controls
- Using direct object references without authorization checks

### SQL Injection Prevention

**Requirement:** Prevent SQL injection through parameterized queries.

**Developer Requirements:**
- Use parameterized queries (prepared statements) for all database access
- Use ORM frameworks where appropriate
- Apply principle of least privilege to database accounts

**Prohibited Practices:**
- Building SQL queries through string concatenation
- Using dynamic SQL without parameterization

### Cross-Site Scripting (XSS) Prevention

**Requirement:** Prevent XSS through input validation and output encoding.

**Developer Requirements:**
- Apply context-aware output encoding
- Use Content Security Policy (CSP) headers
- Validate and sanitize rich text input (use established libraries)

**Prohibited Practices:**
- Directly rendering user input in HTML without encoding
- Using innerHTML or eval() with untrusted data

### Cross-Site Request Forgery (CSRF) Prevention

**Requirement:** Protect state-changing operations against CSRF.

**Developer Requirements:**
- Use anti-CSRF tokens for all state-changing requests
- Validate token on server side
- Use SameSite cookie attribute

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Input Validation | A.8.26 | PO.1 | ASVS V5 | BAI03 |
| Authentication | A.5.17, A.5.18 | PS.1 | ASVS V2, V3 | DSS05 |
| Cryptography | A.8.24 | PS.2 | ASVS V6 | DSS05 |
| Error Handling | A.8.16 | RV.2 | ASVS V7 | DSS05 |
| Authorization | A.5.15 | PO.1 | ASVS V4 | DSS05 |

## Developer Checklist

Before committing code:

- [ ] All external input is validated using allowlist approach
- [ ] All dynamic output is context-encoded
- [ ] No credentials or secrets in source code
- [ ] Parameterized queries used for all database access
- [ ] Authentication and authorization checks on all protected endpoints
- [ ] SAST scan passes with no high or critical findings

## Governance Implications

**Risk if not implemented:**
- Introduction of OWASP Top 10 vulnerabilities
- Data breaches and regulatory penalties
- Reputational damage and loss of customer trust

**Operational impact:**
- Reduced vulnerability remediation costs
- Faster security testing and code review
- Improved code quality and maintainability

**Audit consequences:**
- Non-compliance with PCI-DSS, HIPAA, GDPR requirements
- Failed penetration tests and security assessments

**Cross-team dependencies:**
- Security team provides security testing and advisory
- QA team validates security requirements in test plans
- DevOps team configures SAST tools in CI/CD pipeline

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. Secure Coding Standard

## References

- OWASP Application Security Verification Standard (https://owasp.org/www-project-application-security-verification-standard/)
- OWASP Top 10 (https://owasp.org/www-project-top-ten/)
- CWE Top 25 (https://cwe.mitre.org/top25/)
- NIST SP 800-53 (System and Services Acquisition controls)
- SEI CERT Coding Standards (https://wiki.sei.cmu.edu/confluence/display/seccode)

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial secure coding standard |
