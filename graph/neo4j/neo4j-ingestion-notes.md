# Neo4j Ingestion Notes

## Recommended approach

Do not start with Neo4j as the system of record.

Start with Markdown/CSV/JSON files in GitHub, then later import the structured context into Neo4j.

## Why

GitHub gives:

- audit trail
- branches
- pull requests
- human review
- low setup friction

Neo4j later adds:

- source-to-claim traceability
- decision dependency mapping
- contradiction detection
- capability-to-platform relationships
- impact analysis
- "what should I build next?" reasoning

## First import candidates

1. Source register
2. Decision records
3. Context packs
4. Claims extracted from sources
5. Platform/capability relationships
