# class_as_blueprint

```python
# Class as template
# --------------------------------------------------------------------------------
# A class can act as a template from which many objects are built. This file
# defines a Person blueprint containing attributes and methods that every
# instance will share.

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is {} and my age is {}".format(self.name, self.age))
```
