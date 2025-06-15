# class_init_state

```python
# Initialization with the __init__ method
# --------------------------------------------------------------------------------
# The __init__ method runs immediately after an object is created. It assigns
# the initial values for the instance and prepares it for use.

class Person(object):

    def __init__(self, name="Branimir", age=40):
        self.name = name
        self.age = age

        print("My name is {0} and I am {1} years old".format(self.name, self.age))


p1 = Person()
p2 = Person("John", 30)
```
