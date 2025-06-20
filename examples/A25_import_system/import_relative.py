# Shows how to use relative imports within a package.
# ------------------------------------------------------------------------------
# Demonstrates importing modules from the current package using relative syntax.

from .foo.api.submodule1 import func1
from .foo.core.submodule2 import func2
# Relative imports are scoped to packages.

# Call the imported functions
func1()
func2()
