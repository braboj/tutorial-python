#!/usr/bin/env python3
"""Generate a Markdown page from Python example files.

Usage:
    python .scripts/examples_to_markdown.py \
        --examples-dir examples \
        --template templates/examples_page.mustache \
        --output examples.md
"""

import argparse
from pathlib import Path
import pystache


def parse_example(path: Path) -> dict:
    """Extract description and code from a Python example file."""
    description_lines = []
    code_lines = []
    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    in_description = True
    for line in lines:
        if in_description and line.startswith("#"):
            description_lines.append(line.lstrip("# ").rstrip())
        else:
            in_description = False
            code_lines.append(line.rstrip())

    return {
        "name": path.stem,
        "description": "\n".join(description_lines).strip(),
        "code": "\n".join(code_lines).strip(),
    }


def gather_examples(directory: Path) -> list:
    """Collect all examples from the directory recursively."""
    examples = []
    for file in sorted(directory.rglob("*.py")):
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
