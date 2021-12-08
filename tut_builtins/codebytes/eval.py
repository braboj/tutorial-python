"""
In simple terms, the eval() function runs the python code (which is passed as an argument) within the program.

eval(expression, globals, locals)

expression - the string parsed and evaluated as a Python expression
globals (optional) - a dictionary
locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

If you allow users to input a value using eval(input()), the user may issue commands to change file or even delete
all the files using the command: os.system('rm -rf *').

"""
from math import *

x = 1
print(eval('x + 1'))

print(eval('dir()'))
print(eval('dir()', {}))
print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))
names = {'square_root': sqrt, 'power': pow}
print(eval('dir()', names))

a = 25
sqrt(a)
print(eval('sqrt(a)'))
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))
print(eval('sqrt(25)', {}))
