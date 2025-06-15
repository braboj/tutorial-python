# Linting Tools

## Lint Black

```python
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
```

## Lint Flake8

```python
# Linting code with flake8
# -----------------------------------------------------------------------------
# This script runs the ``flake8`` linter on the target file and reports
# any issues. It gracefully handles the case where flake8 is not installed.

import subprocess
import sys


def run_flake8(target: str) -> None:
    try:
        subprocess.run(["flake8", target], check=True)
    except FileNotFoundError:
        print("flake8 is not installed.")
    except subprocess.CalledProcessError as exc:
        print(f"flake8 found issues: {exc}")


if __name__ == "__main__":
    file_to_check = sys.argv[1] if len(sys.argv) > 1 else __file__
    run_flake8(file_to_check)
```

## Lint Pylint

```python
# Linting code with pylint
# -----------------------------------------------------------------------------
# ``pylint`` performs static code analysis. This script demonstrates how to
# call it from Python and handle common error cases.

import subprocess
import sys


def run_pylint(target: str) -> None:
    try:
        subprocess.run(["pylint", target], check=True)
    except FileNotFoundError:
        print("pylint is not installed.")
    except subprocess.CalledProcessError as exc:
        print(f"pylint found issues: {exc}")


if __name__ == "__main__":
    file_to_check = sys.argv[1] if len(sys.argv) > 1 else __file__
    run_pylint(file_to_check)
```
