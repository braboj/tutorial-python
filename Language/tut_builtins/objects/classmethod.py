from datetime import date


##############################################################################
# Example A : Basic demonstration
##############################################################################
class ClassMethodTest(object):

    answer = 42

    @classmethod
    def test_method(cls):
        print(cls.answer)


ClassMethodTest.test_method()


##############################################################################
# Example B : Classmethod as factory method
##############################################################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.from_birth_year('John', 1985)
person1.display()
