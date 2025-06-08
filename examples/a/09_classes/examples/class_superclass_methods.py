# Example: Call super class methods

class Person(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Employee(Person):

    def __init__(self, name, id_number):
        super(Employee, self).__init__(name)
        self.id_number = id_number

    def get_id_number(self):
        return self.id_number


e = Employee("John", 1234)
print(e.get_name())
print(e.get_id_number())

