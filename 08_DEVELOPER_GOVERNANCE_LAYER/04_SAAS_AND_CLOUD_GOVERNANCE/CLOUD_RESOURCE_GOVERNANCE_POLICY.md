# Cloud Resource Governance Policy

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 04_SAAS_AND_CLOUD_GOVERNANCE
**Governance Scope:** Policy
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_SAAS_AND_CLOUD_GOVERNANCE

**Governance Scope:** Cloud resource provisioning, tagging, lifecycle, and cost control policies.

**Control Authority Relationship:** Implements:

- Layer 02: Infrastructure Controls
- Layer 04: Information Security Policy
- Cloud provider best practices (AWS Well-Architected, Azure WAF, GCP Best Practices)

## Purpose

Defines governance for cloud resource management including provisioning standards, tagging requirements, lifecycle management, and cost optimization.

## Governance Principles

- **Control-Centric Architecture:** Policy-as-code enforcement
- **Security-by-Design:** Secure-by-default resource configuration
- **Audit Traceability:** Full resource change tracking
- **Developer-Operational Alignment:** Self-service with guardrails

## Resource Tagging Requirements

**Requirement:** All cloud resources must be tagged with mandatory metadata.

**Mandatory Tags:**

| Tag Key | Description | Example |
|---|---|---|
| `Environment` | Deployment environment | `production`, `staging`, `dev` |
| `Owner` | Team responsible | `backend-team` |
| `CostCenter` | Billing allocation | `engineering` |
| `Application` | Application name | `user-api` |
| `ManagedBy` | Provisioning method | `terraform`, `manual` |
| `DataClassification` | Data sensitivity | `public`, `internal`, `confidential` |

**Enforcement:** Use cloud policy engines (AWS Organizations SCP, Azure Policy, GCP Organization Policies) to block untagged resources.

## Infrastructure as Code (IaC)

**Requirement:** Provision all cloud resources via IaC.

**Approved Tools:**

- Terraform
- AWS CloudFormation / CDK
- Azure Resource Manager / Bicep
- Pulumi

**Developer Requirements:**

- Store IaC in version control
- Require code review for infrastructure changes
- Use IaC modules for reusable patterns
- Scan IaC for security issues (Checkov, tfsec)

## Access Control

**Requirement:** Implement least-privilege IAM policies.

**Developer Requirements:**

- Use role-based access (no user-based policies)
- Grant minimum necessary permissions
- Use managed policies where available
- Enable MFA for production access
- Use temporary credentials (STS, workload identity)

## Cost Control

**Requirement:** Implement cost monitoring and optimization.

**Developer Requirements:**

- Set budget alerts per environment
- Auto-scale resources based on demand
- Use reserved instances / savings plans
- Delete unused resources (orphaned volumes, old snapshots)
- Right-size instances based on utilization

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Resource Tagging | A.5.9 | PO.5 | - | APO13 |
| IaC | A.8.32 | PO.1 | - | BAI03 |
| Access Control | A.5.15 | PS.1 | - | DSS05 |

## Developer Checklist

- [ ] All resources tagged with mandatory tags
- [ ] Resources provisitioned via IaC
- [ ] Least-privilege IAM policies applied
- [ ] Cost budgets configured
- [ ] IaC security scanning enabled

## References

- AWS Well-Architected Framework
- Azure Well-Architected Framework
- GCP Best Practices
- NIST SP 800-144: Cloud Computing Security

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial cloud resource governance policy |
