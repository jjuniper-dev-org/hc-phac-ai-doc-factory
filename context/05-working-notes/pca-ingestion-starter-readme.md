# PCA Ingestion Starter Pack

This pack provides a controlled way to feed actionable context into an AI-assisted document factory while staying aligned with PCA principles.

## Core flow

1. Drop raw files into `ingest/inbox`.
2. Create or update a source card for each file.
3. Classify the material.
4. Extract actionable claims, decisions, concepts, and tasks.
5. Create context packs for bot use.
6. Create decision records when an architectural position or working decision emerges.
7. Use GitHub Issues to assign bot work.
8. Keep SACR as the final repository of record for stable approved documents.

## Golden rule

Do not give bots a random pile of files. Give them controlled context:

- source register
- context pack
- decision record
- task instruction
- acceptance criteria
