# VSCode EATGF Integration

This directory contains VSCode configuration files that enforce EATGF Document Signature Template standards.

## Files

### `.vscode/settings.json`

Workspace settings that enforce EATGF document standards through GitHub Copilot instructions and markdown formatting rules.

**Key Features:**

- GitHub Copilot custom instructions for EATGF compliance
- Markdown formatting enforcement
- File associations for EATGF documents
- Auto-formatting on save

### `.vscode/eatgf.code-snippets`

Code snippets for rapid EATGF-compliant document creation.

**Available Snippets:**

- `eatgf-doc` - Full EATGF document template with all mandatory sections
- `eatgf-mapping` - Control mapping table (ISO/NIST/OWASP/COBIT)
- `eatgf-checklist` - Developer checklist section
- `eatgf-implications` - Governance implications section
- `eatgf-code` - Production-grade code example block

### `.vscode/tasks.json`

VSCode tasks for EATGF framework operations.

**Available Tasks:**

- **EATGF: Validate Document Compliance** - Shows compliance checklist
- **EATGF: Create New Document from Template** - Guide for new documents
- **EATGF: Check Framework Structure** - List all framework markdown files
- **EATGF: Build Docusaurus Site** - Build the documentation site
- **EATGF: Serve Docusaurus Site** - Serve the site locally

Run tasks via: `Cmd+Shift+P` → `Tasks: Run Task`

### `.editorconfig`

Editor configuration enforcing consistent formatting across all EATGF documents.

### `.github/copilot-instructions.md`

GitHub Copilot workspace instructions that enforce EATGF Document Signature Template compliance.

## Usage

### Creating a New EATGF Document

1. Create a new `.md` file in the appropriate layer directory
2. Type `eatgf-doc` and press Tab to insert the full template
3. Fill in all required sections:
   - Architectural Position
   - Governance Principles
   - Control Mapping
   - Content
   - Developer Checklist
   - Governance Implications
   - Version Information

### Editing Existing Documents

GitHub Copilot will automatically enforce EATGF standards when:

- Creating new content
- Refactoring documents
- Suggesting improvements

All suggestions will comply with:

- Professional tone (NO emojis)
- Production-grade code examples only
- Official references only (NIST/ISO/OWASP/COBIT)
- Docusaurus-ready formatting

### Validation

Before committing any document:

1. Run: `Tasks: Run Task` → `EATGF: Validate Document Compliance`
2. Verify all mandatory sections are present
3. Ensure control mapping is complete
4. Confirm version information is current

## Mandatory Requirements

Every EATGF document MUST include:

1. **Architectural Position**
   - EATGF Layer Placement
   - Governance Scope
   - Control Authority Relationship

2. **Governance Principles**
   - Which principles apply

3. **Control Mapping**
   - Explicit mapping table (ISO 27001/NIST SSDF/OWASP/COBIT)

4. **Developer Checklist**
   - Actionable items
   - Role-specific

5. **Governance Implications**
   - Risk if not implemented
   - Operational impact
   - Audit consequences
   - Cross-team dependencies

6. **Version Information**
   - Version number
   - Change type
   - Date
   - Status

## Authority Hierarchy

In case of conflicts, this order prevails:

1. MASTER_CONTROL_MATRIX
2. Governance Charter
3. Official Naming Freeze
4. EATGF Document Signature Template

## Reference

Full template: [eatgf-framework/00_FOUNDATION/EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md](../eatgf-framework/00_FOUNDATION/EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md)

**NO DOCUMENT MAY BE PUBLISHED WITHOUT FULL COMPLIANCE TO THIS TEMPLATE.**
