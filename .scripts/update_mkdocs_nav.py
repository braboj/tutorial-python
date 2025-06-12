#!/usr/bin/env python3
"""Update the navigation section in mkdocs.yml automatically.

The script scans the docs directory for ``*.md`` files and rewrites the
``nav`` section of ``mkdocs.yml`` so each file appears in the menu. Run it
whenever pages are added, renamed or removed.
"""

import argparse
from pathlib import Path
import yaml


def title_from_path(path: Path) -> str:
    """Return a human readable title for the nav entry."""
    return path.stem.replace("_", " ").title()


def build_nav(docs_dir: Path) -> list:
    """Return a list suitable for the MkDocs ``nav`` config."""
    entries = []
    for md_file in sorted(docs_dir.rglob("*.md")):
        rel = md_file.relative_to(docs_dir)
        entries.append({title_from_path(rel): str(rel.as_posix())})
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description="Update mkdocs navigation")
    parser.add_argument("--docs-dir", default="docs", help="Directory with markdown files")
    parser.add_argument("--mkdocs-file", default="mkdocs.yml", help="Path to mkdocs.yml")
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir)
    mkdocs_file = Path(args.mkdocs_file)

    if not docs_dir.is_dir():
        raise SystemExit(f"Docs directory {docs_dir} not found")

    if not mkdocs_file.is_file():
        raise SystemExit(f"MkDocs configuration {mkdocs_file} not found")

    with mkdocs_file.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config["nav"] = build_nav(docs_dir)

    with mkdocs_file.open("w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False)


if __name__ == "__main__":
    main()
