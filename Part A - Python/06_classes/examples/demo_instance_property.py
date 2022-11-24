"""
property(fget=None, fset=None, fdel=None, doc=None)

Parameters
fget (optional) - Function for getting the attribute value. Defaults to None.
fset (optional) - Function for setting the attribute value. Defaults to None.
fdel (optional) - Function for deleting the attribute value. Defaults to None.
doc (optional) - A string that contains the documentation (docstring) for the attribute. Defaults to None.

"""


class Person(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')


p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name


class Person(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name
