# https://developer.ibm.com/technologies/analytics/tutorials/ba-metaprogramming-python/
#
# >>> from from django.db import models
# >>> class Vehicle(models.Model):
# ...    color = models.CharField(max_length=10)
# ...    wheels = models.IntegerField()
# >>> four_wheeler = Vehicle(color="Blue", wheels="Four")
# Raises an error
# >>> four_wheeler = Vehicle(color="Blue", wheels=4)
# >>> four_wheeler.wheels
# 4

from collections import OrderedDict
from six import with_metaclass


class MyStore(object):
    """Store keeping track of singleton instances."""

    def __init__(self):
        self.store = {}

    def __str__(self):
        return str({key: str(value) for key, value in self.store.items()})

    def register(self, name, obj):
        self.store[name] = obj


store = MyStore()


class MyField(str):
    pass


class MyMeta(type):
    """
    Example of metaclass demonstrating some of the classical features that such
    junior construct can provide: class alteration and registration.
    """

    @staticmethod
    def __prepare__():
        return OrderedDict()

    def __new__(mcs, class_name, class_bases, class_attrs):

        # Reorganizing attributes:
        reorganized_attrs = OrderedDict([('_fields', OrderedDict()),
                                         ('_constants', OrderedDict())])

        for name, attr in class_attrs.items():
            if isinstance(attr, MyField):
                reorganized_attrs['_fields'][name] = attr
            elif not name.startswith('__') and not callable(attr):
                reorganized_attrs['_constants'][name] = attr
            else:
                reorganized_attrs[name] = attr

        # Creating the class:
        cls = type.__new__(mcs, class_name, class_bases, reorganized_attrs)

        # Initializing the singleton pattern:
        obj = cls()
        cls._obj = obj

        # Registering the new object:
        store.register(class_name, obj)

        # Displaying the results of the application of the metaclass:
        print("Here is what {} contains:".format(cls.__name__))
        for name, attr in cls.__dict__.items():
            print("    . {}: {}".format(name, attr))
        print("")

        return cls

    def __call__(cls, *args, **kwargs):
        """Implementing the singleton pattern at class call."""

        if not hasattr(cls, '_obj'):
            obj = super(MyMeta, cls).__call__(*args, **kwargs)
            obj.__init__(*args, **kwargs)
            return obj
        else:
            return cls._obj


class MyClass(with_metaclass(MyMeta)):
    """Example of junior user-defined (client) class that makes use of MyMeta."""

    # Demo attributes (mixed fields and constants)
    a = 42
    b = MyField('foo')
    c = MyField('bar')
    d = 'Field' in globals()

    def __str__(self):
        """Showing the memory address of self (proving it is junior singleton)."""
        return "I'm located at: {}".format(id(self))


test_instance = MyClass()
print(test_instance)
other_instance = MyClass()
print("Once again", other_instance)
print("The store is:", store)
