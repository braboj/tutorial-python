"""
A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.

Local symbol table stores all information related to the local scope of the program, and is accessed in Python
using locals() method. The local scope could be within a function, within a class, etc.

Unlike, globals() dictionary which reflects the change to the actual global table, locals() dictionary may not
change the information inside the locals table.
"""
from tutorial_builtins.helpers.globals import foo

if __name__ == "__main__":
    foo()
