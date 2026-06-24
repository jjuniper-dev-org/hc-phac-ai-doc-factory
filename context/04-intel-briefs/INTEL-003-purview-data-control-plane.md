---
id: INTEL-003
title: "Purview Data Control Plane"
doc_type: intel_brief
status: draft
classification: unclassified
confidence: medium
source_controlled: true
pipeline_use: true
graph_enabled: true
promoted_to_context_pack: false
source_ids:
  - SRC-PURVIEW-CONTROL-PLANE
review_after: 2026-07-31
tags: [purview, data-governance, lineage, classification]
---

# INTEL-003 — Purview Data Control Plane

Stub to be expanded by the Librarian from Purview control-plane source material.

Must cover: Purview as enterprise data governance control plane, centralized/inherited controls, data lineage, data classification, auditability, and relationship to PATH, HAIL, Fabric, and Databricks.

## Working interpretation

Purview should be treated as the enterprise data governance control plane. PATH/HAIL should consume data governance controls rather than recreate them.

## Graph extraction

### Concepts

- Purview
- data control plane
- data classification
- lineage
- auditability
- Fabric
- Databricks
- PATH
- HAIL

### Relationships

```text
Purview GOVERNS data classification
Purview GOVERNS data lineage
PATH CONSUMES Purview controls
HAIL CONSUMES Purview controls
```
