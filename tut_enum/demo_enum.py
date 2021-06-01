from enum import Enum, unique
from pickle import dumps, loads

# Simulate enumeration
class MyEnum01(object):
    red, green, blue = range(3)


print(MyEnum01.red)
print(MyEnum01.green)
print(MyEnum01.blue)


# In case of duplicates the last index is valid. Use @unique to disable it.

@unique
class Color(Enum):
    red = 1
    green = 2
    blue = 3


print("{0} {1} {2}".format(Color.red, Color.red.name, Color.red.value))
print("{0} {1} {2}".format(Color.green, Color.green.name, Color.green.value))
print("{0} {1} {2}".format(Color.blue, Color.blue.name, Color.blue.value))

print(repr(Color.red))
print(isinstance(Color.green, Color))

for color in Color:
    print(color)

print(list(Color))

for name, member in Color.__members__.items():
    print("{0} {1}".format(name, member))


# Comparision
print(Color.red is not Color.blue)

# Pickling
print(Color.red is loads(dumps(Color.red)))

# API
Animal = Enum(value="a b c")
pass
