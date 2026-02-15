# Cloud & SaaS Governance Standard

**Version:** 2.0-COMPREHENSIVE
**Status:** Active
**Authority:** EATGF Layer 08 (Developer Governance) - Domain 05
**Effective Date:** 2026-02-15
**Classification:** Internal - Governance & Operations

---

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / Domain 05_SAAS_AND_CLOUD_GOVERNANCE

**Document Authority:** Implements (does not define new) MCM controls:

- EATGF-CLD-ARCH-01: Cloud Architecture & Design Standards
- EATGF-CLD-SEC-01: Cloud Security & Compliance Configuration
- EATGF-CLD-MON-01: Cloud Cost, Performance & Compliance Monitoring
- EATGF-CLD-RES-01: Cloud Resilience & Disaster Recovery

**Relationship to EATGF:** Derivative document - operationalizes MCM cloud controls with implementation standards.

---

## Governance Principles

1. **Multi-Cloud Flexibility** -- Architecture supports deployment across AWS/Azure/GCP without lock-in; abstraction layers enable provider switching
2. **Shared Responsibility Clarity** -- Customer vs. provider security obligations explicitly documented per service model (IaaS/PaaS/SaaS)
3. **Compliance-by-Design** -- Security baselines aligned with CIS benchmarks; compliance tooling automated (no manual audit required)
4. **Cost Transparency** -- Real-time cost dashboards visible to technical teams; anomalies trigger investigation within 24 hours
5. **Resilience Over Performance** -- Multi-AZ/region redundancy prioritized; RTO/RPO targets based on business criticality, not technical convenience
6. **Continuous Monitoring** -- No "set it and forget it"; quarterly reviews of architecture, security posture, and cost efficiency

---

## Control 1: Cloud Architecture & Design Standards (EATGF-CLD-ARCH-01)

### Purpose

Organization maintains clear cloud architecture standards covering multi-cloud strategy, region selection, network design, and shared responsibility model documentation, enabling consistent secure-by-default cloud deployments.

### Cloud Strategy Document

**Required Sections:**

1. **Multi-Cloud Approach**
   - Single cloud (AWS/Azure/GCP) with rationale
   - Multi-cloud (active-active across providers)
   - Hybrid cloud (on-prem + cloud)
   - Key dependencies (e.g., customer mandates AWS, data residency requires local cloud)

2. **Region Selection Policy**
   - **Data Residency:** Where customer data must be stored (GDPR/CCPA/local regulations)
   - **Disaster Recovery:** Secondary region selected (e.g., US-East primary, US-West secondary for 500mi minimum separation)
   - **Performance:** Region selection based on latency requirements
   - **Cost:** Pricing differences documented (e.g., GCP cheaper for analytics)

3. **Network Architecture**
   - **VPC/VNet Design:** Subnet layout, public/private separation
   - **Security Groups:** Ingress/egress rules per tier (web, app, database)
   - **Load Balancing:** External LB for public APIs, internal LB for service mesh
   - **NAT/Bastion:** Secure access patterns documented

4. **Shared Responsibility Model**

| Service Model | Example                | Customer Responsibility                      | Provider Responsibility                                |
| ------------- | ---------------------- | -------------------------------------------- | ------------------------------------------------------ |
| **IaaS**      | EC2 / VM               | OS patching, firewalls, application security | Hypervisor, physical infrastructure, global redundancy |
| **PaaS**      | AppService / Cloud Run | Application code, data encryption keys       | OS patching, runtime, infrastructure                   |
| **SaaS**      | Salesforce / GitHub    | Data classification, access controls         | Everything; only configuration                         |

1. **Disaster Recovery Architecture**
   - RTO: Recovery Time Objective (e.g., 4 hours max downtime)
   - RPO: Recovery Point Objective (e.g., 1 hour data loss acceptable)
   - Cross-region replication enabled for critical databases
   - Failover testing quarterly documented

2. **Cost Optimization Framework**
   - Reserved instances: Commit to 1/3-year discount for predictable workloads
   - Spot instances: Use for batch/non-critical workloads (cost reduction 70-90%)
   - Rightsizing: Monthly analysis of under-utilized instances
   - Archive strategy: Data aged >90 days moved to cold storage

### Network Architecture Example

```
┌────────────────────────────────────────────────┐
│ Public Subnets (DMZ) - NAT Gateway             │
│ ┌──────────────┐  ┌──────────────┐             │
│ │ Web Tier 1   │  │ Web Tier 2   │  (ALB)      │
│ └──────────────┘  └──────────────┘             │
└────────────────────────────────────────────────┘
          ↓              ↓
┌────────────────────────────────────────────────┐
│ Private Subnets (App) - Network ACLs           │
│ ┌──────────────┐  ┌──────────────┐             │
│ │ App Tier 1   │  │ App Tier 2   │  (Service)  │
│ └──────────────┘  └──────────────┘             │
└────────────────────────────────────────────────┘
          ↓              ↓
┌────────────────────────────────────────────────┐
│ Data Subnets (DB) - Encryption at Rest         │
│ ┌──────────────────────────────────┐           │
│ │ RDS Multi-AZ Primary & Replica   │           │
│ └──────────────────────────────────┘           │
└────────────────────────────────────────────────┘
```

### Evidence Checklist

- [ ] Cloud architecture document published and approved
- [ ] Multi-cloud strategy documented (single/multi/hybrid decision with rationale)
- [ ] Region selection policy enforced (data residency, DR, latency)
- [ ] Network architecture diagram (VPC/VNet design with security groups)
- [ ] Shared responsibility matrix per provider (IaaS/PaaS/SaaS)
- [ ] Disaster recovery RTO/RPO targets defined
- [ ] Quarterly architecture review completed and documented

---

## Control 2: Cloud Security & Compliance Configuration (EATGF-CLD-SEC-01)

### Purpose

Cloud infrastructure enforces security baselines through encryption, network controls, access management, and automated compliance checking.

### Security Baseline Standards

**Encryption at Rest:**

- Database encryption: AWS KMS (customer-managed keys), Azure Key Vault, or GCP CMEK
- Key rotation: Annually minimum
- Application data in S3/Blob: Encrypted with customer-managed keys

**Encryption in Transit:**

- TLS 1.2 minimum (TLS 1.3 preferred)
- Certificates from trusted CAs (AWS Certificate Manager, DigiCert)
- Mutual TLS (mTLS) for service-to-service communication
- VPN tunnels for hybrid cloud connections

**Access Control:**

- **IAM Policies:** Least privilege principle (no wildcards, specific actions)
- **MFA:** Required for all console access (AWS IAM, Azure AD)
- **Federated Identity:** SAML/OIDC for SSO and centralized access
- **Service Accounts:** Short-lived credentials, rotated every 30 days

**Network Security:**

- **Security Groups:** Deny-by-default, explicit allow rules only
- **WAF:** Web Application Firewall enabled for public endpoints
- **DDoS:** AWS Shield Standard included; Shield Advanced for critical apps
- **VPC Flow Logs:** Enabled for all traffic analysis

### Auto-Compliance Checking

**Tools by Platform:**

| Platform  | Tool                                            | Checks                                 | Frequency  |
| --------- | ----------------------------------------------- | -------------------------------------- | ---------- |
| **AWS**   | AWS Config                                      | 50+ compliance rules (CIS benchmarks)  | Continuous |
| **AWS**   | CloudTrail + GuardDuty                          | Unauthorized access attempts           | Real-time  |
| **Azure** | Azure Policy                                    | Enforce tagging, encryption, NSG rules | Continuous |
| **GCP**   | Cloud Asset Inventory + Security Command Center | Resource compliance                    | Daily      |

**Critical Compliance Checks:**

- [ ] All S3 buckets encrypted (KMS keys, not S3-managed)
- [ ] S3 block public access enabled
- [ ] CloudTrail enabled for all regions (12-month retention)
- [ ] VPC Flow Logs enabled for all subnets
- [ ] Security groups deny-by-default (no 0.0.0.0/0 to ports <1024)
- [ ] MFA required for console access
- [ ] NAT gateways present (private subnets not directly internet-routable)
- [ ] Auto-scaling groups configured (high availability)

### Evidence Checklist

- [ ] Cloud security baseline document (CIS benchmarks applied)
- [ ] Encryption at rest enabled (customer-managed keys)
- [ ] Encryption in transit enforced (TLS 1.2+)
- [ ] MFA required for console access
- [ ] IAM policies follow least privilege
- [ ] Compliance scanner deployed (AWS Config / Azure Policy / GCP SCC)
- [ ] Scan results reviewed monthly; critical findings tracked to remediation
- [ ] CloudTrail/audit logging retained 12 months

---

## Control 3: Cloud Cost, Performance & Compliance Monitoring (EATGF-CLD-MON-01)

### Purpose

Real-time monitoring of cloud infrastructure performance, cost, and compliance enables rapid anomaly detection and cost optimization.

### Cost Monitoring Dashboard

**Metrics Tracked:**

1. **Monthly Cost Trend**
   - Budget vs. actual spend
   - Cost by service (compute, storage, data transfer)
   - Cost per application tier
   - Top 10 most expensive resources

2. **Cost Anomalies**
   - Threshold: >10% month-over-month variance
   - Alert: Triggered automatically; escalated to CFO/Finance
   - Investigation: Action plan within 24 hours

3. **Reserved Instance Utilization**
   - Target: >80% utilization of reserved capacity
   - Unused capacity identified and freed
   - Opportunity: Recommend RI purchase for static workloads

4. **Cost per User/Customer** (SaaS)
   - Calculated: Total cloud cost ÷ active users
   - Trend: Track weekly; alert if >10% increase week-over-week
   - Optimization: Identify cost drivers per customer segment

### Performance Monitoring

**Metrics:**

| Metric                     | Target        | Alert  |
| -------------------------- | ------------- | ------ |
| **API Latency (p99)**      | <200ms        | >500ms |
| **Uptime**                 | 99.95% (SaaS) | <99.5% |
| **Database Response Time** | <20ms         | >100ms |
| **Error Rate**             | <0.1%         | >1%    |

**Dashboards:**

- Real-time (CloudWatch / Azure Monitor / Cloud Monitoring)
- Updated every 1 minute
- Accessible to on-call engineers 24/7

### Compliance Monitoring

**Automated Checks (Continuous):**

```
AWS Config Rules:
  ✓ s3-bucket-server-side-encryption-enabled
  ✓ rds-encryption-enabled
  ✓ iam-policy-no-statements-with-admin-access
  ✓ cloudtrail-enabled
  ✓ internet-gateway-authorized-vpc-endpoints-only
  ✓ vpc-flow-logs-enabled

Azure Policy:
  ✓ Require encryption on storage accounts
  ✓ Enforce HTTPS only
  ✓ Enforce tag on resources
  ✓ Require MFA for Azure AD
```

**Monthly Compliance Report:**

- Compliance score (% resources compliant)
- Critical findings: Listed with remediation plan
- Cost impact analysis: (Compliance vs. cost trade-offs)

### Evidence Checklist

- [ ] Cost dashboard live (AWS Cost Explorer / Azure Cost Management)
- [ ] Cost anomaly alerts configured (>10% threshold)
- [ ] Monthly cost review meeting held; stakeholders notified
- [ ] Performance dashboard accessible to on-call team
- [ ] SLA: API latency p99 <200ms tracked weekly
- [ ] Compliance scan results reviewed monthly
- [ ] Critical findings tracked to remediation
- [ ] Quarterly cost optimization report approved

---

## Control 4: Cloud Resilience & Disaster Recovery (EATGF-CLD-RES-01)

### Purpose

Cloud infrastructure implements redundancy across availability zones/regions with defined RTO/RPO targets, enabling rapid recovery from infrastructure failures.

### Resilience Architecture

**High Availability (HA):**

```
Primary Region (US-East-1)
─────────────────────────────
  Availability Zone A       AZ B
  ┌─────────────┐    ┌─────────────┐
  │ App (1)     │    │ App (2)     │  (Multi-AZ)
  │ RDS Primary │    │ RDS Replica │
  └─────────────┘    └─────────────┘
       ↓                    ↓
       │        ALB         │
       └──────────────────────
              Route 53

↓ (Continuous replication)

Secondary Region (US-West-1)  [Disaster Recovery]
─────────────────────────────
  Availability Zone A       AZ B
  ┌─────────────┐    ┌─────────────┐
  │ App (Warm)  │    │ App (Warm)  │
  │ RDS Replica │    │ (Read-only) │
  └─────────────┘    └─────────────┘
```

### RTO/RPO Definitions

**Service Critical (Customer-facing APIs):**

- RTO: 1 hour (maximum acceptable downtime)
- RPO: 15 minutes (data loss acceptable)
- Strategy: Active-active multi-region

**Database (Customer Data):**

- RTO: 30 minutes (database failover)
- RPO: 5 minutes (18-point-in-time recovery with 5min intervals)
- Strategy: Multi-AZ primary + cross-region read replica

**Batch Processing (Non-critical):**

- RTO: 4 hours (can wait for maintenance window)
- RPO: 1 day (re-run yesterday's batch)
- Strategy: Single region, point-in-time restore

### Backup & Recovery Procedures

**Database Backup Strategy:**

```
Frequency: Every hour
Retention:
  - Daily backups: kept 7 days
  - Weekly backups: kept 4 weeks
  - Monthly backups: kept 12 months

Destination:
  - Primary region: 3 replicas (durability)
  - Secondary region: 1 replica (DR)
  - S3 Glacier: Monthly archives (compliance)

Recovery Testing:
  - Point-in-time restore: Tested monthly
  - Full region failover: Tested quarterly
```

**Failover Procedures (Documented & Tested):**

1. **Detection:** Monitoring alert triggers (primary region unavailable)
2. **Notification:** On-call team paged immediately
3. **Assessment:** Verify primary failure (not DNS issue)
4. **Failover:** Run automated failover script or manual steps:

   ```bash
   # Promote read replica to primary
   aws rds promote-read-replica --db-instance-identifier dr-db-instance

   # Update DNS to point to secondary
   aws route53 change-resource-record-sets --hosted-zone-id Z123 \
     --change-batch '{"Changes": [{"Action": "UPSERT", ...}]}'

   # Verify health checks passing
   ```

5. **Validation:** Application tests passing in secondary region
6. **Notification:** Stakeholders updated on status
7. **Post-Incident:** RCA documented within 24 hours

### Evidence Checklist

- [ ] Multi-AZ/region architecture documented
- [ ] RTO targets defined per service (1hr / 4hr / 1day as examples)
- [ ] RPO targets defined per service (5min / 15min / 1day as examples)
- [ ] Database backup strategy (frequency, retention, destinations)
- [ ] Backup restoration testing completed monthly (automated)
- [ ] Full failover test completed quarterly (documented)
- [ ] Failover procedures documented and accessible to on-call team
- [ ] Annual disaster recovery drill completed (full team participation)

---

## Compliance Alignment

| EATGF Control | ISO 27001:2022 | NIST 800-53       | CSA CAIQ |
| ------------- | -------------- | ----------------- | -------- |
| CLD-ARCH-01   | 5.23, A.8.23   | SA-9, RA-3        | GRC      |
| CLD-SEC-01    | 8.21, 8.22     | AC-3, SC-7, SC-28 | ILM, EKM |
| CLD-MON-01    | 9.1, 9.2       | AU-6, SI-4        | UEM      |
| CLD-RES-01    | 8.24, 8.25     | CP-2, CP-9        | BCR      |

### Governance Implications

**Risk if Not Implemented:**

- Cloud resources misconfigured; data exposure (S3 bucket public)
- Cost overruns (unchecked resource creation, unoptimized instances)
- No disaster recovery capability; single-region failure = total outage
- Compliance violations; audit findings

**Operational Impact:**

- Faster incident recovery (documented procedures, quarterly testing)
- Cost savings (10-20% through optimization without performance loss)
- Improved reliability (multi-AZ redundancy with <1hr RTO)
- Team confidence (well-documented playbooks)

**Audit Consequences:**

- SOC 2 Type II: Requires encryption, access controls, monitoring
- PCI-DSS: Encryption, access logging, firewall rules required
- ISO 27001: Shared responsibility model must be defined and understood

---

## Version & Authority

| Field           | Value                                      |
| --------------- | ------------------------------------------ |
| **Version**     | 2.0-COMPREHENSIVE                          |
| **Date Issued** | 2026-02-15                                 |
| **Change Type** | Major (placeholder → comprehensive)        |
| **Related MCM** | EATGF-CLD-ARCH-01 through EATGF-CLD-RES-01 |
| **Next Review** | 2026-08-15                                 |

**Classification:** Internal - Governance
**Authority:** EATGF Layer 08, Domain 05
**Distribution:** Cloud Architects, DevOps,Security, Finance
