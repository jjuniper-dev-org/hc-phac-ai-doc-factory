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
  - SRC-TBS-DIRECTIVE-AUTOMATED-DECISION-MAKING
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
- Last updated: 2026-06-25
- Owner / steward: EA / AI governance working context
- Source basis: TBS Directive on Automated Decision-Making, verbatim live fetch (`SRC-TBS-DIRECTIVE-AUTOMATED-DECISION-MAKING`), original effective date 2019-04-01 with a 2025-06-24 compliance-timeline amendment for pre-existing systems
- Review state: Source-backed facts now populated from the primary directive text. Still draft; still needs human review of the DADM-scope interpretation before promotion.
- Promotion recommendation: Keep as `draft`. Source-backed facts now exist (`SRC-TBS-DIRECTIVE-AUTOMATED-DECISION-MAKING`), but human review of the DADM-scope interpretation (which HC/PHAC systems actually meet the section 5.1/5.2 test) is still needed before any promotion.

## 2. Executive takeaway

DADM / AIA is a primary governance source for automated decision systems and administrative decision-making. It should inform AI intake, Pattern Zero, ADM accountability, impact assessment, privacy/legal consultation, monitoring, recourse, and publication obligations.

Not every AI use case triggers DADM, but every AI use case still needs governance triage.

## 3. What is source-backed

All facts below are drawn from `SRC-TBS-DIRECTIVE-AUTOMATED-DECISION-MAKING`, the verbatim text of the TBS Directive on Automated Decision-Making (live fetch, page-stated `dateModified: 2025-06-24`).

### Scope — the most important fact to get right

- Section 5.1 (verbatim): "This directive applies to any automated decision system in production used to make an administrative decision or a related assessment about a client."
- Section 5.2 (verbatim): "This directive excludes automated decision systems used solely for research and experimentation purposes, and those operating in test environments."
- "Production" (Appendix A) means in use and impacting real clients, including beta/user testing that produces client-impacting outputs. "Test environment" (Appendix A) means an environment that may mimic production but does not impact real clients, including exploration zones and sandboxes.
- **This directive is not a blanket AI governance instrument.** It applies only where an automated decision system is in production and is being used to make, or produce a related assessment supporting, an administrative decision about a client. A general-purpose productivity tool (e.g., a drafting-assistance chatbot) is not automatically in scope unless it is actually making or materially assisting an administrative decision as defined below.

### Core definitions (Appendix A, verbatim)

- "administrative decision": "Any decision that is made by an authorized official of a department as identified in section 8 of this directive pursuant to powers conferred by an Act of Parliament or an order made pursuant to a prerogative of the Crown that affects legal rights, privileges or interests."
- "automated decision system": "Any technology that either assists or replaces the judgment of human decision makers. These systems draw from fields like statistics, linguistics and computer science, and use techniques such as rules-based systems, regression, predictive analytics, machine learning, deep learning, and neural networks."
- "algorithmic impact assessment": "A framework to help departments better understand and reduce the risks associated with automated decision systems and to provide the appropriate requirements that best match the type of system being designed."

### Impact Assessment Levels (Appendix B)

Four levels (I-IV), each assessed across the same three axes (risk context, decision impact, data risk) at increasing severity:

- Level I: low risk context; little-to-no, easily reversible, brief decision impact; low data risk (e.g., non-personal/unclassified, structured data).
- Level II: moderate risk context; moderate, likely reversible, short-term decision impact; moderate data risk (personal/protected mix, structured or unstructured data).
- Level III: high risk context; high, difficult-to-reverse, potentially ongoing decision impact; high data risk (personal or protected information, unstructured data).
- Level IV: very high risk context; very high, irreversible, perpetual decision impact; very high data risk (personal, protected, or classified information; unstructured or incomplete data).

The AIA determines which level applies; the level determines which Appendix C requirements (notice, explanation, peer review, Gender-based Analysis Plus, training, human involvement, approval-to-operate) apply and at what intensity.

### Section 6 requirement categories

- **6.1 Algorithmic impact assessment**: complete, approve, and publish the AIA on the Open Government Portal before production; apply the Appendix C requirements the AIA determines; review/update on a scheduled basis and on functionality/scope change.
- **6.2 Transparency**: notice before decisions (all service channels, plain language, per the Canada.ca Content Style Guide); meaningful explanation after decisions, tiered by impact level; software-component access/licensing rights, including retained audit/test/monitor rights for proprietary components; documentation of decisions and assessments.
- **6.3 Quality assurance**: pre-production testing and in-production monitoring for accuracy, bias, and human-rights impacts (Charter, Canadian Human Rights Act, UNDRIP Act); data quality validation; data governance (traceability, lawful collection/use/retention/disclosure/disposal); peer review with panel composition/count tiered by impact level; Gender-based Analysis Plus; employee training tiered by impact level; security risk assessments and data/model integrity protections; legal consultation from the concept stage; ensuring human involvement tiered by impact level; tiered approval-to-operate.
- **6.4 Recourse**: informing clients of timely, effective, easy-to-access recourse options to challenge the administrative decision.
- **6.5 Reporting**: publishing effectiveness/efficiency information and fairness/human-rights information on the Open Government Portal.

### Tiered approval-to-operate (section 6.3.14 / Appendix C)

- Level I/II: assistant deputy minister responsible for the program.
- Level III: deputy head.
- Level IV: Treasury Board — except agents of Parliament, whose own heads approve Level IV systems (section 8.3.5).

### Application and compliance timeline

- Section 8: applies to all institutions subject to the Policy on Service and Digital (8.1); other institutions are encouraged but not required to comply (8.2); seven named agents of Parliament are subject with specific carve-outs from sections 6.2.2.1 and 7.4, and from AIA-publication/reporting requirements (8.3.1-8.3.4).
- Effective April 1, 2019, compliance required by April 1, 2020 (section 1.1), applying to systems developed/procured after that date (section 1.2).
- 2025-06-24 amendment (section 1.2.1): existing automated decision systems developed or procured before June 24, 2025 have until June 24, 2026 to comply with new/updated requirements. Agents of Parliament also have until June 24, 2026 to comply (section 1.2.2).

## 4. Working interpretation

DADM/AIA should be treated as a mandatory decision gate for AI use cases that meet the directive's own scope test (section 5.1/5.2): a production system making, or producing a related assessment supporting, an administrative decision (as statutorily/prerogative-defined in Appendix A) about a client. This is now more defensible than before, because the scope test is the directive's explicit text, not an inference — it is a narrow, two-part test (production + administrative-decision-or-related-assessment), not a general "uses AI" test.

For AI use cases that do not meet that test — including R&D/test-environment systems (explicitly excluded by 5.2) and general-purpose productivity tools that do not make or materially assist an administrative decision — DADM/AIA does not apply by its own terms. The same underlying concepts still inform good governance as a matter of policy choice, not directive obligation: risk assessment, human oversight, logging, monitoring, transparency, recourse, privacy, legal review, bias and fairness analysis.

The practical triage question is therefore not "does this use AI?" but "is this a production system that makes or materially assists an administrative decision about a client?" Getting this distinction wrong in either direction is itself flagged as a risk in section 7.

## 5. Why it matters

DADM/AIA provides the governance spine for higher-risk AI use cases. PATH Pattern Zero should include a DADM/AIA triage question so that model/API access is not separated from decision-risk assessment.

## 6. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Add DADM/AIA triage to AI intake, using the section 5.1/5.2 production + administrative-decision test verbatim | Proposed | OCDO / EA / TPO | Needs governance approval; directive text itself now confirmed, but no HC/PHAC system has been triaged against it |
| Link Pattern Zero to AIA trigger assessment | Proposed | EA / PATH | Needs intake model |
| Define ADM accountability for AI-enabled applications, consistent with the directive's tiered approval-to-operate (ADM for Level I/II, deputy head for Level III, Treasury Board for Level IV) | Open | Program ADM / Deputy Head delegate | Needs formal accountability model mapping HC/PHAC program structure to these tiers |
| Define publication and review path for any HC/PHAC AIA (Open Government Portal, per 6.1.1/6.1.3) | Open | Program / OCDO | Directive requirement now confirmed; HC/PHAC-specific process still undefined |
| Track the 2025-06-24 compliance-timeline amendment (section 1.2.1) against any existing HC/PHAC automated decision system developed/procured before that date | Open | OCDO / EA / Program owners | No inventory yet exists of HC/PHAC systems that would fall under the June 24, 2026 compliance deadline |

## 7. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| Over-applying DADM | Treating any AI use as DADM-scoped contradicts the directive's own section 5.1/5.2 text and could slow low-risk productivity uses unnecessarily | Apply the explicit production + administrative-decision test verbatim; do not default to "AI implies DADM" |
| Under-applying DADM | Could miss mandatory obligations for systems that do meet the section 5.1 test (in production, making/assisting an administrative decision) | Require an AIA trigger assessment using the directive's own scope test for every candidate system |
| Confusing advice with decision-making | RAG or drafting tools may influence decisions indirectly without being "in production used to make an administrative decision" themselves | Capture the system's actual role in the decision chain; only systems materially assisting the decision (not general drafting/retrieval support) meet the section 5.1 test |
| Weak accountability | Platform teams may be mistaken for decision owners | Separate platform owner from program owner; approval-to-operate tiers (Appendix C) assign authority to ADM/deputy head/Treasury Board, not platform teams |
| Missing the 2025-06-24 compliance deadline | Pre-existing systems (developed/procured before June 24, 2025) have only until June 24, 2026 to meet new/updated requirements; missing this is a compliance gap, not just a governance nicety | Inventory any HC/PHAC automated decision system that predates June 24, 2025 and track its compliance status against the June 24, 2026 deadline |

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
- production
- test environment
- impact assessment level
- human involvement
- recourse
- monitoring
- publication
- privacy consultation
- legal consultation
- approval to operate

### Claims

- DADM/AIA is primary governance context for automated decision systems, but only within its own stated scope.
- The directive applies only to automated decision systems in production used to make an administrative decision or related assessment about a client (section 5.1), and explicitly excludes research/experimentation and test-environment systems (section 5.2).
- Not all AI use cases trigger DADM; the trigger is the section 5.1/5.2 scope test, not AI usage generally.
- All AI use cases should still be triaged for governance, privacy, security, and accountability, even when DADM/AIA does not formally apply.
- Pattern Zero should include a DADM/AIA trigger assessment using the directive's own scope test.
- Existing automated decision systems developed/procured before June 24, 2025 have until June 24, 2026 to comply with new/updated requirements (section 1.2.1).
- Approval-to-operate authority is tiered by impact level: ADM (I/II), deputy head (III), Treasury Board (IV), with agents-of-Parliament heads approving their own Level IV systems.

### Decisions

- Define AI intake triage for DADM/AIA using the section 5.1/5.2 scope test.
- Define AIA responsibility model, including ADM/deputy head/Treasury Board approval tiers.
- Define publication/update process for HC/PHAC AIAs on the Open Government Portal.
- Inventory HC/PHAC systems against the 2025-06-24 / 2026-06-24 compliance-timeline amendment.

### Risks

- Over-application (treating all AI as DADM-scoped).
- Under-application (missing systems that meet the section 5.1 test).
- Weak accountability (platform teams mistaken for decision owners).
- Inadequate human oversight.
- Poor evidence of monitoring and recourse.
- Missing the June 24, 2026 compliance deadline for pre-existing systems.

### Relationships

```text
DADM GOVERNS automated decision systems IN_SCOPE_WHEN production AND administrative decision
DADM EXCLUDES research/experimentation systems
DADM EXCLUDES test environment systems
AIA ASSESSES automated decision systems
AIA DETERMINES impact assessment level
impact assessment level DETERMINES approval to operate tier
Pattern Zero REQUIRES DADM/AIA triage
Program owner RETAINS_ACCOUNTABILITY_FOR administrative decision use
PATH HOSTS AI-enabled applications
Purview SUPPORTS data governance evidence
```

## 11. Open questions

- Which current HC/PHAC AI use cases meet the section 5.1 production + administrative-decision test, as distinct from general productivity/drafting use?
- Who signs off AIA completion and publication for HC/PHAC systems, and at what approval-to-operate tier (ADM, deputy head, or Treasury Board) per Appendix C?
- How does ADM accountability map to PATH-hosted applications, given the directive assigns approval-to-operate to program ADMs/deputy heads, not platform owners?
- How should DADM/AIA triage be embedded into Pattern Zero?
- Does any existing HC/PHAC automated decision system predate June 24, 2025, and if so, what is its plan to meet the June 24, 2026 compliance deadline under section 1.2.1?
- Is the Algorithmic Impact Assessment tool's current question set (the live online instrument, not yet independently reviewed per the source card's evidence gaps) consistent with the impact-level framework summarized here?
