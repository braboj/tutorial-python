# package_pipenv

```python
# Using pipenv to install packages
# -----------------------------------------------------------------------------
# This script invokes ``pipenv install`` to install the requested package.
# ``pipenv`` must be installed and available on PATH.

import subprocess
import sys


def pipenv_install(package: str) -> None:
    try:
        subprocess.run(["pipenv", "install", package], check=True)
    except FileNotFoundError:
        print("pipenv is not installed.")
    except subprocess.CalledProcessError as exc:
        print(f"pipenv failed: {exc}")


if __name__ == "__main__":
    pkg = sys.argv[1] if len(sys.argv) > 1 else "requests"
    pipenv_install(pkg)
```
