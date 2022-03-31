"""
oct(x)

x: integer or class implementing __int__ or __index__

For compatibility, it's recommended to implement __int__() and __index__() with the same output.
"""

number = 435
print(number, 'in hex =', oct(number))


class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('The oct is:', oct(person))