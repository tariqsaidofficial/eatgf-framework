# Secure SDLC Enforcement Matrix

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Domain:** 01_SECURE_SDLC
**Classification:** Operational Enforcement Standard
**Reference:** SECURE_SDLC_GOVERNANCE_STANDARD.md

---

## Purpose

This matrix operationalizes the Secure SDLC standard by defining **specific enforcement requirements** for each organization profile and risk level.

It converts abstract governance principles into actionable deployment gates and audit criteria.

---

## Executive Summary

| Organization Profile     | Secure SDLC Requirement | Threat Modeling | Code Review Gate       | SAST/SCA Gate | Artifact Signing | SBOM Mandatory |
| ------------------------ | ----------------------- | --------------- | ---------------------- | ------------- | ---------------- | -------------- |
| **Enterprise**           | MANDATORY               | Required        | Required (2 approvers) | Blocking      | Required         | Required       |
| **SaaS**                 | MANDATORY               | Required        | Required (1 approver)  | Blocking      | Recommended      | Required       |
| **Startup**              | RECOMMENDED             | Recommended     | Recommended            | Advisory      | Recommended      | Recommended    |
| **Individual Developer** | RECOMMENDED             | Optional        | Recommended            | Advisory      | Optional         | Optional       |

---

## Control Enforcement Details

### Control 1: Security Requirements Integration

| Profile                  | Enforcement | Evidence Required                                                                      | Exception Process              |
| ------------------------ | ----------- | -------------------------------------------------------------------------------------- | ------------------------------ |
| **Enterprise**           | MANDATORY   | Jira/ADO tickets with security requirement tag, acceptance criteria, control reference | Risk acceptance from CTO/CISO  |
| **SaaS**                 | MANDATORY   | ClickUp/Linear tickets with security section                                           | Risk acceptance from tech lead |
| **Startup**              | RECOMMENDED | GitHub issues with security label                                                      | Document with team rationale   |
| **Individual Developer** | RECOMMENDED | README or design document                                                              | Self-assessment                |

---

### Control 2: Design & Threat Modeling

| Profile                  | Enforcement | Methodology       | Approval Required             | Documentation                  | Review Cycle                 |
| ------------------------ | ----------- | ----------------- | ----------------------------- | ------------------------------ | ---------------------------- |
| **Enterprise**           | MANDATORY   | STRIDE or PASTA   | CISO/InfoSec lead             | Diagram + matrix + mitigations | Quarterly + on design change |
| **SaaS**                 | MANDATORY   | STRIDE or PASTA   | Tech lead + security champion | Diagram + risk assessment      | Bi-annual + on design change |
| **Startup**              | RECOMMENDED | STRIDE simplified | Team lead                     | Text or diagram                | On major feature             |
| **Individual Developer** | OPTIONAL    | Self-assessment   | Self                          | README notes                   | Before release               |

---

### Control 3: Secure Coding Practices

| Profile                  | Enforcement | Code Review Focus   | SAST Tools Required       | Blocking Severity |
| ------------------------ | ----------- | ------------------- | ------------------------- | ----------------- |
| **Enterprise**           | MANDATORY   | Manual + automated  | Bandit, SonarQube, CodeQL | CRITICAL          |
| **SaaS**                 | MANDATORY   | Automated checklist | Bandit or SonarQube       | CRITICAL, HIGH    |
| **Startup**              | RECOMMENDED | Peer review         | Bandit (free tier)        | CRITICAL          |
| **Individual Developer** | RECOMMENDED | Self-review         | None required             | Self-assessment   |

---

### Control 4: Code Review Gate

| Profile                  | Reviewers Required    | Security-Sensitive Changes             | Approval Time   | Bypass Exception                          |
| ------------------------ | --------------------- | -------------------------------------- | --------------- | ----------------------------------------- |
| **Enterprise**           | Minimum 2 independent | Require 2 reviewers, 24h review window | Within 48 hours | Documented exception + CISO approval      |
| **SaaS**                 | Minimum 1 independent | Require 2 reviewers, 12h review window | Within 24 hours | Documented exception + tech lead approval |
| **Startup**              | Minimum 1             | Recommended 2 reviewers                | Flexible        | Team decision documented                  |
| **Individual Developer** | Self + peer optional  | Optional 2 reviewers                   | N/A             | N/A                                       |

**Branch Protection Settings (GitHub/GitLab):**

```yaml
# Enterprise/SaaS
Require status checks to pass before merge: true
Require branches to be up to date: true
Require code review approval: 2 (Enterprise) or 1 (SaaS)
Dismiss stale pull request approvals: true
Require signed commits: true
Include administrators: true

# Startup
Require code review approval: 1
Require signed commits: recommended
Include administrators: false
```

---

### Control 5: Automated Security Testing Gate (SAST/SCA)

| Profile                  | CI/CD Frequency | SAST Threshold          | Dependency Threshold | Container Scan | SBOM Generation      | Blocking Behavior |
| ------------------------ | --------------- | ----------------------- | -------------------- | -------------- | -------------------- | ----------------- |
| **Enterprise**           | On every push   | 0 CRITICAL allowed      | 0 CRITICAL allowed   | Required       | Required (SPDX)      | Blocks deployment |
| **SaaS**                 | On every push   | 0-1 CRITICAL allowed    | 0-1 CRITICAL allowed | Required       | Required (CycloneDX) | Blocks deployment |
| **Startup**              | On PR + nightly | Allow CRITICAL w/ issue | Allow HIGH w/ issue  | Recommended    | Recommended          | Advisory report   |
| **Individual Developer** | On PR           | Self-assessed           | Self-assessed        | N/A            | Optional             | Advisory          |

**Scan Tools by Profile:**

| Tool           | Enterprise            | SaaS                          | Startup               | Developer     |
| -------------- | --------------------- | ----------------------------- | --------------------- | ------------- |
| **SAST**       | SonarQube + CodeQL    | Bandit or SonarQube Community | Bandit                | None required |
| **Dependency** | Snyk + Trivy          | Trivy + npm audit             | npm audit / pip-audit | Manual check  |
| **Container**  | Aqua Security + Trivy | Trivy                         | Trivy base            | N/A           |
| **SBOM**       | CycloneDX + SPDX      | CycloneDX                     | Optional              | Optional      |

---

### Control 6: Supply Chain Security

| Profile                  | Dependency Review         | Recursive Dependency Audit | Version Pinning       | Update Frequency                     | Critical Patch SLA |
| ------------------------ | ------------------------- | -------------------------- | --------------------- | ------------------------------------ | ------------------ |
| **Enterprise**           | Required (all deps)       | Required                   | Major versions pinned | Quarterly baseline + ad-hoc critical | 7 days             |
| **SaaS**                 | Required (high-risk only) | Recommended                | Minor versions pinned | Quarterly                            | 14 days            |
| **Startup**              | Recommended               | Optional                   | Flexible              | As needed                            | 30 days            |
| **Individual Developer** | Self-assessed             | Optional                   | Flexible              | Flexible                             | Self-determined    |

---

### Control 7: Secrets Management

| Profile                  | Vault Solution                       | Rotation Frequency     | Access Audit       | CI/CD Integration               | Blocking          |
| ------------------------ | ------------------------------------ | ---------------------- | ------------------ | ------------------------------- | ----------------- |
| **Enterprise**           | Vault / AWS Secrets / Azure KeyVault | 90 days (quarterly)    | Daily audit logs   | CloudFormation / Terraform      | Pre-commit hook   |
| **SaaS**                 | AWS Secrets / 1Password / Vault      | 90 days (quarterly)    | Weekly spot checks | GitHub Secrets + GitHub Actions | Pre-commit hook   |
| **Startup**              | AWS Secrets / 1Password / Vault      | 180 days (semi-annual) | Monthly review     | Environment variables           | Recommended       |
| **Individual Developer** | 1Password / keepass / .env.local     | As needed              | N/A                | Local only                      | Manual discipline |

**Pre-commit Secret Detection (All Profiles):**

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Scan for secrets before commit
if truffleHog filesystem . --json | grep -q '"matched": true'; then
    echo "ERROR: Secrets detected in commit. Aborting."
    exit 1
fi
```

---

### Control 8: Logging & Monitoring

| Profile                  | Centralized Logging | SIEM Integration | Alert Configuration          | Retention | Real-time Response   |
| ------------------------ | ------------------- | ---------------- | ---------------------------- | --------- | -------------------- |
| **Enterprise**           | Required            | Required         | Critical events within 5 min | 90+ days  | 24/7 SOC monitoring  |
| **SaaS**                 | Required            | Recommended      | High-priority events         | 60+ days  | On-demand response   |
| **Startup**              | Recommended         | Optional         | Key events logged            | 30 days   | Alert + daily review |
| **Individual Developer** | Optional            | N/A              | Self-assessed                | As needed | Manual review        |

**Log Retention Standards:**

```yaml
Enterprise:
  Critical: 2 years (regulatory)
  High: 90 days
  Standard: 30 days

SaaS:
  Critical: 1 year
  High: 90 days
  Standard: 30 days

Startup:
  All: 30 days

Individual:
  All: As storage permits
```

---

### Control 9: Artifact Integrity & Provenance

| Profile                  | Code Signing             | Git Tag Requirements              | Release Approval           | SBOM Format      | Artifact Storage                |
| ------------------------ | ------------------------ | --------------------------------- | -------------------------- | ---------------- | ------------------------------- |
| **Enterprise**           | GPG signed (mandatory)   | Semantic versioning + commit hash | CISO/Architecture approval | SPDX + CycloneDX | Secure repository (Artifactory) |
| **SaaS**                 | GPG signed (recommended) | Semantic versioning + commit hash | Tech lead approval         | CycloneDX        | Artifact repository             |
| **Startup**              | Recommended              | Semantic versioning               | Team approval              | Optional         | GitHub Releases                 |
| **Individual Developer** | Optional                 | Semantic versioning               | Self                       | N/A              | GitHub Releases or similar      |

---

## Deployment Gate Sequencing

### Enterprise Deployment Gate

```
1. Code commit → Branch protection enforced
2. SAST scan → Must pass (0 CRITICAL allowed)
3. Dependency scan → Must pass (0 CRITICAL allowed)
4. Container scan → Must pass (if containerized)
5. Code review → Require 2 approvers
6. Signed commits → Verify GPG signature
7. Threat model → Verify exists and current
8. SBOM generation → Must be present
9. Signed artifact → Package must be signed
10. Security approval → CISO/Security sign-off
11. Deploy to staging → Full integration tests
12. Deploy to production → Audit logging enabled
```

### SaaS Deployment Gate

```
1. Code commit → Branch protection enforced
2. SAST scan → Blocking on CRITICAL/HIGH
3. Dependency scan → Blocking on CRITICAL
4. Code review → 1 approver required
5. Signed commits → Recommended
6. Threat model → For new public APIs
7. SBOM generation → CycloneDX format
8. Artifact signing → Recommended
9. Deploy to staging → Smoke tests
10. Deploy to production → Rolling deployment
```

### Startup Deployment Gate

```
1. Code commit → Basic hygiene
2. Peer review → Recommended
3. Basic scans → npm audit, pip-audit
4. Deploy to staging → Functional tests
5. Deploy to production → Documented
```

---

## Risk-Level Enforcement Overrides

For exceptionally high-risk changes, organizations may bypass standard gates:

### Level RED (Critical Incident Response)

- Security patch for active exploitation
- Requirements: CTO + CISO approval, documented risk acceptance
- Bypass: All gates except critical security scan
- Post-deployment: Full audit and verification within 24 hours

### Level ORANGE (High Priority)

- Security vulnerability with available patch
- Requirements: Tech lead + Security approval
- Bypass: Code review (but manual security check required)
- Post-deployment: Verification within 48 hours

### Level YELLOW (Standard)

- Standard changes following normal process
- No exceptions

---

## Maturity Assessment Mapping

| Control                   | Level 1: Ad Hoc | Level 2: Defined | Level 3: Managed | Level 4: Integrated  | Level 5: Optimized          |
| ------------------------- | --------------- | ---------------- | ---------------- | -------------------- | --------------------------- |
| **Security Requirements** | Optional        | Recommended      | MANDATORY        | MANDATORY            | MANDATORY                   |
| **Threat Modeling**       | Rare            | Sometimes        | Required         | Required             | Required + continuous       |
| **Code Review**           | Informal        | Documented       | 1-2 reviewers    | Automated checklist  | AI-assisted + peer          |
| **SAST/SCA**              | Manual          | Ad-hoc scans     | Blocking gates   | Dashboard + trending | Predictive feedback         |
| **Secrets**               | Hard-coded      | Environment vars | Vault + rotation | Auto-rotation        | Zero-knowledge architecture |
| **Logging**               | Sporadic        | File-based       | Centralized      | SIEM + alerts        | ML-based anomaly detection  |

---

## Audit & Evidence Collection

For compliance audits (ISO 27001, SOC 2, PCI-DSS), organizations must provide:

### Evidence by Control

| Control             | Enterprise Evidence       | SaaS Evidence            | Startup Evidence           |
| ------------------- | ------------------------- | ------------------------ | -------------------------- |
| **Req. Planning**   | Jira export (6 months)    | Linear export (6 months) | GitHub issues + README     |
| **Threat Modeling** | Diagram + approval record | Design doc + sign-off    | Architecture notes         |
| **Code Review**     | GitHub PR history         | GitLab MR history        | Git log + README           |
| **SAST/SCA**        | SonarQube report + logs   | Bandit JSON + logs       | Manual checklist           |
| **Secrets**         | Vault audit logs          | AWS Secrets logs         | .env files (not committed) |
| **Logging**         | SIEM dashboard + reports  | CloudWatch logs          | Application logs (30 days) |
| **Artifacts**       | GPG signatures + SBOM     | Release artifacts + SBOM | GitHub releases            |

---

## Exceptions & Waivers

Organizations may request exceptions using this process:

### Exception Request Template

```
Title: Exception Request – [Control Name]
Requester: [Team Lead Name]
Date: [YYYY-MM-DD]
Expiration: [YYYY-MM-DD]

Control: [SECURE_SDLC_GOVERNANCE_STANDARD, Section X]

Business Justification:
[Explain why control cannot be followed]

Risk Analysis:
- Likelihood: [High/Medium/Low]
- Impact: [High/Medium/Low]
- Mitigation: [Proposed compensating controls]

Approval:
- [Tech Lead] – Date: ___
- [Security Lead] – Date: ___
- [Risk Owner] – Date: ___

Review Date: [Quarterly]
```

---

## Version History

| Version | Date       | Change Type | Description                                                                                      |
| ------- | ---------- | ----------- | ------------------------------------------------------------------------------------------------ |
| 1.0     | 2026-02-14 | Major       | Initial enforcement matrix: organization profiles, risk levels, deployment gates, audit criteria |
