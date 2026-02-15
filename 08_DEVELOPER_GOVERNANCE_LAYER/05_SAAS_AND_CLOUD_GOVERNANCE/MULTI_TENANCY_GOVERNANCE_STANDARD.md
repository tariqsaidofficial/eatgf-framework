# Multi-Tenancy Governance Standard

| Field | Value |
|-------|-------|
| Document Type | Implementation Standard |
| Version | 1.0 |
| Classification | Controlled |
| Effective Date | 2026-02-16 |
| Authority | Chief Technology Officer and Chief Security Officer |
| EATGF Layer | 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE |
| MCM Reference | EATGF-CLOUD-MT-01 |

---

## Purpose

Define architectural patterns and security controls for multi-tenant SaaS applications ensuring complete customer data isolation, preventing cross-tenant data leakage, and enforcing compliance per customer contract.

**Mandatory for:** All SaaS platforms; shared infrastructure serving multiple customers.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE

- **Upstream dependency:** Layer 04 Data Governance Policy; Layer 05 API Governance Framework
- **Downstream usage:** Enforces tenant isolation throughout application stack
- **Cross-layer reference:** Aligns with ISO 27001 A.8.2 (multi-tenancy requirements), NIST CSF

## Governance Principles

1. **Strong Isolation** – Cryptographic enforcement of tenant boundaries, not trust-based
2. **Least Privilege Per Tenant** – Each tenant accesses only own data; no cross-tenant exceptions
3. **Independent Compliance** – Each tenant's compliance posture independent; one tenant breach doesn't expose others
4. **Automated Compliance Assessment** – Continuous verification of isolation controls

## Technical Implementation

### Tenancy Models

| Model | Architecture | Data Isolation | Cost | Compliance | Use Case |
|-------|--------------|-----------------|------|-----------|----------|
| Database per Tenant | Separate databases per customer | Strong | High | Highest | Regulated industries; strict isolation |
| Schema per Tenant | Separate schemas in shared DB | Strong | Medium | High | Standard SaaS; good isolation |
| Row-Level Security (RLS) | Shared table; RLS policy enforcement | Medium | Low | Medium | Startups; cost-sensitive |

**Recommended:** Schema per Tenant + RLS as secondary validation.

```sql
-- Schema per Tenant Architecture
CREATE SCHEMA customer_123;
CREATE TABLE customer_123.users (id UUID, email TEXT);
CREATE TABLE customer_123.documents (id UUID, content TEXT);

-- RLS Policy (defense in depth)
CREATE POLICY tenant_isolation ON users
  USING (tenant_id = current_user_id());

-- Query enforcement
SELECT * FROM customer_123.users WHERE id = ?;
-- User cannot access customer_456 schema
```

### Data Isolation Implementation

**Query Isolation:**

```javascript
// Express.js middleware: inject tenant context
app.use((req, res, next) => {
  const tenantId = req.headers['x-tenant-id'];
  
  // Verify tenant ID matches authenticated user
  if (req.user.tenant_id !== tenantId) {
    return res.status(403).json({ error: 'Unauthorized tenant' });
  }
  
  // Pass context to all queries
  req.tenant = { id: tenantId, schema: `customer_${tenantId}` };
  next();
});

// ORM query builder
app.get('/api/documents', (req, res) => {
  // Automatically scoped to tenant
  prisma.$queryRaw`
    SELECT * FROM ${req.tenant.schema}.documents
    WHERE user_id = $1
  `;
});
```

**Cache Isolation:**

```python
# Redis cache with tenant prefix (prevents cache collision)
def get_user_cache_key(tenant_id, user_id):
    return f"tenant:{tenant_id}:user:{user_id}"

# Retrieve from cache
cache_key = get_user_cache_key(request.tenant_id, user_id)
cached_user = redis.get(cache_key)
if cached_user:
    return json.loads(cached_user)

# Store in cache with tenant isolation
redis.setex(cache_key, 3600, json.dumps(user_data))

# List all tenant keys (verify no cross-contamination)
tenant_keys = redis.keys(f"tenant:{tenant_id}:*")
```

**Search Index Isolation:**

```yaml
# Elasticsearch multi-tenant indexing
PUT /app-index-v1/_mapping
{
  "properties": {
    "tenant_id": {
      "type": "keyword"
    },
    "document": {
      "type": "text"
    }
  }
}

# Search with tenant filter (mandatory)
GET /app-index-v1/_search
{
  "query": {
    "bool": {
      "must": [
        { "term": { "tenant_id": "customer_123" } },  # Enforced
        { "match": { "document": "search_term" } }
      ]
    }
  }
}
```

### Backup and Restore Isolation

**Backup Strategy:**

- Separate backups per tenant (not shared backup)
- Backup encryption with tenant-specific key
- Restore tests quarterly to verify isolation

```bash
# Backup per tenant
pg_dump -Fc \
  --host=db.prod.internal \
  --username=backup_user \
  customer_123 > backups/customer_123/2024-02-16.sql.gz

# Encryption with tenant key (stored in vault)
openssl enc -aes-256-cbc -in backup.sql.gz -out backup.sql.gz.enc \
  -K $(vault kv get -field=key prod/backup-keys/customer_123)

# Restore isolation test
pg_restore -d test_customer_123 backups/customer_123/2024-02-16.sql.gz
# Verify no other tenant data present
SELECT COUNT(*) FROM pg_tables WHERE schemaname NOT LIKE 'customer_123%';
```

### Audit Logging Per Tenant

```sql
-- Audit table with tenant enforcement
CREATE TABLE audit_log (
  id UUID PRIMARY KEY,
  tenant_id UUID NOT NULL,
  user_id UUID NOT NULL,
  action TEXT NOT NULL,
  resource TEXT NOT NULL,
  timestamp TIMESTAMPTZ,
  
  CONSTRAINT tenant_fk FOREIGN KEY (tenant_id) REFERENCES tenants(id),
  
  -- RLS policy: only access own audit logs
  POLICY tenant_audit_policy ON audit_log
    USING (tenant_id = current_tenant_id())
);

-- Audit log query (cannot cross tenants)
SELECT * FROM audit_log WHERE tenant_id = ? ORDER BY timestamp DESC;
```

### Compliance Validation

**Automated Tenant Isolation Verification:**

```python
def verify_tenant_isolation():
    """Daily verification of tenant data isolation"""
    
    for tenant_id in get_all_tenants():
        schema = f"customer_{tenant_id}"
        
        # Verify no cross-tenant foreign keys
        cross_tenant_refs = query(f"""
            SELECT COUNT(*) FROM {schema}.documents
            WHERE tenant_id != '{tenant_id}'
        """)
        assert cross_tenant_refs == 0, f"Tenant {tenant_id} has cross-tenant data!"
        
        # Verify encryption at rest per tenant
        db_encryption_key = get_tenant_encryption_key(tenant_id)
        encrypted_fields = query(f"""
            SELECT COUNT(*) FROM {schema}.documents
            WHERE encrypted = true AND encryption_key_id = '{db_encryption_key}'
        """)
        
        # Verify cache has no cross-tenant entries
        tenant_cache_keys = redis.keys(f"tenant:{tenant_id}:*")
        for key in tenant_cache_keys:
            cached_value = redis.get(key)
            assert verify_tenant_ownership(tenant_id, cached_value)
    
    log_compliance_check(passed=True)
```

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | COBIT |
|---|---|---|---|
| Tenant isolation | A.8.2, A.8.3 | - | BAI10.02 |
| Data segregation | A.8.3 | - | DSS04 |

## Developer Checklist

- [ ] Tenancy model selected (Database/Schema/RLS)
- [ ] Query isolation middleware implemented
- [ ] Cache key isolation enforced
- [ ] Search index tenant filter mandatory
- [ ] Backup per-tenant strategy implemented
- [ ] Audit logging per-tenant enforced
- [ ] RLS policies configured as secondary validation
- [ ] Quarterly isolation verification automated
- [ ] Compliance dashboard created

## Version History

| Version | Date | Change Type | Description |
|---------|------|-------------|-------------|
| 1.0 | 2026-02-16 | Major | Initial multi-tenancy standard |
