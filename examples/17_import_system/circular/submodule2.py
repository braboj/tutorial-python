"""Second module that completes the circular import chain."""
from . import submodule1

def func2():
    submodule1.func3()