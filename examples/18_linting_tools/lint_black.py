# Formatting code with black
# -----------------------------------------------------------------------------
# This script demonstrates invoking the ``black`` code formatter from Python.
# It formats the target file if ``black`` is installed.

import subprocess
import sys


def run_black(target: str) -> None:
    try:
        subprocess.run(["black", target], check=True)
    except FileNotFoundError:
        print("black is not installed.")
    except subprocess.CalledProcessError as exc:
        print(f"black reported an error: {exc}")


if __name__ == "__main__":
    file_to_format = sys.argv[1] if len(sys.argv) > 1 else __file__
    run_black(file_to_format)
