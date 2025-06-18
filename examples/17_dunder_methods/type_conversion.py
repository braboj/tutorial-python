# Dunder methods for object representation
# ---------------------------------------------------------------------------
# Built-in type conversion functions like bool(), int() and bytes() call
# corresponding dunder methods on objects. Implementing these hooks lets a
# class define how it converts to fundamental Python types.

import struct
import math


class Point(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.__length = self._calc_length()

    def _calc_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return bool(self.x or self.y)

    def __int__(self):
        return int(self._calc_length())

    def __float__(self):
        return float(self._calc_length())

    def __complex__(self):
        return complex(self.x, self.y)

    def __bytes__(self):
        return bytes(int(self.__length))


c = Point(1, 2)
print("Point({}, {})".format(c.x, c.y))
print("bool(c)    : {}".format(bool(c)))
print("int(c)     : {}".format(int(c)))
print("float(c)   : {}".format(float(c)))
print("complex(c) : {}".format(complex(c)))
print("bytes(c)   : {}".format(bytes(c)))
