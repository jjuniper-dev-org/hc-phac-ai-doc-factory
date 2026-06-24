---
id: INTEL-011
title: "DADM / AIA Governance"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids:
  - SRC-DADM-AIA-PRIMARY
review_after: 2026-07-31
tags:
  - dadm
  - aia
  - automated-decision-making
  - responsible-ai
  - governance
  - accountability
---

# INTEL-011 — DADM / AIA Governance

## 1. Status

- Classification: Unclassified working draft
- Document status: Draft
- Confidence level: Medium
- Last updated: 2026-06-23
- Owner / steward: EA / AI governance working context
- Source basis: Directive on Automated Decision-Making and Algorithmic Impact Assessment primary-source pathway
- Review state: Needs source-card confirmation and human review

## 2. Executive takeaway

DADM / AIA is a primary governance source for automated decision systems and administrative decision-making. It should inform AI intake, Pattern Zero, ADM accountability, impact assessment, privacy/legal consultation, monitoring, recourse, and publication obligations.

Not every AI use case triggers DADM, but every AI use case still needs governance triage.

## 3. What is source-backed

To be completed from primary source cards. Expected source-backed areas include automated decision system definition, AIA timing, impact level, mitigation requirements, publication requirements, legal consultation, privacy consultation, procedural fairness, recourse, monitoring and updates, and human involvement.

## 4. Working interpretation

DADM/AIA should be treated as a mandatory decision gate for AI use cases that automate or support administrative decisions.

For non-DADM AI use cases, the same concepts still inform good governance: risk assessment, human oversight, logging, monitoring, transparency, recourse, privacy, legal review, bias and fairness analysis.

## 5. Why it matters

DADM/AIA provides the governance spine for higher-risk AI use cases. PATH Pattern Zero should include a DADM/AIA triage question so that model/API access is not separated from decision-risk assessment.

## 6. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Add DADM/AIA triage to AI intake | Proposed | OCDO / EA / TPO | Needs governance approval |
| Link Pattern Zero to AIA trigger assessment | Proposed | EA / PATH | Needs intake model |
| Define ADM accountability for AI-enabled applications | Open | Program ADM / Deputy Head delegate | Needs formal accountability model |
| Define publication and review path | Open | Program / OCDO | Needs source confirmation |

## 7. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| Over-applying DADM | Could slow low-risk productivity uses unnecessarily | Use triage, not blanket assumption |
| Under-applying DADM | Could miss mandatory obligations | Require AIA trigger assessment |
| Confusing advice with decision-making | RAG or drafting tools may influence decisions indirectly | Capture role of system in decision chain |
| Weak accountability | Platform teams may be mistaken for decision owners | Separate platform owner from program owner |

## 8. Use in document-production pipeline

| Target artifact | How this intel informs it |
|---|---|
| AI Playbook | Adds DADM/AIA triage and risk framing |
| Data Architecture Plan | Connects data quality, bias, classification, and lineage to decision risk |
| ARB briefing | Defines governance evidence required for automated decision systems |
| Platform roadmap | Adds DADM/AIA checks to Pattern Zero |
| Agent / voice KB | Lets Ayla distinguish DADM-triggering from non-DADM AI use |
| GitHub issues / dev bot tasks | Generates intake checklist and validation tasks |

## 9. Retrieval tags

- dadm
- aia
- automated-decision-making
- administrative-decision
- governance
- accountability
- recourse
- monitoring

## 10. Graph extraction

### Concepts

- DADM
- AIA
- automated decision system
- administrative decision
- impact level
- human involvement
- recourse
- monitoring
- publication
- privacy consultation
- legal consultation

### Claims

- DADM/AIA is primary governance context for automated decision systems.
- Not all AI use cases trigger DADM.
- All AI use cases should still be triaged for governance, privacy, security, and accountability.
- Pattern Zero should include a DADM/AIA trigger assessment.

### Decisions

- Define AI intake triage for DADM/AIA.
- Define AIA responsibility model.
- Define publication/update process.

### Risks

- Over-application.
- Under-application.
- Weak accountability.
- Inadequate human oversight.
- Poor evidence of monitoring and recourse.

### Relationships

```text
DADM GOVERNS automated decision systems
AIA ASSESSES automated decision systems
Pattern Zero REQUIRES DADM/AIA triage
Program owner RETAINS_ACCOUNTABILITY_FOR administrative decision use
PATH HOSTS AI-enabled applications
Purview SUPPORTS data governance evidence
```

## 11. Open questions

- Which current HC/PHAC AI use cases trigger DADM/AIA?
- Who signs off AIA completion and publication?
- How does ADM accountability map to PATH-hosted applications?
- How should DADM/AIA triage be embedded into Pattern Zero?
