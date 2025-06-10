# Example: Different sources to create and initialize objects
import os


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_file(cls, file):

        with open(file, 'r') as f:
            data = f.read()
            name, age = data.split(',')

        return cls(name=name, age=age)


# Create a file named profile.txt with the following contents:
# mayank,27

with open('profile.txt', 'w') as f:
    f.write('mayank,27')

person = Person.from_file('profile.txt')
print(person.name, person.age)

# Delete the file profile.txt
os.remove('profile.txt')
