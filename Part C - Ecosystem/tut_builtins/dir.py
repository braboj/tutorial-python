number = [1, 2, 3]
print(dir(number))

print('\nReturn Value from empty dir()')
print(dir())


class Person(object):
    def __dir__(self):
        return ['age', 'name', 'salary']


teacher = Person()
print(dir(teacher))