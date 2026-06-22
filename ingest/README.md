# Ingestion Inbox

Use this folder for files before they are processed.

## Recommended file handling

- `inbox/` = raw material waiting for review
- `processed/` = material registered and extracted
- `rejected/` = material excluded from bot use

## File naming convention

Use:

`YYYY-MM-DD__source-name__short-topic__classification.ext`

Example:

`2026-06-22__hc-ai-strategy__policy-context__unclassified.pdf`

## Classification note

Do not place Protected B or sensitive material here unless the repository and workflow are formally approved for that classification.
