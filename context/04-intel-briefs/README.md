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

## Guardrails

- Do not add sensitive or controlled operational information unless the target runtime is approved.
- Do not invent ARB, TPO, OCDO, ADM, or DM approvals.
- Separate source-backed facts from working interpretation, recommendations, assumptions, open decisions, and evidence gaps.
- Mark meeting-derived content clearly.
- Treat Markdown as the source of truth.
- Treat graph and semantic retrieval layers as derived.
