# Using a custom module defined in the same directory
# ------------------------------------------------------------------------------
# A *module* is simply a Python file that defines variables, functions, or
# classes. This example imports ``mymodule`` and calls its functions. Modules
# help organize related code and can be reused across projects.

import mymodule

print(mymodule.greet('World'))
print('Area of circle:', mymodule.area_circle(3))
print('Module name:', mymodule.__name__)
