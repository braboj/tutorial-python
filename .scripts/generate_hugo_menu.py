#!/usr/bin/env python3
"""Generate a Hugo menu from the docs directory structure.

This script walks through the ``docs`` folder and produces a YAML file
with a ``menu.main`` configuration that mirrors the layout of the
Markdown files. Each entry includes an ``identifier``, ``name``, ``url`` and
``weight``. Subdirectories are handled automatically via the ``parent``
field so that the hierarchy is preserved.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import yaml


def dump_yaml(data: dict, file: Path) -> None:
    """Write *data* to *file* as YAML."""
    yaml.dump(data, file, sort_keys=False)


def title_from_path(path: Path) -> str:
    """Return a human readable title for the menu entry."""
    return path.stem.replace("_", " ").title()


def build_menu(
    base: Path,
    current: Path | None = None,
    parent: str | None = None,
    weight_counter: list[int] | None = None,
) -> list[dict]:
    """Return a list of menu entries for Hugo."""
    if current is None:
        current = base
    if weight_counter is None:
        weight_counter = [0]

    entries: list[dict] = []
    for item in sorted(current.iterdir()):
        if item.is_dir():
            entries.extend(
                build_menu(
                    base,
                    item,
                    parent=item.relative_to(base).as_posix(),
                    weight_counter=weight_counter,
                )
            )
        elif item.suffix.lower() == ".md":
            weight_counter[0] += 1
            rel = item.relative_to(base).with_suffix("")
            entry: dict[str, object] = {
                "identifier": rel.as_posix(),
                "name": title_from_path(item),
                "url": f"/{rel.as_posix()}/",
                "weight": weight_counter[0],
            }
            if parent:
                entry["parent"] = parent
            entries.append(entry)
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Hugo menu from docs directory"
    )
    parser.add_argument(
        "--docs-dir", default="docs", help="Directory containing Markdown files"
    )
    parser.add_argument(
        "--output", default="hugo_menu.yml", help="Output YAML file"
    )
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir)
    if not docs_dir.is_dir():
        raise SystemExit(f"Docs directory {docs_dir} not found")

    menu = build_menu(docs_dir)
    with Path(args.output).open("w", encoding="utf-8") as f:
        dump_yaml({"menu": {"main": menu}}, f)


if __name__ == "__main__":
    main()
