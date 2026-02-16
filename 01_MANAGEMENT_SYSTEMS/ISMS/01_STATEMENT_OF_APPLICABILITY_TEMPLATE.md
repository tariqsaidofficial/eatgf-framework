# Statement of Applicability (SoA) - ISO 27001:2022
## Enterprise AI-Aligned Technical Governance Framework (EATGF)

**Organization:** [Organization Name]  
**Assessment Date:** [Date]  
**Valid From:** [Date] **To:** [Date]  
**Scope:** [Describe scope - e.g., "All IT systems and cloud infrastructure"]  
**Version:** 1.0  
**Classification:** Controlled - Management Only  

---

##  PURPOSE & AUTHORITY

This Statement of Applicability (SoA) formally documents:

1. **Which ISO 27001:2022 Annex A controls are applicable** to the organization
2. **Why** controls are included or excluded (justification)
3. **How** controls map to EATGF internal controls
4. **Current implementation status** of each control
5. **Risk justification** for any exclusions

### Authority & Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Information Security Officer (CISO) | ______________ | ______________ | __/__/__ |
| Chief Governance Officer (CGO) | ______________ | ______________ | __/__/__ |
| Head of Audit | ______________ | ______________ | __/__/__ |

---

##  SCOPE DEFINITION

### Within Scope
- [System 1: Describe systems in scope]
- [System 2: Describe systems in scope]
- [Location/Department: Describe]

### Out of Scope & Justification
- [System/Location: Justification for exclusion]

### Future Scope Items
- [Planned future systems with timeline]

---

##  SoA SUMMARY STATISTICS

| Metric | Value | Notes |
|--------|-------|-------|
| **Total ISO 27001 Annex A Controls** | 76 | Standard count |
| **Controls Selected (Applicable)** | ___ | To be populated |
| **Controls Excluded** | ___ | To be populated |
| **Applicability Rate** | __% | (Applicable / Total) |
| **Implementation Status** | | |
| • Fully Implemented | ___ | |
| • Partially Implemented | ___ | |
| • Not Yet Implemented | ___ | |
| **Implementation Readiness** | __% | (Implemented + Partial) / Applicable |

---

##  CONTROL-BY-CONTROL SoA TABLE

**Legend:**
-  **Applicable** = Control is relevant to organization
-  **Not Applicable** = Control is excluded with documented justification
-  **Fully Implemented** = Control operating effectively
-  **Partial** = Control partially implemented, improvement plan in place
-  **Not Started** = Control not yet implemented

### SECTION A.5: ORGANIZATIONAL CONTROLS

#### A.5.1: Policies for information security

| Field | Value |
|-------|-------|
| **ISO Control** | A.5.1 |
| **Control Name** | Policies for information security |
| **Applicable?** |  YES |
| **Justification** | Essential for governance framework - organization requires documented security policy suite |
| **EATGF Mapping** | EATGF-EDM-GOV-01, EATGF-APO-SEC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | /policies/02_INFORMATION_SECURITY_POLICY.md |
| **Owner** | Chief Information Security Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.5.2: Information security roles and responsibilities

| Field | Value |
|-------|-------|
| **ISO Control** | A.5.2 |
| **Control Name** | Information security roles and responsibilities |
| **Applicable?** |  YES |
| **Justification** | Required for accountability - ongoing security responsibility assignment needed |
| **EATGF Mapping** | EATGF-EDM-GOV-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Governance Charter (RACI matrix), ISMS Manual (Section 5) |
| **Owner** | Chief Governance Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.5.3: Segregation of duties

| Field | Value |
|-------|-------|
| **ISO Control** | A.5.3 |
| **Control Name** | Segregation of duties |
| **Applicable?** |  YES |
| **Justification** | Critical for fraud prevention and access control - organization processes require segregation |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | IAM policy, RBAC matrix (50% complete), SAP module segregation (20% complete) |
| **Owner** | Chief Information Security Officer |
| **Remediation Plan** | Complete RBAC matrix by Q1 2026, full implementation by Q2 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

#### A.5.4: Management responsibilities

| Field | Value |
|-------|-------|
| **ISO Control** | A.5.4 |
| **Control Name** | Management responsibilities for information security |
| **Applicable?** |  YES |
| **Justification** | Governance requirement - management must actively support information security |
| **EATGF Mapping** | EATGF-EDM-BEN-01, EATGF-APO-SEC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Board-approved ISMS charter, management KPIs, quarterly review meetings |
| **Owner** | Chief Executive Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

### SECTION A.6: PEOPLE CONTROLS

#### A.6.1: Screening

| Field | Value |
|-------|-------|
| **ISO Control** | A.6.1 |
| **Control Name** | Screening |
| **Applicable?** |  YES |
| **Justification** | Required for critical roles - background checks needed for access to sensitive systems |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | HR background check procedures, contractor vetting procedure |
| **Owner** | Chief Human Resources Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.6.2: Terms and conditions of employment

| Field | Value |
|-------|-------|
| **ISO Control** | A.6.2 |
| **Control Name** | Terms and conditions of employment |
| **Applicable?** |  YES |
| **Justification** | Legal requirement - all employees must acknowledge security policies and responsibilities |
| **EATGF Mapping** | EATGF-APO-SEC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Employment contract template (Section 4.5), annual acknowledgment process |
| **Owner** | Chief Human Resources Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.6.3: Information security awareness, education and training

| Field | Value |
|-------|-------|
| **ISO Control** | A.6.3 |
| **Control Name** | Information security awareness, education and training |
| **Applicable?** |  YES |
| **Justification** | Mandatory for all organizations - awareness training reduces human risk |
| **EATGF Mapping** | EATGF-APO-SEC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | Annual awareness training (100% completion), scheduled security workshops (2/year), role-based training (30% complete) |
| **Owner** | Chief Information Security Officer |
| **Remediation Plan** | Role-specific training by Q3 2026, phishing simulation by Q2 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

#### A.6.4: Disciplinary process

| Field | Value |
|-------|-------|
| **ISO Control** | A.6.4 |
| **Control Name** | Disciplinary process |
| **Applicable?** |  YES |
| **Justification** | Governance requirement - consistent enforcement needed for security violations |
| **EATGF Mapping** | EATGF-APO-SEC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Security incident response procedures (Section 6), discipline matrix in ISMS Manual |
| **Owner** | Chief Human Resources Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.6.5: Responsibilities after termination or change of employment

| Field | Value |
|-------|-------|
| **ISO Control** | A.6.5 |
| **Control Name** | Responsibilities after termination or change of employment |
| **Applicable?** |  YES |
| **Justification** | Risk mitigation - timely access removal required for departing/transferred employees |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | Offboarding checklist (90% implemented), SAP user removal (manual, 3-day cycle), system access removal (24h target, 80% compliance) |
| **Owner** | Chief Information Security Officer |
| **Remediation Plan** | Automated access removal system by Q2 2026, improve to 95% same-day compliance |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

### SECTION A.7: ACCESS CONTROL

#### A.7.1: Business requirement of access control

| Field | Value |
|-------|-------|
| **ISO Control** | A.7.1 |
| **Control Name** | Business requirement of access control |
| **Applicable?** |  YES |
| **Justification** | Foundational control - least privilege principle required across all systems |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | RBAC matrix (60% complete), access policy, role definitions (most systems) |
| **Owner** | Chief Information Security Officer |
| **Remediation Plan** | Complete RBAC audit by Q1 2026, all systems compliant by Q2 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

#### A.7.2: User registration and de-registration

| Field | Value |
|-------|-------|
| **ISO Control** | A.7.2 |
| **Control Name** | User registration and de-registration |
| **Applicable?** |  YES |
| **Justification** | Essential for identity management - documented process for user lifecycle |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | System access request form, approval workflow (Okta), quarterly access review |
| **Owner** | Identity & Access Management Lead |
| **Remediation Plan** | Automate provisioning by Q3 2026, achieve 100% timely de-registration |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

#### A.7.3: User access provision

| Field | Value |
|-------|-------|
| **ISO Control** | A.7.3 |
| **Control Name** | User access provision |
| **Applicable?** |  YES |
| **Justification** | Operational requirement - formal process for provisioning access |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Okta provisioning workflow, documented approval process, audit logs |
| **Owner** | Identity & Access Management Lead |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.7.4: Access due diligence and review

| Field | Value |
|-------|-------|
| **ISO Control** | A.7.4 |
| **Control Name** | Access due diligence and review |
| **Applicable?** |  YES |
| **Justification** | Compliance requirement - quarterly access reviews to maintain least privilege |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Quarterly access review process, signed approval from managers, remediation tracking |
| **Owner** | Chief Information Security Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.7.5: Access rights adjustment

| Field | Value |
|-------|-------|
| **ISO Control** | A.7.5 |
| **Control Name** | Access rights adjustment |
| **Applicable?** |  YES |
| **Justification** | Operational/governance - adjustments needed when roles change |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | System exceptions list (5 manual systems), Okta sync (95% automated) |
| **Owner** | Identity & Access Management Lead |
| **Remediation Plan** | Migrate remaining systems to identity platform by Q2 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

### SECTION A.8: CRYPTOGRAPHY

#### A.8.1: Cryptographic controls

| Field | Value |
|-------|-------|
| **ISO Control** | A.8.1 |
| **Control Name** | Cryptographic controls |
| **Applicable?** |  YES |
| **Justification** | Critical control - encryption required for data protection |
| **EATGF Mapping** | EATGF-DSS-ENC-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Encryption audit report, configuration evidence |
| **Standards** | AES-256 (at-rest), TLS 1.2+ (in-transit) |
| **Owner** | Chief Information Security Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.8.2: Cryptographic key management

| Field | Value |
|-------|-------|
| **ISO Control** | A.8.2 |
| **Control Name** | Cryptographic key management |
| **Applicable?** |  YES |
| **Justification** | Operational requirement - key management essential for encryption effectiveness |
| **EATGF Mapping** | EATGF-DSS-ENC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | HSM deployed in production (80% coverage), key rotation policy (manual for some), key audit trail |
| **Owner** | Chief Information Security Officer |
| **Remediation Plan** | Automated key rotation for all systems by Q2 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

### SECTION A.9: PHYSICAL AND ENVIRONMENTAL CONTROLS

[Example structure - continue for all A.9.x controls]

---

### SECTION A.10: OPERATIONS SECURITY

[Example structure - continue for all A.10.x controls]

---

### SECTION A.11: COMMUNICATIONS SECURITY

[Example structure - continue for all A.11.x controls]

---

### SECTION A.12: SYSTEM ACQUISITION, DEVELOPMENT AND MAINTENANCE

#### A.12.1: Security requirements of information and information processing systems

| Field | Value |
|-------|-------|
| **ISO Control** | A.12.1 |
| **Control Name** | Security requirements of information systems |
| **Applicable?** |  YES |
| **Justification** | Design control - security requirements needed before development begins |
| **EATGF Mapping** | EATGF-BAI-CHG-01, EATGF-BAI-TEST-01 |
| **Implementation Status** |  Partial |
| **Evidence** | Security requirements template (10% of projects), threat modeling (0% current), OWASP Top 10 checklist (pilot) |
| **Owner** | Engineering Lead |
| **Remediation Plan** | Implement security requirements in all new projects by Q3 2026, retroactive for 50% existing by Q4 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

#### A.12.2: Secure development, test and acceptance processes

| Field | Value |
|-------|-------|
| **ISO Control** | A.12.2 |
| **Control Name** | Secure SDLC processes |
| **Applicable?** |  YES |
| **Justification** | Quality/security requirement - formal SDLC testing required |
| **EATGF Mapping** | EATGF-BAI-CHG-01, EATGF-BAI-TEST-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | SDLC policy, test phase documentation, UAT process, security testing checklist |
| **Owner** | QA Lead / Engineering Lead |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.12.3: Secure development environment

| Field | Value |
|-------|-------|
| **ISO Control** | A.12.3 |
| **Control Name** | Secure development environment |
| **Applicable?** |  YES |
| **Justification** | Operational control - dev environment requires isolation and access control |
| **EATGF Mapping** | EATGF-BAI-CONF-01 |
| **Implementation Status** |  Partial |
| **Evidence** | Dev environment network isolation (80%), credential management (Vault, 70% coverage) |
| **Owner** | DevOps Lead |
| **Remediation Plan** | Complete dev environment segmentation by Q1 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

#### A.12.4: Change management

| Field | Value |
|-------|-------|
| **ISO Control** | A.12.4 |
| **Control Name** | Change management |
| **Applicable?** |  YES |
| **Justification** | Operational requirement - controlled changes essential |
| **EATGF Mapping** | EATGF-BAI-CHG-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Change management policy, CAB process, change log, rollback procedures |
| **Owner** | Engineering Lead |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.12.5: Access control for program and information systems

| Field | Value |
|-------|-------|
| **ISO Control** | A.12.5 |
| **Control Name** | Access control in development |
| **Applicable?** |  YES |
| **Justification** | Operational control - separation between dev/test/prod required |
| **EATGF Mapping** | EATGF-DSS-SEC-01 |
| **Implementation Status** |  Partial |
| **Evidence** | GitHub branch protection (90%), production access restrictions (85%), audit log |
| **Owner** | Identity & Access Management Lead |
| **Remediation Plan** | 100% branch protection and access restrictions by Q1 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

#### A.12.6: Management of technical vulnerabilities

| Field | Value |
|-------|-------|
| **ISO Control** | A.12.6 |
| **Control Name** | Management of technical vulnerabilities |
| **Applicable?** |  YES |
| **Justification** | Critical control - vulnerability scanning and patching required |
| **EATGF Mapping** | EATGF-DSS-VULN-01 |
| **Implementation Status** |  Fully Implemented |
| **Evidence** | Vulnerability scanning (monthly with Qualys), patch SLAs, patch history |
| **Owner** | Chief Information Security Officer |
| **Last Review** | [Date] |
| **Next Review** | [Date + 1 year] |

---

#### A.12.7: Information systems security testing

| Field | Value |
|-------|-------|
| **ISO Control** | A.12.7 |
| **Control Name** | Information systems security testing |
| **Applicable?** |  YES |
| **Justification** | Assurance control - security testing validates control effectiveness |
| **EATGF Mapping** | EATGF-BAI-TEST-01, EATGF-MEA-AUD-01 |
| **Implementation Status** |  Partial |
| **Evidence** | SAST (integrated into CI/CD, 100%), DAST (quarterly, 40% coverage), penetration testing (annual external) |
| **Owner** | Chief Information Security Officer |
| **Remediation Plan** | Expand DAST coverage to 100% by Q2 2026, internal pentesting program by Q3 2026 |
| **Last Review** | [Date] |
| **Next Review** | [Date + 6 months] |

---

### SECTION A.13: COMMUNICATIONS SECURITY

[Continue similarly...]

---

### SECTION A.14: SYSTEM ACQUISITION, DEVELOPMENT AND MAINTENANCE (Continued)

[Continue similarly...]

---

##  IMPLEMENTATION ROADMAP

### Phase 1: Achieve 95% Implementation (Current → EOY 2026)

| Control | Current | Target | Effort | Owner | Timeline |
|---------|---------|--------|--------|-------|----------|
| A.5.3 - Segregation of Duties | Partial | Full | Medium | CISO | Q1-Q2 2026 |
| A.6.3 - Security Training | Partial | Full | Low | CISO | Q2 2026 |
| A.6.5 - Offboarding | Partial | Full | Medium | CISO | Q1 2026 |
| A.7.1 - RBAC | Partial | Full | High | CISO | Q1-Q2 2026 |
| A.8.2 - Key Management | Partial | Full | High | CISO | Q2 2026 |
| A.12.1 - Security Requirements | Partial | Full | High | Eng Lead | Q2-Q3 2026 |
| A.12.3 - Dev Environment | Partial | Full | Medium | DevOps | Q1 2026 |
| A.12.5 - Dev Access Control | Partial | Full | Low | IAM Lead | Q1 2026 |
| A.12.7 - Security Testing | Partial | Full | High | CISO | Q2-Q3 2026 |

### Phase 2: Optimization (2027+)

- Achieve ISO 27001 certification
- Expand to 100% implementation across all controls
- Implement continuous monitoring for all controls
- Establish metrics-based control effectiveness program

---

##  EXCLUSIONS & JUSTIFIED NON-APPLICABILITY

| Control | Reason for Exclusion | Compensating Control | Review Date |
|---------|---------------------|---------------------|-------------|
| [Example] | [Reason] | [Alternative] | [Date] |

---

##  COMPLIANCE DASHBOARD

### Overall Status
- **Applicable Controls:** ___ / 76 (___%)
- **Fully Implemented:** ___ / ___ (___%)
- **Partially Implemented:** ___ / ___ (___%)
- **Not Started:** ___ / ___ (___%)
- **Overall Compliance:** ___%

### To Your Auditor
This SoA demonstrates that [Organization Name]:
1.  Has systematically selected applicable controls based on risk assessment
2.  Has documented implementation status for each control
3.  Has identified gaps and remediation plans
4.  Has assigned clear ownership for each control
5.  Has scheduled regular reviews

---

##  MAINTENANCE & UPDATES

**Owner:** Chief Information Security Officer  
**Review Frequency:** Semi-annually (Feb & Aug)  
**Emergency Updates:** Upon material changes to scope or risk profile  

**Next Scheduled Review:** [Date + 6 months]  
**Last Updated:** February 13, 2026

---

**Document Status:**  TEMPLATE READY FOR POPULATION  
**This template should be customized with your organization-specific data and control evidence.**
