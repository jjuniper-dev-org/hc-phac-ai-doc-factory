"""
Validate intel brief structure for the HC/PHAC AI document factory.

This validator checks only mechanical structure. It does not judge whether
content is complete, approved, or authoritative.
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INTEL_DIR = ROOT / "context" / "04-intel-briefs"
MANIFEST_PATH = ROOT / "data" / "intel_manifest.csv"

REQUIRED_FRONTMATTER_FIELDS = [
    "id",
    "title",
    "doc_type",
    "status",
    "classification",
    "confidence",
    "source_controlled",
    "pipeline_use",
    "graph_enabled",
    "promoted_to_context_pack",
    "source_ids",
    "review_after",
    "tags",
]

REQUIRED_SECTIONS = [
    "Status",
    "Executive takeaway",
    "What is source-backed",
    "Working interpretation",
    "Decisions implied or needed",
    "Risks and caveats",
    "Use in document-production pipeline",
    "Graph extraction",
    "Open questions",
]

HARD_FAILURE_PREFIXES = (
    "missing file",
    "empty file",
    "missing frontmatter",
    "missing manifest row",
    "manifest path missing",
)


@dataclass
class Finding:
    path: str
    severity: str
    message: str


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def split_frontmatter(text: str) -> tuple[dict[str, str], str, bool]:
    """Return parsed frontmatter, body, and whether a frontmatter block exists."""
    if not text.startswith("---"):
        return {}, text, False

    lines = text.splitlines()
    if len(lines) < 3:
        return {}, text, False

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, text, False

    metadata: dict[str, str] = {}
    current_key: str | None = None
    for line in lines[1:end_index]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" in line and not line.startswith((" ", "\t", "-")):
            key, value = line.split(":", 1)
            current_key = key.strip()
            metadata[current_key] = value.strip()
        elif current_key and stripped.startswith("-"):
            existing = metadata.get(current_key, "")
            metadata[current_key] = f"{existing} {stripped}".strip()

    body = "\n".join(lines[end_index + 1 :])
    return metadata, body, True


def load_manifest() -> tuple[dict[str, dict[str, str]], list[Finding]]:
    findings: list[Finding] = []
    rows_by_path: dict[str, dict[str, str]] = {}

    if not MANIFEST_PATH.exists():
        findings.append(Finding(rel(MANIFEST_PATH), "ERROR", "missing file: manifest does not exist"))
        return rows_by_path, findings

    with MANIFEST_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required_columns = {"id", "path", "title", "status", "confidence", "graph_enabled", "pipeline_use"}
        fieldnames = set(reader.fieldnames or [])
        missing_columns = sorted(required_columns - fieldnames)
        if missing_columns:
            findings.append(
                Finding(rel(MANIFEST_PATH), "ERROR", f"missing manifest columns: {', '.join(missing_columns)}")
            )
        for row in reader:
            row_path = (row.get("path") or "").strip()
            if not row_path:
                findings.append(Finding(rel(MANIFEST_PATH), "ERROR", "manifest row has blank path"))
                continue
            rows_by_path[row_path] = row
            target = ROOT / row_path
            if not target.exists():
                findings.append(Finding(rel(MANIFEST_PATH), "ERROR", f"manifest path missing: {row_path}"))

    return rows_by_path, findings


def validate_brief(path: Path, manifest_rows: dict[str, dict[str, str]]) -> list[Finding]:
    findings: list[Finding] = []
    relative_path = rel(path)
    text = path.read_text(encoding="utf-8-sig")

    if not text.strip():
        return [Finding(relative_path, "ERROR", "empty file")]

    metadata, body, has_frontmatter = split_frontmatter(text)
    if not has_frontmatter:
        findings.append(Finding(relative_path, "ERROR", "missing frontmatter"))
    else:
        for field in REQUIRED_FRONTMATTER_FIELDS:
            if field not in metadata:
                findings.append(Finding(relative_path, "ERROR", f"missing frontmatter field: {field}"))
            elif metadata[field] == "" or metadata[field] == "[]":
                if field in {"source_ids", "tags"}:
                    findings.append(Finding(relative_path, "WARN", f"empty frontmatter field: {field}"))
                else:
                    findings.append(Finding(relative_path, "ERROR", f"empty frontmatter field: {field}"))

    for section in REQUIRED_SECTIONS:
        if section.lower() not in body.lower():
            findings.append(Finding(relative_path, "WARN", f"missing required section: {section}"))

    if "graph extraction" not in body.lower():
        findings.append(Finding(relative_path, "ERROR", "missing graph extraction section"))

    if relative_path not in manifest_rows:
        findings.append(Finding(relative_path, "ERROR", "missing manifest row"))
    else:
        row = manifest_rows[relative_path]
        metadata_id = metadata.get("id")
        manifest_id = (row.get("id") or "").strip()
        if metadata_id and manifest_id and metadata_id != manifest_id:
            findings.append(Finding(relative_path, "ERROR", f"id mismatch: frontmatter={metadata_id}, manifest={manifest_id}"))

        graph_enabled = (row.get("graph_enabled") or "").strip().lower()
        if graph_enabled == "true" and "graph extraction" not in body.lower():
            findings.append(Finding(relative_path, "ERROR", "manifest graph_enabled=true but graph extraction is missing"))

    return findings


def is_hard_failure(finding: Finding) -> bool:
    if finding.severity == "ERROR":
        return True
    return finding.message.startswith(HARD_FAILURE_PREFIXES)


def main() -> int:
    manifest_rows, findings = load_manifest()
    files = sorted(INTEL_DIR.glob("INTEL-*.md"))

    print(f"Intel brief validation")
    print(f"Root: {ROOT}")
    print(f"Found {len(files)} intel briefs")

    if not files:
        findings.append(Finding(rel(INTEL_DIR), "ERROR", "missing file: no INTEL-*.md files found"))

    for path in files:
        text_len = len(path.read_text(encoding="utf-8-sig"))
        print(f"- {rel(path)} ({text_len} chars)")
        findings.extend(validate_brief(path, manifest_rows))

    if findings:
        print("\nValidation findings:")
        for finding in findings:
            print(f"[{finding.severity}] {finding.path}: {finding.message}")
    else:
        print("\nNo validation findings.")

    hard_failures = [finding for finding in findings if is_hard_failure(finding)]
    if hard_failures:
        print(f"\nValidation failed: {len(hard_failures)} hard failure(s).")
        return 1

    print("\nValidation passed: no hard structural failures.")
    if findings:
        print("Warnings should be addressed before promotion to review-ready or accepted-context.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
