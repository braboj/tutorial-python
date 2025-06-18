# Property used to encapsulate an instance variable
# --------------------------------------------------------------------------------
# The `@property` decorator exposes getter and setter functions as attribute
# access. This allows validation or computation while keeping the public
# interface simple as if it were a regular attribute accessed using dot
# notation.

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # -------- Getter and Setter for name --------
    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    # -------- Getter/Setter acting as  --------
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._age = value


# Explicit getter/setter methods
person = Person("John", 30)
person.set_name("Jane")
print(person.get_name())
# Output: Jane

# Getter/setter as property (acting as an attribute)
person.age = 35
print(person.age)
# Output: 35
