# Decision Record 0002 — EAIF Evidence-to-Draft Pipeline

Date: 2026-08-20  
Status: Working decision  
Owner: Enterprise Architecture  
Related Jira: EAID-21  
Related GitHub issue: #22

## Decision

Extend the existing HC/PHAC AI Document Factory conventions to support the Enterprise AI Integration Framework (EAIF).

Use the following pipeline:

`evidence → normalized requirements → EAIF source → validators → generated working draft → pull-request review`

Do not create a separate EAIF-specific orchestration model when existing source-register, context-pack, decision-record, intel, document-package and pull-request conventions can be reused.

## Source-of-truth boundaries

- Jira tracks work, backlog, ownership, dependencies and decisions requiring action.
- GitHub stores working document sources, normalized evidence/requirements and review history.
- Machine-readable EAIF evidence and requirements are the drafting inputs.
- Generated documents are derivative outputs and are not the authoritative requirement store.
- SACR remains the repository of record for stable drafts and approved documents.

## Validation policy

The pipeline must mechanically enforce at least the following:

- Every normative requirement has an authority classification and maturity status.
- Every MUST or SHOULD has explicit evidence references.
- An observed meeting statement cannot by itself support a normative MUST or SHOULD.
- A MUST cannot be based on proposed/observed authority or on `requires validation` maturity.
- Evidence references must resolve to registered evidence records.
- Duplicate evidence and requirement identifiers fail validation.

Mechanical validation does not determine whether a policy interpretation or architecture position is substantively correct. Human review remains required.

## CI model

GitHub Actions runs structural validation and deterministic generation on relevant pull requests.

The generated EAIF working draft is uploaded as a workflow artifact for review rather than committed as an authoritative source file.

## Guardrails

- Do not commit Protected B, sensitive security details, credentials, Cabinet confidence or controlled records unless the repository/workflow is formally approved for that classification.
- Bots do not merge to main.
- Product-specific implementations are not promoted to universal EAIF requirements without supporting approved evidence.
- Existing document-factory controls in `AGENTS.md` and DR-0001 remain in force.

## Consequences

This creates an auditable path from evidence to requirements to reviewable draft output while preserving human authority and allowing the framework to be regenerated as evidence and architecture decisions evolve.
