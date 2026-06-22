# Source Card — SRC-003

## Source identity

| Field | Value |
|---|---|
| Source ID | SRC-003 |
| Title | AI Readiness — Data Perspective |
| File name / URL | AI Readiness - Data Perspective.pptx |
| Source type | Working architecture input |
| Owner / origin | DTPOD-SDTAD Enterprise Architecture |
| Status | Candidate for ingestion |
| Classification / sensitivity | Unclassified unless otherwise marked |
| Intended use | Data Architecture Plan, AI Playbook, context packs |
| Repository location | To be confirmed |
| Last reviewed | 2026-06-22 |

## Summary

This source provides the initial data-readiness framing for AI at HC/PHAC. It identifies foundational gaps in enterprise data architecture, governance, metadata/catalogue, standards, data quality, and AI-grade infrastructure.

## Why it matters

This source should become one of the core inputs for the Data Architecture Plan because it connects AI adoption to data governance, FAIR data principles, SACR or acceptable repositories, data inventories, data dictionaries, stewardship, and Data Management Plans.

## Allowed uses

- [x] Drafting
- [x] Review
- [x] Evidence support
- [x] Architecture decision input
- [x] Context pack input
- [ ] Not for agent use

## Key facts / claims

| Claim ID | Claim | Confidence | Notes |
|---|---|---|---|
| C-003-001 | HC/PHAC AI readiness depends on fixing foundational data gaps. | High | Source framing |
| C-003-002 | Current gaps include lack of enterprise data architecture, fragmented governance, no enterprise metadata catalogue, and limited Responsible AI controls. | High | Source framing |
| C-003-003 | Future state includes operational Data & AI Governance, Enterprise Data/AI Architecture, centralized catalogues, standardized data models, and integrated Data & AI platforms. | High | Source framing |
| C-003-004 | AI-ready data should follow FAIR principles and have appropriate repository, inventory, dictionary, steward, and Data Management Plan support. | High | Source framing |

## Key concepts

| Concept | Description |
|---|---|
| AI readiness | Organizational ability to use AI responsibly and effectively through governed data, platforms, and controls |
| Enterprise Data Architecture | Common data models, standards, lineage, metadata, and platform alignment |
| FAIR data | Findable, accessible, interoperable, reusable data |
| SACR alignment | Use of SACR or another acceptable repository as part of controlled information management |
| Data Management Plan | Plan defining stewardship, access, use, quality, lifecycle, and governance expectations |

## Decision candidates

| Decision candidate | Notes |
|---|---|
| Data Architecture Plan should treat AI readiness as a primary driver. | Strong candidate |
| Enterprise data catalogue and lineage should be positioned as foundational AI capabilities. | Strong candidate |
| Data readiness should become an intake gate for AI use cases. | Strong candidate |
| SACR should remain a repository-of-record anchor, not the messy drafting workspace. | Aligns with current document factory model |

## Actionable tasks

| Task | Owner | Destination |
|---|---|---|
| Extract AI readiness claims into Data Architecture Plan context pack. | Agent / James | context/01-context-packs/data-architecture-plan-context-pack.md |
| Create Data Architecture Plan section stub for AI readiness. | Agent / James | docs/data-architecture-plan/02-source/09-ai-readiness.md |
| Create review issue for data governance assumptions. | James | GitHub Issues |
| Map source claims to future Neo4j Source, Claim, Concept, and Decision nodes. | Agent / future graph workflow | graph/neo4j |

## Exclusions / cautions

This source should not be treated as a final approved enterprise architecture decision unless governance status is confirmed. Agents must distinguish source framing from formally approved ARB/TPO/OCDO decisions.

## Related sources

- SRC-001 — TBS AI Strategy
- SRC-002 — HC AI Strategy
- SRC-004 — PATH Agent Briefing
- SRC-005 — HAIL Agent Briefing
- SRC-006 — Purview Control Plane Briefing
