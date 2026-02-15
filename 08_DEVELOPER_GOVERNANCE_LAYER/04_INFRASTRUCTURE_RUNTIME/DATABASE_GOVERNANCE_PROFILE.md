# Database Governance Profile

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
- **Governance Scope:** Implementation Standard
- **Control Authority:** Implements controls from API_GOVERNANCE_STANDARD

---

## Governance Principles

This profile enforces:

- **Security-by-Design:** Connection pooling, row-level security, encryption
- **Control-Centric Architecture:** 8 mandatory controls + audit logging
- **Versioned Governance:** Schema migration versioning, rollback capabilities
- **Developer-Operational Alignment:** ORM type safety, parameterized queries
- **Audit Traceability:** DML audit triggers, actor tracking, change history
- **Single Source of Truth:** Source control for schema migrations, idempotent scripts

---

## Control Mapping

| EATGF Control | ISO 27001:2022 | NIST SSDF | OWASP SAMM | COBIT |
|---|---|---|---|---|
| Authentication (non-root) | A.8.2 | PW.4 | ASVS V1 | APO13 |
| Authorization (RLS) | A.8.2 | PW.4 | ASVS V4 | APO13 |
| Schema Versioning | A.8.22 | PW.8 | Build.1 | DSS05 |
| SQL Injection Prevention | A.8.9 | PW.8 | ASVS V5 | CM-6 |
| Connection Pooling | A.8.9 | PW.8 | ASVS V14 | CM-3 |
| Query Auditing | A.8.15 | RV.1 | Verify.1 | MEA01 |
| Backup & Recovery | A.8.13 | PW.8 | Verify.2 | CM-3 |
| Encryption (TLS) | A.8.24 | PW.4 | ASVS V2 | IA-5 |

---

## Purpose

Define governance controls for database connections, multi-tenancy isolation, schema evolution, and audit logging to ensure data integrity and compliance in production databases.

**Applies to:**

- PostgreSQL, MySQL, Oracle databases
- Microservice databases
- Shared multi-tenant databases
- OLTP workloads
- Data warehouses & OLAP systems

---

## Technical Implementation

### Connection Pooling & Authentication

```python
# ✅ COMPLIANT: Service account (non-root), connection pooling
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Use environment variable for password (not hardcoded)
db_url = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:5432/app_db"
)

# SQLAlchemy connection pooling
engine = create_engine(
    db_url,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,  # Verify connection before use
    echo_pool=False,
    connect_args={
        "sslmode": "require",  # Force TLS
        "connect_timeout": 5,
        "options": "-c statement_timeout=30000"  # 30s timeout
    }
)

# Usage
from sqlalchemy import select
from sqlalchemy.orm import Session

with Session(engine) as session:
    stmt = select(User).where(User.tenant_id == current_tenant_id)
    users = session.execute(stmt).scalars()
```

### Row-Level Security (PostgreSQL)

```sql
-- ✅ COMPLIANT: RLS policies enforce tenant isolation
CREATE POLICY tenant_isolation ON users
    USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

CREATE POLICY tenant_isolation ON orders
    USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Set tenant context before queries
SET app.current_tenant_id = '550e8400-e29b-41d4-a716-446655440000';

-- Now this query returns only current tenant's users
SELECT * FROM users;  -- RLS enforces WHERE tenant_id = '550e8400...'
```

### Schema Versioning (Alembic/Flyway)

```python
# ✅ COMPLIANT: Version control for all schema changes
# migrations/env.py
from alembic import context
from sqlalchemy import engine_from_config, pool
from alembic.config import Config

config = Config('alembic.ini')
target_metadata = Base.metadata

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.begin() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Usage:
# alembic revision --autogenerate -m "Add users table"
# alembic upgrade head
```

### Audit Logging with Triggers

```sql
-- ✅ COMPLIANT: Audit trail for all DML operations
CREATE TABLE audit_log (
    id BIGSERIAL PRIMARY KEY,
    table_name VARCHAR(255) NOT NULL,
    operation VARCHAR(10) NOT NULL,  -- INSERT, UPDATE, DELETE
    actor_id UUID NOT NULL,
    actor_role VARCHAR(50),
    old_values JSONB,
    new_values JSONB,
    changed_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_audit_table_changed (table_name, changed_at)
);

CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (
        table_name, operation, actor_id, actor_role, old_values, new_values
    ) VALUES (
        TG_TABLE_NAME,
        TG_OP,
        current_user_id(),  -- From JWT or session
        current_user_role(),
        CASE WHEN TG_OP = 'DELETE' THEN row_to_json(OLD) ELSE NULL END,
        CASE WHEN TG_OP != 'DELETE' THEN row_to_json(NEW) ELSE NULL END
    );
    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;

-- Attach to relevant tables
CREATE TRIGGER users_audit AFTER INSERT OR UPDATE OR DELETE ON users
    FOR EACH ROW EXECUTE FUNCTION audit_trigger();

CREATE TRIGGER orders_audit AFTER INSERT OR UPDATE OR DELETE ON orders
    FOR EACH ROW EXECUTE FUNCTION audit_trigger();
```

---

## Developer Checklist

- [ ] Database user (service account) has minimal privilege (not root/admin)
- [ ] Connection string uses environment variables (not hardcoded)
- [ ] TLS/SSL enforced (sslmode=require for PostgreSQL)
- [ ] Connection pooling configured (SQLAlchemy, HikariCP, pgBouncer)
- [ ] Query timeout set (30-60 seconds depending on workload)
- [ ] All queries use parameterized statements (no string concatenation)
- [ ] Row-Level Security (RLS) policies defined and tested per tenant
- [ ] Schema migrations version controlled (Alembic, Flyway, Liquibase)
- [ ] Audit triggers log all INSERT/UPDATE/DELETE with actor & timestamp
- [ ] Database backups automated and tested (PITR capability)
- [ ] Secrets (DB password) managed externally (AWS Secrets Manager, Vault)
- [ ] Read replicas for reporting (OLAP separated from OLTP)
- [ ] Indexes created for all foreign keys and filtering columns
- [ ] Query performance monitored (slow query logging enabled)
- [ ] Data recovery tested monthly (backup → restore → verify)

---

## Governance Implications

### Risk if Not Implemented

- **SQL Injection:** String concatenation → unauthorized data access/modification
- **Privilege Escalation:** Admin account used for app → all table access
- **Data Breach:** No RLS → one tenant reads another tenant's data
- **Audit Trail Loss:** No triggers → cannot detect unauthorized changes
- **Unrecoverable Data Loss:** No backups → business continuity failure

### Operational Impact

- Tenant isolation failure → compliance violation + potential lawsuit
- Connection exhaustion → application unresponsive
- Schema drift (manual changes not tracked) → deployment conflicts
- Backup failure → data loss in disaster scenario

### Audit Consequences

- **ISO 27001 A.8.2:** Access control not minimal
- **SOC2 CC6.1:** Privilege management failure
- **HIPAA 45 CFR §164.308:** Backup procedures not implemented
- **PCI-DSS 3.4:** Cardholder data not protected in transit

### Cross-Team Dependencies

- DBA team: Must maintain RLS policies, backup automation
- Security team: Must rotate DB passwords, validate encryption
- Development team: Must write migrations, use parameterized queries
- Platform team: Must secure secrets management system

---

## Official References

- PostgreSQL Security: <https://www.postgresql.org/docs/current/sql-createrls.html>
- NIST SP 800-218: Secure Software Development Framework
- OWASP Top 10: A03:2021 Injection
- CIS PostgreSQL Benchmark v1.3.0
- Alembic Documentation: <https://alembic.sqlalchemy.org/>

---

## Version Information

- **Version:** 1.0
- **Change Type:** Major (Initial Release)
- **Date:** 2026-02-15
- **Status:** Published
- **Target Audience:** Database architects, backend engineers, DBAs
- **Database Versions:** PostgreSQL 13+, MySQL 8.0+, Oracle 19c+

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)
