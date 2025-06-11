# Installing a package with pip
# -----------------------------------------------------------------------------
# This example invokes ``pip`` through ``subprocess`` to install the requested
# package. In real scenarios this requires network access.

import subprocess
import sys


def pip_install(package: str) -> None:
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
    except subprocess.CalledProcessError as exc:
        print(f"pip failed: {exc}")


if __name__ == "__main__":
    pkg = sys.argv[1] if len(sys.argv) > 1 else "requests"
    pip_install(pkg)
