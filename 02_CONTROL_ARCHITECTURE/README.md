---
sidebar_label: Control Architecture
sidebar_position: 1
---

# Layer 02 — Control Architecture

**EATGF Layer:** 02_CONTROL_ARCHITECTURE
**Governance Scope:** Control Definition | Architecture
**Status:** Under Active Development — v1.1-Enhanced (Q3 2026)

---

## Layer Purpose

The Control Architecture layer is the structural core of EATGF. It defines all governance controls, establishes cross-standard mappings (ISO 27001, NIST SSDF, OWASP, COBIT), and specifies the risk framework that underpins every domain implementation. This layer provides the single authoritative reference for what controls exist and how they align to regulatory and industry standards.

---

## Scope

| Control Domain                 | Coverage                                                   |
| ------------------------------ | ---------------------------------------------------------- |
| Master Control Matrix (MCM)    | 35 controls across 7 COBIT-aligned domains                 |
| ISO 27001:2022 Annex A Mapping | Full Annex A alignment for all applicable controls         |
| NIST SSDF (SP 800-218)         | Practitioner-level mapping for secure development controls |
| OWASP Alignment                | Top 10, ASVS, API Security Top 10                          |
| COBIT 2019 Domain Mapping      | DSS, APO, BAI, MEA domain cross-references                 |
| AI RMF (NIST AI 600-1)         | Govern, Map, Measure, Manage functions                     |

---

## Planned Documents

- `MASTER_CONTROL_MATRIX_v1.1.md` — Authoritative control register (35 controls, all domains)
- `CROSS_STANDARD_MAPPING_v1.1.md` — ISO / NIST / OWASP / COBIT mapping tables
- `RISK_FRAMEWORK_v1.1.md` — Control risk classification and treatment hierarchy
- `CONTROL_INHERITANCE_MODEL_v1.1.md` — Parent/child control relationships across layers

---

## Control Authority Relationship

This layer **defines controls** consumed by all downstream layers (03–07). No control may be implemented in any domain without a corresponding entry in the Master Control Matrix documented here.

**Authority:** Second only to the Foundation layer in the EATGF authority hierarchy.

---

Return to the [Framework Overview](../README.md).
