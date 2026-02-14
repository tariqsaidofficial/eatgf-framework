# Data Residency and Compliance Standard

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 04_SAAS_AND_CLOUD_GOVERNANCE
**Governance Scope:** Compliance Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_SAAS_AND_CLOUD_GOVERNANCE

**Governance Scope:** Data residency requirements, cross-border data transfers, and regulatory compliance.

**Control Authority Relationship:** Implements:

- Layer 02: Data Protection Controls
- Layer 04: Data Governance Policy
- GDPR, CCPA, regional data protection laws

## Purpose

Defines requirements for data residency, sovereignty, and cross-border data transfer compliance.

## Governance Principles

- **Control-Centric Architecture:** Technical enforcement of data residency
- **Security-by-Design:** Data location controls by default
- **Audit Traceability:** Data location and transfer logging
- **Developer-Operational Alignment:** Transparent compliance controls

## Data Residency Requirements

**Requirement:** Store data in approved geographic regions based on data classification and customer location.

**Regional Requirements:**

| Region        | Data Types           | Storage Location | Cross-Border Transfer              |
| ------------- | -------------------- | ---------------- | ---------------------------------- |
| **EU**        | Personal data (GDPR) | EU region        | Requires SCCs or adequacy decision |
| **US**        | Customer data        | US region        | State-specific (CCPA, etc.)        |
| **China**     | Customer data        | China region     | Requires PIPL compliance           |
| **Australia** | Personal data        | Australia region | Privacy Act compliance             |

**Developer Requirements:**

- Configure cloud resources in compliant regions
- Use region-specific endpoints
- Block data replication to non-compliant regions
- Validate data residency in CI/CD

## Cross-Border Data Transfer Mechanisms

**EU to US (GDPR Compliance):**

- Standard Contractual Clauses (SCCs)
- Data Privacy Framework (if applicable)
- Encryption in transit and at rest

**Developer Requirements:**

- Document cross-border data flows
- Implement SCCs with cloud providers
- Obtain user consent where required
- Log international data transfers

## Data Sovereignty Controls

**Requirement:** Implement technical controls to enforce data sovereignty.

**Controls:**

- Region-locked storage buckets (AWS S3, Azure Blob)
- VPC/network-level geo-fencing
- Application-level region routing
- Monitoring for unauthorized cross-region access

## Encryption Requirements

**Requirement:** Encrypt data at rest and in transit.

**Developer Requirements:**

- Use AES-256 for data at rest
- Use TLS 1.3 / TLS 1.2 for data in transit
- Manage encryption keys regionally (no cross-region key access)
- Use customer-managed keys (CMK) for sensitive data

## Compliance Validation

**Requirement:** Regularly validate data residency compliance.

**Validation Activities:**

- Quarterly audit of data storage locations
- Review cloud configuration for region compliance
- Test data residency controls in CI/CD
- Generate compliance reports for auditors

## Control Mapping

| EATGF Context         | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
| --------------------- | -------------- | --------- | ----- | ----- |
| Data Residency        | A.5.23         | PO.3      | -     | APO02 |
| Cross-Border Transfer | A.5.14         | PS.1      | -     | DSS05 |
| Encryption            | A.8.24         | PS.2      | -     | DSS05 |

## Developer Checklist

- [ ] Data stored in compliant regions
- [ ] Cross-border transfer mechanisms documented
- [ ] Region-locked storage configured
- [ ] Encryption enabled for data at rest and in transit
- [ ] Compliance validation automated

## References

- GDPR (General Data Protection Regulation)
- CCPA (California Consumer Privacy Act)
- PIPL (China Personal Information Protection Law)
- Standard Contractual Clauses (European Commission)
- NIST SP 800-144: Cloud Security and Privacy

## Version History

| Version | Date       | Change Type | Description                                    |
| ------- | ---------- | ----------- | ---------------------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial data residency and compliance standard |
