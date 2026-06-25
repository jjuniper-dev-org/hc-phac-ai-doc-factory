---
id: SRC-HC-DATA-STRATEGY-2019
title: "Health Canada Data Strategy (2019)"
doc_type: source_card
status: draft
classification: unclassified_internal
source_file: "hc-data-strategy-2019.txt (pdftotext extraction of official HC publication)"
source_owner: "Health Canada"
source_date: 2019-10
review_after: 2026-07-31
tags:
  - hc-data-strategy
  - data-governance
  - enterprise-architecture
  - data-maturity
  - chief-data-officer
  - ai-readiness
  - currency-gap
---

# SRC-HC-DATA-STRATEGY-2019 — Health Canada Data Strategy (2019)

## Source identity

- Source: "Health Canada Data Strategy," October 2019. Official Health Canada departmental publication.
- Catalogue: Cat.: H14-336/2019E-PDF, ISBN: 978-0-660-32513-2, Pub.: 190327.
- Crown copyright: "Her Majesty the Queen in Right of Canada, as represented by the Minister of Health, 2019."
- Signed by Deputy Minister Stephen Lucas, Ph.D., in the Message from the Deputy Minister.
- Hosted copy retrieved as a PDF mirror on a GC collaboration wiki (gccollab.ca); the document itself carries the catalogue number, ISBN, and ministerial message expected of a genuine official HC publication.
- Extraction method: verbatim `pdftotext` extraction, otherwise unedited, read in full (1275 lines).
- Relevance to AI document factory: primary candidate HC-specific (department-wide) counterpart to the PHAC Data Strategy 2025/26–2027/28; needed to distinguish HC-wide claims from PHAC-specific claims in AI-readiness intel.

## Source-backed facts

- Vision: "Effectively use data as an asset to provide credible information, reliable advice and quality services."
- Five guiding principles: Everyone is Responsible (everyone responsible for data quality and accessibility); Sharing and Reuse (data collected once, designed/managed for reuse); Maximize Value (maximize usage/value while incorporating privacy, security, confidentiality, ethics); Enterprise Tools and Training (appropriate tools/training, leveraging enterprise tools); Leverage Governance and Stewardship (data architected and managed at the enterprise level through governance and stewardship).
- Three foundation pillars: People and Culture; Governance; Environment and Digital Infrastructure (per Table 1, "Health Canada's Data Strategy Framework").
- HC's programs fall under two core responsibilities: Health Care Systems, and Health Protection and Promotion.
- The strategy was produced in response to the November 2018 Clerk of the Privy Council "Data Strategy Roadmap for the Federal Public Service," which asked all departments to establish a departmental data strategy by September 2019; this is described as "the first of its kind" for Health Canada.
- 2019 Gartner-facilitated data maturity assessment: Health Canada rated as approaching Level 2 "Developing" on a scale of 0 "Nascent" to 5 "Optimizing" (Figure 2).
- The maturity assessment found data literacy/maturity increasing "within pockets of the organization" but not at the departmental ("enterprise") level, with the current lack of enterprise-level data governance cited as a hindrance to taking stock of data assets and identifying common digital infrastructure opportunities.
- Explicit HC–PHAC relationship statement (Message from the Deputy Minister / "Why Health Canada Needs a Data Strategy" section): "The Public Health Agency of Canada's Data Strategy is also highly dependant upon Health Canada's internal services for human resources, information management, information technology, and enterprise architecture."
- Shared infrastructure fact: recent investments upgrading SAS Grid software are described as "a key foundational data infrastructure for both Health Canada and the Public Health Agency of Canada (PHAC) to perform statistical analysis and advanced analytics," used by "520 epidemiologists, statisticians and data scientists, across ten Health Canada / PHAC branches."
- DG-Science forum: described as bringing together "the Health Portfolio partners (i.e. Health Canada, Public Health Agency of Canada, Canadian Institutes of Health Research and Canadian Food Inspection Agency)" for horizontal science and risk-based issues.
- "Delivering on our Data Priorities" section states that internal service providers "will need to understand the needs of branches and PHAC, working together collaboratively to create an enterprise environment and digital infrastructure."
- Concrete examples cited as Health Canada data-in-action:
  - Project Cyclops: a DM Solutions Fund initiative developing an app allowing inspectors to use a smartphone/wearable camera to scan product labels, verify label information, and flag non-compliance.
  - Cannabis Tracking and Licensing System (CTLS): federal licence holders and provincially authorized distributors/retailers submit monthly reports; the Cannabis program's Business Intelligence Unit uses visualizations of this data for regulatory oversight, policymaking, and public trend reporting.
  - Solutions Fund AI/ML pilots: the Healthy Environments and Consumer Safety Branch conducting a proof of concept testing a systematic-review approach for human health risk assessments using AI; the Regulatory Operations and Enforcement Branch leveraging AI/ML on data mined from regulatory inspection reports and databases to inform risk-based decision-making.
- A new Chief Data Officer role for Health Canada is stated as being created "in the coming months" (as of October 2019), to work in partnership with the CIO.
- The strategy explicitly self-describes as "evergreen," intended to "evolve over time" rather than function as a fixed one-time document.

## Working interpretation

This is a department-wide (enterprise) HC data strategy, broader in scope than PHAC's 2025/26–2027/28 strategy: it spans both of HC's core responsibilities (health care systems, and health protection/promotion regulatory work), not just health-surveillance data. It establishes HC as the internal-services dependency for PHAC (HR, IM, IT, enterprise architecture) — a structural relationship, not merely a collaborative one. Detailed comparison with PHAC's newer strategy is maintained in INTEL-006, not duplicated here.

## Evidence gaps

- **Currency caveat (flag prominently):** this document is dated October 2019 — six-plus years old at time of this card's drafting (2026-06-25). No newer standalone HC Data Strategy publication was found by the orchestrator via web search. However, Health Canada's 2024-25 and 2025-26 Departmental Plans (public canada.ca pages) both still reference "Health Canada's Data Strategy" by name, in the present tense, as an active strategic reference. The strategy text itself self-describes as "evergreen" — intended to evolve rather than be replaced by a new fixed document — so the named strategy may have evolved in practice without a new public document to point to. Do not treat this card as evidence that the 2019 framework, goals, or maturity rating are still current as written; do not treat the absence of a newer document as evidence the strategy lapsed.
- This card is built entirely from web-extracted PDF text (`pdftotext` output), not independently re-verified against the original PDF's visual layout or figures. Figures 1–6 (visual framework diagrams, e.g. "Health Canada Data Strategy Foundation, Pillars, and Outcome" and the maturity-assessment radar/bar chart in Figure 2) were not visually reviewed — only the surrounding/captioned text was read. Table 2 ("Data Strategy Framework Actions") was read but its action items were not independently cross-checked for completeness against the source PDF's table formatting.
- The 2019 Chief Data Officer role creation is stated as forthcoming ("in the coming months") as of the document's publication; whether/when this role was actually created and who has held it since 2019 is not addressed in this source and is unverified here.
- No information in this source post-dates 2019; any HC organizational changes, machine-learning/AI program developments, or governance restructuring since 2019 are out of scope for this card.

## Use in intel briefs

- `INTEL-002 — AI Readiness / Data Foundation` (minimal HC-specific additions only; see INTEL-006 for full comparison)
- `INTEL-006 — HC/PHAC Data Strategy Alignment` (primary home for HC-vs-PHAC comparison)

## Graph extraction

### Concepts

- Health Canada Data Strategy
- data as an asset
- People and Culture (pillar)
- Governance (pillar)
- Environment and Digital Infrastructure (pillar)
- Health Care Systems (core responsibility)
- Health Protection and Promotion (core responsibility)
- Chief Data Officer
- Gartner data maturity model
- SAS Grid
- DG-Science forum
- Health Portfolio
- Solutions Fund
- Project Cyclops
- Cannabis Tracking and Licensing System (CTLS)

### Claims

- Health Canada's 2019 Data Strategy is HC's first department-wide data strategy.
- Health Canada's 2019 Gartner-facilitated maturity assessment rated HC as approaching Level 2 "Developing" (scale 0–5).
- The Public Health Agency of Canada's Data Strategy is explicitly stated to be highly dependent on Health Canada's internal services for HR, IM, IT, and enterprise architecture.
- SAS Grid is explicitly described as shared foundational data infrastructure for both Health Canada and PHAC.
- The DG-Science forum brings together Health Canada, PHAC, CIHR, and CFIA as Health Portfolio partners.
- The Health Canada Data Strategy self-describes as evergreen, intended to evolve rather than remain fixed.

### Relationships

```text
Health Canada Data Strategy INFORMS AI readiness
Health Canada Data Strategy REQUIRES enterprise data governance
Health Canada Data Strategy ESTABLISHES Chief Data Officer role
PHAC Data Strategy DEPENDS_ON Health Canada internal services
SAS Grid SUPPORTS Health Canada data analytics
SAS Grid SUPPORTS PHAC data analytics
DG-Science forum CONNECTS Health Canada
DG-Science forum CONNECTS Public Health Agency of Canada
```

## Open questions

- Does a newer (post-2019) HC Data Strategy edition exist that is not publicly discoverable, or has the strategy evolved informally ("evergreen") without a new published document?
- Was the Chief Data Officer role for Health Canada created as planned, and how has it evolved since 2019?
- How, if at all, has the explicit "PHAC depends on HC internal services" relationship changed given PHAC's own newer (2025/26–2027/28) data strategy?
