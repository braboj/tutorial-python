# Example: Very naive implementation of the import statement

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
    """ Compile the source code of a module to bytecode. """

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
    s1 = _import('./product/api/submodule1')
    s2 = _import('./product/api/submodule1')
    print(s1.my_id, s2.my_id)
