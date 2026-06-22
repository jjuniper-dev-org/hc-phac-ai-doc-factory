# Neo4j Graph Model — PCA Document Factory

This model supports later graph ingestion of sources, claims, concepts, decisions, tasks, documents, and agents.

## Node labels

| Label | Purpose |
|---|---|
| Source | A file, strategy, briefing, deck, note, or external reference |
| Claim | A factual or interpretive statement extracted from a source |
| Concept | A reusable architecture, governance, or platform concept |
| Decision | A formal, working, or proposed decision |
| Document | A generated or maintained document |
| Section | A section within a document |
| Agent | A drafting or review agent |
| Task | An assigned unit of work |
| Platform | A system/platform such as PATH, HAIL, Purview, Fabric, Databricks |
| Capability | A business, data, application, or AI capability |
| Risk | A risk, issue, or concern |
| Control | A guardrail, review gate, policy, or enforcement mechanism |

## Relationship types

| Relationship | Meaning |
|---|---|
| SUPPORTS | Source/claim supports a decision, concept, or section |
| CONTRADICTS | Source/claim conflicts with another claim or decision |
| DERIVED_FROM | Claim, context pack, or section is derived from a source |
| REFERENCES | Document or section references a source |
| REQUIRES | Task or decision requires a control, source, or review |
| ASSIGNED_TO | Task assigned to agent or human |
| REVIEWS | Agent reviews section/document |
| IMPLEMENTS | Platform implements capability or control |
| GOVERNS | Control or platform governs data, AI execution, or access |
| DEPENDS_ON | Decision, platform, or section depends on another entity |
| ROUTES_TO | Intake outcome routes to a platform, review, or control |

## Example pattern

Source -> DERIVED_FROM -> Claim -> SUPPORTS -> Decision -> IMPACTS -> Document Section
