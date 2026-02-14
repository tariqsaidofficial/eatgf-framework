# Control Mapping Appendix – Secure SDLC

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Domain:** 01_SECURE_SDLC
**Classification:** Reference Standard
**Reference:** SECURE_SDLC_GOVERNANCE_STANDARD.md

---

## Purpose

This appendix provides detailed cross-reference mapping between EATGF Secure SDLC controls and authoritative external frameworks:

- ISO/IEC 27001:2022
- NIST Secure Software Development Framework (SP 800-218)
- OWASP Application Security Verification Standard (ASVS) v4.0
- OWASP Software Assurance Maturity Model (SAMM)
- COBIT 2019
- NIST SP 800-53 Rev. 5

This enables organizations to demonstrate compliance against multiple regulatory and audit frameworks using a single EATGF implementation.

---

## ISO/IEC 27001:2022 Mapping

### Annex A: Information Security Controls

| EATGF Control                     | ISO 27001:2022 Annex A                | Mapping Rationale                         |
| --------------------------------- | ------------------------------------- | ----------------------------------------- |
| Security Requirements Integration | A.8.1 – Asset management              | Document security assets and requirements |
|                                   | A.8.28 – Secure coding                | Embed security in development             |
| Design & Threat Modeling          | A.8.25 – Security architecture        | Design systems with security principles   |
| Secure Coding Practices           | A.8.28 – Secure coding                | Code-level vulnerability prevention       |
|                                   | A.8.29 – Security testing             | Test for security weaknesses              |
| Code Review Enforcement           | A.8.28 – Secure coding                | Peer review validates secure practices    |
|                                   | A.8.10 – Problem management           | Track and remediate issues                |
| Dependency Security               | A.8.31 – Secure development services  | Manage third-party components             |
|                                   | A.8.30 – Supplier code review         | Review external code                      |
| Secrets Management                | A.8.2 – Information security policies | Define secret handling policies           |
|                                   | A.8.3 – Access control                | Restrict access to credentials            |
| Logging & Monitoring              | A.8.15 – Access logging               | Audit all access events                   |
|                                   | A.8.16 – Monitoring                   | Detect security incidents                 |
| Artifact Integrity                | A.8.32 – Change management            | Track all production changes              |
|                                   | A.8.33 – Segregation of duties        | Separate build, test, deploy roles        |

---

## NIST SP 800-218 (Secure Software Development Framework) Mapping

### NIST SSDF Practice Mapping

| EATGF Control                         | NIST SSDF Practice                       | Mapping Detail                                     |
| ------------------------------------- | ---------------------------------------- | -------------------------------------------------- |
| **Security Requirements Integration** | **PW.1 – Prepare Workforce**             | Establish secure development training and policies |
|                                       | PW.1.1                                   | Identify workforce roles responsible for security  |
|                                       | PW.1.2                                   | Document training requirements                     |
| **Design & Threat Modeling**          | **PO.1 – Prepare Organization**          | Perform threat modeling and security analysis      |
|                                       | PO.1.1                                   | Create threat models for high-risk components      |
|                                       | PO.1.2                                   | Document security objectives                       |
| **Secure Coding Practices**           | **PS.2 – Protect Software**              | Implement secure coding standards                  |
|                                       | PS.2.1                                   | Use secure coding practices                        |
|                                       | PO.2 – Produce Well-Secured Software     | Implement coding standards                         |
|                                       | PO.2.1                                   | Establish and enforce secure coding standards      |
|                                       | PO.2.2                                   | Use approved tools for development                 |
| **Code Review Enforcement**           | **PO.4 – Produce Well-Secured Software** | Code review and configuration review               |
|                                       | PO.4.1                                   | Review code for security defects                   |
|                                       | PO.4.2                                   | Approve all code changes                           |
| **SAST/Dependency Scanning**          | **PO.3 – Produce Well-Secured Software** | Analyze dependencies and components                |
|                                       | PO.3.1                                   | Identify components and dependencies               |
|                                       | PO.3.2                                   | Document component usage                           |
|                                       | RV.1 – Respond to Vulnerabilities        | Review and verify vulnerabilities                  |
|                                       | RV.1.1                                   | Identify and document vulnerabilities              |
|                                       | RV.1.2                                   | Evaluate potential impacts                         |
| **Supply Chain Security**             | **RV.2 – Respond to Vulnerabilities**    | Analyze and fix vulnerabilities                    |
|                                       | RV.2.1                                   | Determine root causes                              |
|                                       | RV.2.2                                   | Fix vulnerabilities                                |
| **Secrets Management**                | **PS.2 – Protect Software**              | Protect credentials and configuration              |
|                                       | PS.2.3                                   | Externalize all secrets                            |
| **Logging & Monitoring**              | **RV.1 – Respond to Vulnerabilities**    | Monitor and detect vulnerabilities                 |
|                                       | RV.1.3                                   | Respond to vulnerability findings                  |
| **Artifact Integrity**                | **PS.3 – Protect Software**              | Protect built software                             |
|                                       | PS.3.1                                   | Sign artifacts                                     |
|                                       | PS.3.2                                   | Generate SBOM                                      |

---

## OWASP Application Security Verification Standard (ASVS) v4.0 Mapping

| EATGF Control                         | OWASP ASVS v4.0         | Requirements Met                        |
| ------------------------------------- | ----------------------- | --------------------------------------- |
| **Security Requirements Integration** | V1 – Architecture       | V1.1 Verify security requirements       |
|                                       | V1.2                    | Verify threat model exists              |
|                                       | V1.3                    | Verify architecture controls identified |
| **Design & Threat Modeling**          | V1.9                    | V1.9.1 Threat model identifies threats  |
|                                       | V1.9.2                  | Trust boundaries identified             |
|                                       | V1.9.3                  | External dependencies documented        |
| **Secure Coding Practices**           | V5 – Validation         | V5.1 – V5.5 Input validation controls   |
|                                       | V6 – Encoding           | V6.1 – V6.2 Output encoding             |
|                                       | V8 – Error Handling     | V8.1 – V8.5 Exception handling          |
|                                       | V14 – Configuration     | V14.1 Secure configuration management   |
| **Code Review**                       | V10 – Malicious Code    | V10.1 Code review process               |
|                                       | V10.2                   | Identify suspicious code patterns       |
|                                       | V10.3                   | Prevent time-of-check-time-of-use flaws |
| **Dependency Security**               | V13 – API & Web Service | V13.1 Secure API design                 |
|                                       | V13.2                   | Validate external API responses         |
| **Secrets Management**                | V2 – Authentication     | V2.4 Secure credential storage          |
|                                       | V3 – Session Management | V3.3 Session tokens                     |
|                                       | V14 – Configuration     | V14.5 Config file protection            |
| **Logging & Monitoring**              | V7 – Error Handling     | V7.4 Log sensitive information safely   |
|                                       | V8.3                    | Appropriate logging levels              |

---

## OWASP Software Assurance Maturity Model (SAMM) Mapping

| EATGF Control                         | OWASP SAMM Practice                  | Maturity Level                                  |
| ------------------------------------- | ------------------------------------ | ----------------------------------------------- |
| **Security Requirements Integration** | **Governance: Strategy & Metrics**   | SAMM Level 2                                    |
|                                       | **Governance: Education & Guidance** | Activities include secure requirements training |
| **Design & Threat Modeling**          | **Design: Threat Assessment**        | SAMM Level 2                                    |
|                                       |                                      | Document threat models for new services         |
| **Secure Coding Practices**           | **Implementation: Secure Build**     | SAMM Level 2                                    |
|                                       |                                      | Implement secure coding standards               |
|                                       | **Verification: Code Review**        | SAMM Level 2                                    |
|                                       |                                      | Perform security-focused code review            |
| **Code Review Enforcement**           | **Verification: Code Review**        | SAMM Level 3                                    |
|                                       |                                      | Automated code review tooling                   |
| **SAST/Dependency Scanning**          | **Verification: Security Testing**   | SAMM Level 2                                    |
|                                       |                                      | Automated SAST/SCA in pipeline                  |
| **Supply Chain Security**             | **Governance: Risk Management**      | SAMM Level 2                                    |
|                                       |                                      | Identify and manage dependency risks            |
| **Secrets Management**                | **Implementation: Secure Build**     | SAMM Level 2                                    |
|                                       |                                      | Secrets protected in configuration              |
| **Logging & Monitoring**              | **Operations: Incident Management**  | SAMM Level 2                                    |
|                                       |                                      | Incident logging and monitoring                 |
| **Artifact Integrity**                | **Operations: Release**              | SAMM Level 2                                    |
|                                       |                                      | Artifact signing and verification               |

---

## COBIT 2019 Mapping

| EATGF Control                         | COBIT Domain                           | Process                                           | Mapping                             |
| ------------------------------------- | -------------------------------------- | ------------------------------------------------- | ----------------------------------- |
| **Security Requirements Integration** | **Align, Plan and Organise (APO)**     | APO01 – Set the Direction of I.T.                 | Define security objectives          |
|                                       |                                        | APO07 – Manage Information Technology Knowledge   | Workforce security training         |
| **Design & Threat Modeling**          | **Build, Acquire and Implement (BAI)** | BAI03 – Manage Solutions Identification and Build | Threat modeling in design           |
|                                       |                                        | BAI05 – Manage Organizational Change Enablement   | Architecture security design        |
| **Secure Coding Practices**           | **BAI**                                | BAI06 – Manage IT Changes                         | Secure coding in development        |
|                                       |                                        | BAI09 – Manage Service Agreements                 | Developer security responsibilities |
| **Code Review Enforcement**           | **Deliver, Service and Support (DSS)** | DSS05 – Manage Access and Security                | Control access to code              |
|                                       |                                        | DSS06 – Manage IT Security                        | Secure development practices        |
| **SAST/Dependency Scanning**          | **BAI**                                | BAI03 – Manage Solutions Identification and Build | SAST/SCA in build process           |
|                                       |                                        | BAI06 – Manage IT Changes                         | Dependency management               |
| **Supply Chain Security**             | **APO**                                | APO12 – Manage Risk                               | Supply chain risk assessment        |
|                                       |                                        | APO10 – Manage Vendors                            | Third-party component governance    |
| **Secrets Management**                | **DSS**                                | DSS02 – Manage System Security                    | Credential protection               |
|                                       |                                        | DSS05 – Manage Access and Security                | Access control to secrets           |
| **Logging & Monitoring**              | **DSS**                                | DSS01 – Manage Operations                         | Security event logging              |
|                                       |                                        | DSS06 – Manage IT Security                        | Security monitoring                 |
| **Artifact Integrity**                | **DSS**                                | DSS05 – Manage Access and Security                | Change management                   |
|                                       |                                        | DSS06 – Manage IT Security                        | Release integrity                   |

---

## NIST SP 800-53 Rev. 5 Mapping

| EATGF Control             | NIST 800-53 Control                      | Mapping                           |
| ------------------------- | ---------------------------------------- | --------------------------------- |
| **Security Requirements** | **SA-3: System Development Life Cycle**  | Integrate security into SDLC      |
|                           | **SI-7: Information System Monitoring**  | Monitor for security events       |
| **Threat Modeling**       | **SA-11: System Security Evaluation**    | Develop security architecture     |
|                           | **RA-2: Security Categorization**        | Classify system components        |
| **Secure Coding**         | **SA-11: Developer Security**            | Implement secure coding practices |
|                           | **SI-11: Error Handling**                | Secure error handling             |
| **Code Review**           | **SA-3: Code Review**                    | Review code for security          |
|                           | **CM-3: Change Control**                 | Approve code changes              |
| **Dependency Security**   | **SA-3: Supply Chain**                   | Manage external components        |
|                           | **RA-5: Vulnerability Scanning**         | Identify vulnerable dependencies  |
| **Secrets Management**    | **IA-4: Identifier Management**          | Manage credentials                |
|                           | **IA-5: Authentication Mechanics**       | Cryptographic mechanisms          |
|                           | \*\*IA-6: Access to Authentication       | Protect authentication data       |
| **Logging & Monitoring**  | **AU-12: Audit and Accountability**      | Generate audit logs               |
|                           | **AU-2: Audit Events**                   | Define auditable events           |
|                           | **SI-4: System Monitoring**              | Monitor information systems       |
| **Artifact Integrity**    | **CA-7: Continuous Monitoring**          | Monitor artifacts and changes     |
|                           | **CM-5: Access Restrictions for Change** | Control artifact deployment       |

---

## Framework Compliance Matrices

### Can EATGF Secure SDLC Help Achieve These Certifications?

#### ISO 27001:2022 Certification

| Requirement                    | EATGF Coverage | Gap Analysis                         |
| ------------------------------ | -------------- | ------------------------------------ |
| A.8.28 – Secure coding         | **Full**       | All coding practices covered         |
| A.8.29 – Security testing      | **Full**       | SAST/SCA/DAST covered                |
| A.8.31 – Supplier code review  | **Full**       | Dependency and supply chain controls |
| A.8.25 – Security architecture | **Full**       | Threat modeling and design reviews   |

**Compliance Assessment:** ✓ Achievable with this standard

---

#### NIST SP 800-218 Compliance

| SSDF Practice Area                     | EATGF Coverage | Implementation                                 |
| -------------------------------------- | -------------- | ---------------------------------------------- |
| **PW – Prepare Workforce**             | **Full**       | Security training and champion program         |
| **PS – Protect Software**              | **Full**       | Repository protection, CI/CD security, secrets |
| **PO – Produce Well-Secured Software** | **Full**       | Threat modeling, secure coding, testing        |
| **RV – Respond to Vulnerabilities**    | **Full**       | Scanning, patching, incident response          |

**Compliance Assessment:** ✓ Complete implementation

---

#### SOC 2 Type II Certification

| SOC 2 Principle      | EATGF Coverage | Evidence                           |
| -------------------- | -------------- | ---------------------------------- |
| Security             | **Full**       | All 8 core controls                |
| Availability         | **Partial**    | Covered via incident response      |
| Processing Integrity | **Full**       | Artifact integrity, logging        |
| Confidentiality      | **Full**       | Secrets management, access control |
| Privacy              | **Full**       | Data classification, logging       |

**Compliance Assessment:** ✓ Strong foundation

---

#### PCI DSS v3.2.1 Compliance

| PCI DSS Requirement          | EATGF Control | Mapping                           |
| ---------------------------- | ------------- | --------------------------------- |
| 6.2 – Secure configuration   | Secure Coding | Encode data correctly             |
| 6.3 – Security testing       | SAST/SCA      | Code scanning for vulnerabilities |
| 6.4 – Code review            | Code Review   | Security peer review              |
| 6.5.1 – Injection prevention | Secure Coding | Input validation                  |
| 6.5.7 – XSS prevention       | Secure Coding | Output encoding                   |

**Compliance Assessment:** ✓ Partial support (combined with ops controls)

---

## Control Implementation Calendar

### Year 1 – Foundation (Level 2)

| Quarter | Deliverable                        | Controls Affected                |
| ------- | ---------------------------------- | -------------------------------- |
| Q1      | Secure SDLC policy adoption        | Requirements, threat modeling    |
| Q2      | CI/CD security gate implementation | SAST, SCA, code review           |
| Q3      | Developer training program         | Security coding, threat modeling |
| Q4      | Audit and compliance testing       | Logging, monitoring setup        |

---

### Year 2 – Maturity (Level 3)

| Quarter | Deliverable                  | Controls Affected                |
| ------- | ---------------------------- | -------------------------------- |
| Q1      | Automated policy enforcement | All controls via pipeline        |
| Q2      | Secrets vault deployment     | Secrets management               |
| Q3      | Runtime security monitoring  | Logging and monitoring           |
| Q4      | Artifact signing and SBOM    | Artifact integrity, supply chain |

---

### Year 3 – Optimization (Level 4-5)

| Quarter | Deliverable                    | Controls Affected       |
| ------- | ------------------------------ | ----------------------- |
| Q1      | AI-assisted code review        | Code review automation  |
| Q2      | Advanced threat modeling       | Design, threat modeling |
| Q3      | Supply chain risk dashboard    | Dependency security     |
| Q4      | Red team / penetration testing | Full SDLC testing       |

---

## Terminology & Definitions

| Term              | Definition                                                            |
| ----------------- | --------------------------------------------------------------------- |
| **SAST**          | Static Application Security Testing – analyzes code without execution |
| **SCA**           | Software Composition Analysis – scans for vulnerable dependencies     |
| **DAST**          | Dynamic Application Security Testing – tests via API/web interface    |
| **SBOM**          | Software Bill of Materials – inventory of components and dependencies |
| **Threat Model**  | Analysis of potential attacks and mitigations                         |
| **Secrets**       | Credentials (API keys, passwords, certificates)                       |
| **CI/CD**         | Continuous Integration / Continuous Deployment pipelines              |
| **Code Review**   | Peer examination of code changes for security and quality             |
| **Secure Coding** | Practices that prevent common vulnerabilities (injection, XSS, etc.)  |

---

## Version History

| Version | Date       | Change Type | Description                                                                               |
| ------- | ---------- | ----------- | ----------------------------------------------------------------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial control mapping across ISO 27001, NIST SSDF, OWASP ASVS, SAMM, COBIT, NIST 800-53 |
