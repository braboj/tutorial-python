@echo off
REM Install and run pylint on a file (Windows)
REM Usage: lint_pylint_windows.cmd <python_file>

python -m pip install pylint
pylint %1
