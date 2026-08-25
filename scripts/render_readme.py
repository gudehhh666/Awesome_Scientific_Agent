#!/usr/bin/env python3
"""Render README.md from the editorial template and catalog data."""

from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.catalog import CatalogError, load_catalog, render_readme


def expected_readme(root: Path) -> str:
    template = (root / "templates" / "README.md").read_text(encoding="utf-8")
    return render_readme(template, load_catalog(root))


def write_atomically(path: Path, content: str) -> None:
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=path.parent, delete=False
        ) as temporary_file:
            temporary_file.write(content)
            temporary_name = temporary_file.name
        os.replace(temporary_name, path)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="fail when README.md is not current"
    )
    arguments = parser.parse_args()

    try:
        expected = expected_readme(ROOT)
    except (CatalogError, OSError) as error:
        print(error, file=sys.stderr)
        return 1

    readme_path = ROOT / "README.md"
    if arguments.check:
        actual = readme_path.read_text(encoding="utf-8")
        if actual != expected:
            print(
                "README.md is stale; run python3 scripts/render_readme.py",
                file=sys.stderr,
            )
            return 1
        print("README.md is current")
        return 0

    write_atomically(readme_path, expected)
    print("Rendered README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
