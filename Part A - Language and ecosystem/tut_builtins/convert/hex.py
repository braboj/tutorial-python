"""
hex(x)

x: integer or class implementing __int__ or __index__

For compatibility, it's recommended to implement __int__() and __index__() with the same output.

"""
number = 435
print(number, 'in hex =', hex(number))

number = 2.5
print(number, 'in hex =', float.hex(number))