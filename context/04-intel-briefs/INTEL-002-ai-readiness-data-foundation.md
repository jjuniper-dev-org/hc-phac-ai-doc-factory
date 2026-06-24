---
id: INTEL-002
title: "AI Readiness / Data Foundation"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids:
  - SRC-AI-READINESS-DATA-PERSPECTIVE
  - SRC-HC-PHAC-IT-PLAN-FOCUS-AREAS
review_after: 2026-07-31
tags:
  - ai-readiness
  - data-architecture
  - fair
  - sacr
  - data-governance
  - data-quality
  - metadata
  - stewardship
---

# INTEL-002 — AI Readiness / Data Foundation

## 1. Status

- Classification: Unclassified working draft
- Document status: Draft
- Confidence level: Medium
- Last updated: 2026-06-24
- Owner / steward: EA / AI document factory working context
- Source basis: AI Readiness — Data Perspective and HC/PHAC IT/data architecture planning material
- Review state: Suitable for draft document production; not accepted context
- Promotion recommendation: Keep as `draft` until source cards are created for the AI Readiness deck and data architecture planning inputs.

## 2. Executive takeaway

AI readiness at HC/PHAC is constrained less by model access than by data readiness: discoverability, quality, stewardship, classification, lineage, metadata, acceptable repositories, and reusable data architecture. AI use cases should therefore be assessed for data foundation readiness before platform or model selection.

The practical EA position is:

```text
AI readiness depends on governed, reusable, findable, and stewarded data.
```

## 3. What is source-backed

- The AI readiness data perspective identifies foundational data gaps as blockers for responsible and scalable AI.
- Recurring data-readiness needs include inventories, dictionaries, metadata, data quality, stewardship, FAIR-aligned practices, acceptable repositories, and data management planning.
- Enterprise data and AI architecture work is expected to reduce fragmentation and improve reuse across AI, analytics, surveillance, and decision-support workloads.
- AI use cases that rely on weakly governed data create downstream risks for quality, auditability, reproducibility, privacy, security, and public trust.

## 4. Working interpretation

AI readiness should be treated as a data architecture maturity problem, not only a technology acquisition problem. A model/API request should be routed through a data-readiness triage that asks whether the data is known, classified, governed, documented, stewarded, and fit for the intended use.

For HC/PHAC, this points to a reusable pattern:

| Readiness area | Minimum question |
|---|---|
| Inventory | Is the data asset known and findable? |
| Classification | Is the sensitivity and Protected B posture understood? |
| Stewardship | Is there an accountable data steward or program owner? |
| Quality | Is quality sufficient for AI-supported use? |
| Metadata | Are definitions, lineage, and usage constraints documented? |
| Repository | Is the data held in an acceptable managed repository? |
| Reuse | Can the data serve multiple products without bespoke duplication? |

## 5. Why it matters

Without a governed data foundation, PATH, HAIL, Fabric, Databricks, Copilot, and RAG patterns all inherit inconsistent data controls. This creates a risk that AI delivery appears successful at pilot scale while remaining difficult to audit, scale, defend, or reuse.

The data foundation is also what links the HC AI Roadmap pillars to enterprise execution: productivity gains need trusted knowledge sources, surveillance use cases need reliable and timely data, and efficiency use cases need repeatable data products rather than one-off extracts.

## 6. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Define AI data-readiness triage | Proposed | OCDO / EA / TPO | Needs endorsed intake criteria |
| Confirm acceptable repository expectations for AI-relevant data | Open | OCDO / Data governance / Security | Needs formal repository guidance |
| Define minimum metadata and stewardship requirements | Proposed | OCDO / Data stewards | Needs source-backed checklist |
| Align AI use-case inventory with data asset inventory | Proposed | OCDO / EA | Needs integration pattern |
| Decide where data readiness evidence is captured | Open | OCDO / TPO / ARB | Needs governance workflow |

## 7. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| Treating AI as tool-first | Leads to model access without fit-for-use data | Put data readiness into intake |
| Siloed data products | Recreates one-off extracts for every AI project | Promote reusable data products and enterprise patterns |
| Weak metadata | Reduces discoverability and auditability | Require catalogue, dictionary, and lineage evidence |
| Ambiguous stewardship | Blurs accountability for quality and use constraints | Identify data stewards and program owners |
| Overclaiming readiness | Could imply governance maturity not yet achieved | Mark maturity gaps and evidence gaps explicitly |

## 8. Use in document-production pipeline

| Target artifact | How this intel informs it |
|---|---|
| AI Playbook | Adds data-readiness triage before model/platform selection |
| Data Architecture Plan | Defines why inventories, metadata, stewardship, and repositories matter for AI |
| ARB briefing | Gives reviewers a data-readiness evidence checklist |
| TPO / intake workflow | Supports early routing of AI requests based on data maturity |
| PATH / HAIL convergence | Clarifies that runtime patterns must inherit data controls |
| Agent / voice KB | Gives a plain-language answer to “why data readiness blocks AI” |

## 9. Retrieval tags

- ai-readiness
- data-readiness
- data-governance
- metadata
- stewardship
- fair
- sacr
- data-quality
- enterprise-data-architecture

## 10. Graph extraction

### Concepts

- AI readiness
- data readiness
- enterprise data architecture
- data governance
- FAIR
- SACR
- acceptable repository
- data inventory
- data dictionary
- data steward
- Data Management Plan
- metadata catalogue
- data quality
- Protected B posture
- reusable data product

### Claims

- AI readiness depends on foundational data readiness.
- AI use cases should be triaged for data availability, quality, governance, and stewardship.
- Model access alone does not create enterprise AI readiness.
- PATH and HAIL must inherit data governance controls from enterprise data architecture.
- Data inventories and stewardship are prerequisites for scalable AI reuse.

### Decisions

- Define AI data-readiness triage.
- Confirm acceptable repository expectations for AI-relevant data.
- Align AI use-case inventory with data asset inventory.
- Define where data-readiness evidence is captured.

### Risks

- Tool-first AI delivery.
- Siloed data products.
- Weak metadata.
- Ambiguous stewardship.
- Overclaimed readiness.

### Relationships

```text
AI readiness REQUIRES data readiness
AI readiness REQUIRES data governance
AI readiness REQUIRES enterprise data architecture
Data Architecture Plan INFORMS AI Playbook
Data steward OWNS data quality evidence
Purview SUPPORTS metadata catalogue
PATH INHERITS data governance controls
HAIL INHERITS data governance controls
```

## 11. Open questions

- What is the minimum data-readiness evidence package for an AI workload?
- Where should data-readiness triage live: ARB, TPO intake, OCDO inventory, or PATH intake?
- Which repositories are acceptable for AI-relevant data at each classification level?
- How should AI use cases be linked to authoritative data assets and stewards?
- What evidence is required before a brief can move from `draft` to `review-ready`?
