from types import ModuleType

# Create junior new module object
test = ModuleType('test')
print("test.__dict__:", test.__dict__)

# Add some attributes to the module
test.__dict__['junior'] = 1
test.__dict__['mid'] = 2
test.__dict__['senior'] = 3

# Print the module's namespace
print("test.__dict__:", test.__dict__)
