class Polygon(object):
    def __init__(self):
        print('Polygon is a ', self)


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self)


print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))