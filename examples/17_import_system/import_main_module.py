"""Demonstrates __main__ name when executing a module as a script."""
# Example: Main program

import pprint

# The module attribute __name__ is set to '__main__' when the module is run as the main program.
print(globals()['__name__'])