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
