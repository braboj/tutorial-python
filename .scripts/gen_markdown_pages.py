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


def process_file(py_path: Path, template: str, base_dir: Path, output_dir: Path) -> None:
    """Write a Markdown version of *py_path* under *output_dir*."""
    context = parse_example(py_path)
    markdown = render_markdown(template, context)

    relative = py_path.relative_to(base_dir).with_suffix(".md")
    md_path = output_dir / relative
    md_path.parent.mkdir(parents=True, exist_ok=True)
    with md_path.open("w", encoding="utf-8") as f:
        f.write(markdown)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Markdown files mirroring the examples directory"
    )
    parser.add_argument(
        "--examples-dir",
        default="../examples",
        help="Directory containing example .py files",
    )
    parser.add_argument(
        "--template",
        default="../templates/example_file.mustache",
        help="Mustache template file",
    )
    parser.add_argument(
        "--output-dir",
        default="../docs",
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


if __name__ == "__main__":
    main()
