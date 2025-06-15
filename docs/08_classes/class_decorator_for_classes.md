# class_decorator_for_classes

```python
# Class as a decorator for a class
# --------------------------------------------------------------------------------
# A class can implement the __call__ method and be applied as a decorator to
# another class. When used this way it may attach attributes or modify the
# decorated class at definition time.
class Counter(object):

    # The constructor accepts the parameter passed to the decorator
    def __init__(self, start_value):
        self.counter = start_value

    # The __call__ method is called when the class is used as a decorator
    def __call__(self, cls):

        # Modify the class by adding an attribute with the specified value
        cls.counter = self.counter

        # Return the modified class
        return cls


# Apply the class decorator with a parameter
@Counter(start_value=1)
class DecoratedClass(object):
    pass


# Use the explicit decorator syntax
DecoratedClass = Counter(start_value=1)(DecoratedClass)
obj = DecoratedClass()
print(obj.counter)  # Output: 1


# Use Python's decorator syntax
obj = DecoratedClass()
print(obj.counter)  # Output: Custom Value
```
