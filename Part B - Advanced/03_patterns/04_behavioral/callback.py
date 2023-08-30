"""
* Event handling
-> Blocking callbacks
-> Non-blocking callbacks

"""

import math


def get_sqrt(val):
    """Callback."""
    return math.sqrt(val)


def get_square(val):
    """Callback."""
    return val ** 2


def caller(func, val):
    return func(val)


val = caller(get_square, 2)
print(val)

val = caller(get_sqrt, 3)
print(val)
