# class_constructors

```python
# How __new__ and __init__ cooperate in object creation
# --------------------------------------------------------------------------------
# Object creation begins with __new__, which allocates the instance. The fresh
# object is then passed to __init__ for further initialization. Separating these
# steps gives developers flexibility to customize how objects come into
# existence.

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
```
