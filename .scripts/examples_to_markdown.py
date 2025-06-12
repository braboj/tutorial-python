#!/usr/bin/env python3
"""Generate a Markdown page from Python example files.

Usage::
    python .scripts/examples_to_markdown.py \
        --examples-dir examples \
        --template templates/examples_page.mustache \
        --output examples.md

Each file's content is inserted verbatim as a code block in the output.  Files
named ``__init__.py`` are ignored.
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
    """Return the file name and its entire contents."""
    with path.open("r", encoding="utf-8") as f:
        code = f.read()

    return {
        "name": path.stem,
        "code": code.rstrip(),
    }


def gather_examples(directory: Path) -> list:
    """Collect all ``*.py`` files from the directory recursively."""
    examples = []
    for file in sorted(directory.rglob("*.py")):
        if file.name == "__init__.py":
            continue
        examples.append(parse_example(file))
    return examples


def render_markdown(template_path: Path, output_path: Path, examples: list) -> None:
    """Render the markdown file using a Mustache template."""
    with template_path.open("r", encoding="utf-8") as f:
        template = f.read()
    renderer = pystache.Renderer()
    markdown = renderer.render(template, {"examples": examples})
    with output_path.open("w", encoding="utf-8") as f:
        f.write(markdown)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate examples markdown")
    parser.add_argument(
        "--examples-dir",
        default="examples",
        help="Directory containing example .py files",
    )
    parser.add_argument(
        "--template",
        default="templates/examples_page.mustache",
        help="Mustache template file",
    )
    parser.add_argument(
        "--output",
        default="examples.md",
        help="Output markdown file",
    )
    args = parser.parse_args()

    examples = gather_examples(Path(args.examples_dir))
    render_markdown(Path(args.template), Path(args.output), examples)


if __name__ == "__main__":
    main()
