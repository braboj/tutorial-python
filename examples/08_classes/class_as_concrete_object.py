# Object as concrete realization of a class
# --------------------------------------------------------------------------------
# The code creates an instance of the Person class as a tangible object.
# The constructor assigns initial values to the instance. After creation, the
# object can call its methods and access stored data.
from class_as_blueprint import Person


John = Person("John", 32)
John.say_hello()
