# First module in a circular import chain.
# ------------------------------------------------------------------------------
# Imports submodule2 and exposes a function.
from . import submodule2


def func1():
    print('Begin circular import')
    submodule2.func2()


def func3():
    print('End of circular import')
