# Cloud Cost Control Standard

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 04_SAAS_AND_CLOUD_GOVERNANCE
**Governance Scope:** Operational Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_SAAS_AND_CLOUD_GOVERNANCE

**Governance Scope:** Cloud cost optimization, monitoring, and accountability.

**Control Authority Relationship:** Implements:

- Layer 02: Financial Controls
- Layer 04: Resource Management Policy
- Cloud FinOps practices

## Purpose

Defines requirements for cloud cost management including budgeting, monitoring, optimization, and accountability.

## Governance Principles

- **Control-Centric Architecture:** Automated cost controls
- **Developer-Operational Alignment:** Cost visibility for engineers
- **Audit Traceability:** Cost attribution and reporting
- **Single Source of Truth:** Centralized cost tracking

## Budget and Alerts

**Requirement:** Set budgets and alerts for cloud spending.

**Developer Requirements:**

- Set monthly budget per environment (dev, staging, prod)
- Configure alerts at 50%, 80%, 100% of budget
- Alert engineering team and management
- Review budget usage weekly

## Resource Tagging for Cost Attribution

**Requirement:** Tag all resources for cost allocation.

**Cost Allocation Tags:**

- `CostCenter`
- `Team`
- `Application`
- `Environment`

## Cost Optimization Practices

**Automated Cleanup:**

- Delete orphaned resources (EBS volumes, unused IPs)
- Stop/delete dev/staging resources outside business hours
- Delete old snapshots (retention policy)

**Right-Sizing:**

- Monitor resource utilization (CPU, memory)
- Downsize over-provisioned instances
- Use auto-scaling for variable workloads

**Reserved Capacity:**

- Purchase reserved instances / savings plans for predictable workloads
- Analyze usage patterns for reservation opportunities

## Cost Monitoring

**Requirement:** Track and report cloud costs monthly.

**Metrics:**

- Cost per environment
- Cost per application
- Cost per team
- Month-over-month cost trend
- Cost anomalies (unexpected spikes)

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Budget Management | A.5.1 | PO.5 | - | APO06 |
| Cost Monitoring | A.5.37 | PO.5 | - | MEA01 |

## Developer Checklist

- [ ] Budget set for each environment
- [ ] Cost alerts configured
- [ ] Resources tagged for cost attribution
- [ ] Automated cleanup scripts deployed
- [ ] Monthly cost review scheduled

## References

- Cloud FinOps Foundation
- AWS Cost Optimization Best Practices
- Azure Cost Management Best Practices

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial cloud cost control standard |
