#!/usr/bin/env bash
# Install and run flake8 on a file (Linux/macOS)
# Usage: ./lint_flake8_linux.sh <python_file>

pip install flake8
flake8 "$1"
