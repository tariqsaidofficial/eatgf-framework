---
sidebar_label: "Annex v1.1 – Technical Details"
---

# Annex v1.1 – Technical Details

## Table of Contents

1. Registry JSON Schema
2. Control Field Reference
3. Compliance Engine CLI Usage
4. Evidence Model
5. Sample Compliance Report (JSON)
6. Negative Matrix Test Cases
7. Versioning & ADR Policy
8. Evidence Metrics Status (v1.1)

---

## Registry Top-Level Structure

```json
{
  "version": "1.1",
  "controls": [
    // ...control objects...
  ]
}
```

**Notes:**

- `version` is immutable and uniquely identifies the registry release.
- The registry is append-only. No in-place mutation is allowed post-activation.
- Control IDs are immutable and must never be reused or altered.

---

## Example Control (Audit-Grade, 1:1 with Canonical Registry)

### EATGF-EDM-GOV-01

```json
{
  "control_id": "EATGF-EDM-GOV-01",
  "domain": "EDM",
  "primary_authority": "ISO 27001 A.5.3",
  "authority_class": "ISO27001",
  "atomic_objective": "Establish and maintain formal governance operating structure with clearly defined organizational roles, decision rights, committee authorities, and escalation mechanisms for IT and AI governance.",
  "lifecycle_state": "Approved",
  "applicability": {
    "environments": ["Cloud", "SaaS", "On-Prem", "Hybrid"],
    "ai_usage": "All",
    "mandatory": true
  },
  "relationships": {
    "implements": [],
    "enforces": [],
    "requires": []
  }
}
```

**Operational Artifact Note:**
If `implements` and `enforces` are empty, operational artifacts (e.g., Governance Charter, RACI Matrix, Committee Charters, Internal Audit, Board Governance Review) are documented in governance documentation and are not structurally enforced in registry relationships. This is a deliberate design for structural minimalism and audit clarity.

---

## Evidence Metrics Status (v1.1)

- `evidence_metrics` is present structurally in the evidence model.
- `evidence_metrics` is ignored by v1.1 scoring and reporting.
- `evidence_metrics` is reserved for v1.2+ structured evaluation extensions.

---
