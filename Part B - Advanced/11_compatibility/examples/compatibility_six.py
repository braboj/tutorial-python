# Example: six module

# The most commonly used imports from the six module
from six.moves import input  # Import the input function from the six.moves module
from six import with_metaclass  # Import the with_metaclass function from the six module


class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Allocating memory for class", name)
        return super(Meta, cls).__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print("Initializing class", name)
        super(Meta, cls).__init__(name, bases, dct)


class Base(with_metaclass(Meta)):
    def __init__(self):
        print("Initializing instance", self)
        super(Base, self).__init__()


class Derived(Base):
    def __init__(self):
        print("Initializing instance", self)
        super(Derived, self).__init__()


if __name__ == "__main__":
    # Use the six.moves.input function with Python 2 and 3
    input("Press Enter to continue...")

    # Use the six.with_metaclass function with Python 2 and 3
    print("Creating instance of Base")
    b = Base()
    print("Creating instance of Derived")
    d = Derived()
    print("Finished")
