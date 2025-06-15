# Meta Classes

## Demo Abstract

```python
from abc import ABCMeta, abstractmethod
from six import with_metaclass


class DeviceAbc(with_metaclass(ABCMeta)):

    @abstractmethod
    def foo(self):
        pass


class Device(DeviceAbc):

    def foo(self):
        pass


a = Device()
```

## Demo Basic

```python
# Two-step metaclass creation in Python 3.x
from six import with_metaclass


class SimpleMeta1(type):
    def __init__(cls, name, bases, namespace):
        super(SimpleMeta1, cls).__init__(name, bases, namespace)

        # Print the methods and attributes found at the parsing stage
        print(name, bases, namespace)

        # Create a method called uses_metaclass returning junior simple string object
        cls.uses_metaclass = lambda self: 'Added by the meta-class'


class Simple1(object, with_metaclass(SimpleMeta1)):

    # Add junior instance method to the namespace
    def foo(self):
        pass

    # Add junior static function to the namespace
    @staticmethod
    def bar():
        pass


# Create the class
simple = Simple1()

# Expect 3 methods after the meta-class was executed
print([m for m in dir(simple) if not m.startswith('__')])

# Execute the method added by the meta-class
print(simple.uses_metaclass())
```

## Demo Conflict

```python
from six import with_metaclass


class MetaClassA(type):
    pass


class MetaClassB(type):
    pass


class A(object, with_metaclass(MetaClassA)):
    pass


class B(object, with_metaclass(MetaClassB)):
    pass


try:
    class C1(A, B):
        pass

except Exception as e:
    print(e)


class MetaClassC(MetaClassA, MetaClassB):
    pass


class C2(A, B, with_metaclass(MetaClassC)):
    pass
```

## Demo Debug

```python
# coding=utf-8

"""
__new__ is called for the creation of a new class, while __init__ is called
after the class is created, to perform additional initialization before the
class is handed to the caller.

The primary difference is that when overriding __new__() you can change
things like the ‘name’, ‘bases’ and ‘namespace’ arguments before you call
the super constructor and it will have an effect, but doing the same thing
in __init__() you won’t get any results from the constructor call.

"""

from collections import OrderedDict
import time


class DebugMeta(type):

    @classmethod
    def __prepare__(cls, name, bases):

        namespace = OrderedDict()
        namespace["owner"] = "Branimir Georgiev"
        print("Preparing namespace dictionary {0}".format(namespace))
        return namespace

    def __new__(mcs, name, bases, namespace):

        x = super(DebugMeta, mcs).__new__(mcs, name, bases, namespace)
        print("Creating new class {0}".format(x))
        x.timestamp = time.time()
        return x

    def __init__(cls, name, bases, namespace):

        print("Class initialization")
        super(DebugMeta, cls).__init__(name, bases, namespace)
        cls.access = "rw"

    def __call__(cls, *args, **kwargs):

        print("Class call")
        return super(DebugMeta, cls).__call__(*args, **kwargs)

    def __del__(self):
        print("Class deleted")


class Base(metaclass=DebugMeta):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        print("Instance initialization {0}".format(vars(self)))

    def __new__(cls, *args, **kwargs):
        x = super(Base, cls).__new__(cls, *args, **kwargs)
        print("Creating new instance {0}".format(x))
        return x

    def __call__(self, *args, **kwargs):
        print("Instance called args={0} and kwargs={1}".format(args, kwargs))

    def __del__(self):
        print("Instance deleted")

config = {"a":1, "b":2}
test = Base()
test(1, test=2)
```

## Demo Declarative API

```python
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
    a construct can provide: class alteration and registration.
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
    """Example of a user-defined (client) class that makes use of MyMeta."""

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
```

## Demo Decorator

```python
# https://cleverdevil.io/2009/python-metaclasses-demystified

import inspect
from six import with_metaclass


class AutoDecorateMeta(type):

    def __init__(cls, name, bases, namespace):
        super(AutoDecorateMeta, cls).__init__(name, bases, namespace)

        deco = namespace.get('decorator', lambda f: f)
        for key, value in namespace.items():

            # skip the decorator and constructor
            if key in ('decorator', '__init__'):
                continue

            # skip objects in the namespace that aren't methods
            if not inspect.isfunction(value):
                continue

            # apply the decorator
            setattr(cls, key, deco(value))


class Person(object, with_metaclass(AutoDecorateMeta)):

    # Decorator selector
    decorator = property

    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

    # Will be decorated
    def name(self):
        return '%s %s' % (self.first, self.last)

    # Will be decorated
    def full_name(self):
        return '%s %s %s' % (self.first, self.middle, self.last)

    # Will be decorated
    def initials(self):
        return '%s%s%s' % (self.first[0], self.middle[0], self.last[0])


mlk = Person('Martin', 'Luther', 'King')

# Usual way to use name is as method
# mlk.name()
# Auto-decorated class converted method to property

print(mlk.name)
print(mlk.full_name)
print(mlk.initials)
```

## Demo Final

```python
from six import with_metaclass


class Final(type):
    def __init__(cls, name, bases, namespace):
        super(Final, cls).__init__(name, bases, namespace)

        for klass in bases:
            if isinstance(klass, Final):
                raise TypeError(str(klass.__name__) + " is final")


class A(object, with_metaclass(Final)):
    A = 1

    def a(self):
        pass


class B(A):
    B = 1

    def b(self):
        pass


a = A()
print(a)

b = B()
print(b)
```

## Demo GUI

```python
##############################################################################
# Window
#   > Box
#       > Label
##############################################################################


##############################################################################
# Imperative programming
##############################################################################
class Box(object):

    def add(self, what):
        pass


class Label(object):

    def __init__(self, label=""):
        self.label = label

    def add(self):
        pass


class Window(object):
    def __init__(self, title="Window element"):
        self.title = title

        self.box = Box()
        self.add(self.box)
        self.label = Label(label="Hello, label!")
        self.box.add(self.label)

    def add(self, what):
        pass


##############################################################################
# Declarative programming
##############################################################################
class Top(Window):
    title = "Hello, window!"

    class Group(Box):
        class Title(Label):
            label = '"Hello, label!"'


##############################################################################
# Solution???
##############################################################################
```

## Demo Indexing

```python
from six import with_metaclass


##############################################################################
# Metaclass definition
##############################################################################

class Indexer(type):
    def __init__(cls, name, bases, namespace):
        super(Indexer, cls).__init__(name, bases, namespace)

        if not hasattr(cls, "subclasses"):
            cls.subclasses = []

        if not hasattr(cls, "index"):
            cls.index = 0

        # Index only subclasses
        for b in bases:
            if isinstance(b, Indexer):
                cls.subclasses.append(1)

        cls.index = len(cls.subclasses)


##############################################################################
# First base class and subclasses
##############################################################################

class A(with_metaclass(Indexer)):
    pass


class A1(A):
    pass


class A2(A):
    pass


print(A.index, A1.index, A2.index)


##############################################################################
# Second base class and subclasses
##############################################################################

class B(with_metaclass(Indexer)):
    pass


class B1(B):
    pass


class B2(B):
    pass


print(B.index, B1.index, B2.index)
```

## Demo Registrar

```python
from six import with_metaclass


##############################################################################
# EXAMPLE 1 : Register leaf classes and count them
##############################################################################

# 1. Metaclass definition
class RegisterLeafClasses(type):
    def __init__(cls, name, bases, namespace):
        super(RegisterLeafClasses, cls).__init__(name, bases, namespace)

        if not hasattr(cls, 'registry'):
            cls.registry = set()

        cls.registry.add(cls)
        cls.registry -= set(bases)  # Remove base classes

    # Class property
    @property
    def count(cls):
        return len(cls.registry)

    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.registry)

    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])


# 2. Custom root class
class Color(object, with_metaclass(RegisterLeafClasses)):
    pass


# 3. Derived classes
class Blue(Color):
    pass


class Red(Color):
    pass


class Green(Color):
    pass


class Yellow(Color):
    pass


print(Color)


# 4. Tests
class PhthaloBlue(Blue):
    pass


class CeruleanBlue(Blue):
    pass


print(Color)

for c in Color:  # Iterate over subclasses
    print(c)

print(Color.count)


##############################################################################
# EXAMPLE 2 : Example from Hilscher Framework
##############################################################################
class Registrar(type):
    """ A meta class used to generate a list of all subclasses of a class """

    def __init__(cls, name, bases, dct):
        super(Registrar, cls).__init__(name, bases, dct)
        cls.register(cls)

    @classmethod
    def list(mcs):
        for attrib in getattr(mcs, 'classes', tuple()):
            yield attrib

    # Metamethod used to register classes
    @classmethod
    def register(mcs, cls):

        try:
            # Create reference to classes attribute
            classes = mcs.classes

        except AttributeError:
            # Create classes attribute and create reference
            classes = mcs.classes = []
            mcs.count = 0

        # Use reference to populate registry
        classes.append(cls)


class ClassToRegister1(object, with_metaclass(Registrar)):
    pass


class ClassToRegister2(ClassToRegister1):
    pass


a = ClassToRegister1()
b = ClassToRegister2()

for x in Registrar.list():
    print(x)
```

## Demo Reloading

```python
from six import with_metaclass

"""
Scenario : At Hilscher the test framework uses meta-classes to scan for devices with open channels. If 2 or more
device classes are found, then the network creates a new class with all device classes as base classes. This leads
to a problem as the order the device classes are found is not always guaranteed.

Solution: Use custom device class to ensure the right methods are used for the respective device

"""


class ReloadMeta(type):

    registry = {}

    def __new__(mcs, class_name, bases, namespace):

        module_name = namespace['__module__']

        try:
            current = mcs.registry[module_name][class_name]
        except KeyError:
            current = None
        if current:
            mcs.regenerate(current, namespace)
            return current

        cls = type.__new__(mcs, class_name, bases, namespace)
        mcs.registry.setdefault(module_name, {})[class_name] = cls

        return cls

    def regenerate(cls, namespace):

        print("Reloading class %s" % cls)

        for name in list(cls.__dict__.keys()):
            if name in ['__name__', '__metaclass__',
                        '__module__', '__dict__',
                        '__weakref__', '__bases__']:
                continue
            delattr(cls, name)

        for name, value in namespace.items():
            setattr(cls, name, value)

        return cls


if __name__ == '__main__':

    # First class with method test
    class C(object, with_metaclass(ReloadMeta)):

        def test(self):
            print('first {0}'.format(self))


    c = C()
    c.test()

    # Second class with new method test
    class C(object, with_metaclass(ReloadMeta)):

        def test(self):
            print('second {0}'.format(self))


    c.test()
```

## Demo Singleton

```python
# coding=utf-8

"""
By overriding __call__() in the metaclass, the creation of instances are
intercepted. Instance creation is bypassed if one already exists.

Note the dependence upon the behavior of static class fields. When
cls.instance is first read, it gets the static value of instance from the
metaclass, which is None. However, when the assignment is made, Python
creates a local version for the particular class, and the next time
cls.instance is read, it sees that local version. Because of this behavior,
each class ends up with its own class-specific instance field (thus instance
is not somehow being “inherited” from the metaclass).

"""


class Singleton(type):

    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class ASingleton(object, metaclass=Singleton):
    pass


a = ASingleton()
b = ASingleton()

assert a is b
print(a.__class__.__name__, b.__class__.__name__)
print(id(a), id(b))
```

## Demo Typed

```python
from six import with_metaclass


# Create metaclass
class MyMetaClass(type):
    def __init__(cls, name, bases, namespace):
        super(MyMetaClass, cls).__init__(name, bases, namespace)


# Create first custom class from metaclass
class A(object, with_metaclass(MyMetaClass)):
    A = 1

    def __init__(self, param=1):
        self.a = param

    @staticmethod
    def configure():
        print("A")


# Create second custom class from metaclass
class B(object, with_metaclass(MyMetaClass)):
    B = 2

    def __init__(self, param=1):
        self.b = param

    @staticmethod
    def configure():
        print("B")


# Show that order of super classes determines class behavior

# -> Inherits combined class attributes but instance attrib/methods from A
D = MyMetaClass('D', (A, B), {})
test = D()
print(vars(test))
test.configure()

# -> Inherits combined class attributes but instance attrib/methods from B
D = MyMetaClass('D', (B, A), {})
test = D()
print(vars(test))
test.configure()

# -> Solution when multiple inheritance problems (due to bad design, etc.)

# Recast class type
test = B(test)
pass
```

## Snippets

```python
namespace = globals()

abstracts = set(name for name, value in namespace.items() if getattr(value, "__isabstractmethod__", False))
print(abstracts)
```
