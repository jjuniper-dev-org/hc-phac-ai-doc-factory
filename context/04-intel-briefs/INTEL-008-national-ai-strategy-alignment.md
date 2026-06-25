---
id: INTEL-008
title: "National AI Strategy Alignment"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids:
  - SRC-ISED-AI-FOR-ALL-NATIONAL-AI-STRATEGY
review_after: 2026-12-08
tags:
  - national-ai-strategy
  - ised
  - ai-for-all
  - sovereign-compute
  - health-sector-data-space
  - vital
  - ai-missions
  - ai-safety-institute
  - public-service-delivery
---

# INTEL-008 — National AI Strategy Alignment

## 1. Status

- Classification: Unclassified working draft
- Document status: Draft
- Confidence level: Medium
- Last updated: 2026-06-25
- Owner / steward: EA / AI document factory working context
- Source basis: ISED's published national strategy, "Canada's National Artificial Intelligence Strategy: AI for All" (`SRC-ISED-AI-FOR-ALL-NATIONAL-AI-STRATEGY`)
- Review state: Working interpretation only; not a citeable HC/PHAC policy position. The source is a Government of Canada national strategy document, not an HC/PHAC document.

## 2. Executive takeaway

Canada's national AI strategy names health and life sciences as one of five priority sectors and commits its first AI Mission ($200 million) to health outcomes nationally, alongside $200 million in new health-data infrastructure investment (Health Sector Data Space with CIHI, and VITAL expansion) and a sovereign-compute "build-partner-buy" posture. None of this names Health Canada or PHAC, and none of it constitutes a department-specific funding or implementation commitment. For HC/PHAC, the strategy is best read as national context that may create future intersections with HC/PHAC's data and platform work (sovereignty, governance, health data infrastructure) — not as a current resource or mandate.

```text
The national strategy sets a health-sector and sovereign-AI agenda at the country level. Whether and how HC/PHAC connects to it (AI Mission funding, Health Sector Data Space, VITAL) is not stated and remains open.
```

## 3. What is source-backed

- The strategy sets out six pillars (trust, opportunity, sovereignty) and names five priority sectors, including health and life sciences.
- The first AI Mission commits $200 million "towards improving health outcomes for Canadians," described as a national mission, not a department-specific program.
- The strategy commits $100 million to launch a Health Sector Data Space with CIHI, and a further $100 million to expand VITAL (a pan-Canadian health-data platform) into five additional provinces.
- The strategy cites institutional/provincial health-AI examples (CHARTWatch at St. Michael's Hospital, Amii's Okaki and Jenkins tools in Alberta, Vector Institute cancer/stroke research) — none of which are federal or HC/PHAC deployments.
- Pillar 4 commits to a "build-partner-buy" approach to sovereign AI infrastructure across compute, cloud, connectivity, data, and talent, including a planned public supercomputer and large compute-capacity expansions.
- Pillar 3 commits to public-service-delivery AI principles: human-in-the-loop oversight, transparency, privacy, and accountability standards, delivered through the Office of Digital Transformation.
- Pillar 1 commits $50 million to expand the Canadian AI Safety Institute, plus a Canada Trusted AI Certification program, AI watermarking work, and a continuing Privacy Act review.
- The strategy text does not mention Health Canada or PHAC anywhere.

## 4. Working interpretation

The strategy should be read as a signal of national direction and potential future funding/governance pressure, not as a current resource for HC/PHAC. Three working interpretations:

| Theme | Interpretation |
|---|---|
| AI Mission health funding | A future mechanism HC/PHAC may want to track or seek participation in, but not a current allocation — no department-specific commitment exists in the source. |
| Health Sector Data Space / VITAL | National health-data infrastructure investments that could eventually intersect with HC/PHAC data holdings or surveillance systems (see `INTEL-002`), but the source names CIHI and provincial hospital networks as the connected parties, not HC/PHAC. |
| Sovereign compute / build-partner-buy | Reinforces the same sovereignty and governed-control-plane logic already driving HC/PHAC's PATH/HAIL work (`INTEL-004`), at a national rather than departmental scale. |

## 5. Why it matters

If HC/PHAC's AI Playbook, ARB briefings, or platform roadmap reference "alignment with national AI strategy," this brief is the evidence base for what that strategy actually says — and, just as important, for what it does not say about HC/PHAC. Treating the strategy's health-sector emphasis as an implicit HC/PHAC mandate or funding source would be an evidence-gap error; this brief exists to prevent that by keeping the source-backed national framing separate from any HC/PHAC-specific claim.

## 6. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Determine whether HC/PHAC should pursue engagement with the AI Missions Program (health mission, $200M) | Open | EA / DTB / PHAC policy | Strategy does not name HC/PHAC as a recipient or delivery partner; no application or eligibility process is described in the source |
| Determine whether HC/PHAC has or should seek a role in the Health Sector Data Space (CIHI partnership, $100M) | Open | EA / DTB / PHAC EA | Source names CIHI as the named partner; HC/PHAC's relationship to CIHI in this initiative is not addressed |
| Determine whether VITAL's provincial hospital-data expansion has any touchpoint with HC/PHAC surveillance or data-holding mandates | Open | PHAC EA / Data Strategy owners | Source describes VITAL as connecting "clinical data from hospitals across multiple provinces"; no federal department role is stated |
| Reconcile national build-partner-buy sovereign-compute posture with HC/PHAC's existing PATH/HAIL platform choices | Open | EA / TPO / OCDO | Strategy speaks at national infrastructure scale; no HC/PHAC-specific compute/cloud decision is implied or required by the source |
| Assess whether national public-service-delivery commitments (human-in-the-loop, transparency, Office of Digital Transformation procurement acceleration) create new expectations for PATH/HAIL/CANChat governance | Open | EA / Security / OCDO | Source states general GC commitments; does not reference PATH, HAIL, CANChat, or any HC/PHAC governance artifact directly |

## 7. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| Overclaiming HC/PHAC relevance | The strategy's health-sector emphasis could be misread internally as a funding or mandate signal specific to HC/PHAC | Keep "national strategy" and "HC/PHAC commitment" explicitly separate in all downstream artifacts; cite this brief's evidence-gap section |
| Premature resource planning | Teams may plan around AI Mission or Health Sector Data Space funding that has no stated HC/PHAC allocation | Treat as a watch item, not a budget line, until a department-specific commitment is published |
| Sovereignty-narrative conflation | National sovereign-compute framing (Pillar 4) could be cited to justify specific PATH/HAIL architecture decisions it does not actually address | Use `INTEL-004` for HC/PHAC-specific platform claims; use this brief only for national-context framing |
| Governance-expectation creep | National human-in-the-loop/transparency commitments could be cited as if they were binding HC/PHAC policy | Confirm any such expectation through HC/PHAC's own governance channels (WF10, DADM-AIA per `INTEL-011`) before treating it as a requirement |

## 8. Use in document-production pipeline

| Target artifact | How this intel informs it |
|---|---|
| AI Playbook | Provides national-strategy context section, clearly scoped as background, not HC/PHAC direction |
| ARB briefing | Gives ARB a accurate summary of what the national strategy does and does not commit to for health/HC/PHAC |
| Executive briefing | Lets leadership distinguish "national ambition" from "departmental resourcing" when asked about AI strategy alignment |
| Platform roadmap | Cross-references `INTEL-004`'s PATH/HAIL sovereignty framing against the national build-partner-buy posture |
| Agent / voice KB | Lets the assistant correctly answer "does the national AI strategy fund HC/PHAC AI work?" with a source-backed "not stated" |
| GitHub issues / dev bot tasks | Anchors any future issue proposing HC/PHAC engagement with AI Missions Program or Health Sector Data Space in accurate source claims |

## 9. Retrieval tags

- national-ai-strategy
- ised
- ai-for-all
- sovereign-compute
- health-sector-data-space
- vital
- ai-missions
- ai-safety-institute
- public-service-delivery
- human-in-the-loop

## 10. Graph extraction

### Concepts

- AI for All (national AI strategy)
- six pillars (trust, opportunity, sovereignty)
- health and life sciences priority sector
- AI Missions Program
- Health Sector Data Space
- VITAL
- CIHI
- sovereign AI foundation
- build-partner-buy
- Canadian AI Safety Institute
- Office of Digital Transformation
- human-in-the-loop
- PATH
- HAIL
- CANChat
- DADM-AIA

### Claims

- The national strategy names health and life sciences as a priority sector and commits its first AI Mission ($200M) to health outcomes nationally, without naming HC/PHAC.
- The national strategy commits $200M combined to Health Sector Data Space (with CIHI) and VITAL expansion, both described as national/provincial infrastructure, not HC/PHAC programs.
- The national strategy's sovereign-compute "build-partner-buy" posture parallels but does not specify HC/PHAC's PATH/HAIL control-plane work.
- The national strategy's public-service-delivery commitments (human-in-the-loop, transparency, accountability) parallel but do not specify HC/PHAC's existing PATH/HAIL/CANChat governance work.
- HC/PHAC's relationship to any of the above remains unaddressed by the source and is an open question, not a confirmed alignment.

### Decisions

- Determine whether to pursue AI Missions Program engagement.
- Determine whether to seek a role in the Health Sector Data Space.
- Assess VITAL's relevance to HC/PHAC data holdings.
- Reconcile national sovereign-compute posture with PATH/HAIL.
- Assess national public-service-delivery commitments against existing HC/PHAC AI governance.

### Risks

- Overclaiming HC/PHAC relevance.
- Premature resource planning.
- Sovereignty-narrative conflation.
- Governance-expectation creep.

### Relationships

```text
INTEL-008 RELATES_TO INTEL-004 ON sovereign compute and control-plane framing
INTEL-008 RELATES_TO INTEL-002 ON health-data infrastructure and AI readiness
INTEL-008 RELATES_TO INTEL-001 ON PATH/HAIL convergence as HC/PHAC's own control-plane question
INTEL-008 RELATES_TO INTEL-003 ON data-platform/control-plane themes (Purview)
INTEL-008 RELATES_TO INTEL-005 ON decision-assurance patterns relevant to AI Mission/governance decisions
INTEL-008 RELATES_TO INTEL-011 ON DADM-AIA governance as the existing HC/PHAC AI accountability mechanism
AI for All strategy DOES_NOT_NAME Health Canada
AI for All strategy DOES_NOT_NAME PHAC
```

## 11. Open questions

- Has any GC or ISED follow-up document named HC/PHAC as a participant in the AI Missions Program health mission?
- Has CIHI's Health Sector Data Space published a participant list that includes HC/PHAC or any HC/PHAC data holding?
- Does VITAL's clinical-data network intersect with any PHAC surveillance system (per `INTEL-002`'s reference to 50+ active surveillance systems)?
- Will national build-partner-buy sovereign-compute investments (supercomputer, Compute Access Fund expansion) be accessible to HC/PHAC, or are they scoped to SMEs and broader public/private compute users as stated in the source?
- Does the Office of Digital Transformation's federal AI procurement acceleration intersect with HC/PHAC's own AI procurement or PATH/HAIL governance processes?
