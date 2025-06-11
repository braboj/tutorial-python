"""Illustrates various forms of the import statement."""
# Example: Import Statements

# Importing the package
import foo
print('version =', foo.__version__)

# Importing a submodule
import foo.api.submodule1
print('api.submodule1.my_id =', foo.api.submodule1.my_id)

# Importing the entire module with an alias
import foo.api.submodule1 as sm1
print('sm1.my_id =', sm1.my_id)

from foo.api import submodule1
print('submodule1.my_id =', submodule1.my_id)

from foo.api.submodule1 import my_id
print('my_id =', my_id)
