# Data Residency and Compliance Standard

| Property | Value |
|----------|-------|
| **Document Type** | Implementation Standard |
| **Version** | 1.0 |
| **Classification** | Governance |
| **Effective Date** | February 16, 2026 |
| **Authority** | Chief Legal Officer / Data Protection Officer |
| **EATGF Layer** | 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE |
| **MCM Reference** | [Control #28: Data Location & Sovereignty](../../02_CONTROL_ARCHITECTURE/MASTER_CONTROL_MATRIX.md) |

---

## Purpose

Data residency laws require personal data to remain within specific geographic boundaries (EU, California, China, India). This standard ensures:

- **Compliance with data residency regulations** (GDPR, CCPA, LGPD, data localization laws)
- **Enforcement of geographic constraints** for personal and sensitive data
- **Verification and auditing** of data location
- **Cross-border transfer controls** with legal authority
- **Incident response** when data inadvertently crosses jurisdictions

**Mandatory:** All customer personal data and regulated data must comply with this standard or explicitly marked as exempt with legal approval.

---

## Architectural Position

**Upstream Dependencies:**
- Layer 02 Control Architecture [Control #28: Data Location & Sovereignty]
- Layer 04 DATA_GOVERNANCE_POLICY (data classification and handling)
- Layer 04 DATA_PRIVACY_AND_PROTECTION_POLICY (GDPR/CCPA requirements)

**Downstream Usage:**
- Layer 06 AUDIT_AND_ASSURANCE (data residency verification)
- Layer 08.04 INFRASTRUCTURE_RUNTIME (physical server location)
- Layer 08.05 MULTI_TENANCY_GOVERNANCE_STANDARD (per-customer residency)

**Cross-Layer References:**
- INFRASTRUCTURE_AS_CODE_GOVERNANCE.md (region constraints in Terraform)
- SECURITY_MANAGEMENT_STANDARD.md (encryption at rest in-region)

---

## Governance Principles

1. **Data Sovereignty:** Personal data location determined by customer jurisdiction, not convenience
2. **Legal Authority:** Data residency policy set by Legal/DPO, not engineering optimization
3. **Explicit Consent:** Cross-border transfer requires explicit customer consent + legal review
4. **Continuous Verification:** Automated checks ensure data doesn't migrate across boundaries
5. **Incident Transparency:** Any cross-border data movement immediately escalated; customer notification required

---

## Technical Implementation

### 1. Data Residency Classification

**Customer Data Classification by Jurisdiction:**

```yaml
# Company policies by region

EU Customers (GDPR):
  data_residency: "EU-only"  # EU-27 + UK + Iceland + Liechtenstein + Norway
  processing:
    - Storage: Ireland (AWS eu-west-1) ✓
    - Backups: Germany (AWS eu-central-1) ✓
    - Disaster recovery: France (if agreed by customer) ✓
  prohibited_regions:
    - USA (AWS us-east-1): Schrems II ruling forbids
    - China (AWS cn-*): Not permitted
    - Australia: No legal basis for transfer
  legal_basis: "Standard Contractual Clauses (SCCs) + controller consent"

California Customers (CCPA):
  data_residency: "USA recommended; other NA acceptable"
  processing:
    - Primary storage: California (AWS us-west-1) ✓
    - Backups: Oregon or N. Virginia acceptable if encrypted in-transit TLS ✓
    - Disaster recovery: Canada (AWS ca-central-1) ✓ with SCC
  prohibited_regions:
    - EU: May be permitted with specific consent
    - China: Prohibited
  legal_basis: "CCPA OptOut mechanism; explicit SCC if cross-border"

China Customers (CAC / PIPL):
  data_residency: "China-only (mandatory)"
  processing:
    - Storage: China AWS/Alibaba CN region only
    - All processing in-country; cannot outsource
    - Chinese government data sovereignty laws apply
  prohibited_regions:
    - Outside China: Chinese law forbids
  legal_basis: "CAC law (2016) + PIPL (2021) data localization requirements"

Brazil Customers (LGPD):
  data_residency: "Brazil recommended; South America + US acceptable"
  processing:
    - Primary storage: São Paulo (AWS sa-east-1) ✓
    - Backup: Rio acceptable if within Brazil ✓
    - Disaster recovery: US permitted if customer consents ✓
  prohibited_regions:
    - EU: Requires specific SCC
    - China: Prohibited
  legal_basis: "LGPD Article 33 (optional data localization); SCC for cross-border"

Default (No Jurisdiction Specified):
  data_residency: "Primary region only (no replication)"
  processing:
    - Determined by cloud architecture (e.g., AWS us-east-1 only)
    - No automatic backups across regions unless explicitly approved
  legal_basis: "Terms of Service default jurisdiction"
```

### 2. Infrastructure & Cloud Region Mapping

**AWS Region Selection by Residency Requirement:**

```
╔════════════════════════════════════════════════════════════════╗
║ EU Data (GDPR)                                                 ║
╠════════════════════════════════════════════════════════════════╣
║ Primary:  eu-west-1 (Ireland, Amazon EC2) ✓                   ║
║ Backup:   eu-central-1 (Frankfurt) ✓                          ║
║ DR:       eu-south-1 (Milan) ✓ if customer specifically agrees║
║ Forbidden: us-east-1, ap-*                                     ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ US Data (CCPA, Default)                                        ║
╠════════════════════════════════════════════════════════════════╣
║ Primary:  us-west-1 (California) ✓                            ║
║ Backup:   us-west-2 (Oregon) ✓                                ║
║ DR:       ca-central-1 (Canada) ✓ with SCC                    ║
║ Allowed:  us-east-1 (N. Virginia) ✓                           ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ China Data (PIPL)                                              ║
╠════════════════════════════════════════════════════════════════╣
║ Primary:  cn-northwest-1 (Beijing) ✓                          ║
║ Backup:   cn-north-1 (Zhangjiakou) ✓                          ║
║ DR:       In-country emergency only                            ║
║ Forbidden: Any cross-border transfer                           ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ Brazil Data (LGPD)                                             ║
╠════════════════════════════════════════════════════════════════╣
║ Primary:  sa-east-1 (São Paulo) ✓                             ║
║ Backup:   sa-east-1 in separate AZ (Rio) ✓                    ║
║ DR:       us-east-1 (N. Virginia) ✓ if customer consents      ║
╚════════════════════════════════════════════════════════════════╝
```

**Terraform Enforcement:**

```hcl
# Terraform code enforcing residency constraints

locals {
  residency_requirements = {
    "customer-eu-example" = {
      allowed_regions = ["eu-west-1", "eu-central-1"]
      denied_regions  = ["us-east-1", "ap-northeast-1"]
      legal_basis     = "GDPR Standard Contractual Clauses"
    }
    "customer-us-default" = {
      allowed_regions = ["us-west-1", "us-west-2", "ca-central-1"]
      denied_regions  = ["eu-west-1", "cn-*"]
      legal_basis     = "CCPA Terms of Service"
    }
    "customer-china" = {
      allowed_regions = ["cn-north-1", "cn-northwest-1"]
      denied_regions  = ["*"]  # No cross-border permitted
      legal_basis     = "PIPL data localization (mandatory)"
    }
  }
}

# Database must be in allowed region
resource "aws_db_instance" "customer_data" {
  customer_id     = var.customer_id
  engine          = "postgres"
  allocated_storage = 100
  
  # Enforce residency constraint
  availability_zone = var.allowed_az  # e.g., eu-west-1a

  # Validation (will error if wrong region selected)
  lifecycle {
    precondition {
      condition = contains(
        local.residency_requirements[var.customer_id].allowed_regions,
        var.aws_region
      )
      error_message = "Customer ${var.customer_id} data must reside in ${
        join(", ", local.residency_requirements[var.customer_id].allowed_regions)
      }. Requested region: ${var.aws_region}"
    }
  }

  # Encryption must be in-region (not cross-region key)
  kms_key_id = var.in_region_kms_key_arn
  
  # Backups retained in-country only
  backup_retention_period = 30
  # Cross-region backups DISABLED by default
  copy_backups_to_region = ""  # Empty = no cross-region copy
  
  tags = {
    Residency = var.customer_residency_zone
    Customer  = var.customer_id
    Compliance = var.legal_basis
  }
}

# RDS backup policy: MUST be in-region
resource "aws_db_instance_automated_backup" "customer_data" {
  db_instance_id      = aws_db_instance.customer_data.id
  backup_retention_period = 30
  copy_backups_to_region  = ""  # No cross-region copy for EU data
}
```

### 3. Data Transfer Controls & SCCs

**Standard Contractual Clauses (SCCs) for Cross-Border Transfers:**

When data transfer justified (backups, DR, processing), SCC required:

```
Data Transfer Authority Request Form (DPA-001)

Customer: Acme EU Corp
Source Region: Ireland (eu-west-1) [GDPR OK]
Destination Region: N. Virginia (us-east-1) [GDPR VIOLATION without SCC]
Purpose: Disaster recovery failover
Legal Basis: GDPR Article 49 (necessity) + SCC Module 2

Required Approvals:
✓ Customer Data Protection Officer consent
✓ Company Legal approved SCC
✓ GDPR Impact Assessment (30 min analysis, below)
✗ EU Supervisory Authority notification (only if systematic transfer)

GDPR Impact Assessment (Article 35):
1. Necessity: ✓ DR failover is essential for service continuity
2. Frequency: ✓ Only on disaster (not routine)
3. Safeguards: ✓ TLS encryption in-transit + key material separate
4. Recipient Safeguards: ✓ US cloud provider subject to SCC + supervisory orders
5. Flow: ✓ One-way encrypted backup; automatic return after DR

Conclusion: Proportionate risk; approve transfer with conditions below

Conditions:
- Data encrypted with customer's master key (company cannot decrypt)
- Transfer only on confirmed disaster; customer triggers
- Automatic deletion 30 days post-disaster
- No re-processing in US; only storage awaiting replication back to Ireland
- Annual audit of cross-border transfers
```

### 4. Data Residency Verification

**Automated Daily Checks:**

```python
# Daily verification that EU data doesn't leave EU regions

import boto3
import alerts

def verify_eu_data_residency():
    """Verify all EU customer data remains in EU-only AWS regions"""
    
    # EU-allowed regions
    allowed_regions = ['eu-west-1', 'eu-central-1']
    forbidden_regions = ['us-east-1', 'us-west-1', 'ap-northeast-1']
    
    # Query all EU customers
    eu_customers = rds.query_customers(
        where="residency_zone = 'EU' AND status = 'active'"
    )
    
    violations = []
    
    for customer in eu_customers:
        # Check RDS database location
        db_region = customer.database.region
        if db_region not in allowed_regions:
            violations.append({
                'customer': customer.id,
                'violation': 'DATABASE_IN_FORBIDDEN_REGION',
                'current_region': db_region,
                'allowed_regions': allowed_regions,
                'severity': 'CRITICAL'
            })
        
        # Check S3 bucket region
        s3_region = customer.s3_bucket.region
        if s3_region not in allowed_regions:
            violations.append({
                'customer': customer.id,
                'violation': 'S3_IN_FORBIDDEN_REGION',
                'current_region': s3_region,
                'severity': 'CRITICAL'
            })
        
        # Check backup locations
        for backup in customer.database.backups:
            backup_region = backup.region
            if backup_region not in allowed_regions and backup_region != "pending_restore":
                violations.append({
                    'customer': customer.id,
                    'violation': 'BACKUP_IN_FORBIDDEN_REGION',
                    'current_region': backup_region,
                    'backup_id': backup.id,
                    'severity': 'CRITICAL'
                })
    
    # Report violations
    if violations:
        for v in violations:
            alerts.CRITICAL(f"""
                DATA RESIDENCY VIOLATION: {v['customer']}
                Type: {v['violation']}
                Current Region: {v['current_region']}
                Allowed: {', '.join(v['allowed_regions'])}
                
                Action: IMMEDIATE DATA RETURN to {v['allowed_regions'][0]}
                Escalation: DPO + Legal + Engineering
                Deadline: 4 hours
            """)
        
        # Pause all write operations to flagged customer data (safety)
        for v in violations:
            customer_id = v['customer']
            disable_write_access(customer_id)
            notify_customer(customer_id, v)
    
    return len(violations)  # 0 = success, >0 = violations
```

### 5. Disaster Recovery & Cross-Border Failover

**Tiered DR Strategy:**

```
┌────────────────────────────────────────────────────────────────┐
│ TIER 1: In-Country DR (PREFERRED)                              │
├────────────────────────────────────────────────────────────────┤
│ EU Customer: Backup in same EU region, different AZ            │
│ RTO: 4 hours   RPO: 1 hour                                     │
│ Legal: GDPR fully compliant; no SCC needed                     │
│ Example: DB in eu-west-1a fails → restore from eu-west-1c     │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│ TIER 2: Regional DR (REQUIRES CUSTOMER CONSENT + SCC)           │
├────────────────────────────────────────────────────────────────┤
│ EU Customer disaster: Fail over to different EU country        │
│ RTO: 8 hours   RPO: 2 hours                                    │
│ Legal: Requires SCC + customer explicit approval               │
│ Example: eu-west-1 down → restore to eu-central-1 (Germany)   │
│ Process: Automatic failover if customer pre-approved           │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│ TIER 3: Cross-Border DR (EMERGENCY ONLY)                        │
├────────────────────────────────────────────────────────────────┤
│ Entire EU region destroyed: Manual failover to US              │
│ RTO: 24 hours   RPO: 24 hours                                  │
│ Legal: Requires court order or explicit emergency consent      │
│ Activation: DPO approves; customer notified 4 hours before     │
│ Duration: Max 72 hours; then return to EU mandatory            │
└────────────────────────────────────────────────────────────────┘
```

**Failover Process for EU Customer Emergency (Tier 3):**

1. **Disaster Detection** (Automated): Entire eu-west-1 region unavailable >1h
2. **DPO Escalation** (Automated): Notify DPO + Customer of pending TIER 3 activation
3. **Delay Period** (4 hours): Allow time to restore in-country resources
4. **Failover Decision** (Manual): DPO approves cross-border if TIER 1/2 restoration impossible
5. **Encrypted Data Transfer** (In-Transit): Customer data encrypted with customer's key; company cannot access
6. **Notification** (Customer): Inform of temporary US residency; explain legal authority (Necessity)
7. **Duration Clock** (72h max): Automatic return to EU once in-country infrastructure restored
8. **Post-Incident Review** (Legal): Determine if SCC required retroactively; assess supervisory notification

---

## Control Mapping

| EATGF Control | ISO 27001:2022 | NIST SSDF | COBIT 2019 | OWASP |
|---|---|---|---|---|
| Data Location & Sovereignty | A.8.8, A.8.9, A.8.30 | N/A | BAI06.01, DSS04.08 | Not Directly |
| Cross-Border Transfer | A.8.8 (GDPR Article 46) | N/A | BAI06.01 | Not Directly |
| Compliance Verification | A.8.17, A.6.7 | N/A | MEA03.01 | Not Directly |
| Incident Notification | A.5.31, A.7.4 | N/A | APO12.06 | Not Directly |

---

## Developer Checklist

- [ ] Understand customer residency requirement (GDPR/CCPA/LGPD/PIPL/other)
- [ ] Infrastructure deployed to correct AWS region for customer jurisdiction
- [ ] Infrastructure as Code includes residency constraint validation (Terraform preconditions)
- [ ] Database backups configured to stay in-country (no cross-region copy)
- [ ] Encryption keys located in-region (KMS key in same AWS region as data)
- [ ] Disaster recovery tested with in-country failover (TIER 1/2)
- [ ] Standard Contractual Clauses reviewed by Legal for any cross-border processing
- [ ] Daily residency verification script running and reporting to alerts
- [ ] Documentation of residency zone and legal basis present in infrastructure code
- [ ] Customer notified of residency commitments in data processing agreement
- [ ] Team trained on data residency requirements and violation procedures
- [ ] Audit evidence prepared (region screenshots, backup configurations, legal agreements)

---

## Governance Implications

**Risk if not implemented:**
- GDPR fines: €10-15 million or 4% annual revenue for violations
- CCPA penalties: $2,500-$7,500 per violation; class action status
- LGPD fines: Up to 2% annual revenue (~$10 million for large companies)
- Regulatory shutdown of data processing; customer churn

**Operational impact:**
- Engineering must know customer residency before deploying infrastructure
- Disaster recovery procedures require pre-approval for cross-border failover
- Legal team involved in any exception requests
- Monitoring overhead (daily residency verification checks)

**Audit consequences:**
- External auditors verify infrastructure location matches customer agreement
- GDPR audits require demonstration of SCC compliance
- Multi-jurisdiction evidence collection (one per regulatory body)
- Potential regulatory investigation if violations discovered

**Cross-team dependencies:**
- **Legal/DPO:** Reviews SCC; approves cross-border transfers; handles regulatory inquiries
- **Engineering:** Implements region constraints; verifies residency daily
- **Finance:** Tracks per-region cost (EU data more expensive due to premium regions)
- **Customer Success:** Communicates residency commitments to prospects

---

## Official References

- **GDPR Article 44-50:** International Data Transfers
- **NIST SP 800-188:** Guidelines for Managing the Security of Mobile Devices in the Enterprise
- **ISO 27001:2022 Annex A.8.8:** Handling of Assets
- **AWS Standards & Compliance:** https://aws.amazon.com/compliance/ (regional certification)
- **Standard Contractual Clauses:** https://ec.europa.eu/info/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses_en (official EU templates)
- **Schrems II Decision (2020):** European Court judgment on US adequacy (landmark GDPR ruling)

---

## Version History

| Version | Date | Change Type | Notes |
|---------|------|-------------|-------|
| 1.0 | Feb 16, 2026 | Major | Initial release; GDPR/CCPA/LGPD/PIPL residency requirements, SCC procedures, daily verification, emergency DR |

---

*Last Updated: February 16, 2026*  
*EATGF v1.0-Foundation: Data Residency and Compliance Standard*
