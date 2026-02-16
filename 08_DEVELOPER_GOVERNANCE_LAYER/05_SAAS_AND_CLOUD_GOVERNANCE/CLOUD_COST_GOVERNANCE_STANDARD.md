# Cloud Cost Governance Standard

| Property           | Value                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Document Type**  | Implementation Standard                                                                                           |
| **Version**        | 1.0                                                                                                               |
| **Classification** | Governance                                                                                                        |
| **Effective Date** | February 16, 2026                                                                                                 |
| **Authority**      | Chief Technology Officer                                                                                          |
| **EATGF Layer**    | 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE                                                      |
| **MCM Reference**  | [EATGF-CLD-MON-01: Cloud Cost, Performance & Compliance Monitoring](../../00_FOUNDATION/MASTER_CONTROL_MATRIX.md) |

---

## Purpose

Cloud infrastructure costs escalate rapidly without disciplined cost governance. This standard establishes **predictable budgeting, anomaly detection, and continuous cost optimization** to:

- **Prevent runaway cloud spending** through budget enforcement
- **Optimize infrastructure costs** through right-sizing and commitments
- **Enable cost attribution** to business units and projects
- **Provide cost transparency** for decision-making
- **Maintain service quality** while reducing waste

**Mandatory:** All cloud infrastructure (AWS, GCP, Azure) must implement cost governance per this standard.

---

## Architectural Position

**Upstream Dependencies:**

- Layer 02 Control Architecture [EATGF-CLD-MON-01: Cloud Cost, Performance & Compliance Monitoring]
- Layer 04 INFORMATION_SECURITY_POLICY (budget authorization procedures)
- Layer 05 DOMAIN_FRAMEWORKS (cost requirements in architectural decisions)

**Downstream Usage:**

- Layer 06 AUDIT_AND_ASSURANCE (cost variance findings)
- Layer 08.04 INFRASTRUCTURE_RUNTIME (infrastructure cost reporting)

**Cross-Layer References:**

- ZERO_TRUST_ARCHITECTURE_STANDARD.md (network cost implications)
- MULTI_TENANCY_GOVERNANCE_STANDARD.md (cost per customer)
- INFRASTRUCTURE_AS_CODE_GOVERNANCE.md (IaC cost estimation)

---

## Governance Principles

1. **Cost Visibility:** Every infrastructure resource tags cost center; monthly dashboards published
2. **Budget Accountability:** Team leads approve resource lifecycle; cost overages require escalation
3. **Waste Prevention:** Auto-shutdown of idle resources; reserved capacity for committed workloads
4. **Cost Optimization:** Quarterly reviews identify rightsizing opportunities; target 10-15% YoY cost reduction
5. **Stakeholder Alignment:** Finance, Engineering, Product aligned on cloud budget trade-offs

---

## Technical Implementation

### 1. Cost Tagging & Attribution

**Mandatory Tag Structure:**

Every cloud resource must have these tags:

```yaml
# AWS example
Tags:
  CostCenter: "engineering" # billing code
  Project: "platform-apis" # project identifier
  Environment: "production" # prod/staging/dev
  Owner: "platform-team" # person/team responsible
  AutoShutdown: "false" # auto-shut down after hours?
  Lifecycle: "permanent" # permanent/temporary/experiment
```

**Tag Enforcement:**

- AWS: IAM policy prevents resource creation without tags
- GCP: Organization Policy requires labels
- Azure: Azure Policy requires tags
- Automation: Daily scan for untagged resources; automatic termination if not tagged within 48h

**Billing Allocation:**

Monthly cost report by tag:

```
Cost Center Report (February 2026):
┌─────────────────┬──────────┬─────────┬──────────┐
│ Cost Center     │ Budget   │ Spent   │ Variance │
├─────────────────┼──────────┼─────────┼──────────┤
│ Engineering     │ $50,000  │ $48,200 │ -3.6%    │
│ Data Science    │ $30,000  │ $31,500 │ +5%      │
│ DevOps          │ $20,000  │ $19,800 │ -1%      │
│ Infrastructure  │ $15,000  │ $14,900 │ -0.7%    │
└─────────────────┴──────────┴─────────┴──────────┘

Total Budget: $115,000 | Total Spent: $114,400 | Variance: -0.5% 
```

### 2. Budget Tiers & Escalation

**Tier-1 (Under-utilized: <50% committed):**

- Action: Notify team lead
- Timeline: 1 week to resize or confirm necessity
- Escalation: Finance review if not addressed

**Tier-2 (Expected: 50-100% committed):**

- Action: Normal operation; monitor for efficiency
- Success: 80-90% utilization (not all resources always at peak)

**Tier-3 (Approaching limit: 80-100% budget spent):**

- Action: Alert team lead and cost owner
- Timeline: 48h decision (reduce scope or increase budget)
- Escalation: CTO approval required for budget increase

**Tier-4 (Exceeded: 100%+ budget spent):**

- Action: IMMEDIATE suspension of new resources
- Temporary: Existing workloads continue; no scaling
- Escalation: Finance + CTO review; emergency budget decision

### 3. Reserved Capacity & Commitment Discounts

**Commitment Strategy:**

For predictable baseline load, purchase multi-year discounts:

```
AWS Reserved Instances (RI):
- Production database: 3-year RI = 72% discount = $8,000/month 
- Predictable API servers: 1-year RI = 40% discount = $3,200/month 
- Test/staging: On-demand only = no commitment 

GCP Commitments:
- Compute Engine: $50k/year commitment = 37% discount
- BigQuery: $2k/month commitment = 25% discount + priority queue

Azure Reserved Instances:
- Production VMs: 3-year RI + hybrid benefit = 72% discount
- SQL Database: RI for primary replicas; on-demand for standby
```

**Savings Plan vs. Reserved Instances:**

- **Reserved Instances (RIs):** Fixed resource = predictable workloads (databases, always-on APIs)
- **Savings Plans:** Flexible compute = variable workloads (batch jobs, dynamic scaling)
- **Target:** 60-70% of infrastructure via commitments; 30-40% on-demand for flexibility

**Review Frequency:**

- Quarterly: Analyze actual usage vs. commitments
- If < 60% utilization: Reduce commitment size
- If > 90% utilization: Consider additional commitments
- Annual: Full RI/commitment refresh aligned with budget cycle

### 4. Idle Resource Cleanup

**Auto-Shutdown Policy:**

Resources in "development" or "experiment" environments auto-shutdown:

```bash
# AWS: EC2 auto-shutdown (Lambda scheduled event)
# Off-hours: 7 PM - 7 AM UTC and weekends
if (Resource.Tag.AutoShutdown == "true" and Hour > 19 or Hour < 7) {
  instance.stop()  # not terminate; preserve data
  sns_notify("Instance ${instance.name} stopped by auto-shutdown policy")
}

# Excluded: Production tagged resources never auto-stop
# Excluded: Databases (RDS) unless explicitly tagged

# Cost savings: ~30% reduction in compute costs in dev/staging
```

**Orphaned Resource Detection:**

Monthly scan for unused resources:

```python
# Detect unused EC2 instances (no network traffic > 7 days)
unused_instances = []
for instance in ec2.instances:
    network_stats = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='NetworkIn',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance.id}],
        StartTime=now - timedelta(days=7),
        EndTime=now,
        Period=86400  # 1 day
    )
    if sum(datapoint['Sum'] for datapoint in network_stats) == 0:
        unused_instances.append(instance)

# Notification to owner
for instance in unused_instances:
    owner = instance.tags['Owner']
    send_email(owner, f"""
        Instance {instance.id} ({instance.tags['Project']}) has
        no network traffic for 7 days. Please confirm continued need or
        terminate to save ${instance.hourly_cost * 720}/month.

        Auto-terminate in 7 days unless confirmed.
    """)
```

**Termination Policy:**

- Day 1: Email notification to resource owner
- Day 4: Slack message; escalate to manager
- Day 8: Auto-terminate; archive logs for 30 days in case of incident

### 5. Cost Anomaly Detection

**Anomaly Definition:**

Cost increase flagged if any of these trigger:

```
Daily Spend Rules:
├─ >25% daily increase from 7-day average → ALERT
├─ Single resource >$1000/day → ALERT
├─ Unexpected >50% increase in data transfer → INVESTIGATE
└─ New resource >$500/month → REVIEW

Example:
Day 1-7 average spend: $3,500/day
Day 8 actual: $4,600/day
Flag: (+33% anomaly, meets >25% threshold) → Immediate investigation
```

**Investigation Process:**

1. **Automated:** CloudWatch + Cost Anomaly Detection + Slack bot alerts

   ```
    Cost Anomaly Detected
   Date: Feb 16 2026
   Amount: $4,600 (↑ 33% from $3,500 baseline)
   Primary driver: Data transfer EC2 to S3 (+$1,100)
   Likely cause: New ETL job in production

   Action: Review data transfer, confirm necessity, optimize or rollback
   Owner notification: Sent to platform-team@company.com
   ```

2. **Manual Investigation:**
   - Identify which resources caused increase (cost explorer drilldown)
   - Correlate with recent deployments (git log, release notes)
   - Determine if intentional (new feature) or unintended (misconfiguration)

3. **Remediation:**
   - **Intentional:** Update budget; plan cost reduction
   - **Misconfiguration:** Rollback deployment; optimize resource config
   - **Attack/Exploit:** Isolate compromised resource; investigate security incident

### 6. Chargeback & Cost Allocation

**Chargeback Model:**

Cost allocated to business units monthly:

```
Monthly Chargeback Report:
┌───────────────────────────────┬──────────┬──────────┬──────────┐
│ Business Unit                 │ Cost     │ Budget   │ Variance │
├───────────────────────────────┼──────────┼──────────┼──────────┤
│ Product (customer-facing)     │ $68,000  │ $70,000  │ -2.9%    │
│ Platform (shared infrastructure) │ $30,000 │ $30,000  │ 0%       │
│ Data Science (analytics)      │ $12,000  │ $15,000  │ -20%     │
│ DevOps (build/deployment)     │ $4,400   │ $5,000   │ -12%     │
└───────────────────────────────┴──────────┴──────────┴──────────┘
```

**Showback (Informational, no charge) vs. Chargeback (Actual billing):**

- **Startups/Scale-ups:** Showback only (cloud cost is opex shared budget)
- **Mature Organizations:** Chargeback to departments/projects
- **SaaS Companies:** Chargeback per customer (multi-tenant cost allocation)

### 7. Cost Optimization Roadmap

**Quarterly Cost Review:**

Every 3 months, cross-functional review identifies savings:

```
Q4 2025 Cost Optimization Review:
┌──────────────────────────────┬──────────┬──────────────┐
│ Optimization Opportunity     │ Savings  │ Implementation │
├──────────────────────────────┼──────────┼──────────────┤
│ Upgrade to latest Gen CPU    │ $2,100/m │ Jan-Feb      │
│ Increase RI commitment       │ $1,500/m │ Done (Feb)   │
│ Migrate colddata to S3 tier  │ $800/m   │ Mar-Apr      │
│ Optimize lambda memory alloc │ $600/m   │ Feb-Mar      │
│ Consolidate unused databases │ $950/m   │ Mar          │
├──────────────────────────────┼──────────┼──────────────┤
│ Total Projected Savings      │ $5,950/m │                │
│ Annual impact (12 months)    │ $71,400  │                │
│ Target % reduction           │ 6.2%     │ vs $115k baseline │
└──────────────────────────────┴──────────┴──────────────┘
```

**Process:**

1. Analyze 90-day spend data (waste, underutilization, optimization opportunities)
2. Prioritize by ROI (implementation effort vs. savings)
3. Assign owner; set implementation deadline
4. Track savings; report in next quarter

---

## Control Mapping

| EATGF Control                    | ISO 27001:2022   | NIST SSDF | COBIT 2019         | OWASP        |
| -------------------------------- | ---------------- | --------- | ------------------ | ------------ |
| Infrastructure Cost Optimization | A.8.1, A.12.2    | N/A       | BAI03.05, BAI09.02 | Not Directly |
| Budget Enforcement               | A.8.1            | N/A       | BAI01.01, BAI09.02 | Not Directly |
| Cost Attribution                 | A.8.17, A.6.7    | N/A       | MEA03.01           | Not Directly |
| Anomaly Detection                | A.8.16, A.12.4.1 | N/A       | DSS05.01           | Not Directly |

---

## Developer Checklist

- [ ] All cloud resources have mandatory tags (CostCenter, Project, Environment, Owner, AutoShutdown, Lifecycle)
- [ ] Team-level budget set in cloud provider; alerts configured at 80% and 100%
- [ ] Reserved instances/commitments purchased for all predictable baseline workloads
- [ ] Auto-shutdown policy enabled for dev/staging environments
- [ ] Unused resource detection scan running weekly; notifications sent to owners
- [ ] Cost anomaly detection integrated with Slack alerts
- [ ] Monthly cost report generated and reviewed by team leads
- [ ] Quarterly cost optimization review conducted; opportunities prioritized
- [ ] Finance team has read-only access to cost dashboard
- [ ] Chargeback model documented and communicated to stakeholders
- [ ] Cost governance training completed for all team members
- [ ] Annual budget plan includes historical trend analysis

---

## Governance Implications

**Risk if not implemented:**

- Unchecked cloud spending; 30-50% of resources unused/underutilized
- Budget overruns with no visibility until end of month
- Inefficient infrastructure (paying for unused capacity)
- Business units unable to understand cost-benefit trade-offs

**Operational impact:**

- Finance team gains infrastructure cost visibility and predictability
- Engineering teams empowered to optimize within budget guardrails
- Product teams can make cost-aware infrastructure decisions
- Monthly chargeback discipline ensures efficient resource use

**Audit consequences:**

- External auditors verify budget enforcement controls (compliance)
- Cost governance demonstrates infrastructure management maturity
- Anomaly detection shows proactive waste prevention

**Cross-team dependencies:**

- **Finance:** Budget approval and chargeback administration
- **Engineering:** Implement tagging, monitoring, optimization
- **Product:** Awareness of cost trade-offs in feature planning
- **Security:** Cost governance not security concern; coordinate on resource tags

---

## Official References

- **NIST SP 800-53 RA-3:** Risk Assessment
- **ISO 27001:2022 Annex A.8.1:** User endpoint devices
- **COBIT 2019 BAI03:** Manage Resource Optimization; BAI09: Assess and Manage IT Risks
- **AWS Cost Optimization:** https://aws.amazon.com/architecture/cost-optimization/ (official AWS best practices)
- **GCP Cost Management:** https://cloud.google.com/architecture/framework-for-cloud-cost-optimization (official GCP)
- **Azure Cost Management:** https://learn.microsoft.com/en-us/azure/cost-management-billing/ (official Azure)

---

## Version History

| Version | Date         | Change Type | Notes                                                                                                                                 |
| ------- | ------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Feb 16, 2026 | Major       | Initial release; comprehensive cost governance framework with budget tiers, commitment strategies, anomaly detection, cost allocation |

---

_Last Updated: February 16, 2026_
_EATGF v1.0-Foundation: Cloud Cost Governance Standard_
