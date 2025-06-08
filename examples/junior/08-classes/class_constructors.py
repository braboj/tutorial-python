
class Calculator(object):

    def __new__(cls):

        # Use the parent class to create the object
        obj = object.__new__(cls)

        # Return the object
        print("__new__ : Created object {}".format(obj))
        return obj

    def __init__(self):

        # Self is the object that was created by __new__
        print("__init__: Using object {}".format(self))

        # Add attributes to the object
        self.name = "Cool Calculator"


calc = Calculator()
print(calc.name)