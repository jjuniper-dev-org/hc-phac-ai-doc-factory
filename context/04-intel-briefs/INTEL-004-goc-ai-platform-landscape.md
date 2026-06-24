---
id: INTEL-004
title: "GoC AI Platform Landscape"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids:
  - SRC-GOC-AI-PLATFORM-INTELLIGENCE
review_after: 2026-07-31
tags:
  - goc-ai-platforms
  - canchat
  - copilot
  - gctranslate
  - radia
  - path
  - hail
  - maplept
  - platform-landscape
---

# INTEL-004 — GoC AI Platform Landscape

## 1. Status

- Classification: Unclassified working draft
- Document status: Draft
- Confidence level: Medium
- Last updated: 2026-06-24
- Owner / steward: EA / AI document factory working context
- Source basis: GoC AI Platform Intelligence — HC/PHAC EA working intelligence
- Review state: Working interpretation only; not a citeable GC policy position
- Promotion recommendation: Keep as `draft` until platform claims are refreshed and separated into source cards by tool/platform.

## 2. Executive takeaway

The current GC AI landscape should be treated as a fragmented set of tools, services, and partial runtime patterns rather than a single coherent enterprise AI platform. For HC/PHAC, this strengthens the case for PATH as a governed enterprise AI control plane and for HAIL as the current operational runtime proof point.

```text
GC tools solve pieces of the AI landscape. HC/PHAC still needs a governed control plane for protected enterprise AI execution.
```

## 3. What is source-backed

- The source briefing identifies CANChat, Microsoft Copilot, GCTranslate, RADIA, PATH, HAIL, and MaplePT as distinct elements in the current AI tool landscape.
- The source briefing characterizes the landscape as fragmented and not yet a unified governed AI control plane.
- GCTranslate is identified as a clearer vertical AI service pattern.
- Copilot is identified as embedded AI inside existing systems of record and permission layers.
- HAIL is positioned as an active operational runtime pattern, while PATH is positioned as the intended governed HC/PHAC control-plane/service model.
- The source explicitly warns that EA interpretation must not be presented as formal GC strategy or approved architecture.

## 4. Working interpretation

The landscape should be presented as a capability map, not as a procurement shopping list. Each tool occupies a different architectural layer:

| Capability / tool | Working architectural role |
|---|---|
| CANChat | Workforce productivity and multi-model interaction surface |
| M365 Copilot | Embedded assistant in M365 data and permission context |
| GCTranslate | Governed vertical AI service pattern for translation |
| RADIA | Historical runtime/orchestration signal; not a current active dependency |
| PATH | Target governed AI control-plane/service model for HC/PHAC |
| HAIL | Operational runtime and implementation proof point |
| MaplePT | Horizon-scan signal for sovereign foundation-model options |

This framing helps avoid two bad decisions: treating all AI tools as equivalent, or assuming that any single existing tool solves enterprise protected AI governance.

## 5. Why it matters

ARB, TPO, OCDO, and platform owners need a shared vocabulary for where each AI tool fits. Otherwise, productivity tools, vertical services, runtime environments, and enterprise control-plane patterns will be compared as if they solve the same problem.

For HC/PHAC, the core architecture question is not “which AI tool do we buy?” but “which layer is this use case asking for, and what controls must be inherited?”

## 6. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Confirm target AI control-plane role for PATH | Proposed | DTB / EA / TPO / OCDO | Needs formal architecture decision |
| Confirm HAIL runtime role relative to PATH | Proposed | PHAC / DTB / EA | Needs convergence model |
| Define where CANChat fits for Protected B or workflow use | Open | OCDO / Security / DTB | Needs approved usage pattern |
| Define GCTranslate API/platform integration posture | Open | OCDO / DTB / PSPC interface | Needs service integration evidence |
| Maintain horizon scan for Canadian/sovereign models | Watch | EA / OCDO | Needs policy and platform evaluation |

## 7. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| Tool equivalence error | Productivity tools may be mistaken for enterprise runtime | Maintain layer map |
| Overclaiming GC alignment | Working intelligence may be treated as policy | Mark as EA interpretation |
| PATH/HAIL divergence | Separate runtime/control assumptions could harden | Require convergence architecture |
| Duplicative procurement | Programs may buy vertical tools without pattern reuse | Route through capability and pattern assessment |
| Weak Protected B posture | Public or productivity AI surfaces may not meet workload needs | Use classification and control triage |

## 8. Use in document-production pipeline

| Target artifact | How this intel informs it |
|---|---|
| AI Playbook | Provides “which AI surface fits which problem?” guidance |
| ARB briefing | Separates productivity, vertical service, runtime, and control-plane layers |
| Procurement rubric | Helps evaluate whether a proposed tool duplicates an existing capability |
| PATH / HAIL convergence deck | Supports control-plane/runtime distinction |
| Executive briefing | Explains why fragmentation creates governance and investment risk |
| Agent / voice KB | Lets the assistant answer “where does CANChat/Copilot/GCTranslate fit?” |

## 9. Retrieval tags

- goc-ai-platforms
- canchat
- copilot
- gctranslate
- radia
- path
- hail
- maplept
- ai-control-plane
- platform-landscape

## 10. Graph extraction

### Concepts

- CANChat
- M365 Copilot
- GCTranslate
- RADIA
- PATH
- HAIL
- MaplePT
- AI control plane
- productivity interface
- vertical AI service
- runtime layer
- foundation model layer
- Protected B posture

### Claims

- The current GC AI landscape is fragmented rather than a single coherent enterprise AI platform.
- PATH is the intended HC/PHAC governed AI control-plane/service model.
- HAIL is the active operational runtime proof point.
- GCTranslate is a vertical governed AI service pattern.
- Copilot embeds AI inside existing systems of record and permission layers.
- EA platform intelligence must not be represented as formal GC policy.

### Decisions

- Confirm PATH target control-plane role.
- Confirm HAIL runtime convergence role.
- Define CANChat usage pattern.
- Define GCTranslate integration posture.
- Maintain sovereign model horizon scan.

### Risks

- Tool equivalence error.
- Overclaiming GC alignment.
- PATH/HAIL divergence.
- Duplicative procurement.
- Weak Protected B posture.

### Relationships

```text
CANChat SUPPORTS productivity interface
Copilot EMBEDS AI in M365 workflows
GCTranslate PROVIDES vertical AI service
PATH GOVERNS AI control plane
HAIL RUNS AI workloads
MaplePT SIGNALS sovereign model option
PATH REQUIRES HAIL convergence model
AI Playbook USES platform landscape
Procurement rubric USES platform landscape
```

## 11. Open questions

- What GC tools are formally approved for which data classifications and workflow types?
- What is the approved role of CANChat relative to M365 Copilot and PATH?
- Can GCTranslate be consumed through an approved API pattern for HC/PHAC workflows?
- What architecture decision will formally resolve PATH/HAIL convergence?
- Which tool categories should be treated as enterprise capabilities versus local program tools?
