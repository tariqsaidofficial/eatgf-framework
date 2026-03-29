# EATGF_GIT_GOVERNANCE_POLICY

| Field          | Value                                                         |
| -------------- | ------------------------------------------------------------- |
| Document Type  | Policy                                                        |
| Version        | 1.2                                                           |
| Classification | Controlled                                                    |
| Effective Date | 2026-02-14                                                    |
| Authority      | Enterprise Architecture and Governance Office                 |
| EATGF Layer    | 04_POLICY_LAYER                                               |
| MCM Reference  | EATGF-BAI-CHG-01, EATGF-BAI-CONF-01, EATGF-DEV-CI-01          |
| Standards      | ISO 27001:2022 A.8.32/A.8.9, NIST SSDF PW.3/PW.4, COBIT BAI06 |

---

## Purpose

This policy defines official Git governance model for EATGF framework repositories ensuring controlled, audit itable, and tamper-resistant framework evolution. Git is treated as governance control surface (not mere collaboration tool) with branch discipline, pull request controls, commit integrity standards, repository protection rules, review authority model, and security hardening expectations. All framework changes must comply with Git governance to preserve control alignment and version integrity.

## Architectural Position

This policy operates within **04_POLICY_LAYER** as the authoritative Git workflow and version control governance standard.

- **Upstream dependency:** Governance Charter (Layer 04) establishes change authority; Version Governance Policy defines semantic versioning rules; Master Control Matrix references change management controls (BAI-CHG-01)
- **Downstream usage:** All EATGF framework repositories (`eatgf-framework`, `governance-docs-site`) implement branch protection and PR workflows per this policy; developer workflows (Layer 08) enforce Git standards; audit evidence collection (Layer 06) references Git commit history
- **Cross-layer reference:** BAI-CHG-01 (Change Management) implemented through Git PR workflow; DEV-CI-01 (CI/CD Governance) enforces Git pipeline integration; MEA-AUD-01 (Internal Audit) audits Git commit compliance

## Governance Principles

1. **No Direct Commits to Main** – All framework changes require pull request review; direct commits to main branch prohibited without exception
2. **Traceable Change History** – Every commit must include descriptive message with layer context, control impact, and version classification
3. **Immutable Version Tags** – Release tags (EATGF-vX.Y format) are immutable once published; tag modification prohibited
4. **Security-First Repository** – Secret scanning, dependency vulnerability alerts, and branch protection enabled across all EATGF repositories
5. **Git as Audit Evidence** – Commit history, PR approvals, and branch protection logs serve as compliance evidence for change management audits

## Technical Implementation

### Branch Model

Standard branch structure:

```
main                → Stable baseline (protected)
release/*           → Version preparation branches
feature/*           → Structured additions and enhancements
hotfix/*            → Emergency corrections
```

Development workflow: No development occurs directly on main branch. All changes originate from feature or hotfix branches merged via pull request.

### Branch Protection Rules

Mandatory GitHub branch protection settings for main branch:

- Require pull request before merging
- Require at least 1 approval from codeowners
- Require status checks to pass before merging
- Prevent force pushes
- Prevent branch deletion
- Require signed commits (recommended for Enterprise edition)
- Require linear history (optional)

Configuration enforcement: Repository administrators verify branch protection quarterly per MEA-PERF-01 monitoring requirements.

### Commit Message Standard

Required commit message format:

```
[LAYER_CODE] Short summary (max 72 characters)

Extended explanation (if required, wrapped at 72 chars)
Control impact: [Control IDs affected]
Version impact: [MAJOR/MINOR/PATCH]
```

Example commit message:

```bash
git commit -m "[02_CONTROL_ARCHITECTURE] Add NIST SSDF mapping to API Governance

Expanded Control Mapping table in API_GOVERNANCE_FRAMEWORK.md
Control impact: EATGF-API-SEC-01, EATGF-DEV-SDLC-01
Version impact: MINOR"
```

Layer codes:

- 00_FOUNDATION
- 01_MANAGEMENT_SYSTEMS
- 02_CONTROL_ARCHITECTURE
- 03_GOVERNANCE_MODELS
- 04_POLICY_LAYER
- 05_DOMAIN_FRAMEWORKS
- 06_AUDIT_AND_ASSURANCE
- 07_REFERENCE_AND_EVOLUTION
- 08_DEVELOPER_GOVERNANCE_LAYER

### Pull Request Requirements

Each pull request must include:

**PR Title Format:**

```
[LAYER_CODE] Brief description of change
```

**PR Description Template:**

```
## Change Description
[Detailed description of what changed and why]

## Affected Layers
- [ ] 00_FOUNDATION
- [ ] 01_MANAGEMENT_SYSTEMS
- [ ] 02_CONTROL_ARCHITECTURE
- [ ] 03_GOVERNANCE_MODELS
- [ ] 04_POLICY_LAYER
- [ ] 05_DOMAIN_FRAMEWORKS
- [ ] 06_AUDIT_AND_ASSURANCE
- [ ] 07_REFERENCE_AND_EVOLUTION
- [ ] 08_DEVELOPER_GOVERNANCE_LAYER

## Control Impact Statement
[List affected control IDs and impact description]

## Version Classification
- [ ] MAJOR (breaking changes, control structure modifications)
- [ ] MINOR (new controls, enhancements)
- [ ] PATCH (clarifications, typo fixes, documentation updates)

## Documentation Confirmation
- [ ] README updated (if applicable)
- [ ] CHANGELOG updated (for MINOR/MAJOR changes)
- [ ] Control Mapping verified (if control changes)
- [ ] No secrets in diff

## Reviewer Checklist
- [ ] Change aligns with affected layer purpose
- [ ] Control alignment preserved
- [ ] Version impact correctly classified
- [ ] Documentation complete
```

PR approval authority: Minimum 1 approval required from CODEOWNERS file designated reviewers. Major version changes require 2 approvals.

### Signed Tags for Releases

Release tagging procedure:

```bash
# Create signed tag
git tag -s EATGF-v1.2.0 -m "Minor enhancement - Git Governance Policy formalization"

# Verify tag signature
git tag -v EATGF-v1.2.0

# Push tag to origin
git push origin EATGF-v1.2.0
```

Tag naming convention: `EATGF-vMAJOR.MINOR.PATCH` (e.g., EATGF-v1.2.0)

Tag immutability: Once pushed to origin, tags must not be deleted or modified. Tag corrections require new patch version.

Tag signing: GPG signature required for all release tags in SaaS and Enterprise editions.

### Repository Security Controls

Mandatory security configurations:

**Secret Scanning:**

- GitHub secret scanning enabled
- Pre-commit hooks to prevent secret commits (recommended)
- Secret scanning alerts monitored weekly

**Dependency Vulnerability Alerts:**

- Dependabot enabled for all repositories
- Security vulnerabilities addressed within SLA: Critical (4 hours deployment + 24 hours verification), High (7 days), Medium (30 days)
- Reference: VULNERABILITY_REMEDIATION_TERMINOLOGY.md (authoritative source)

**Code Scanning (Optional but Recommended):**

- CodeQL or similar static analysis enabled
- Scan results reviewed before merge

**Audit Log Access:**

- Repository audit log reviewed quarterly
- Audit log retention: 12 months minimum

### CODEOWNERS File

CODEOWNERS file structure:

```
# EATGF Framework Codeowners
# Format: path pattern    @owner-username

# Default owners for all files
*                           @governance-team

# Layer-specific ownership
/00_FOUNDATION/             @architecture-lead @governance-lead
/01_MANAGEMENT_SYSTEMS/     @isms-lead @audit-lead
/02_CONTROL_ARCHITECTURE/   @architecture-lead @compliance-lead
/03_GOVERNANCE_MODELS/      @governance-lead
/04_POLICY_LAYER/           @governance-lead @legal-counsel
/05_DOMAIN_FRAMEWORKS/      @domain-architects
/06_AUDIT_AND_ASSURANCE/    @audit-lead
/07_REFERENCE_AND_EVOLUTION/ @governance-lead
/08_DEVELOPER_GOVERNANCE_LAYER/ @engineering-lead

# Specific high-authority documents
/00_FOUNDATION/MASTER_CONTROL_MATRIX.md    @ciso @governance-lead
/04_POLICY_LAYER/GOVERNANCE_CHARTER*.md     @ceo @ciso @governance-lead
```

CODEOWNERS enforcement: GitHub automatically requests review from designated owners when files in their scope are modified.

## Control Mapping

| Governance Aspect     | ISO 27001:2022                 | NIST SSDF                     | OWASP                  | COBIT                  |
| --------------------- | ------------------------------ | ----------------------------- | ---------------------- | ---------------------- |
| Change Management     | A.8.32 (Change control)        | PW.3 (Change tracking)        | SAMM Governance        | BAI06 (Manage changes) |
| Configuration Control | A.8.9 (Asset management)       | PW.4 (Configuration baseline) | ASVS V1 (Architecture) | DSS01 (Operations)     |
| Secure Code Practices | A.8.28 (Secure coding)         | PW.7 (Code review)            | SAMM Implementation    | BAI03 (Solutions)      |
| Compliance Monitoring | A.5.35 (Compliance monitoring) | RV.1 (Verification)           | SAMM Governance        | MEA03 (Assurance)      |
| Governance Oversight  | A.5.1 (Policy framework)       | PO.1 (Governance)             | -                      | EDM02 (Benefits)       |

Git governance directly supports:

- EATGF-BAI-CHG-01 (Change Management) – PR workflow enforces change approval
- EATGF-BAI-CONF-01 (Configuration Management) – Git history provides configuration baseline
- EATGF-DEV-CI-01 (CI/CD Governance) – Branch protection integrates with pipeline gates
- EATGF-MEA-AUD-01 (Internal Audit) – Git commit history serves as audit evidence

## Developer Checklist

Before merging any framework change:

- [ ] Feature or hotfix branch created from main (not committed directly to main)
- [ ] Branch name follows convention (feature/_, hotfix/_)
- [ ] Commit messages follow [LAYER_CODE] format with control impact and version classification
- [ ] Pull request created with complete PR description template
- [ ] Affected layers identified in PR description
- [ ] Control impact statement completed
- [ ] Version impact classified (MAJOR/MINOR/PATCH)
- [ ] Documentation updated (README, CHANGELOG if applicable)
- [ ] No secrets detected in diff (verified via git-secrets or manual review)
- [ ] At least 1 reviewer approval obtained from CODEOWNERS
- [ ] All status checks passed (CI/CD pipeline green)
- [ ] Branch protection rules satisfied
- [ ] For releases: Signed tag prepared with EATGF-vX.Y.Z format
- [ ] For releases: Tag verified with `git tag -v EATGF-vX.Y.Z`

Critical requirement: No merge permitted without complete checklist compliance.

## Governance Implications

### Framework Integrity Risk

If Git governance not enforced:

- Framework drift occurs due to uncontrolled modifications
- Version mapping becomes unreliable (tags modified or deleted)
- Audit traceability lost (no PR approval evidence)
- Unauthorized changes bypass review process
- Control alignment weakens (no control impact assessment)
- Compliance evidence chain broken (commit history incomplete)

Enforcement requirement: Git governance discipline preserves framework authority and audit defensibility.

### Change Authority and Accountability

- Pull request approval serves as change authorization evidence for BAI-CHG-01 compliance
- CODEOWNERS assignments establish clear accountability for framework changes
- Commit author attribution provides audit trail for change responsibility
- PR review comments document change rationale and impact assessment

Governance Council oversight: Quarterly review of Git governance compliance metrics (PR approval rate, branch protection compliance, commit message quality).

### Version Control and Release Management

- Immutable tags ensure version baseline stability for audit reference
- Semantic versioning (per Version Governance Policy) implemented through Git tag naming
- Release branches enable controlled version preparation with pre-release testing
- Tag signatures provide tamper-evidence for release authenticity (Enterprise edition requirement)

Release authority: Only designated release managers (per CODEOWNERS) may create and push version tags.

### Security and Confidentiality

- Secret scanning prevents accidental credential exposure in framework documentation
- Branch protection prevents unauthorized force pushes that could erase audit history
- Repository audit logs track administrative actions (branch protection changes, tag deletions)
- Access control (GitHub repository permissions) aligned with principle of least privilege

Security incident response: Any detected secret in commit history triggers immediate rotation per DSS-INC-01.

## Official References

- **ISO/IEC 27001:2022 A.8.32** – Change Management (ISO, 2022)
- **ISO/IEC 27001:2022 A.8.9** – Configuration Management (ISO, 2022)
- **NIST SP 800-218** – Secure Software Development Framework, Practices PW.3, PW.4 (NIST, 2022)
- **COBIT 2019** – BAI06 Managed Changes (ISACA, 2019)
- **OWASP SAMM** – Software Assurance Maturity Model, Governance and Implementation (OWASP, 2020)
- **GitHub Documentation** – Branch Protection Rules (GitHub, 2024)
- **Pro Git Book** – Distributed Workflows and Tagging (Chacon & Straub, 2014)

This document defines the official Git governance model for the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It establishes:

- Branch discipline
- Pull request controls
- Commit integrity standards
- Repository protection rules
- Review authority model
- Security hardening expectations

This policy ensures that framework evolution is controlled, auditable, and resistant to accidental or unauthorized modification.

**Git is treated as a governance control surface.**

---

## Architectural Position

**EATGF Layer:** 00_FOUNDATION

**Control Scope:** Framework Source Integrity

**Applies To:**

- `eatgf-framework` (Authority Repo)
- `governance-docs-site` (Portal Repo)

Git Governance enforces structural protection across all EATGF layers.

This policy supports MASTER_CONTROL_MATRIX integrity but does not define business controls.

---

## Governance Principles

- No direct commits to `main`
- All changes require Pull Request review
- Branch protection must be enabled
- Commits must be traceable and descriptive
- Version tags are immutable
- Security scanning must be enabled
- Git history is part of audit evidence

**Git workflow is an enforcement mechanism, not a collaboration convenience.**

---

## Technical Implementation

### 1. Branch Model

```
main                → stable baseline
release/*           → version preparation
feature/*           → structured additions
hotfix/*            → emergency correction
```

**No development occurs directly on `main`.**

### 2. Branch Protection Rules

Enable the following on GitHub:

- Require Pull Request before merging
- Require at least 1 approval
- Require status checks to pass
- Prevent force pushes
- Prevent branch deletion
- Require signed commits (recommended)

### 3. Commit Standard

Commit messages must follow:

```
[Layer] Short summary

Extended explanation (if required)
Control impact (if applicable)
Version impact (MAJOR/MINOR/PATCH)
```

**Example:**

```bash
git commit -m "[02_CONTROL_ARCHITECTURE] Add NIST SSDF mapping to API Governance

Expanded Control Mapping table
Version impact: MINOR"
```

### 4. Pull Request Requirements

Each PR must include:

- Change description
- Affected layer(s)
- Control impact statement
- Version classification
- Documentation confirmation

**PR template must be enforced.**

### 5. Signed Tags for Releases

```bash
git tag -s EATGF-v1.1 -m "Minor enhancement - Developer layer integration"
git push origin EATGF-v1.1
```

**Tags must not be modified once published.**

### 6. Repository Security Controls

Enable:

- Secret scanning
- Dependency vulnerability alerts
- Code scanning (optional but recommended)
- Audit log review access

---

## Control Mapping

| Governance Aspect     | ISO 27001:2022 | NIST SSDF | OWASP               | COBIT |
| --------------------- | -------------- | --------- | ------------------- | ----- |
| Change Management     | A.8.32         | PW.3      | SAMM Governance     | BAI06 |
| Configuration Control | A.8.9          | PW.4      | ASVS V1             | DSS01 |
| Secure Code Practices | A.8.28         | PW.7      | SAMM Implementation | BAI03 |
| Compliance Monitoring | A.5.35         | RV.1      | SAMM Governance     | MEA03 |
| Governance Oversight  | A.5.1          | PO.1      | —                   | EDM02 |

Git governance directly supports structured software integrity practices.

---

## Developer Checklist

Before merging any change:

- [ ] Branch created from `main`
- [ ] No direct commit to `main`
- [ ] PR created
- [ ] Reviewer approval obtained
- [ ] Version impact classified
- [ ] Control impact assessed
- [ ] No secrets in diff
- [ ] Changelog updated (if applicable)
- [ ] Tag prepared (if release)

**No merge without checklist completion.**

---

## Governance Implications

If Git governance is not enforced:

- Framework drift occurs
- Version mapping becomes unreliable
- Audit traceability is lost
- Unauthorized changes may bypass review
- Control alignment weakens

**Git discipline preserves framework authority.**

---

## Official References

- ISO/IEC 27001:2022 – A.8.32 Change Management
- ISO/IEC 27001:2022 – A.8.9 Configuration Management
- NIST SP 800-218 (SSDF) – PW.3, PW.4
- COBIT 2019 – BAI06 Managed Changes
- OWASP SAMM – Governance & Implementation

---

**Document Version:** 1.1
**Change Type:** Structured Refactor
**Baseline Compatibility:** EATGF-v1.0-Foundation Compatible
