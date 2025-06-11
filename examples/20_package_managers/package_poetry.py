# Managing packages with poetry
# -----------------------------------------------------------------------------
# This script calls ``poetry add`` to add the requested package to the
# ``pyproject.toml`` of the current directory. ``poetry`` must be installed.

import subprocess
import sys


def poetry_add(package: str) -> None:
    try:
        subprocess.run(["poetry", "add", package], check=True)
    except FileNotFoundError:
        print("poetry is not installed.")
    except subprocess.CalledProcessError as exc:
        print(f"poetry failed: {exc}")


if __name__ == "__main__":
    pkg = sys.argv[1] if len(sys.argv) > 1 else "requests"
    poetry_add(pkg)
