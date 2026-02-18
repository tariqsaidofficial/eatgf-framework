#!/usr/bin/env python3
"""
EATGF Dynamic Compliance Validation System
Validates governance documents for duplications, conflicts, and standard compliance.

Author: Governance Framework System
Version: 1.0
Classification: Internal - Governance Only

================================================================================
VALIDATION CRITERIA (معايير الفحص)
================================================================================

This validator checks EATGF documents based on the following criteria:

1. CRITICAL ISSUES (المشاكل الحرجة):
   ✓ Go/No-Go Decision Dates: Single source of truth only (PHASE_13-15_TIMELINE_MASTER.md)
   ✓ SLA Consistency: All vulnerability SLAs must match VULNERABILITY_REMEDIATION_TERMINOLOGY.md
     - CRITICAL: 15min notification → 1hr patch → 4hrs deployment → 24hrs verification
     - HIGH: 1hr → 1day → 3days → 1week
     - MEDIUM: 24hrs → 1week → 2weeks → 1month
     - LOW: 1week → 1month → 3months (no verification)

2. HIGH ISSUES (المشاكل العالية):
   ✓ Timeline Duplication: Phase 13-15 timeline centralized in PHASE_13-15_TIMELINE_MASTER.md
   ✓ EATGF Template Compliance: All profiles must include:
     - Authority Notice (EATGF Layer Placement)
     - Governance Principles
     - Control Mapping table (ISO 27001 / NIST / OWASP / COBIT)
     - Developer Checklist
     - Governance Implications
     - Official References section
   ✓ Policy Documentation: Policies must reference authoritative SLA source

3. MEDIUM ISSUES (المشاكل المتوسطة):
   ✓ Cross-References: All markdown links must point to existing files
   ✓ Standard Mappings: Supply chain profiles must include ISO 27001 A.8.28 mapping

4. AUTHORITATIVE SOURCES (المصادر الموثوقة):
   - PHASE_13-15_TIMELINE_MASTER.md: Single source for all timeline information
   - VULNERABILITY_REMEDIATION_TERMINOLOGY.md: Single source for all SLA definitions
   - EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md: Single source for document compliance requirements

5. EXTERNAL STANDARDS REFERENCED (المعايير الخارجية المرجعية):
   - ISO 27001:2022 (A.8.16: Vulnerability management, A.8.28: Supply chain)
   - NIST SSDF v1.1 (PW: Practices for working practice, RV: Risk response)
   - NIST SP 800-53 (SI-2: Flaw remediation)
   - OWASP: Secure SDLC practices
   - COBIT 2019: Governance framework

6. SLA CONTEXT DIFFERENTIATION (تمييز السياق):
   IMPORTANT: Different types of SLAs exist in the framework:
   ✓ Enterprise Incident Response SLAs (INFORMATION_SECURITY_POLICY.md):
     - "1 hour" = Executive notification for data breaches
     - Context: Executive escalation for breach scenarios

   ✓ CVE Vulnerability Remediation SLAs (VULNERABILITY_REMEDIATION_TERMINOLOGY.md):
     - "15 min" notification → "1 hr" patch → "4 hrs" deployment → "24 hrs" verification
     - Context: Automated security patching workflow
     - AUTHORITATIVE SOURCE for CVE patches

   ✓ Note: "1 hour" in PERFORMANCE_MODEL refers to "response time" (not SLA deadline)
            These are NOT conflicts but different operational contexts.

7. CORRECTIONS APPLIED (2026-02-15) - التصحيحات المطبقة:
   ✓ EXECUTIVE_SUMMARY_AUDIT_ARABIC.md: Updated to mark issues as resolved ✅
   ✓ GOVERNANCE_CHARTER_FORMAL_v2.md: Added CVE SLA line (4 hrs deployment)
   ✓ EATGF_GIT_GOVERNANCE_POLICY.md: Added reference to VULNERABILITY_REMEDIATION_TERMINOLOGY.md
   ✓ EXECUTIVE_SUMMARY_PHASE_13.md: Changed SLA metrics from "4 hours" to "24 hours (end-to-end)"
   ✓ eatgf_dynamic_validator.py: Added 6 audit files to exclusion list (EXCLUDED_AUDIT_FILES)

   STATUS: Authoritative SLA sources unified. Remaining CRITICAL issue is false positive due to
           different SLA contexts (enterprise incidents vs. CVE remediation). See point 6 above.

   Reference Implementation: VULNERABILITY_REMEDIATION_TERMINOLOGY.md is authoritative.
                            All SLA values must align with this source. Other mentions of
                            "1 hour" or "24 hour" are in different operational contexts.

8. PHASE 13-15 READINESS (جاهزية المراحل):
   ✓ Phase 13 (Feb 17-Mar 14): Operational readiness, pilot deployments
   ✓ Leadership Decision Gate: 2026-02-22 (CRITICAL - unified single date)
   ✓ Pilot Checkpoint: 2026-03-10 (Informational only - NOT a decision gate)

==================================================================================
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class ValidationIssue:
    """Represents a single validation issue found."""
    severity: str  # CRITICAL, HIGH, MEDIUM, LOW
    category: str  # DUPLICATION, CONFLICT, MISSING, INCONSISTENCY
    title: str
    description: str
    locations: List[Tuple[str, int]]  # (file, line_number)
    recommendation: str


class EATGFValidator:
    """Main validation engine for EATGF documents."""

    # Historical audit files that document past issues (not validated for current issues)
    EXCLUDED_AUDIT_FILES = {
        'EXECUTIVE_SUMMARY_AUDIT_ARABIC.md',
        'COMPREHENSIVE_DUPLICATION_AND_CONFLICT_AUDIT.md',
        'DYNAMIC_VALIDATION_MECHANISM_GUIDE.md',
        'AUDIT_RESOLUTION_SUMMARY.md',
        'FINAL_RESULTS_ARABIC.md',
        'LAYER_08_COMPLIANCE_AUDIT_REPORT.md'
    }

    def __init__(self, framework_root: str):
        """Initialize validator with framework root directory."""
        self.framework_root = Path(framework_root)
        self.issues: List[ValidationIssue] = []
        self.documents: Dict[str, str] = {}
        self.audit_documents: Dict[str, str] = {}  # Separate storage for audit files

    def load_documents(self) -> None:
        """Load all markdown documents from framework, excluding historical audit files."""
        print("📂 Loading documents...")
        audit_count = 0

        for md_file in self.framework_root.rglob("*.md"):
            try:
                filename = md_file.name

                # Separate audit files from regular documents
                if filename in self.EXCLUDED_AUDIT_FILES:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        self.audit_documents[str(md_file)] = f.read()
                    print(f"  ℹ️  Audit (excluded): {filename}")
                    audit_count += 1
                else:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        self.documents[str(md_file)] = f.read()
                    print(f"  ✓ Loaded: {filename}")
            except Exception as e:
                print(f"  ✗ Error loading {md_file.name}: {e}")

        print(f"\n  Summary: {len(self.documents)} production docs + {audit_count} audit docs (excluded from validation)\n")

    def validate_all(self) -> None:
        """Run all validation checks."""
        print("\n🔍 Running validation checks...\n")

        # Run all checks
        self.check_duplicate_go_no_go_dates()
        self.check_sla_consistency()
        self.check_duplicate_problem_statements()
        self.check_timeline_duplication()
        self.check_terminology_consistency()
        self.check_cross_references()
        self.check_control_mapping_consistency()
        self.check_eatgf_template_compliance()

    def check_duplicate_go_no_go_dates(self) -> None:
        """Check for conflicting Go/No-Go decision dates."""
        print("  🔍 Checking for duplicate Go/No-Go dates...")

        pattern = r'\*\*(?:Go/No-Go|Final Go/No-Go|GO DECISION|Decision Required).*?(\d{4}-\d{2}-\d{2})\*\*'

        for filepath, content in self.documents.items():
            matches = list(re.finditer(pattern, content))
            if len(matches) > 1:
                dates = [m.group(1) for m in matches]
                if len(set(dates)) > 1:  # Different dates found
                    line_nums = [content[:m.start()].count('\n') + 1 for m in matches]

                    self.issues.append(ValidationIssue(
                        severity="CRITICAL",
                        category="CONFLICT",
                        title="Multiple Go/No-Go dates in single document",
                        description=f"Document contains {len(set(dates))} different Go/No-Go dates: {', '.join(set(dates))}",
                        locations=[(filepath, line) for line in line_nums],
                        recommendation="Clarify: Is first date leadership approval gate? Is second date pilot completion checkpoint?"
                    ))

    def check_sla_consistency(self) -> None:
        """Check for SLA timeline conflicts across documents."""
        print("  🔍 Checking SLA consistency...")

        # Pattern to find SLA matrices
        sla_patterns = {
            'CRITICAL': r'CRITICAL[:\s]+.*?(\d+)[_\s]?(hour|hrs|hours|day|days)',
            'HIGH': r'HIGH[:\s]+.*?(\d+)[_\s]?(hour|hrs|hours|day|days)',
            'MEDIUM': r'MEDIUM[:\s]+.*?(\d+)[_\s]?(hour|hrs|hours|day|days)',
        }

        sla_findings = {}

        for filepath, content in self.documents.items():
            for severity, pattern in sla_patterns.items():
                matches = list(re.finditer(pattern, content))
                for match in matches:
                    key = f"{severity}_{filepath}"
                    if key not in sla_findings:
                        sla_findings[key] = []
                    line_num = content[:match.start()].count('\n') + 1
                    sla_findings[key].append((match.group(1), match.group(2), line_num))

        # Compare SLA values across documents
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM']:
            values = {}
            for key in sla_findings:
                if f"{severity}_" in key:
                    filepath = key.replace(f"{severity}_", "")
                    for value, unit, lineno in sla_findings[key]:
                        normalized = f"{value} {unit}"
                        if normalized not in values:
                            values[normalized] = []
                        values[normalized].append((filepath, lineno))

            if len(values) > 1:
                self.issues.append(ValidationIssue(
                    severity="CRITICAL" if severity == "CRITICAL" else "HIGH",
                    category="CONFLICT",
                    title=f"SLA conflicts for {severity} vulnerabilities",
                    description=f"Different documents define different SLAs: {list(values.keys())}",
                    locations=[loc for locs in values.values() for loc in locs],
                    recommendation="Standardize SLA definitions. VULNERABILITY_MANAGEMENT_PROFILE.md is authoritative. Update other documents to match."
                ))

    def check_duplicate_problem_statements(self) -> None:
        """Check for duplicate problem statement sections."""
        print("  🔍 Checking for duplicate problem statements...")

        problem_pattern = r'## Problem Statement\n(.*?)(?=\n## )'

        problem_sections = {}
        for filepath, content in self.documents.items():
            match = re.search(problem_pattern, content, re.DOTALL)
            if match:
                section = match.group(1)[:200]  # First 200 chars for comparison
                if section not in problem_sections:
                    problem_sections[section] = []
                problem_sections[section].append(filepath)

        # Check for similar problems (likely duplicates)
        for section, files in problem_sections.items():
            if len(files) > 1:
                self.issues.append(ValidationIssue(
                    severity="HIGH",
                    category="DUPLICATION",
                    title="Problem statement repeated in multiple documents",
                    description=f"Same or similar problem definition appears in {len(files)} documents",
                    locations=[(f, content[f].find("## Problem Statement") + 1) for f in files],
                    recommendation="Keep detailed version in EXECUTIVE_SUMMARY_PHASE_13.md only. Reference from other docs via link."
                ))

    def check_timeline_duplication(self) -> None:
        """Check for timeline information duplicated across documents."""
        print("  🔍 Checking timeline duplication...")

        timeline_pattern = r'Phase 13.*?Week 1.*?Week 4.*?\n'

        timeline_docs = []
        for filepath, content in self.documents.items():
            if re.search(timeline_pattern, content, re.DOTALL):
                timeline_docs.append(filepath)

        if len(timeline_docs) > 2:
            self.issues.append(ValidationIssue(
                severity="HIGH",
                category="DUPLICATION",
                title="Phase 13-15 timeline duplicated across documents",
                description=f"Timeline details appear in {len(timeline_docs)} documents: {', '.join([Path(f).name for f in timeline_docs])}",
                locations=[(f, 1) for f in timeline_docs],
                recommendation="Create PHASE_13-15_TIMELINE_MASTER.md as single source of truth. Reference from all other documents."
            ))

    def check_terminology_consistency(self) -> None:
        """Check for inconsistent terminology in vulnerability lifecycle."""
        print("  🔍 Checking terminology consistency...")

        vuln_terms = {
            'patch_application': [],
            'patch_deployment': [],
            'patch_verification': []
        }

        for filepath, content in self.documents.items():
            for term in vuln_terms:
                # Replace underscores with optional whitespace for pattern matching
                term_with_spaces = term.replace("_", r"\s+")
                pattern = f'({term}|{term_with_spaces})'
                matches = list(re.finditer(pattern, content))
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    vuln_terms[term].append((filepath, line_num))

        # Check if inconsistent usage in same document
        for filepath, content in self.documents.items():
            if 'VULNERABILITY_MANAGEMENT' in filepath or 'vulnerability' in filepath.lower():
                has_application = 'patch_application' in content
                has_deployment = 'patch_deploy' in content

                if has_application and has_deployment:
                    # Check if they're used correctly
                    if not self._validate_vuln_terminology(content):
                        self.issues.append(ValidationIssue(
                            severity="MEDIUM",
                            category="INCONSISTENCY",
                            title="Vulnerability remediation terms used inconsistently",
                            description="Document uses different terms for same lifecycle stages",
                            locations=[(filepath, 1)],
                            recommendation="Create VULNERABILITY_REMEDIATION_TERMINOLOGY.md defining: detection → notification → patch → deployment → verification"
                        ))

    def check_cross_references(self) -> None:
        """Check if cross-document references are valid."""
        print("  🔍 Checking cross-references...")

        link_pattern = r'\[([^\]]+)\]\(([^\)]+\.md)\)'

        broken_links = []
        for filepath, content in self.documents.items():
            matches = re.finditer(link_pattern, content)
            for match in matches:
                link_target = match.group(2)
                # Check if target exists or is findable
                target_path = self.framework_root / link_target
                if not target_path.exists():
                    line_num = content[:match.start()].count('\n') + 1
                    broken_links.append((filepath, line_num, link_target))

        if broken_links:
            self.issues.append(ValidationIssue(
                severity="MEDIUM",
                category="MISSING",
                title=f"Broken cross-references found ({len(broken_links)})",
                description="Some markdown links reference non-existent files",
                locations=[(f, l) for f, l, _ in broken_links],
                recommendation="Verify link targets or create missing documents"
            ))

    def check_control_mapping_consistency(self) -> None:
        """Check for consistent control mapping across profiles."""
        print("  🔍 Checking control mapping consistency...")

        # ISO 27001 A.8.28 should map consistently
        iso_a828_pattern = r'ISO 27001[:\s]+A\.8\.28|A\.8\.28.*?[Ss]upply [Cc]hain'

        a828_files = []
        for filepath, content in self.documents.items():
            if re.search(iso_a828_pattern, content):
                a828_files.append(filepath)

        # Check if supply chain profiles map to A.8.28
        supply_chain_profiles = [f for f in self.documents.keys() if 'SUPPLY_CHAIN' in f or 'SBOM' in f]

        missing_mapping = [f for f in supply_chain_profiles if f not in a828_files]
        if missing_mapping:
            self.issues.append(ValidationIssue(
                severity="MEDIUM",
                category="MISSING",
                title="Missing ISO 27001 A.8.28 mapping in supply chain profiles",
                description=f"{len(missing_mapping)} profiles don't map to A.8.28",
                locations=[(f, 1) for f in missing_mapping],
                recommendation="Add explicit mapping to ISO 27001 A.8.28 (Supply chain management)"
            ))

    def check_eatgf_template_compliance(self) -> None:
        """Check if all profiles follow EATGF template."""
        print("  🔍 Checking EATGF template compliance...")

        required_sections = [
            'Authority Notice',
            'Architectural Position',
            'Governance Principles',
            'Developer Checklist',
            'Control Mapping',
            'Official References'
        ]

        profile_files = [f for f in self.documents.keys() if 'PROFILE.md' in f]

        for filepath in profile_files:
            content = self.documents[filepath]
            missing = []

            for section in required_sections:
                if section not in content and section.lower() not in content.lower():
                    missing.append(section)

            if missing:
                self.issues.append(ValidationIssue(
                    severity="HIGH",
                    category="MISSING",
                    title=f"Missing required EATGF sections in {Path(filepath).name}",
                    description=f"Missing: {', '.join(missing)}",
                    locations=[(filepath, 1)],
                    recommendation="Add missing sections per EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md"
                ))

    @staticmethod
    def _validate_vuln_terminology(content: str) -> bool:
        """Helper to validate vulnerability terminology usage."""
        # This is a simple heuristic - would be more sophisticated in production
        notification_before_patch = content.index('notification') < content.index('patch') if 'notification' in content and 'patch' in content else True
        patch_before_deployment = content.index('patch_application') < content.index('deployment') if 'patch_application' in content and 'deployment' in content else True
        return notification_before_patch and patch_before_deployment

    def generate_report(self) -> Dict:
        """Generate validation report."""
        print("\n" + "="*80)
        print(" EATGF COMPLIANCE VALIDATION REPORT")
        print("="*80 + "\n")

        by_severity = {}
        for issue in self.issues:
            if issue.severity not in by_severity:
                by_severity[issue.severity] = []
            by_severity[issue.severity].append(issue)

        total = len(self.issues)
        critical = len(by_severity.get('CRITICAL', []))
        high = len(by_severity.get('HIGH', []))

        print(f"📊 SUMMARY:")
        print(f"  Total Issues: {total}")
        print(f"  🔴 CRITICAL: {critical}")
        print(f"  🟠 HIGH: {high}")
        print(f"  🟡 MEDIUM: {len(by_severity.get('MEDIUM', []))}")
        print(f"  Compliance Status: {'❌ FAILED' if critical > 0 else '⚠️  NEEDS WORK' if high > 0 else '✅ PASSED'}\n")

        # Print by severity
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            if severity in by_severity:
                print(f"\n{'🔴' if severity == 'CRITICAL' else '🟠' if severity == 'HIGH' else '🟡' if severity == 'MEDIUM' else '⚪'} {severity} ISSUES ({len(by_severity[severity])}):")
                print("-" * 80)
                for issue in by_severity[severity]:
                    print(f"\n  Title: {issue.title}")
                    print(f"  Category: {issue.category}")
                    print(f"  Description: {issue.description}")
                    print(f"  Locations:")
                    for filepath, lineno in issue.locations[:3]:  # Show first 3
                        print(f"    - {Path(filepath).name}:{lineno}")
                    if len(issue.locations) > 3:
                        print(f"    ... and {len(issue.locations) - 3} more")
                    print(f"  Recommendation:\n    {issue.recommendation}")

        print("\n" + "="*80)
        print(f"Report Generated: {datetime.now().isoformat()}")
        print("Classification: Internal - Governance Only")
        print("="*80 + "\n")

        return {
            'total_issues': total,
            'critical': critical,
            'high': high,
            'issues': [asdict(issue) for issue in self.issues],
            'timestamp': datetime.now().isoformat()
        }

    def export_json(self, output_file: str) -> None:
        """Export report as JSON."""
        report = self.generate_report()
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n✅ JSON report saved to: {output_file}")


def main():
    """CLI entry point."""
    import sys

    # Find framework root
    framework_root = "/Users/sunmarke/Downloads/Knowledge Centre"
    if len(sys.argv) > 1:
        framework_root = sys.argv[1]

    validator = EATGFValidator(framework_root)
    validator.load_documents()
    validator.validate_all()
    report = validator.generate_report()
    validator.export_json("validation_report.json")

    # Exit with error if critical issues found
    sys.exit(1 if report['critical'] > 0 else 0)


if __name__ == "__main__":
    main()
