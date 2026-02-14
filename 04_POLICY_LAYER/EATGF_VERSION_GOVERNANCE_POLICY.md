# EATGF Version Governance Policy

## Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field | Value |
|-------|-------|
| Document Type | Policy |
| Version | 1.0 |
| Classification | Internal |
| Effective Date | 2026-02-14 |
| Authority | Enterprise Architecture & Governance Office |
| MCM Reference | EATGF-GOV-DOC-004 |

---

## 1. Purpose

This document establishes the version governance policy for the Enterprise AI-Aligned Technical Governance Framework (EATGF). It defines baseline freeze rules, version increment models, control modification impact scoring, deprecation and archival rules, edition branching strategy, public portal versioning, and changelog structure.

## 2. Scope

This policy applies to:

- All versioned content within the EATGF authority repository (`tariqsaidofficial/eatgf-framework`)
- All 8 governance layers (00–07) and their constituent documents
- The Master Control Matrix and all control definitions
- The public portal version display and version history
- Edition-specific content variants (Startup, SaaS, Enterprise)

This policy does not govern the version of the portal application itself (Docusaurus, Node.js dependencies), which is managed by the portal maintainer through standard package management.

## 3. Definitions

| Term | Definition |
|------|-----------|
| Baseline | A declared, immutable snapshot of the framework at a specific version tag. Once frozen, a baseline cannot be modified. |
| Version Increment | A change to the version identifier following semantic versioning rules (Major.Minor.Patch). |
| Control Modification Impact Score | A numeric assessment (1–10) of the governance significance of a change to an MCM control. |
| Deprecation | The formal process of marking a document as superseded, with a defined transition period before archival. |
| Archival | The permanent transfer of a deprecated document to the Reference & Evolution layer (Layer 07) in a read-only state. |
| Edition | A tailored variant of the framework scaled for a specific organizational size (Startup, SaaS, Enterprise). |

## 4. Responsibilities

| Role | Responsibility |
|------|---------------|
| Framework Owner | Declares baselines, approves major version increments, and authorizes deprecation |
| Governance Reviewer | Validates control modification impact scores and version increment classification |
| Document Author | Assigns initial impact scores and maintains version history in Document Control blocks |
| Portal Maintainer | Executes Docusaurus versioning commands and maintains the version dropdown |

---

## 5. Baseline Freeze Rules

### 5.1 Declaration

A baseline freeze is declared when the following conditions are met:

1. All documents in the target scope pass the 10-element Document Signature Template compliance check (per DOCUMENTATION_STYLE_REVIEW_REPORT.md).
2. The Master Control Matrix contains no unresolved control taxonomy conflicts.
3. All cross-references between layers are validated (no broken internal links).
4. A Baseline Declaration document is authored and approved (per BASELINE_DECLARATION_v1.0.md precedent).
5. An annotated Git tag is created on the `main` branch.

### 5.2 Immutability

Once a baseline is declared:

1. The tagged commit is permanently immutable. The tag shall not be deleted or force-pushed.
2. No changes may be made to any file at the tagged commit — corrections create a new version.
3. The Baseline Declaration document is part of the frozen state and is itself immutable.
4. The frozen state includes all 8 layers and their directory structure at that commit.

### 5.3 Correction of Frozen Baselines

If an error is discovered in a frozen baseline:

1. A new patch version is created (e.g., v1.0.0 → v1.0.1).
2. The correction is documented in the changelog with a reference to the frozen baseline.
3. The frozen baseline tag remains intact — it is never modified.
4. The correction carries a `FIX` commit type per the Git Governance Policy.

---

## 6. Version Increment Model

### 6.1 Semantic Versioning

The EATGF uses semantic versioning with governance-specific interpretation:

```
vMAJOR.MINOR.PATCH
```

| Component | Increment Trigger | Examples |
|-----------|------------------|----------|
| **PATCH** (v1.0.X) | Editorial corrections that do not alter meaning, scope, or authority | Typo fix, formatting correction, broken link repair, clarification of existing text without scope change |
| **MINOR** (v1.X.0) | Content additions or updates that do not alter the control taxonomy or framework architecture | New policy document, section addition, framework mapping extension, governance model update, evidence specification addition |
| **MAJOR** (vX.0.0) | Changes that alter the control taxonomy, framework layer structure, or architectural boundaries | MCM control addition/removal, layer restructuring, control ID format change, edition model redesign, management system scope change |

### 6.2 Version Increment Decision Matrix

| Change Type | Impact Score | Version Increment | Approval |
|-------------|-------------|-------------------|----------|
| Editorial correction | 1–2 | Patch | 1 reviewer |
| Content clarification | 2–3 | Patch | 1 reviewer |
| New section in existing document | 3–4 | Minor | 1 reviewer |
| New document addition | 4–5 | Minor | 2 reviewers |
| Policy expansion | 5–6 | Minor | 2 reviewers + Framework Owner |
| Framework mapping addition | 4–5 | Minor | 2 reviewers |
| Control objective modification | 6–7 | Minor or Major | Framework Owner |
| MCM control addition | 8–9 | Major | Executive Steering Committee |
| Control taxonomy restructuring | 9–10 | Major | Executive Steering Committee |
| Layer architecture change | 10 | Major | Executive Steering Committee |

---

## 7. Control Modification Impact Scoring

### 7.1 Scoring Criteria

Every change that affects an MCM control shall be assigned an impact score on a scale of 1–10:

| Score | Severity | Definition | Downstream Impact |
|-------|----------|-----------|-------------------|
| 1 | Negligible | Formatting or typographic correction within a control field | None |
| 2 | Minimal | Clarification of a control description without scope change | None |
| 3 | Low | Update to evidence requirements or evidence type specification | Evidence Register update |
| 4 | Moderate-Low | Change to control owner assignment | RACI chart update |
| 5 | Moderate | Modification of a control's mapping to external standards | Framework Mappings update |
| 6 | Moderate-High | Change to a control objective's measurable target | Performance Model + Maturity Assessment update |
| 7 | High | Addition of a new control within an existing domain | All dependent documents update |
| 8 | High-Critical | Removal or merger of an existing control | All dependent documents + audit procedure update |
| 9 | Critical | Change to the control ID naming convention | All documents referencing control IDs update |
| 10 | Architectural | Restructuring of control domains or framework layers | Full framework review cycle |

### 7.2 Scoring Process

1. The change author assigns the initial impact score in the pull request description.
2. The Governance Reviewer validates or adjusts the score during review.
3. Changes scoring 7+ require Framework Owner review.
4. Changes scoring 9+ require Executive Steering Committee review.
5. The final impact score is recorded in the changelog entry.

---

## 8. Deprecation Rules

### 8.1 Deprecation Process

When a document is superseded by a replacement:

1. Add the following deprecation notice at the top of the document, immediately after the H1 title:

```markdown
> **DEPRECATED** — This document has been superseded by [replacement document name](relative-link).
> Deprecation Date: YYYY-MM-DD | Archival Target Date: YYYY-MM-DD
> This document remains accessible during the transition period. After the archival target date,
> it will be moved to 07_REFERENCE_AND_EVOLUTION/HISTORICAL_IMPLEMENTATION_ARTIFACTS/.
```

2. Update the Version & Status Block with a final entry recording the deprecation.
3. The replacement document shall include a reference to the deprecated document for traceability.
4. Cross-references to the deprecated document across the framework shall be updated to point to the replacement.

### 8.2 Transition Period

- Deprecated documents remain in their current directory for **2 review cycles** of the replacement document.
- Review cycle duration is defined in the replacement document's metadata (typically quarterly or semi-annually).
- During the transition period, both documents are accessible. The deprecated document is read-only.

### 8.3 Deprecation Candidates

Documents eligible for deprecation:

1. Documents superseded by a formal v2 replacement (e.g., `01_GOVERNANCE_CHARTER.md` → `GOVERNANCE_CHARTER_FORMAL_v2.md`)
2. Documents with content absorbed into other authoritative documents
3. Documents with obsolete references (e.g., pre-expansion 14-control taxonomy documents after in-place update)

---

## 9. Archival Rules

### 9.1 Archival Process

After the transition period expires:

1. Move the deprecated document to `07_REFERENCE_AND_EVOLUTION/HISTORICAL_IMPLEMENTATION_ARTIFACTS/`.
2. Add `[ARCHIVED]` prefix to the H1 title:

```markdown
# [ARCHIVED] Original Document Title
```

3. Add archival metadata block immediately after the H1:

```markdown
| Archival Field | Value |
|---------------|-------|
| Original Location | [original path] |
| Archive Date | YYYY-MM-DD |
| Archival Authority | [approver name/role] |
| Reason | Superseded by [replacement document] |
| Replacement Document | [relative link to replacement] |
```

4. The archived document is **read-only** — no further modifications are permitted.
5. Remove the deprecated document's entry from any `_category_.json` sidebar configuration (it should not appear in the portal navigation after archival, though it remains accessible via direct URL in the Reference & Evolution layer).

### 9.2 Archival Exceptions

The following documents shall not be archived regardless of age:

- Baseline Declaration documents (historical baselines are governance artifacts)
- MCM snapshots (each version represents a governance state)
- Governance approval records (PHASE_2_WEEK_1_GO_APPROVAL.md, etc.)

---

## 10. Edition Branching Rules

### 10.1 Edition Definitions

| Edition | Target Organization | Team Size | Control Scope | Version Track |
|---------|--------------------|-----------|--------------|--------------| 
| **Startup** | Early-stage organizations | 1–10 | Core controls per MCM applicability matrix | vX.Y-Startup |
| **SaaS** | Growth-stage technology organizations | 11–100 | Core + domain-specific controls | vX.Y-SaaS |
| **Enterprise** | Mature organizations with regulatory requirements | 100+ | Full 35-control MCM | vX.Y-Enterprise |

### 10.2 Edition Version Tracking

1. All editions share the same **major version** — they represent views of the same framework, not separate frameworks.
2. Edition-specific minor versions are permitted when an edition requires content not applicable to other editions.
3. The edition identifier is appended to the version tag: `EATGF-v1.0.0-Startup`, `EATGF-v1.0.0-Enterprise`.
4. Control applicability per edition is defined in GOVERNANCE_BY_TEAM_SIZE.md (Layer 03).

### 10.3 Edition Governance

1. Changes to the MCM control applicability matrix require Framework Owner approval.
2. A control marked as "Not Applicable" for an edition remains defined in the MCM — it is excluded from the edition's implementation scope, not from the framework itself.
3. Edition-specific implementation guidance is maintained in GOVERNANCE_BY_TEAM_SIZE.md, not in separate repositories or branches.

---

## 11. Public Portal Versioning

### 11.1 Docusaurus Version Snapshots

The public portal uses Docusaurus versioned documentation to maintain access to previous framework versions:

1. **Create a version snapshot** when a new major or significant minor version is tagged:

```bash
cd governance-docs-site/portal
npx docusaurus docs:version X.Y
```

2. This creates a `versioned_docs/version-X.Y/` directory containing the framework state at that version.
3. The portal navbar displays a version dropdown allowing readers to switch between versions.

### 11.2 Version Display Rules

| Location | Display Format |
|----------|---------------|
| Navbar version dropdown | `v1.0`, `v1.1`, `v2.0` |
| Footer | `EATGF v1.0 — Foundation Edition` |
| Hero banner badge | `EATGF v1.0 | Foundation Edition | Baseline Frozen YYYY-MM-DD` |
| Document header table | `Version: 1.0` (document-level version) |

### 11.3 Version Lifecycle in Portal

| Portal Version State | Meaning |
|---------------------|---------|
| **Current** | The default version shown to all readers; the latest approved baseline |
| **Maintained** | A previous version that is still referenced by adopters; accessible via dropdown |
| **Unmaintained** | A historical version that is no longer updated; accessible via dropdown with notice |
| **Archived** | Removed from the dropdown; accessible only via direct URL |

---

## 12. Changelog Structure

### 12.1 Changelog File

Maintain `07_REFERENCE_AND_EVOLUTION/CHANGELOG.md` as the authoritative record of all framework changes.

### 12.2 Changelog Format

```markdown
# EATGF Changelog

## [vX.Y.Z] — YYYY-MM-DD

### Edition
[Foundation / Startup / SaaS / Enterprise]

### Impact Classification
[Minor / Structural / Control-Affecting]

### Added
- [LAYER-NN] Description of addition (MCM Ref: EATGF-XXX-YYY-NNN)

### Changed
- [LAYER-NN] Description of change (MCM Ref: EATGF-XXX-YYY-NNN)

### Removed
- [LAYER-NN] Description of removal (MCM Ref: EATGF-XXX-YYY-NNN)

### Fixed
- [LAYER-NN] Description of correction

### Security
- [LAYER-NN] Description of security-related change (MCM Ref: EATGF-XXX-YYY-NNN)

### Governance
- Control Modification Impact Score: [1–10]
- Approval Authority: [Reviewer / Framework Owner / Executive Steering Committee]
- Baseline Freeze Status: [Active / Not applicable]
```

### 12.3 Changelog Rules

1. Every tagged version shall have a corresponding changelog entry.
2. Changelog entries shall reference affected MCM control IDs where applicable.
3. The changelog is append-only — previous entries shall not be modified.
4. Changelog entries for Control-Affecting changes shall include the impact score.

---

## 13. Governance Enforcement Rules

1. All version increments shall follow the semantic versioning model defined in Section 6.
2. Baseline freezes are irrevocable except through the Emergency Unfreeze process defined in the Git Governance Policy.
3. Control modifications scoring 7+ on the impact scale require formal governance review prior to merge.
4. Deprecated documents that exceed their transition period without archival constitute a policy violation.
5. Edition-specific changes that alter control applicability require Framework Owner approval.
6. The changelog shall be updated as part of every version tag. Tags without corresponding changelog entries shall not be created.
7. Public portal version snapshots shall be created for every major version and for minor versions that introduce new documents or policies.

---

**Document Control**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-14 | Enterprise Architecture & Governance Office | Initial version governance policy |

**Authority Sign-Off**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Framework Owner | | | |
| Chief Governance Officer | | | |
