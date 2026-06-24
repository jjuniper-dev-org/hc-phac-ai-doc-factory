"""
Export Markdown intel brief graph extraction blocks to data/intel_graph_seed.csv.

This is a phase 1 stub. It creates the output file and can be expanded by the dev bot.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "intel_graph_seed.csv"

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("source_id,node_type,name,relationship,target\n", encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
