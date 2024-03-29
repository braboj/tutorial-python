# The delattr() deletes an attribute from the object (if the object allows it).

class Coordinate(object):
    x = 10
    y = 10
    z = 10


point1 = Coordinate()

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)

delattr(Coordinate, 'z')

try:
    print('--After deleting z attribute--')
    print('x = ',point1.x)
    print('y = ',point1.y)
    print('z = ',point1.z)
except AttributeError:
    pass

del Coordinate.y

try:
    print('--After deleting y attribute--')
    print('x = ',point1.x)
    print('y = ',point1.y)
    print('z = ',point1.z)
except AttributeError:
    pass

