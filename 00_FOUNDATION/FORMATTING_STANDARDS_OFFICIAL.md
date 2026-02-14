# EATGF Official Formatting Standards

## Purpose

This document establishes mandatory formatting standards for all Enterprise AI-Aligned Technical Governance Framework (EATGF) documentation. All authors, contributors, and publishing processes must adhere strictly to these standards without exception.

**Effective Date:** February 14, 2026  
**Authority:** EATGF Governance Council  
**Classification:** Controlled

---

## Markdown Structure (Mandatory)

Every EATGF documentation file MUST follow this exact hierarchical structure:

### Primary Sections (H2)

Every governance document must include these eight sections in this precise order:

1. **## Purpose** – Clear statement of the document's business objective and scope
2. **## Architectural Position** – Where this fits within EATGF's 8-layer architecture
3. **## Governance Principles** – 3–5 core principles guiding implementation
4. **## Technical Implementation** – How-to guidance, procedures, or specification details
5. **## Control Mapping** – Explicit mapping to ISO 27001:2022, NIST SSDF, OWASP, COBIT
6. **## Developer Checklist** – Actionable verification steps for implementation teams
7. **## Governance Implications** – Organizational impact, roles, responsibilities, audit considerations
8. **## Official References** – Only primary sources (NIST, ISO, IETF RFC, COBIT, OWASP)

### Document Header (H1 + Metadata)

```markdown
# Document Title (Exact Name)

| Field | Value |
|-------|-------|
| Document Type | Framework / Policy / Procedure / Specification |
| Version | X.Y |
| Classification | Controlled / Public / Internal |
| Effective Date | YYYY-MM-DD |
| Authority | Role / Team / Council |
| EATGF Layer | 00_FOUNDATION / 01_MANAGEMENT_SYSTEMS / etc. |

---
```

---

## Writing Style

### What IS Required

✅ **Clear, structured, readable prose**
- Short paragraphs (2–4 sentences maximum)
- Action-oriented language
- Precise technical terminology
- Concise but complete explanations

✅ **Enterprise authority tone**
- Professional and formal
- Confident without being condescending
- Prescriptive for mandatory controls
- Advisory for guidance sections

✅ **No academic tone**
- Avoid: "This paper explores...", "It is noteworthy that...", "As per the literature..."
- Use: "The control requires...", "Implementation must ensure...", "Organizations adopt..."

### What IS NOT Allowed

❌ **Footnotes** – Use inline clarification or separate sections instead

❌ **Hidden HTML** – No HTML comments, no embedded styling

❌ **Emojis** – No ✅, ❌, 🔒, or any emoji characters (except in tables where already established)

❌ **Decorative text** – No stars, arrows, or special characters for formatting

❌ **Toy examples** – All code and process examples must be production-grade

❌ **Personal voice** – Avoid "I", "we", "you"; use passive or organizational voice

❌ **Casual language** – No colloquialisms, slang, or informal phrasing

---

## Code Examples

### Requirements

✅ **Use fenced code blocks with language specification**

```python
# All code blocks must specify the language: python, yaml, javascript, bash, json, sql, etc.
# Include brief inline comments explaining purpose
# This is production-grade example code only
```

✅ **Brief inline comments (max 2 per code block)**
- Comment WHAT and WHY, not obvious implementation details
- Example: `# Validate API token expiration` instead of `# Check if token < 1 hour`

✅ **Production-grade examples only**
- Real-world configuration patterns
- Security best practices applied
- Error handling included where critical
- No placeholder variables unless clearly indicated

### Examples of Acceptable Code

**Python: API Integration with Security**
```python
import requests
from cryptography.fernet import Fernet
import logging

class SecureAPIClient:
    def __init__(self, api_key_encrypted: str, cipher: Fernet):
        # Decrypt API key from secure storage on initialization
        self.api_key = cipher.decrypt(api_key_encrypted.encode())
        self.logger = logging.getLogger(__name__)
    
    def call_governance_api(self, endpoint: str, payload: dict) -> dict:
        # Add security headers and request signing
        headers = {
            "Authorization": f"Bearer {self.api_key.decode()}",
            "X-Request-Signature": self._sign_request(payload)
        }
        response = requests.post(endpoint, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
```

**YAML: Control Definition Structure**
```yaml
control:
  id: EATGF-APO-GOV-01
  name: Governance Authority Definition
  category: Governance Architecture
  iso27001_mapping: [5.1, 5.2]
  cobit_mapping: [EDM01, APO01]
  objective: |
    Establish formal governance authority and accountability
    structures with clear responsibility assignments.
  implementation:
    - Define governance bodies and decision rights
    - Document accountability matrices
    - Execute role-based activity authorization
```

**Bash: Infrastructure Deployment**
```bash
#!/bin/bash
# Deploy governance documentation site with standard security posture

set -euo pipefail

SITE_DIR="/opt/governance-site"
CONFIG_FILE="/etc/governance/config.yaml"

# Validate configuration file exists and is readable
if [[ ! -r "$CONFIG_FILE" ]]; then
    echo "Error: Configuration file not found at $CONFIG_FILE" >&2
    exit 1
fi

# Build and deploy documentation with TLS enforcement
cd "$SITE_DIR"
npm run build --production
npm run deploy -- --tls-required --csp-enabled
```

---

## Sources and Citations

### ONLY Approved Primary Sources

✅ **Required sources (use these exclusively)**
- NIST (SP 800 series, AI RMF, SSDF)
- ISO/IEC (27001:2022, 27002:2022, 42001:2023, others)
- IETF RFC documents
- OWASP (Top 10, secure coding guides, architecture reviews)
- COBIT (ISACA governance framework)

### NEVER Use These Sources

❌ **Secondary sources never allowed**
- Wikipedia (unreliable, not authoritative)
- Blog posts (no matter how credible the author)
- Academic papers from arXiv (not peer-reviewed official sources)
- Non-official medium articles or dev.to
- ChatGPT or other LLM outputs as sources
- Internal organization documentation from other enterprises

### Citation Format

**In-text** (no footnotes):
```
According to NIST SP 800-53 Rev. 5, access control policies must 
establish role definitions before implementation.
```

**Reference Section** (mandatory at end):

```markdown
## Official References

- **NIST Special Publication 800-53 Rev. 5** – Security and Privacy Controls for Information Systems (2020)
- **ISO/IEC 27001:2022** – Information Security Management Systems (ISACA, 2022)
- **COBIT 2019** – Governance of Enterprise IT (ISACA, 2019)
- **OWASP Top 10** – Web Application Security Risks (OWASP Foundation)
```

---

## Structural Consistency

### EATGF Architecture Alignment

Every document must explicitly state its position in the 8-layer architecture:

```markdown
## Architectural Position

This specification operates within **04_POLICY_LAYER** of EATGF.

- **Upstream dependency:** 02_CONTROL_ARCHITECTURE (defines required controls)
- **Downstream implementation:** Organization-specific policy instantiation
- **Cross-layer reference:** 01_MANAGEMENT_SYSTEMS (normative reference for ISO compliance)
```

### Mandatory Control Mappings

Every policy, framework, and specification MUST include a "Control Mapping" section with explicit mappings:

```markdown
## Control Mapping

### ISO 27001:2022 Alignment
- **Clause 5.2** – Information security policies and procedures
- **Clause 6.2** – Risk assessment and treatment
- **Clause 7.2** – Competence and awareness

### NIST SSDF v1.1 Alignment
- **PO1.3** – Review and incorporate security requirements into criteria
- **PO2.1** – Document and communicate security and privacy requirements
- **PR3.1** – Use standard security configurations for infrastructure

### OWASP Alignment
- **Secure Code Review** – OWASP SAMM (SM: Governance)
- **Threat Modeling** – OWASP Threat Modeling Framework
- **Architecture Review** – OWASP Architecture Review Board

### COBIT 2019 Alignment
- **EDM02** – Ensure stakeholder value delivery
- **APO01** – Manage IT management framework
- **APO05** – Manage portfolio
```

---

## Formatting and Layout

### Spacing and Readability

✅ **Proper spacing**
- Blank line before each H2 section
- Blank line between paragraphs
- No more than 4 consecutive paragraph lines
- Tables must have blank lines before and after

✅ **Lists and structure**
- Use unordered lists (`-`) for parallel items
- Use ordered lists (`1.`) only for sequential procedures
- Indent sublists with 4 spaces
- No more than 3 nesting levels

### Visual Hierarchy

```markdown
# H1: Document Title Only (one per file)

## H2: Major Sections (8 required sections in order)

### H3: Subsection (as needed within H2 sections)

#### H4: Minor subsection (rarely needed; max 1 level deeper)

```

**NO OTHER ELEMENTS:**
- No decorative lines (---) except after H1
- No colored text or highlighting
- No tables outside metadata blocks
- No internal links without full context

### Table Format

Metadata tables use standard Markdown tables:

```markdown
| Field | Value |
|-------|-------|
| Document Type | Framework |
| Version | 1.0 |
| Classification | Controlled |
```

Data tables must use clear headers:

```markdown
| Control ID | Control Objective | ISO Mapping | Implementation |
|------------|-------------------|-------------|-----------------|
| EATGF-APO-01 | Governance Structure | 5.1, 5.2 | Establish bodies |
```

---

## No Hidden Content

### What IS Allowed

✅ **Standard Markdown**
- Headers, paragraphs, lists
- Fenced code blocks
- Tables
- Links to other documentation
- Emphasis: **bold** and *italic* (minimal use)

### What IS NOT Allowed

❌ **NO HTML tags** – Even those that "don't render"
- `<!-- comments -->`
- `<div>`, `<span>`, `<style>` tags
- `&nbsp;`, `&mdash;`, or HTML entities

❌ **NO custom formatting directives**
- No Jekyll front matter beyond YAML metadata blocks
- No preprocessing instructions
- No Docusaurus-specific JSX or MDX

❌ **NO unescaped special characters**
- Content must be valid Markdown that renders identically across platforms

---

## Docusaurus Publication Standards

### Filename Conventions

- Use **SCREAMING_SNAKE_CASE.md** for all files
- Example: `INFORMATION_SECURITY_POLICY.md`, `CONTROL_MAPPING_GUIDE.md`
- NO spaces, NO lowercase, NO hyphens

### Directory Structure

Files must be organized exactly as:

```
eatgf-framework/
├── 00_FOUNDATION/
│   ├── README.md
│   ├── OFFICIAL_DESIGNATION.md
│   ├── FORMATTING_STANDARDS_OFFICIAL.md
│   └── [other framework documents]
├── 01_MANAGEMENT_SYSTEMS/
│   ├── README.md
│   └── [system specifications]
├── [02–07_LAYERS]/
│   ├── README.md
│   └── [domain documents]
```

### H1 Requirement

Every document MUST have exactly one H1 (`#`) header as the document title. This is the Docusaurus page title.

```markdown
# Actual Document Title Here

(Metadata table follows immediately)

| Field | Value |
```

---

## Compliance Auditing

### Automated Checks (Future)

All documents will be validated against:
- ✅ Single H1 per file
- ✅ Presence of all 8 major H2 sections
- ✅ No emojis in content
- ✅ No HTML tags
- ✅ All code blocks have language specification
- ✅ All references are primary sources only

### Manual Review Checklist

Before publication, reviewers must verify:

- [ ] Document title matches exactly: `# Title`
- [ ] Metadata table present and complete
- [ ] All 8 sections present in exact order
- [ ] No emojis, footnotes, or hidden HTML
- [ ] Code examples are production-grade
- [ ] All citations are primary sources
- [ ] Control mappings align with MCM
- [ ] Developer checklist is actionable
- [ ] Writing tone is authority, not academic
- [ ] Docusaurus sidebar includes document

---

## Authority and Change Control

**This formatting standard is binding on all EATGF contributors.**

**Change Authority:** EATGF Governance Council  
**Review Frequency:** Quarterly  
**Last Updated:** February 14, 2026  
**Next Review:** May 14, 2026

Document changes require:
1. Formal change request to governance council
2. Impact assessment on existing documentation
3. Bulk update of all affected documents
4. Baseline update to BASELINE_DECLARATION_v1.0.md

---

## Official References

- **NIST Special Publication 800-53 Rev. 5** – Security and Privacy Controls for Information Systems and Organizations (2020)
- **ISO/IEC 27001:2022** – Information Security Management Systems (2022)
- **ISO/IEC 27002:2022** – Information Security Code of Practice (2022)
- **COBIT 2019** – Governance of Enterprise IT (ISACA, 2019)
- **OWASP Secure Coding Practices** – OWASP Foundation
- **CommonMark Specification 0.30** – Markdown Reference (2023)
