@echo off
REM Install pipenv and install a package (Windows)
REM Usage: package_pipenv_windows.cmd <package>

python -m pip install pipenv
pipenv install %1
