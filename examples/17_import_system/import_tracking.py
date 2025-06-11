"""Replaces builtins.__import__ to trace loaded modules."""
def my_import(modname, *args, imp=__import__):
    print('importing', modname)
    return imp(modname, *args)


import builtins
builtins.__import__ = my_import
import socket