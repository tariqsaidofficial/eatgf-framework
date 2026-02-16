# Secrets Management Standard

| Field          | Value                                                   |
| -------------- | ------------------------------------------------------- |
| Document Type  | Implementation Standard                                 |
| Version        | 1.0                                                     |
| Classification | Restricted                                              |
| Effective Date | 2026-02-16                                              |
| Authority      | Chief Security Officer and Platform Engineering Lead    |
| EATGF Layer    | 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE |
| MCM Reference  | EATGF-DSS-ENC-01                                        |

---

## Purpose

This standard defines mandatory requirements for managing cryptographic secrets, credentials, and sensitive configuration across development, staging, and production environments. Secrets must never be stored in source code, build logs, or documentation.

**Mandatory for:** All APIs, microservices, applications, and infrastructure requiring credentials.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

- **Upstream dependency:** Layer 04 Information Security Policy (credential management); Layer 02 Control Objectives (secret handling)
- **Downstream usage:** Ensures secrets protected throughout application lifecycle from development through production operations
- **Cross-layer reference:** Maps to NIST SSDF PO.5.1 (cryptographic key management), PW.3.1 (secret handling in code), PW.5 (build environment security)

## Governance Principles

1. **Never in Source Code** – Secrets never committed to Git; automated scanning blocks commits with secrets
2. **Hardware-Backed Protection** – Production secrets protected by hardware security module (HSM); development secrets by configuration vault
3. **Automatic Rotation** – Database passwords rotated every 90 days; API keys rotated every 180 days; certificates rotated 30 days before expiration
4. **Least Privilege Access** – Each service/application receives minimum secrets required; no shared credentials
5. **Audit Trail** – All secret access logged; access patterns analyzed for anomalies

## Technical Implementation

### Secret Classification

| Class             | Examples                                         | Storage               | Rotation                   | Access Control         |
| ----------------- | ------------------------------------------------ | --------------------- | -------------------------- | ---------------------- |
| Tier-1 (Critical) | Private keys, HSM keys, root credentials         | HSM only              | Quarterly or on compromise | CISO + 1 approval      |
| Tier-2 (High)     | Database passwords, API keys for payment/billing | Vault + encryption    | 90 days                    | Engineering lead + 1   |
| Tier-3 (Medium)   | Internal API tokens, service credentials         | Vault (encrypted)     | 180 days                   | Service owner          |
| Tier-4 (Low)      | GitHub tokens, npm credentials                   | Local encrypted vault | 90 days                    | Developer self-service |

### Development Environment

**Secrets in Development (Local Machine):**

```yaml
# ~/.bashrc or ~/.zshrc - DO NOT commit this
export VAULT_ADDR="https://vault.internal.example.com"
export VAULT_TOKEN="hvs.xxx"  # 24-hour token, auto-refreshed

# Option 1: Local encrypted vault
brew install pass  # macOS password manager
pass insert auth/database_password  # prompts for password

# Option 2: 1Password CLI
export OP_ACCOUNT_ID="xxx"
export OP_DEVICE="xxx"
eval "$(op signin my.1password.com user@company.com)"
```

**Prohibited in Development:**

- Hardcoded secrets in .env files
- Unencrypted secrets in configuration files
- Shared credentials in team channels (Slack, Discord)
- Credentials in Git history (if committed, rotate immediately)

**Approved Development Secret Storage:**

- 1Password
- LastPass
- HashiCorp Vault (local instance)
- Local encrypted `.env.local` (Git-ignored)
- macOS Keychain
- Linux `pass` or `keepass`

### Staging Environment

**Staging Secrets (Non-Production Sensitive Data):**

```yaml
# Deployed to AWS Secrets Manager or HashiCorp Vault
# Never reuse production secrets in staging
# Use test/disposable credentials with reduced permissions

secrets:
  database:
    username: staging_app_user # Read-only or limited to staging data
    password: <rotated every 90 days>
    host: staging-db.internal
    # NOT production host

  api_keys:
    stripe: sk_test_xxx # Stripe test key
    sendgrid: SG_test_xxx # SendGrid test key
    # NOT production keys

  certificates:
    tls_cert: /etc/secrets/staging-cert.pem
    tls_key: /etc/secrets/staging-key.pem
    # Test certificate; not production
```

**Access Control in Staging:**

- Staging Vault access: Development team only
- Password reset: No Vault access for non-engineers; manual request process
- Audit logging: All secret access logged; daily review for anomalies
- Credential rotation: 90-day cycle (same as production for consistency)

### Production Environment

**Production Secrets (Hardware-Backed):**

Requirements:

- **Vault:** AWS Secrets Manager (with KMS encryption) OR HashiCorp Vault Enterprise
- **Key Storage:** Hardware Security Module (FIPS 140-2 Level 2+)
- **Access:** Restricted service accounts only; human access requires break-glass procedure
- **Audit:** All access logged; SIEM integration for anomaly detection
- **Redundancy:** Multi-region replication; RTO <4 hours

```yaml
# Production Vault Structure

/prod/database/primary:
  username: prod_service_account # Service account with minimal privileges
  password: <auto-rotated every 90 days>
  read_replica_hosts:
    - replica-1.prod.internal
    - replica-2.prod.internal

/prod/tls_certificates/web:
  certificate: <cert.pem> # Auto-renewed 30 days before expiration
  private_key: <key.pem> # Hardware-backed; never exported
  key_id: prod-web-2024
  rotation_schedule: annually

/prod/api_keys/external:
  stripe_secret: sk_live_xxx
  stripe_publishable: pk_live_xxx
  datadog_api_key: xxx
  pagerduty_token: xxx
```

**Production Secret Access Procedures:**

| Scenario                  | Method                              | Approval            | Audit           |
| ------------------------- | ----------------------------------- | ------------------- | --------------- |
| Application startup       | Service account token (short-lived) | Deployment approval | Logged in SIEM  |
| Emergency database access | Break-glass procedure               | On-call lead + CISO | Immediate alert |
| Credential rotation       | Automated runner                    | None (scheduled)    | Routine logging |
| Key compromise            | Emergency rotation                  | CTO/CISO            | Incident log    |

### Automated Secret Rotation

**Database Password Rotation (90-day cycle):**

```yaml
# Kubernetes CronJob
apiVersion: batch/v1
kind: CronJob
metadata:
  name: db-secret-rotation
spec:
  schedule: "0 2 1 */3 *" # 2 AM, first day of every 3rd month
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: secret-rotator
          containers:
            - name: rotator
              image: postgres:15
              command:
                - /bin/sh
                - -c
                - |
                  # Fetch current password from vault
                  OLD_PASS=$(vault kv get -field=password prod/database/primary)

                  # Generate new password
                  NEW_PASS=$(openssl rand -base64 32)

                  # Update database user
                  psql -U admin -c "ALTER USER prod_service_account WITH PASSWORD '$NEW_PASS'"

                  # Update vault
                  vault kv put prod/database/primary password="$NEW_PASS"

                  # Notify applications (they refresh on next pod restart)
                  # or trigger rolling restart of deployments
                  kubectl rollout restart deployment/app-primary deployment/app-secondary
```

**Certificate Auto-Renewal (30 days before expiration):**

```yaml
# HashiCorp Vault PKI with auto-renewal
vault secrets enable pki
vault secrets tune -max-lease-ttl=87600h pki

# Certificate stored in Vault with renewal trigger at 30-day mark
vault write pki/roles/web \
  allowed_domains="*.example.com,example.com" \
  allow_subdomains=true \
  max_ttl=8760h \
  generate_lease=true
```

### Secrets in CI/CD Pipelines

**GitHub Actions Example:**

```yaml
name: Deploy to Production
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      # Get secrets from GitHub Secrets Manager
      - uses: actions/checkout@v3

      - name: Deploy with secrets
        env:
          DB_PASSWORD: ${{ secrets.PROD_DB_PASSWORD }}
          API_KEY: ${{ secrets.PROD_API_KEY }}
          TLS_KEY: ${{ secrets.PROD_TLS_KEY }}
        run: |
          # Secrets passed as environment variables; NOT printed in logs
          helm deploy --set db.password=$DB_PASSWORD \
                      --set api.key=$API_KEY \
                      --set tls.key=$TLS_KEY

          # Verify secrets NOT in logs
          if grep -i "password\|secret\|key" $GITHUB_STEP_SUMMARY; then
            echo "ERROR: Secret leaked in logs!"
            exit 1
          fi
```

**Prohibited in CI/CD:**

- Secrets in shell scripts (they get printed in logs)
- Secrets in YAML manifests committed to Git
- Secrets as commit messages or Pull Request descriptions
- Secrets in environment variable exports (use vault integration instead)

### Secret Scanning and Prevention

**Automated Secret Detection (Pre-Commit):**

```bash
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
        args: ['--verbose']
        stages: [commit]

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

**CI/CD Scanning Gate:**

```yaml
# GitLab CI secret detection
stages:
  - scan

secret_scan:
  stage: scan
  image: zricethezav/gitleaks:latest
  script:
    - gitleaks detect --verbose --exit-code=1
  allow_failure: false # Fail on secrets detected
```

### Secret Access Audit

**Vault Audit Policy:**

```json
{
  "type": "file",
  "format": "json",
  "path": "stdout",
  "description": "Log all secret access"
}
```

**Audit Log Analysis:**

```yaml
# Daily scan for suspicious patterns
SELECT timestamp, client_ip, action, path, error
FROM vault_audit_log
WHERE
timestamp > now() - interval '24 hours'
AND (
client_ip NOT IN (allowed_ips)
OR action IN ('create', 'delete')  -- unusual actions
OR error IS NOT NULL  -- access denied = potential breach attempt
)
ORDER BY timestamp DESC
```

**Anomaly Detection Triggers:**

- Access from unexpected IP address → block and alert
- Excessive access attempts → rate limit and investigate
- After-hours access to production secrets → escalate to CISO
- Secret accessed but not used (leaked?) → credential rotation

### Break-Glass (Emergency Access)

**Procedure for Emergency Production Access:**

1. On-call engineer calls CISO/CTO (verbal approval required)
2. Manager approval via email with incident description
3. Vault admin generates temporary session token (1-hour expiration)
4. Access logged with full audit trail
5. Post-incident review within 24 hours

```yaml
# Break-glass access grant
vault write auth/approle/role/breakglass/secret-id \
  ttl=1h \
  num_uses=1

# Usage
vault login -method=approle role_id=$ROLE_ID secret_id=$SECRET_ID
vault kv get prod/database/primary
# Access logged; token expires in 60 minutes
```

## Control Mapping

| EATGF Context  | ISO 27001:2022 | NIST SSDF    | OWASP    | COBIT    |
| -------------- | -------------- | ------------ | -------- | -------- |
| Secret storage | A.9.2, A.10.1  | PO.5.1, PW.3 | A02:2021 | BAI04.02 |
| Access control | A.9.2, A.9.4   | PO.1, PO.2   | A01:2021 | APO01.03 |
| Rotation       | A.9.2, A.10.1  | PO.5.1       | ASVS     | BAI04.02 |
| Audit logging  | A.12.4, A.12.7 | RV.1, RV.2   | -        | MEA02    |

## Developer Checklist

Before implementing secrets management:

- [ ] Vault system deployed (AWS Secrets Manager or HashiCorp Vault)
- [ ] HSM provisioned for production tier-1 secrets
- [ ] Secret classification taxonomy defined
- [ ] Pre-commit hooks configured (gitleaks, detect-secrets)
- [ ] CI/CD secret scanning gates implemented
- [ ] Development team trained on secret handling
- [ ] Automated rotation policies configured (90-day cycle)
- [ ] Certificate auto-renewal configured (30-day pre-expiration)
- [ ] Audit logging enabled; SIEM integration verified
- [ ] Break-glass procedure documented and tested
- [ ] Quarterly access audit performed
- [ ] Incident response procedures for compromised secrets
- [ ] All legacy hardcoded secrets migrated to vault

## Governance Implications

**Risk if not implemented:**

- Secrets leaked in source code; attackers gain production access
- Shared credentials across services; one compromise affects all
- Manual password management; rotation forgotten or skipped
- Audit cannot track who accessed which secrets; insider threat undetectable

**Operational impact:**

- Development velocity increases with pre-commit scanning
- Incident response time decreases (automated rotation limits damage window)
- Operational complexity increases initially (vault learning curve)
- Production resilience improves (automated credential management)

**Audit consequences:**

- Missing rotation evidence = ISO 27001 A.10.1 finding
- Access audit trail = key evidence for incident investigation
- Break-glass procedure = key compensating control for emergency access
- Compromised credentials = reportable security incident

**Cross-team dependencies:**

- Development: secret integration into applications, pre-commit scanning
- Platform/DevOps: vault infrastructure, rotation automation, audit logging
- Security: audit oversight, anomaly investigation, break-glass approval
- Compliance/Audit: control verification, access pattern review

## Official References

- **NIST SP 800-218** – Secure Software Development Framework (PO.5, PW.3, PW.5)
- **NIST SP 800-53** – Security and Privacy Controls (IA-4, IA-5, SC-12)
- **HashiCorp Vault Documentation** – Secret management architecture
- **AWS Secrets Manager** – AWS credential management service
- **OWASP A02:2021** – Cryptographic Failures
- **ISO/IEC 27001:2022** – Information Security Management

## Version History

| Version | Date       | Change Type | Description                                      |
| ------- | ---------- | ----------- | ------------------------------------------------ |
| 1.0     | 2026-02-16 | Major       | Initial secrets management standard for Layer 08 |
