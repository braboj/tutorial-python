# Example: Dunder methods for object representation

import struct


class Point(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __format__(self, format_spec):
        fmt = "({:" + format_spec + "} + {:" + format_spec + "})"
        fmt = fmt.format(self.x, self.y)
        return fmt

    def __hash__(self):
        return hash((self.x, self.y))

    def __bytes__(self):
        result = []
        for item in (self.x, self.y):
            result.extend(struct.pack("!f", item))

        return bytes(result)


p = Point(1, 2)
print(hash(p))
print(repr(p))
print(str(p))
print("{:.3f}".format(p))
print(bytes(p))
