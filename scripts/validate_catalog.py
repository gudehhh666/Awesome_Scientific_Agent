#!/usr/bin/env python3
"""Validate catalog data and local documentation links."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.catalog import CatalogError, find_missing_local_links, load_catalog


def markdown_files(root: Path) -> list[Path]:
    candidates = [root / "README.md", root / "CONTRIBUTING.md"]
    candidates.extend((root / "docs").glob("**/*.md"))
    candidates.extend((root / "methods").glob("**/*.md"))
    return sorted(path for path in candidates if path.exists())


def main() -> int:
    try:
        catalog = load_catalog(ROOT)
        missing = find_missing_local_links(ROOT, markdown_files(ROOT))
    except (CatalogError, OSError) as error:
        print(error, file=sys.stderr)
        return 1

    if missing:
        for item in missing:
            print(f"missing local target: {item}", file=sys.stderr)
        return 1

    agents = catalog["agents"]
    resources = catalog["resources"]
    benchmarks = catalog["benchmarks"]
    print(f"taxonomy={len(agents['taxonomy'])}")
    for level, records in agents["reading_lists"].items():
        print(f"reading_lists.{level}={len(records)}")
    for section in ("watchlist", "construction", "enhancement"):
        print(f"{section}={len(resources[section])}")
    print(f"benchmarks={len(benchmarks['items'])}")
    print("catalog and local links are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
