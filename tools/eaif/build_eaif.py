"""Build a deterministic EAIF working draft from version-controlled inputs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTROL = ROOT / "docs" / "eaif" / "00-control" / "document-control.md"
OUTLINE = ROOT / "docs" / "eaif" / "01-outline" / "outline.md"
SOURCE = ROOT / "docs" / "eaif" / "02-source" / "EAIF-source.md"
REQUIREMENTS = ROOT / "data" / "eaif_requirements.csv"
OUTPUT = ROOT / "build" / "eaif" / "EAIF-working-draft.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").strip()


def read_requirements() -> list[dict[str, str]]:
    with REQUIREMENTS.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def cell(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ").strip()


def requirements_table(rows: list[dict[str, str]]) -> str:
    lines = [
        "| ID | Requirement | Authority | Normativity | Maturity | Evidence |",
        "|---|---|---|---|---|---|",
    ]
    for row in sorted(rows, key=lambda item: item.get("requirement_id", "")):
        lines.append(
            "| {id} | {statement} | {authority} | {normativity} | {maturity} | {evidence} |".format(
                id=cell(row.get("requirement_id", "")),
                statement=cell(row.get("requirement_statement", "")),
                authority=cell(row.get("authority", "")),
                normativity=cell(row.get("normativity", "")),
                maturity=cell(row.get("maturity", "")),
                evidence=cell(row.get("source_evidence_ids", "")),
            )
        )
    return "\n".join(lines)


def main() -> int:
    requirements = read_requirements()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    document = "\n\n".join(
        [
            "# EAIF Working Draft — Generated Artifact",
            "> Generated deterministically by `tools/eaif/build_eaif.py`. Do not treat this artifact as the authoritative requirements store. Human review and approval remain required.",
            "## Document Control",
            read_text(CONTROL),
            "## Controlled Outline",
            read_text(OUTLINE),
            "## Working Source",
            read_text(SOURCE),
            "## Appendix A — Normalized Requirements",
            requirements_table(requirements),
        ]
    )

    OUTPUT.write_text(document + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    print(f"Included {len(requirements)} normalized requirement(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
