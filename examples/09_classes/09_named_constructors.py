# Named constructors provide alternative ways to create instances of a class
# --------------------------------------------------------------------------------
# A class can offer several named constructors for convenience. Each one accepts
# parameters tailored for a specific situation and returns a configured
# instance.

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_diagonal(cls, x1, y1, x2, y2):
        """Usecase: Alternative constructor parameters."""
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return cls(width, height)

    @classmethod
    def square(cls, size):
        """Usecase: Reduced constructor parameters."""
        return cls(size, size)

    @classmethod
    def from_file(cls, file):
        """Usecase: Create an instance from a file."""

        with open(file, 'r') as f:
            data = f.read()
            x1, y1, x2, y2 = data.split(',')

        return cls.from_diagonal(float(x1), float(y1), float(x2), float(y2))

    @classmethod
    def from_json(cls, data):
        """Usecase: Create an instance from JSON data object."""
        return cls(**data)
