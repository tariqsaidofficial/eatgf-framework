# Threat Modeling Governance Standard

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Change Type:** Major  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Domain:** 01_SECURE_SDLC  
**Classification:** Annex Standard  
**Authority:** Subordinate to SECURE_SDLC_GOVERNANCE_STANDARD.md  
**Control Reference:** SDLC-TM-01

---

## Purpose

This Annex defines the mandatory threat modeling requirements within the EATGF Developer Governance Layer.

It establishes a structured, repeatable, and auditable threat modeling process aligned with modern secure software development practices.

**Critical:** Threat modeling under this standard is not optional documentation work. It is a governance control that directly affects deployment approval, risk acceptance, and certification posture.

---

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 01_SECURE_SDLC

**Classification:** Subordinate Annex to SECURE_SDLC_GOVERNANCE_STANDARD.md

**Authority Relationship:**

- Operationalizes Secure SDLC Phase 2: Design & Architecture
- Enforces pre-implementation gate control
- Status: MANDATORY for Enterprise & SaaS
- Applicability: Enterprise / SaaS / Startup / Developer

**Integration Points:**

- ENFORCEMENT_MATRIX.md (Threat modeling enforcement by org profile)
- CONTROL_MAPPING_APPENDIX.md (Framework alignment)
- SECURE_SDLC_GOVERNANCE_STANDARD.md (6-phase model, Phase 2)

---

## Governance Principles

1. **Threat modeling must occur before implementation**
   - Findings must be documented before coding starts
   - Architectural changes require threat model updates

2. **Threat modeling must be documented and version controlled**
   - Artifacts stored in repository alongside code
   - Version history maintained (threat-model.yaml)
   - Changes tracked in git log

3. **Threat modeling must be revisited on architectural changes**
   - Major feature additions trigger threat model review
   - New integrations require threat model updates
   - Security findings drive architectural reconsideration

4. **Threat modeling output must map to actionable mitigation tasks**
   - Every identified threat has corresponding task/story
   - Mitigations tracked to completion
   - Residual risks formally approved

5. **Risk acceptance must be formally approved**
   - High/Critical risks require written approval
   - Approver must be executive (CTO, CISO, Risk Owner)
   - Approval expires annually; must be re-certified

6. **Deployment cannot proceed if MANDATORY threats remain unmitigated**
   - Blocking gate in CICD unless waiver granted
   - Waivers documented with risk assessment and approval
   - Waivers reviewed quarterly for expiration

---

## Severity Model

| Risk Level   | Definition                                        | Approval Required             | Deployment Impact | SLA                                  |
| ------------ | ------------------------------------------------- | ----------------------------- | ----------------- | ------------------------------------ |
| **Critical** | Could enable major breach or data loss            | CISO + CTO + Legal            | Blocks deployment | Must mitigate before production      |
| **High**     | Could compromise system integrity                 | Tech lead + Security champion | Advisory gate     | Mitigate within 30 days post-release |
| **Medium**   | Potential vulnerability under specific conditions | Tech lead                     | Warning logged    | Mitigate within 90 days              |
| **Low**      | Minimal risk; defense-in-depth enhancement        | Backlog item                  | No gate           | Backlog; implement opportunistically |

---

## Threat Modeling Methodology

### Approved Approaches

Organizations must use one of these established methodologies:

#### 1. STRIDE (Microsoft)

**Categories:** Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege

**Best for:** Web applications, APIs, traditional architectures

**Tool:** Microsoft Threat Modeling Tool, OWASP Threat Dragon

#### 2. PASTA (Process for Attack Simulation and Threat Analysis)

**Stages:**

1. Define business objectives
2. Define technical scope
3. Decompose application
4. Threat analysis
5. Vulnerability analysis
6. Countermeasures
7. Risk ranking

**Best for:** Risk-driven threat modeling; enterprise applications

**Tool:** PASTA workflows (custom or OWASP Threat Dragon)

#### 3. Attack Tree Methodology

**Approach:** Visual decomposition of attacks as tree structure

**Best for:** Complex systems, distributed architectures

**Tool:** Attack tree visualization tools

#### 4. OWASP Threat Dragon Structured Flow

**Format:** JSON/YAML diagrams + threat enumeration

**Best for:** Automated validation, CI/CD integration

**Tool:** OWASP Threat Dragon, custom YAML parsing

---

## Required Threat Model Artifacts

Every system undergoing threat modeling MUST produce:

### 1. Data Flow Diagram (DFD)

**Definition:** Visual representation of how data moves through the system

**Requirements:**

- External entities (users, external systems) clearly labeled
- Processes/services identified with numbered bubbles
- Data stores (databases, caches) identified
- Data flows labeled with data types and sensitivity
- Trust boundaries clearly marked with boxes/barriers

**Example:**

```
┌──────────────────────────────────────────────────────────┐
│ TRUST BOUNDARY: INTERNET                                 │
│                                                          │
│ ┌─────────────┐                                          │
│ │   User App  │                                          │
│ └──────┬──────┘                                          │
│        │ HTTPS (encrypted)                              │
│        ▼                                                 │
│  ┌──────────────────────────┐                           │
│  │  (1) API Gateway         │                           │
│  │  - Authentication        │                           │
│  │  - Rate limiting         │                           │
│  └──────┬───────────────────┘                           │
│         │                                                │
└─────────┼────────────────────────────────────────────────┘
          │
┌─────────┼──────────────────────────────────────────────┐
│ TRUST BOUNDARY: INTERNAL NETWORK                       │
│         │                                              │
│         ▼                                              │
│  ┌─────────────────┐                                  │
│  │ (2) Auth Service│                                  │
│  └────────┬────────┘                                  │
│           │ JWT tokens                                │
│           ▼                                           │
│  ┌──────────────────┐        ┌────────────────────┐  │
│  │ (3) API Service  │◄──────►│ (D) PostgreSQL DB  │  │
│  │ - Validate JWT   │        │ - User data        │  │
│  │ - Process logic  │        │ - Audit logs       │  │
│  └──────────────────┘        └────────────────────┘  │
│                                                       │
└───────────────────────────────────────────────────────┘
```

### 2. Trust Boundary Identification

**Definition:** Boundaries separating system components with different privilege levels

**Examples:**

- Internet ↔ DMZ
- DMZ ↔ Internal network
- Application ↔ Database
- User code ↔ Kernel

**Format:** Document/diagram showing:

- Which boundaries exist
- What data crosses each boundary
- How data is protected (encryption, authentication)
- Who/what can cross boundaries

### 3. Asset Classification

**Definition:** Inventory of valuable assets targeted by threats

**Categories:**

| Asset Type            | Example                    | Confidentiality | Integrity | Availability |
| --------------------- | -------------------------- | --------------- | --------- | ------------ |
| **Data Assets**       | Customer PII, payment data | H               | H         | M            |
| **Credential Assets** | API keys, DB passwords     | H               | H         | L            |
| **Infrastructure**    | Servers, databases         | M               | H         | H            |
| **Application Code**  | Source code, algorithms    | H               | M         | L            |

**Sensitivity Levels:**

- **High (H):** Regulatory (PCI-DSS, GDPR, HIPAA) or business-critical
- **Medium (M):** Internal use; not public but not critical
- **Low (L):** Publicly available or non-sensitive

### 4. Threat Enumeration Table

**Format:** Structured table with threat taxonomy

```yaml
threats:
  - id: TM-001
    category: Spoofing
    description: "Attacker impersonates legitimate user via stolen JWT token"
    affected_asset: "User Identity"
    entry_point: "API endpoint /api/users/profile"
    likelihood: "Medium"
    impact: "High"
    risk: "High"
    attack_scenario: |
      1. Attacker intercepts JWT from unencrypted connection
      2. Attacker adds token to Authorization header
      3. Attacker accesses user profile as impersonated user
    existing_controls: "HTTPS required"
    gap: "HTTPS not enforced in all environments"
    mitigation: "Enforce TLS 1.3+ globally; add HSTS headers"
    mitigation_owner: "Platform team"
    mitigation_deadline: "2026-03-31"
    status: "Open"

  - id: TM-002
    category: "Information Disclosure"
    description: "Sensitive data (passwords, tokens) logged in plaintext"
    affected_asset: "Credentials"
    likelihood: "High"
    impact: "Critical"
    risk: "Critical"
    mitigation: "Implement structured logging with PII masking"
    status: "In Progress"
    mitigation_owner: "AppSec team"
```

### 5. Risk Rating Matrix

**Definition:** Quantitative risk assessment

**Formula:** RISK = LIKELIHOOD × IMPACT

| Likelihood              | Impact | Risk Score | Action                          |
| ----------------------- | ------ | ---------- | ------------------------------- |
| High (3) × High (3)     | 9      | Critical   | Must mitigate before release    |
| High (3) × Medium (2)   | 6      | High       | Must mitigate or formally waive |
| High (3) × Low (1)      | 3      | Medium     | Mitigate when feasible          |
| Medium (2) × High (3)   | 6      | High       | Must mitigate or formally waive |
| Medium (2) × Medium (2) | 4      | Medium     | Mitigate when feasible          |
| Medium (2) × Low (1)    | 2      | Low        | Document and monitor            |
| Low (1) × High (3)      | 3      | Medium     | Mitigate when feasible          |
| Low (1) × Medium (2)    | 2      | Low        | Document and monitor            |
| Low (1) × Low (1)       | 1      | Low        | Document and monitor            |

### 6. Mitigation Mapping

**Definition:** Link each threat to specific actions

**Format:**

| Threat ID | Threat            | Control          | Implementation                     | Owner    | Deadline   | Status      |
| --------- | ----------------- | ---------------- | ---------------------------------- | -------- | ---------- | ----------- |
| TM-001    | JWT spoofing      | Enforce TLS 1.3  | HSTS headers + certificate pinning | Platform | 2026-03-31 | In Progress |
| TM-002    | Plaintext logging | PII masking      | Structured logging filter          | Backend  | 2026-03-15 | Complete    |
| TM-003    | SQL injection     | Input validation | Parameterized queries in ORM       | Backend  | 2026-04-30 | Not Started |

### 7. Residual Risk Statement

**Definition:** Summary of risks that remain after mitigations

**Format:**

```markdown
## Residual Risk Assessment – Payment API v2.1

### Critical Risks (Unmitigated)

None. All critical threats have mitigations in place.

### High Risks (Accepted)

1. **Dependency Vulnerability: Log4j-like RCE**
   - Likelihood: Low (weekly scanning)
   - Impact: Critical (RCE possible)
   - Risk: High
   - Acceptance: Operations team has 24-hour patch SLA
   - Approval: CTO signed off 2026-02-14

### Medium Risks (Monitored)

1. **DDOS via Rate Limit Bypass**
   - Mitigation: WAF configured; monitoring active
   - Review date: Quarterly

### Risk Owner

CTO (name, email)

### Approval Date

2026-02-14

### Next Review

2026-05-14 (90 days)
```

---

## Threat Model Version Control

### Repository Structure

```
project-root/
├── threat-model/
│   ├── threat-model.yaml      (Current version)
│   ├── threat-model.md        (Human-readable summary)
│   ├── dfd.png                (Data flow diagram)
│   ├── archive/
│   │   ├── threat-model-v1.0.yaml
│   │   ├── threat-model-v1.1.yaml
│   │   └── ...
│   └── CHANGES.md             (Version history)
├── .github/
│   └── workflows/
│       └── threat-model-validation.yml
└── README.md                  (References threat model)
```

### Minimal YAML Format

```yaml
---
metadata:
  system: payment-api
  version: 2.1.0
  document_date: 2026-02-14
  last_updated: 2026-02-14
  owner: Backend Team Lead
  reviewers:
    - Security Architect
    - CTO
  status: Approved

assets:
  - name: User Credentials
    sensitivity: High
    impact: "Account compromise"
  - name: Payment Tokens
    sensitivity: High
    impact: "Fraudulent transactions"
  - name: API Keys
    sensitivity: High
    impact: "Service compromise"

trust_boundaries:
  - name: Internet to API
    description: "Public API endpoint"
    protection: "TLS 1.3 enforcement"
  - name: API to Database
    description: "Internal network"
    protection: "Encrypted connection + RBAC"

threats:
  - id: TM-001
    stride_category: Spoofing
    description: "JWT token hijacking"
    likelihood: Low
    impact: High
    risk_score: 6
    mitigation: "Token rotation + HSTS"
    status: Mitigated

  - id: TM-002
    stride_category: Information Disclosure
    description: "Plaintext secrets in logs"
    likelihood: High
    impact: Critical
    risk_score: 9
    mitigation: "Structured logging + masking"
    status: In-Progress
    owner: Backend Lead
    deadline: 2026-03-31

residual_risks:
  - risk: "Dependency RCE (Log4j-like)"
    mitigation: "Weekly scanning + 24h patch SLA"
    approved_by: CTO
    approval_date: 2026-02-14
```

---

## CI/CD Threat Model Validation Gate

### GitHub Actions Example

```yaml
name: Threat Model Validation

on:
  pull_request:
    branches: [main, develop]
    paths:
      - "threat-model/**"
      - ".github/workflows/threat-model-validation.yml"
  push:
    branches: [main]

jobs:
  validate-threat-model:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write

    steps:
      - uses: actions/checkout@v4

      # Check file exists
      - name: Check threat model exists
        run: |
          if [ ! -f threat-model/threat-model.yaml ]; then
            echo "ERROR: threat-model/threat-model.yaml missing"
            exit 1
          fi

      # Validate YAML structure
      - name: Validate YAML syntax
        run: |
          pip install pyyaml
          python3 -c "
          import yaml
          with open('threat-model/threat-model.yaml', 'r') as f:
            data = yaml.safe_load(f)
          # Validate required keys
          required = ['metadata', 'assets', 'threats']
          for key in required:
            if key not in data:
              print(f'Missing required section: {key}')
              exit(1)
          print('Threat model structure valid')
          "

      # Check for open Critical risks
      - name: Check for unmitigated Critical threats
        run: |
          python3 -c "
          import yaml
          with open('threat-model/threat-model.yaml', 'r') as f:
            data = yaml.safe_load(f)

          critical_open = [t for t in data.get('threats', []) 
                          if t.get('risk_score', 0) >= 9 
                          and t.get('status') != 'Mitigated']

          if critical_open:
            print('Found unmitigated Critical threats:')
            for t in critical_open:
              print(f\"  - {t['id']}: {t['description']}\")
            exit(1)
          "

      # Check mitigation deadlines
      - name: Verify mitigation deadlines
        run: |
          python3 -c "
          import yaml
          from datetime import datetime

          with open('threat-model/threat-model.yaml', 'r') as f:
            data = yaml.safe_load(f)

          today = datetime.now().date()

          for t in data.get('threats', []):
            if 'deadline' in t and t['status'] != 'Mitigated':
              deadline = datetime.strptime(t['deadline'], '%Y-%m-%d').date()
              if deadline < today:
                print(f\"ALERT: Threat {t['id']} mitigation OVERDUE\")
          "

      # Comment on PR with summary
      - name: Comment PR with validation results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const yaml = require('js-yaml');
            const doc = yaml.load(fs.readFileSync('threat-model/threat-model.yaml', 'utf8'));

            const totalThreats = doc.threats.length;
            const mitigated = doc.threats.filter(t => t.status === 'Mitigated').length;
            const open = totalThreats - mitigated;

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `
                ## Threat Model Update
                - **Total Threats:** ${totalThreats}
                - **Mitigated:** ${mitigated}
                - **Open:** ${open}
                
                All Critical threats mitigated: ✓
              `
            });
```

---

## Threat Model Review Process

### Review Checklist

Before approval, reviewers must verify:

- [ ] Data flow diagram is accurate and complete
- [ ] Trust boundaries clearly identified
- [ ] Assets classified by sensitivity
- [ ] STRIDE categories comprehensively addressed (all 6 present)
- [ ] Threats prioritized by risk (likelihood × impact)
- [ ] Critical/High risks have concrete mitigations
- [ ] Mitigations are feasible and assigned to owners
- [ ] Deadlines are realistic
- [ ] Residual risks formally accepted
- [ ] Threat model version incremented
- [ ] Changes documented in CHANGES.md
- [ ] No implementation has begun without approved threat model

### Review Cadence

| Trigger                        | Action                                              |
| ------------------------------ | --------------------------------------------------- |
| **New system/service**         | Threat model required before design review          |
| **Major architectural change** | Threat model updated within 1 week                  |
| **New integration**            | Threat model addendum within 2 weeks                |
| **Vulnerability discovery**    | Threat model reviewed and updated within 48 hours   |
| **Annual review**              | All threat models reviewed and re-approved annually |

---

## Common Threat Categories by System Type

### Web API Threats

| Category                   | Example Threat                              |
| -------------------------- | ------------------------------------------- |
| **Spoofing**               | JWT token hijacking, API key compromise     |
| **Tampering**              | Request data modification, header injection |
| **Repudiation**            | User denies action; no audit trail          |
| **Info Disclosure**        | Sensitive data in logs, error messages      |
| **Denial of Service**      | Rate limit bypass, resource exhaustion      |
| **Elevation of Privilege** | Authorization bypass, privilege escalation  |

### Microservices Threats

| Category                   | Example Threat                            |
| -------------------------- | ----------------------------------------- |
| **Spoofing**               | Inter-service impersonation without mTLS  |
| **Tampering**              | Message interception in service mesh      |
| **Information Disclosure** | Secrets in environment variables          |
| **Denial of Service**      | Cascading service failures                |
| **Elevation**              | Overly permissive service-to-service RBAC |

### Database Threats

| Category                   | Example Threat                          |
| -------------------------- | --------------------------------------- |
| **Tampering**              | SQL injection attacks                   |
| **Information Disclosure** | Unauthorized access to sensitive tables |
| **Denial of Service**      | Resource-exhaustion queries             |
| **Elevation**              | Over-privileged application account     |

---

## Control Mapping

| Framework                | Mapping                                                                     |
| ------------------------ | --------------------------------------------------------------------------- |
| **ISO 27001:2022**       | A.8.28 (Secure coding), A.8.25 (Security architecture), A.8.16 (Monitoring) |
| **NIST SSDF SP 800-218** | PW.2 (Identify & evaluate security risks), PO.1 (Threat modeling)           |
| **OWASP ASVS v4**        | V1.1 (SDL), V1.9 (Threat modeling)                                          |
| **OWASP SAMM**           | Governance → Strategy & Metrics, Design → Threat Assessment                 |
| **COBIT 2019**           | BAI03 (Solutions identification), BAI05 (Organizational change)             |
| **NIST 800-53 Rev.5**    | SA-8 (Security engineering principles), RA-3 (Risk assessment)              |

---

## Developer Checklist

Before implementation, confirm:

- [ ] Threat model completed and version controlled
- [ ] All STRIDE categories addressed
- [ ] Data flow diagram created and reviewed
- [ ] Trust boundaries clearly identified and documented
- [ ] Assets classified by sensitivity level
- [ ] Threats enumerated and prioritized
- [ ] Risk scores calculated (likelihood × impact)
- [ ] Critical/High risks have concrete mitigations
- [ ] Mitigations assigned to owners with deadlines
- [ ] No High/Critical unmitigated risks without waiver
- [ ] Waivers formally approved and documented
- [ ] Threat model validated in CI/CD pipeline
- [ ] Residual risk statement approved by CTO/CISO
- [ ] Threat model linked in repository README

---

## Governance Implications

### Risk if not implemented:

- **Systemic Vulnerabilities:** Unidentified architectural weaknesses
- **Late Discovery:** Flaws found in production are 10-100x more expensive to fix
- **Regulatory Violation:** ISO 27001 Annex A.8.25 requires security architecture documentation
- **Certification Impact:** SOC 2, PCI-DSS audits fail without threat modeling evidence

### Operational impact:

- **Design Efficiency:** Threat modeling early prevents expensive rework
- **Team Alignment:** Structured threat modeling aligns security and development teams
- **Risk Ownership:** Clear threat documentation enables informed risk decisions
- **Compliance Readiness:** Threat models are primary evidence for certification audits

### Audit consequences:

- **ISO 27001:** A.8.25 requires evidence of security architecture design
- **SOC 2 SA:** Evidence of threat-based design principles
- **FedRAMP:** SA-3 requires security architecture documentation
- **Audit Questions:** "Show us your threat models" – Missing models = failed audits

---

## Official References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- [Microsoft Threat Modeling Tool](https://www.microsoft.com/en-us/securityengineering/threatmodelingtool)
- [OWASP Threat Dragon](https://owasp.org/www-community/Application_Threat_Modeling)
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001)
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

---

## Version History

| Version | Date       | Change Type | Description                                                                                                                                |
| ------- | ---------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1.0     | 2026-02-14 | Major       | Authoritative Threat Modeling Annex; includes STRIDE/PASTA methodologies, artifact requirements, CI/CD validation, governance implications |
