---
id: INTEL-006
title: "HC/PHAC Data Strategy Alignment"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids:
  - SRC-HC-DATA-STRATEGY-2019
  - SRC-PHAC-DATA-STRATEGY-2025-2028
review_after: 2026-07-31
tags:
  - hc-data-strategy
  - phac-data-strategy
  - data-governance
  - enterprise-architecture
  - currency-gap
  - interoperability
  - ai-readiness
---

# INTEL-006 — HC/PHAC Data Strategy Alignment

## 1. Status

- Classification: Unclassified working draft
- Document status: Draft
- Confidence level: Medium
- Last updated: 2026-06-25
- Owner / steward: EA / AI document factory working context
- Source basis: Health Canada Data Strategy (2019) source card and PHAC Data Strategy 2025/26–2027/28 source card
- Review state: Suitable for draft document production; not accepted context

## 2. Executive takeaway

Health Canada and PHAC each have their own named Data Strategy, but they are not parallel documents: HC's (2019) is an enterprise-wide strategy spanning all HC programs, while PHAC's (2025/26–2027/28) is a health-data/surveillance-specific renewal six years newer. The two documents also describe an explicit, asymmetric structural dependency — PHAC's data strategy is stated to depend on HC's internal services (HR, IM, IT, enterprise architecture) — which predates PHAC's current strategy and has not been revisited in any source reviewed here. This brief keeps HC-specific, PHAC-specific, and shared-relationship facts separated so neither strategy is read as representing the other.

```text
HC Data Strategy (2019, enterprise-wide) + PHAC Data Strategy (2025-28, health-data-specific)
  -> distinct scopes, 6-year vintage gap, asymmetric dependency (PHAC depends on HC), not yet reconciled
```

## 3. What is source-backed

### HC-specific (per SRC-HC-DATA-STRATEGY-2019)

- HC's Data Strategy (October 2019) is described as the first of its kind for the department, developed in response to the Privy Council's November 2018 Data Strategy Roadmap for the Federal Public Service.
- Vision: "Effectively use data as an asset to provide credible information, reliable advice and quality services."
- Five guiding principles: Everyone is Responsible; Sharing and Reuse; Maximize Value; Enterprise Tools and Training; Leverage Governance and Stewardship.
- Three foundation pillars: People and Culture; Governance; Environment and Digital Infrastructure.
- HC's programs fall under two core responsibilities: Health Care Systems, and Health Protection and Promotion — i.e., the strategy spans regulatory/health-protection work as well as health-systems work, not health-surveillance data alone.
- 2019 Gartner-facilitated maturity assessment rated HC as approaching Level 2 "Developing" (scale 0 Nascent–5 Optimizing).
- A new Chief Data Officer role for HC was stated as forthcoming "in the coming months" as of October 2019.
- Concrete examples: Project Cyclops (label-scanning inspection app), Cannabis Tracking and Licensing System (CTLS) business intelligence, and Solutions Fund AI/ML pilots in Healthy Environments and Consumer Safety Branch (systematic-review AI proof of concept) and Regulatory Operations and Enforcement Branch (AI/ML on inspection data).
- The strategy self-describes as "evergreen," intended to evolve over time rather than function as a fixed one-time document.

### PHAC-specific (per SRC-PHAC-DATA-STRATEGY-2025-2028)

- PHAC's renewed Data Strategy covers 2025/26–2027/28 and focuses on health data specifically, not all corporate data.
- PHAC operates more than 50 active surveillance systems relying on more than 180 sources; provinces/territories represent 64 percent of frequently reported data providers and hospitals/healthcare settings represent 28 percent.
- Four priorities: effective data governance; connected data and systems; a culture of data stewardship; a data-literate workforce.
- Priority 1 explicitly includes AI integration as a data-governance issue and calls for collaboration with HC-DTB on a public-health-focused data architecture.
- Strategy emphasizes FAIR/CARE principles, OCAP and Indigenous data sovereignty, SGBA+, anti-racism, and disaggregated data.
- The afterword states PHAC must formalize AI best practices in data governance structures to responsibly leverage AI for public health action.

### Explicitly stated HC-PHAC relationship

- HC's 2019 strategy states directly: **"The Public Health Agency of Canada's Data Strategy is also highly dependant upon Health Canada's internal services for human resources, information management, information technology, and enterprise architecture."** This is a one-directional structural dependency — PHAC depends on HC, not the reverse — stated in HC's own document, not inferred.
- Shared infrastructure: SAS Grid is described in the 2019 HC document as "a key foundational data infrastructure for both Health Canada and the Public Health Agency of Canada (PHAC)," used by 520 epidemiologists, statisticians, and data scientists across ten HC/PHAC branches.
- The DG-Science forum is described as bringing together Health Portfolio partners: Health Canada, PHAC, CIHR, and CFIA.
- HC's 2019 "Delivering on our Data Priorities" section states internal service providers "will need to understand the needs of branches and PHAC, working together collaboratively."
- PHAC's 2025-28 strategy (Priority 1) separately calls for collaboration with "HC-DTB" on a public-health-focused data architecture — a newer, narrower collaboration touchpoint than the 2019 broad internal-services dependency statement, but it is not stated in either source as superseding or revising that 2019 dependency.

## 4. Working interpretation

HC's 2019 strategy is enterprise-wide: it covers both of HC's core responsibilities (health care systems financing/policy work, and health protection/promotion regulatory work spanning consumer products, food, pesticides, cannabis, and controlled substances). PHAC's 2025-28 strategy is narrower and domain-specific: it is scoped to health data and built around PHAC's surveillance-system landscape. These are not competing or duplicate strategies — they are different altitudes of the same overall HC/PHAC data environment.

The explicit 2019 dependency statement (PHAC depends on HC for HR, IM, IT, and enterprise architecture) is a real structural fact, not a soft collaboration claim, and it predates PHAC's current strategy by six years. Because PHAC's 2025-28 strategy independently calls for a new "public-health-focused data architecture" in partnership with HC-DTB, there is an open tension worth naming: PHAC's newer strategy appears to be asking for architecture tailored to its own needs, while the older HC document frames PHAC's IT/architecture posture as dependent on HC's internal-services structures. Whether the underlying dependency has loosened, been formalized differently, or remains structurally intact as described in 2019 cannot be determined from these two sources alone.

The six-year vintage gap (2019 vs. 2025-28) is itself a gap worth flagging on its own terms, independent of the dependency question: HC's maturity rating, CDO-role status, and stated AI pilot activity are all 2019 snapshots, while PHAC's strategy reflects 2025-26 planning assumptions. Any reconciliation that treats both documents as equally current would overstate HC's currency and understate how much has likely changed in HC's data posture since 2019.

## 5. Why it matters

AI-readiness assessments (see INTEL-002) need to know which strategy governs which scope. Treating PHAC's surveillance-specific 2025-28 priorities as if they describe HC's enterprise-wide posture (or vice versa) risks misapplying governance gates, misattributing maturity levels, or assuming HC's internal-services posture is more current than it actually is. The explicit dependency statement also matters operationally: if PHAC's AI ambitions (e.g., Priority 1's AI integration goal) require IT/EA capacity that is structurally provided by HC, then HC's own data/EA maturity (rated "Developing" in 2019, with unknown current status) is a direct constraint on PHAC's ability to deliver its newer strategy — not just a loosely related fact.

## 6. Decisions implied or needed

| Decision | Status | Owner | Evidence gap |
|---|---|---|---|
| Confirm whether HC's 2019 data strategy/maturity posture has been formally updated since 2019 | Open | HC CDO / EA | No newer standalone HC document found; departmental plans reference it by name but do not republish it |
| Determine whether the 2019 "PHAC depends on HC internal services" statement still holds given PHAC's newer 2025-28 strategy | Open | HC CDO / PHAC CDO / EA | Neither source confirms or revises the 2019 statement; PHAC's HC-DTB collaboration ask (Priority 1) may be a partial successor but this is not stated explicitly |
| Reconcile HC's enterprise-wide maturity rating (2019: approaching Level 2 "Developing") against PHAC's current AI-integration ambitions | Open | OCDO / PHAC CDO / EA | Needs a current HC maturity assessment; 2019 figure may be stale |
| Decide whether INTEL-002's AI-readiness triage should be gated separately for HC-wide vs. PHAC-specific data assets | Proposed | OCDO / EA | Needs scope-tagging convention across intel briefs |

## 7. Risks and caveats

| Risk | Why it matters | Mitigation |
|---|---|---|
| Treating the 2019 HC strategy as current | HC's maturity rating, CDO status, and AI pilots described are 6+ years old; assuming no change overstates HC's data-governance readiness | Always pair HC-2019 facts with the currency caveat; do not cite the 2019 maturity rating as HC's current state without flagging staleness |
| Reversing or softening the dependency direction | The source states PHAC depends on HC, not a mutual or HC-depends-on-PHAC relationship; softening this into generic "collaboration" language would misrepresent a structural fact | Always quote the dependency statement verbatim when cited; do not paraphrase it as bidirectional |
| Assuming PHAC's HC-DTB collaboration ask (2025-28, Priority 1) supersedes the 2019 dependency statement | No source states this; it is a plausible but unconfirmed inference | Flag as an open question, not a resolved fact |
| Blending HC-wide and PHAC-specific claims in downstream documents | Risks the exact problem this brief and issue #11 exist to prevent | Keep HC and PHAC facts in clearly labeled sub-sections in any document that draws on both sources |

## 8. Use in document-production pipeline

| Target artifact | How this intel informs it |
|---|---|
| AI Playbook | Clarifies that HC-wide and PHAC-specific data-readiness gates are not interchangeable |
| Data Architecture Plan | Surfaces the explicit PHAC-depends-on-HC dependency as an architecture constraint, plus the currency gap in HC's own architecture maturity |
| ARB briefing | Gives reviewers the verbatim dependency statement and the vintage-gap caveat before any HC/PHAC data-governance comparison is presented |
| Platform roadmap | Flags that PHAC's AI-integration ambitions may be bottlenecked by HC's (possibly stale) internal-services maturity |
| Agent / voice KB | Gives a plain-language answer distinguishing "HC's data strategy" from "PHAC's data strategy" when asked |

## 9. Retrieval tags

- hc-data-strategy
- phac-data-strategy
- data-governance
- enterprise-architecture
- currency-gap
- interoperability
- ai-readiness
- chief-data-officer
- data-maturity

## 10. Graph extraction

### Concepts

- Health Canada Data Strategy
- PHAC Data Strategy
- enterprise data governance
- public-health-focused data architecture
- Chief Data Officer
- SAS Grid
- DG-Science forum
- Health Portfolio
- HC-DTB

### Claims

- HC's 2019 Data Strategy is enterprise-wide, spanning both of HC's core responsibilities.
- PHAC's 2025-28 Data Strategy is health-data/surveillance-specific, not enterprise-wide.
- The Public Health Agency of Canada's Data Strategy is explicitly stated (in HC's 2019 document) to be highly dependent on Health Canada's internal services for HR, IM, IT, and enterprise architecture.
- HC's 2019 and PHAC's 2025-28 strategies are six years apart in vintage, with no confirmed newer HC document closing that gap.
- SAS Grid is shared foundational infrastructure for both HC and PHAC.

### Decisions

- Confirm whether HC's 2019 data strategy/maturity posture has been formally updated.
- Determine whether the PHAC-depends-on-HC statement still holds given PHAC's newer strategy.
- Reconcile HC's 2019 maturity rating against PHAC's current AI ambitions.

### Risks

- Treating the 2019 HC strategy as current.
- Reversing or softening the dependency direction.
- Assuming an unconfirmed supersession of the 2019 dependency statement.
- Blending HC-wide and PHAC-specific claims.

### Relationships

```text
INTEL-006 RELATES_TO INTEL-002 ON HC-vs-PHAC data strategy distinction
PHAC Data Strategy DEPENDS_ON Health Canada internal services
Health Canada Data Strategy PRECEDES PHAC Data Strategy 2025-28 BY six years
SAS Grid SUPPORTS Health Canada data analytics
SAS Grid SUPPORTS PHAC data analytics
DG-Science forum CONNECTS Health Canada
DG-Science forum CONNECTS Public Health Agency of Canada
HC-DTB COLLABORATES_WITH PHAC ON public-health-focused data architecture
```

## 11. Open questions

- Does a newer (post-2019) HC Data Strategy edition exist outside what is publicly discoverable, given that HC's 2024-25 and 2025-26 Departmental Plans still reference "Health Canada's Data Strategy" by name without citing a newer document?
- Does the explicit 2019 statement that "PHAC's Data Strategy is highly dependent upon Health Canada's internal services" still hold given that PHAC's own 2025/26–2027/28 strategy is newer and separately calls for HC-DTB collaboration on a public-health-focused data architecture?
- Has HC's Chief Data Officer role (stated as forthcoming in 2019) been established, and if so, has HC's data maturity rating been reassessed since the 2019 Gartner assessment?
- Should AI-readiness gating (INTEL-002) apply HC-wide criteria, PHAC-specific criteria, or both, depending on which department's data asset is in scope?
