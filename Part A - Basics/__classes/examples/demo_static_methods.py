class Shape(object):

    @staticmethod
    def area():
        print(0)


class Circle(Shape):

    @staticmethod
    def area():
        print(1)


class Rectangle(Shape):

    @staticmethod
    def area():
        print(2)


Shape.area()
Circle.area()
Rectangle.area()