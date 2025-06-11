#!/usr/bin/env bash
# Install and run black on a file (Linux/macOS)
# Usage: ./lint_black_linux.sh <python_file>

pip install black
black "$1"
