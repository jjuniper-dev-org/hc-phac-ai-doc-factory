// Example Neo4j import pattern for PCA Document Factory

MERGE (s:Source {source_id: "SRC-001"})
SET s.title = "Placeholder Source",
    s.source_type = "Candidate",
    s.classification = "Unclassified",
    s.status = "Candidate";

MERGE (c:Concept {name: "Document Factory"})
SET c.description = "A controlled GitHub-based workflow for AI-assisted document generation.";

MERGE (d:Decision {decision_id: "DR-0001"})
SET d.title = "Working Document Factory Model",
    d.status = "Working";

MERGE (s)-[:SUPPORTS]->(c);
MERGE (c)-[:SUPPORTS]->(d);
