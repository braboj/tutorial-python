"""
The exec() method executes the dynamically created program, which is either a string or a code object.

exec(object, globals, locals)

object - Either a string or a code object
globals (optional) - a dictionary
locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

If you allow users to input a value using exec(input()), the user may issue commands to change file or even delete
all the files using the command os.system('rm -rf *').

"""
from math import *

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

# program = input('Enter a program:')
# exec(program)

sqrt(25)
# exec('print(dir())', {})
# exec('print(sqrt(9))', {})

# exec('print(dir())', {'sqrt': sqrt, 'pow': pow})
# exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})
#
# exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})
# exec('print(squareRoot(9))', {'squareRoot': sqrt, 'pow': pow})

exec('print(dir())', {'__builtins__' : None}, {'print': print, 'dir': dir, 'sqrt': sqrt})
exec('print(sqrt(9))', {'__builtins__' : None}, {'print': print, 'dir': dir, 'sqrt': sqrt})