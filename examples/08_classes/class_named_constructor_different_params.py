# Example: Named constructors as alternative constructors

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_diagonal(cls, x1, y1, x2, y2):
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return cls(width, height)


# Create a square using the default constructor
rect1 = Rectangle(1, 1)
print(rect1.width, rect1.height)

# Create the same square using the named constructor
rect2 = Rectangle.from_diagonal(1, 1, 2, 2)
print(rect2.width, rect2.height)
