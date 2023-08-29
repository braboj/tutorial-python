# Example: Initialization in multiple steps

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.step_1()
        self.step_2()

    def step_1(self):
        print("Step 1: Enter the person's name:")

    def step_2(self):
        print("Step 2: Enter the person's age:")


John = Person("John", 32)
