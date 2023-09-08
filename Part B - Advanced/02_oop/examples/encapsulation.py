# Example: Encapsulation with getters and setters

class Person(object):
    """ The abstract base class for a person answers what a person shall be able to do. """

    def __init__(self, name, age):

        # Modify the access to the internal state
        self.__name = name
        self.__age = age

    @property
    def name(self):
        """ The getter for the name """
        return self.__name

    @name.setter
    def name(self, name):
        """ The setter for the name """

        # Protection logic
        if name is None:
            raise ValueError("name cannot be None")

        self.__name = name

    @property
    def age(self):
        """ The getter for the age """

        return self.__age

    @age.setter
    def age(self, age):
        """ The setter for the age """

        # Protection logic
        if self.__age is None:
            raise ValueError("age cannot be None")

        elif self.__age < 0:
            raise ValueError("age cannot be negative")

        elif self.__age > 150:
            raise ValueError("age cannot be greater than 150")

        self.__age = age


person = Person("John", 30)
print(person.name)
print(person.age)
