# class_init_steps

```python
# Initialization in multiple steps
# --------------------------------------------------------------------------------
# Some objects gather their initial data through a sequence of operations. This
# file breaks the process into helper methods that collect the values one by
# one. Each step can perform validation before returning its result.

class Person(object):
    def __init__(self):
        self.name = self.step_1()
        self.age = self.step_2()

    @staticmethod
    def step_1():
        name = input("Step 1: Enter the person's name: ")
        return name

    @staticmethod
    def step_2():
        age = input("Step 2: Enter the person's age: ")
        return age


john = Person()
print(john.name, john.age)
```
