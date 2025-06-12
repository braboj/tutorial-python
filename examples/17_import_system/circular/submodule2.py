# Second module that completes the circular import chain.
# ------------------------------------------------------------------------------
# Imports submodule1 to complete the cycle.
from . import submodule1

def func2():
    submodule1.func3()
