# API Control Mapping Appendix

## Purpose

Demonstrates formal cross-mapping between API_GOVERNANCE_STANDARD controls and seven external compliance frameworks.

Enables ISO 27001, SOC 2 Type II, PCI-DSS, FedRAMP, and GDPR audit defensibility by establishing control-to-framework traceability with no improvisation.

## Architectural Position

- **Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
- **Domain:** 02_API_GOVERNANCE / Operational
- **Authority Source:** API_GOVERNANCE_STANDARD.md (root authority)
- **Control Authority Relationship:** Subordinate operational document implementing root standard controls with framework alignment evidence

## Governance Principles

Mapping operates under these mandatory principles:

- **Framework Alignment:** No EATGF control exists without documented alignment to at least two external frameworks
- **No Invented Controls:** Every mapped control derives from published framework (ISO, NIST, OWASP, COBIT, RFC, or GDPR)
- **Audit Traceability:** Every framework reference includes exact annex, practice, or control number for auditor verification
- **Automation Enablement:** Mappings enable automated evidence collection (log queries, configuration snapshots, test reports)
- **Regulatory Defensibility:** Certification impact documented (which audit, which auditor requirement, which risk category)
- **Single Source of Truth:** Centralized mapping prevents framework-specific fragmentation

## Section 1: ISO 27001:2022 Annex A Mapping

ISO 27001:2022 establishes mandatory Information Security Controls for organizations seeking certification. This section maps API governance controls to ISO control objectives.

| EATGF Control                    | ISO 27001:2022 Annex A | Clause Title                                                | Requirement Statement                                           | API Governance Implementation                                                                                 | Audit Evidence                                                                                                 |
| -------------------------------- | ---------------------- | ----------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Authentication**               | A.8.2                  | Confidentiality and integrity of authentication information | "Organizations shall protect authentication information..."     | OAuth2/OIDC with token validation; mTLS for service-to-service; API key management in HashiCorp Vault         | Gateway logs showing successful/failed auth attempts; token validation error rates; JWKS endpoint availability |
| **Authorization**                | A.8.2, A.8.5           | Authentication, Access control                              | "Enforce the principle of least privilege..."                   | RBAC matrix with role definitions; ABAC for resource-level access; tenant isolation enforcement               | RBAC policy file; authorization decision logs; cross-tenant access rejection rate (should be 0%)               |
| **Input Validation**             | A.8.22                 | Secure development                                          | "Organizations shall establish secure development practices..." | JSON Schema validation; Pydantic type hints; OpenAPI input constraints; SAST scanning (Bandit, CodeQL)        | Schema definition files; Bandit/CodeQL scan reports; SAST exception tracking                                   |
| **Secrets Management**           | A.8.2, A.8.12          | Sensitive/cryptographic information                         | "Secrets shall be protected..."                                 | Vault-based key rotation; encrypted at rest/in transit; no hardcoded secrets in deployed code                 | Vault audit logs; pre-commit hook scan results; secret rotation timestamps                                     |
| **Rate Limiting**                | A.8.30                 | Information Security Incident Management                    | "Organizations shall prevent DoS attacks..."                    | Per-tier rate limiting; 429 response codes; traffic shaping; monitoring for anomalous patterns                | Rate limit configuration files; 429 response frequency; traffic spike detection logs                           |
| **Logging & Observability**      | A.8.15, A.8.16         | Monitoring and Recording                                    | "Organize collection of sufficient user-related activities..."  | JSON structured logging with correlation IDs; 90+ day retention; real-time alerting; audit trail immutability | Structured log samples; retention policy documentation; alerting configuration; log integrity checks           |
| **API Versioning**               | A.8.31                 | Supplier relationships                                      | "Control interfaces with suppliers..."                          | Semantic versioning; 6-month deprecation windows; Sunset header per RFC 8594; breaking change policy          | Version tag history; deprecation notice archives; changelog entries; sunset header verification                |
| **Webhook Security**             | A.8.28                 | Message authentication codes\*\*                            | "Ensure integrity of API events..."                             | HMAC-SHA256 signature verification; timestamp validation (300s tolerance); replay attack prevention           | Webhook signature validation code; timestamp check logs; replay attempt rate (should be 0%)                    |
| **Documentation**                | A.8.29                 | Testing                                                     | "Establish practices to test...secure development"              | OpenAPI 3.0+ spec; machine-readable format; updated with each release; SDK auto-generation capability         | Published OpenAPI spec; spec validation reports; SDK generation success rate; API changelog                    |
| **Denial of Service Prevention** | A.8.30                 | Resource consumption control                                | "Implement resource limits..."                                  | Rate limiting, connection pooling, timeout enforcement, request size limits                                   | Configuration files documenting limits; performance metrics showing enforcement                                |

**Certification Impact:** ISO 27001:2022 certification audit requires evidencing control implementation for A.8.x (Cryptography and Access Control domain). Absence of API versioning documentation or authentication controls will result in certification finding.

## Section 2: NIST SP 800-218 (SSDF) Mapping

NIST Secure Software Development Framework (SP 800-218) defines 15 secure development practices across 4 categories. API governance contributes to PW (Prepare the Organization), PO (Perform Secure Software Development), and RV (Review, Verify, Validate) categories.

### PW (Prepare the Organization)

| EATGF Control          | NIST SSDF Practice | Practice Title                                                      | API Governance Implementation                                                                           | Audit Evidence                                                                                  |
| ---------------------- | ------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Secrets Management** | PW.2               | Identify and manage a set of secure development practices and tools | Establish Vault as organization-wide secret manager; integrate pre-commit hooks into developer workflow | Vault setup documentation; pre-commit hook configuration in all repositories; usage statistics  |
| **API Documentation**  | PW.3               | Document secure development practices and tools                     | Maintain OpenAPI specification as API documentation standard; enforce schema validation in CI/CD        | OpenAPI specification governance policy; CI/CD gate enforcement logs; documentation audit trail |

### PO (Perform Secure Development)

| EATGF Control               | NIST SSDF Practice | Practice Title                                                                       | API Governance Implementation                                                                         | Audit Evidence                                                                                  |
| --------------------------- | ------------------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Authentication**          | PO.1               | Define the security requirements and functionality for the applications and services | Define OAuth2/OIDC as mandatory authentication for APIs; specify token lifetime and refresh policies  | Authentication requirements document; OAuth2 implementation checklist; enforcement gate results |
| **Authorization**           | PO.2               | Use secure design principles in software, firmware, and services                     | Implement RBAC/ABAC as secure design pattern; enforce resource ownership verification to prevent BOLA | Design review checklist; authorization matrix templates; BOLA prevention validation results     |
| **Input Validation**        | PO.5               | Implement secure coding practices                                                    | Establish JSON Schema validation as mandatory; require Pydantic type hints; enforce SAST gate         | Schema definition files; type annotation audit; Bandit/CodeQL scan reports                      |
| **API Versioning**          | PO.3               | Manage versions of components, and monitor changes in source code                    | Enforce semantic versioning; maintain API version headers; document breaking changes                  | Version control logs; versioning policy document; breaking change notification records          |
| **Logging & Observability** | PO.4               | Enable monitoring of events and collection of monitoring data                        | Configure structured JSON logging; include request/correlation IDs; implement 24/7 alerting           | Logging configuration files; alert rule definitions; log aggregation platform setup             |

### RV (Review, Verify, Validate)

| EATGF Control        | NIST SSDF Practice | Practice Title                                                                            | API Governance Implementation                                                                          | Audit Evidence                                                                        |
| -------------------- | ------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Input Validation** | RV.1               | Maintain a system to monitor reports of security flaws                                    | Subscribe to CVE feeds; automate dependency scanning; track vulnerability lifecycle                    | Dependency scanning tool configuration; CVE alert frequency; remediation SLA tracking |
| **Rate Limiting**    | RV.2               | Perform dynamic and static analysis of the code and the artifact produced through a build | Execute SAST (CodeQL), DAST, and load testing before production release                                | SAST/DAST scan reports; load test results; performance baseline comparisons           |
| **Webhook Security** | RV.3               | Perform security testing of completeness and effectiveness                                | Implement webhook signature verification testing; timestamp validation testing; retry logic validation | Test case results; webhook security test coverage metrics; integration test logs      |

**Certification Impact:** FedRAMP and CMMC (Cybersecurity Maturity Model Certification) leverage NIST SSDF practices. API governance controls map to SSDF Level 3 (Managed) requirements; absence of versioning/logging practices will prevent CMMC L3 certification.

## Section 3: OWASP API Security Top 10 2023 Mapping

OWASP API Top 10 identifies ten critical security risks specific to modern APIs. API governance controls provide mitigations for all ten categories.

| OWASP API Risk | Risk Category                                      | EATGF Control(s)                           | Mitigation Strategy                                                                                                        | Enforcement Gate               | Evidence of Mitigation                                                                                           |
| -------------- | -------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **API1**       | Broken Object Level Authorization (BOLA)           | Authorization, Input Validation            | Implement resource ownership verification; validate user can access only their own objects; prevent cross-tenant access    | Pre-Release Authorization Gate | Authorization test results; tenant isolation verification logs                                                   |
| **API2**       | Broken Authentication                              | Authentication                             | Enforce OAuth2/OIDC; validate token expiration; prevent hardcoded credentials; implement token rotation                    | Pre-Merge Security Gate        | OAuth2 implementation audit; token rotation configuration; credential scan results                               |
| **API3**       | Broken Object Property Level Authorization (BOPLA) | Authorization, Input Validation            | Validate all request properties against user permissions; prevent property-level privilege escalation                      | Pre-Release Authorization Gate | Authorization matrix covering properties; property-level access test cases                                       |
| **API4**       | Unrestricted Resource Consumption                  | Rate Limiting, Input Validation            | Implement per-tier rate limiting; enforce request size limits; timeout enforcement                                         | Pre-Release Compliance Gate    | Rate limit configuration per tier; timeout settings; load test verification                                      |
| **API5**       | Broken Function Level Authorization                | Authorization                              | Implement API endpoint access matrix; map endpoints to required roles; validate authorization before processing            | Pre-Release Architecture Gate  | API endpoint authorization matrix; role-to-endpoint mapping document                                             |
| **API6**       | Unrestricted Access to Sensitive Business Flows    | Rate Limiting, Webhook Security            | Implement flow-level rate limiting; prevent abuse of sensitive operations (password reset, payment); webhook rate limiting | Pre-Release Compliance Gate    | Rate limit configuration for sensitive endpoints; webhook rate limit settings; abuse attempt logs (should be 0%) |
| **API7**       | Server-Side Request Forgery (SSRF)                 | Input Validation, Webhooks                 | Validate webhook URLs against whitelist; prevent internal service access; validate all external requests                   | Pre-Merge Security Gate        | Webhook URL validation rules; SSRF test case execution; URL whitelist configuration                              |
| **API8**       | Security Misconfiguration                          | Documentation, Logging, Secrets Management | Maintain current OpenAPI spec; enforce logging configuration; regular security scanning                                    | Pre-Release Architecture Gate  | OpenAPI spec freshness audit; logging configuration verification; security scanning results                      |
| **API9**       | Improper Inventory Management                      | Documentation, API Versioning              | Maintain comprehensive API registry; document all endpoints; enforce versioning discipline; sunset deprecated APIs         | Pre-Release Documentation Gate | API inventory in OpenAPI format; versioning compliance audit; sunset notice delivery logs                        |
| **API10**      | Unsafe Consumption of APIs                         | Documentation                              | Document all upstream API dependencies; include security properties; maintain SDK versioning                               | Pre-Release Architecture Gate  | Upstream API inventory; dependency security assessment; SDK version tracking                                     |

**Certification Impact:** PCI-DSS, HIPAA, and FedRAMP require OWASP Top 10 mitigation. Insurance companies (Cyber Insurance) require OWASP API Top 10 controls as risk assessment criteria. Absence of BOLA/BOPLA controls will result in claim denial.

## Section 4: COBIT 2019 Mapping

COBIT 2019 (Control Objectives for Information and Related Technologies) provides governance framework used by internal audit teams and IT governance committees.

| EATGF Control               | COBIT 2019 Domain               | COBIT Process | Governance Area                                                                      | API Governance Implementation                                                                   |
| --------------------------- | ------------------------------- | ------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **Authentication**          | EDM (Evaluate, Direct, Monitor) | EDM01         | Establish governance objectives; articulate authentication as non-negotiable control | Authentication requirement in API governance policy; enforcement gates block non-compliant APIs |
| **Authorization**           | DSS (Deliver, Service, Support) | DSS05         | Protect against unauthorized access; implement access control                        | RBAC/ABAC matrix; role definitions; tenant isolation enforcement                                |
| **Input Validation**        | DSS (Deliver, Service, Support) | DSS06         | Identify and classify information; protect information                               | Input schema validation; data classification requirements; protection rules per classification  |
| **API Versioning**          | BAI (Build, Acquire, Implement) | BAI07         | Manage IT changes; control version deployment process                                | Semantic versioning discipline; deprecation windows; change control process                     |
| **Logging & Observability** | MEA (Monitor, Evaluate, Assess) | MEA02         | Monitor and evaluate IT performance; collect sufficient audit evidence               | Structured logging requirement; correlation ID enforcement; retention policies                  |
| **Rate Limiting**           | DSS (Deliver, Service, Support) | DSS02         | Determine IT service levels; prevent DoS                                             | Rate limiting tiers; threshold configuration; SLA mapping to tier                               |
| **Secrets Management**      | DSS (Deliver, Service, Support) | DSS05         | Control access to authentication secrets; encryption key management                  | Vault-based key rotation; access logging; key lifecycle policy                                  |
| **Webhook Security**        | BAI (Build, Acquire, Implement) | BAI04         | Enable operational processes; ensure data integrity                                  | HMAC signature validation; replay attack prevention; webhook event tracking                     |

**Certification Impact:** Large enterprises undergoing IT audit will have COBIT-based control assessment. Governance Charter must map to COBIT DSS/BAI/MEA processes. Absence of versioning/logging controls will require "remediation plan" in audit report.

## Section 5: NIST SP 800-53 Revision 5 Mapping

NIST 800-53 (Security and Privacy Controls for Information Systems and Organizations) provides 988 minimum security controls structured across 23 families (AC, AU, CA, CM, CP, etc.). This section maps API controls to most relevant families.

### AC (Access Control) Family

| EATGF Control      | NIST 800-53 Control | Control Title                | API Implementation                                          | Audit Evidence                                           |
| ------------------ | ------------------- | ---------------------------- | ----------------------------------------------------------- | -------------------------------------------------------- |
| **Authentication** | AC-2                | Account Management           | OAuth2/OIDC token lifecycle; account suspension enforcement | Token validation logs; account lifecycle audit trail     |
| **Authorization**  | AC-3                | Access Enforcement           | RBAC/ABAC authorization matrix; deny-by-default policy      | Authorization policy documentation; access decision logs |
| **Authorization**  | AC-6                | Principle of Least Privilege | Role definitions with minimal required permissions          | Role definition document; permission pruning audit       |

### AU (Audit and Accountability) Family

| EATGF Control               | NIST 800-53 Control | Control Title                    | API Implementation                                             | Audit Evidence                                             |
| --------------------------- | ------------------- | -------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------- |
| **Logging & Observability** | AU-2                | Audit Events                     | JSON structured logging; correlation IDs; real-time collection | Log format specification; log sample review                |
| **Logging & Observability** | AU-6                | Audit Review, Analysis, Response | 24/7 alerting; anomaly detection; incident escalation          | Alert rule definitions; escalation procedure documentation |
| **Logging & Observability** | AU-11               | Audit Record Retention           | 90+ day minimum retention; immutable log storage               | Retention policy; log archival configuration               |

### SC (System and Communications Protection) Family

| EATGF Control          | NIST 800-53 Control | Control Title                                  | API Implementation                                         | Audit Evidence                                   |
| ---------------------- | ------------------- | ---------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| **Secrets Management** | SC-12               | Cryptographic Key Establishment and Management | Vault-based key rotation; rotation frequency documentation | Key rotation logs; Vault audit trail             |
| **API Versioning**     | SC-4                | Information Flow Enforcement                   | API version isolation; version-specific security policies  | Version isolation configuration                  |
| **Rate Limiting**      | SC-5                | Denial of Service Protection                   | Rate limiting per client; traffic shaping                  | Rate limit configuration; 429 response frequency |

### SI (System and Information Integrity) Family

| EATGF Control        | NIST 800-53 Control | Control Title                             | API Implementation                                       | Audit Evidence                                 |
| -------------------- | ------------------- | ----------------------------------------- | -------------------------------------------------------- | ---------------------------------------------- |
| **Input Validation** | SI-10               | Information System Monitoring             | Input validation schema; SAST scanning                   | Schema definitions; Bandit/CodeQL reports      |
| **Webhook Security** | SI-7                | Software, Firmware, Information Integrity | Webhook signature verification; replay attack prevention | Webhook verification code; replay attempt logs |

**Certification Impact:** FedRAMP High baseline requires NIST 800-53 SC family controls (all). Absence of rate limiting / DoS protection will result in FedRAMP audit finding.

## Section 6: IETF RFC Alignment

IETF Request for Comments establish Internet Standards referenced in NIST, OWASP, and ISO documents. API governance implements these standards directly.

| API Control          | RFC Number | RFC Title                                  | Requirement                                             | Implementation                                                             |
| -------------------- | ---------- | ------------------------------------------ | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Authentication**   | RFC 6749   | OAuth 2.0 Authorization Framework          | "Request MUST include client_id and use HTTPS"          | OAuth2 implementation enforces HTTPS; client ID validation in gateway      |
| **Authentication**   | RFC 7519   | JSON Web Token (JWT)                       | "Claims MUST be verified before use"                    | JWT RS256/ES256 validation; expiration/nbf checks                          |
| **Authentication**   | RFC 8705   | OAuth 2.0 Mutual-TLS Client Authentication | "Mutual TLS certificate used for client authentication" | mTLS certificate validation in PRE-Release gate                            |
| **API Versioning**   | RFC 8594   | Sunset Header                              | "Sunset header SHOULD indicate deprecation date"        | Sunset header in API responses; automated date calculation                 |
| **Rate Limiting**    | RFC 9110   | HTTP Semantics                             | "429 Too Many Requests" status code requirement         | 429 response format compliance; RateLimit-\* header implementation per RFC |
| **Webhook Security** | RFC 7231   | HTTP Message Syntax                        | "Retry-After header for 429/503 responses"              | Webhook retry policy with exponential backoff; Retry-After header          |

**Compliance Note:** GDPR Article 32 (Security Measures) references IETF standards for cryptography/authentication. Implementation of RFC 6749 demonstrates GDPR-compliant authentication.

## Section 7: Certification Readiness Impact

This section documents which external certifications depend on API governance controls.

### ISO 27001:2022 Certification

| Certification Stage                   | API Control Dependency                            | Impact of Non-Compliance                                                                         |
| ------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Preparation (Gap Analysis)**        | Authentication, Authorization, Secrets Management | Auditors will identify gaps in A.8.2 (authentication) and A.8.12 (secret protection)             |
| **Stage 1 (Readiness Audit)**         | Documentation, Logging, Versioning                | Auditors verify OpenAPI specs, logging configuration, version control                            |
| **Stage 2 (Certification Audit)**     | All controls                                      | Non-compliance with any control results in "Major Non-Conformity" finding; certification delayed |
| **Post-Certification (Surveillance)** | Logging, Secrets Management, Rate Limiting        | Annual audits verify controls remain operational; findings require 30-day remediation            |

**Timeline Impact:** ISO certification delays 3-6 months per major finding requiring remediation.

### SOC 2 Type II Certification

| Control Environment                 | API Control Dependency                            | Evidence Required                                                 |
| ----------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| **CC1 (Organization & Objectives)** | All controls; Governance Principles               | Policy documents stating all 10 controls                          |
| **CC6 (Logical Access)**            | Authentication, Authorization, Secrets Management | 12-month audit trail of authentication/authorization decisions    |
| **CC7 (System Monitoring)**         | Logging & Observability                           | Structured logs with correlation IDs; real-time alerting evidence |
| **CC9 (Change Management)**         | API Versioning, Documentation                     | Version control history; deprecation notice delivery logs         |

**Timeline Impact:** SOC 2 audit typically 4-6 months; non-compliance with any CC control requires remediation before pass.

### PCI-DSS 4.0 Compliance

| PCI-DSS Requirement | API Control Dependency             | Specific Control Evidence                                          |
| ------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| **Requirement 1**   | Input Validation, Rate Limiting    | API gateway configuration showing input validation + rate limiting |
| **Requirement 2**   | Secrets Management                 | Evidence that no hard-coded credentials exist in APIs              |
| **Requirement 3**   | Secrets Management, Authentication | Encryption of secrets at rest/in transit                           |
| **Requirement 6**   | Input Validation, Logging          | SAST scan results; error logging configuration                     |
| **Requirement 7**   | Authorization, Logging             | Role-to-permission mapping; access decision logs                   |
| **Requirement 8**   | Authentication                     | OAuth2 implementation; token management                            |
| **Requirement 10**  | Logging & Observability            | Structured logging with correlation IDs; 90-day retention          |

**Timeline Impact:** Annual PCI-DSS audit; any failing requirement delays assessment; requires Point-in-Time assessment (can re-test quarterly).

### GDPR Compliance

| GDPR Article                            | API Control Dependency            | Regulatory Requirement                                                              |
| --------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------- |
| **Article 4 (Definitions)**             | Documentation                     | Define "processing" activities in OpenAPI specs                                     |
| **Article 32 (Security Measures)**      | All controls                      | Demonstrate appropriate technical measures (encryption, versioning, authentication) |
| **Article 33 (Breach Notification)**    | Logging & Observability           | 72-hour breach notification requires immediate access to audit logs                 |
| **Article 35 (Data Protection Impact)** | Authorization, Secrets Management | DPIA must show data isolation and access control measures                           |

**Timeline Impact:** GDPR enforcement focus is "privacy by design"; absence of encryption/access controls can result in €20M fines.

### HIPAA Compliance

| HIPAA Department                     | API Control Dependency              | Security Rule Requirement                                                      |
| ------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------ |
| **Technical Safeguards (§164.312)**  | Authentication, Encryption, Logging | User authentication mandatory; encryption at rest/in transit; activity logging |
| **Access Controls (§164.312(a)(2))** | Authorization, Secrets Management   | Access control policies; encryption of authentication keys                     |

**Timeline Impact:** HIPAA violations: $100-$50,000 per record exposed; repeated violations result in OCR investigation and mandatory corrective action plan.

## Developer Checklist

Before deploying API to production, verify framework alignment:

- [ ] **Authentication:** OAuth2/OIDC token validation implemented (ISO A.8.2, NIST PW.1, OWASP API2, RFC 6749)
- [ ] **Authorization:** RBAC/ABAC matrix defined; resource ownership validated (ISO A.8.2, NIST PW.2, OWASP API1, COBIT DSS05)
- [ ] **Input Validation:** JSON Schema validation enabled; SAST passed (NIST PO.5, OWASP API3, NIST 800-53 SI-10)
- [ ] **Secrets:** No hardcoded credentials; HashiCorp Vault integration (ISO A.8.12, NIST PW.2, NIST 800-53 SC-12)
- [ ] **Rate Limiting:** Per-tier configuration with 429 responses (NIST RV.2, OWASP API4/API6, RFC 9110, NIST 800-53 SC-5)
- [ ] **Logging:** JSON structured logging with correlation IDs; 90+ day retention (ISO A.8.15, NIST RV.2, NIST 800-53 AU-2)
- [ ] **Versioning:** Semantic versioning; Sunset headers (NIST PO.3, OWASP API7/API9, RFC 8594, COBIT BAI07)
- [ ] **Documentation:** OpenAPI 3.0+ spec complete; tested with validator (NIST PW.3, OWASP API9, COBIT BAI07)
- [ ] **Webhook Security:** HMAC-SHA256 + timestamp validation (ISO A.8.28, NIST PO.4, OWASP API6, RFC 7231)
- [ ] **Compliance Readiness:** Verified certification impact statement (ISO/SOC2/PCI-DSS/GDPR/HIPAA) before deployment

## Governance Implications

### Risk If Not Implemented

- **ISO 27001:** Certification denial; audit finding issued
- **SOC 2 Type II:** Cannot demonstrate LDM (trust principles); audit fails Stage 2
- **PCI-DSS:** Unencrypted secrets = Requirement 2 violation; potential assessment failure
- **GDPR:** Unencrypted APIs = Article 32 violation; €20M fine exposure
- **FedRAMP:** Missing rate limiting = SC-5 control failure; High baseline not achievable

### Audit Consequences

- **External Auditors:** Cannot verify compliance without framework mapping documentation
- **Internal Audit:** Control gaps become "high-risk findings" requiring remediation tracking
- **Board/Stakeholders:** Lack of certification readiness impacts M&A diligence, customer contracts
- **Incident Response:** Absence of correlation IDs prevents attack timeline reconstruction; forensic investigation delayed

### Regulatory Compliance

Organizations handling customer data must demonstrate compliance to at least two frameworks (typically ISO 27001 + PCI-DSS for payment processors; HIPAA for healthcare; GDPR for EU customers). Absence of API governance controls creates regulatory gaps.

## Official References

- **EATGF Foundation:** `eatgf-framework/00_FOUNDATION/MASTER_CONTROL_MATRIX.md`
- **Root Authority:** `API_GOVERNANCE_STANDARD.md`
- **Operations Matrix:** `API_ENFORCEMENT_MATRIX.md`
- **ISO 27001:2022:** Annex A (Control objectives and controls)
- **NIST SP 800-218:** Secure Software Development Framework
- **OWASP API Security Top 10 2023:** https://owasp.org/www-project-api-security/
- **COBIT 2019:** Process Reference Guide (ISACA)
- **NIST SP 800-53 Revision 5:** Security and Privacy Controls for Information Systems
- **GDPR:** Regulation (EU) 2016/679, Articles 32-35
- **PCI-DSS 4.0:** Payment Card Industry Data Security Standard
- **HIPAA:** 45 CFR Parts 160, 164 (Technical Safeguards)

## Version Information

| Element               | Value                                                                          |
| --------------------- | ------------------------------------------------------------------------------ |
| **Document Version**  | 2.0 (Refined Framework Alignment)                                              |
| **Change Type**       | Major (explicit framework mapping + compliance impact statements)              |
| **Issue Date**        | 2024-Q1                                                                        |
| **Supersedes**        | API_CONTROL_MAPPING_APPENDIX v1.0                                              |
| **Relation to EATGF** | Implements EATGF Layer 08, Domain 02; operational evidence for external audits |
| **Next Review**       | Annual (align with ISO/SOC2/PCI-DSS/GDPR regulatory updates)                   |
