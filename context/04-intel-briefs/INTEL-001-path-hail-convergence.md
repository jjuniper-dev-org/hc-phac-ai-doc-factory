---
id: INTEL-001
title: "PATH / HAIL Convergence"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids: []
review_after: 2026-07-31
tags:
  - path
  - hail
  - foundry
  - databricks
  - pattern-zero
  - ai-platform
  - mlops
---

# INTEL-001 — PATH / HAIL Convergence

## 1. Status

- Classification: Unclassified working draft
- Document status: Draft
- Confidence level: Medium
- Last updated: 2026-06-23
- Owner / steward: EA / AI document factory working context
- Source basis: No formal source card exists for PATH or HAIL. This brief is built entirely from meeting-derived working interpretation, consistent with the source register's own classification of SRC-004 (PATH Agent Briefing) and SRC-005 (HAIL Agent Briefing) as "Working interpretation" / "Working" status — though note those register IDs do not correspond to any actual file in `context/02-source-cards/`, and the prior frontmatter values `SRC-PATH-BRIEFING`/`SRC-HAIL-BRIEFING` did not resolve to any file either.
- Evidence gap: No formal source card exists for PATH or HAIL as of this review (2026-06-25). All facts in this brief are working interpretation derived from internal meetings/discussions, not a citable document. This brief should not be promoted past `draft` until real PATH/HAIL source material is identified and source-carded.
- Review state: Needs human review before promotion to context pack; specifically needs real PATH/HAIL source material before any status change.
- Promotion recommendation: Keep as `draft` until real PATH/HAIL source material is identified and source-carded.

## 2. Executive takeaway

PATH has evolved from a technical SA&A / ATO enablement item into the emerging enterprise platform pattern for protected AI application hosting, governance, and operationalization. HAIL remains the operational runtime proof point. The direction is not merger; it is reconfiguration of responsibilities.

```text
HAIL runs workloads. PATH governs AI execution.
```

## 3. What is source-backed

- HAIL is the most concrete current operational AI runtime pattern.
- PATH is emerging as a protected AI service model and control-plane-enabled platform pattern.
- Foundry and Databricks are major technical components in the platform discussion.
- Governance, security, monitoring, logging, and operational controls are recurring requirements for AI workloads.

## 4. Working interpretation

PATH should be treated as the enterprise protected AI hosting and governance pattern. HAIL should be treated as the operational runtime proof point and AI workload environment.

This is not a consolidation story. It is a specialization story.

| Area | PATH | HAIL |
|---|---|---|
| Primary role | Protected platform model and governance wrapper | Operational AI runtime / workload environment |
| Governance | Common controls, patterns, monitoring, promotion path | Runtime evidence, experimentation, implementation lessons |
| Relationship | Defines reusable enterprise pattern | Proves and runs workloads |
| Risk | Could become another silo if not integrated | Could remain lab-like if not connected to enterprise path |

## 5. Pattern Zero

Any request for AI model/API access is a candidate request for the first reusable PATH pattern: approved model access wrapped with security, monitoring, logging, governance, and operational controls.

## 6. Why it matters

This gives ARB, TPO, DTB, OCDO, and program owners a clearer way to assess AI requests. A request for AI model access is not just a software request. It is a request for a governed execution pattern.

## 7. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Confirm PATH as platform-level AI hosting/governance pattern | Open | DTB / EA / TPO / OCDO | Formal governance confirmation |
| Confirm HAIL runtime role relative to PATH | Open | PHAC / DTB / EA | Formal operating model |
| Confirm Foundry access pattern | Open | Cloud / Security / EA | Technical and security approval |
| Confirm Databricks role | Open | Data / Platform / EA | Platform fit and governance model |
| Define Pattern Zero | Proposed | EA / AI governance | Needs ratification |

## 8. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| Overstating approval | Could imply decisions not yet made | Mark as working interpretation |
| PATH/HAIL confusion | Causes duplicated platform work | Maintain control/runtime distinction |
| Pattern Zero undefined | Every AI request becomes bespoke | Define reusable wrapper |
| Program accountability blurred | Business owners may assume platform owns decisions | Separate platform responsibility from program accountability |

## 9. Use in document-production pipeline

| Target artifact | How this intel informs it |
|---|---|
| AI Playbook | Explains where AI workloads should go and what governance wrapper is needed |
| Data Architecture Plan | Clarifies data/platform dependencies for AI execution |
| ARB briefing | Provides control/runtime split and architecture review frame |
| Platform roadmap | Supports PATH/HAIL sequencing and platform enablement |
| Agent / voice KB | Gives Ayla a short explanation of PATH vs HAIL |
| GitHub issues / dev bot tasks | Drives Pattern Zero and platform-intake tasks |

## 10. Graph extraction

### Concepts

- PATH
- HAIL
- Pattern Zero
- Foundry
- Databricks
- MLOps
- protected AI hosting
- platform-level responsibility
- program-level accountability

### Claims

- PATH has evolved into an enterprise platform pattern for protected AI application hosting and governance.
- HAIL remains the operational runtime proof point.
- PATH and HAIL should not be described as merging.
- Pattern Zero should become the standard entry point for AI model/API access.

### Decisions

- Confirm PATH platform role.
- Confirm HAIL runtime role.
- Confirm Pattern Zero as intake pattern.

### Risks

- Approval overstatement.
- Duplicated platform work.
- Weak ownership split.
- Unclear production path for AI workloads.

### Relationships

```text
PATH GOVERNS AI application hosting
HAIL RUNS AI workloads
PATH USES Foundry
PATH USES Databricks
Pattern Zero STANDARDIZES AI model/API access
Program owner RETAINS_ACCOUNTABILITY_FOR operational risk
PATH INFORMS AI Playbook
```

## 11. Open questions

- Has PATH’s platform role been formally ratified?
- What is the exact division of responsibilities between PATH and HAIL?
- Who owns Pattern Zero?
- What is the first approved implementation of Pattern Zero?
- How do Purview controls attach to PATH workloads?
