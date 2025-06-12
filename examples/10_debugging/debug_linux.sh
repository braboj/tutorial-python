#!/usr/bin/env bash
# Debugging a Python Script on Linux
# --------------------------------------------------------------------------------
# This shell script starts the Python debugger for the target file.
# Provide the path to the program as the first argument and control execution
# interactively. The script can be modified to pass extra options if needed.

python -m pdb "$1"
