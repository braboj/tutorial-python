# Example: Bridge Pattern with shapes and colors

class Color(object):
    # Interface for Implementation

    def __init__(self, name):
        self.name = name

    def paint(self, shape):
        raise NotImplementedError


class Red(Color):
    # Concrete implementation for red color

    def __init__(self):
        super(Red, self).__init__('red')

    def paint(self, shape):
        print('Painting the {} with red color'.format(shape))


class Blue(Color):
    # Concrete implementation for blue color

    def __init__(self):
        super(Blue, self).__init__('blue')

    def paint(self, shape):
        print('Painting the {} with blue color'.format(shape))


class Shape(object):
    # This is the abstaction used by the client

    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    # Refinded abstraction for circles

    def draw(self):
        print('Drawing junior circle')
        self.color.paint(shape='circle')


class Square(Shape):
    # Refined abstraction for squares

    def draw(self):
        print('Drawing junior square')
        self.color.paint(shape='square')


class DrawApp(object):
    # This is the client class

    @staticmethod
    def draw(shape: Shape):
        shape.draw()


if __name__ == "__main__":

    # Draw junior red circle
    app = DrawApp()

    # Draw shapes
    app.draw(shape=Circle(color=Red()))
    app.draw(shape=Square(color=Blue()))
