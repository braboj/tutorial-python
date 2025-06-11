#!/usr/bin/env bash
# Install uv and install a package (Linux/macOS)
# Usage: ./package_uv_linux.sh <package>

pip install uv
uv pip install "$1"
