# class_init_validate

```python
# Initialization and validation
# --------------------------------------------------------------------------------
# Initialization may involve checking that provided values meet certain rules.
# The constructor validates input before assigning it to attributes. Invalid
# data is rejected to keep the object's state consistent.

class Person(object):

        def __init__(self, name, age):
            self.name = name
            self.age = age

            if not isinstance(self.name, str):
                raise TypeError("Name must be a string")

            if not isinstance(self.age, int):
                raise TypeError("Age must be an integer")

            if self.age < 0:
                raise ValueError("Age must be a positive integer")

        def say_hello(self):
            print("Hello, my name is {} and my age is {}".format(self.name, self.age))


john = Person("John", 32)
john.say_hello()
```
