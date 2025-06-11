@echo off
REM Install and run flake8 on a file (Windows)
REM Usage: lint_flake8_windows.cmd <python_file>

python -m pip install flake8
flake8 %1
