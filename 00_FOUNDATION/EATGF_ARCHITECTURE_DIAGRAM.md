---
sidebar_label: "EATGF Architecture Model & Structural Diagram"
---

# EATGF Architecture Model & Structural Diagram

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**

**Version:** 1.1
**Layer:** Foundation
**Status:** Structured Refactor

---

## Purpose

This document defines the formal architectural structure of the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It provides:

- Layered governance model
- Structural separation of concerns
- Control authority positioning
- Relationship between Enterprise Backbone and Developer Layer
- Diagrammatic representation of framework hierarchy

The architecture ensures that governance logic, operational controls, and developer guidance remain structurally aligned and non-duplicative.

---

## Architectural Position

**EATGF Layer:** Foundation

**Scope:** Meta-Architecture Definition

**Authority Relationship:** Defines structural topology of all EATGF layers

This document governs how the framework is organized, not how individual controls operate.

---

## Governance Principles

- Single Control Authority (MCM is exclusive source of controls)
- Layered Separation (Foundation ≠ Management ≠ Developer Guidance)
- Non-Duplication of Controls
- Explicit Mapping to International Standards
- Scalability Across Organization Sizes
- Audit Traceability by Design

**The architecture prevents structural drift and duplication.**

---

## Technical Implementation

### 1. EATGF Layer Taxonomy

```
Foundation
Management Systems
Control Architecture
Governance Models
Policy Layer
Domain Frameworks
Audit and Assurance
Reference and Evolution
08_DEVELOPER_LAYER (Planned Integration)
```

### 2. Structural Hierarchy Diagram

```
                        ┌───────────────────────────┐
                        │        Foundation       │
                        │  Identity / Version / MCM  │
                        └──────────────┬────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
┌──────────────┐              ┌──────────────┐              ┌──────────────┐
│01_MANAGEMENT │              │02_CONTROL    │              │03_GOVERNANCE │
│SYSTEMS       │              │ARCHITECTURE  │              │MODELS        │
│(ISMS/AIMS)   │              │(Mappings)    │              │(Maturity)    │
└──────────────┘              └──────────────┘              └──────────────┘
        │                              │                              │
        └──────────────┬───────────────┴──────────────┬───────────────┘
                       │                              │
              ┌──────────────┐               ┌──────────────┐
              │04_POLICY     │               │05_DOMAIN     │
              │LAYER         │               │FRAMEWORKS    │
              └──────────────┘               └──────────────┘
                       │                              │
                       └──────────────┬───────────────┘
                                      │
                              ┌──────────────┐
                              │06_AUDIT      │
                              │ASSURANCE     │
                              └──────────────┘
                                      │
                              ┌──────────────┐
                              │08_DEVELOPER  │
                              │LAYER         │
                              └──────────────┘
```

### 3. Control Authority Model

- **MASTER_CONTROL_MATRIX (MCM)** is the sole control definition source.
- All layers reference MCM.
- No layer defines new standalone controls without MCM update.
- Developer Layer implements, not redefines.

### 4. Enterprise Backbone vs Developer Layer

| Component           | Role                                        |
| ------------------- | ------------------------------------------- |
| Enterprise Backbone | Governance, compliance, audit defensibility |
| Developer Layer     | Secure implementation guidance              |
| MCM                 | Control authority                           |
| Management Systems  | ISO-aligned governance                      |
| Developer Modules   | Implementation playbooks                    |

**The two coexist without conflict.**

### 5. Mermaid Diagram Source

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'fontSize': '14px',
    'fontFamily': 'Segoe UI, -apple-system, sans-serif',
    'lineColor': '#4b5563',
    'primaryTextColor': '#1f2937'
  }
}}%%

graph LR
  MCM["<b>Master Control Matrix</b><br/>35 Controls"]
  ISMS["ISMS<br/>ISO 27001"]
  AIMS["AIMS<br/>ISO 42001"]
  SOA["SoA"]
  CO["Control<br/>Objectives"]
  RF["Risk<br/>Framework"]
  FM["Framework<br/>Mappings"]
  IAP["Internal<br/>Audit"]
  ER["Evidence"]
  GC["Charter"]
  ISP["Security<br/>Policy"]
  DGP["Data<br/>Policy"]
  AIGF["AI Framework"]
  APIGF["API Framework"]
  MM["Maturity Model"]
  PM["Performance Model"]
  GTS["Team Size"]
  RD["Roadmap"]

  MCM -->|scope| ISMS
  MCM -->|scope| AIMS
  MCM -->|scope| SOA
  MCM -->|define| CO
  MCM -->|establish| RF
  MCM -->|map| FM
  MCM -->|enforce| GC
  MCM -->|enforce| ISP
  MCM -->|enforce| DGP
  CO -->|measure| MM
  CO -->|track| PM
  CO -->|scale| GTS
  CO -->|specialize| AIGF
  CO -->|specialize| APIGF
  ISP -->|rules| APIGF
  ER -->|evidence| IAP
  IAP -->|audit| ISMS
  IAP -->|audit| AIMS
  IAP -->|validate| MCM
  IAP -->|findings| RF
  RF -->|updates| MCM
  RD -->|track| MCM
  FM -.->|ISO27001| ISMS
  FM -.->|ISO42001| AIMS
  FM -.->|COBIT| CO

  style MCM fill:#0d9488,stroke:#0f766e,stroke-width:4px,color:#fff,font-weight:bold
  style CO fill:#0369a1,stroke:#0c4a6e,stroke-width:2px,color:#fff
  style RF fill:#0369a1,stroke:#0c4a6e,stroke-width:2px,color:#fff
  style FM fill:#0369a1,stroke:#0c4a6e,stroke-width:2px,color:#fff
  style IAP fill:#d97706,stroke:#b45309,stroke-width:2px,color:#fff
  style ISMS fill:#6366f1,stroke:#4f46e5,stroke-width:2px,color:#fff
  style AIMS fill:#6366f1,stroke:#4f46e5,stroke-width:2px,color:#fff
  style SOA fill:#6366f1,stroke:#4f46e5,stroke-width:2px,color:#fff
  style GC fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff
  style ISP fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff
  style DGP fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff
  style AIGF fill:#d946ef,stroke:#be185d,stroke-width:2px,color:#fff
  style APIGF fill:#d946ef,stroke:#be185d,stroke-width:2px,color:#fff
  style MM fill:#ec4899,stroke:#be185d,stroke-width:1px,color:#fff
  style PM fill:#ec4899,stroke:#be185d,stroke-width:1px,color:#fff
  style GTS fill:#ec4899,stroke:#be185d,stroke-width:1px,color:#fff
  style ER fill:#6b7280,stroke:#4b5563,stroke-width:2px,color:#fff
  style RD fill:#6b7280,stroke:#4b5563,stroke-width:2px,color:#fff
```

---

## Control Mapping

| Architectural Aspect            | ISO 27001:2022 | NIST SSDF | OWASP               | COBIT |
| ------------------------------- | -------------- | --------- | ------------------- | ----- |
| Governance Structure            | A.5.1          | PO.1      | SAMM Governance     | EDM02 |
| Change Governance               | A.8.32         | PW.3      | SAMM Implementation | BAI06 |
| Secure Development Architecture | A.8.28         | PW.7      | ASVS V1             | BAI03 |
| Audit Architecture              | A.5.35         | RV.1      | —                   | MEA03 |

Architecture model ensures structural compliance alignment.

---

## Developer Checklist

Before adding new content:

- [ ] Identify correct EATGF layer
- [ ] Confirm no duplication of controls
- [ ] Map to MCM control ID
- [ ] Include ISO/NIST/OWASP/COBIT mapping
- [ ] Confirm architectural consistency
- [ ] Validate placement within taxonomy

**No document may exist outside defined layers.**

---

## Governance Implications

Without architectural discipline:

- Control duplication occurs
- Standards mapping fragments
- Audit scope becomes unclear
- Developer guidance conflicts with governance backbone
- Public portal loses structural credibility

**Architecture governance preserves institutional authority.**

---

## Official References

- ISO/IEC 27001:2022 – A.5.1 Policies
- ISO/IEC 27001:2022 – A.8.28 Secure Development
- NIST SP 800-218 (SSDF) – PO.1, PW.7
- COBIT 2019 – EDM02, BAI03
- OWASP SAMM – Governance & Architecture

---

**Document Version:** 1.1
**Change Type:** Structured Refactor
**Baseline Compatibility:** EATGF-v1.0-Foundation Compatible
