"""Shows manual creation of ModuleType objects to demonstrate import internals."""
from types import ModuleType

# Create a new module object
test = ModuleType('test')
print("test.__dict__:", test.__dict__)

# Add some attributes to the module
test.__dict__['a'] = 1
test.__dict__['b'] = 2
test.__dict__['c'] = 3

# Print the module's namespace
print("test.__dict__:", test.__dict__)
