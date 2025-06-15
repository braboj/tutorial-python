# lint_flake8

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
