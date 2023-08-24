
class Calculator():

    def __new__(cls):
        obj = object.__new__(cls)
        print("__new__ : Created object {}".format(obj))
        return obj

    def __init__(self):
        print("__init__: Using object {}".format(self))
        self.name = "Cool Calculator"


calc = Calculator()
print(calc.name)