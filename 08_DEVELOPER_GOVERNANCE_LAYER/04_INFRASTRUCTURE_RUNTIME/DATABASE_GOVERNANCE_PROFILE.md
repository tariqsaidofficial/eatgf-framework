# Database Governance Profile

## Enterprise Data Persistence Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Infrastructure Runtime - Data Layer)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → 04_INFRASTRUCTURE_RUNTIME → DATA_LAYER

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** data governance controls from [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **extends** BACKEND framework profiles (Django ORM, FastAPI Pydantic, Node.js TypeORM, Spring Data JPA)
- This profile **enforces** multi-tenancy isolation at database layer
- This profile **coordinates** with KUBERNETES_GOVERNANCE_PROFILE.md (credentials injection)
- This profile **does not** manage backup infrastructure (see cloud provider policies)

**COMPLIANCE STATEMENT:** Database represents the **DATA_LAYER** where application data persists. Non-conformance results in:

- Cross-tenant data leaks (no row-level security)
- SQL injection (unvalidated input at ORM layer)
- Unauthorized data access (weak connection authentication)
- Privilege escalation (unused database accounts with high privileges)
- Audit trail loss (no statement logging)

Every database instance must enforce this profile.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for databases (relational: PostgreSQL, MySQL; non-relational: MongoDB, Redis) supporting backend applications under EATGF.

**Scope:** Database connection management, authentication, authorization, multi-tenancy isolation, input validation, encryption, audit logging, backup procedures

**Non-Scope:** Database provisioning infrastructure (see Terraform profile), Cloud storage (see Cloud Runtime profile), Data warehouse/analytics (different governance model)

**Supported Engines:** PostgreSQL 14+, MySQL 8.0+, MongoDB 6.0+, Redis 7.0+

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES (Application Layer)
│   ├── BACKEND (Django, FastAPI, Node.js, Spring Boot)
│   └── FRONTEND (8 frameworks)
└── 04_INFRASTRUCTURE_RUNTIME (Container + Orchestration)
    ├── DOCKER_GOVERNANCE (Container Layer)
    ├── KUBERNETES_GOVERNANCE (Orchestration Layer)
    ├── DATABASE_GOVERNANCE (Data Layer) ← THIS PROFILE
    ├── TERRAFORM_GOVERNANCE (Infrastructure as Code)
    └── CLOUD_RUNTIME_GOVERNANCE (Cloud Controls)
```

**Database operates as:**

- Persistent storage for application state
- Multi-tenant data isolation enforcer
- Query audit trail recorder
- Credential validator (connection pooling)
- Encryption boundary (at-rest and in-transit)

**Critical Principle:** Data isolation by default. Queries scoped to tenant, no cross-tenant access possible.

---

## 3. Governance Principles

### Principle 1: Connection Authentication & Pooling (MANDATORY)

Database connections authenticated, pooled for efficiency, non-root accounts only.

```python
# ❌ PROHIBITED: Direct connection, root credentials
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",    # Root account (prohibited)
    password="postgres",
    database="app_db"
)

# ✅ COMPLIANT: Connection pooling with service account
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Service account with minimal permissions
DATABASE_URL = "postgresql://app_user:$(DB_PASSWORD)@pg-host:5432/app_db"

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,           # Max connections in pool
    max_overflow=5,         # Max overflow connections
    pool_timeout=30,        # Timeout if no connection available
    pool_pre_ping=True,     # Verify connection before use
    pool_recycle=3600,      # Recycle connections hourly
    echo=False              # Disable query logging to stdout
)
```

---

### Principle 2: Row-Level Security (Multi-Tenancy) (MANDATORY)

All queries implicitly filtered by tenant ID. No cross-tenant exposure.

```sql
-- ✅ COMPLIANT: RLS policy PostgreSQL
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid);

CREATE POLICY tenant_isolation_insert ON invoices
  FOR INSERT
  WITH CHECK (tenant_id = current_setting('app.tenant_id')::uuid);

-- Application sets tenant context before queries
SET app.tenant_id = 'tenant-abc-123';

-- Query automatically filtered
SELECT * FROM invoices;  -- Only invoices where tenant_id = tenant-abc-123

-- ❌ PROHIBITED: Application-layer filtering only
SELECT * FROM invoices WHERE tenant_id = :tenant_id;
-- If developer forgets WHERE clause, all invoices exposed (race condition risk)
```

---

### Principle 3: Minimal Privilege Database Accounts (MANDATORY)

Separate accounts for app (read/write), app-readonly, migrations (DDL).

```sql
-- ✅ COMPLIANT: Role hierarchy
CREATE ROLE app_group;
CREATE ROLE app_user LOGIN;
CREATE ROLE app_readonly LOGIN;
CREATE ROLE app_migrations LOGIN;

-- App user: INSERT, UPDATE, SELECT, DELETE
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- Read-only user: SELECT only
GRANT USAGE ON SCHEMA public TO app_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_readonly;

-- Migrations: DDL (schema changes)
GRANT ALL PRIVILEGES ON SCHEMA public TO app_migrations;
GRANT ALL PRIVILEGES ON DATABASE app_db TO app_migrations;

-- ❌ PROHIBITED: Single superuser account
GRANT ALL PRIVILEGES ON DATABASE app_db TO postgres;
-- Used by application (violates least privilege)
```

---

### Principle 4: Encrypted Connections (MANDATORY)

All connections encrypted in-transit (TLS 1.2+), secrets never in plaintext logs.

```python
# ✅ COMPLIANT: SSL/TLS connection
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@pg-host:5432/db?sslmode=require"
# sslmode=require: Connection fails if TLS unavailable

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require",
        "sslcert": "/path/to/client-cert.pem",
        "sslkey": "/path/to/client-key.pem",
        "sslrootcert": "/path/to/ca-cert.pem"
    }
)

# ❌ PROHIBITED: Plaintext connection
DATABASE_URL = "postgresql://user:password@pg-host:5432/db"
# Password exposed in network traffic

# ❌ PROHIBITED: Credentials in logs
logger.info(f"Connecting to {DATABASE_URL}")  # Logs credentials
```

---

### Principle 5: Input Validation & Query Safety (MANDATORY)

All user input validated before database query, prepared statements mandatory.

```python
# ✅ COMPLIANT: Prepared statement (ORM automatic)
from sqlalchemy import select, text

# ORM automatically parameterizes
from app.models import User
user = session.query(User).filter(User.email == user_input).first()

# ✅ COMPLIANT: Explicit parameterization
connection.execute(
    text("SELECT * FROM invoices WHERE invoice_id = :id"),
    {"id": int(user_input)}  # Parameterized, validated
)

# ❌ PROHIBITED: String concatenation (SQL injection)
query = f"SELECT * FROM invoices WHERE invoice_id = {user_input}"
# user_input = "1 OR 1=1" → query returns all invoices
connection.execute(query)

# ❌ PROHIBITED: format() without parameterization
query = "SELECT * FROM invoices WHERE invoice_id = {}".format(user_input)
connection.execute(query)
```

---

### Principle 6: Query Audit & Logging (MANDATORY)

All data modification (INSERT, UPDATE, DELETE) logged with actor, timestamp, before/after values.

```sql
-- ✅ COMPLIANT: Audit table & trigger
CREATE TABLE audit_log (
    id BIGSERIAL PRIMARY KEY,
    table_name TEXT,
    action TEXT,  -- INSERT, UPDATE, DELETE
    record_id UUID,
    actor_id UUID,
    old_values JSONB,
    new_values JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (table_name, action, record_id, actor_id, old_values, new_values)
    VALUES (
        TG_TABLE_NAME,
        TG_OP,
        COALESCE(NEW.id, OLD.id),
        current_setting('app.user_id')::uuid,
        row_to_json(OLD),
        row_to_json(NEW)
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER audit_invoices
AFTER INSERT OR UPDATE OR DELETE ON invoices
FOR EACH ROW EXECUTE FUNCTION audit_trigger();

-- ❌ PROHIBITED: No audit logging
UPDATE invoices SET amount = 9999 WHERE id = 'abc-123';
-- Modification invisible, cannot trace who changed amount
```

---

### Principle 7: Backup & Restore Procedures (MANDATORY)

Regular backups with encryption, restore procedures tested annually.

```bash
# ✅ COMPLIANT: Encrypted backup with WAL archiving
pg_basebackup -h pg-host -D /backup/base -F tar -z \
  -U app_backup_user --wal-method=fetch \
  2>/backup/backup.log

# Verify backup integrity
pg_verify_backup /backup/base

# ✅ COMPLIANT: Point-in-time recovery (PITR)
# WAL archived, can restore to any point in time
SELECT pg_start_backup('backup_label', false);
# ... backup takes full filesystem snapshot
SELECT pg_stop_backup();

# ✅ COMPLIANT: Encrypted backup storage
# Backup encrypted with database certificate
tar -czf backup.tar.gz --exclude-caches /backup/base
gpg --encrypt --default-key backup@example.com backup.tar.gz

# ❌ PROHIBITED: Unencrypted backups
tar -czf backup.tar.gz /backup/base
# Backup exposed if storage compromised
```

---

### Principle 8: Disaster Recovery & Failover (MANDATORY)

Replication enabled, failover procedures documented and tested.

```yaml
# ✅ COMPLIANT: PostgreSQL replication
# Primary (pg-primary)
wal_level = replica
max_wal_senders = 10
wal_keep_size = 1GB

# Replica (pg-replica)
standby_mode = on
primary_conninfo = 'host=pg-primary port=5432 user=replication_user'
restore_command = 'cp /archive/%f "%p"'

# ✅ COMPLIANT: Health check & automatic failover
# Monitoring detects primary failure
# Replica promoted to primary
promotion_command = 'touch /tmp/promote'

# ❌ PROHIBITED: No replication
# Single database instance, no failover possible
```

---

## 4. Control 1: Authentication (Database Connection)

**Objective:** Verify database connection credentials, audit connection attempts.

### Requirement

- Connection authenticated with non-root account
- Failed connection attempts logged
- Connection timeout enforced

### Compliant Implementation

```bash
# ✅ COMPLIANT: Connection validation
psql -h pg-host -U app_user -d app_db \
  -c "SELECT 1"  # Test connection

# ✅ COMPLIANT: Authentication failure logging
tail -f /var/log/postgresql/*.log | grep "authentication failed"
# 2026-02-15 10:30:00 app_user [140293]: authentication failed for user "app_user"

# ❌ PROHIBITED: Root account connection
psql -h pg-host -U postgres -d app_db
# Root privileges in application
```

---

## 5. Control 2: Authorization (Database Permissions)

**Objective:** Role-based database access, minimal table/column permissions.

### Requirement

- App account cannot grant permissions (non-admin)
- Column-level masking for sensitive data
- No SELECT on system tables

### Compliant Implementation

```sql
-- ✅ COMPLIANT: Column masking
CREATE ROLE masked_account;

CREATE POLICY column_masking ON users
  USING (tenant_id = current_setting('app.tenant_id')::uuid)
  WITH (email CASE WHEN current_user_id = id THEN email ELSE '*' END);

-- ✅ COMPLIANT: Minimal permissions
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE ON TABLE users TO app_user;
GRANT UPDATE (first_name, last_name) ON TABLE users TO app_user;
-- app_user can UPDATE name, but not password or admin flag

-- ❌ PROHIBITED: All permissions to app user
GRANT ALL ON DATABASE app_db TO app_user;
```

---

## 6. Control 3: Versioning (Schema Migrations)

**Objective:** Track schema changes, enable rollback.

### Requirement

- Migration framework (Alembic, Flyway) mandatory
- All DDL changes versioned
- Rollback procedures tested

### Compliant Implementation

```bash
# ✅ COMPLIANT: Schema versioning with Alembic
alembic init migrations

# Migration created
alembic revision -m "add_users_table"
# Generated: alembic/versions/001_add_users_table.py

# Apply migration
alembic upgrade head

# ✅ Version tracking
SELECT * FROM alembic_version;
# version_num: 001_add_users_table

# ❌ PROHIBITED: Ad-hoc DDL
psql -h pg-host -U postgres -d app_db -c "CREATE TABLE users (...);"
# No versioning, no rollback path
```

---

## 7. Control 4: Input Validation (Query Parameters)

**Objective:** Validate all query inputs, prevent injection attacks.

### Requirement

- All user input parameterized
- String input length limits enforced
- Type validation (integer, date, UUID, etc.)

### Compliant Implementation

```python
# ✅ COMPLIANT: Pydantic + ORM parameterization
from pydantic import BaseModel, constr
from sqlalchemy import select
from app.models import User

class UserQuery(BaseModel):
    email: constr(max_length=255, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

query_input = UserQuery(email=user_email)
# Pydantic validates type, length, format

user = session.query(User).filter(User.email == query_input.email).first()
# SQLAlchemy parameterizes query

# ❌ PROHIBITED: Raw string input
user = session.query(User).filter(User.email == user_email).first()
# If user_email = "abc' OR '1'='1", SQL injection occurs
```

---

## 8. Control 5: Rate Limiting (Query Performance)

**Objective:** Limit resource-intensive queries, protect against DoS.

### Requirement

- Query timeout enforced
- Connection limits per tenant
- Long-running query cancellation

### Compliant Implementation

```sql
-- ✅ COMPLIANT: Query timeout
SET statement_timeout = 30000;  -- 30 second timeout

SELECT * FROM large_table WHERE complex_condition;
-- Query automatically canceled if exceeds 30s

-- ✅ COMPLIANT: Per-tenant connection limits
CREATE ROLE app_user_tenant_abc CONNECTION LIMIT 10;
-- Max 10 concurrent connections for tenant A

-- ✅ COMPLIANT: Slow query logging
log_min_duration_statement = 1000;  -- Log queries > 1 second
log_statement = 'ddl';  -- Log DDL (CREATE, ALTER, DROP)

-- ❌ PROHIBITED: No query timeout
SELECT * FROM massive_table WHERE 1=1;
-- Can consume all database resources (DoS)
```

---

## 9. Control 6: Testing & Data Integrity

**Objective:** Validate schema integrity, test backup/restore, referential integrity.

### Requirement

- Foreign key constraints enforced
- Data integrity tests in CI/CD
- Backup restoration tested quarterly

### Compliant Implementation

```sql
-- ✅ COMPLIANT: Referential integrity
ALTER TABLE invoices
ADD CONSTRAINT fk_tenant FOREIGN KEY (tenant_id)
  REFERENCES tenants(id) ON DELETE RESTRICT;
-- Cannot delete tenant with invoices (data integrity)

ALTER TABLE invoices
ADD CONSTRAINT fk_user FOREIGN KEY (user_id)
  REFERENCES users(id) ON DELETE CASCADE;
-- Delete user, invoices automatically deleted

-- ✅ COMPLIANT: Check constraints
ALTER TABLE invoices
ADD CONSTRAINT check_amount CHECK (amount > 0);
-- Prevents negative amounts at database layer

-- ❌ PROHIBITED: No foreign keys (application-layer enforcement)
-- Application responsible for referential integrity
-- Risk: Application bug → referential integrity violation
```

---

## 10. Control 7: Logging & Query Traceability

**Objective:** Log all DDL, DML, authentication, and performance events.

### Requirement

- Query statements logged (if approved by compliance)
- Actor ID tracked (user_id in session)
- Timestamp resolution to millisecond or better

### Compliant Implementation

```sql
-- ✅ COMPLIANT: Audit traceability
-- Client request includes actor
SET app.user_id = 'user-123-abc';
SET app.tenant_id = 'tenant-abc-123';

-- Trigger captures context
INSERT INTO audit_log (table_name, action, record_id, actor_id, created_at)
VALUES ('invoices', 'INSERT', NEW.id, current_setting('app.user_id'), NOW());

-- Query execution logging
log_statement = 'all';  # Log all SQL (if security approved)
log_duration = on;      # Log execution time
logging_collector = on; # Centralize logs

-- Sample log
2026-02-15 10:30:00.123 app_user LOG: execute <unnamed>
  PREPARE statement_1 AS SELECT * FROM invoices WHERE id = $1
  Duration: 0.500 ms

-- ❌ PROHIBITED: No audit trail
UPDATE users SET password = 'reset' WHERE id = 'user-123';
-- Who changed the password? When? No visibility.
```

---

## 11. Control 8: Zero Trust Data Access

**Objective:** No implicit cross-tenant access, all queries scoped by tenant.

### Requirement

- Row-level security enforced
- Cross-tenant queries rejected
- Default-deny tenant context validation

### Compliant Implementation

```python
# ✅ COMPLIANT: Tenant context on every query
from sqlalchemy.orm import Session
from app.models import Invoice

@app.get("/invoices")
def list_invoices(session: Session, current_user: User):
    # Tenant context set from user JWT
    session.execute(text("SET app.tenant_id = :tenant_id"),
                   {"tenant_id": current_user.tenant_id})

    # Query automatically filtered by RLS policy
    invoices = session.query(Invoice).all()
    # Returns only invoices where tenant_id = current_user.tenant_id
    return invoices

# ✅ COMPLIANT: Explicit tenant validation
def get_invoice(invoice_id: UUID, current_user: User, session: Session):
    invoice = session.query(Invoice).filter(
        Invoice.id == invoice_id,
        Invoice.tenant_id == current_user.tenant_id  # Explicit check
    ).first()

    if not invoice:
        raise 403 Forbidden  # Not found or not owner
    return invoice

# ❌ PROHIBITED: Tenant context missing
invoices = session.query(Invoice).filter(Invoice.id == invoice_id).first()
# RLS policy not applied, could return invoice from different tenant
```

---

## 12. Multi-Tenancy Controls

**Objective:** Complete data isolation per tenant, no cross-contamination.

### Requirement

- Separate schema per tenant OR row-level security
- Tenant context validated on connection
- Backup/restore preserves tenant boundaries

### Compliant Implementation

```sql
-- ✅ COMPLIANT: Schema-per-tenant
CREATE SCHEMA tenant_abc;
CREATE TABLE tenant_abc.invoices (id UUID, amount DECIMAL);

CREATE SCHEMA tenant_xyz;
CREATE TABLE tenant_xyz.invoices (id UUID, amount DECIMAL);

-- Application connects to tenant-specific schema
-- No cross-tenant access possible at query level

-- ✅ COMPLIANT: Row-level security (shared schema)
CREATE TABLE invoices (
    id UUID,
    tenant_id UUID,
    amount DECIMAL
);

ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

CREATE POLICY invoice_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid);

-- ✅ COMPLIANT: Tenant isolation validation
-- Every query executed with tenant context
SELECT * FROM invoices;
-- WHERE clause automatically applied: tenant_id = 'tenant-abc'

-- ❌ PROHIBITED: Shared table, no RLS
SELECT * FROM invoices;  -- Returns all tenants' invoices
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** Database version tracking, dependency patching, security updates.

### Requirement

- Database version pinned
- Security patches applied monthly
- Backup verification includes dependency check

### Compliant Implementation

```bash
# ✅ COMPLIANT: Pinned database version
docker run -e POSTGRES_VERSION=14.8 postgres:14.8

# ✅ COMPLIANT: Security update process
apt-get update && apt-get install postgresql-14=14.8-1.pgdg22.04+1 \
  && systemctl restart postgresql

# ✅ COMPLIANT: Dependency tracking
SELECT version();  # PostgreSQL 14.8 on x86_64-pc-linux-gnu
# Verifiable, upgradeable

# ❌ PROHIBITED: Floating version
pg_restore -d app_db backup.dump  # May restore with incompatible version
```

---

## 14. Control Mapping

| EATGF Control     | ISO 27001:2022 | NIST SSDF 1.1 | OWASP SAMM   | NIST 800-53 | COBIT 2019 |
| ----------------- | -------------- | ------------- | ------------ | ----------- | ---------- |
| Connection Auth   | A.8.2, A.8.5   | AS.1          | Governance.1 | AC-2        | DSS05.01   |
| Row-Level Access  | A.8.5, A.8.9   | AS.2          | Verify.1     | AC-3, AC-6  | DSS05.03   |
| Schema Versioning | A.8.28         | PO.3          | Build.1      | CM-3        | BAI09.02   |
| Query Validation  | A.8.22         | PW.8          | Build.2      | CM-5        | DSS05.04   |
| Query Performance | A.8.22         | PW.8          | Verify.1     | SC-5        | DSS01.05   |
| Integrity Testing | A.8.28         | PO.2          | Build.3      | SA-3        | BAI03.07   |
| Audit Logging     | A.8.15, A.8.23 | RV.1          | Verify.3     | AU-2        | MEA01.02   |
| Data Isolation    | A.8.1, A.8.9   | PW.1          | Verify.1     | SC-7        | DSS05.02   |

---

## 15. Developer Checklist

Before deploying database to production:

- [ ] Connection pool configured (min 5, max 20 connections)
- [ ] Connection timeout set (30-60 seconds)
- [ ] Database user created with least privilege (SELECT, INSERT, UPDATE, DELETE only)
- [ ] Root/superuser account separate from application account
- [ ] All connections use TLS/SSL (sslmode=require)
- [ ] Row-level security enabled for multi-tenant isolation
- [ ] Row-level security policies attached to all tables
- [ ] Audit trigger created to log all INSERTs, UPDATEs, DELETEs
- [ ] Foreign key constraints enforced (referential integrity)
- [ ] Check constraints defined (domain validation)
- [ ] Query timeout configured (statement_timeout)
- [ ] Long-running query logging enabled
- [ ] Backup encryption enabled
- [ ] Backup restoration procedure tested (quarterly minimum)
- [ ] Replication configured (primary + replica)
- [ ] Failover procedure documented and tested

---

## 16. Governance Implications

**Risk if not implemented:**

- **SQL Injection:** Unparameterized queries → data breach via malicious input
- **Cross-Tenant Leakage:** No RLS → tenant A views tenant B data
- **Privilege Escalation:** App uses superuser account → full database access compromised
- **Audit Trail Loss:** No logging → cannot trace who accessed sensitive data
- **Data Loss:** No backup/replication → complete data loss without recovery

**SOC2/ISO 27001 Impact:**

- **SOC2 CC6.1:** (Access Control) Database authentication enforces logical access
- **SOC2 CC6.2:** (Change Management) Audit trail satisfies compliance requirements
- **SOC2 CC7.1:** (Monitoring) Query logging tracks database access
- **ISO 27001 A.8.22:** (Input Validation) RLS + prepared statements prevent injection
- **ISO 27001 A.8.23:** (Audit) Query and connection logging satisfies audit requirements

**Operational Impact:**

- Data breach exposure if RLS not enabled
- Performance degradation from unoptimized queries (no timeout)
- Data loss if backup/replication unavailable

---

## 17. Implementation Risks

| Risk                   | Severity | Mitigation                                        |
| ---------------------- | -------- | ------------------------------------------------- |
| Cross-tenant data leak | CRITICAL | Enable RLS on all tables; audit quarterly         |
| SQL injection          | HIGH     | Parameterized queries; input validation in ORM    |
| Superuser account used | CRITICAL | Separate app account; test permissions            |
| No audit trail         | HIGH     | Trigger-based logging; audit logs encrypted       |
| Unencrypted backups    | HIGH     | Backup encryption with GPG; verify regularly      |
| No failover            | MEDIUM   | Replication + automated promotion; test quarterly |

---

## 18. Official References

**Normative (Governance):**

- NIST SP 800-218: Secure Software Development Framework (SSDF)
- ISO/IEC 27001:2022 Annex A: Control Objectives
- NIST SP 800-53 Rev. 5: Security & Privacy Controls

**Informative (Database Security):**

- PostgreSQL Security: https://www.postgresql.org/docs/current/sql-syntax.html
- MySQL Security: https://dev.mysql.com/doc/refman/8.0/en/security.html
- MongoDB Security: https://docs.mongodb.com/manual/security/
- OWASP Database Security: https://cheatsheetseries.owasp.org/
- CIS Database Benchmarks

**Tools & Standards:**

- SQLAlchemy ORM (Python)
- Alembic Migration Framework
- Flyway Database Versioning

---

## 19. Version Information

| Field                | Value                                                 |
| -------------------- | ----------------------------------------------------- |
| **Document Version** | 1.0                                                   |
| **Change Type**      | Major (Initial Release)                               |
| **Issue Date**       | February 15, 2026                                     |
| **EATGF Baseline**   | v1.0 (Layer 08 Infrastructure Runtime)                |
| **Database Engines** | PostgreSQL 14+, MySQL 8.0+, MongoDB 6.0+, Redis 7.0+  |
| **Target Audience**  | Database administrators, backend engineers, DevSecOps |

**Compliance Statement:** This profile is 100% conformant to EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md and enforces all governance principles at Layer 08, Infrastructure Runtime → Data Layer.

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)

**Supersedes:** N/A (new document)
**Superseded By:** None (active)
