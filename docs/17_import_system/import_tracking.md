# import_tracking

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
