# EATGF Git Governance Policy

## Enterprise AI-Aligned Technical Governance Framework (EATGF)

| Field | Value |
|-------|-------|
| Document Type | Policy |
| Version | 1.0 |
| Classification | Internal |
| Effective Date | 2026-02-14 |
| Authority | Enterprise Architecture & Governance Office |
| MCM Reference | EATGF-GOV-DOC-003 |

---

## 1. Purpose

This document establishes the Git repository governance policy for the Enterprise AI-Aligned Technical Governance Framework (EATGF). It defines the authority repo and portal repo architecture, submodule management rules, version tagging strategy, branch discipline, pull request governance, change approval workflows, freeze policies, and commit message conventions.

## 2. Scope

This policy applies to:

- The EATGF authority repository (`tariqsaidofficial/eatgf-framework`)
- The EATGF portal repository (`governance-docs-site`)
- All contributors, reviewers, and maintainers with write access to either repository
- All branches, tags, releases, and submodule references within these repositories

This policy does not govern third-party repositories or forks that are not under the control of the EATGF governance authority.

## 3. Definitions

| Term | Definition |
|------|-----------|
| Authority Repository | The single source of truth for all EATGF governance content. All content changes originate here. |
| Portal Repository | The presentation layer — a Docusaurus site that renders the authority repository content via Git submodule. |
| Submodule | A Git reference from the portal repository to a specific commit in the authority repository. The `framework/` directory in the portal is a read-only submodule. |
| Baseline Freeze | A governance-mandated state in which no changes may be made to a tagged version. |
| Control-Affecting Change | A modification that adds, removes, or alters a control in the Master Control Matrix. |

## 4. Responsibilities

| Role | Responsibility |
|------|---------------|
| Framework Owner | Approves all Structural and Control-affecting changes; manages version tags |
| Governance Reviewer | Reviews pull requests for policy compliance, structural consistency, and writing identity |
| Portal Maintainer | Updates submodule pointer after authority repo releases; maintains portal build integrity |
| Contributor | Follows branch discipline, commit conventions, and PR requirements defined in this policy |

---

## 5. Repository Architecture

### 5.1 Authority Repository

| Attribute | Value |
|-----------|-------|
| Repository | `tariqsaidofficial/eatgf-framework` |
| Branch Model | `main` (protected) + feature/release/hotfix branches |
| Content | All 8 governance layers (00–07), 44 documents, MCM, policies, controls |
| Role | Single source of truth — content changes originate exclusively here |

### 5.2 Portal Repository

| Attribute | Value |
|-----------|-------|
| Repository | `governance-docs-site` |
| Branch Model | `main` (protected) + staging/hotfix branches |
| Content | Docusaurus configuration, custom CSS, components, blog, portal-specific docs |
| Submodule | `framework/` → read-only reference to `eatgf-framework` |
| Role | Presentation layer — renders framework content; never modifies it |

### 5.3 Submodule Architecture Rules

1. The `framework/` directory in the portal repository is a Git submodule pointing to the authority repository.
2. Content changes shall never be made directly in the `framework/` submodule directory. All changes originate in the authority repository.
3. The submodule pointer shall reference a tagged commit, not a branch HEAD, in production deployments.
4. Portal repository maintainers update the submodule pointer via:

```bash
cd governance-docs-site
git submodule update --remote framework
git add framework
git commit -m "[META] SUBMODULE: Update framework to EATGF-vX.Y"
```

5. After updating the submodule pointer, a portal build verification shall be executed prior to merge:

```bash
cd portal && npm run build
```

---

## 6. Branch Discipline

### 6.1 Authority Repository Branches

| Branch Pattern | Purpose | Protection | Lifecycle |
|---------------|---------|-----------|-----------|
| `main` | Current approved baseline | Protected — requires PR + review | Permanent |
| `release/vX.Y` | Release candidate preparation | Protected — freeze-eligible | Deleted after merge to `main` and tag |
| `hotfix/[description]` | Critical corrections to released versions | Requires 1 reviewer | Deleted after merge |
| `feature/[description]` | New content, new documents, structural changes | Requires PR | Deleted after merge |

### 6.2 Portal Repository Branches

| Branch Pattern | Purpose | Protection | Lifecycle |
|---------------|---------|-----------|-----------|
| `main` | Production-deployed portal | Protected — requires PR + build pass | Permanent |
| `staging` | Pre-production validation | Build must pass | Permanent |
| `hotfix/[description]` | Critical portal fixes | Requires 1 reviewer | Deleted after merge |

### 6.3 Branch Naming Convention

```
[type]/[layer-nn]-[brief-description]
```

**Examples:**

| Branch Name | Description |
|------------|-------------|
| `feature/layer-02-update-risk-framework-taxonomy` | Update control IDs in Risk Framework |
| `feature/layer-04-add-git-governance-policy` | Add new policy document |
| `hotfix/fix-iso-42001-version-references` | Correct ISO version year across documents |
| `release/v1.1` | Prepare v1.1 release candidate |

---

## 7. Pull Request Governance

### 7.1 PR Description Template

Every pull request to the authority repository shall follow this structure:

```markdown
## What
[Brief description of the change]

## Why
[Governance rationale for the change]

## Impact
- [ ] Minor (editorial, formatting)
- [ ] Structural (new document, section reorganization)
- [ ] Control-affecting (MCM modification)

## MCM Controls Affected
[List EATGF-xxx control IDs, or "None"]

## Layers Modified
[List affected layers: 00, 01, 02, etc.]

## Checklist
- [ ] Document follows EATGF Document Signature Template
- [ ] No prohibited phrasing (per Writing Identity Framework)
- [ ] EATGF header signature present
- [ ] Version & Status Block updated
- [ ] No placeholder content (@enterprise.com, [Organization Name])
```

### 7.2 Review Requirements

| Change Classification | Minimum Reviewers | Approval Authority |
|----------------------|-------------------|-------------------|
| Minor | 1 Governance Reviewer | Any reviewer |
| Structural | 2 Governance Reviewers | Framework Owner |
| Control-Affecting | 2 Governance Reviewers + Framework Owner | Executive Steering Committee |

### 7.3 Review Criteria

Reviewers shall validate:

1. Compliance with the EATGF Document Signature Template (10-element checklist)
2. Adherence to the EATGF Writing Identity Framework (tone, terminology, prohibited phrasing)
3. Correct use of EATGF control IDs (no legacy taxonomy)
4. Accurate ISO/standard version references
5. No placeholder content
6. Heading hierarchy discipline (per UX & Visual Standard Guide)
7. Portal build passes without broken links (for structural changes)

---

## 8. Governance Impact Classification

### 8.1 Classification Definitions

| Classification | Version Impact | Description | Examples |
|---------------|---------------|-------------|----------|
| **Minor** | v1.0 → v1.0.1 | Editorial corrections that do not alter the meaning, scope, or authority of any governance statement | Typo fixes, formatting corrections, broken link repairs, clarification of existing text |
| **Structural** | v1.0 → v1.1.0 or v1.x → v2.0.0 | Changes that add, reorganize, or substantially modify document content without altering MCM controls | New documents, section additions, policy expansions, cross-reference updates, framework mapping additions |
| **Control-Affecting** | Requires governance review | Changes that add, remove, modify, or reclassify any control within the Master Control Matrix | MCM control addition, control objective modification, control ID restructuring, taxonomy changes, evidence requirement changes |

### 8.2 Classification Determination

The change author assigns the initial classification. The Governance Reviewer validates or escalates the classification during pull request review. If a change is misclassified, the reviewer shall:

1. Request reclassification with justification
2. Block merge until correct classification is applied
3. Ensure the appropriate review and approval chain is completed

---

## 9. Version Tagging Strategy

### 9.1 Tag Format

```
EATGF-vMAJOR.MINOR.PATCH[-Edition]
```

**Examples:**

| Tag | Meaning |
|-----|---------|
| `EATGF-v1.0.0-Foundation` | Initial baseline — Foundation Edition |
| `EATGF-v1.1.0` | Minor release with structural additions |
| `EATGF-v1.0.1` | Patch release with editorial corrections |
| `EATGF-v2.0.0-Enterprise` | Major release — Enterprise Edition |

### 9.2 Tagging Rules

1. Tags are created on the `main` branch only, after a release branch has been merged.
2. Tags are **immutable** — force-pushing tags is prohibited.
3. Tags are created on the authority repository only. The portal repository references tags via submodule pointer.
4. Every tag shall include an annotated message:

```bash
git tag -a EATGF-v1.1.0 -m "EATGF v1.1.0 — Structural additions: Git Governance Policy, Version Governance Policy, Writing Identity Framework"
```

5. Tags shall be pushed to the remote immediately after creation:

```bash
git push origin EATGF-v1.1.0
```

---

## 10. Commit Message Convention

### 10.1 Format

```
[LAYER-NN] TYPE: Brief description

Extended description (optional — for Structural and Control-affecting changes)

MCM-Refs: EATGF-XXX-YYY-NNN (if applicable)
```

### 10.2 Type Definitions

| Type | Meaning | Example |
|------|---------|---------|
| `CONTROL` | Change to a control definition, objective, or evidence requirement | `[LAYER-00] CONTROL: Add EATGF-GOV-DOC-003 to MCM` |
| `POLICY` | Change to a governance policy document | `[LAYER-04] POLICY: Add Git Governance Policy` |
| `AUDIT` | Change to audit procedures or evidence specifications | `[LAYER-06] AUDIT: Update internal audit checklist` |
| `DOC` | Content change to a non-policy/non-control document | `[LAYER-03] DOC: Update maturity assessment criteria` |
| `FIX` | Correction of an error (typo, broken link, incorrect reference) | `[LAYER-02] FIX: Correct ISO 42001 version to 2023` |
| `META` | Repository metadata, CI/CD, submodule updates | `[META] SUBMODULE: Update framework to EATGF-v1.1.0` |
| `STYLE` | Formatting, heading hierarchy, template alignment | `[LAYER-05] STYLE: Add EATGF header to AI Governance Framework` |

### 10.3 Commit Message Rules

1. Subject line shall not exceed 72 characters.
2. Subject line shall use imperative mood ("Add", "Update", "Remove", "Correct" — not "Added", "Updates").
3. The `[LAYER-NN]` prefix is mandatory for all changes to framework content. Use `[META]` for repository-level changes.
4. Emoji are prohibited in commit messages.
5. Multi-layer changes shall use the primary affected layer in the prefix and list secondary layers in the body.

---

## 11. Freeze Policy

### 11.1 Pre-Release Freeze

| Parameter | Value |
|-----------|-------|
| Duration | 72 hours before version tag creation |
| Trigger | Release branch creation |
| Scope | All content changes to the release branch |
| Exceptions | Critical corrections classified as `FIX` with Framework Owner approval |

During a pre-release freeze:

1. No new features or structural changes may be merged to the release branch.
2. Only `FIX` commits are permitted, with explicit Framework Owner approval per commit.
3. All reviewers are notified of the freeze via the release branch PR description.

### 11.2 Baseline Freeze

| Parameter | Value |
|-----------|-------|
| Duration | Indefinite — immutable once declared |
| Trigger | Baseline Declaration document publication |
| Scope | All content at the tagged commit |
| Exceptions | None — create a new version for corrections |

A baseline freeze establishes the immutable state of the framework at a specific version tag. Per the Baseline Declaration (BASELINE_DECLARATION_v1.0.md):

1. The tagged commit is permanently locked.
2. Corrections to frozen baselines create a new patch version (e.g., v1.0.1), never modify the frozen tag.
3. The Baseline Declaration document itself is part of the frozen state.

### 11.3 Emergency Unfreeze

Emergency unfreeze is permitted only under the following conditions:

1. A critical error is discovered that creates legal, compliance, or security risk.
2. Written approval from the Framework Owner is obtained and documented in the PR.
3. The unfreeze is limited to the specific correction — no scope expansion is permitted.
4. The correction follows the hotfix branch process (Section 6.1).
5. A revised tag is created per semantic versioning rules (patch increment).

---

## 12. Change Approval Workflow

### 12.1 Standard Workflow

```
1. Contributor creates feature branch
2. Contributor makes changes and commits per convention (Section 10)
3. Contributor opens PR with structured description (Section 7.1)
4. Contributor assigns classification (Minor / Structural / Control-Affecting)
5. Governance Reviewer validates classification and content
6. Required reviewers approve (per Section 7.2)
7. Framework Owner merges (for Structural+) or Reviewer merges (for Minor)
8. Release branch created when accumulation warrants a version increment
9. Pre-release freeze (72 hours)
10. Tag created on main after release branch merge
11. Portal submodule pointer updated
12. Portal build verified
```

### 12.2 Control-Affecting Workflow

```
1–4. Same as Standard Workflow
5. Governance Reviewer escalates to Framework Owner
6. Framework Owner prepares impact assessment:
   - Which MCM controls are affected?
   - What downstream documents require update?
   - What is the risk of the change?
7. Executive Steering Committee review (if required by impact score)
8. Minimum 2 Governance Reviewers + Framework Owner approve
9. Merge, tag, and cascade updates to all dependent documents
10. Pre-release freeze includes validation of all dependent updates
11. Tag and submodule update per standard process
```

---

## 13. Governance Enforcement Rules

1. All changes to the authority repository shall follow the branch discipline defined in Section 6. Direct commits to `main` are prohibited.
2. Pull requests that do not include the structured description template (Section 7.1) shall not be reviewed.
3. Misclassified changes shall be blocked until correct classification is applied by the Governance Reviewer.
4. Tags are immutable. Force-pushing tags constitutes a policy violation subject to escalation.
5. Submodule pointer updates in the portal repository shall reference tagged commits only in production deployments.
6. Commit messages that do not follow the convention in Section 10 shall be corrected via interactive rebase before merge.
7. Freeze violations require formal incident documentation.

---

**Document Control**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-14 | Enterprise Architecture & Governance Office | Initial Git governance policy |

**Authority Sign-Off**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Framework Owner | | | |
| Chief Governance Officer | | | |
