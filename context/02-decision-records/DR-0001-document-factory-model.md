# Decision Record 0001 — Working Document Factory Model

Date: 2026-06-22  
Status: Working decision  
Owner: James / Enterprise Architecture  

## Decision

Use GitHub as the working source-control and orchestration layer for AI-assisted document generation.

Use OneDrive for rendered draft exchange.

Use SACR as the repository of record for stable drafts and final approved documents.

## Rationale

Large AI-assisted documents require multiple iterations, review cycles, and bot-generated changes. GitHub provides branching, issues, pull requests, traceability, and structured bot collaboration.

SACR should remain the official repository of record, but should not be used as the messy early drafting workspace.

## Guardrails

- Do not commit Protected B or sensitive content unless explicitly approved.
- Bots must work through branches and pull requests.
- Humans approve merges.
- Stable drafts move to SACR.
- GitHub is not the final record repository.

## Implications

This allows autonomous drafting and review while preserving traceability and human control.
