#!/usr/bin/env bash
# Install pipenv and install a package (Linux/macOS)
# Usage: ./package_pipenv_linux.sh <package>

pip install pipenv
pipenv install "$1"
