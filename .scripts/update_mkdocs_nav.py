#!/usr/bin/env python3
"""Update the navigation section in ``mkdocs.yml``.

The script mirrors the layout of the ``docs/`` directory so that every
Markdown file is reachable from the MkDocs navigation. It should be run
whenever pages are added, renamed or removed so the menu stays in sync.

"""

import argparse
from pathlib import Path
import yaml


def title_from_path(path: Path) -> str:
    """Return a human readable title for the nav entry."""
    return path.stem.replace("_", " ").title()


def build_nav(base: Path, current: Path | None = None) -> list:
    """Return a list suitable for the MkDocs ``nav`` config."""
    if current is None:
        current = base

    entries = []
    for item in sorted(current.iterdir()):
        if item.is_dir():
            sub_nav = build_nav(base, item)
            if sub_nav:
                entries.append({title_from_path(item): sub_nav})
        elif item.suffix.lower() == ".md":
            rel = item.relative_to(base)
            entries.append({title_from_path(item): str(rel.as_posix())})
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
