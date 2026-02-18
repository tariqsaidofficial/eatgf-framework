# EATGF Mandatory Document Standards

## Critical Rule: All EATGF documents MUST comply with the Document Signature Template

Before creating or editing any document in the EATGF framework, you MUST follow these mandatory requirements:

## 1. Architectural Position (MANDATORY)

Every document must declare:

- **EATGF Layer Placement**: (00_FOUNDATION / 01_MANAGEMENT_SYSTEMS / 02_CONTROL_ARCHITECTURE / 03_GOVERNANCE_MODELS / 04_POLICY_LAYER / 05_DOMAIN_FRAMEWORKS / 06_AUDIT_AND_ASSURANCE / 07_REFERENCE_AND_EVOLUTION / 08_DEVELOPER_GOVERNANCE_LAYER)
- **Governance Scope**: (Policy / Architecture / Control Definition / Implementation Standard / Audit Methodology)
- **Control Authority Relationship**: (Defines controls / Interprets controls / Implements controls / References controls)

## 2. Governance Principles (MANDATORY)

State which principles apply:
- Single Source of Truth
- Control-Centric Architecture
- Security-by-Design
- Versioned Governance
- Developer-Operational Alignment
- Audit Traceability

## 3. Control Mapping (MANDATORY)

Include explicit mapping table:

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| [Context] | [Annex A ref] | [Practice] | [Standard] | [Domain] |

## 4. Developer Checklist (MANDATORY)

Provide actionable, role-specific checklist:

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

## 5. Governance Implications (MANDATORY)

Explain:
- Risk if not implemented
- Operational impact
- Audit consequences
- Cross-team dependencies

## 6. Technical Implementation Standards

When including code:
- Use fenced code blocks with language declaration
- Production-grade examples only
- No toy examples or pseudo-code (unless marked as conceptual)
- Concise inline comments only

Example:
```python
# Enforce branch protection using GitHub API
import requests

response = requests.put(
    "https://api.github.com/repos/org/repo/branches/main/protection",
    headers={"Authorization": "Bearer <TOKEN>"},
    json={"required_status_checks": {"strict": True}}
)
```

## 7. Official References Only

Use ONLY primary sources:
- NIST SP publications
- ISO standards
- OWASP official documentation
- COBIT (ISACA)

NO blogs, NO Wikipedia, NO academic summaries.

## 8. Writing Standards (MANDATORY)

- Clear professional tone
- No emojis
- No decorative formatting
- Balanced spacing
- Structured headings only
- No hidden HTML
- Ready for Docusaurus publication without modification

## 9. Version Discipline (MANDATORY)

Declare:
- Version number
- Change type (Major / Minor / Patch)
- Date of issue
- Relation to EATGF baseline

## 10. Authority Hierarchy

If conflict exists, this order prevails:
1. MASTER_CONTROL_MATRIX
2. Governance Charter
3. Official Naming Freeze
4. EATGF Document Signature Template

## Reference Document

Full template: `/eatgf-framework/00_FOUNDATION/EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md`

**NO DOCUMENT MAY BE PUBLISHED WITHOUT FULL COMPLIANCE TO THIS TEMPLATE.**
