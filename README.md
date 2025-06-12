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

The script requires the `pystache` package which is listed in
`requirements.txt`.

## License
This project is licensed under the [MIT License](LICENSE).
