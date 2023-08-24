# Example: Call super class method and access super class attributes

class Person(object):

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, id_number):
        super(Employee, self).__init__(name)
        self.id_number = id_number


e = Employee("John", 1234)
print(e.name)
print(e.id_number)