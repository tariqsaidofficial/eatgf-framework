# API Governance: Authority Hierarchy and Enforcement Clarification

| Field          | Value                                                              |
| -------------- | ------------------------------------------------------------------ |
| Document Type  | Architecture Clarification                                         |
| Version        | 1.0                                                                |
| Classification | Controlled                                                         |
| Effective Date | 2026-02-16                                                         |
| Authority      | Chief Information Security Officer and Chief Technology Officer    |
| EATGF Layer    | Cross-Layer (05_DOMAIN_FRAMEWORKS + 08_DEVELOPER_GOVERNANCE_LAYER) |

---

## Purpose

Clarify the architectural relationship between API_GOVERNANCE_FRAMEWORK (Layer 05 - strategic) and API_GOVERNANCE_STANDARD (Layer 08 - operational) to eliminate audit questions about authority, enforcement, and applicability.

## Architectural Position

**Cross-Layer Reference:** This document clarifies authority relationships across:

- **Layer 05:** API_GOVERNANCE_FRAMEWORK (strategic governance)
- **Layer 08 / 02_API_GOVERNANCE:** API_GOVERNANCE_STANDARD (operational enforcement)

## Authority Hierarchy

### Layer 05: Strategic API Governance Framework

**Document:** `eatgf-framework/05_DOMAIN_FRAMEWORKS/API_GOVERNANCE_FRAMEWORK.md`

**Authority Type:** STRATEGIC / POLICY-LEVEL

**Scope:** Establishes **what** APIs must do:

- API design principles (contract-first, semantic versioning)
- Lifecycle stages (planning, design, implementation, deployment, monitoring, decommissioning)
- Security requirements (authentication, authorization, encryption, TLS 1.3)
- Versioning strategy (backward compatibility, deprecation, migration)
- Documentation standards (OpenAPI specification, SDK requirements)
- Monitoring and observability (performance, security, business metrics)
- Compliance requirements (rate limiting, quota enforcement, audit trails)

**Governance Scope:** Organizational direction for ALL APIs; non-negotiable requirements

**Enforcement Level:** MANDATORY for enterprise and SaaS systems; applies to:

- Internal microservice APIs
- External public APIs
- Third-party API integrations
- Mobile app backend APIs

**Authority Reference:** Layer 05_DOMAIN_FRAMEWORKS → maps to Layer 02_CONTROL_ARCHITECTURE (API-SEC-01, API-LC-01 controls)

---

### Layer 08: Operational API Governance Standard

**Document:** `eatgf-framework/08_DEVELOPER_GOVERNANCE_LAYER/02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md`

**Authority Type:** OPERATIONAL / IMPLEMENTATION-LEVEL

**Scope:** Establishes **how** to implement Layer 05 requirements:

- Security gate implementation specifics (which tools, configurations, thresholds)
- Authentication technology choices (OAuth 2.0 vs. mTLS vs. API keys)
- Request/response validation rules (input sanitization, output encoding)
- Rate limiting implementation (token bucket algorithm, distributed tracing)
- Error handling procedures (error codes, logging, response formats)
- Testing requirements (integration tests, contract tests, chaos engineering)
- Deployment procedures (canary deployments, circuit breakers, rollback)
- Monitoring implementation (metrics collection, alerting rules)

**Governance Scope:** Adds technical specificity to Layer 05 principles; includes:

- Enforcement gates (which CI/CD gates to implement)
- Tool selection (approved frameworks, libraries, platforms)
- Configuration standards (defaults, exceptions, overrides)
- Evidence collection (audit trails, proof of compliance)
- Team responsibilities (who approves, who deploys, who monitors)

**Enforcement Level:** MANDATORY for developers; provides:

- Code templates and examples
- Integration with CI/CD pipelines
- Automated compliance checking
- Exception handling procedures

**Authority Reference:** Maps to Layer 08 controls; implements Layer 05 strategic governance

---

## Relationship and Hierarchy

**Parent-Child Model:**

```
Layer 02: Control Architecture (Master Control Matrix)
    ↓
    ├─ Defines: API-SEC-01 (API security), API-LC-01 (API lifecycle)
    ↓
Layer 05: API Governance Framework (Strategic)
    ├─ Authority: API Governance Lead
    ├─ Document: 1,022 lines
    ├─ Scope: Design principles, lifecycle stages, versioning strategy
    ├─ Decisions: "APIs must use semantic versioning with 6-month migration"
    ├─ Applies to: ALL organizational APIs
    ↓
Layer 08: API Governance Standard (Operational)
    ├─ Authority: Development teams (with Layer 05 constraints)
    ├─ Document: 269 lines (core) + annexes (implementation details)
    ├─ Scope: Technical implementation of Layer 05 principles
    ├─ Details: "Implement semantic versioning with automated SemVer checking in CI/CD"
    ├─ Tools: GitHub Actions gate → prevents non-compliant version tags
    └─ Applies to: Development teams building APIs
```

**Audit Trail:**

| Audit Question                               | Answer                                                                                     | Authority             | Evidence Location                                         |
| -------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------- | --------------------------------------------------------- |
| What is the API security policy?             | Layer 05 API_GOVERNANCE_FRAMEWORK                                                          | API Governance Lead   | 05_DOMAIN_FRAMEWORKS/README.md                            |
| How do we implement API security?            | Layer 08 API_GOVERNANCE_STANDARD                                                           | Development team lead | 08_DEVELOPER_GOVERNANCE_LAYER/02_API_GOVERNANCE/README.md |
| Where does versioning requirement come from? | Layer 05 Section: "Versioning and Stability"                                               | Policy authority      | API_GOVERNANCE_FRAMEWORK.md line 180-210                  |
| How is versioning implemented?               | Layer 08 Section: "Version Tag Validation"                                                 | Technical authority   | API_GOVERNANCE_STANDARD.md + CI/CD gate                   |
| Who decides if an exception is granted?      | Layer 05: API Governance Lead Layer 08: Development Lead (escalates to Layer 05 if needed) | Hierarchical approval | GOVERNANCE_CHARTER.md authorities                         |

---

## No Duplication; Clear Boundary

**Critical Clarification:**

These are NOT duplicate documents. They serve different purposes:

| Dimension                | Layer 05 (Framework)                                | Layer 08 (Standard)                                                     |
| ------------------------ | --------------------------------------------------- | ----------------------------------------------------------------------- |
| **Audience**             | Architects, policy makers                           | Developers, DevOps, QA                                                  |
| **Read Time**            | 30-40 minutes (strategic)                           | 15-20 minutes (tactical)                                                |
| **Decision Level**       | "What must be true?"                                | "How do we prove it?"                                                   |
| **Change Frequency**     | Annual review; strategic changes rare               | Quarterly updates; tooling updates regular                              |
| **Approval Authority**   | API Governance Lead + executive sponsor             | Development team lead + Layer 05 veto                                   |
| **Content Examples**     | "Backward compatibility required for 6 months"      | "Implement SemVer checking: `v1.2.3` format enforced by regex in CI/CD" |
| **References Standards** | OWASP Top 10, OpenAPI Spec, industry best practices | NIST SSDF, GitHub Actions, specific frameworks                          |

---

## Enforcement Hierarchy

**Question:** What if Layer 05 and Layer 08 conflict?

**Answer:** Layer 05 wins; Layer 08 must be updated.

```
Conflict Resolution Process:
1. Developer identifies conflict (Layer 05 requirement vs. Layer 08 implementation)
2. Escalates to Development Lead
3. Development Lead consults with API Governance Lead
4. Options:
   a) Layer 08 revised to better implement Layer 05
   b) Layer 05 clarified (strategic requirement was ambiguous)
   c) Exception granted (documented and time-limited)
5. Resolution documented in both documents' "Amendment Log"
```

---

## Cross-Referencing for Auditors

**Audit Navigation:**

To verify API security compliance, audit should:

1. **Start at Layer 05** (strategic requirements)
   - Question: "What is required for API security?"
   - Answer: API_GOVERNANCE_FRAMEWORK.md Section: "Security by Default"
   - Evidence: Framework document

2. **Map to Layer 08** (implementation)
   - Question: "How do we verify APIs implement the framework?"
   - Answer: API_GOVERNANCE_STANDARD.md Section: "Authentication Implementation"
   - Evidence: CI/CD gates, code review checklist, test results

3. **Verify Compliance** (execution)
   - Question: "Is this API compliant?"
   - Answer: Check API against Layer 08 standard; trace exceptions to Layer 05
   - Evidence: API audit checklist, exception log, remediation plans

---

## Version Control and Updates

**Layer 05 (API_GOVERNANCE_FRAMEWORK.md):**

- Version: 2.0 (effective 2026-02-14)
- Change Control: Annual review; major changes require executive approval
- Backward Compatibility: Yes; breaking changes deprecated with 6-month notice period
- Amendment Process: Strategic amendment committee approval required

**Layer 08 (API_GOVERNANCE_STANDARD.md + Annexes):**

- Version: 1.0 (effective 2026-02-14)
- Change Control: Tactical updates per sprint; no formal approval
- Backward Compatibility: Yes; tool updates must remain compatible with Layer 05
- Amendment Process: Development team lead decision; escalate if Layer 05 conflict

---

## References for Auditors

**To Verify Authority Clarity:**

1. Read GOVERNANCE_CHARTER.md (Layer 04) for role definitions
   - API Governance Lead: strategic authority
   - Development Lead: operational authority
   - CISO: security oversight

2. Read MASTER_CONTROL_MATRIX (Layer 00) for control references
   - EATGF-API-SEC-01: API security control
   - EATGF-API-LC-01: API lifecycle control
   - Map to Layer 05 and Layer 08

3. Review exception log (stored in 06_AUDIT_AND_ASSURANCE)
   - Documents cases where Layer 05 requirements modified
   - Shows Layer 05 → Layer 08 amendment process

4. Check CI/CD gates for Layer 08 enforcement
   - Verify that Layer 05 requirements verified in CI/CD
   - Review policy-as-code (OPA/Rego) for policy mapping

---

## Conclusion

**API Governance in EATGF:**

- **Layer 05** = "The Law" (what is required; strategic; rarely changes)
- **Layer 08** = "The Implementation" (how to comply; tactical; regular updates)
- **No conflict:** Layer 05 is parent; Layer 08 implements
- **Clear audit trail:** Any API can be traced to Layer 05 requirement through Layer 08 implementation

## Amendment Log

| Date       | Amendment        | Authority | Reason                            |
| ---------- | ---------------- | --------- | --------------------------------- |
| 2026-02-16 | Initial document | CISO      | Clarify audit authority questions |

## Version History

| Version | Date       | Change Type | Description                               |
| ------- | ---------- | ----------- | ----------------------------------------- |
| 1.0     | 2026-02-16 | Major       | Initial authority hierarchy clarification |
