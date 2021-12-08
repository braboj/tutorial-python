"""
The setattr() function sets the value of the attribute of an object.

setattr(object, name, value)

object - object whose attribute has to be set
name - attribute name
value - value given to the attribute

If the attribute is not found, setattr() creates a new attribute an assigns value to it. However, this is only possible if the object implements the __dict__() method.
You can check all the attributes of an object by using the dir() function.
"""


class Person:
    name = 'Adam'


p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'John')

print('After modification:', p.name)


class Person:
    name = 'Adam'


p = Person()

# setting attribute name to John
setattr(p, 'name', 'John')
print('Name is:', p.name)

# setting an attribute not present in Person
setattr(p, 'age', 23)
print('Age is:', p.age)
