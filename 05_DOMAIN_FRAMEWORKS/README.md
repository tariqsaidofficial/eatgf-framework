# 05_DOMAIN_FRAMEWORKS

| Field | Value |
|-------|-------|
| Document Type | Layer Navigation & Overview |
| Version | 2.0 |
| Classification | Controlled |
| Effective Date | 2026-02-14 |
| Authority | Chief AI Officer and Chief Security Officer |
| EATGF Layer | 05_DOMAIN_FRAMEWORKS |

---

## Purpose

This layer extends EATGF into specialized technology domains requiring additional governance beyond the core framework. Domain frameworks add domain-specific controls and procedures for emerging technology areas.

## Architectural Position

This layer operates within **05_DOMAIN_FRAMEWORKS** as the extension point for specialized governance.

- **Upstream dependency:** Layers 00-04 provide foundation; domain frameworks extend and specialize
- **Downstream usage:** Domain-specific controls implement through domain governance bodies
- **Cross-layer reference:** Domain controls map back to MCM; audited by Layer 06

## Governance Principles

1. **Domain Extension Strategy** – Domain frameworks extend core EATGF without replacing foundation
2. **Standards Alignment** – Domain controls align to recognized standards (ISO 42001, OWASP)
3. **Specialized Procedures** – Domain-specific implementation procedures address unique technical requirements
4. **Risk Management** – Domain-specific risk assessment aligned with core enterprise governance
5. **Audit Coverage** – Domain governance subject to same audit rigor as core framework

## Technical Implementation

### AI Governance Framework

Document: AI_GOVERNANCE_FRAMEWORK.md

AI-specific governance extension:
- AI system lifecycle governance (development through retirement)
- AI model governance and version control
- Bias detection and mitigation procedures
- Model performance monitoring and alerting
- Explainability and interpretability requirements
- AI-specific risk assessment methodology
- Extends AIMS (ISO 42001:2023) with operational procedures
- Maps to MCM AI domain controls: EATGF-AI-LC-01, EATGF-AI-RISK-01, EATGF-APO-AI-01

### API Governance Framework

Document: API_GOVERNANCE_FRAMEWORK.md

API-specific governance extension:
- API security and governance procedures
- API authentication, authorization, and access control
- Rate limiting, throttling, and quota management
- API versioning and backwards compatibility
- API change management and lifecycle
- Security testing and penetration testing for APIs
- API inventory management and cataloging
- Aligns with OWASP API Security Top 10
- Maps to MCM API domain controls

### Domain Governance Integration

Layer Relationships:
- **Layer 00 (Foundation):** Domain MCM controls included in Master Control Matrix
- **Layer 01 (Management Systems):** AIMS includes AI governance; ISMS includes API security
- **Layer 02 (Control Architecture):** Framework mappings include domain-specific control alignment
- **Layer 06 (Audit & Assurance):** Internal audit covers domain-specific control compliance

### Organizational Governance Bodies

AI Governance Oversight:
- Chief AI Officer – Strategic AI governance authority
- AI Governance Board – Review and approval of AI initiatives
- ML Engineering Leadership – Technical and operational implementation
- AI Ethics Committee – Fairness, transparency, and responsible AI oversight

API Governance Oversight:
- Chief Technology Officer – API architecture and standards
- API Review Board – Security and lifecycle governance
- Security Team – API security assessment and enforcement
- Development Teams – API implementation and compliance

## Control Mapping

### ISO 42001:2023 Alignment (AI Governance)
- **Clause 5.2** – AI management policies
- **Clause 6.1** – AI risk management planning
- **Clause 8.1** – AI system operational planning and control
- **Clause 8.2** – AI system lifecycle management
- **Clause 9.2** – AI system performance evaluation

### OWASP API Security Top 10 Alignment (API Governance)
- **API1:2023** – Broken Object Level Authorization
- **API2:2023** – Broken Authentication
- **API3:2023** – Broken Object Property Level Authorization
- **API4:2023** – Unrestricted Resource Consumption
- **API5:2023** – Broken Function Level Authorization

### NIST AI Risk Management Framework
- **GOVERN** – AI governance and risk framework
- **MAP** – AI system mapping and documentation
- **MEASURE** – AI system performance and fairness measurement
- **MANAGE** – AI system risk mitigation and monitoring

## Developer Checklist

Before implementing domain-specific governance:

- [ ] Appropriate domain framework identified (AI or API)
- [ ] Domain-specific controls reviewed and understood
- [ ] Domain governance body established and chartered
- [ ] Domain-specific procedures documented
- [ ] Risk assessment methodology for domain applied
- [ ] Control implementation timeline established
- [ ] Evidence collection and tracking procedures defined
- [ ] Audit procedures for domain controls documented

## Governance Implications

### Domain Governance Authority

AI Governance Authority: Chief AI Officer  
API Governance Authority: Chief Technology Officer  
Security Oversight: Chief Information Security Officer

Domain governance operates under core EATGF framework with domain-specific extensions and specialized procedures.

### Cross-Domain Coordination

Domain frameworks must coordinate:
- AI systems using APIs must conform to both frameworks
- Security controls apply to all domains
- Incident response procedures consistent across domains
- Risk reporting aggregated to enterprise governance

### Future Domain Extensions

Additional domains may be added in future framework versions:
- Cloud infrastructure governance
- DevSecOps and CI/CD pipeline governance
- Data platform and analytics governance
- Blockchain and distributed ledger governance

## Official References

- **ISO/IEC 42001:2023** – Artificial Intelligence Management Systems (2023)
- **OWASP API Security Top 10** – API Security Risks (OWASP Foundation, 2023)
- **NIST AI Risk Management Framework 1.0** – AI Governance Framework (2023)
- **NIST SP 800-53 Rev. 5** – Security and Privacy Controls (2020)
- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
