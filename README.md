# Python by Example

by Branimir Georgiev (www.codewithbranko.com)

This tutorial offers a comprehensive set of examples for the Python programming
language for junior, intermediate, and advanced programmers. It covers
everything from the basics of Python syntax to advanced topics like
SOLID principles, design patterns, and best practices.

## Pre-requisites

Ensure that the following tools are installed before setting up the project:

- **Python 3.10+** - the examples rely on modern Python features
- **git** - to clone this repository

## Installation

Create a virtual environment and install dependencies:

### Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows

```cmd
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Generating a Markdown page from examples

Use the `examples_to_markdown` script to collect all example files and render
them via a Mustache template. The command below writes the output to
`examples.md`:

```bash
python .scripts/examples_to_markdown.py \
    --examples-dir examples \
    --template templates/examples_page.mustache \
    --output examples.md
```

Files named `__init__.py` are automatically ignored when collecting examples.

Each file's contents are included verbatim as a code block in the generated
page; no attempt is made to parse comments or headings from the code.

The script requires the `pystache` package which is listed in
`requirements.txt`.

## Generating Markdown files for each example

To replicate the `examples` directory tree as Markdown files, run:

```bash
python .scripts/examples_to_markdown_files.py \
    --examples-dir examples \
    --template templates/example_file.mustache \
    --output-dir docs
```

The script mirrors the directory layout under `examples` inside `docs`.
Each `foo.py` becomes `foo.md` containing the source code in a single code
block. Any `__init__.py` files are ignored.

## Building the documentation site

This project can publish its Markdown files as a static website using
[MkDocs](https://www.mkdocs.org/). After installing the dependencies listed in
`requirements.txt` (which now include `mkdocs`). The navigation menu in
`mkdocs.yml` mirrors the directory layout under `docs/`. Regenerate the menu
and build the site with:

```bash
python .scripts/update_mkdocs_nav.py
mkdocs build
```



Preview the pages locally by running `mkdocs serve` and opening the displayed
URL in your browser. The generated HTML files are written to the `site/`
directory.

## License
This project is licensed under the [MIT License](LICENSE).
