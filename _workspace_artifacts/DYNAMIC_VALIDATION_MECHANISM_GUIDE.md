# EATGF Dynamic Validation Mechanism

## Automated Compliance Checking System

**Version:** 1.0
**Status:** Ready for Phase 13 Integration
**Authority:** Governance Framework Validation System

---

## Overview

The EATGF Dynamic Validator is an automated Python script that continuously checks governance documents for:

✅ **Duplication detection** (problem statements, timelines, duplicated controls)
✅ **Conflict resolution** (SLA mismatches, timeline contradictions, competing definitions)
✅ **Template compliance** (all profiles follow EATGF signature template)
✅ **Cross-reference validation** (no broken links between documents)
✅ **Terminology consistency** (vulnerability lifecycle stage names)
✅ **Authority hierarchy** (control mapping hierarchy vs baseline)

---

## How It Works

### 1. Validation Checks (8 categories)

| Check                            | What It Validates                                 | Severity If Fails |
| -------------------------------- | ------------------------------------------------- | ----------------- |
| **Duplicate Go/No-Go Dates**     | Single document has multiple decision dates       | CRITICAL          |
| **SLA Consistency**              | Vulnerability SLA timelines match across docs     | CRITICAL          |
| **Duplicate Problem Statements** | Same problem described multiple places            | HIGH              |
| **Timeline Duplication**         | Phase 13-15 timeline repeated in 3+ docs          | HIGH              |
| **Terminology Consistency**      | Vulnerability lifecycle stages named consistently | MEDIUM            |
| **Cross-References**             | All .md links point to real files                 | MEDIUM            |
| **Control Mapping**              | ISO/NIST/OWASP controls mapped consistently       | MEDIUM            |
| **EATGF Template**               | All profiles have required sections               | HIGH              |

### 2. Severity Classification

```
🔴 CRITICAL → Must fix before leadership decision (2026-02-22)
🟠 HIGH    → Must fix before pilot deployment (2026-03-15)
🟡 MEDIUM  → Must fix before production (2026-04-15)
⚪ LOW     → Backlog for post-Phase 15
```

### 3. Output Format

The validator produces:

- **Console output:** Real-time issue reporting with file locations
- **JSON export:** Machine-readable report for CI/CD integration
- **Exit codes:** 0 (pass) or 1 (fail with critical issues)

---

## Installation & Usage

### Prerequisites

```bash
Python 3.8+
```

### Run Validation

```bash
# Validate current framework
python3 eatgf_dynamic_validator.py

# Validate specific directory
python3 eatgf_dynamic_validator.py /path/to/framework

# Export JSON report
python3 eatgf_dynamic_validator.py && cat validation_report.json
```

### Example Output

```
════════════════════════════════════════════════════════════════════════════════
 EATGF COMPLIANCE VALIDATION REPORT
════════════════════════════════════════════════════════════════════════════════

📊 SUMMARY:
  Total Issues: 7
  🔴 CRITICAL: 2
  🟠 HIGH: 3
  🟡 MEDIUM: 2
  Compliance Status: ❌ FAILED

🔴 CRITICAL ISSUES (2):
────────────────────────────────────────────────────────────────────────────────

  Title: Multiple Go/No-Go dates in single document
  Category: CONFLICT
  Description: Document contains 2 different Go/No-Go dates: 2026-02-22, 2026-03-10
  Locations:
    - PHASE_13_IMPLEMENTATION_ROADMAP.md:43
    - PHASE_13_IMPLEMENTATION_ROADMAP.md:375
  Recommendation:
    Clarify: Is first date leadership approval gate? Is second date pilot completion checkpoint?

  [... 6 more issues listed ...]
```

---

## Integration Points

### Pre-Commit Hook

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
echo "Running EATGF validation..."
python3 eatgf_dynamic_validator.py
if [ $? -ne 0 ]; then
  echo "❌ Validation failed. Fix issues before committing."
  exit 1
fi
```

### CI/CD Pipeline (GitHub Actions)

```yaml
name: EATGF Validation
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: python3 eatgf_dynamic_validator.py
      - name: Export report
        if: always()
        run: |
          python3 eatgf_dynamic_validator.py
          cat validation_report.json | jq '.'
```

### Weekly Automated Check

```bash
# Add to crontab
0 9 * * 1 /usr/bin/python3 /path/to/eatgf_dynamic_validator.py >> /var/log/eatgf_validation.log 2>&1
```

---

## Remediation Workflow

### Step 1: Run Validation

```bash
python3 eatgf_dynamic_validator.py
```

### Step 2: Review CRITICAL Issues

(Must fix for 2026-02-22 meeting)

```
🔴 CRITICAL Example: SLA Conflict
  File: FRAMEWORK_COMPLETION_SUMMARY.md:147
  Issue: CRITICAL vulnerability remediation time is 24 hours, but profile says 4 hours
  Fix: Update line 147 from "deployment: 24_hours" to "deployment: 4_hours"
```

### Step 3: Review HIGH Issues

(Must fix for pilot deployment)

```
🟠 HIGH Example: Duplicate Problem Statements
  Files: EXECUTIVE_SUMMARY_PHASE_13.md, PHASE_13_STRATEGIC_RECOMMENDATIONS.md
  Issue: Same 4-gap problem description in 2 documents
  Fix: Keep in EXECUTIVE, add link in STRATEGIC
```

### Step 4: Fix & Re-Validate

```bash
# Edit files per recommendations
vim FRAMEWORK_COMPLETION_SUMMARY.md

# Re-run validation
python3 eatgf_dynamic_validator.py
```

### Step 5: Verify Compliance

Target: ✅ PASSED (0 CRITICAL, 0 HIGH)

---

## Custom Rules (For Phase 14+)

Extend the validator with custom checks:

```python
class EnhancedValidator(EATGFValidator):
    def check_custom_rule(self):
        """Add your custom validation rule."""
        # Your logic here
        self.issues.append(ValidationIssue(...))
```

---

## Limitations & Future Enhancements

### Current Limitations

- Simple regex-based matching (not AST parsing)
- Cannot detect semantic duplications (similar but not identical text)
- Manual review still required for complex governance issues

### Phase 14 Enhancements

1. **Semantic similarity detection** (identifies similar problem statements)
2. **Authority hierarchy validation** (ensures only authoritative sources define controls)
3. **Version drift detection** (e.g., NIST SP 800-53 Rev 5 vs Rev 4)
4. **Tool version consistency** (Cosign 2.1.0 referenced vs 2.0.0)
5. **SLA breach prediction** (detects if timelines are achievable)

### Phase 15+ Enhancements

1. **Real-time dashboard** (compliance metrics by document, team, framework layer)
2. **Historical tracking** (issues fixed per week, compliance trend chart)
3. **Audit trail integration** (links each issue to PR/commit that introduced it)
4. **ML-powered categorization** (auto-categorizes new issues by historical patterns)

---

## Authority & Governance

**Authority Notice:**
This validator implements EATGF Layer 06 (Audit & Assurance) controls for automated compliance checking. It does NOT override human judgment or governance decisions. All CRITICAL/HIGH issues require manual review and approval before remediation.

**Control Mapping:**
| EATGF Control | ISO 27001 | NIST SSDF | Authority |
|---|---|---|---|
| Automated Compliance Check | A.8.15 | MEA01 | Audit & Assurance |
| Issue Detection & Classification | A.8.16 | MEA02 | Audit & Assurance |
| Remediation Tracking | A.8.17 | MEA03 | Audit & Assurance |

---

## Support & Escalation

### Common Issues

**Error: "Module not found"**

```bash
pip install python-dateutil  # If needed
python3 eatgf_dynamic_validator.py
```

**Error: "Permission denied"**

```bash
chmod +x eatgf_dynamic_validator.py
python3 eatgf_dynamic_validator.py  # Run as Python, not bash
```

**Error: "Cannot find documents"**

```bash
# Ensure you're in correct directory
cd /Users/sunmarke/Downloads/Knowledge\ Centre
python3 eatgf_dynamic_validator.py
```

### Escalation Path

1. **Technical Issue:** Open issue in framework repository
2. **Governance Question:** Contact Compliance Officer
3. **Authority Conflict:** Escalate to CISO/CTO

---

## Next Review Points

- **2026-02-16:** Re-validate after corrections (target: 0 CRITICAL)
- **2026-02-22:** Final validation before leadership meeting
- **2026-03-10:** Pilot completion validation
- **2026-03-15:** Phase 13 completion validation
- **2026-04-15:** Phase 14 completion validation
- **Weekly:** Automated check runs every Monday 9 AM

---

**Classification:** Internal - Governance Only
**Last Updated:** 2026-02-15
**Next Update:** Post Phase 13 launch
