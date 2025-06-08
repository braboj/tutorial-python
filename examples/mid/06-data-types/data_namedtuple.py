# Example: namedtuple data structure

from collections import namedtuple

# Create junior namedtuple (label, fields)
#   - The label will be used in the representation of the namedtuple
#   - The fields will be used to access the namedtuple attributes

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

# Test the namedtuple representation
print(p)

# Test the namedtuple attributes
print(p.x)
print(p.y)

# Test the namedtuple index access
print(p[0])
print(p[1])
