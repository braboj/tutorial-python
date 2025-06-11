@echo off
REM Install poetry and add a package (Windows)
REM Usage: package_poetry_windows.cmd <package>

python -m pip install poetry
poetry add %1
