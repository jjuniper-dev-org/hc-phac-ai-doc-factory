# Intel Briefs — Document Production Context Layer

This folder contains source-controlled intelligence briefs for the HC/PHAC AI document-production pipeline.

Intel briefs sit between raw sources/source cards and generated document drafts.

```text
raw sources
→ source cards
→ intel briefs
→ context packs
→ document-production briefs
→ working drafts
→ reviewed PRs
→ official records later
```

## Operating model

```text
Markdown = canonical working memory
Neo4j = derived relationship/query layer
Qdrant = semantic retrieval layer
GitHub = audit trail / review mechanism
```

## Purpose

Intel briefs provide stable, reviewable working context for AI Playbook drafting, Data Architecture Plan drafting, ARB/TPO/DTB briefings, AI governance analysis, PATH/HAIL/Purview platform reasoning, agent and voice-assistant retrieval, and future graph extraction.

## Ownership split

| Work | Owner |
|---|---|
| Scaffold, validation, export scripts | Dev bot |
| Populate and maintain brief content | Librarian |
| Promote accepted context | Human reviewer |

## Validation

Run the structural validator from the repository root:

```bash
python tools/intel/validate_intel_docs.py
```

The validator checks that intel briefs are non-empty, have required frontmatter, include expected sections, appear in `data/intel_manifest.csv`, and include graph extraction when marked as graph-enabled.

Validation is mechanical only. It does not confirm that content is approved, complete, authoritative, or ready for promotion.

Hard structural failures return a non-zero exit code. Warnings should be resolved before moving a brief from `draft` to `review-ready`.

## Guardrails

- Do not add sensitive or controlled operational information unless the target runtime is approved.
- Do not invent ARB, TPO, OCDO, ADM, or DM approvals.
- Separate source-backed facts from working interpretation, recommendations, assumptions, open decisions, and evidence gaps.
- Mark meeting-derived content clearly.
- Treat Markdown as the source of truth.
- Treat graph and semantic retrieval layers as derived.
