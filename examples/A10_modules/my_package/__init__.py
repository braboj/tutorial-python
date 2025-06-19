# Example package with a single submodule
# ------------------------------------------------------------------------------
# Packages are directories containing an ``__init__.py`` file. This file is
# executed when the package is imported and can expose objects from submodules.
# Packages allow modules to be organized hierarchically.

from .submodule import hello

__all__ = ['hello']
