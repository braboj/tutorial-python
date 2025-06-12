# Define and access instance attributes
# --------------------------------------------------------------------------------
# Instance attributes are defined in the __init__ method. They store data
# unique to each object and can be accessed through the instance of the class.

class Person(object):

    def __init__(self):
        self.name = "Branimir"
        self.age = 40


# Create the instance
p = Person()

# Access to the instance attributes
print(p.name)
print(p.age)
