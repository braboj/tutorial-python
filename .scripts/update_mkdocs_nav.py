#!/usr/bin/env python3
"""Generate the MkDocs navigation structure.

The script mirrors the layout of the ``docs/`` directory so that every
Markdown file is reachable from the MkDocs navigation. It can update a
``mkdocs.yml`` file directly or write the navigation to a separate YAML file
so that the configuration can be assembled without modifying the original file.

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
    parser.add_argument("--mkdocs-file", help="Path to mkdocs.yml to update")
    parser.add_argument(
        "--nav-file",
        default="nav.yml",
        help="Write navigation structure as YAML (default: nav.yml)",
    )
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir)

    if not docs_dir.is_dir():
        raise SystemExit(f"Docs directory {docs_dir} not found")

    nav = build_nav(docs_dir)

    if args.nav_file:
        nav_path = Path(args.nav_file)
        # ``mkdocs build -f nav.yml`` expects a mapping, so wrap the nav
        # list in a dictionary to avoid configuration errors.
        with nav_path.open("w", encoding="utf-8") as f:
            yaml.dump({"nav": nav}, f, sort_keys=False)

    if args.mkdocs_file:
        mkdocs_file = Path(args.mkdocs_file)
        if not mkdocs_file.is_file():
            raise SystemExit(f"MkDocs configuration {mkdocs_file} not found")

        with mkdocs_file.open("r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        config["nav"] = nav

        with mkdocs_file.open("w", encoding="utf-8") as f:
            yaml.dump(config, f, sort_keys=False)


if __name__ == "__main__":
    main()
