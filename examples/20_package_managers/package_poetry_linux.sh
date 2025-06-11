#!/usr/bin/env bash
# Install poetry and add a package (Linux/macOS)
# Usage: ./package_poetry_linux.sh <package>

pip install poetry
poetry add "$1"
