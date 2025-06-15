#!/usr/bin/env python3
"""Generate a Markdown file for each Python example.

Usage:
    python .scripts/examples_to_markdown_files.py \
        --examples-dir examples \
        --template templates/example_file.mustache \
        --output-dir docs

The directory structure under ``examples`` is mirrored under the output
directory. Each ``.py`` file becomes a ``.md`` file with the same name and
relative path. Files named ``__init__.py`` are ignored and skipped.
"""

import argparse
import re
from pathlib import Path

try:
    import pystache
except ModuleNotFoundError as exc:  # pragma: no cover - import guard
    raise SystemExit(
        "pystache is required to run this script. Install it via `pip install pystache`."
    ) from exc


def parse_example(path: Path) -> dict:
    """Return the file name and entire contents of the example."""
    with path.open("r", encoding="utf-8") as f:
        code = f.read()
    return {"name": path.stem, "code": code.rstrip()}


def render_markdown(template: str, context: dict) -> str:
    """Render the Markdown using a Mustache template."""
    renderer = pystache.Renderer()
    return renderer.render(template, context)


def to_camel_case(name: str) -> str:
    """Return *name* converted to CamelCase without leading digits."""
    # Strip leading numeric prefixes like ``01_``
    name = re.sub(r"^\d+_?", "", name)
    parts = re.split(r"[_\-\s]+", name)
    return "".join(word.capitalize() for word in parts if word)


def process_file(py_path: Path, template: str, base_dir: Path, output_dir: Path) -> None:
    """Write a Markdown version of *py_path* under *output_dir*."""
    context = parse_example(py_path)
    markdown = render_markdown(template, context)

    relative = py_path.relative_to(base_dir).with_suffix(".md")
    md_path = output_dir / relative
    md_path.parent.mkdir(parents=True, exist_ok=True)
    with md_path.open("w", encoding="utf-8") as f:
        f.write(markdown)


def generate_aggregate(folder: Path, base_dir: Path, output_dir: Path) -> None:
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
        description="Generate Markdown files mirroring the examples directory"
    )
    parser.add_argument(
        "--examples-dir",
        default="examples",
        help="Directory containing example .py files",
    )
    parser.add_argument(
        "--template",
        default="templates/example_file.mustache",
        help="Mustache template file",
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

    with Path(args.template).open("r", encoding="utf-8") as f:
        template = f.read()

    for py_file in sorted(examples_dir.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue
        process_file(py_file, template, examples_dir, output_dir)

    for folder in sorted(examples_dir.iterdir()):
        if folder.is_dir():
            generate_aggregate(folder, examples_dir, output_dir)


if __name__ == "__main__":
    main()
