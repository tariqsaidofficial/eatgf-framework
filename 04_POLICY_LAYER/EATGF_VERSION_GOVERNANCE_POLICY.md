# EATGF_VERSION_GOVERNANCE_POLICY

| Field          | Value                                                         |
| -------------- | ------------------------------------------------------------- |
| Document Type  | Policy                                                        |
| Version        | 1.2                                                           |
| Classification | Controlled                                                    |
| Effective Date | 2026-02-14                                                    |
| Authority      | Enterprise Architecture and Governance Office                 |
| EATGF Layer    | 04_POLICY_LAYER                                               |
| MCM Reference  | EATGF-BAI-CHG-01, EATGF-BAI-CONF-01                           |
| Standards      | ISO 27001:2022 A.8.32/A.8.9, NIST SSDF PW.3/PW.4, COBIT BAI06 |

---

## Purpose

This policy defines official version governance model for EATGF framework establishing semantic versioning structure (MAJOR.MINOR.PATCH), release discipline, tagging rules, governance freeze policies, change classification standards, and cross-repository version synchronization. Version governance ensures framework structural stability, change traceability, audit defensibility, and institutional credibility. All framework releases must comply with versioning standards to maintain baseline integrity and external audit reference.

## Architectural Position

This policy operates within **04_POLICY_LAYER** as the authoritative framework version control and release management standard.

- **Upstream dependency:** Governance Charter (Layer 04) establishes change approval authority; Git Governance Policy defines branch and tag enforcement; BASELINE_DECLARATION (00_FOUNDATION) establishes version 1.0 baseline
- **Downstream usage:** All EATGF framework documents reference version numbers per this policy; CHANGELOG.md tracked in 00_FOUNDATION per release requirements; governance documentation site displays current version; audit reports reference specific version baselines
- **Cross-layer reference:** BAI-CHG-01 (Change Management) implemented through version release workflow; MEA-AUD-01 (Internal Audit) audits version compliance; MASTER_CONTROL_MATRIX remains control authority across all versions

## Governance Principles

1. **Baseline Freeze Discipline** – Published version baselines are immutable; corrections require new patch version release
2. **Semantic Versioning Integrity** – All changes classified as MAJOR (breaking changes), MINOR (additions), or PATCH (corrections) without exception
3. **Transparent Change History** – Every version includes changelog entry documenting changes, affected layers, and compatibility impact
4. **Backward Compatibility Protection** – MINOR and PATCH versions maintain backward compatibility; MAJOR versions document breaking changes and migration guidance
5. **Audit Traceability** – Git tags and version documentation provide audit trail for framework evolution and baseline verification

## Technical Implementation

### Semantic Versioning Model

EATGF versioning follows semantic versioning standard (SemVer 2.0.0):

```
MAJOR.MINOR.PATCH
```

**Version Component Definitions:**

**MAJOR Version (X.0.0):**

- Structural or architectural framework changes
- Control taxonomy modifications (control ID changes, domain restructuring)
- Breaking changes requiring organizational implementation updates
- Layer additions or removal
- Incompatible with previous major version

Examples:

- EATGF-v1.0-Foundation (Initial 14 controls)
- EATGF-v2.0-Extended (35 controls, 11 domains added)

**MINOR Version (1.X.0):**

- New domain frameworks added (e.g., Developer Governance Layer addition)
- New controls added to existing domains without breaking taxonomy
- Significant enhancements to existing documents maintaining compatibility
- New policy additions

Examples:

- EATGF-v1.1-Control-Enhancement (Control Objectives expanded)
- EATGF-v1.2-Git-Governance (Git and Version policies formalized)

**PATCH Version (1.1.X):**

- Clarifications and corrections to existing content
- Typo fixes and formatting improvements
- Documentation enhancements without control changes
- Minor evidence requirement clarifications

Examples:

- EATGF-v1.1.1 (Typo corrections in FRAMEWORK_MAPPINGS.md)
- EATGF-v1.2.1 (Formatting standardization across Layer 04 policies)

### Git Tagging Standard

All formal releases require Git tag creation:

**Tag Naming Convention:**

```
EATGF-vMAJOR.MINOR.PATCH
```

**Tag Creation Procedure:**

```bash
# Create annotated tag with descriptive message
git tag -a EATGF-v1.2.0 -m "MINOR: Git Governance and Version Governance policies formalized"

# Verify tag
git tag -l "EATGF-v*"

# Push tag to origin
git push origin EAT GF-v1.2.0
```

**For Signed Tags (Enterprise edition requirement):**

```bash
# Create GPG-signed tag
git tag -s EATGF-v1.2.0 -m "MINOR: Git Governance and Version Governance policies formalized"

# Verify signature
git tag -v EATGF-v1.2.0

# Push signed tag
git push origin EATGF-v1.2.0
```

**Tag Immutability:**

- Once pushed to origin, tags must not be deleted or modified
- Tag corrections require new patch version (e.g., EATGF-v1.2.1 replaces incorrect EATGF-v1.2.0)
- Tag tampering triggers audit investigation per DSS-INC-01

### Release Branch Model

Standard branch structure for version management:

```
main                → Stable baseline (always tagged with latest release)
release/vX.Y        → Version preparation branches (e.g., release/v1.2)
feature/*           → Development branches for new capabilities
hotfix/*            → Emergency patch corrections
```

**Release Workflow:**

1. **Feature Development:** Create feature branch from main
2. **Feature Completion:** Merge feature to main via pull request
3. **Release Preparation:** Create release/vX.Y branch when preparing new version
4. **Release Candidate Testing:** Test release branch; apply fixes directly to release branch
5. **Release Finalization:** Merge release branch to main, create tag, update changelog
6. **Release Publication:** Push tag to origin, update documentation site

**Branch Protection:** Main branch protected per Git Governance Policy (no direct commits, PR approval required).

### Changelog Requirement

Changelog location: `/00_FOUNDATION/CHANGELOG.md`

**Changelog Entry Format:**

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Summary

Brief description of release purpose

### Change Classification

- Type: MAJOR / MINOR / PATCH
- Breaking Changes: Yes / No

### Affected Layers

- List of EATGF layers modified

### Changes

#### Added

- New features or documents added

#### Changed

- Modifications to existing documents

#### Fixed

- Corrections and bug fixes

#### Removed

- Deprecated or removed content

### Impact Statement

Description of how this version affects implementers

### Compatibility Status

- Backward Compatible: Yes / No
- Migration Required: Yes / No
- Migration Guide: [Link if applicable]

### Control Impact

- List of control IDs affected by this release

### References

- Related decision records
- GitHub PR numbers
```

**Example Changelog Entry:**

```markdown
## [1.2.0] - 2026-02-14

### Summary

Formalization of Git Governance and Version Governance policies with comprehensive EATGF formatting standards enforcement.

### Change Classification

- Type: MINOR
- Breaking Changes: No

### Affected Layers

- 04_POLICY_LAYER (Git and Version governance policies added)
- 00_FOUNDATION (FORMATTING_STANDARDS_OFFICIAL.md added)

### Changes

#### Added

- EATGF_GIT_GOVERNANCE_POLICY.md (comprehensive Git workflow governance)
- EATGF_VERSION_GOVERNANCE_POLICY.md (semantic versioning standards)
- FORMATTING_STANDARDS_OFFICIAL.md (8-section mandatory template)

#### Changed

- All layer README files reformatted to 8-section template
- Policy documents updated with enhanced metadata tables

### Impact Statement

Organizations implementing EATGF should update documentation standards to align with 8-section template. No control changes; existing implementations remain valid.

### Compatibility Status

- Backward Compatible: Yes
- Migration Required: No

### Control Impact

- EATGF-BAI-CHG-01: Git Governance Policy implements change management requirements
- EATGF-BAI-CONF-01: Version Governance Policy implements configuration baseline requirements

### References

- Decision Record: PHASE_2_vs_PHASE_3_DECISION_FRAMEWORK.md
- GitHub PR: #42, #43, #44
```

### Versioning Decision Matrix

Decision tree for version classification:

| Change Type                   | Control Changes | Layer Changes | Documentation Only | Version Classification |
| ----------------------------- | --------------- | ------------- | ------------------ | ---------------------- |
| Control ID modified           | Yes             | Any           | Any                | MAJOR                  |
| Control added                 | Yes (new ID)    | No            | Any                | MINOR                  |
| Layer added/removed           | No              | Yes           | Any                | MAJOR                  |
| Policy added                  | No              | No            | Yes (new policy)   | MINOR                  |
| Enhanced documentation        | No              | No            | Yes (existing doc) | PATCH                  |
| Typo fixes                    | No              | No            | Yes                | PATCH                  |
| Evidence requirements changed | Yes             | No            | Any                | MAJOR                  |
| Mapping expanded              | No              | No            | Yes                | MINOR                  |

**When in doubt:** Classify as MINOR. MAJOR reserved for breaking changes only.

### Release Approval Authority

Version release approval levels:

| Version Type | Approval Authority           | Documentation Required                                                               |
| ------------ | ---------------------------- | ------------------------------------------------------------------------------------ |
| PATCH        | Technical Lead               | Changelog entry, PR approval                                                         |
| MINOR        | Governance Council           | Changelog entry, impact assessment, PR approval                                      |
| MAJOR        | Board or Executive Committee | Changelog entry, impact assessment, migration guide, board presentation, PR approval |

Release authority documented in CODEOWNERS file per Git Governance Policy.

### Cross-Repository Version Synchronization

EATGF spans multiple repositories:

- `eatgf-framework` (framework documents - authority repository)
- `governance-docs-site` (Docusaurus portal)

**Synchronization Requirement:**

- Portal version must match framework version
- Submodule reference in governance-docs-site updated with each framework release
- Portal deployment triggered only after framework tag published

**Synchronization Procedure:**

```bash
# In eatgf-framework repository
git tag -a EATGF-v1.2.0 -m "MINOR: Git and Version governance formalization"
git push origin EATGF-v1.2.0

# In governance-docs-site repository
cd framework
git pull origin main
git checkout EATGF-v1.2.0
cd ..
git add framework
git commit -m "Update framework submodule to EATGF-v1.2.0"
git tag -a portal-v1.2.0 -m "Portal release aligned with EATGF-v1.2.0"
git push origin portal-v1.2.0
```

## Control Mapping

| Governance Aspect       | ISO 27001:2022                      | NIST SSDF                          | OWASP                  | COBIT                         |
| ----------------------- | ----------------------------------- | ---------------------------------- | ---------------------- | ----------------------------- |
| Change Control          | A.8.32 (Change management)          | PW.3 (Change tracking)             | SAMM Governance        | BAI06 (Manage changes)        |
| Configuration Integrity | A.8.9 (Configuration management)    | PW.4 (Configuration baseline)      | SAMM Implementation    | DSS01 (Operations management) |
| Audit Traceability      | A.5.35 (Independent review)         | RV.1 (Verification and validation) | ASVS V1 (Architecture) | MEA03 (Compliance assurance)  |
| Governance Oversight    | A.5.1 (Information security policy) | PO.1 (Define governance strategy)  | SAMM Governance        | EDM02 (Benefits delivery)     |

Version governance supports:

- EATGF-BAI-CHG-01 (Change Management) – Version release workflow enforces change approval
- EATGF-BAI-CONF-01 (Configuration Management) – Git tags establish immutable configuration baselines
- EATGF-MEA-AUD-01 (Internal Audit) – Version history provides audit trail for framework evolution

## Developer Checklist

Before creating any version release:

- [ ] All changes classified as MAJOR, MINOR, or PATCH per versioning decision matrix
- [ ] Changelog entry written following changelog entry format template
- [ ] Impact statement completed (how version affects implementers)
- [ ] Compatibility status determined (backward compatible yes/no)
- [ ] Control impact identified (list of affected control IDs)
- [ ] Git tag created with EATGF-vX.Y.Z naming convention
- [ ] Tag message includes change type and brief summary
- [ ] Signed tag created (if Enterprise edition requirement)
- [ ] Branch protection verified active on main branch
- [ ] Pull request approved by designated authority per approval authority table
- [ ] No direct commits to main (all changes via PR)
- [ ] CHANGELOG.md updated in /00_FOUNDATION/
- [ ] For MAJOR versions: Migration guide prepared if backward incompatible
- [ ] For portal release: Submodule reference updated in governance-docs-site
- [ ] For portal release: Portal tag created matching framework version

Critical requirement: No release is valid without complete checklist compliance.

## Governance Implications

### Framework Baseline Integrity

If version governance not enforced:

- Framework drift occurs without controlled baseline
- Control mappings lose integrity (audit references invalid)
- External auditors cannot verify baseline version during certification
- Implementers deploy inconsistent framework versions
- Governance documentation site publishes unreliable content
- Institutional credibility compromised

Enforcement requirement: Version discipline protects framework authority and organizational trust.

### Change Traceability and Audit Defense

- Git tags provide immutable version baselines for audit reference
- Changelog entries document rationale for framework evolution
- Version history demonstrates continuous improvement aligned with maturity progression
- Audit findings reference specific version baselines (e.g., "Assessed against EATGF-v1.2.0")

Audit preparation: Organizations specify EATGF version in Statement of Applicability for audit scope definition.

### Release Authority and Accountability

- MAJOR version releases require Board or Executive approval demonstrating governance oversight
- MINOR version releases require Governance Council approval ensuring controlled enhancement
- PATCH version releases delegated to technical authority for efficiency
- CODEOWNERS enforce approval workflow per Git Governance Policy

Release authority documentation: Governance Council minutes record version approval decisions.

### Cross-Repository Consistency

- Submodule synchronization ensures portal always displays current framework version
- Version mismatch between repositories triggers configuration management audit finding
- Portal deployment automation gated on framework tag publication

Deployment discipline: Portal releases only occur after framework tag verified and published.

## Official References

- **Semantic Versioning 2.0.0** – SemVer specification (Preston-Werner, 2013)
- **ISO/IEC 27001:2022 A.8.32** – Change Management (ISO, 2022)
- **ISO/IEC 27001:2022 A.8.9** – Configuration Management (ISO, 2022)
- **NIST SP 800-218** – Secure Software Development Framework, Practices PW.3, PW.4 (NIST, 2022)
- **COBIT 2019** – BAI06 Managed Changes, MEA03 Compliance with External Requirements (ISACA, 2019)
- **OWASP SAMM** – Software Assurance Maturity Model, Governance and Implementation (OWASP, 2020)
- **Pro Git Book** – Tagging and Distributed Workflows (Chacon & Straub, 2014)

This document defines the official version governance model for the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It establishes:

- Version control structure for framework evolution
- Release discipline and tagging rules
- Governance freeze policies
- Change classification (Major / Minor / Patch)
- Cross-repository version synchronization

This policy ensures structural stability, traceability, and audit defensibility.

---

## Architectural Position

**EATGF Layer:** 00_FOUNDATION

**Scope:** Governance Meta-Control (Framework-Level Control)

**Authority Relationship:** Governs all documents across Layers 00–08

This policy does not define operational controls.
It governs how the framework itself evolves.

MASTER_CONTROL_MATRIX remains the sole control authority.

---

## Governance Principles

- Baseline Freeze Discipline
- Controlled Evolution
- Transparent Change History
- Semantic Versioning Integrity
- Backward Compatibility Protection
- Audit Traceability

Versioning is treated as a governance control, not a documentation convenience.

---

## Technical Implementation

### 1. Semantic Versioning Model

EATGF follows:

```text
MAJOR.MINOR.PATCH
```

Where:

- **MAJOR** → Structural or architectural change
- **MINOR** → New domain or significant addition
- **PATCH** → Clarification, correction, formatting fix

Example:

```text
EATGF-v1.0-Foundation
EATGF-v1.1-Control-Enhancement
EATGF-v2.0-Developer-Layer
```

### 2. Git Tagging Standard

All releases must be tagged.

```bash
git tag -a EATGF-v1.1 -m "Minor enhancement: Added Developer Implementation Layer"
git push origin EATGF-v1.1
```

Tags are immutable once published.

### 3. Release Branch Model

```text
main           → stable baseline
release/*      → candidate versions
feature/*      → controlled development
hotfix/*       → patch corrections
```

Branch protection must be enforced.

### 4. Changelog Requirement

Each version must include:

- Summary of change
- Change classification
- Affected layers
- Impact statement
- Compatibility status

Changelog must live in:

```text
/00_FOUNDATION/CHANGELOG.md
```

---

## Control Mapping

| Governance Aspect       | ISO 27001:2022                 | NIST SSDF | OWASP               | COBIT |
| ----------------------- | ------------------------------ | --------- | ------------------- | ----- |
| Change Control          | A.8.32 Change Management       | PW.3      | SAMM Governance     | BAI06 |
| Configuration Integrity | A.8.9 Configuration Management | PW.4      | SAMM Implementation | DSS01 |
| Audit Traceability      | A.5.35 Compliance              | RV.1      | ASVS V1             | MEA03 |
| Governance Oversight    | A.5.1 Policies                 | PO.1      | SAMM Governance     | EDM02 |

Version governance acts as a meta-layer alignment control.

---

## Developer Checklist

- [ ] All changes classified as MAJOR / MINOR / PATCH
- [ ] Changelog entry written
- [ ] Git tag created
- [ ] Branch protection active
- [ ] Pull request approved by governance authority
- [ ] No direct commits to main
- [ ] Release notes updated

No release is valid without these steps.

---

## Governance Implications

If version governance is not enforced:

- Framework drift occurs
- Control mappings lose integrity
- External auditors lose baseline reference
- Developers implement inconsistent standards
- Public portal becomes unreliable

Version discipline protects institutional credibility.

---

## Official References

- ISO/IEC 27001:2022 – Annex A.8.32 (Change Management)
- ISO/IEC 27001:2022 – Annex A.8.9 (Configuration Management)
- NIST SP 800-218 (SSDF) – PW.3, PW.4
- COBIT 2019 – BAI06 (Managed Changes), MEA03 (Compliance)
- OWASP SAMM – Governance & Implementation

---

## Version Declaration

**Document Version:** 1.1
**Change Type:** Structural Refactor (Template Alignment)
**Date:** February 2026
**Baseline Compatibility:** Fully compatible with EATGF-v1.0-Foundation
