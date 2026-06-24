"""
Validate intel brief structure.

Phase 1 validator:
- reports empty intel files
- reports missing frontmatter fence
- reports missing Graph extraction section
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
INTEL_DIR = ROOT / "context" / "04-intel-briefs"

def main() -> int:
    files = sorted(INTEL_DIR.glob("INTEL-*.md"))
    print(f"Found {len(files)} intel briefs")
    failures = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        print(f"- {path.relative_to(ROOT)} ({len(text)} chars)")
        if not text.strip():
            failures.append((path, "empty file"))
        if not text.startswith("---"):
            failures.append((path, "missing frontmatter"))
        if "## 10. Graph extraction" not in text and "## Graph extraction" not in text:
            failures.append((path, "missing graph extraction section"))
    if failures:
        print("
Validation failures:")
        for path, reason in failures:
            print(f"- {path.relative_to(ROOT)}: {reason}")
        return 1
    print("Validation passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
