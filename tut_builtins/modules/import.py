"""
__import__(name, globals=None, locals=None, fromlist=(), level=0)

name - the name of the module you want to import
globals and locals - determines how to interpret name
fromlist - objects or submodules that should be imported by name
level - specifies whether to use absolute or relative imports

"""

mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))