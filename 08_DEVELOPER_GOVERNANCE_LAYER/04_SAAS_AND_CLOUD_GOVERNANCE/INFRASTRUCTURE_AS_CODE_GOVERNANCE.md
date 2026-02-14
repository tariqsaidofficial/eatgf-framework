# Infrastructure as Code Governance

## Document Metadata

**Version:** 1.0  
**Issue Date:** 2026-02-14  
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER  
**Subdomain:** 04_SAAS_AND_CLOUD_GOVERNANCE  
**Governance Scope:** Implementation Standard  
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_SAAS_AND_CLOUD_GOVERNANCE

**Governance Scope:** IaC development, security scanning, version control, and deployment standards.

**Control Authority Relationship:** Implements:

- Layer 02: Change Management Controls
- Layer 04: Information Security Policy
- IaC security best practices

## Purpose

Defines requirements for Infrastructure as Code (IaC) including code standards, security scanning, testing, and deployment processes.

## Governance Principles

- **Security-by-Design:** IaC security scanning before deployment
- **Control-Centric Architecture:** Policy-as-code enforcement
- **Developer-Operational Alignment:** GitOps workflow
- **Audit Traceability:** Version-controlled infrastructure changes

## IaC Security Scanning

**Requirement:** Scan IaC for security misconfigurations before deployment.

**Approved Tools:**

- **Checkov:** Multi-cloud, comprehensive rules
- **tfsec:** Terraform-specific
- **Terrascan:** Policy-as-code
- **KICS:** Multi-IaC support

**Developer Requirements:**

- Run IaC security scan in CI/CD pipeline
- Fail deployment on critical/high findings
- Remediate findings before merging

**Example CI/CD Integration:**

```yaml
- name: Run Checkov
  run: |
    checkov -d . --framework terraform --soft-fail-on MEDIUM,LOW
```

## IaC Code Review

**Requirement:** Peer review for all IaC changes.

**Review Checklist:**

- [ ] Least-privilege IAM policies
- [ ] Encryption enabled for data at rest and in transit
- [ ] No hard-coded credentials
- [ ] Network security groups/firewalls configured
- [ ] Logging and monitoring enabled
- [ ] Cost implications reviewed

## IaC Testing

**Requirement:** Test IaC before production deployment.

**Testing Levels:**

1. **Static Analysis:** Security scanning (Checkov)
2. **Unit Tests:** Terraform validate, policy checks
3. **Integration Tests:** Deploy to ephemeral environment
4. **Compliance Tests:** Policy validation (OPA, Sentinel)

## State Management

**Requirement:** Secure IaC state file storage.

**Developer Requirements (Terraform):**

- Use remote backend (S3 + DynamoDB, Terraform Cloud)
- Enable state file encryption
- Enable state locking
- Do not commit state files to version control
- Restrict access to state files (contains sensitive data)

## Control Mapping

| EATGF Context         | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
| --------------------- | -------------- | --------- | ----- | ----- |
| IaC Security Scanning | A.8.29         | RV.1      | -     | BAI07 |
| Code Review           | A.8.26         | PS.2      | -     | BAI03 |
| State Security        | A.8.24         | PS.2      | -     | DSS05 |

## Developer Checklist

- [ ] IaC stored in version control
- [ ] Security scanning integrated in CI/CD
- [ ] Peer review completed
- [ ] Remote state backend configured
- [ ] State file encryption enabled

## References

- Terraform Best Practices
- Checkov Documentation (https://www.checkov.io/)
- NIST SP 800-218 (SSDF)

## Version History

| Version | Date       | Change Type | Description                     |
| ------- | ---------- | ----------- | ------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial IaC governance standard |
