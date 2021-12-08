"""
The globals() method returns the dictionary of the current global symbol table.

A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.
These include variable names, methods, classes, etc. There are mainly two kinds of symbol table.

A global symbol table stores all information related to the global scope of the program, and is accessed
in Python using globals() method. The global scope contains all functions, variables that are not associated with
any class or function.

"""

from pprint import pprint

a = 100
b = 4


def foo():
    x = 100 # x is a local variable
    print("###################################################################")
    print("# GLOBALS")
    print("###################################################################")
    pprint(globals())

    print("###################################################################")
    print("# LOCALS")
    print("###################################################################")
    pprint(locals())


if __name__ == "__main__":
    pprint(globals())
    globals()["a"] = 101
    print(a)