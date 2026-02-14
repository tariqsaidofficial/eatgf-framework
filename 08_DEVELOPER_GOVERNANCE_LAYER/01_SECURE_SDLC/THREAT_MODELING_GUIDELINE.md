# Threat Modeling Guideline

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 01_SECURE_SDLC  
**Governance Scope:** Implementation Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 01_SECURE_SDLC

**Governance Scope:** Threat modeling methodology, requirements, and documentation standards.

**Control Authority Relationship:** Implements:
- Layer 02: Risk Assessment Controls
- Layer 04: Information Security Policy
- NIST SSDF PO.1 (Design software securely)

## Purpose

This guideline provides a practical approach to threat modeling for software systems. It covers:

- When threat modeling is required
- Threat modeling methodologies (STRIDE, PASTA)
- Threat identification and risk assessment
- Mitigation documentation
- Ongoing threat model maintenance

## Governance Principles

- **Security-by-Design:** Security risks identified before development
- **Control-Centric Architecture:** Threats mapped to security controls
- **Developer-Operational Alignment:** Practical, developer-led process
- **Audit Traceability:** Threat models documented and version-controlled

## When Threat Modeling is Required

**Mandatory Scenarios:**
- New application or microservice development
- Significant architecture changes to existing systems
- Introduction of new external integrations or APIs
- Data classification changes (e.g., handling PII for the first time)
- Security incident remediation affecting architecture

**Recommended Scenarios:**
- Major feature additions
- Technology stack changes
- Cloud migration or infrastructure changes

## Threat Modeling Methodology

### STRIDE Methodology

**Recommended for:** Application-level threat modeling

**STRIDE Categories:**
- **S**poofing: Illegitimate authentication claims
- **T**ampering: Unauthorized data modification
- **R**epudiation: Denying actions without proof
- **I**nformation Disclosure: Unauthorized data access
- **D**enial of Service: Service disruption
- **E**levation of Privilege: Unauthorized privilege gain

**Process:**
1. Diagram the system architecture
2. Identify trust boundaries
3. Enumerate threats using STRIDE per component
4. Assess risk and prioritize
5. Define mitigations
6. Document and track

### PASTA Methodology

**Recommended for:** Enterprise-level, risk-focused threat modeling

**PASTA Stages:**
1. Define business objectives
2. Define technical scope
3. Application decomposition
4. Threat analysis
5. Vulnerability and weakness analysis
6. Attack modeling
7. Risk and impact analysis

**Process is more comprehensive but requires more time investment.**

## Threat Modeling Process

### Step 1: Define Scope and Context

**Developer Requirements:**
- Identify the system or component being modeled
- Define system boundaries and trust zones
- Identify assets (data, functionality, infrastructure)
- Define data classification levels

**Artifacts:**
- System context diagram
- Asset inventory

### Step 2: Create Architecture Diagram

**Developer Requirements:**
- Document data flow between components
- Identify external entities (users, external systems)
- Mark trust boundaries (e.g., internet to DMZ, DMZ to internal network)
- Include authentication and authorization points

**Recommended Tooling:**
- Draw.io, Lucidchart, or PlantUML for diagrams
- Microsoft Threat Modeling Tool
- OWASP Threat Dragon (open-source)

### Step 3: Identify Threats

**Developer Requirements:**
- For each component and data flow, apply STRIDE categories
- Consider OWASP Top 10 and CWE Top 25 vulnerabilities
- Review historical incidents and known attack patterns

**Example Threat Identification:**

| Component | Threat Type | Threat Description | STRIDE Category |
|---|---|---|---|
| User Login API | Spoofing | Attacker brute-forces credentials | Spoofing |
| Database Connection | Information Disclosure | SQL injection exposes PII | Information Disclosure |
| Admin Panel | Elevation of Privilege | Broken access control allows non-admin access | Elevation of Privilege |

### Step 4: Assess Risk

**Developer Requirements:**
- Assign likelihood (Low, Medium, High)
- Assign impact (Low, Medium, High)
- Calculate risk level (Likelihood × Impact)

**Risk Matrix:**

| Likelihood / Impact | Low | Medium | High |
|---|---|---|---|
| **High** | Medium | High | Critical |
| **Medium** | Low | Medium | High |
| **Low** | Low | Low | Medium |

**Prioritization:**
- Critical: Address before release
- High: Address within current sprint
- Medium: Address within current release cycle
- Low: Backlog for future consideration

### Step 5: Define Mitigations

**Developer Requirements:**
- For each identified threat, define mitigation strategy
- Map mitigations to security controls (OWASP ASVS, NIST 800-53)
- Assign responsibility and target completion date

**Mitigation Strategies:**
- **Prevent:** Implement controls to eliminate threat
- **Detect:** Implement monitoring and alerting
- **Respond:** Implement incident response procedures
- **Accept:** Document acceptance of residual risk (requires approval)

**Example Mitigation Table:**

| Threat | Mitigation Strategy | Security Control | Responsible | Status |
|---|---|---|---|---|
| Credential brute-force | Implement rate limiting and account lockout | ASVS V2.2 | Backend Team | Implemented |
| SQL injection | Use parameterized queries | ASVS V5.3 | Backend Team | Implemented |
| Broken access control | Implement RBAC with server-side checks | ASVS V4.1 | Backend Team | In Progress |

### Step 6: Document Threat Model

**Developer Requirements:**
- Create THREAT_MODEL.md file in repository
- Include architecture diagram
- Include threat table and mitigation table
- Version-control the threat model
- Link to related security requirements and architecture decisions

**Threat Model Template Structure:**

```markdown
# Threat Model: [System Name]

## System Overview
[Brief description]

## Architecture Diagram
[Include or link to diagram]

## Assets
[List critical assets and data]

## Trust Boundaries
[Define trust zones]

## Identified Threats
[Threat table from Step 3]

## Risk Assessment
[Risk assessment from Step 4]

## Mitigations
[Mitigation table from Step 5]

## Residual Risks
[Any accepted risks with justification]

## Review History
| Date | Reviewer | Changes |
|---|---|---|
```

### Step 7: Review and Approval

**Developer Requirements:**
- Threat model reviewed by security champion
- For high-risk systems, security team review required
- Approval documented before development proceeds

**Security Team Escalation Criteria:**
- Handling of highly sensitive data (e.g., financial, health records)
- Internet-facing systems
- Critical infrastructure systems
- Third-party integrations with privileged access

### Step 8: Maintain and Update

**Developer Requirements:**
- Review threat model when architecture changes
- Update threat model after security incidents
- Annual review of threat models for production systems

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Threat Identification | A.8.25 | PO.1 | SAMM Design | APO12 |
| Risk Assessment | A.8.2 | PO.1 | - | APO12 |
| Mitigation Planning | A.8.9 | PO.1 | ASVS | APO13 |
| Documentation | A.5.37 | PO.3 | SAMM | BAI03 |

## Developer Checklist

Before starting development:

- [ ] Threat model created for new system or feature
- [ ] Architecture diagram included
- [ ] STRIDE categories applied to all components
- [ ] Risk assessment completed
- [ ] Mitigations defined for high and critical risks
- [ ] Security champion review completed
- [ ] Threat model stored in version control

## Governance Implications

**Risk if not implemented:**
- Security vulnerabilities discovered late in development (higher remediation cost)
- Insufficient security controls for identified threats
- Non-compliance with security-by-design requirements

**Operational impact:**
- Early identification reduces remediation costs (10x cheaper than post-release fixes)
- Improved security awareness across engineering teams
- Clear security requirements for development and testing

**Audit consequences:**
- Threat modeling is standard requirement for ISO 27001, SOC 2, and PCI-DSS
- Demonstrates proactive risk management
- Provides evidence of security-by-design approach

**Cross-team dependencies:**
- Security team provides methodology training and high-risk reviews
- Architecture team provides system diagrams and context
- QA team validates security controls during testing

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Risk Framework (Layer 02)
3. Information Security Policy (Layer 04)
4. Threat Modeling Guideline

## References

- NIST SP 800-218 (SSDF Practice PO.1)
- Microsoft Threat Modeling Tool (https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling)
- OWASP Threat Dragon (https://owasp.org/www-project-threat-dragon/)
- OWASP Threat Modeling Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- PASTA Threat Modeling Methodology
- Adam Shostack, "Threat Modeling: Designing for Security"

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial threat modeling guideline |
