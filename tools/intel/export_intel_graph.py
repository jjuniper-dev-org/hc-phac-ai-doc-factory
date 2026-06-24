"""Export a derived graph seed CSV from Markdown intel briefs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INTEL_DIR = ROOT / "context" / "04-intel-briefs"
OUT = ROOT / "data" / "intel_graph_seed.csv"
FIELDS = ["source_id", "node_type", "name", "relationship", "target"]


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines()
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return {}, text

    data: dict[str, object] = {}
    current_key: str | None = None
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped:
            continue
        if ":" in line and not line.startswith((" ", "-")):
            key, value = line.split(":", 1)
            current_key = key.strip()
            value = value.strip().strip('"')
            if value.startswith("[") and value.endswith("]"):
                data[current_key] = [part.strip() for part in value[1:-1].split(",") if part.strip()]
            else:
                data[current_key] = value
        elif current_key and stripped.startswith("-"):
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(stripped[1:].strip())
    return data, "\n".join(lines[end + 1 :])


def metadata_list(data: dict[str, object], key: str) -> list[str]:
    value = data.get(key, [])
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def section_after_heading(text: str, heading: str, level: str = "##") -> str:
    marker = f"{level} {heading}".lower()
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        normalized = line.strip().lower()
        if normalized == marker or normalized.endswith(marker):
            start = index + 1
            break
    if start is None:
        return ""
    out: list[str] = []
    stop_prefix = level + " "
    for line in lines[start:]:
        if line.startswith(stop_prefix):
            break
        out.append(line)
    return "\n".join(out)


def bullets(text: str) -> list[str]:
    found: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            found.append(stripped[2:].strip())
    return found


def relationship_lines(text: str) -> list[str]:
    lines: list[str] = []
    in_block = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_block = not in_block
            continue
        if not line:
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        if in_block or " " in line:
            lines.append(line)
    return lines


def add_row(rows: list[dict[str, str]], source_id: str, node_type: str, name: str, relationship: str = "", target: str = "") -> None:
    if not name:
        return
    rows.append({
        "source_id": source_id,
        "node_type": node_type,
        "name": name,
        "relationship": relationship,
        "target": target,
    })


def rows_for_file(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    data, body = parse_frontmatter(text)
    source_id = str(data.get("id") or path.stem)
    title = str(data.get("title") or path.stem).strip('"')
    rows: list[dict[str, str]] = []

    add_row(rows, source_id, "IntelBrief", title)
    for source in metadata_list(data, "source_ids"):
        add_row(rows, source_id, "Source", source, "DERIVED_FROM", title)
    for tag in metadata_list(data, "tags"):
        add_row(rows, source_id, "Tag", tag, "TAGS", title)

    graph = section_after_heading(body, "10. Graph extraction") or section_after_heading(body, "Graph extraction")
    for heading, node_type in [("Concepts", "Concept"), ("Claims", "Claim"), ("Decisions", "Decision"), ("Risks", "Risk")]:
        for item in bullets(section_after_heading(graph, heading, "###")):
            add_row(rows, source_id, node_type, item, "MENTIONED_IN", title)

    for line in relationship_lines(section_after_heading(graph, "Relationships", "###")):
        parts = line.split()
        if len(parts) >= 3:
            add_row(rows, source_id, "Relationship", parts[0], parts[1], " ".join(parts[2:]))
    return rows


def dedupe(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str, str, str, str]] = set()
    out: list[dict[str, str]] = []
    for row in rows:
        key = tuple(row[field] for field in FIELDS)
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def main() -> int:
    rows: list[dict[str, str]] = []
    files = sorted(INTEL_DIR.glob("INTEL-*.md"))
    for path in files:
        rows.extend(rows_for_file(path))
    rows = dedupe(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Processed {len(files)} intel brief(s)")
    print(f"Wrote {len(rows)} graph seed row(s) to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
