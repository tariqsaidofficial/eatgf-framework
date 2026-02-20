# METADATA_GOVERNANCE_RULES_v1.1

**Purpose:**
Establishes binding, immutable rules for metadata governance of the EATGF Registry and any dependent Engine. This document is normative and must be referenced by the Registry Schema. Any modification requires a formal Architectural Decision Record (ADR).

**Scope:**
- Applies to all EATGF domains (EDM, DSS, BAI, APO, etc.)
- Governs all registry metadata, control identity, authority binding, versioning, evidence, applicability, lifecycle, decomposition, relationships, and mutation rules
- Required reading before any Engine implementation or registry modification

---

## 1. Control Identity Governance
1.1 Control ID is immutable and unique. No reuse, renumbering, reclassification, or migration between domains. Any substantive change requires a new Control ID.
1.2 ID Naming Convention (frozen):
- Format: EATGF-{DOMAIN}-{CATEGORY}-{NN}
- DOMAIN: fixed (e.g., EDM, DSS)
- CATEGORY: functional abbreviation (e.g., GOV, RISK)
- NN: sequential number within category

## 2. Authority Binding Rules
2.1 Every control must bind to:
- Standard Name
- Standard Version
- Clause Identifier
- Authority Class
2.2 Authority Version Lock: Controls are bound to the standard version at activation. No update on new standard release; if clause meaning changes, a new control is created.
2.3 Secondary Alignment: Allowed (NIST, OWASP, COBIT, ISO), but does not override or create multi-parent authority.

## 3. Versioning Model
3.1 Distinction between Framework Version (e.g., EATGF v1.1) and Control Version (fixed after activation).
3.2 Pre-activation: controls editable, no version increment.
3.3 Post-activation: any substantive change → new Control ID. Only non-substantive metadata updates allowed.

## 4. Change Classification Matrix
| Change Type                        | Allowed After Activation | Action                |
|------------------------------------|-------------------------|-----------------------|
| Typo Fix                           | Yes                     | Metadata patch        |
| Clarification (non-substantive)    | Yes                     | Logged                |
| Evidence descriptor clarification  | Yes                     | Logged                |
| Secondary alignment update         | Yes                     | Logged                |
| Atomic objective modification      | No                      | New Control ID        |
| Scope expansion/reduction          | No                      | New Control ID        |
| Authority change                   | No                      | New Control ID        |
| Decomposition change               | No                      | ADR + New Control ID  |
| Applicability fundamental change   | No                      | New Control ID        |

## 5. Evidence Contract
5.1 Evidence is external to the registry; only descriptors, type, frequency, verification method, and responsible role are stored.
5.2 Required fields for each control:
- evidence_expected_type (policy, log, dashboard, report, etc.)
- evidence_owner_role
- verification_method
- verification_frequency
- retention_expectation
Control without evidence contract is incomplete.

## 6. Applicability Rules
6.1 Applicability dimensions (frozen):
- Environment Type: Cloud, SaaS, On-Prem, Hybrid
- AI Usage: AI-enabled, Non-AI
6.2 Conditional controls must specify explicit trigger condition and NOT_APPLICABLE case, clearly separated from NON_COMPLIANT.

## 7. Lifecycle Governance
7.1 Allowed states: Draft, Approved, Active, Deprecated, Sunset, Retired
7.2 Activation is batch-wide, framework-level, with effective date, and occurs once only.
7.3 Post-activation: append-only, deprecation/sunset allowed, metadata clarifications only, no rewriting history, no retroactive authority change.

## 8. Decomposition Policy
8.1 Conditional decomposition allowed (max 2 controls per clause per domain), with layer distinction, no functional overlap, full clause coverage, explicit documentation. Violation invalidates decomposition.

## 9. Relationship Policy
9.1 Relationship types (frozen): DERIVES_FROM, IMPLEMENTS, ENFORCES, REQUIRES
9.2 REQUIRES only when control cannot be valid without dependency; not for optimization or sequencing.

## 10. Post-Activation Mutation Rules
- Registry is append-only after activation
- No silent scope or authority changes
- All changes logged and auditable

---

**Normative Status:**
This document is normative. It must be referenced by the Registry Schema and is required for any audit, engine implementation, or registry change. Modification is only allowed via formal ADR process.

**Version:** v1.1
**Date of Issue:** 2026-02-16
**Change Type:** Major (Initial Freeze)
**Relation to EATGF Baseline:** Baseline-defining
