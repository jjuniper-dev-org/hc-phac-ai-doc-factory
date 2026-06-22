# Context Pack — Data Architecture Plan

## Purpose

This context pack provides controlled context for agents drafting or reviewing the HC/PHAC Data Architecture Plan.

## Mission context

HC/PHAC requires a stronger enterprise data foundation to support AI, analytics, surveillance, regulatory intelligence, reporting, and evidence-based decision-making.

The Data Architecture Plan should define the target data architecture needed for AI-ready, governed, findable, accessible, interoperable, and reusable data.

## Core architecture position

Data governance should be centralized and inherited where possible, not recreated project by project.

Working EA framing:

> Purview is the enterprise data governance control plane. Fabric, Databricks, HAIL, PATH, Power Platform, and business applications should consume or align to enterprise data governance controls rather than independently defining them.

## Core problems to address

- Fragmented data architecture
- Inconsistent governance
- Weak metadata and catalogue maturity
- Limited lineage
- Uneven stewardship
- Project-by-project data design
- Limited AI-ready data foundations
- Lack of consistent data quality and standards
- Unclear platform alignment across Fabric, Databricks, PATH, HAIL, Purview, and SACR

## Core topics

The Data Architecture Plan should cover:

- Current-state data fragmentation
- Target-state enterprise data architecture
- Data governance operating model
- Metadata and catalogue
- Lineage and traceability
- Data quality
- FAIR principles
- Data stewardship
- SACR and repository-of-record alignment
- Purview control plane
- Fabric / Databricks alignment
- HAIL / PATH alignment
- Roadmap and sequencing

## Required distinctions

Agents must distinguish between:

1. Enterprise data governance
2. Platform-level data controls
3. Application-specific data management
4. Official repository of record
5. Working analytical environments
6. AI runtime environments

## Do not do

Agents must not:

- treat OneDrive as the repository of record
- treat GitHub as approved storage for controlled records
- treat Purview as a full data architecture by itself
- collapse Fabric, Databricks, HAIL, PATH, and SACR into one platform
- include Protected B or sensitive content
