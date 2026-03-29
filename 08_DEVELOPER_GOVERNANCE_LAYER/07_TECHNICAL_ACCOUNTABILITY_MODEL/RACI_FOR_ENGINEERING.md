# RACI for Engineering

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 07_TECHNICAL_ACCOUNTABILITY_MODEL
**Governance Scope:** Accountability Framework
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 07_TECHNICAL_ACCOUNTABILITY_MODEL

**Governance Scope:** Responsibility assignment matrix for engineering activities and decision-making.

**Control Authority Relationship:** Implements:

- Layer 02: Organizational Controls
- Layer 04: Governance Charter
- COBIT APO01 (Managed Organizational Framework)

## Purpose

Defines accountability for engineering activities using RACI matrix (Responsible, Accountable, Consulted, Informed).

## Governance Principles

- **Control-Centric Architecture:** Clear accountability for control implementation
- **Developer-Operational Alignment:** Defined roles reduce ambiguity
- **Audit Traceability:** Accountability documented for audit
- **Single Source of Truth:** One person accountable per activity

## RACI Definitions

**R – Responsible:** Does the work to complete the task.

**A – Accountable:** Ultimately answerable for completion and approval. Only ONE person accountable per activity.

**C – Consulted:** Provides input before decision or action. Two-way communication.

**I – Informed:** Notified of decision or action after completion. One-way communication.

## Engineering RACI Matrix

### Software Development Lifecycle

| Activity                     | Developer | Tech Lead | Eng Manager | Security Champion        | Product Owner | DevOps |
| ---------------------------- | --------- | --------- | ----------- | ------------------------ | ------------- | ------ |
| **Feature Design**           | R         | C         | I           | C                        | A             | I      |
| **Code Implementation**      | R/A       | C         | I           | I                        | I             | I      |
| **Code Review**              | R         | R         | I           | C (if security-relevant) | I             | I      |
| **Unit Testing**             | R/A       | C         | I           | I                        | I             | I      |
| **Integration Testing**      | R         | A         | I           | I                        | C             | R      |
| **Deployment to Staging**    | R         | A         | I           | I                        | I             | C      |
| **Deployment to Production** | I         | A         | I           | C                        | I             | R      |
| **Release Approval**         | I         | C         | A           | C                        | C             | I      |

### Security and Compliance

| Activity                       | Developer | Tech Lead | Eng Manager | Security Champion | Security Team | Compliance |
| ------------------------------ | --------- | --------- | ----------- | ----------------- | ------------- | ---------- |
| **Threat Modeling**            | R         | C         | I           | A                 | C             | I          |
| **Security Code Review**       | I         | C         | I           | R/A               | C             | I          |
| **SAST/SCA Remediation**       | R         | C         | I           | A                 | C             | I          |
| **DAST Findings**              | R         | A         | I           | C                 | C             | I          |
| **Vulnerability Disclosure**   | C         | C         | I           | I                 | R/A           | I          |
| **Security Incident Response** | R         | R         | I           | R                 | A             | I          |
| **Compliance Documentation**   | C         | C         | C           | C                 | I             | R/A        |
| **Security Exception Request** | I         | C         | C           | R                 | A             | C          |

### Infrastructure and DevOps

| Activity                        | Developer | Tech Lead | Eng Manager | DevOps | Security | SRE |
| ------------------------------- | --------- | --------- | ----------- | ------ | -------- | --- |
| **CI/CD Pipeline Config**       | C         | R         | I           | A      | C        | I   |
| **Infrastructure as Code**      | C         | C         | I           | R/A    | C        | C   |
| **Cloud Resource Provisioning** | I         | C         | I           | R/A    | C        | C   |
| **Production Monitoring**       | C         | C         | I           | R      | I        | A   |
| **Incident Response (Infra)**   | I         | C         | I           | R      | I        | A   |
| **Capacity Planning**           | C         | C         | C           | R      | I        | A   |
| **Cost Optimization**           | C         | C         | C           | R/A    | I        | C   |

### API and Architecture

| Activity                         | Developer | Tech Lead | Eng Manager | Architect | Product Owner | API Consumers |
| -------------------------------- | --------- | --------- | ----------- | --------- | ------------- | ------------- |
| **API Design**                   | R         | A         | I           | C         | C             | C             |
| **OpenAPI Spec Definition**      | R/A       | C         | I           | C         | I             | I             |
| **API Versioning**               | R         | A         | I           | C         | C             | I             |
| **Breaking Change Approval**     | I         | C         | A           | C         | C             | I             |
| **API Deprecation**              | C         | C         | C           | R/A       | C             | I             |
| **Architecture Decision Record** | R         | A         | C           | C         | I             | I             |

### Data Governance

| Activity                           | Developer | Tech Lead | Eng Manager | Data Engineer | DPO | Legal |
| ---------------------------------- | --------- | --------- | ----------- | ------------- | --- | ----- |
| **Data Model Design**              | R         | A         | I           | C             | I   | I     |
| **Data Classification**            | C         | C         | I           | R             | A   | C     |
| **Data Retention Policy**          | I         | C         | C           | C             | C   | R/A   |
| **Data Privacy Impact Assessment** | C         | C         | C           | R             | A   | C     |
| **Data Breach Response**           | I         | I         | I           | R             | A   | C     |

### Change Management

| Activity                    | Developer | Tech Lead | Eng Manager | DevOps | Security | Product Owner |
| --------------------------- | --------- | --------- | ----------- | ------ | -------- | ------------- |
| **Standard Change Request** | R         | A         | I           | I      | I        | I             |
| **Normal Change Request**   | R         | A         | I           | C      | C        | I             |
| **Major Change Request**    | R         | C         | A           | C      | C        | C             |
| **Emergency Change**        | R         | A         | I           | C      | I        | I             |
| **Post-Incident Review**    | R         | A         | C           | C      | C        | I             |

## Role Descriptions

### Developer

**Responsibilities:**

- Implement features and bug fixes
- Write and maintain tests
- Participate in code reviews
- Remediate security findings
- Document code and technical decisions

### Tech Lead

**Responsibilities:**

- Approve technical designs and code
- Mentor developers
- Ensure code quality and standards compliance
- Accountable for feature delivery
- Conduct technical interviews

### Engineering Manager

**Responsibilities:**

- Approve major changes and releases
- Manage team performance and growth
- Allocate resources and prioritize work
- Escalate issues to leadership
- Budget and headcount planning

### Security Champion

**Responsibilities:**

- Review security-sensitive code
- Champion security best practices within team
- Conduct or facilitate threat modeling
- Triage security findings
- Liaison with central security team

### Security Team

**Responsibilities:**

- Define security policies and standards
- Provide security training and guidance
- Lead incident response for security events
- Approve security exceptions
- Perform security assessments

### DevOps / SRE

**Responsibilities:**

- Manage CI/CD infrastructure
- Provision and maintain cloud resources
- Monitor production systems
- Incident response for infrastructure issues
- Capacity planning and cost optimization

### Product Owner

**Responsibilities:**

- Define product requirements and priorities
- Approve feature designs
- Accept completed work
- Customer communication
- Roadmap planning

## Decision Escalation

**Requirement:** Escalate decisions when accountability unclear or consensus not reached.

**Escalation Paths:**

| Issue Type                  | Escalate From     | Escalate To                     |
| --------------------------- | ----------------- | ------------------------------- |
| Technical disagreement      | Developers        | Tech Lead                       |
| Technical complexity        | Tech Lead         | Engineering Manager             |
| Cross-team dependency       | Tech Lead         | Engineering Manager             |
| Security risk acceptance    | Security Champion | Security Team                   |
| Resource prioritization     | Product Owner     | VP Engineering / VP Product     |
| Major architecture decision | Tech Lead         | Architect / Engineering Manager |

## Control Mapping

| EATGF Context         | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
| --------------------- | -------------- | --------- | ----- | ----- |
| Accountability        | A.5.24         | PO.1      | -     | APO01 |
| Segregation of Duties | A.5.3          | PS.1      | -     | DSS06 |

## Developer Checklist

For every major activity:

- [ ] Identify who is Responsible
- [ ] Identify who is Accountable (only one person)
- [ ] Consult relevant stakeholders
- [ ] Inform appropriate parties after completion
- [ ] Document decisions and accountability

## References

- RACI Matrix (Wikipedia: https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)
- COBIT 2019: APO01 (Managed Organizational Framework)
- ITIL 4: Service Value System

## Version History

| Version | Date       | Change Type | Description                  |
| ------- | ---------- | ----------- | ---------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial RACI for engineering |
