# Demonstrates __main__ name when executing a module as a script.
# ------------------------------------------------------------------------------
# Shows module __name__ when executed directly.
# Main program entry point

import pprint

# The module attribute __name__ is set to '__main__' when the module is run as the main program.
print(globals()['__name__'])
