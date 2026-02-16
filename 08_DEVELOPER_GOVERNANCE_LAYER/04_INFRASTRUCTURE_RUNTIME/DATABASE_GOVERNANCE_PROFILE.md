# Database Governance Profile

> **Authority Notice:** This profile implements EATGF controls for relational and non-relational database systems. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW databases satisfy Infrastructure Runtime (Layer 04), Data Protection, and Multi-Tenancy Isolation requirements.

## Purpose

Defines mandatory governance controls for relational and non-relational databases supporting web applications, SaaS systems, and multi-tenant platforms to ensure confidentiality, integrity, availability, and regulatory compliance.

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME (Primary) + Layer 05 (Domain Frameworks - Data Governance)
- **Governance Scope:** Data Storage, Access Control, Encryption, Multi-Tenancy Isolation
- **Control Authority:** Implements controls from MASTER_CONTROL_MATRIX for data protection and access control

**Applies to:**

- PostgreSQL
- MySQL
- MongoDB
- Managed DB services (RDS, Cloud SQL, Azure SQL)

---

## Governance Principles

### 1. Least Privilege Access

- Application service accounts must have only required CRUD permissions
- No shared superuser accounts

### 2. Encryption by Default

- Encryption in transit (TLS 1.2+) mandatory
- Encryption at rest mandatory for production systems

### 3. Multi-Tenant Isolation

- Tenant isolation must be enforced at schema, row, or database level

### 4. Data Integrity Protection

- Constraints, foreign keys, and transaction enforcement required

### 5. Auditability

- Database access and privilege escalation must be logged centrally

---

## Technical Implementation

### Encrypted Connection (PostgreSQL Example)

```python
import psycopg2
import os

conn = psycopg2.connect(
    dbname="billing",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host="db.internal",
    sslmode="require"  # Enforce TLS
)
```

### Role-Based Access Control

```sql
-- Create application role
CREATE ROLE billing_app LOGIN PASSWORD 'secure_password';

-- Grant only required permissions
GRANT SELECT, INSERT, UPDATE ON TABLE invoices TO billing_app;

-- Revoke dangerous privileges
REVOKE ALL ON SCHEMA public FROM billing_app;
```

**Key Principle:** No usage of superuser accounts by application runtime.

### Row-Level Security (Multi-Tenant)

```sql
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy
ON invoices
FOR ALL
USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

**Key Principle:** Tenant ID must be injected at connection/session level.

### Backup & Recovery Policy

```bash
# Logical backup example
pg_dump -U backup_user -F c billing > billing_backup.dump
```

**Mandatory:**

- Daily automated backups
- Offsite replication
- Restore testing quarterly

### Secrets Isolation

Database credentials must not exist in code or Git.

**Use:**

- Vault dynamic secrets
- AWS Secrets Manager
- Azure Key Vault

Example (Vault dynamic DB credentials):

```bash
vault read database/creds/billing-role
```

### Monitoring & Logging

Enable:

- Failed login logging
- Privilege escalation logging
- DDL statement logging
- Slow query monitoring

PostgreSQL example:

```
log_connections = on
log_disconnections = on
log_statement = 'ddl'
log_min_duration_statement = 500
```

### High Availability Configuration

- Replication (primary-replica)
- Automatic failover
- Read replicas for heavy queries
- Connection pooling (PgBouncer)

---

## Severity Model

| Control               | Severity    |
| --------------------- | ----------- |
| No TLS encryption     | MANDATORY   |
| Superuser app account | MANDATORY   |
| No tenant isolation   | MANDATORY   |
| No backups            | MANDATORY   |
| No encryption at rest | MANDATORY   |
| No query logging      | RECOMMENDED |
| No connection pooling | RECOMMENDED |

---

## Maturity Model

| Level | Database Governance State       |
| ----- | ------------------------------- |
| 1     | Single DB, manual backups       |
| 2     | Role-based access               |
| 3     | Row-level security              |
| 4     | Encrypted, monitored, HA        |
| 5     | Automated compliance validation |

---

## Control Mapping

| Control              | ISO 27001:2022 | NIST SSDF | OWASP   | NIST 800-53 | COBIT |
| -------------------- | -------------- | --------- | ------- | ----------- | ----- |
| Access control       | A.8.2          | PW.4      | ASVS V4 | AC-6        | APO13 |
| Encryption           | A.8.24         | PS.1      | ASVS V9 | SC-13       | DSS05 |
| Backup & recovery    | A.8.13         | RV.1      | -       | CP-9        | DSS04 |
| Logging & monitoring | A.8.15         | RV.1      | -       | AU-2        | MEA01 |
| Data integrity       | A.8.9          | PW.8      | ASVS V1 | CM-6        | DSS05 |

---

## Developer Checklist

- [ ] TLS enforced for DB connections
- [ ] No superuser runtime accounts
- [ ] Row-level or schema isolation implemented
- [ ] Daily automated backups configured
- [ ] Backup restore tested (monthly minimum)
- [ ] Secrets externalized (no hardcoded credentials)
- [ ] Audit logging enabled for all DML
- [ ] Resource limits defined (memory, storage)
- [ ] Encryption at rest enabled (production minimum)
- [ ] Connection pooling configured
- [ ] Replication/failover validated
- [ ] Read replicas for reporting queries
- [ ] Query performance monitoring active
- [ ] Compliance framework validated (ISO/SOC2/PCI)

---

## Governance Implications

### Risk if Ignored

- **Cross-tenant data leakage:** RLS not enforced
- **Privilege escalation:** Superuser runtime accounts
- **Data loss:** No backup/recovery procedures
- **Regulatory non-compliance:** PCI-DSS, HIPAA, SOC2 violations

### Audit Impact

- **ISO 27001 Annex A:** Access control & encryption failures
- **SOC2 Type II:** Data protection controls missing
- **PCI-DSS v4.0:** Database encryption & access control requirements
- **HIPAA 45 CFR §164.308:** Backup & recovery failure

### Operational Impact

- Service outage due to DDOS or resource exhaustion
- Irrecoverable data loss in disaster scenario
- Incident escalation due to forensic inability
- Extended RTO/RPO exceeding SLA

---

## Official References

- NIST SP 800-218: Secure Software Development Framework
- ISO/IEC 27001:2022 Annex A (Information Security Controls)
- NIST SP 800-53 Rev.5 (Security & Privacy Controls)
- CIS Database Benchmarks (PostgreSQL, MySQL, MongoDB)
- OWASP ASVS v4.0.3 (Application Security Verification)
- PCI-DSS v4.0 (Payment Card Industry Data Security)

---

## Version Information

- **Version:** 1.0 (Enterprise Release)
- **Change Type:** Major
- **Date:** 2026-02-15
- **Status:** CLOSED - Infrastructure Runtime Governance Complete
- **Target Audience:** Database architects, backend engineers, platform teams
- **Support Versions:** PostgreSQL 13+, MySQL 8.0+, MongoDB 5.0+, AWS RDS/GCP Cloud SQL/Azure SQL

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)

**Last Updated:** February 15, 2026

**Next Review:** August 15, 2026 (6-month cycle)

---

## Formal Closure Statement

**Database Governance Layer is now CLOSED.**

Backend Infrastructure Layer completion status:

-  Docker Governance Profile (complete)
-  Kubernetes Governance Profile (complete)
-  Database Governance Profile (complete)
-  Terraform Governance Profile (complete)
-  Cloud Runtime Governance Profile (complete)

**Infrastructure Runtime Governance is now FORMALLY CLOSED.**

All five (5) infrastructure runtime governance profiles have been deployed, reviewed, and published in compliance with EATGF_DOCUMENT_SIGNATURE_TEMPLATE and .github/copilot-instructions.md standards.

**Status: READY FOR PRODUCTION DEPLOYMENT**
