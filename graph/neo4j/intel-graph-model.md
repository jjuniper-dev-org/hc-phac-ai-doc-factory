# Intel Brief Graph Model

Neo4j is a derived relationship/query layer for intel briefs. Markdown remains the source of truth.

## Node labels

- IntelBrief
- Source
- Claim
- Concept
- Decision
- Risk
- Platform
- Capability
- Control
- Document

## Relationship types

- DERIVED_FROM
- SUPPORTS
- CONTRADICTS
- REFERENCES
- GOVERNS
- RUNS
- USES
- REQUIRES
- INFORMS
- IMPLIES_DECISION
- HAS_RISK
- HAS_CONCEPT

## Rule

Do not hand-author Neo4j as the primary record. Generate graph seeds from Markdown intel briefs.
