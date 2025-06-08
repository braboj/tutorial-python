# Define the packet API
__version__ = '1.0.0'

# The dot(.) operator is used to import modules relative to the current package.
# A single dot (.) refers to the current package.
# Two dots (..) refer to the parent package.
# Three dots (...) refer to the grandparent package, and so on.

from .api.submodule1 import func1
from .core.submodule2 import func2
from .gui.submodule3 import func3


# The __all__ variable is used to define the public API of a module or a package.
__all__ = ['func1', 'func2', 'func3']


# Export decorator
def export(defn):

    # Add the object to the global namespace
    globals()[defn.__name__] = defn

    # Set the object to be exported
    __all__.append(defn.__name__)

    # Return the object
    return defn


# Example of the export decorator
@export
def func4():
    print('func4')