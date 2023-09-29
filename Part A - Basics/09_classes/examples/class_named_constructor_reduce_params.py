# Example: Reduce the number of parameters

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size):
        return cls(size, size)


# Create a square using the default constructor
square1 = Rectangle(1, 1)
print(square1.width, square1.height)

# Create the same square using the named constructor
square2 = Rectangle.square(size=1)
print(square2.width, square2.height)



