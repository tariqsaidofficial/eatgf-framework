# ENGINE_BASELINE_v1.1

**EATGF Engine Baseline – Version 1.1**

## Status

- Registry Schema: Frozen
- Domains: EDM (Governance), DSS (Security) – Closed
- Loader: Stable
- Validator: Stable
- Cycle Detection: Stable
- Compliance Engine: Deterministic
- Reporting: Audit-grade
- Engine State: Production-ready

## Determinism Verification

- Multiple runs produce identical compliance reports (except timestamp)
- No random ordering, no float drift, no missing fields
- Controls and domains sorted deterministically

## Negative Matrix Validation

- Unknown control: Fail-fast
- Invalid status: Fail-fast
- Wrong evidence_metrics type: Fail-fast
- Empty evidence: All controls NOT_TESTED, score = 0.0%
- Partial evidence: Only provided controls resolved, others NOT_TESTED
- API conditional: Applicability logic confirmed

## Cycle Detection

- REQUIRES graph validated, no cycles detected
- Cross-domain dependencies supported

## Reporting Contract

- JSON output, machine-readable, audit-grade
- Fixed structure, no optional fields, no interpretation
- Compliance score: count-based, unweighted
- NOT_TESTED policy: documented, counted as non-compliant

## Canonical Verification Set

- registry_v1.1.json (immutable)
- org_profile.json (reference)
- evidence.json (reference)
- compliance_report.json (reference output)

## Scope

- Domains: EDM, DSS only
- No weights, no scoring logic beyond count-based
- No strict mode, no domain expansion

## Lifecycle State

- Approved (pre-activation)

## Freeze Declaration

- Engine v1.1 is now frozen as production baseline
- Any change requires formal ADR and new version tag

**Date of Freeze:** 2026-02-16
**Git Tag:** v1.1.0
