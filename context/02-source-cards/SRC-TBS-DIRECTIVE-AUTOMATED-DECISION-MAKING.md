---
id: SRC-TBS-DIRECTIVE-AUTOMATED-DECISION-MAKING
title: "Directive on Automated Decision-Making"
doc_type: source_card
status: draft
classification: unclassified_internal
source_file: "https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592&section=html"
source_owner: "Treasury Board of Canada Secretariat"
source_date: "2019-04-01 (original effective date); 2025-06-24 (page-stated last-modified date, carrying a compliance-timeline amendment per section 1.2.1)"
review_after: 2026-07-31
tags:
  - dadm
  - aia
  - automated-decision-making
  - administrative-decision
  - algorithmic-impact-assessment
  - tbs-directive
  - responsible-ai
  - governance
---

# SRC-TBS-DIRECTIVE-AUTOMATED-DECISION-MAKING — Directive on Automated Decision-Making

## Source identity

- Source: live, current (non-archived) HTML page at `https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592&section=html`, fetched directly (not via search/cache) by the orchestrator.
- The page's own metadata states `dateModified: "2025-06-24"`, confirming this is the current version rather than an archived/superseded one.
- The page carries a 2021 Crown-copyright/ISBN notice (© His Majesty the King in right of Canada, represented by the President of the Treasury Board, 2021, ISBN: 9780660389394) alongside the 2025-06-24 "Date modified" metadata. Both dates are preserved here rather than collapsed into one: the 2021 notice is the copyright/ISBN registration of the directive text; the 2025-06-24 date is the page's own "last modified" stamp, which corresponds to the amendment described in section 1.2.1 (compliance-timeline extension for pre-existing systems).
- Extracted as HTML-stripped, otherwise verbatim text. Saved locally at fetch time; not re-fetched or diffed against a prior version.
- Relevance to AI document factory: this is the primary authoritative instrument defining "automated decision system," "administrative decision," and "algorithmic impact assessment" (AIA) as terms, and the AIA's impact-level (I-IV) framework — the single most load-bearing governance source for any AI-and-administrative-decision question in this corpus.

## Source-backed facts

### Effective date and compliance timeline

- Section 1.1: the directive takes effect April 1, 2019, with compliance required no later than April 1, 2020.
- Section 1.2: the directive applies to all automated decision systems developed or procured after April 1, 2020.
- Section 1.2.1 (the 2025-06-24 amendment): "Existing automated decision systems developed or procured prior to June 24, 2025, will have until June 24, 2026 to comply with the new or updated requirements." This is a compliance-timeline extension for pre-existing systems, not a scope expansion or contraction.
- Section 1.2.2: agents of Parliament will have until June 24, 2026, to comply with the requirements.
- Section 1.3: the directive is reviewed every two years, and as determined by the Chief Information Officer of Canada.

### Scope (critical — narrow, not blanket)

- Section 5.1 (verbatim): "This directive applies to any automated decision system in production used to make an administrative decision or a related assessment about a client."
- Section 5.2 (verbatim): "This directive excludes automated decision systems used solely for research and experimentation purposes, and those operating in test environments."
- Appendix A defines "production": "An automated decision system is in production when it is in use and has impacts on real clients. This can include when it is in beta or user testing and producing outputs that impact clients."
- Appendix A defines "test environment": "An environment containing hardware, instrumentation, simulators, software tools, and other support elements needed to conduct a test. A system in a test environment may mimic a production environment but does not impact real clients. Test environments may include exploration zones and sandboxes."
- Appendix A defines "administrative decision" verbatim: "Any decision that is made by an authorized official of a department as identified in section 8 of this directive pursuant to powers conferred by an Act of Parliament or an order made pursuant to a prerogative of the Crown that affects legal rights, privileges or interests."
- Net effect: the directive is scoped to production systems that make or materially assist a specific class of decision (administrative decisions affecting legal rights, privileges, or interests, made by an authorized official under statutory/prerogative authority) about a client — not to AI generally, and not to R&D/test-environment use.

### Appendix A — "automated decision system" definition (verbatim)

"Any technology that either assists or replaces the judgment of human decision makers. These systems draw from fields like statistics, linguistics and computer science, and use techniques such as rules-based systems, regression, predictive analytics, machine learning, deep learning, and neural networks."

### Appendix B — Impact Assessment Levels (I-IV), summarized gradation

- **Level I**: context likely low risk (client identity factors, line of business, technology type); decision impact likely little-to-none, easily reversible, brief, on rights/equality-dignity-privacy-autonomy/health-wellbeing/economic interests/ecosystem sustainability; data risk likely low (e.g., non-personal/unclassified, structured data).
- **Level II**: context likely moderate risk; decision impact likely moderate, likely reversible, short-term, on the same impact categories; data risk likely moderate (personal/non-personal/unclassified/protected mix, structured or unstructured data).
- **Level III**: context likely high risk; decision impact likely high, difficult to reverse, potentially ongoing; data risk likely high (personal or protected information, unstructured data).
- **Level IV**: context likely very high risk; decision impact likely very high, irreversible, perpetual; data risk likely very high (personal, protected, or classified information; unstructured or incomplete data).
- All four levels assess the same three axes (risk context, decision impact, data risk) at increasing severity; the level drives which Appendix C requirements apply.

### Section 6 requirement categories

- **6.1 Algorithmic impact assessment**: complete, approve, and publish the final AIA results in an accessible format on the Open Government Portal prior to production (6.1.1); apply the Appendix C requirements the AIA determines apply (6.1.2); review/approve/update the published AIA on a scheduled basis, including on functionality/scope change (6.1.3).
- **6.2 Transparency**: notice before decisions — through all service channels in use, prominently, in plain language, per the Canada.ca Content Style Guide (6.2.1-6.2.2.1); explanation after decisions — a meaningful explanation of how/why the decision was made, as prescribed in Appendix C (6.2.3); access to components — appropriate licensing determination, retaining/safeguarding released software-component versions, and (for proprietary licences) retained rights to access/test/monitor/audit including by authorized external parties (6.2.4-6.2.6.2); documenting decisions per the Directive on Service and Digital, supporting testing/monitoring/data-governance/reporting requirements (6.2.7).
- **6.3 Quality assurance**: testing pre-production and monitoring in production for accuracy, unintended bias, and human-rights impacts, consistent with the Charter, Canadian Human Rights Act, and UNDRIP Act (6.3.1-6.3.4.1); data quality — validating training/input data relevance, accuracy, currency per the Policy on Service and Digital and Privacy Act (6.3.5); data governance — traceability, protection, lawful collection/use/retention/disclosure/disposal per Directive on Service and Digital, Directive on Privacy Practices, Directive on Security Management (6.3.6); peer review — consulting qualified experts and publishing the review or a plain-language summary prior to production, with the panel composition and count tiered by impact level per Appendix C (6.3.7); Gender-based Analysis Plus during development/modification, tiered by impact level per Appendix C (6.3.8); employee training for staff involved in development/use/management, tiered by impact level per Appendix C (6.3.9); security — risk assessments and IM/IT security protections per the Policy on Government Security and Policy on Service and Digital, plus data/model integrity measures against tampering (6.3.10-6.3.11); legal — consulting departmental legal services from the concept stage (6.3.12); ensuring human involvement, tiered by impact level per Appendix C (6.3.13); obtaining appropriate approval-to-operate prior to production, tiered by impact level per Appendix C (6.3.14).
- **6.4 Recourse**: informing clients of recourse options to challenge the administrative decision, ensured to be timely, effective, and easy to access (6.4.1-6.4.1.1).
- **6.5 Reporting**: publishing information on the Open Government Portal on the system's effectiveness/efficiency in meeting program objectives (6.5.1), and on fairness/transparency/non-violation of human rights and freedoms (6.5.2).

### Section 7 — TBS's own role

- Providing government-wide guidance on automated decision system use (7.1).
- Developing and maintaining the Algorithmic Impact Assessment tool and supporting documentation (7.2) — note: this is the tool/instrument itself, distinct from the directive text (see Evidence gaps).
- Communicating/engaging government-wide and with other jurisdictions/sectors on common strategies and approaches (7.3).
- Raising compliance issues with the relevant deputy head as appropriate (7.4).
- Supporting policy implementation with departments to ensure systems are fair, effective, and transparent (7.5).

### Section 8 — Application

- 8.1: applies to all institutions subject to the Policy on Service and Digital.
- 8.2: other departments/separate agencies not subject to that policy are encouraged to meet the directive's requirements as good practice (not mandatory for them).
- 8.3 Agents of Parliament: named organizations are Office of the Auditor General of Canada; Office of the Chief Electoral Officer; Office of the Commissioner of Lobbying of Canada; Office of the Commissioner of Official Languages; Office of the Information Commissioner of Canada; Office of the Privacy Commissioner of Canada; Office of the Public Sector Integrity Commissioner of Canada (8.3.1).
- Agents of Parliament: their own heads are solely responsible for monitoring/ensuring compliance and responding to non-compliance (8.3.2).
- Carve-outs for agents of Parliament: sections 6.2.2.1 (Canada.ca Content Style Guide notice formatting) and 7.4 (TBS raising compliance issues with deputy heads) do not apply to them (8.3.3); they are not required to publish the AIA (6.1.1) or reporting information (6.5.1, 6.5.2) on the Open Government Portal (8.3.4); their own heads approve Level 4 systems to operate, per 6.3.14/Appendix C, instead of Treasury Board (8.3.5).

### Appendix C — tiered approval-to-operate (section 6.3.14)

- Level I and Level II: assistant deputy minister responsible for the program.
- Level III: deputy head.
- Level IV: Treasury Board — except for agents of Parliament, where the head of the agent of Parliament approves Level 4 systems per section 8.3.5.

(Appendix C also tiers notice, explanation, peer review, Gender-based Analysis Plus, and training requirements by impact level; see section 6 summary above for what each category covers substantively.)

## Working interpretation

This directive is the controlling authority for when "DADM applies" and what "AIA" means as a term — both load-bearing for INTEL-011. Its scope is deliberately narrow: production systems making or materially assisting administrative decisions (as statutorily/prerogative-defined) about a client, excluding R&D and test environments. This directly supports, and should be cited for, the distinction between DADM-triggering AI use and general-purpose/non-administrative-decision AI use already gestured at in INTEL-011's working interpretation — that distinction is not a hedge, it is what the directive's own text says.

## Evidence gaps

- The Algorithmic Impact Assessment *tool itself* — the actual online questionnaire instrument referenced in sections 6.1.1 and 7.2 — is a separate artifact from this directive text and was not independently fetched or reviewed. This card covers the directive's AIA *framework* (definitions, impact levels, requirement categories) but not the live tool's current question set, scoring logic, or UI.
- This card is built from a single live fetch of the **English HTML** version of the directive. The French version, any superseded/archived prior versions, and any TBS guidance/FAQ documents (e.g., AIA tool user guides) were not reviewed.
- The directive references several related instruments by name (Directive on Service and Digital, Directive on Privacy Practices, Directive on Security Management, Policy on Government Security, Policy on Service and Digital) that were not independently fetched or source-carded; their content is taken on the directive's own characterization only.
- No independent confirmation was sought on whether any HC/PHAC automated decision system currently meets the section 5.1 production/administrative-decision threshold — that determination is out of scope for this source card and belongs to INTEL-011's working interpretation and open questions.

## Use in intel briefs

- `INTEL-011 — DADM / AIA Governance` (primary)

## Graph extraction

### Concepts

- Directive on Automated Decision-Making
- automated decision system
- administrative decision
- algorithmic impact assessment
- impact assessment level
- production
- test environment
- approval to operate
- peer review
- Gender-based Analysis Plus
- recourse
- Open Government Portal
- agents of Parliament

### Claims

- The directive applies only to automated decision systems in production used to make an administrative decision or related assessment about a client.
- The directive excludes systems used solely for research/experimentation and those in test environments.
- "Administrative decision" is a defined term requiring an authorized official acting under statutory or prerogative authority, affecting legal rights, privileges, or interests.
- Approval-to-operate authority scales with impact level: ADM (I/II), deputy head (III), Treasury Board (IV), with agents-of-Parliament heads approving their own Level IV systems.
- Existing systems developed/procured before June 24, 2025 have until June 24, 2026 to comply with new/updated requirements introduced by the amendment reflected in the page's 2025-06-24 dateModified metadata.

### Relationships

```text
Directive on Automated Decision-Making DEFINES automated decision system
Directive on Automated Decision-Making DEFINES administrative decision
Directive on Automated Decision-Making DEFINES algorithmic impact assessment
Directive on Automated Decision-Making APPLIES_TO production systems making administrative decisions
Directive on Automated Decision-Making EXCLUDES research/experimentation systems
Directive on Automated Decision-Making EXCLUDES test environments
algorithmic impact assessment DETERMINES impact assessment level
impact assessment level DETERMINES Appendix C requirements
Appendix C REQUIRES tiered approval to operate
Treasury Board of Canada Secretariat MAINTAINS Algorithmic Impact Assessment tool
```
