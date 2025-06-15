# encapsulation

```python
# Encapsulation: guarding internal state with getters and setters
# -----------------------------------------------------------------------------
# Encapsulation hides internal state behind methods.  Properties provide a
# controlled interface so that validation logic in setters and getters can
# protect the data from invalid values or direct manipulation.

class Person(object):
    """Represents a person with controlled access to internal state."""

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
        if age is None:
            raise ValueError("age cannot be None")

        elif age < 0:
            raise ValueError("age cannot be negative")

        elif age > 150:
            raise ValueError("age cannot be greater than 150")

        self.__age = age


person = Person("John", 30)
print(person.name)
print(person.age)
```
