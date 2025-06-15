# lint_pylint

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
