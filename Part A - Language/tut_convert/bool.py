"""
The bool() method converts a value to Boolean (True or False) using the standard truth testing procedure. The
following values are considered false in Python:

None
False
Zero of any numeric type. For example, 0, 0.0, 0j
Empty sequence. For example, (), [], ''.
Empty mapping. For example, {}
objects of Classes which has __bool__() or __len()__ method which returns 0 or False

All other values except these values are considered true.
"""

test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
