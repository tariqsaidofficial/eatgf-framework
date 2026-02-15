# Terraform Governance Profile
## Infrastructure-as-Code Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Infrastructure Runtime - IaC Layer)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → 04_INFRASTRUCTURE_RUNTIME → INFRASTRUCTURE_AS_CODE_LAYER

**CONTROL AUTHORITY RELATIONSHIP:**
- This profile **implements** infrastructure governance controls from [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **orchestrates** DOCKER_GOVERNANCE_PROFILE.md, KUBERNETES_GOVERNANCE_PROFILE.md, DATABASE_GOVERNANCE_PROFILE.md provisioning
- This profile **enforces** infrastructure immutability and auditability
- This profile **does not** manage CI/CD pipelines (see SECURE_SDLC governance)

**COMPLIANCE STATEMENT:** Terraform (IaC layer) represents the **INFRASTRUCTURE_AS_CODE_LAYER** where all infrastructure declared and versioned. Non-conformance results in:
- Undocumented infrastructure drift (manual changes)
- Uncontrolled state file exposure (credentials in plaintext)
- Privilege escalation via overpermissioned service accounts
- Deployment inconsistency (config not matching code)
- Audit trail loss (infrastructure changes untracked)

Every infrastructure change must flow through versioned Terraform.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Terraform infrastructure-as-code supporting backend applications under EATGF.

**Scope:** Terraform configuration management, state file security, secrets handling, policy enforcement, plan validation, dependency isolation

**Non-Scope:** Ansible/CloudFormation/bicep (different IaC tools), CI/CD execution environment (see SECURE_SDLC), Cloud provider-specific features

**Terraform Version:** 1.6.0+

**Supported Cloud Providers:** AWS, GCP, Azure, Kubernetes (multicloud)

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
    ├── DATABASE_GOVERNANCE (Data Layer)
    ├── TERRAFORM_GOVERNANCE (Infrastructure as Code) ← THIS PROFILE
    └── CLOUD_RUNTIME_GOVERNANCE (Cloud Controls)
```

**Terraform operates as:**
- Infrastructure state manager (tfstate file)
- Deployment automation engine
- Plan approval enforcer
- Dependency graph resolver
- Resource versioning system

**Critical Principle:** Infrastructure immutability. All changes via `terraform apply`, never manual changes.

---

## 3. Governance Principles

### Principle 1: State File Encryption & Versioning (MANDATORY)

Terraform state must be encrypted at rest and versioned in secure backend.

```bash
# ❌ PROHIBITED: Local unencrypted state
terraform init  # Creates terraform.tfstate locally (plaintext)

# ✅ COMPLIANT: Remote encrypted backend
cat > backend.tf <<EOF
terraform {
  backend "s3" {
    bucket             = "terraform-state-prod"
    key                = "core/terraform.tfstate"
    region             = "us-east-1"
    encrypt            = true              # Encrypt at rest
    dynamodb_table     = "terraform-locks"  # State locking
  }
}
EOF

# ✅ COMPLIANT: Backend configuration
# AWS S3 backend settings:
# - Versioning: enabled (history of state changes)
# - Encryption: AES-256 (SSE-S3)
# - Public Access: blocked (deny-all ACLS)
# - MFA Delete: enabled (require MFA to delete versions)
```

---

### Principle 2: Secrets Management (MANDATORY)

No secrets in tfvars or state files. External secret manager (AWS Secrets Manager, Vault) mandatory.

```hcl
# ❌ PROHIBITED: Secrets in tfvars
variable "db_password" {
  default = "super-secret-password"  # Visible in state, SCM
}

# ✅ COMPLIANT: External secret manager
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "prod/database/password"
}

resource "aws_db_instance" "production" {
  allocated_storage = 100
  engine             = "postgres"
  username           = "app_user"
  password           = data.aws_secretsmanager_secret_version.db_password.secret_string
  # Password never appears in tfstate, logs, or SCM
}

# ✅ COMPLIANT: Sensitive output masking
output "db_password" {
  value       = aws_db_instance.production.password
  sensitive   = true  # Prevent logging in console
}
```

---

### Principle 3: Service Account Least Privilege (MANDATORY)

Service accounts used by Terraform have minimal IAM permissions.

```json
# ✅ COMPLIANT: Minimal IAM policy for Terraform
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:GetReservedInstancesDiscount",
        "elasticloadbalancing:Describe*",
        "cloudformation:ListStacks",
        "cloudformation:ListStackResources",
        "cloudformation:DescribeStacks",
        "cloudformation:DescribeStackResource",
        "cloudformation:DescribeStackResources",
        "rds:Describe*",
        "s3:List*",
        "s3:Get*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:RunInstances",
        "ec2:TerminateInstances",
        "ec2:ModifyInstanceAttribute",
        "elasticloadbalancing:Create*",
        "elasticloadbalancing:Delete*"
      ],
      "Resource": [
        "arn:aws:ec2:region:account-id:instance/*",
        "arn:aws:elasticloadbalancing:region:account-id:targetgroup/*"
      ]
    }
  ]
}

# ❌ PROHIBITED: AdministratorAccess
# "Effect": "Allow",
# "Action": "*",
# "Resource": "*"
```

---

### Principle 4: Infrastructure Immutability (MANDATORY)

No manual infrastructure changes. All changes via `terraform apply`.

```hcl
# ✅ COMPLIANT: Infrastructure-as-Code enforces immutability
resource "aws_kubernetes_cluster" "production" {
  name    = "prod-cluster"
  version = "1.28.0"  # Pinned version, immutable

  # All config changes via terraform
  desired_capacity     = 3
  max_size            = 5
  min_size            = 3
  node_group_version  = "1.28.0"  # Must rebuild nodes
}

# ❌ PROHIBITED: Manual changes
# aws ec2 modify-instance-attribute --instance-id i-123 --security-group sg-new
# OK, this changes infrastructure outside Terraform, state drift occurs
```

---

### Principle 5: Plan Review & Approval (MANDATORY)

All infrastructure changes require peer review before apply.

```bash
# ✅ COMPLIANT: Plan review workflow
terraform plan -out=tfplan
# Output: create aws_db_instance.prod, destroy aws_ec2_instance.legacy

# Plan reviewed in pull request (peer approval)
# PR must be approved before merge

# Post-approval:
terraform apply tfplan

# ✅ COMPLIANT: Policy enforcement (Sentinel/OPA)
# Prevent high-risk operations:
# - Deletion of prod resources
# - Changes to security groups without justification
# - Modifications to database passwords
```

---

### Principle 6: Dependency Isolation & Modularity (MANDATORY)

Infrastructure split into modules with explicit dependencies, no cross-module coupling.

```hcl
# ✅ COMPLIANT: Module structure
# modules/database/main.tf
resource "aws_db_instance" "core" {
  allocated_storage = var.storage
  engine             = var.engine
  # No hardcoded references to other modules
}

# modules/database/variables.tf
variable "storage" { type = number }
variable "engine" { type = string }

# root/main.tf
module "database" {
  source = "./modules/database"
  storage = 100
  engine  = "postgres"
}

module "kubernetes" {
  source = "./modules/kubernetes"
  # Explicit dependency
  depends_on = [module.database]
}

# ❌ PROHIBITED: Cross-module coupling
# modules/database/main.tf references ../kubernetes/output
# data "aws_eks_cluster" "main" { name = aws_eks_cluster.primary.name }
# Circular dependency, difficult to test/maintain
```

---

### Principle 7: Change Validation & Testing (MANDATORY)

All Terraform changes validated before merge, syntax verified, policy tested.

```bash
# ✅ COMPLIANT: Automated validation
terraform fmt -check .          # Format compliance
terraform validate              # Syntax check
terraform plan -json > plan.json # JSON output for analysis

# Static analysis (tflint)
tflint --init
tflint .
# Detects: unused resources, deprecated syntax, AWS best practices

# Policy validation (Sentinel)
sentinel test -verbose policy.sentinel

# ❌ PROHIBITED: No validation
terraform apply -auto-approve main.tf
# Syntax errors, policy violations deployed undetected
```

---

### Principle 8: Audit & Compliance Logging (MANDATORY)

All Terraform executions logged: plan, apply, actor, timestamp, changes.

```bash
# ✅ COMPLIANT: Audit logging
# CI/CD system logs all terraform commands
# Job ID: job-12345
# Actor: devops-bot@example.com
# Timestamp: 2026-02-15T10:30:00Z
# Command: terraform apply tfplan
# Changes: +3 -0 ~1 (3 created, 0 destroyed, 1 modified)

# ✅ COMPLIANT: Change tracking
terraform show  # Display current state

# Sample output:
# resource "aws_db_instance" "prod" {
#   allocated_storage = 100
#   engine             = "postgres"
#   backup_retention_period = 30
#   modified_by = "devops-team"
#   modified_at = "2026-02-15T10:30:00Z"
# }

# ❌ PROHIBITED: Manual terraform apply without logging
# Actor unable to be traced, audit trail loss
```

---

## 4. Control 1: Authentication (Service Account)

**Objective:** Service account credentials authenticated to cloud provider.

### Requirement
- Service account has assume-role trust
- Credentials rotated quarterly
- MFA required for privileged operations

### Compliant Implementation

```bash
# ✅ COMPLIANT: Service account authentication
# AWS: iam.tf
resource "aws_iam_user" "terraform" {
  name = "terraform-core"
}

resource "aws_iam_access_key" "terraform" {
  user = aws_iam_user.terraform.name
  # Access key automatically rotated by AWS
}

# Terraform provider configuration
provider "aws" {
  assume_role {
    role_arn = "arn:aws:iam::ACCOUNT_ID:role/terraform-role"
  }
}

# ✅ COMPLIANT: MFA for sensitive operations
# CI/CD vault stores credentials
# Terraform bot assumes role with time-limited credentials
```

---

## 5. Control 2: Authorization (IAM Policy)

**Objective:** Service account permissions minimal, limited to required resources.

### Requirement
- No wildcard permissions (Action: *)
- Resource-specific ARNs
- Deny-list for sensitive operations

### Compliant Implementation

```json
# ✅ COMPLIANT: Minimal permissions
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:region:account:instance/*"
      ],
      "Condition": {
        "StringEquals": {
          "ec2:instance-type": ["t3.medium"]
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": "ec2:TerminateInstances",
      "Resource": "arn:aws:ec2:region:account:instance/i-prod-*"
    }
  ]
}

# ❌ PROHIBITED: Overpermissioned
# "Action": "*",
# "Resource": "*"
```

---

## 6. Control 3: Versioning (Terraform & Provider Versions)

**Objective:** Pin Terraform and provider versions for reproducibility.

### Requirement
- Terraform version constraint in code
- Provider versions pinned
- Upgrade path documented

### Compliant Implementation

```hcl
# ✅ COMPLIANT: Version constraints
terraform {
  required_version = ">= 1.6.0, < 2.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0, < 6.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.23.0"  # PINNED
    }
  }
}

# ✅ COMPLIANT: Version upgrade procedure
# 1. Run terraform plan with new version locally
# 2. Verify no unexpected changes
# 3. Merge to main, CI/CD applies new version
# 4. Monitor for regressions

# ❌ PROHIBITED: Floating versions
# source  = "hashicorp/aws"
# version = ">= 1.0"  # Latest version, unpredictable changes
```

---

## 7. Control 4: Input Validation (Terraform Variables)

**Objective:** Validate all variable inputs, prevent invalid configuration.

### Requirement
- Type constraints on variables
- Min/max validation rules
- CIDRs, email, ARNs validated

### Compliant Implementation

```hcl
# ✅ COMPLIANT: Variable validation
variable "instance_count" {
  type        = number
  description = "Number of EC2 instances"
  validation {
    condition     = var.instance_count >= 1 && var.instance_count <= 10
    error_message = "instance_count must be between 1 and 10."
  }
}

variable "environment" {
  type        = string
  description = "Environment name"
  validation {
    condition     = contains(["prod", "staging", "dev"], var.environment)
    error_message = "environment must be prod, staging, or dev."
  }
}

variable "cidr_block" {
  type        = string
  description = "VPC CIDR block"
  validation {
    condition     = can(cidrhost(var.cidr_block, 0))
    error_message = "cidr_block must be a valid CIDR notation."
  }
}

# ❌ PROHIBITED: No validation
variable "password" {
  type = string
  # No length validation, complexity check
}
```

---

## 8. Control 5: Rate Limiting (API Call Throttling)

**Objective:** Limit API calls to cloud provider, respect rate limits.

### Requirement
- Retry logic with exponential backoff
- Parallelism limited
- Circuit breaker on sustained errors

### Compliant Implementation

```hcl
# ✅ COMPLIANT: Parallelism limit
terraform apply -parallelism=3
# Max 3 parallel API calls to AWS

# ✅ COMPLIANT: Retry logic (built-in)
provider "aws" {
  max_retries = 3
  # Terraform automatically retries on 429 (rate limit)
}

# ✅ COMPLIANT: Custom retry logic
resource "aws_instance" "web" {
  count = 3
  # Terraform serializes creation due to dependencies
  depends_on = [aws_security_group.web]
}

# ❌ PROHIBITED: No throttling
terraform apply -parallelism=1000
# All resources created simultaneously, API limit exceeded
```

---

## 9. Control 6: Testing & Validation

**Objective:** Test Terraform code before apply, validate resource configuration.

### Requirement
- Unit tests (terratest)
- Integration tests (plan validation)
- Compliance scanning

### Compliant Implementation

```bash
# ✅ COMPLIANT: TFLint validation
tflint . --init
tflint .
# Checks: unused variables, AWS best practices, deprecated args

# ✅ COMPLIANT: Sentinel policy validation
sentinel test
# Policy: storage > 100 GB, encryption enabled, backup retention

# ✅ COMPLIANT: Terratest (Go integration tests)
package test

func TestKubernetesCluster(t *testing.T) {
  opts := &terraform.Options{
    TerraformDir: "../",
  }

  defer terraform.Destroy(t, opts)
  terraform.InitAndApply(t, opts)

  clusterName := terraform.Output(t, opts, "cluster_name")
  assert.NotEmpty(t, clusterName)
}

# ❌ PROHIBITED: No testing
terraform apply
# Untested configuration, runtime errors possible
```

---

## 10. Control 7: Logging & Audit Trail

**Objective:** Log all terraform operations, changes, actors.

### Requirement
- All apply/destroy operations logged
- Actor identification in logs
- Change summaries captured

### Compliant Implementation

```bash
# ✅ COMPLIANT: Terraform logging
export TF_LOG=DEBUG  # Enable debug logging
terraform apply -json 2>&1 | tee apply.log

# Sample log:
{
  "type": "apply_complete",
  "change": {
    "actions": ["create"],
    "type": "aws_db_instance",
    "name": "prod",
    "after": {
      "allocated_storage": 100,
      "engine": "postgres"
    }
  },
  "actor": "devops-bot@example.com",
  "timestamp": "2026-02-15T10:30:00Z"
}

# ✅ COMPLIANT: State file versioning (history)
# S3 backend with versioning enabled
# All state file changes tracked with timestamps
# Can rollback to previous state if needed

# ❌ PROHIBITED: No logging
terraform apply -auto-approve
# No audit trail, changes untracked
```

---

## 11. Control 8: Zero Trust Infrastructure

**Objective:** Explicit resource creation, no implicit defaults, network policies enforced.

### Requirement
- Security groups deny-all by default
- Database backups mandatory
- Encryption enforced

### Compliant Implementation

```hcl
# ✅ COMPLIANT: Default deny security group
resource "aws_security_group" "default" {
  name = "default-deny"

  # EXPLICITLY allow only required traffic
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]  # VPC only
  }

  # DENY all other ingress (implicit)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["10.0.0.0/8"]  # VPC only
  }
}

# ✅ COMPLIANT: Database encryption mandatory
resource "aws_db_instance" "prod" {
  allocated_storage     = 100
  engine               = "postgres"
  storage_encrypted    = true           # MANDATORY
  backup_retention_period = 30          # MANDATORY
  preferred_backup_window = "03:00-04:00"
  multi_az             = true           # High availability
}

# ❌ PROHIBITED: Default allow
resource "aws_security_group" "insecure" {
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow all (!)
  }
}
```

---

## 12. Multi-Tenancy Controls

**Objective:** Separate infrastructure per tenant, no cross-tenant resource sharing.

### Requirement
- Separate AWS accounts or VPCs per tenant
- Terraform workspaces or state files separated
- IAM isolation

### Compliant Implementation

```hcl
# ✅ COMPLIANT: Workspaces per tenant
# terraform workspace new tenant-abc
# terraform workspace select tenant-abc

variable "tenant_id" {
  type        = string
  description = "Tenant identifier"
  default     = terraform.workspace
}

resource "aws_eks_cluster" "tenant" {
  name = "eks-${var.tenant_id}"
  # Each workspace gets isolated cluster
}

# ✅ COMPLIANT: Separate backend per tenant
terraform {
  backend "s3" {
    bucket = "terraform-state-prod"
    key    = "tenants/${var.tenant_id}/terraform.tfstate"
    # State files isolated per tenant
  }
}

# ❌ PROHIBITED: Shared infrastructure
resource "aws_eks_cluster" "shared" {
  name = "shared-cluster"
  # All tenants on same cluster (cross-tenant network access possible)
}
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** Module versioning, dependency locking, pin provider/module versions.

### Requirement
- Terraform modules versioned in registry
- Dependency lock file committed
- GIT commit SHA referenced for custom modules

### Compliant Implementation

```hcl
# ✅ COMPLIANT: Pinned module versions
module "kubernetes" {
  source = "terraform-aws-modules/eks/aws"
  version = "19.16.0"  # SPECIFIC VERSION

  cluster_name = "prod"
}

module "vpc" {
  source = "git::https://github.com/company/terraform-modules.git//vpc?ref=v2.3.0"
  # GIT commit SHA, immutable reference
}

# ✅ COMPLIANT: Dependency lock file
# .terraform.lock.hcl
# provider "aws" {
#   version = "5.23.0"
#   hashes = ["h1:abc123..."]  # Reproducible download
# }

# ❌ PROHIBITED: Floating module versions
module "database" {
  source = "terraform-aws-modules/rds/aws"
  # version unspecified, latest version fetched (unpredictable changes)
}
```

---

## 14. Control Mapping

| EATGF Control | ISO 27001:2022 | NIST SSDF 1.1 | OWASP SAMM | NIST 800-53 | COBIT 2019 |
|---|---|---|---|---|---|
| Service Auth | A.8.2, A.8.5 | AS.1 | Governance.1 | AC-2 | DSS05.01 |
| IAM Policy | A.8.5, A.8.9 | AS.2 | Governance.2 | AC-3, AC-6 | DSS05.03 |
| Version Pinning | A.8.28 | PO.3 | Build.1 | CM-3 | BAI09.02 |
| Input Validation | A.8.22 | PW.8 | Build.2 | CM-5 | DSS05.04 |
| API Throttling | A.8.22 | PW.8 | Verify.1 | SC-5 | DSS01.05 |
| Code Testing | A.8.28 | PO.2 | Build.3 | SA-3 | BAI03.07 |
| Audit Logging | A.8.15, A.8.23 | RV.1 | Verify.3 | AU-2 | MEA01.02 |
| State Encryption | A.8.1, A.8.9 | PW.1 | Build.1 | SC-7 | DSS05.02 |

---

## 15. Developer Checklist

Before running `terraform apply` in production:

- [ ] Terraform version pinned in `required_version`
- [ ] All provider versions pinned (no floating constraints)
- [ ] State backend configured with encryption enabled
- [ ] S3 state bucket has versioning and MFA delete enabled
- [ ] State file locking enabled (DynamoDB)
- [ ] Service account IAM policy is minimal (least privilege)
- [ ] No secrets in `.tfvars` or resource defaults
- [ ] All secrets referenced from external manager (AWS Secrets Manager, Vault)
- [ ] All variables have type constraints and validation rules
- [ ] Terraform validation passes: `terraform validate`
- [ ] TFLint passes: `tflint .`
- [ ] Sentinel policy tests pass
- [ ] `terraform plan` output reviewed in PR
- [ ] PR approved by peer before merge
- [ ] All modules have explicit versions pinned
- [ ] `.terraform.lock.hcl` committed to version control

---

## 16. Governance Implications

**Risk if not implemented:**

- **State File Exposure:** Plaintext secrets in tfstate → credential compromise
- **Infrastructure Drift:** Manual changes outside Terraform → inconsistent state
- **Audit Trail Loss:** No logging of who made changes when
- **Supply Chain Attack:** Unpinned modules → malicious code deployment
- **Privilege Escalation:** Overpermissioned service account → full cloud access

**SOC2/ISO 27001 Impact:**

- **SOC2 CC4.1:** (Data classification) IaC enforces encryption
- **SOC2 CC6.1:** (Access control) IAM policies enforced via code
- **SOC2 CC6.2:** (Change management) All infrastructure changes via versioned code
- **ISO 27001 A.8.28:** (Supply chain) Module versions pinned, auditable

---

## 17. Implementation Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Unencrypted state | CRITICAL | S3 encryption + remote backend mandatory |
| Secrets in code | CRITICAL | External secret manager; tfstate scanning |
| Overpermissioned SA | HIGH | Audit IAM policy; use policy simulator |
| Manual changes | HIGH | Infrastructure policies enforced in PR review |
| Unpinned versions | HIGH | Require all versions pinned in code review |

---

## 18. Official References

**Normative (Governance):**
- NIST SP 800-218: Secure Software Development Framework (SSDF)
- ISO/IEC 27001:2022 Annex A: Control Objectives
- NIST SP 800-53 Rev. 5: Security & Privacy Controls

**Informative (IaC Security):**
- Terraform Official Documentation
- Hashicorp Security Best Practices
- CIS Terraform Benchmark
- OWASP Infrastructure as Code Security

**Tools & Standards:**
- TFLint: Terraform linting
- Sentinel: Policy as Code
- Terratest: Infrastructure testing
- TerraForm Cloud: Remote state management

---

## 19. Version Information

| Field | Value |
|---|---|
| **Document Version** | 1.0 |
| **Change Type** | Major (Initial Release) |
| **Issue Date** | February 15, 2026 |
| **EATGF Baseline** | v1.0 (Layer 08 Infrastructure Runtime) |
| **Terraform Version** | 1.6.0+ |
| **Target Audience** | Platform engineers, DevOps, Infrastructure architects |

**Compliance Statement:** This profile is 100% conformant to EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md and enforces all governance principles at Layer 08, Infrastructure Runtime → Infrastructure as Code Layer.

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)

**Supersedes:** N/A (new document)
**Superseded By:** None (active)
