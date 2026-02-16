# Terraform Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Infrastructure-as-Code (IaC) using Terraform. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Terraform codifies Secure SDLC (Layer 01), DevSecOps (Layer 03), and Infrastructure Runtime (Layer 04) requirements.

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 04_INFRASTRUCTURE_RUNTIME (Primary) + Layer 01 (Secure SDLC) + Layer 03 (DevSecOps)
- **Governance Scope:** Implementation Standard for Infrastructure-as-Code
- **Control Authority:** Implements controls from MASTER_CONTROL_MATRIX via Secure SDLC, DevSecOps, and Cloud Governance standards

---

## Governance Principles

This profile enforces:

- **Security-by-Design:** Remote encrypted state, secrets externalization
- **Control-Centric Architecture:** 8 mandatory controls + policy validation
- **Versioned Governance:** Provider/Terraform version pinning, lock files
- **Developer-Operational Alignment:** Code review before apply, GitOps approval
- **Audit Traceability:** State file versioning, change history, actor tracking
- **Single Source of Truth:** Version-controlled infrastructure code (no manual changes)

---

## Control Mapping

| EATGF Control                | ISO 27001:2022 | NIST SSDF | OWASP SAMM | COBIT |
| ---------------------------- | -------------- | --------- | ---------- | ----- |
| Authentication (Assume-Role) | A.8.2          | PW.4      | ASVS V1    | APO13 |
| Authorization (IAM Policy)   | A.8.2          | PW.4      | ASVS V4    | APO13 |
| Version Pinning              | A.8.22         | PW.8      | Build.1    | DSS05 |
| Input Validation             | A.8.9          | PW.8      | ASVS V5    | CM-6  |
| Policy Enforcement           | A.8.22         | PW.8      | Build.2    | DSS05 |
| State File Encryption        | A.8.24         | PW.4      | ASVS V2    | IA-5  |
| Backup & DR                  | A.8.13         | PW.8      | Verify.2   | CM-3  |
| Audit Logging                | A.8.15         | RV.1      | Verify.1   | MEA01 |

---

## Purpose

Define governance controls for Infrastructure-as-Code (IaC) using Terraform to ensure immutable deployments, policy enforcement, and auditability across cloud environments.

**Applies to:**

- AWS, GCP, Azure infrastructure
- Networking, security groups, IAM
- Database provisioning
- Monitoring & alerting infrastructure
- All infrastructure managed via Terraform

---

## Technical Implementation

### Provider & Version Pinning

```hcl
#  COMPLIANT: Explicit provider versions + lock file
terraform {
  required_version = ">= 1.5.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.20"  # Allow 5.20.x but not 5.21+
    }
    postgresql = {
      source  = "cyrilgdn/postgresql"
      version = "~> 1.22"
    }
  }

  # Remote state with encryption
  backend "s3" {
    bucket         = "terraform-state-prod"
    key            = "app/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true  # Enable state file encryption
    dynamodb_table = "terraform-locks"  # Prevent concurrent applies
  }
}

provider "aws" {
  region = "us-east-1"

  assume_role {
    role_arn = "arn:aws:iam::${var.aws_account}:role/TerraformRole"
    duration = "1h"  # Time-limited credentials
  }

  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Repository  = "github.com/org/infrastructure"
      Applied      = timestamp()
    }
  }
}
```

### Secrets Externalization

```hcl
#  COMPLIANT: Secrets from AWS Secrets Manager/Vault, never in code
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "prod/rds/master_password"
}

data "aws_secretsmanager_secret_version" "api_key" {
  secret_id = "prod/third_party/api_key"
}

resource "aws_db_instance" "main" {
  db_name               = var.db_name
  master_username       = "postgres"
  master_password       = jsondecode(
    data.aws_secretsmanager_secret_version.db_password.secret_string
  ).password

  skip_final_snapshot   = false
  final_snapshot_identifier = "${var.app_name}-final-${timestamp()}"
  backup_retention_period = 30

  # Encryption at rest
  storage_encrypted     = true
  kms_key_id           = aws_kms_key.rds.arn
}

resource "aws_rds_cluster_parameter_group" "audit" {
  family = "aurora-postgresql14"

  parameter {
    name  = "log_statement"
    value = "all"  # Audit all statements
  }

  parameter {
    name  = "log_min_duration_statement"
    value = "-1"  # Log all statements regardless of duration
  }
}
```

### Policy Enforcement (Sentinel)

```hcl
#  COMPLIANT: Sentinel policy prevents non-compliant resources
# policy.sentinel

import "tfplan/v2" as tfplan

# Deny resources without required tags
allowed_tags = ["Environment", "ManagedBy", "CostCenter"]

has_required_tags = rule {
  all tfplan.resource_changes as resource {
    resource.change.after.tags contains all allowed_tags
  }
}

main = rule {
  has_required_tags
}

# Deny insecure security group rules
deny_public_security_groups = rule {
  all tfplan.resource_changes[
    "aws_security_group"
  ] as security_group {
    not any security_group.change.after.ingress as rule {
      rule.cidr_blocks[0] == "0.0.0.0/0"
    }
  }
}
```

### Testing with Terratest

```go
//  COMPLIANT: Go testing framework for IaC
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestTerraformExample(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../",
        Vars: map[string]interface{}{
            "environment": "test",
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    dbEndpoint := terraform.Output(t, terraformOptions, "db_endpoint")
    assert.Contains(t, dbEndpoint, ".rds.amazonaws.com")

    securityGroupId := terraform.Output(t, terraformOptions, "security_group_id")
    assert.NotEmpty(t, securityGroupId)
}
```

---

## Developer Checklist

- [ ] `terraform init` uses S3 backend with encryption enabled
- [ ] `.terraform.lock.hcl` committed to git (version lock)
- [ ] All provider versions explicitly pinned (no "latest")
- [ ] `terraform fmt` applied (consistent formatting)
- [ ] `terraform validate` passes
- [ ] `tflint` runs in CI/CD with no warnings
- [ ] Sentinel policies enforced (tags, security groups, encryption)
- [ ] `terraform plan` reviewed before `terraform apply`
- [ ] All secrets sourced from Secrets Manager/Vault (never in code)
- [ ] `terraform apply` locked (DynamoDB table prevents concurrent runs)
- [ ] Drift detection enabled (regular `terraform plan` validation)
- [ ] Terratest unit tests pass for infrastructure code
- [ ] State file backups enabled with 30-day retention
- [ ] Audit logging enabled for all API calls (CloudTrail)
- [ ] Pull request approval required before `apply` (branch protection)

---

## Governance Implications

### Risk if Not Implemented

- **Configuration Drift:** Manual changes untracked → infrastructure inconsistent
- **Privilege Escalation:** No time-limited credentials → assume-role compromised indefinitely
- **Secret Exposure:** Hardcoded secrets in code → git history compromised
- **Uncontrolled Destruction:** No lock → concurrent apply causes conflicts
- **Unrecoverable State:** State file loss → infrastructure unmanaged

### Operational Impact

- State file corruption → entire infrastructure undeployable
- Terraform version mismatch → apply failures in production
- Missing Sentinel policies → insecure resources deployed
- No audit trail → cannot debug deployment issues

### Audit Consequences

- **ISO 27001 A.8.2:** Access control audit trail missing
- **SOC2 CC6.2:** Configuration change management failure
- **PCI-DSS 6.5.9:** Infrastructure code review requirement not met

### Cross-Team Dependencies

- Platform team: Must operate S3 state backend + DynamoDB locks
- Security team: Must define Sentinel policies + approval gates
- DevOps team: Must enforce CI/CD Terraform workflow
- Development team: Must write infrastructure code, review plans

---

## Official References

- Terraform Official Docs: <https://www.terraform.io/docs/>
- NIST SP 800-218: Secure Software Development Framework
- HashiCorp Sentinel: <https://www.terraform.io/cloud-docs/policy-enforcement/sentinel/>
- Terratest: <https://terratest.gruntwork.io/>
- AWS Secrets Manager: <https://docs.aws.amazon.com/secretsmanager/>

---

## Version Information

- **Version:** 1.0
- **Change Type:** Major (Initial Release)
- **Date:** 2026-02-15
- **Status:** Published
- **Target Audience:** Infrastructure engineers, platform teams, DevOps
- **Terraform Version:** 1.5+
- **Cloud Providers:** AWS, GCP, Azure

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)
