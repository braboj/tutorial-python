# Import System

## Export Decorator

```python
# Defines an export decorator for populating a package's __all__.
# ------------------------------------------------------------------------------
# Utility that adds functions to a package's __all__.
# Demonstrates placing the export decorator in a package's __init__ file

# Export decorator
def export(defn):
    # Add the object to the global namespace
    globals()[defn.__name__] = defn

    # Set the object to be exported
    __all__.append(defn.__name__)

    # Return the object
    return defn


# Demonstration of the export decorator
@export
def func4():
    print('func4')
```

## Import Absolute

```python
# Shows how to enforce and use absolute imports.
# ------------------------------------------------------------------------------
# Example script demonstrating absolute imports.
# Using absolute imports
import asyncio

# Enforce absolute imports
from __future__ import absolute_import

# Absolute imports
from foo.api.submodule1 import func1
from foo.core.submodule2 import func2
from foo.gui.submodule3 import func3

# Call all functions
func1()
func2()
func3()
```

## Import Circular

```python
# Triggers a circular import between two submodules.
# ------------------------------------------------------------------------------
# Runs the circular import scenario.
import circular.submodule1 as submodule1

submodule1.func1()
```

## Import Conditional

```python
# Shows conditional imports based on Python version.
# ------------------------------------------------------------------------------
# Uses different imports depending on Python version.
import sys

# Option 1
try:
    import Queue as queue
except ImportError:
    import queue

q = queue.Queue()
print(q)

# Option 2
is_py2 = sys.version[0] == '2'
if is_py2:
    import Queue as test2
else:
    import queue as test2

q = test2.Queue()
print(q)
```

## Import Main Module

```python
# Demonstrates __main__ name when executing a module as a script.
# ------------------------------------------------------------------------------
# Shows module __name__ when executed directly.
# Main program entry point

import pprint

# The module attribute __name__ is set to '__main__' when the module is run as the main program.
print(globals()['__name__'])
```

## Import Module Objects

```python
# Shows manual creation of ModuleType objects to demonstrate import internals.
# ------------------------------------------------------------------------------
# Creates modules manually via ModuleType.
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
```

## Import Namespaces

```python
# Explores namespaces at different scopes using builtins and custom classes.
# ------------------------------------------------------------------------------
# Traces namespace dictionaries at various scopes.
# Namespace of the builtins module.

import pprint


class MyClass(object):

    def __init__(self):
        self.a = 1
        self.b = 2

    def instance_method(self):
        pprint.pprint("INSTANCE GLOBALS: {}".format(globals().keys()))
        pprint.pprint("INSTANCE LOCALS: {}".format(locals().keys()))
        print()

    @classmethod
    def class_method(cls):
        pprint.pprint("CLASS GLOBALS: {}".format(globals().keys()))
        pprint.pprint("CLASS LOCALS: {}".format(locals().keys()))
        print()

    def func1(self):

        print("@FUNC1: Before the assignment of a")
        pprint.pprint("FUNC1 GLOBALS: {}".format(globals().keys()))
        pprint.pprint("FUNC1 LOCALS: {}".format(locals().keys()))
        print()

        a = 1

        print("@FUNC1: After the assignment of a")
        pprint.pprint("FUNC1 GLOBALS: {}".format(globals().keys()))
        pprint.pprint("FUNC1 LOCALS: {}".format(locals().keys()))
        print()

        def func2():

            print("@FUNC2: Before the assignment of b")
            pprint.pprint("FUNC2 GLOBALS: {}".format(globals().keys()))
            pprint.pprint("FUNC2 LOCALS: {}".format(locals().keys()))
            print()

            b = a + 1

            print("@FUNC2: After the assignment of b")
            pprint.pprint("FUNC2 GLOBALS: {}".format(globals().keys()))
            pprint.pprint("FUNC2 LOCALS: {}".format(locals().keys()))
            print()

        func2()

        print("@FUNC1: After the call to func2")
        pprint.pprint("FUNC1 GLOBALS: {}".format(globals().keys()))
        pprint.pprint("FUNC1 LOCALS: {}".format(locals().keys()))
        print()


# Builtins level
print("===== Builtins namespace =====")
print()
pprint.pprint("BUILTINS VARS: {}".format(vars(__builtins__).keys()))
print()

# Module level
print("===== Module namespace =====")
print()
pprint.pprint("MODULE GLOBALS VARS: {}".format(globals().keys()))
pprint.pprint("MODULE LOCALS VARS: {}".format(locals().keys()))
print()

# Class level
print("===== Class namespace =====")
print()
pprint.pprint("CLASS VARS: {}".format(vars(MyClass).keys()))
MyClass.class_method()
print()

# Instance level
print("===== Instance namespace =====")
print()
my_instance = MyClass()
print(vars(my_instance))
my_instance.instance_method()
print()

# Function level
print("===== Function namespace =====")
print()
my_instance.func1()
print(vars(my_instance.func1))
print()
```

## Import Packages

```python
# Demonstrates importing a package and using its public API.
# ------------------------------------------------------------------------------
# Imports the foo package and uses its API.
import product

# Use the public API defined in __init__.py
product.func1()
product.func2()
product.func3()
```

## Import Process

```python
# Implements a minimal importer to show how Python loads modules.
# ------------------------------------------------------------------------------
# Minimal demonstration of how the import statement works.
# A naive implementation of the import statement

import marshal
import os
import sys
import types


def _import(module_name):

    # Check if the module is already imported
    if module_name in sys.modules:
        print('Module already imported')
        return sys.modules[module_name]

    # Read the source code from the file
    sourcepath = module_name + '.py'
    with open(sourcepath, 'r') as f:
        sourcecode = f.read()

    # Compile the source code to bytecode
    code = _compile(sourcecode, sourcepath, module_name)

    # Create a new module object
    module = types.ModuleType(module_name)
    module.__file__ = sourcepath

    # Cache the module object in sys.modules
    sys.modules[module_name] = module

    # Execute the bytecode in the module's namespace
    exec(code, module.__dict__)

    # Return the module object
    return sys.modules[module_name]


def _compile(sourcecode, sourcepath, module_name):
    # Compile the source code of a module to bytecode.
    # --------------------------------------------------------------------------------
    # Compiles the code and optionally writes a .pyc file.

    MAGIC_NUMBER = (3439).to_bytes(2, 'little') + b'\r\n'

    # Compile the source code to bytecode
    code = compile(sourcecode, sourcepath, 'exec')

    # The following code is optional

    # Serialize the code object and write it to a .pyc file
    with open(module_name + '.pyc', 'wb') as f:
        mtime = os.path.getmtime(sourcepath)
        size = os.path.getsize(sourcepath)
        f.write(MAGIC_NUMBER)
        f.write(int(mtime).to_bytes(4, sys.byteorder))
        f.write(int(size).to_bytes(4, sys.byteorder))
        marshal.dump(code, f)

    return code


if __name__ == '__main__':
    s1 = _import('./foo/api/submodule1')
    s2 = _import('./foo/api/submodule1')
    print(s1.my_id, s2.my_id)
```

## Import Search Path

```python
# Displays and modifies sys.path to demonstrate search paths.
# ------------------------------------------------------------------------------
# Displays and alters sys.path for searching modules.
# Demonstrates the import search path

import sys
import pprint

from api import submodule1
print('submodule1.my_id =', submodule1.my_id)

# Print the search path
paths = sys.path
for path in paths:
    print(path)

print()

# Add the current directory to the search path
sys.path.append('.')
paths = sys.path
for path in paths:
    print(path)
```

## Import Skip Execution

```python
# Demonstrates guarding code with __name__ to skip execution on import.
# ------------------------------------------------------------------------------
# Guard code to avoid running on import.
# Main program entry point


def func1():
    return 1


def func2():
    return 2


def func3():
    return 3


def test_module():
    assert func1() == 1
    assert func2() == 2
    assert func3() == 3


# The following code prevents the module to be executed when imported as a
# module. It will be executed only when run as a script directly by the Python
# interpreter. If omitted the module will be executed on each import.

if __name__ == '__main__':
    test_module()
```

## Import Statements

```python
# Illustrates various forms of the import statement.
# ------------------------------------------------------------------------------
# Shows many forms of the import statement in use.
# Import statements in action.

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
```

## Import Sys Path

```python
# Shows sys.path details via prefix values.
# ------------------------------------------------------------------------------
# Prints prefix values from sys.path.
import sys
print(sys.prefix)
print(sys.exec_prefix)
```

## Import Tracking

```python
# Replaces builtins.__import__ to trace loaded modules.
# ------------------------------------------------------------------------------
# Wraps __import__ to log module names.
def my_import(modname, *args, imp=__import__):
    print('importing', modname)
    return imp(modname, *args)


import builtins
builtins.__import__ = my_import
import socket
```

## Rootdir

```python
# Absolute path to this directory for search path tests.
# ------------------------------------------------------------------------------
# Convenient variable for retrieving this directory.
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
```
