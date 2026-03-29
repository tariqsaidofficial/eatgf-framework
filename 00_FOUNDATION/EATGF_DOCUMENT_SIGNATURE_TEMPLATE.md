# EATGF Document Signature Template

## Purpose

This document defines the mandatory structural and writing standard for all official documents published under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It ensures:

- **Structural consistency**
- **Governance traceability**
- **Cross-standard alignment**
- **Developer applicability**
- **Audit defensibility**
- **Publication readiness**

**No document may be published inside the EATGF Authority Repository without complying with this template.**

---

## Architectural Position

Every document must explicitly declare:

### EATGF Layer Placement
(e.g., 00_FOUNDATION / 02_CONTROL_ARCHITECTURE / 08_DEVELOPER_IMPLEMENTATION_LAYER)

### Governance Scope
(Policy / Architecture / Control Definition / Implementation Standard / Audit Methodology)

### Control Authority Relationship
(Does this document define controls? Interpret controls? Implement controls?)

**Example:**

- **Layer:** 02_CONTROL_ARCHITECTURE
- **Scope:** Control Interpretation & Mapping
- **Authority:** References MASTER_CONTROL_MATRIX as the sole control source

This prevents duplication and authority conflicts.

---

## Governance Principles

Each document must state the governance principles it enforces, for example:

- **Single Source of Truth**
- **Control-Centric Architecture**
- **Security-by-Design**
- **Versioned Governance**
- **Developer-Operational Alignment**
- **Audit Traceability**

These principles must align with EATGF baseline philosophy.

---

## Technical Implementation

If the document contains technical material:

- All code examples must use fenced blocks.
- Language must be explicitly declared.
- Production-grade examples only.
- Inline comments allowed, but concise.

**Example:**

```python
# Enforce branch protection using GitHub API
import requests

response = requests.put(
    "https://api.github.com/repos/org/repo/branches/main/protection",
    headers={"Authorization": "Bearer <TOKEN>"},
    json={"required_status_checks": {"strict": True}}
)
```

**No toy examples.**
**No pseudo-code unless explicitly marked as conceptual.**

---

## Control Mapping

Every document must include explicit mapping to:

- **ISO/IEC 27001:2022** (Annex A references)
- **NIST SP 800-218** (SSDF practices)
- **OWASP** (ASVS / SAMM / Top 10 where applicable)
- **COBIT 2019** (Primary + Supporting domain references)

Mapping must be structured and explicit.

**Example:**

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Version Governance | A.8.32 Change Management | PW.3 | SAMM Governance | BAI06 |

**No vague references allowed.**

---

## Developer Checklist

Every document must contain a practical checklist:

- Actionable
- Role-specific
- Implementation-oriented

**Example:**

- [ ] Branch protection rules enabled
- [ ] CI required checks enforced
- [ ] Tagged releases follow semantic versioning
- [ ] Changelog maintained

This ensures operational usability.

---

## Governance Implications

Explain:

- **Risk if not implemented**
- **Operational impact**
- **Audit consequences**
- **Cross-team dependencies**

This section connects theory to consequence.

---

## Official References

Only primary sources allowed:

- NIST SP publications
- ISO standards
- OWASP official documentation
- COBIT (ISACA)

**No blogs.**
**No Wikipedia.**
**No academic summaries.**

References must be named formally (no footnotes required).

---

## Writing Standard Enforcement

All EATGF documents must follow:

- Clear professional tone
- No emojis
- No decorative formatting
- Balanced spacing
- Structured headings only
- No hidden HTML

Documents must be ready for Docusaurus publication without modification.

---

## Version Discipline

Each document must declare:

- Version number
- Change type (Major / Minor / Patch)
- Date of issue
- Relation to EATGF baseline

Structural changes require version increment.

---

## Authority Rule

If a document conflicts with:

- MASTER_CONTROL_MATRIX
- Governance Charter
- Official Naming Freeze

**The higher authority document prevails.**

---

## Status

This template is now the **mandatory structural standard** for:

- Version Governance Policy (refactor next)
- Git Governance Policy (refactor after)
- Architecture Diagram document (refactor after)
- All future Developer Implementation Layer documents
