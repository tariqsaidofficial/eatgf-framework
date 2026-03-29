# EATGF Architecture Model & Structural Diagram

**Enterprise AI-Aligned Technical Governance Framework (EATGF)**

**Version:** 1.1
**Layer:** 00_FOUNDATION
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

**EATGF Layer:** 00_FOUNDATION

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
00_FOUNDATION
01_MANAGEMENT_SYSTEMS
02_CONTROL_ARCHITECTURE
03_GOVERNANCE_MODELS
04_POLICY_LAYER
05_DOMAIN_FRAMEWORKS
06_AUDIT_AND_ASSURANCE
07_REFERENCE_AND_EVOLUTION
08_DEVELOPER_LAYER (Planned Integration)
```

### 2. Structural Hierarchy Diagram

```
                        ┌───────────────────────────┐
                        │        00_FOUNDATION       │
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
    'fontFamily': 'Inter, system-ui, sans-serif'
  }
}}%%

flowchart TD

  subgraph L00["<b>LAYER 00 — FOUNDATION</b>"]
    direction LR
    MCM["<b>MASTER CONTROL MATRIX</b><br/>35 Controls | Single Authority<br/>EATGF-[DOMAIN]-[CATEGORY]-[NUM]"]
    BD["Baseline Declaration"]
    OD["Official Designation"]
  end

  subgraph L01["<b>LAYER 01 — MANAGEMENT SYSTEMS</b>"]
    direction LR
    ISMS["<b>ISMS</b><br/>ISO/IEC 27001:2022"]
    AIMS["<b>AIMS</b><br/>ISO/IEC 42001:2023"]
    SOA["Statement of<br/>Applicability"]
  end

  subgraph L02["<b>LAYER 02 — CONTROL ARCHITECTURE</b>"]
    direction LR
    CO["Control Objectives"]
    RF["Risk Framework"]
    FM["Framework Mappings<br/>COBIT | NIST | ISO"]
  end

  subgraph L03["<b>LAYER 03 — GOVERNANCE MODELS</b>"]
    direction LR
    MM["Maturity Model"]
    PM["Performance Model"]
    GTS["Governance by<br/>Team Size"]
  end

  subgraph L04["<b>LAYER 04 — POLICY LAYER</b>"]
    direction LR
    GC["Governance Charter"]
    ISP["Information Security<br/>Policy"]
    DGP["Data Governance<br/>Policy"]
  end

  subgraph L05["<b>LAYER 05 — DOMAIN FRAMEWORKS</b>"]
    direction LR
    AIGF["AI Governance<br/>Framework"]
    APIGF["API Governance<br/>Framework"]
  end

  subgraph L06["<b>LAYER 06 — AUDIT & ASSURANCE</b>"]
    direction LR
    IAP["Internal Audit<br/>Procedure<br/>ISO 19011:2018"]
    ER["Evidence Register"]
  end

  subgraph L07["<b>LAYER 07 — REFERENCE & EVOLUTION</b>"]
    direction LR
    RD["Roadmap &<br/>Decision Records"]
    CL["Changelog &<br/>Version History"]
  end

  %% --- PRIMARY GOVERNANCE FLOW (top-down) ---
  MCM -->|"defines controls for"| ISMS
  MCM -->|"defines controls for"| AIMS
  MCM -->|"scopes applicability"| SOA

  MCM -->|"provides objectives to"| CO
  MCM -->|"establishes risk criteria"| RF
  MCM -->|"maps to external standards"| FM

  CO -->|"measured by"| MM
  CO -->|"tracked by"| PM
  CO -->|"scaled by edition"| GTS

  MCM -->|"enforced through"| GC
  MCM -->|"enforced through"| ISP
  MCM -->|"enforced through"| DGP

  CO -->|"specialized into"| AIGF
  CO -->|"specialized into"| APIGF
  ISP -->|"domain rules for"| APIGF

  %% --- ASSURANCE FLOW (bottom-up) ---
  IAP -->|"audits compliance of"| ISMS
  IAP -->|"audits compliance of"| AIMS
  IAP -->|"validates controls in"| MCM
  ER -->|"stores evidence for"| IAP

  %% --- FEEDBACK LOOP ---
  IAP -->|"findings feed into"| RF
  RF -->|"risk updates to"| MCM
  RD -->|"evolution tracked in"| MCM

  %% --- LATERAL MAPPINGS ---
  FM -.->|"ISO 27001:2022"| ISMS
  FM -.->|"ISO 42001:2023"| AIMS
  FM -.->|"COBIT 2019"| CO

  %% --- STYLING ---
  style L00 fill:#1a365d,stroke:#2d5591,color:#fff,stroke-width:3px
  style L01 fill:#22543d,stroke:#38a169,color:#fff,stroke-width:2px
  style L02 fill:#7b341e,stroke:#c05621,color:#fff,stroke-width:2px
  style L03 fill:#44337a,stroke:#805ad5,color:#fff,stroke-width:2px
  style L04 fill:#742a2a,stroke:#c53030,color:#fff,stroke-width:2px
  style L05 fill:#234e52,stroke:#38b2ac,color:#fff,stroke-width:2px
  style L06 fill:#744210,stroke:#d69e2e,color:#fff,stroke-width:2px
  style L07 fill:#4a5568,stroke:#a0aec0,color:#fff,stroke-width:2px

  style MCM fill:#2b6cb0,stroke:#1a365d,color:#fff,stroke-width:4px
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
