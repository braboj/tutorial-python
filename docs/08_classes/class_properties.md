# class_properties

```python
# Property used to encapsulate an instance variable
# --------------------------------------------------------------------------------
# The property decorator exposes getter and setter functions as attribute
# access. This allows validation or computation while keeping the public
# interface simple.

class Person(object):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self.__name = value


p = Person("John")
print(p.name)
```
