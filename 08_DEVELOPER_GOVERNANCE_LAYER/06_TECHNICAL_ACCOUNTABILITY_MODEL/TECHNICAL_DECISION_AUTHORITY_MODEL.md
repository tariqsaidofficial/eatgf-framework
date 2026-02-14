# Technical Decision Authority Model

## Document Metadata

**Version:** 1.0
**Issue Date:** 2026-02-14
**Layer:** 08_DEVELOPER_GOVERNANCE_LAYER
**Subdomain:** 06_TECHNICAL_ACCOUNTABILITY_MODEL
**Governance Scope:** Decision Framework
**Control Authority Relationship:** Implements controls

## Architectural Position

**EATGF Layer Placement:** 08_DEVELOPER_GOVERNANCE_LAYER / 06_TECHNICAL_ACCOUNTABILITY_MODEL

**Governance Scope:** Technical decision-making authority, escalation, and Architecture Decision Records (ADRs).

**Control Authority Relationship:** Implements:

- Layer 02: Organizational Controls
- Layer 04: Governance Charter
- Technical decision governance

## Purpose

Defines authority levels for technical decisions, decision-making processes, and documentation requirements.

## Governance Principles

- **Control-Centric Architecture:** Decisions traceable and documented
- **Developer-Operational Alignment:** Appropriate delegation of authority
- **Audit Traceability:** All significant decisions recorded
- **Single Source of Truth:** ADRs as authoritative record

## Decision Authority Levels

**Requirement:** Classify technical decisions by impact and assign appropriate authority.

**Decision Levels:**

| Level | Impact Scope | Authority | Documentation | Examples |
|---|---|---|---|---|
| **Level 1: Team** | Single team, reversible | Tech Lead | Optional ADR | Library choice, code structure |
| **Level 2: Domain** | Multiple teams, costly to reverse | Engineering Manager + Architect | Mandatory ADR | Service architecture, data model |
| **Level 3: Platform** | Organization-wide, hard to reverse | Architecture Board | Mandatory ADR + Review | Cloud provider, programming language |
| **Level 4: Strategic** | Company-wide, irreversible | CTO / VP Engineering | Mandatory ADR + Board | Build vs. buy, technology platform |

## Decision-Making Process

### Level 1: Team Decisions

**Authority:** Tech Lead

**Process:**

1. Team discusses options
2. Tech Lead makes decision
3. Team informed via team channel or standup
4. Optional: Document in ADR if precedent-setting

**Timeline:** Same day

**Examples:**

- Choice of testing framework
- Code organization within service
- Internal API design (not exposed externally)

### Level 2: Domain Decisions

**Authority:** Engineering Manager + Architect (if available)

**Process:**

1. Tech Lead drafts proposal with options, pros/cons, recommendation
2. Stakeholder consultation (affected teams, security, devops)
3. Review with Engineering Manager and Architect
4. Decision documented in ADR
5. Communicate decision to stakeholders

**Timeline:** 1-2 weeks

**Examples:**

- Microservices vs. monolith for new feature
- Database selection (Postgres vs. MySQL)
- Event-driven vs. synchronous inter-service communication
- Data retention strategy

### Level 3: Platform Decisions

**Authority:** Architecture Board (or Architecture Review Committee)

**Board Composition:**

- Chief Architect (or Senior Architect)
- Engineering Manager representatives
- Security Lead
- DevOps Lead
- CTO or VP Engineering (optional)

**Process:**

1. Proposal submitted to Architecture Board (RFC format)
2. Research and POC if needed
3. Board review meeting (present options, recommendation)
4. Board deliberation and decision
5. ADR published with board approval
6. Organization-wide communication

**Timeline:** 4-8 weeks

**Examples:**

- Cloud provider selection (AWS vs. Azure vs. GCP)
- Adoption of new programming language
- API gateway / service mesh platform
- Observability platform (monitoring, logging, tracing)
- Identity and access management platform

### Level 4: Strategic Decisions

**Authority:** CTO, VP Engineering, or Executive Leadership

**Process:**

1. Business case and technical proposal
2. Vendor evaluation and due diligence
3. Executive review and decision
4. ADR published
5. Company-wide communication and training plan

**Timeline:** 3-6 months

**Examples:**

- Build in-house vs. buy commercial product
- Acquisition and technology integration
- Major platform migration (on-prem to cloud)
- Open source vs. proprietary licensing model

## Architecture Decision Records (ADRs)

**Requirement:** Document significant technical decisions in ADRs.

**ADR Content:**

- **Title:** Short descriptive title
- **Status:** Proposed, Accepted, Superseded, Deprecated
- **Context:** Problem statement and background
- **Decision:** What was decided
- **Consequences:** Positive and negative outcomes
- **Alternatives Considered:** Other options and why rejected
- **Date:** Decision date
- **Decision Makers:** Who approved

**ADR Format (Markdown):**

```markdown
# ADR-001: Use PostgreSQL for Primary Database

**Status:** Accepted
**Date:** 2026-02-14
**Decision Makers:** Engineering Manager, Chief Architect

## Context

We need to select a relational database for our new SaaS application. Requirements:
- ACID compliance
- JSON support
- Horizontal scalability
- Strong community and support

## Decision

We will use PostgreSQL 15+ as our primary database.

## Consequences

**Positive:**
- Robust ACID guarantees
- Excellent JSON/JSONB support
- Strong community and ecosystem
- Cloud provider managed options (RDS, Cloud SQL, Azure Database)

**Negative:**
- More complex to scale horizontally than NoSQL
- Requires careful query optimization for performance
- Steeper learning curve than MySQL

## Alternatives Considered

**MySQL:**
- Pros: Simpler, faster for read-heavy workloads
- Cons: Weaker JSON support, less advanced features

**Amazon Aurora:**
- Pros: AWS-native, auto-scaling
- Cons: Vendor lock-in, higher cost

**MongoDB:**
- Pros: Flexible schema, horizontal scaling
- Cons: No ACID for multi-document transactions (at decision time)

## References

- PostgreSQL documentation
- PostgreSQL vs MySQL comparison
```

**ADR Storage:**

- Store in version control (`docs/adr/` directory)
- Use sequential numbering (ADR-001, ADR-002, etc.)
- Link related ADRs
- Keep ADRs even when superseded (historical record)

## Decision Escalation

**Requirement:** Escalate decisions when authority unclear, risk high, or consensus not reached.

**Escalation Triggers:**

- **Cost:** Decision involves significant cost (e.g., >$100K/year)
- **Risk:** High technical or business risk
- **Scope:** Affects multiple teams or organization-wide
- **Irreversibility:** Hard or impossible to reverse
- **Disagreement:** Stakeholders cannot reach consensus

**Escalation Paths:**

| Current Authority | Escalate To | Reason |
|---|---|---|
| Tech Lead | Engineering Manager | Cross-team impact, high cost |
| Engineering Manager | Architecture Board | Platform-level decision |
| Architecture Board | CTO / VP Engineering | Strategic decision, high cost |

## Decision Review and Revision

**Requirement:** Periodically review ADRs for relevance.

**Review Cadence:**

- **Annual:** Review all ADRs for accuracy and relevance
- **As Needed:** When technology landscape changes or decision proven incorrect

**ADR Status Transitions:**

- **Proposed → Accepted:** Decision approved and implemented
- **Accepted → Superseded:** New ADR replaces old decision
- **Accepted → Deprecated:** Decision no longer relevant (e.g., system decommissioned)

**Superseding ADR:**

- Create new ADR referencing superseded ADR
- Update old ADR status to "Superseded by ADR-XXX"
- Explain why decision changed

## Lightweight Decision Documentation

**Requirement:** Not all decisions require full ADR.

**Decision Logs (for smaller decisions):**

- Use issue tracker or wiki
- Brief description of decision and rationale
- No formal review required
- Examples: Configuration changes, tool upgrades, minor refactoring

## Control Mapping

| EATGF Context | ISO 27001:2022 | NIST SSDF | OWASP | COBIT |
|---|---|---|---|---|
| Decision Authority | A.5.24 | PO.1 | - | APO01 |
| Decision Documentation | A.5.37 | PO.3 | - | MEA01 |

## Developer Checklist

For significant technical decisions:

- [ ] Classify decision level (1-4)
- [ ] Identify appropriate decision authority
- [ ] Draft proposal or ADR
- [ ] Consult stakeholders
- [ ] Obtain decision approval
- [ ] Document in ADR (if Level 2+)
- [ ] Communicate decision to affected teams

## References

- Architecture Decision Records (<https://adr.github.io/>)
- Michael Nygard, "Documenting Architecture Decisions"
- Thoughtworks Technology Radar

## Version History

| Version | Date | Change Type | Description |
|---|---|---|---|
| 1.0 | 2026-02-14 | Major | Initial technical decision authority model |
