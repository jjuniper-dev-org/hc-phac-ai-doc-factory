/*
Intel brief graph import notes.

Markdown is canonical. The CSV produced by tools/intel/export_intel_graph.py is a derived graph seed for later graph loading and architecture querying.

Expected CSV path:
  data/intel_graph_seed.csv

Expected columns:
  source_id,node_type,name,relationship,target

Rules:
- Use the Markdown intel briefs as the source of truth.
- Regenerate the CSV from Markdown before loading graph data.
- Do not infer relationships that are not represented in the Markdown.
- Treat this file as a placeholder until a graph environment is defined.
*/

MERGE (:Concept {name: "PATH"});
MERGE (:Concept {name: "HAIL"});
MERGE (:Concept {name: "Pattern Zero"});
MERGE (:Concept {name: "DADM"});
MERGE (:Concept {name: "AIA"});
