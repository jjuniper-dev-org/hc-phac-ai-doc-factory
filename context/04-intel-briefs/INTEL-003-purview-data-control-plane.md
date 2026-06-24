---
id: INTEL-003
title: "Purview Data Control Plane"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids:
  - SRC-PURVIEW-CONTROL-PLANE
review_after: 2026-07-31
tags:
  - purview
  - data-governance
  - lineage
  - classification
  - auditability
  - control-plane
---

# INTEL-003 — Purview Data Control Plane

## 1. Status

- Classification: Unclassified working draft
- Document status: Draft
- Confidence level: Medium
- Last updated: 2026-06-24
- Owner / steward: EA / AI document factory working context
- Source basis: HC/PHAC AI Architecture Update — Purview as Enterprise Data Control Plane
- Review state: Suitable for draft document production; not accepted context
- Promotion recommendation: Keep as `draft` until the Purview control-plane position is reviewed by EA/OCDO/security stakeholders.

## 2. Executive takeaway

Microsoft Purview should be positioned as the enterprise data governance control plane for AI-relevant data assets, not as an AI runtime. PATH and HAIL should consume inherited data controls from Purview rather than recreate classification, lineage, audit, and policy controls per project.

```text
PATH governs AI execution. Purview governs data. HAIL runs workloads.
```

## 3. What is source-backed

- The Purview briefing frames Purview as the proposed enterprise data governance control plane for AI.
- The target-state architecture separates AI runtime responsibilities from data governance responsibilities.
- Purview is associated with data classification, lineage, auditability, policy evidence, and enterprise consistency.
- Current-state governance is described as fragmented and often recreated per project.
- Risks include M365-centric bias, PATH/Purview overlap, partial adoption being mistaken for full coverage, and unclear integration with non-M365 platforms.

## 4. Working interpretation

Purview should be treated as a control inheritance layer. PATH should wrap AI execution, while Purview provides the data-governance evidence that supports defensibility.

| Layer | Working role |
|---|---|
| Purview | Data classification, lineage, audit, metadata, policy evidence |
| PATH | AI runtime governance, onboarding, model/API access pattern, monitoring wrapper |
| HAIL | AI/analytics workload runtime and implementation proof point |
| Fabric / Databricks | Data processing, analytics, transformation, workload execution surfaces |
| Business applications | Domain workflows and program accountability |

## 5. Why it matters

Purview reduces the risk that each AI use case creates a new data-governance pattern. If data controls are inherited, ARB/TPO/security reviews can focus on whether the workload consumes the enterprise baseline correctly.

## 6. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Confirm Purview as enterprise data governance control plane | Proposed | OCDO / EA / Security | Needs formal position and scope |
| Define PATH/Purview boundary | Proposed | EA / PATH / OCDO | Needs architecture decision record |
| Confirm integration pattern for Fabric and Databricks | Open | Data platform owners / EA | Needs platform-specific mapping |
| Define minimum Purview evidence for AI workloads | Open | OCDO / ARB / Security | Needs intake checklist |
| Avoid assuming Purview coverage is complete | Active caveat | EA / Data governance | Needs coverage map |

## 7. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| M365-centric bias | Non-M365 platforms may remain under-governed | Define cross-platform coverage explicitly |
| PATH/Purview overlap | Duplicates governance responsibilities | Maintain execution-vs-data boundary |
| False sense of governance | Partial rollout may be mistaken for full enterprise control | Publish coverage map and gaps |
| Weak integration with Databricks/Fabric | AI workloads may bypass inherited controls | Define platform integration patterns |
| Overstating approval | EA interpretation may be mistaken for ratified architecture | Label as draft until reviewed |

## 8. Use in document-production pipeline

| Target artifact | How this intel informs it |
|---|---|
| AI Playbook | Defines inherited data-governance expectations for AI use cases |
| Data Architecture Plan | Positions Purview as the data governance control plane |
| ARB briefing | Provides control-plane separation language and risk framing |
| PATH / HAIL roadmap | Clarifies runtime vs data control responsibilities |
| Vendor/platform assessment | Asks whether tools integrate with enterprise data controls |
| Agent / voice KB | Gives a short explanation of Purview’s role in AI governance |

## 9. Retrieval tags

- purview
- data-control-plane
- data-governance
- classification
- lineage
- auditability
- metadata
- path
- hail
- fabric
- databricks

## 10. Graph extraction

### Concepts

- Purview
- data control plane
- data governance control plane
- data classification
- lineage
- auditability
- control inheritance
- Fabric
- Databricks
- PATH
- HAIL
- Protected B posture
- enterprise data governance

### Claims

- Purview should be positioned as the enterprise data governance control plane for AI-relevant data.
- PATH and HAIL should consume data governance controls rather than recreate them.
- AI projects should inherit data controls from the enterprise layer where possible.
- Partial Purview adoption should not be interpreted as full enterprise governance coverage.
- Data governance control-plane separation reduces duplication in AI review.

### Decisions

- Confirm Purview as enterprise data governance control plane.
- Define PATH/Purview boundary.
- Confirm Fabric and Databricks integration pattern.
- Define minimum Purview evidence for AI workloads.

### Risks

- M365-centric bias.
- PATH/Purview overlap.
- False sense of governance.
- Weak integration with non-M365 platforms.
- Overstating approval.

### Relationships

```text
Purview GOVERNS data classification
Purview GOVERNS data lineage
Purview SUPPORTS auditability
PATH CONSUMES Purview controls
HAIL CONSUMES Purview controls
Fabric REQUIRES Purview integration
Databricks REQUIRES Purview integration
Purview INFORMS Data Architecture Plan
Purview INFORMS AI Playbook
```

## 11. Open questions

- Has Purview’s enterprise data-governance control-plane role been formally ratified?
- What platforms are currently in scope for Purview integration?
- What evidence should ARB request to confirm inherited data controls?
- How will Purview coverage be represented in PATH Pattern Zero?
- What gaps remain for non-M365 data platforms and Protected B workloads?
