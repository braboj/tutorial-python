# Installing packages with uv
# -----------------------------------------------------------------------------
# ``uv`` is a modern package manager that can replace ``pip``. This script
# demonstrates invoking ``uv pip install`` to install a package.

import subprocess
import sys


def uv_install(package: str) -> None:
    try:
        subprocess.run(["uv", "pip", "install", package], check=True)
    except FileNotFoundError:
        print("uv is not installed.")
    except subprocess.CalledProcessError as exc:
        print(f"uv failed: {exc}")


if __name__ == "__main__":
    pkg = sys.argv[1] if len(sys.argv) > 1 else "requests"
    uv_install(pkg)
