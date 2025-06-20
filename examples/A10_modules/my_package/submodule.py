# Submodule inside ``my_package``
# ------------------------------------------------------------------------------
# This module defines the ``hello`` function. ``__init__.py`` re-exports this
# function so it can be imported directly from ``my_package``.


def hello():
    print('Hello from submodule')
