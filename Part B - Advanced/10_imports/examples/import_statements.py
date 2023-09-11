# Example: Import Statements

# Importing the package
import product
print('version =', product.__version__)

# Importing a submodule
import product.api.submodule1
print('api.submodule1.my_id =', product.api.submodule1.my_id)

# Importing the entire module with an alias
import product.api.submodule1 as sm1
print('sm1.my_id =', sm1.my_id)

from product.api import submodule1
print('submodule1.my_id =', submodule1.my_id)

from product.api.submodule1 import my_id
print('my_id =', my_id)
