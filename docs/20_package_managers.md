# Package Managers

## Package List

```python
# Listing installed packages
# -----------------------------------------------------------------------------
# This example prints all installed distributions using ``pkg_resources`` from
# ``setuptools``. It can help inspect the current Python environment.

import pkg_resources

for dist in sorted(pkg_resources.working_set, key=lambda d: d.project_name.lower()):
    print(f"{dist.project_name}=={dist.version}")
```

## Package Pip Install

```python
# Installing a package with pip
# -----------------------------------------------------------------------------
# This example invokes ``pip`` through ``C05_subprocess`` to install the requested
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
```

## Package Pipenv

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

## Package Poetry

```python
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
```

## Package Uv

```python
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
```

## Package Virtualenv

```python
# Creating a virtual environment
# -----------------------------------------------------------------------------
# The ``venv`` module can be used to create isolated Python environments. This
# script programmatically creates one in the ``example_env`` directory.

from pathlib import Path
import venv


def create_env(path: Path) -> None:
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(path)
    print(f"Virtual environment created at {path}")


if __name__ == "__main__":
    create_env(Path("example_env"))
```
