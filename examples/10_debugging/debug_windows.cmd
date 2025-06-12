@echo off
REM Debugging a Python Script on Windows
REM --------------------------------------------------------------------------------
REM This batch file launches the Python debugger for the specified script.
REM Provide the path to the program as the first argument and step through
REM the code interactively.

python -m pdb %1
