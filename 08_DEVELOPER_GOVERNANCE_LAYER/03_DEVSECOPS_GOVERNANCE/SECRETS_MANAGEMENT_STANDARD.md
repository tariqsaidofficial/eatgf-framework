# Secrets Management Standard

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 03_DEVSECOPS_GOVERNANCE
**Governance Scope:** Implementation Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

**Governance Scope:** Secrets management for development, CI/CD, and runtime environments.

**Control Authority Relationship:** Implements:

- Layer 02: Cryptographic Controls
- Layer 04: Information Security Policy
- NIST SSDF PS.2 (Protect sensitive data)

## Purpose

This standard defines requirements for secure management of secrets including:

- API keys, passwords, certificates
- Database credentials
- Encryption keys
- OAuth tokens and service account credentials

## Governance Principles

- **Security-by-Design:** Secrets never stored in code or version control
- **Control-Centric Architecture:** Centralized secrets management
- **Developer-Operational Alignment:** Seamless secret access without compromise
- **Audit Traceability:** All secret access logged

## Secrets Classification

### Secret Types

| Type                            | Examples                                  | Risk Level | Rotation Frequency           |
| ------------------------------- | ----------------------------------------- | ---------- | ---------------------------- |
| **Production Secrets**          | DB passwords, API keys for prod services  | Critical   | 90 days or on exposure       |
| **Non-Production Secrets**      | Dev/staging credentials                   | High       | 180 days                     |
| **Encryption Keys**             | Data encryption keys, signing keys        | Critical   | Per policy or on compromise  |
| **Service Account Credentials** | CI/CD service accounts, cloud credentials | Critical   | 90 days or workload identity |

## Prohibited Practices

**NEVER:**

- Hard-code secrets in source code
- Commit secrets to version control (including `.env` files)
- Store secrets in plain text configuration files
- Share secrets via email, chat, or unencrypted channels
- Log secrets in application logs or CI/CD output
- Store secrets in container images

## Secrets Management Solutions

### Recommended Solutions

**Cloud Provider Native:**

- AWS Secrets Manager / Parameter Store
- Azure Key Vault
- Google Cloud Secret Manager

**Third-Party:**

- HashiCorp Vault (most feature-rich)
- CyberArk Conjur
- Doppler

**Developer Requirements:**

- Use centralized secrets management system (no local secret storage)
- Retrieve secrets at runtime (not build time)
- Use short-lived credentials where possible
- Implement secret rotation

## Development Environment Secrets

### Local Development

**Requirement:** Use local secrets management without committing secrets.

**Developer Requirements:**

- Use environment variables loaded from non-committed files
- Add `.env`, `.env.local` to `.gitignore`
- Use direnv or similar tool to auto-load environment variables
- Provide `.env.example` template with placeholder values

**Example `.env.example`:**

```
DATABASE_URL=postgres://user:password@localhost:5432/dbname
API_KEY=your_api_key_here
```

### Shared Development Secrets

**Requirement:** Use secrets manager for shared dev environment secrets.

**Developer Requirements:**

- Store shared dev secrets in secrets manager
- Grant team access to dev secrets namespace
- Retrieve secrets using CLI or SDK
- Rotate dev secrets every 180 days

## CI/CD Secrets

### CI/CD Platform Secret Storage

**Requirement:** Use CI/CD platform's native secret storage.

**Platform-Specific:**

- **GitHub Actions:** Use GitHub Secrets or OIDC with cloud providers
- **GitLab CI:** Use GitLab CI/CD variables (masked and protected)
- **Jenkins:** Use Jenkins Credentials Plugin
- **CircleCI:** Use CircleCI Contexts and Environment Variables

**Developer Requirements:**

- Mark secrets as "masked" to prevent logging
- Use "protected" secrets for production (limited to protected branches)
- Do not echo secrets in scripts
- Grant access to secrets based on environment (dev/staging/prod)

### Workload Identity (Preferred)

**Requirement:** Use workload identity instead of long-lived credentials.

**Developer Requirements:**

- Configure OIDC between CI/CD platform and cloud provider
- Use short-lived tokens for cloud access
- No static credentials in CI/CD

**Example (GitHub Actions + AWS):**

```yaml
permissions:
  id-token: write # Required for OIDC
  contents: read

steps:
  - name: Configure AWS Credentials
    uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
      aws-region: us-east-1
```

**Benefits:**

- No long-lived credentials to rotate
- Fine-grained access control per workflow
- Automatic expiration

## Runtime Secrets

### Application Runtime

**Requirement:** Retrieve secrets from secrets manager at runtime.

**Developer Requirements:**

- Do not bundle secrets in container images or deployment packages
- Fetch secrets on application startup or on-demand
- Cache secrets in memory (not on disk)
- Refresh secrets periodically (handle rotation)
- Use SDK or sidecar pattern for secret access

**Example (Python with AWS Secrets Manager):**

```python
import boto3
import json

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

db_creds = get_secret('prod/database/credentials')
DATABASE_URL = db_creds['connection_string']
```

### Kubernetes Secrets

**Requirement:** Use external secrets operator or cloud provider integration.

**Developer Requirements:**

- Use External Secrets Operator to sync from Vault/cloud secrets manager
- Do not use Kubernetes Secrets directly (base64 is not encryption)
- Enable encryption at rest for etcd (Kubernetes secret storage)
- Use RBAC to limit secret access per namespace

**Example (External Secrets Operator):**

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: database-secret
spec:
  secretStoreRef:
    name: aws-secretsmanager
  target:
    name: database-credentials
  data:
    - secretKey: password
      remoteRef:
        key: prod/database/password
```

## Secret Rotation

### Rotation Policy

**Requirement:** Rotate secrets on defined schedule and after exposure.

**Rotation Schedule:**

| Secret Type          | Rotation Frequency | Trigger                             |
| -------------------- | ------------------ | ----------------------------------- |
| Production API keys  | 90 days            | On compromise or employee departure |
| Database passwords   | 90 days            | On compromise                       |
| Encryption keys      | Annually           | On algorithm weakness or compromise |
| Service account keys | 90 days            | On compromise                       |

**Developer Requirements:**

- Automate secret rotation where possible
- Test rotation procedure in non-production first
- Use zero-downtime rotation (support both old and new secret during transition)
- Document rotation procedure

### Zero-Downtime Rotation

**Procedure:**

1. Generate new secret
2. Add new secret to secrets manager
3. Update application to accept both old and new secret (grace period)
4. Deploy application changes
5. Update clients to use new secret
6. Revoke old secret after grace period (e.g., 24 hours)

## Secret Detection and Prevention

### Pre-Commit Secret Scanning

**Requirement:** Scan for secrets before committing code.

**Developer Requirements:**

- Install pre-commit hooks with secret detection (e.g., gitleaks, detect-secrets)
- Block commits containing secrets
- Configure `.pre-commit-config.yaml`

**Example Pre-Commit Configuration:**

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

### CI/CD Secret Scanning

**Requirement:** Scan repository for exposed secrets on every commit.

**Developer Requirements:**

- Integrate secret scanning in CI/CD (e.g., GitGuardian, TruffleHog, GitHub Secret Scanning)
- Fail build if secrets detected
- Alert security team on secret exposure

### Secret Rotation on Exposure

**Requirement:** Immediately rotate secrets if exposed.

**Incident Response:**

1. Revoke exposed secret immediately
2. Generate new secret
3. Update all consumers of secret
4. Investigate how secret was exposed
5. Implement preventive measures
6. Document incident and lessons learned

## Access Control

### Least Privilege Access

**Requirement:** Grant minimum necessary access to secrets.

**Developer Requirements:**

- Use namespaces or paths to segment secrets (e.g., `prod/`, `staging/`, `dev/`)
- Grant developers access to dev secrets only
- Grant DevOps access to staging and production secrets
- Use role-based access control (RBAC) in secrets manager
- Require MFA for production secret access

### Audit Logging

**Requirement:** Log all secret access for audit purposes.

**Developer Requirements:**

- Enable audit logging in secrets manager
- Log: timestamp, user/service identity, secret accessed, action (read/write/delete)
- Send logs to SIEM for monitoring
- Alert on anomalous patterns (e.g., bulk secret access, off-hours access)

## Control Mapping

| EATGF Context   | ISO 27001:2022 | NIST SSDF | OWASP      | COBIT |
| --------------- | -------------- | --------- | ---------- | ----- |
| Secret Storage  | A.8.24         | PS.2      | API2:2023  | DSS05 |
| Access Control  | A.5.15, A.5.18 | PS.1      | -          | DSS05 |
| Secret Rotation | A.8.24         | PS.2      | -          | DSS05 |
| Audit Logging   | A.8.15         | RV.1      | API10:2023 | DSS05 |

## Developer Checklist

For every project:

- [ ] No secrets in source code or version control
- [ ] Secrets retrieved from secrets manager at runtime
- [ ] Pre-commit hooks configured for secret detection
- [ ] CI/CD secret scanning enabled
- [ ] Secret rotation schedule defined
- [ ] Workload identity used (if supported by platform)
- [ ] Access to secrets based on least privilege
- [ ] Audit logging enabled

## Governance Implications

**Risk if not implemented:**

- Hardcoded secrets lead to credential exposure
- Compromised credentials enable unauthorized access
- Lack of rotation increases window for exploitation
- Compliance failures (PCI-DSS, SOC 2 require secrets management)

**Operational impact:**

- Centralized secrets management simplifies rotation
- Automated secret rotation reduces manual toil
- Secret detection prevents accidental exposure

**Audit consequences:**

- Audit logs demonstrate access control
- Secret rotation demonstrates proactive security
- Secrets management is standard audit requirement

**Cross-team dependencies:**

- Security team defines rotation policy
- DevOps team manages secrets infrastructure
- Developers implement secret retrieval in applications

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. Secrets Management Standard

## References

- NIST SP 800-218 (SSDF Practice PS.2)
- OWASP Secrets Management Cheat Sheet (<https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>)
- HashiCorp Vault (<https://www.vaultproject.io/>)
- AWS Secrets Manager Best Practices
- Gitleaks (<https://github.com/gitleaks/gitleaks>)

## Version History

| Version | Date       | Change Type | Description                         |
| ------- | ---------- | ----------- | ----------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial secrets management standard |
