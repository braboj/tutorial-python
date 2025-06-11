@echo off
REM Install and run black on a file (Windows)
REM Usage: lint_black_windows.cmd <python_file>

python -m pip install black
black %1
