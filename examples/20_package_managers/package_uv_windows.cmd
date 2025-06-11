@echo off
REM Install uv and install a package (Windows)
REM Usage: package_uv_windows.cmd <package>

python -m pip install uv
uv pip install %1
