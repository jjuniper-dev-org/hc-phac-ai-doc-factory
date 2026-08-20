# EAIF Context Pack

## Purpose

Provide the controlled drafting context for the Enterprise AI Integration Framework (EAIF).

## Working definition

EAIF is the mechanism that connects strategy, capabilities, governance, architecture, data, platforms, acquisition and operations into a repeatable path from AI demand to governed enterprise delivery.

## Operating spine

Demand → Classify → Inventory → Assess → Govern → Reuse Check → Route → Architect → Acquire/Build → Validate → Authorize → Operate → Evaluate → Evolve/Retire

## Required source discipline

Use `context/00-source-register/source-register.md` and the EAIF evidence register before making normative claims.

Distinguish:

- authoritative GC/TBS requirements
- HC/PHAC approved direction
- management direction
- EA working positions
- proposals
- observations / meeting intelligence
- external references

Do not silently convert meeting intelligence, demonstrations, metaphors or working interpretations into approved policy or architecture decisions.

## Core EAIF domains

1. Purpose, scope and authority
2. Principles
3. Capability and classification model
4. Demand, intake and AI inventory
5. Assessment, prioritization and reuse
6. Governance triage and accountability
7. Data readiness and data architecture
8. Platform architecture and workload routing
9. Pattern Zero and reference patterns
10. Acquisition, vendor and model assessment
11. Delivery and shared responsibility
12. Authorization and production promotion
13. AI-Ops / DataOps / FinOps / lifecycle
14. Evidence, metadata and auditability
15. Exceptions and architecture decisions
16. Measures, maturity and value realization
17. Implementation roadmap

## Standing design constraints

- Capability before product.
- Reuse before acquisition/build.
- Pattern Zero is treated as an enterprise control baseline; routing is a separate implementation decision.
- PATH/HAIL convergence remains subject to architecture validation and should not be presented as a settled physical deployment model unless approved evidence exists.
- Purview may be described as a data governance/control-plane capability only to the extent supported by evidence.
- DADM/AIA and other governance obligations are trigger-based and apply where their scope criteria are met.
- AI-enabled solutions require operational ownership, monitoring, evaluation and lifecycle/change management.
- Human accountability is not delegated to the platform.

## Primary machine-readable inputs

- `data/eaif_evidence.csv`
- `data/eaif_requirements.csv`

## Existing supporting context

- `context/04-intel-briefs/`
- `context/02-decision-records/`
- `data/intel_manifest.csv`
- `data/intel_graph_seed.csv`

## Drafting rule

Bots may draft, compare, summarize and propose. Humans approve changes to normative architecture positions and merges to main.
