#!/usr/bin/env bash
# Install and run pylint on a file (Linux/macOS)
# Usage: ./lint_pylint_linux.sh <python_file>

pip install pylint
pylint "$1"
