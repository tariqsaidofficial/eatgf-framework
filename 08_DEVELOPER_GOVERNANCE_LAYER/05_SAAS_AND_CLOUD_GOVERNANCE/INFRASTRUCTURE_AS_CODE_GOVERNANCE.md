# Infrastructure as Code Governance Standard

| Field          | Value                                                        |
| -------------- | ------------------------------------------------------------ |
| Document Type  | Implementation Standard                                      |
| Version        | 1.0                                                          |
| Classification | Controlled                                                   |
| Effective Date | 2026-02-16                                                   |
| Authority      | Chief Technology Officer                                     |
| EATGF Layer    | 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE |
| MCM Reference  | EATGF-CLD-ARCH-01                                            |

---

## Purpose

Define security and governance requirements for Infrastructure as Code (Terraform, CloudFormation, Helm, Kustomize) ensuring infrastructure changes are auditable, tested, peer-reviewed, and comply with organizational security baselines.

**Mandatory for:** All cloud infrastructure; Kubernetes configurations; container orchestration.

## Architectural Position

**EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 05_SAAS_AND_CLOUD_GOVERNANCE

- **Upstream dependency:** CI/CD Security Architecture (03_DEVSECOPS_GOVERNANCE); Layer 04 Information Security Policy
- **Downstream usage:** IaC code reviewed, tested, deployed through secure pipelines
- **Cross-layer reference:** Maps to NIST CSF, ISO 27001 A.8.1 (infrastructure security)

## Governance Principles

1. **Code-First Infrastructure** – All infrastructure defined in version-controlled code; no manual configuration
2. **Policy as Code** – Infrastructure compliance validated by code policies (OPA/Rego, Kyverno)
3. **Separation of Concerns** – Environment configs separate; testing/staging/prod isolated by code
4. **GitOps Model** – Git is source of truth; deployment automated from Git state

## Technical Implementation

### IaC Tool Requirements

**Standard Tools:**

- **Terraform:** Multi-cloud; pure IaC
- **CloudFormation:** AWS-native; template-based
- **Helm:** Kubernetes package manager
- **Kustomize:** Kubernetes customization
- **Pulumi:** Programmatic IaC

**Mandatory Requirements:**

- Terraform state backend encrypted and replicated (S3, Terraform Cloud)
- State file versioning; never delete history
- Variable separation: secrets in vault, not code
- Module registry: approved modules only (private registry)

### Version Control

```yaml
# Terraform project structure
infrastructure/
├── modules/
│   ├── compute/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── networking/
│   └── storage/
├── environments/
│   ├── dev/
│   │   ├── terraform.tfvars  # Dev overrides
│   │   └── main.tf
│   ├── staging/
│   └── prod/
│       ├── terraform.tfvars  # Prod overrides; encrypted
│       └── main.tf
├── .gitignore  # Never commit: .tfstate, .tfvars with secrets
└── README.md
```

**Git Requirements:**

- All .tf files in Git
- terraform.tfvars for prod environment encrypted
- State files never in Git

### Policy as Code

```regex
# OPA/Rego policy: enforce security baselines
package infrastructure

deny[msg] {
    input.resource_type == "aws_s3_bucket"
    not input.versioning[0].enabled
    msg := "S3 bucket must have versioning enabled"
}

deny[msg] {
    input.resource_type == "aws_rds_instance"
    input.publicly_accessible
    msg := "RDS instance must not be publicly accessible"
}

deny[msg] {
    input.resource_type == "aws_security_group"
    rule := input.ingress[_]
    rule.from_port == 0
    rule.to_port == 65535
    rule.cidr_blocks[_] == "0.0.0.0/0"
    msg := "Security group must not allow unrestricted access"
}
```

**Kubernetes Policy (Kyverno):**

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-image-registry
spec:
  validationFailureAction: enforce
  rules:
    - name: check-registry
      match:
        resources:
          kinds:
            - Pod
      validate:
        message: "Images must come from approved registry"
        pattern:
          spec:
            containers:
              - image: "*.myregistry.com/*"
```

### Testing and Validation

**Terraform Validation:**

```bash
# Syntax check
terraform fmt -check -recursive
terraform validate

# Linting
tflint --format json --disable-rule=aws_instance_invalid_type

# Policy validation
conftest test -p policies/ terraform.tfplan

# Cost estimation
terraform plan -out=tfplan
terraform show tfplan | grep -i "will be created"

# Security scanning
checkov -d . --framework terraform
```

**Kubernetes Manifest Validation:**

```bash
# Lint manifests
kubeval manifests/*.yaml
kubelinter lint manifests/*.yaml

# Policy check
kyverno apply /policies --resource manifests/*.yaml
```

### Deployment Pipeline

```yaml
# GitHub Actions: IaC deployment
- name: Infrastructure plan
  run: |
    terraform plan -out=tfplan
    terraform show tfplan > plan-summary.txt

- name: Policy validation
  run: |
    conftest test -p policies/ tfplan
    checkov -f tfplan

- name: Manual approval
  if: github.ref == 'refs/heads/main'
  uses: pullrequest/approve-deploy
  with:
    environment: production

- name: Apply
  if: github.event.review.state == 'approved'
  run: terraform apply tfplan
```

### State Management

**Terraform State:**

```bash
# Remote state with encryption
terraform {
  backend "s3" {
    bucket         = "terraform-state-prod"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

# State locking (prevent concurrent applies)
# DynamoDB table with LockID primary key

# State file access control
# S3 bucket policy: only service account access
```

### Drift Detection

```yaml
# Scheduled drift detection
drift_scan:
  trigger: daily
  script: |
    terraform refresh
    terraform plan -out=drift.tfplan

    if [ ! -z "$(terraform show -json drift.tfplan)" ]; then
      alert "Infrastructure drift detected"
      create_github_issue "Infrastructure drift"
    fi
```

## Control Mapping

| EATGF Context  | ISO 27001:2022 | NIST      | COBIT        |
| -------------- | -------------- | --------- | ------------ |
| IaC governance | A.8.1, A.12.1  | CSF ID/PR | BAI01, BAI06 |
| Policy as code | A.8.1, A.5.1   | CSF PR/DE | BAI01.02     |

## Developer Checklist

- [ ] Terraform project structure created
- [ ] State backend encrypted and configured
- [ ] Module library established (private registry)
- [ ] OPA/Rego policies defined
- [ ] Linting and validation gates in CI/CD
- [ ] Manual approval workflow for prod changes
- [ ] Drift detection automated
- [ ] Team training completed
- [ ] Version control committed

## Version History

| Version | Date       | Change Type | Description                     |
| ------- | ---------- | ----------- | ------------------------------- |
| 1.0     | 2026-02-16 | Major       | Initial IaC governance standard |
