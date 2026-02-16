# End-of-Life Governance Standard

| Property           | Value                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| **Document Type**  | Implementation Standard                                                                                  |
| **Version**        | 1.0                                                                                                      |
| **Classification** | Governance                                                                                               |
| **Effective Date** | February 16, 2026                                                                                        |
| **Authority**      | Chief Technology Officer                                                                                 |
| **EATGF Layer**    | 08_DEVELOPER_GOVERNANCE_LAYER / 06_APPLICATION_LIFECYCLE_GOVERNANCE                                      |
| **MCM Reference**  | [EATGF-DEV-SDLC-01: Secure Software Development Lifecycle](../../00_FOUNDATION/MASTER_CONTROL_MATRIX.md) |

---

## Purpose

Eventually every software version, API, and feature must retire. This standard ensures:

- **Clear sunset timelines** (minimum 6 months notice before EOL)
- **Customer migration pathways** (upgrade guides; assisted migration if critical)
- **Security patch backports** (up to 12 months for critical CVEs only)
- **Data cleanup procedures** (safe deletion of supporting tables/features)
- **Dependent system updates** (notify downstream consumers before EOL)

**Mandatory:** All deprecated features and versions must follow this standard for orderly retirement.

---

## Architectural Position

**Upstream Dependencies:**

- Layer 02 Control Architecture [EATGF-DEV-SDLC-01: Secure Software Development Lifecycle]
- Layer 04 GOVERNANCE_CHARTER (EOL authority and notice timelines)
- Layer 08.06 RELEASE_GOVERNANCE_STANDARD (versioning policy for EOL decisions)

**Downstream Usage:**

- Layer 06 AUDIT_AND_ASSURANCE (EOL audit trails)

**Cross-Layer References:**

- RELEASE_GOVERNANCE_STANDARD.md (semantic versioning; breaking changes)
- API_GOVERNANCE_STANDARD.md (API versioning and deprecation)
- DATA_PRIVACY_AND_PROTECTION_POLICY.md (data cleanup on EOL)

---

## Governance Principles

1. **Long Runway:** Minimum 6 months advance notice before EOL (longer for critical systems)
2. **Clear Migration Path:** Always provide upgrade/migration guide before sunset
3. **Security Responsibility:** Critical security patches backported if feasible (up to 12 months EOL)
4. **Customer Choice:** Customers can choose to remain on old version (with explicit acceptance of risk)
5. **Clean Shutdown:** Data and dependent systems safely cleaned up on EOL

---

## Technical Implementation

### 1. Deprecation & EOL Timeline

**Software Lifecycle Stages:**

```
┌──────────────────────────────────────────────────────────┐
│ ACTIVE SUPPORT (2 years)                                 │
├──────────────────────────────────────────────────────────┤
│ v2.0.0 released: Jan 1, 2024                            │
│ Support: Bug fixes, security patches, features           │
│ SLA: ≤24h response to critical issues                   │
│ Example: v2.4.0 released Jan 1, 2025 (1 year in)        │
└──────────────────────────────────────────────────────────┘
                          │ (1 year)
                          ▼
┌──────────────────────────────────────────────────────────┐
│ MAINTENANCE (1 year)                                     │
├──────────────────────────────────────────────────────────┤
│ v2.0 moves to maintenance: Jan 1, 2026                  │
│ Support: Security patches ONLY (no features, bug fixes) │
│ SLA: ≤7d response to critical CVEs                      │
│ Backports: Critical fixes only; minor patches stop      │
│ Releases: Infrequent; once per quarter if needed        │
└──────────────────────────────────────────────────────────┘
                          │ (1 year)
                          ▼
┌──────────────────────────────────────────────────────────┐
│ EXTENDED SUPPORT (if critical dependency) (Optional)     │
├──────────────────────────────────────────────────────────┤
│ v2.0 extended: Jan 1, 2027 (additional 1-2 years)      │
│ Requirements: Customer paid support contract             │
│ Support: Security patches only; no feature compatibility│
│ SLA: ≤14d response                                      │
│ Cost: $100k/year (enables continued investment)         │
└──────────────────────────────────────────────────────────┘
                          │ (up to 2 years)
                          ▼
┌──────────────────────────────────────────────────────────┐
│ END-OF-LIFE (EOL)                                        │
├──────────────────────────────────────────────────────────┤
│ v2.0 EOL: Jan 1, 2029                                   │
│ Support: NONE (no patches; no bug fixes)                │
│ Official End: Version no longer maintained              │
│ Migration: Customers must upgrade to v3.x               │
│ Data: Cleanup of deprecated tables; historical archive  │
└──────────────────────────────────────────────────────────┘
```

### 2. Deprecation Process & Customer Communication

**Feature Deprecation Lifecycle:**

```
SCENARIO: Deprecate old payment processor integration

T-6 months before EOL (Feb 1, 2026):
├─ Decision: "Old Stripe integration (v1) will be removed June 1"
├─ Announce: Release v2.3.0 includes deprecation notice:
│  {
│    "deprecated": {
│      "Stripe v1 integration": {
│        "removed_in": "v4.0",
│        "removed_date": "2026-06-01",
│        "migration_guide": "https://docs.company.com/stripe-migration-v1-to-v2",
│        "message": "Use Stripe v2 integration instead (backward compatible)"
│      }
│    }
│  }
├─ In-App Warning: Dashboard shows banner to Stripe v1 users
│  "Your Stripe integration (v1) will retire June 1, 2026.
│   Please migrate to Stripe v2. Migration takes ~10 min. [Learn More]"
└─ Email: Proactive outreach to customers still using v1
   Subject: Action Required: Stripe Integration Migration

T-3 months (May 1, 2026):
├─ Escalate: Increase communication frequency
├─ Webinar: "How to migrate from Stripe v1 to v2 (30 min walkthrough)"
├─ In-App: Banner upgraded to red "URGENT: Action required"
├─ Email: "60 days remaining; schedule migration with us" (offer assistance)
└─ Support: Assistance offered; no additional charge

T-1 month (June 1, 2026 minus 30 days):
├─ Final Notice: "30 days until Stripe v1 retirement"
├─ Support Escalation: Dedicated team for v1-to-v2 migrations
├─ Create Jira Tickets: For customers not yet migrated (outreach)
└─ Prepare: Disable v1 infrastructure (scheduled for June 1)

T-0: END-OF-LIFE (June 1, 2026)
├─ Disable v1: Stripe v1 code paths removed
├─ Migrate: Customers not migrated in time:
│  - If integrated: Automatic migration script (run update_payment_provider)
│  - If not integrated: Account suspended (must migrate or contact support)
├─ Cleanup: Delete Stripe v1 database tables (after 30-day archive)
├─ Archive: Historical data exported to cold storage (7-year retention for audits)
└─ Announce: "Stripe v1 officially retired; v2 is standard"

Post-EOL Support:
├─ "Sorry, Stripe v1 is no longer supported. Please upgrade to v2."
├─ Self-service migration instructions available
├─ Premium support available for difficult migrations
└─ No active support resources dedicated to v1
```

### 3. Complex EOL: API Versions

**API Versioning & Sunset Strategy:**

```
API VERSION TIMELINE:

┌─ /api/v1 ────────────────────────────────────────────────┐
│ Released: 2022-01-01                                      │
│ Latest: 1.15.3 (patches through 2024)                    │
│ Status: SUPPORTED until Jan 1, 2025                      │
│ Customer Count: ~40% (industry standard integrations)    │
│                                                            │
│ DEPRECATION (Dec 2024): "v1 will sunset Jan 1, 2025"     │
│ - API responds with X-Deprecated header                 │
│ - SDK logs warnings                                     │
│ - Documentation page v1 marked " Retired"             │
│ - Old clients still work (no breaking changes)          │
│                                                            │
│ EOL (Jan 1, 2025):                                       │
│ ├─ /api/v1 endpoints return 410 Gone (not 404)          │
│ ├─ Error message: "API v1 is retired. Migrate to /api/v3"│
│ ├─ Requests: Rejected with HTTP 410                      │
│ └─ Final redirect: https://docs/migration-v1-to-v3      │
└──────────────────────────────────────────────────────────┘

┌─ /api/v2 ────────────────────────────────────────────────┐
│ Released: 2023-06-01                                      │
│ Latest: 2.8.2                                            │
│ Status: SUPPORTED until June 1, 2025                     │
│ Customer Count: ~50% (mostly new customers)              │
│                                                            │
│ NOTICE (Mar 2025): "v2 supported through June 1, 2025"   │
│ - Dashboard: Notice to v2 users                          │
│ - Email: Upgrade campaign starts                         │
│                                                            │
│ DEPRECATION (Apr 2025): "v2 sunset June 1"               │
│ - Log deprecation warnings                               │
│ - Added X-Deprecated header                              │
│                                                            │
│ EOL (June 1, 2025): Sunset according to v1 pattern       │
└──────────────────────────────────────────────────────────┘

┌─ /api/v3 ────────────────────────────────────────────────┐
│ Released: 2024-06-01                                      │
│ Latest: 3.2.1 (stable, current standard)                │
│ Status: ACTIVE SUPPORT (minimum through June 1, 2026)   │
│ Customer Count: ~10% (early adopters; v1/v2 migrating)   │
│                                                            │
│ Growth Plan:                                              │
│ ├─ Q1 2025: 30% of traffic (migration campaigns)         │
│ ├─ Q2 2025: 60% of traffic (v1/v2 EOL pressure)          │
│ └─ Q3 2025: 90% of traffic (mature version)              │
│                                                            │
│ Support: Full support, new features, ongoing development │
└──────────────────────────────────────────────────────────┘

PARALLEL SUPPORT POLICY:
- Only 2 API versions supported simultaneously (v3 + one legacy)
- When v3 > 50% of traffic, deprecate older version
- Minimum 6 months support for any version
- Maximum 18 months total support (active + maintenance)
```

**HTTP Status Code for Deprecated/EOL:**

```
v1.x API calls after EOL:

HTTP/1.1 410 Gone  ← Permanent removal (not 404 Not Found)
Content-Type: application/json
X-Deprecated: true
X-Deprecated-Until: 2024-12-31

{
  "error": "api_version_retired",
  "message": "/api/v1 was retired Jan 1, 2025",
  "migration_url": "https://docs.company.com/migrate-v1-v3",
  "supported_versions": ["v2", "v3"],
  "alternative": "Use /api/v3 (current stable version)",
  "support_contact": "support@company.com"
}
```

### 4. Data Cleanup on EOL

**Secure Deletion of EOL Feature Data:**

```
SCENARIO: Retiring "Reports v1" feature (old dashboard)

Pre-EOL Phase (3 months before):
├─ Backup: Archive all Reports v1 data
│  - SQL: SELECT * FROM reports_v1 → archive.sql.gz (encrypted)
│  - S3: Upload to s3://archives/reports-v1-EOL/ (retention: 7 years)
│  - Notification: "Reports v1 data backed up for audit trail"
├─ Migration: Offer: "Export Reports v1 data as CSV" (self-service)
└─ Communication: "After EOL, Reports v1 data will be deleted"

On EOL Date:
├─ Step 1: Final backup verification
│  - Confirm archive size > 0
│  - Test restore from archive (successfully restore 10 random records)
│  └─ Duration: ~30 min
├─ Step 2: Database cleanup
│  - Delete reports_v1 table
│  - Disable foreign keys referencing reports_v1
│  - Run: DROP TABLE reports_v1 CASCADE;
│  └─ Duration: ~5 min (small table; no locking)
├─ Step 3: Verify cleanup
│  - Confirm table deleted
│  - Verify no orphaned references
│  - Check disk space reclaimed
│  └─ Duration: ~5 min
└─ Step 4: Audit trail
   - Log: "Reports v1 data deleted per EOL policy (archive: s3://...)"
   - Archive location documented for 7-year retention

Post-EOL:
├─ If customer requests: "We deleted your Reports v1 data per retireemnt notice.
                          Archived backup available (if within 7-year window)."
├─ Support: Can restore from archive if audit-justified (e.g., legal hold)
└─ Compliance: Audit trail shows orderly deletion; retention policy followed
```

### 5. Dependent System Notifications

**Cascading EOL: Notify Downstream Systems**

```
SCENARIO: Database v13 will retire June 1, 2026

Direct Consumers (Tier 1: High priority):
├─ Our applications using PostgreSQL v13 (internal)
├─ Customers using DBaaS PostgreSQL v13
├─ Third-party services using our v13 SDKs
└─ Notification: Email + dedicated migration webinar

Indirect Consumers (Tier 2: Medium priority):
├─ Customers using ORMs compiled against v13 (6 months notice)
├─ Docker images with v13 pre-installed in our registry
├─ Kubernetes Helm charts pinning v13
└─ Notification: Release notes; blog post

Further Downstream (Tier 3: Low priority):
├─ Customers using documentation/examples showing v13
├─ Developers in tutorials mentioning v13
└─ Notification: Updated docs automatically; old versions archived

Notification Template:
Subject: PostgreSQL v13 Support Ends June 1, 2026

Dear Developers,

PostgreSQL v13 will reach end-of-life on June 1, 2026.
We recommend upgrading to PostgreSQL v15 (stable) or v16 (latest).

 Actions Required:
  1. Update your Dockerfile: FROM postgres:15-alpine
  2. Test in staging environment
  3. Schedule production upgrade (RTO: ~30 min)

 Migration Paths:
  - v13 → v15 (recommended): Backward compatible
  - v13 → v16 (cutting edge): Recent release; test thoroughly

 Support:
  - Migration guide: https://docs/postgres-migration-v13-v15
  - Office hours: Fridays 2pm UTC (migration help)
  - Questions: support@company.com

 Timeline:
  - By Feb 1, 2026: Upgrade planning complete
  - By May 1, 2026: Staging environment tested
  - By June 1, 2026: Production environment migrated
```

### 6. EOL Metrics & Dashboards

**EOL Compliance Tracking:**

```
EOL DASHBOARD:

┌──────────────────────────────────────────────────────────┐
│ API v1 EOL (Completed: Jan 1, 2025)                      │
├──────────────────────────────────────────────────────────┤
│ Sunset Date: Jan 1, 2025                                │
│ Migration Rate: 95% (38 of 40 customers migrated)        │
│ Remaining Users: 2 (stuck on legacy; paying for support) │
│ Support Requests: 8 total (average resolution: 2h)      │
│ Compliance:  Completed on schedule                      │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ Reports v1 EOL (In Progress: June 1 target)              │
├──────────────────────────────────────────────────────────┤
│ Sunset Date: June 1, 2026 (106 days remaining)           │
│ Migration Rate: 70% (28 of 40 customers migrated)        │
│ Remaining Users: 12 (outreach in progress)               │
│ At-Risk Customers: 3 (no migration activity; escalate)   │
│ Support Requests: 2 total (migration assistance)         │
│ Compliance Risk:  12 customers need outreach by May 15 │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ PostgreSQL v13 EOL (Planned: June 1, 2026)               │
├──────────────────────────────────────────────────────────┤
│ Sunset Date: June 1, 2026 (106 days remaining)           │
│ Migration Rate: 45% (18 of 40 environments)              │
│ Remaining: 22 environments (staging/dev mostly)          │
│ At-Risk: 5 production environments (critical; escalate)  │
│ Support: Dedicated migration team (M-F 10am-6pm UTC)    │
│ Compliance Risk:  5 prod environments off-schedule     │
└──────────────────────────────────────────────────────────┘

COMPLIANCE STATUS: 1/3   |  2/3 ⏳  |  Success Rate: 33%
```

---

## Control Mapping

| EATGF Control      | ISO 27001:2022  | NIST SSDF  | COBIT 2019   | OWASP        |
| ------------------ | --------------- | ---------- | ------------ | ------------ |
| Software Lifecycle | A.8.2-3, A.8.30 | PW.4, RV.1 | BAI07        | SAMM SM      |
| Data Retention     | A.8.30, A.13    | N/A        | MEA03        | Not Directly |
| Deprecation        | A.8.2           | PW.4       | BAI07        | SAMM SM      |
| Dependent Systems  | A.8.32          | PW.4       | BAI07, DSS04 | SAMM SM      |

---

## Developer Checklist

- [ ] Understand feature lifecycle (active support → maintenance → EOL)
- [ ] For new features: Document sunset timeline (if applicable)
- [ ] For deprecated features: Create migration guide before customers affected
- [ ] API versions: Set X-Deprecated header; include endpoint for migration instructions
- [ ] Notify dependent systems: Identify and notify everyone using old version
- [ ] Communicate: 6-month advance notice before EOL; escalate at 3 months, 1 month
- [ ] Migration assistance: Offer implementation help for critical customers
- [ ] Backup data: Archive EOL data before deletion (7-year retention)
- [ ] Verify cleanup: Test data restoration from archive (post-deletion)
- [ ] Track compliance: Monitor customer migration rates; escalate stragglers
- [ ] Security patches: Backport critical CVEs up to 12 months post-EOL (if feasible)
- [ ] Post-EOL support: Clear answer ("deprecated; here's migration guide")

---

## Governance Implications

**Risk if not implemented:**

- Customers surprised by sudden discontinuation; support load spikes
- Security patches can't be backported; customers stuck on vulnerable versions
- Orphaned data not cleaned up properly; compliance issues
- Dependent systems break abruptly; cascading failures

**Operational impact:**

- Orderly version retirement; predictability for customers
- Long runway allows customers to plan migrations
- Clear timelines reduce support escalations
- Archival process ensures data never truly lost (audit trail)

**Audit consequences:**

- External auditors verify EOL procedures documented
- Data cleanup traceable through audit logs
- Compliance with retention policies demonstrated
- Customer notifications show professional lifecycle management

**Cross-team dependencies:**

- **Engineering:** Develop migration guides; backport security patches
- **Product:** Determine EOL timeline; manage feature retirement
- **Support:** Help customers migrate; escalate stragglers
- **Legal/Compliance:** Retain archives per regulatory requirements
- **Customer Success:** Proactive outreach; conversion of premium support

---

## Official References

- **Semantic Versioning:** https://semver.org/ (EOL planning context)
- **NIST SP 800-88:** Guidelines for Media Sanitization (data cleanup)
- **ISO 27001:2022 Annex A.13:** Removal of assets (EOL data deletion)
- **OpenAPI Specification:** Deprecation field in schema definitions

---

## Version History

| Version | Date         | Change Type | Notes                                                                                                                                                                  |
| ------- | ------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Feb 16, 2026 | Major       | Initial release; EOL timeline (active/maintenance/extended/EOL), deprecation process, API versioning, data cleanup, dependent system notifications, compliance metrics |

---

_Last Updated: February 16, 2026_
_EATGF v1.0-Foundation: End-of-Life Governance Standard_
