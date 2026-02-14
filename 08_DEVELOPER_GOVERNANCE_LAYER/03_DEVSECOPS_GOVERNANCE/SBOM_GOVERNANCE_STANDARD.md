# SBOM Governance Standard

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 03_DEVSECOPS_GOVERNANCE
**Governance Scope:** Implementation Standard
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 03_DEVSECOPS_GOVERNANCE

**Governance Scope:** Software Bill of Materials (SBOM) generation, storage, distribution, and consumption standards.

**Control Authority Relationship:** Implements:

- Layer 02: Asset Management Controls
- Layer 04: Information Security Policy
- NTIA Minimum Elements for SBOM, EO 14028

## Purpose

This standard defines requirements for SBOM generation and management. It covers:

- SBOM format and content requirements
- SBOM generation automation
- SBOM storage and distribution
- SBOM consumption for vulnerability tracking
- Compliance with regulatory requirements

## Governance Principles

- **Control-Centric Architecture:** SBOMs enable vulnerability and license tracking
- **Security-by-Design:** SBOMs generated automatically in CI/CD
- **Developer-Operational Alignment:** Automated SBOM generation without manual effort
- **Audit Traceability:** SBOMs provide component inventory for audit

## SBOM Requirements

### NTIA Minimum Elements

**Requirement:** All SBOMs must include NTIA minimum elements.

**Required Fields:**

| Element                 | Description                | Example                                              |
| ----------------------- | -------------------------- | ---------------------------------------------------- |
| Supplier Name           | Component provider         | Apache Software Foundation                           |
| Component Name          | Name of software component | log4j-core                                           |
| Version                 | Component version          | 2.17.1                                               |
| Component Hash          | Cryptographic hash         | SHA-256: a1b2c3...                                   |
| Unique Identifier       | CPE, PURL, or SWID         | pkg:maven/org.apache.logging.log4j/log4j-core@2.17.1 |
| Dependency Relationship | Direct or transitive       | Direct                                               |
| Author of SBOM          | Tool or organization       | Syft v0.68.0                                         |
| Timestamp               | SBOM generation time       | 2026-02-14T12:00:00Z                                 |

### Supported SBOM Formats

**Requirement:** Generate SBOMs in standard, machine-readable formats.

**Approved Formats:**

| Format        | Use Case                         | Specification                 |
| ------------- | -------------------------------- | ----------------------------- |
| **SPDX**      | ISO/IEC standard, broad adoption | SPDX 2.3+ (JSON or tag-value) |
| **CycloneDX** | OWASP standard, VEX support      | CycloneDX 1.4+ (JSON or XML)  |

**Developer Requirements:**

- Use SPDX or CycloneDX format (both acceptable)
- Generate in JSON format (preferred for automation)
- Include SPDX or CycloneDX schema version
- Validate SBOM against schema before publishing

### SBOM Content Requirements

**Requirement:** SBOMs must comprehensively document all components.

**Inclusion Scope:**

- All direct dependencies (explicitly declared)
- All transitive dependencies (indirect)
- Operating system packages (if containerized)
- Runtime dependencies (interpreters, frameworks)
- Build tools (if included in artifact)

**Exclusion Scope:**

- Development-only dependencies (e.g., test frameworks, linters) – optional to include

**Developer Requirements:**

- Generate SBOM for every build artifact
- Update SBOM when dependencies change
- Document SBOM scope and exclusions in metadata

## SBOM Generation

### Automated Generation

**Requirement:** Automate SBOM generation in CI/CD pipeline.

**CI/CD Integration:**

```yaml
# Example GitHub Actions workflow
- name: Generate SBOM
  run: |
    syft dir:. -o spdx-json=sbom.spdx.json
    syft dir:. -o cyclonedx-json=sbom.cdx.json

- name: Validate SBOM
  run: |
    # Validate SPDX
    java -jar spdx-tools.jar Verify sbom.spdx.json

- name: Upload SBOM
  uses: actions/upload-artifact@v3
  with:
    name: sbom
    path: sbom.*
```

**Developer Requirements:**

- SBOM generation is mandatory step in build pipeline
- Fail build if SBOM generation fails
- Validate SBOM against schema
- Upload SBOM to artifact repository

### SBOM Generation Tools

**Approved Tools:**

| Tool                    | Languages/Ecosystems       | Format Support  | Features                 |
| ----------------------- | -------------------------- | --------------- | ------------------------ |
| **Syft**                | Multi-language, containers | SPDX, CycloneDX | Fast, accurate           |
| **CycloneDX CLI**       | Maven, npm, NuGet, etc.    | CycloneDX       | Ecosystem plugins        |
| **SPDX SBOM Generator** | Multi-language             | SPDX            | Reference implementation |
| **Tern**                | Container images           | SPDX            | Layer-by-layer analysis  |

**Developer Requirements:**

- Use approved SBOM generation tool
- Keep tool updated to latest version
- Configure tool for comprehensive dependency detection

## SBOM Storage and Distribution

### SBOM Storage

**Requirement:** Store SBOMs in artifact repository alongside artifacts.

**Storage Location:**

- Same repository as build artifacts
- Same versioning scheme as artifacts
- Separate SBOM file per artifact (e.g., `myapp-v1.0.0-sbom.spdx.json`)

**Developer Requirements:**

- Upload SBOM automatically in CI/CD pipeline
- Tag SBOM with same version as artifact
- Retain SBOMs for same duration as artifacts (minimum 7 years for regulated industries)

### SBOM Distribution

**Requirement:** Provide SBOMs to customers and stakeholders as appropriate.

**Distribution Channels:**

| Audience           | Distribution Method                  | Access Control          |
| ------------------ | ------------------------------------ | ----------------------- |
| Internal teams     | Internal artifact repository         | Role-based              |
| External customers | Download link, product documentation | Public or authenticated |
| Regulators         | Upon request                         | Secure transfer         |

**Developer Requirements (Commercial Software):**

- Provide SBOM to customers upon request or with product delivery
- Include SBOM download link in product documentation
- Ensure SBOM is current and accurate

**Developer Requirements (Open Source):**

- Publish SBOM in GitHub Releases or equivalent
- Include SBOM in package metadata if supported by ecosystem

## SBOM Consumption

### Vulnerability Tracking

**Requirement:** Use SBOMs for continuous vulnerability monitoring.

**Process:**

1. Ingest SBOM into vulnerability management system
2. Match SBOM components against vulnerability databases (NVD, GitHub Advisory, OSV)
3. Alert on newly disclosed vulnerabilities affecting production components
4. Prioritize remediation based on exploitability and exposure

**Recommended Tools:**

- Grype (vulnerability scanner for SBOMs)
- Dependency-Track (SBOM and vulnerability management platform)
- Cloud provider services (AWS Inspector, Azure Defender)

**Developer Requirements:**

- Ingest SBOM into vulnerability management system on deployment
- Monitor for new vulnerabilities daily
- Alert engineering team on critical/high vulnerabilities
- Track remediation in issue tracker

### License Compliance

**Requirement:** Use SBOMs for license compliance tracking.

**Process:**

1. Extract license information from SBOM
2. Identify problematic licenses (GPL, AGPL if proprietary software)
3. Review license compatibility with product license
4. Generate license report for legal review

**Developer Requirements:**

- Include license information in SBOM
- Review license compliance before release
- Document license exceptions or approvals

### Incident Response

**Requirement:** Use SBOMs for rapid incident response.

**Use Cases:**

- Identify systems using vulnerable component (e.g., Log4Shell)
- Locate all instances of compromised dependency
- Assess blast radius of supply chain attack

**Developer Requirements:**

- Maintain searchable SBOM database
- Enable rapid component search across all deployed systems
- Use SBOM to identify affected systems within hours of vulnerability disclosure

## SBOM Quality and Validation

### SBOM Validation

**Requirement:** Validate SBOM completeness and accuracy.

**Validation Checks:**

- SBOM conforms to SPDX or CycloneDX schema
- All NTIA minimum elements present
- Component versions match actual deployed versions
- No missing or unresolved dependencies
- Cryptographic hashes correct

**Developer Requirements:**

- Use schema validation tools
- Compare SBOM against actual artifact contents
- Investigate and resolve discrepancies

### SBOM Quality Score

**Requirement:** Track SBOM quality metrics.

**Quality Indicators:**

- Percentage of components with version information
- Percentage of components with license information
- Percentage of components with cryptographic hash
- Timestamp freshness (SBOM generated recently)
- Supplier information completeness

**Target Quality:**

- 100% components with version
- 95%+ components with license
- 100% components with hash
- SBOM generated within 24 hours of build

## Vulnerability Exploitability Exchange (VEX)

### VEX Usage

**Requirement:** Use VEX to communicate vulnerability status.

**VEX Purpose:**

- Indicate that vulnerability is "not affected" (component not used in vulnerable way)
- Indicate that vulnerability is "fixed" (patched)
- Indicate that vulnerability is "under investigation"

**Developer Requirements:**

- Use CycloneDX VEX or CSAF VEX format
- Document assessment of vulnerabilities in SBOMs
- Provide VEX statements to customers to reduce false positives

**Example VEX (CycloneDX):**

```json
{
  "vulnerabilities": [
    {
      "id": "CVE-2021-44228",
      "analysis": {
        "state": "not_affected",
        "justification": "code_not_reachable",
        "detail": "JNDI lookup feature is disabled"
      }
    }
  ]
}
```

## Compliance and Regulatory Requirements

### Executive Order 14028 (U.S. Federal)

**Requirement:** Provide SBOM for software sold to U.S. federal government.

**Developer Requirements:**

- Generate SBOM in SPDX or CycloneDX format
- Include NTIA minimum elements
- Provide SBOM upon delivery or upon request
- Ensure SBOM is machine-readable

### Industry-Specific Requirements

**Healthcare (FDA):**

- SBOM for medical devices (per FDA guidance)

**Critical Infrastructure:**

- SBOM for OT/ICS software (per CISA guidance)

**Developer Requirements:**

- Understand industry-specific SBOM requirements
- Generate compliant SBOMs for regulated products

## Control Mapping

| EATGF Context          | ISO 27001:2022 | NIST SSDF | OWASP            | COBIT |
| ---------------------- | -------------- | --------- | ---------------- | ----- |
| SBOM Generation        | A.8.30         | PO.3      | CycloneDX        | BAI07 |
| Vulnerability Tracking | A.8.8, A.8.31  | RV.1      | Dependency-Check | DSS02 |
| License Compliance     | A.5.32         | PO.3      | -                | MEA03 |
| Incident Response      | A.5.26         | RV.2      | -                | DSS02 |

## Developer Checklist

For every release:

- [ ] SBOM generated in SPDX or CycloneDX format
- [ ] SBOM includes all dependencies (direct and transitive)
- [ ] SBOM validated against schema
- [ ] SBOM uploaded to artifact repository
- [ ] SBOM ingested into vulnerability management system
- [ ] License compliance reviewed
- [ ] SBOM provided to customers (if applicable)

## Governance Implications

**Risk if not implemented:**

- Unable to identify vulnerable components in production
- Slow incident response to supply chain vulnerabilities
- Regulatory non-compliance (federal contracts, medical devices)
- License compliance violations

**Operational impact:**

- Rapid vulnerability identification and remediation
- License compliance automation
- Customer transparency and trust

**Audit consequences:**

- SBOM demonstrates component inventory and control
- Required for federal contracts and regulated industries
- Demonstrates supply chain security maturity

**Cross-team dependencies:**

- Security team consumes SBOMs for vulnerability tracking
- Legal team reviews license compliance
- Sales team provides SBOMs to customers

## Authority Hierarchy

If conflict exists, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Information Security Policy (Layer 04)
3. Supply Chain Security Standard
4. SBOM Governance Standard

## References

- NTIA Minimum Elements for SBOM (<https://www.ntia.gov/page/minimum-elements-software-bill-materials-sbom>)
- Executive Order 14028: Improving the Nation's Cybersecurity
- SPDX Specification (<https://spdx.dev/>)
- CycloneDX (<https://cyclonedx.org/>)
- CISA SBOM Sharing Guidance
- Syft (<https://github.com/anchore/syft>)
- Grype (<https://github.com/anchore/grype>)

## Version History

| Version | Date       | Change Type | Description                      |
| ------- | ---------- | ----------- | -------------------------------- |
| 1.0     | 2026-02-14 | Major       | Initial SBOM governance standard |
