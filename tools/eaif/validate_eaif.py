"""Mechanical validation for the EAIF evidence and requirements corpus.

This validator enforces traceability and status discipline. It does not decide
whether a policy interpretation or architecture position is substantively
correct; that remains a human review responsibility.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_PATH = ROOT / "data" / "eaif_evidence.csv"
REQUIREMENTS_PATH = ROOT / "data" / "eaif_requirements.csv"

EVIDENCE_COLUMNS = {
    "evidence_id",
    "evidence_type",
    "source_ref",
    "statement",
    "authority",
    "maturity",
    "eaif_domain",
    "stakeholder",
    "technology_context",
    "notes",
}

REQUIREMENT_COLUMNS = {
    "requirement_id",
    "requirement_statement",
    "authority",
    "normativity",
    "maturity",
    "source_evidence_ids",
    "accountable_role",
    "verification_evidence",
    "exception_path",
    "implementation_notes",
}

AUTHORITIES = {
    "GC/TBS",
    "HC/PHAC approved",
    "management direction",
    "EA working position",
    "proposed",
    "observed",
}

MATURITIES = {"confirmed", "strong signal", "emerging", "requires validation"}
NORMATIVITY = {"MUST", "SHOULD", "MAY", "informative"}
EVIDENCE_TYPES = {
    "source",
    "decision",
    "proposal",
    "observation",
    "demonstration",
    "issue",
    "metaphor",
    "intel",
    "repository-control",
}

FORMAL_MUST_AUTHORITIES = {"GC/TBS", "HC/PHAC approved", "management direction"}
REQUIREMENT_ID = re.compile(r"^EAIF-[A-Z]{3}-\d{3}$")
EVIDENCE_ID = re.compile(r"^EVID-\d{3}$")


@dataclass
class Finding:
    severity: str
    location: str
    message: str


def read_csv(path: Path, required_columns: set[str]) -> tuple[list[dict[str, str]], list[Finding]]:
    findings: list[Finding] = []
    if not path.exists():
        return [], [Finding("ERROR", str(path.relative_to(ROOT)), "missing file")]

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(required_columns - fieldnames)
        if missing:
            findings.append(
                Finding("ERROR", str(path.relative_to(ROOT)), f"missing columns: {', '.join(missing)}")
            )
        rows = [dict(row) for row in reader]
    return rows, findings


def split_refs(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def validate_evidence(rows: list[dict[str, str]]) -> tuple[dict[str, dict[str, str]], list[Finding]]:
    findings: list[Finding] = []
    by_id: dict[str, dict[str, str]] = {}

    for index, row in enumerate(rows, start=2):
        location = f"data/eaif_evidence.csv:{index}"
        evidence_id = (row.get("evidence_id") or "").strip()
        if not EVIDENCE_ID.match(evidence_id):
            findings.append(Finding("ERROR", location, f"invalid evidence_id: {evidence_id!r}"))
        if evidence_id in by_id:
            findings.append(Finding("ERROR", location, f"duplicate evidence_id: {evidence_id}"))
        elif evidence_id:
            by_id[evidence_id] = row

        authority = (row.get("authority") or "").strip()
        maturity = (row.get("maturity") or "").strip()
        evidence_type = (row.get("evidence_type") or "").strip()
        source_ref = (row.get("source_ref") or "").strip()
        statement = (row.get("statement") or "").strip()

        if authority not in AUTHORITIES:
            findings.append(Finding("ERROR", location, f"invalid authority: {authority!r}"))
        if maturity not in MATURITIES:
            findings.append(Finding("ERROR", location, f"invalid maturity: {maturity!r}"))
        if evidence_type not in EVIDENCE_TYPES:
            findings.append(Finding("ERROR", location, f"invalid evidence_type: {evidence_type!r}"))
        if not source_ref:
            findings.append(Finding("ERROR", location, "source_ref is required"))
        if not statement:
            findings.append(Finding("ERROR", location, "statement is required"))

    return by_id, findings


def validate_requirements(
    rows: list[dict[str, str]], evidence_by_id: dict[str, dict[str, str]]
) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[str] = set()

    for index, row in enumerate(rows, start=2):
        location = f"data/eaif_requirements.csv:{index}"
        req_id = (row.get("requirement_id") or "").strip()
        statement = (row.get("requirement_statement") or "").strip()
        authority = (row.get("authority") or "").strip()
        normativity = (row.get("normativity") or "").strip()
        maturity = (row.get("maturity") or "").strip()
        refs = split_refs(row.get("source_evidence_ids") or "")

        if not REQUIREMENT_ID.match(req_id):
            findings.append(Finding("ERROR", location, f"invalid requirement_id: {req_id!r}"))
        if req_id in seen:
            findings.append(Finding("ERROR", location, f"duplicate requirement_id: {req_id}"))
        seen.add(req_id)

        if not statement:
            findings.append(Finding("ERROR", location, "requirement_statement is required"))
        if authority not in AUTHORITIES:
            findings.append(Finding("ERROR", location, f"invalid authority: {authority!r}"))
        if maturity not in MATURITIES:
            findings.append(Finding("ERROR", location, f"invalid maturity: {maturity!r}"))
        if normativity not in NORMATIVITY:
            findings.append(Finding("ERROR", location, f"invalid normativity: {normativity!r}"))

        if normativity in {"MUST", "SHOULD"} and not refs:
            findings.append(Finding("ERROR", location, f"{normativity} requires source evidence"))

        unresolved = [ref for ref in refs if ref not in evidence_by_id]
        if unresolved:
            findings.append(
                Finding("ERROR", location, f"unresolved evidence reference(s): {', '.join(unresolved)}")
            )

        resolved = [evidence_by_id[ref] for ref in refs if ref in evidence_by_id]
        if normativity in {"MUST", "SHOULD"} and resolved:
            evidence_authorities = {(item.get("authority") or "").strip() for item in resolved}
            if evidence_authorities == {"observed"}:
                findings.append(
                    Finding("ERROR", location, "observed evidence alone cannot support MUST/SHOULD")
                )

        if normativity == "MUST":
            if authority not in FORMAL_MUST_AUTHORITIES:
                findings.append(
                    Finding(
                        "ERROR",
                        location,
                        "MUST requires GC/TBS, HC/PHAC approved, or management direction authority",
                    )
                )
            if maturity not in {"confirmed", "strong signal"}:
                findings.append(
                    Finding("ERROR", location, "MUST cannot use emerging/requires validation maturity")
                )

        if normativity == "SHOULD" and authority == "observed":
            findings.append(Finding("ERROR", location, "observed authority cannot directly issue SHOULD"))

    return findings


def main() -> int:
    evidence_rows, findings = read_csv(EVIDENCE_PATH, EVIDENCE_COLUMNS)
    requirement_rows, requirement_file_findings = read_csv(REQUIREMENTS_PATH, REQUIREMENT_COLUMNS)
    findings.extend(requirement_file_findings)

    evidence_by_id, evidence_findings = validate_evidence(evidence_rows)
    findings.extend(evidence_findings)
    findings.extend(validate_requirements(requirement_rows, evidence_by_id))

    print("EAIF validation")
    print(f"Evidence records: {len(evidence_rows)}")
    print(f"Requirements: {len(requirement_rows)}")

    if findings:
        print("\nFindings:")
        for finding in findings:
            print(f"[{finding.severity}] {finding.location}: {finding.message}")

    errors = [finding for finding in findings if finding.severity == "ERROR"]
    if errors:
        print(f"\nValidation failed: {len(errors)} error(s).")
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
