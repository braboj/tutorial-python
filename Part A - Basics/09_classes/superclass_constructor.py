# Example: Call __new__ method of super class

class Person(object):

    def __new__(cls, name):
        return super(Person, cls).__new__(cls)

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __new__(cls, name, id_number):
        return super(Employee, cls).__new__(cls, name)

    def __init__(self, name, id_number):
        super(Employee, self).__init__(name)
        self.id_number = id_number


e = Employee("John", 1234)
print(e.name)
print(e.id_number)
