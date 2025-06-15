#!/usr/bin/env python3
"""Generate aggregated Markdown files for each examples subfolder.

Usage:
    python .scripts/examples_to_markdown_files.py \
        --examples-dir examples \
        --output-dir docs

For every immediate subfolder in ``examples`` a single ``.md`` file is created
in the output directory. The file name matches the subfolder name and contains
all example files from that folder.
"""

import argparse
import re
from pathlib import Path



def to_camel_case(name: str) -> str:
    """Return *name* converted to CamelCase without leading digits."""
    # Strip leading numeric prefixes like ``01_``
    name = re.sub(r"^\d+_?", "", name)
    parts = re.split(r"[_\-\s]+", name)
    return "".join(word.capitalize() for word in parts if word)




def generate_aggregate(folder: Path, output_dir: Path) -> None:
    """Create a single Markdown file aggregating all examples in *folder*."""
    examples = []
    for py_file in sorted(folder.glob("*.py")):
        if py_file.name == "__init__.py":
            continue
        with py_file.open("r", encoding="utf-8") as f:
            code = f.read().rstrip()
        examples.append((to_camel_case(py_file.stem), code))

    if not examples:
        return

    title = to_camel_case(folder.name)
    lines = [f"# {title}", ""]
    for name, code in examples:
        lines.append(f"## {name}")
        lines.append("")
        lines.append("```python")
        lines.append(code)
        lines.append("```")
        lines.append("")

    agg_path = output_dir / f"{folder.name}.md"
    with agg_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate aggregated Markdown files from the examples"
    )
    parser.add_argument(
        "--examples-dir",
        default="examples",
        help="Directory containing example .py files",
    )
    parser.add_argument(
        "--output-dir",
        default="docs",
        help="Directory where Markdown files will be written",
    )
    args = parser.parse_args()

    examples_dir = Path(args.examples_dir)
    output_dir = Path(args.output_dir)
    # Ensure the output directory exists but do not wipe it if it already
    # contains files. ``exist_ok=True`` prevents accidental deletion of
    # previously generated documentation.
    output_dir.mkdir(parents=True, exist_ok=True)



    for folder in sorted(examples_dir.iterdir()):
        if folder.is_dir():
            generate_aggregate(folder, output_dir)


if __name__ == "__main__":
    main()
