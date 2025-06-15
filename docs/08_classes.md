# Classes

## Class Abstract Properties

```python
# Stacking decorators
# --------------------------------------------------------------------------------
# Multiple decorators can be stacked on a single attribute. In this file a
# property is defined using @property together with @abstractmethod. Derived
# classes must supply the concrete implementation for this decorated property.

from abc import ABCMeta, abstractmethod
from six import with_metaclass


class DeviceAbc(with_metaclass(ABCMeta)):
    """Example abstract class

    Usage:

        # Optional
        @property, @staticmethod, @classmethod

        +

        # Obligatory decorator
        @abstractmethod

    Example:

        # Defines and abstract property
        @property
        @abstractmethod
        def prop(self):
            ...

    """

    def __init__(self):
        self._bar = "bar"

    @property
    @abstractmethod
    def bar(self):
        pass

    @abstractmethod
    def foo(self):
        pass


class Samsung(DeviceAbc):

    @property
    def bar(self):
        return self._bar

    def foo(self):
        print('foo')


test = Samsung()
print(test.bar)
test.foo()
```

## Class Abstract Python2

```python
# Abstract class using the six library for python 2
# --------------------------------------------------------------------------------
# The six library helps define abstract base classes that remain compatible with
# Python 2. The metaclass provided by six works with decorators such as
# @abstractmethod so subclasses must implement the required methods.

from six import with_metaclass
from abc import ABCMeta, abstractmethod


class CalculatorAbc(with_metaclass(ABCMeta)):

    def __init__(self, mode="basic"):
        self.mode = mode

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def subtract(self, *args, **kwargs):
        raise NotImplementedError


class Calculator(CalculatorAbc):

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(calc.add(1, 2))
print(calc.mode)
```

## Class Abstract Python3

```python
# Abstract class in python 3+
# --------------------------------------------------------------------------------
# Python 3 provides native support for abstract base classes. The ABC and
# abstractmethod decorators ensure that child classes implement required
# behavior. Instances cannot be created until the abstract methods are
# overridden.

from abc import ABC, abstractmethod


class CalculatorAbc(ABC):

    def __init__(self, mode="basic"):
        self.mode = mode

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def subtract(self, *args, **kwargs):
        raise NotImplementedError


class Calculator(CalculatorAbc):

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(calc.add(1, 2))
print(calc.mode)
```

## Class As Blueprint

```python
# Class as template
# --------------------------------------------------------------------------------
# A class can act as a template from which many objects are built. This file
# defines a Person blueprint containing attributes and methods that every
# instance will share.

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is {} and my age is {}".format(self.name, self.age))
```

## Class As Concrete Object

```python
# Object as concrete realization of a class
# --------------------------------------------------------------------------------
# The code creates an instance of the Person class as a tangible object.
# The constructor assigns initial values to the instance. After creation, the
# object can call its methods and access stored data.
from class_as_blueprint import Person


John = Person("John", 32)
John.say_hello()
```

## Class Constructor Conditional Inheritance

```python
# Conditional inheritance using the __new__ method
# --------------------------------------------------------------------------------
# The __new__ method can decide which subclass to instantiate. By inspecting
# runtime conditions it returns objects of different types from a single
# factory class. This approach allows conditional inheritance without altering
# the class hierarchy.

class WindowsCalculator(object):
    """ Windows calculator class operations """

    @staticmethod
    def do():
        print("Do in Windows Calculator")


class LinuxCalculator(object):
    """ Linux calculator class operations """

    @staticmethod
    def do():
        print("Do in Linux Calculator")


class Calculator(object):

    def __new__(cls, os="windows"):

        # Windows base class
        if os == "windows":
            parents = (WindowsCalculator, )

        # Linux base class
        elif os == "linux":
            parents = (LinuxCalculator, )

        # Invalid operating system
        else:
            raise ValueError("Invalid operating system")

        # Create a new class with the given name and bases
        cls = type("Calculator", parents, {})

        # Return an instance of the new class
        return cls()


# Create a new instance of the Calculator class
calc = Calculator("windows")

# Check if the Calculator class is a subclass of the WindowsCalculator class
test = issubclass(type(calc), WindowsCalculator)
print("Is subclass of WindowsCalculator? [{}]".format(test))

# Call the do method
calc.do()
```

## Class Constructor Factory

```python
# Class factory using the __new__ method
# --------------------------------------------------------------------------------
# Overriding __new__ allows a class to act as a factory. The method returns an
# instance of a specific subclass based on the provided parameters. This
# separates the decision about which object to create from the calling code.

class WindowsCalculator(object):

    @staticmethod
    def do():
        print("Do in Windows Calculator")


class LinuxCalculator(object):

    @staticmethod
    def do():
        print("Do in Linux Calculator")


class Calculator(object):

    def __new__(cls, os="windows"):

        # An instance of the WindowsCalculator class is returned
        if os == "windows":
            return object.__new__(WindowsCalculator)

        # An instance of the LinuxCalculator class is returned
        elif os == "linux":
            return object.__new__(LinuxCalculator)

        # Invalid operating system
        else:
            raise ValueError("Invalid operating system")


# Create a new instance of the Calculator class
calc = Calculator("windows")

# Check if the Calculator class is an instance of the WindowsCalculator class
test = isinstance(calc, WindowsCalculator)
print("Is instance of WindowsCalculator? [{}]".format(test))

# Call the do method
calc.do()
```

## Class Constructor Singleton

```python
# Singleton using the __new__ method
# --------------------------------------------------------------------------------
# By overriding __new__, this class ensures that only one instance ever exists.
# The method stores the created object and returns it on subsequent calls.
# Such control over object creation implements the singleton pattern.

class Singleton(object):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("Creating singleton...")
            cls.__instance = object.__new__(cls)

        else:
            print("Singleton already exists...")

        return cls.__instance


s1 = Singleton()
s2 = Singleton()
print(s1 == s2)
print(s1 is s2)
```

## Class Constructors

```python
# How __new__ and __init__ cooperate in object creation
# --------------------------------------------------------------------------------
# Object creation begins with __new__, which allocates the instance. The fresh
# object is then passed to __init__ for further initialization. Separating these
# steps gives developers flexibility to customize how objects come into
# existence.

class Calculator(object):

    def __new__(cls):

        # Use the parent class to create the object
        obj = object.__new__(cls)

        # Return the object
        print("__new__ : Created object {}".format(obj))
        return obj

    def __init__(self):

        # Self is the object that was created by __new__
        print("__init__: Using object {}".format(self))

        # Add attributes to the object
        self.name = "Cool Calculator"


calc = Calculator()
print(calc.name)
```

## Class Create With Type

```python
# Using ``type`` to inspect objects and create classes
# --------------------------------------------------------------------------------
# The built-in ``type`` function performs two unrelated tasks. When passed a
# single object it returns that object's class, which can be handy for
# inspection. When given a name, base classes and attributes it creates a new
# class dynamically, allowing programs to define types at runtime.

##############################################################################
# USECASE A : Get object type
##############################################################################
numbers_list = [1, 2]
print(type(numbers_list))

numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))


##############################################################################
# USECASE B : Create class with base classes, attributes and methods
##############################################################################

def init(self, name):
    self.name = name


def say_hallo_b(self):
    return "Hi, my name is " + self.name


Robot2 = type("Robot2",
              (),
              {"counter": 0,
               "__init__": init,
               "func": lambda self: "Hi, I am " + self.name,
               "say_hello_b": say_hallo_b
               }
)


x = Robot2("Marvin")
print(x.name)
print(x.func())
print(x.say_hello_b())
```

## Class Decorator For Classes

```python
# Class as a decorator for a class
# --------------------------------------------------------------------------------
# A class can implement the __call__ method and be applied as a decorator to
# another class. When used this way it may attach attributes or modify the
# decorated class at definition time.
class Counter(object):

    # The constructor accepts the parameter passed to the decorator
    def __init__(self, start_value):
        self.counter = start_value

    # The __call__ method is called when the class is used as a decorator
    def __call__(self, cls):

        # Modify the class by adding an attribute with the specified value
        cls.counter = self.counter

        # Return the modified class
        return cls


# Apply the class decorator with a parameter
@Counter(start_value=1)
class DecoratedClass(object):
    pass


# Use the explicit decorator syntax
DecoratedClass = Counter(start_value=1)(DecoratedClass)
obj = DecoratedClass()
print(obj.counter)  # Output: 1


# Use Python's decorator syntax
obj = DecoratedClass()
print(obj.counter)  # Output: Custom Value
```

## Class Decorator For Functions

```python
# Class as a decorator for functions and methods
# --------------------------------------------------------------------------------
# Defining the __call__ method allows a class to wrap functions or methods.
# The decorator can maintain state between invocations and perform actions
# before or after calling the original function.


class Counter(object):

    def __init__(self, init_value=0):
        """ Initialize counter."""
        self._counter = init_value

    def __call__(self, function):
        """ Wrapping call to original function. """

        def wrapper(*args, **kwargs):
            """ Wrapper function."""
            try:
                self._counter += 1
                print("{}".format(self._counter))
                return function(*args, **kwargs)

            except Exception as e:
                print(e)

        return wrapper


def f():
    print("Hello World")


@Counter(0)
def g():
    print("Hello World")


print("#" * 80)

# Use the explicit decorator syntax
f = Counter(0)(f)

# Call the decorated functions
for _ in range(10):
    f()

print("#" * 80)

# Use Python's decorator syntax
for _ in range(10):
    g()
```

## Class Init State

```python
# Initialization with the __init__ method
# --------------------------------------------------------------------------------
# The __init__ method runs immediately after an object is created. It assigns
# the initial values for the instance and prepares it for use.

class Person(object):

    def __init__(self, name="Branimir", age=40):
        self.name = name
        self.age = age

        print("My name is {0} and I am {1} years old".format(self.name, self.age))


p1 = Person()
p2 = Person("John", 30)
```

## Class Init Steps

```python
# Initialization in multiple steps
# --------------------------------------------------------------------------------
# Some objects gather their initial data through a sequence of operations. This
# file breaks the process into helper methods that collect the values one by
# one. Each step can perform validation before returning its result.

class Person(object):
    def __init__(self):
        self.name = self.step_1()
        self.age = self.step_2()

    @staticmethod
    def step_1():
        name = input("Step 1: Enter the person's name: ")
        return name

    @staticmethod
    def step_2():
        age = input("Step 2: Enter the person's age: ")
        return age


john = Person()
print(john.name, john.age)
```

## Class Init Validate

```python
# Initialization and validation
# --------------------------------------------------------------------------------
# Initialization may involve checking that provided values meet certain rules.
# The constructor validates input before assigning it to attributes. Invalid
# data is rejected to keep the object's state consistent.

class Person(object):

        def __init__(self, name, age):
            self.name = name
            self.age = age

            if not isinstance(self.name, str):
                raise TypeError("Name must be a string")

            if not isinstance(self.age, int):
                raise TypeError("Age must be an integer")

            if self.age < 0:
                raise ValueError("Age must be a positive integer")

        def say_hello(self):
            print("Hello, my name is {} and my age is {}".format(self.name, self.age))


john = Person("John", 32)
john.say_hello()
```

## Class Instance

```python
# Class instance with concrete values
# --------------------------------------------------------------------------------
# After defining the Person class, an instance is created with explicit values.
# The object stores these attributes as part of its state. Accessing them later
# confirms that the information persists on the instance.

class Person(object):

    def __init__(self):
        print("Person has ID {}".format(id(self)))


# The person object has a unique id
p1 = Person()
p2 = Person()
```

## Class Instance Attributes

```python
# Define and access instance attributes
# --------------------------------------------------------------------------------
# Instance attributes are defined in the __init__ method. They store data
# unique to each object and can be accessed through the instance of the class.
# Each instance may hold different values for these attributes.

class Person(object):

    def __init__(self):
        self.name = "Branimir"
        self.age = 40


# Create the instance
p = Person()

# Access to the instance attributes
print(p.name)
print(p.age)
```

## Class Instance Methods

```python
# Class instance with instance methods
# --------------------------------------------------------------------------------
# Instance methods operate on a particular object and have access to its state.
# They typically receive the instance as the first parameter. Calling these
# methods affects only the object that invoked them.

class Person(object):

    def do_something(self):
        print("{} is doing something".format(self))

    def do_something_with(self, something, someone):
        print("{} is doing {} with {}".format(self, something, someone))


# Create the instance
p = Person()
p.do_something()
p.do_something_with("nothing", "no one")
```

## Class Method Create Instance

```python
# Class method used to create instances
# --------------------------------------------------------------------------------
# A class method can serve as an alternative constructor. It receives the class
# as the first argument and builds a new instance from provided data. This
# approach collects creation logic in one place.

class Person(object):

    NAME_PREFIX = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, name):
        return cls(name)


p = Person.from_string("John")
print(p.name)
```

## Class Method Modify Instances

```python
# Class method used to modify existing instances of the class
# --------------------------------------------------------------------------------
# Class methods can operate on a collection of instances maintained by the
# class. The method updates every stored object in a single call. Centralizing
# the logic keeps modifications consistent across all instances.

class Person(object):

    NAME_PREFIX = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_prefix(cls, prefix):
        cls.NAME_PREFIX = prefix

    @classmethod
    def add_prefix(cls, person):
        person.name = "{} {}".format(cls.NAME_PREFIX, person.name)


p = Person("John")
Person.set_prefix("Dr.")
Person.add_prefix(p)
print(p.name)
```

## Class Method Modify Itself

```python
# Class method used to modify the class itself
# --------------------------------------------------------------------------------
# Because class methods receive the class as the first argument, they can change
# class-level attributes. This file modifies a shared value that affects all
# future instances.

class Person(object):

    NAME_PREFIX = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_prefix(cls, prefix):
        cls.NAME_PREFIX = prefix


p = Person("John")
Person.set_prefix("Dr.")
print(p.NAME_PREFIX)
```

## Class Mixin

```python
# Mixin class
# --------------------------------------------------------------------------------
# A mixin provides extra methods that can be shared across multiple unrelated
# classes. It relies on cooperative multiple inheritance to join its behavior
# with that of the main class hierarchy.

class RemoteMixin(object):

    def __init__(self, brand=None, volume=0, *args, **kwargs):

        # This syntax is required in order to guarantee that the MRO is not broken
        super(RemoteMixin, self).__init__(*args, **kwargs)

        # Mixin specific attributes
        self.brand = brand
        self.volume = volume

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        self.volume -= 1

    def status(self):
        print("Brand: {}".format(self.brand))
        print("Volume: {}".format(self.volume))


class JvcRemote(RemoteMixin, object):
    """ Mixins should be always inherited first """

    def __init__(self):
        super(JvcRemote, self).__init__(brand="JVC", volume=10)

    def status(self):
        super(JvcRemote, self).status()

    @staticmethod
    def learn():
        print("Learn button")


class SonyRemote(RemoteMixin, object):
    """ Mixins should be always inherited first """

    def __init__(self):
        super(SonyRemote, self).__init__(brand="Sony", volume=5)

    @staticmethod
    def home():
        print("Home button")


remote = JvcRemote()
actions = ["volume_up", "status", "volume_down", "status", "learn", "status"]
for action in actions:
    print("Action: {}".format(action))
    func = getattr(remote, action)
    func()

print("\n")

remote = SonyRemote()
actions = ["volume_up", "status", "volume_down", "status", "home", "status"]
for action in actions:
    print("Action: {}".format(action))
    func = getattr(remote, action)
    func()
```

## Class Mro Bottom First

```python
# Mro (method resolution order) - bottom first
# --------------------------------------------------------------------------------
# In this layout the interpreter begins searching for methods in the most
# derived class and moves upward through the hierarchy. The arrangement helps
# clarify how attribute lookup progresses when multiple parents define the same
# name.

class A(object):

    @staticmethod
    def process():
        print('A.process()')


class B(object):
    @staticmethod
    def process():
        print('B.process()')


class C(A, B):

    @staticmethod
    def process():
        print('C.process()')


obj = C()
obj.process()
print(C.mro())
```

## Class Mro Complex

```python
# Mro (method resolution order) - combined bottom first and left first
# --------------------------------------------------------------------------------
# Python resolves method names by considering both the depth of the inheritance
# tree and the order in which bases are listed. This file sets up a hierarchy
# that makes the combined bottom-first and left-first rules apparent.

class A(object):
    @staticmethod
    def process():
        print("A.process()")


class B(object):
    @staticmethod
    def process():
        print("B.process()")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
print(D.mro())
d.process()
```

## Class Mro Diamond

```python
# Mro (method resolution order) - diamond problem
# --------------------------------------------------------------------------------
# A diamond inheritance pattern occurs when two classes share a common base
# class. The method resolution order ensures that the base is initialized only
# once. The classes here are organized so that each path to the base is
# considered without duplication.

class A(object):
    @staticmethod
    def process():
        print("A.process()")


class B(A):
    @staticmethod
    def process():
        print("B.process()")


class C(A):
    @staticmethod
    def process():
        print("C.process()")


class D(B, C):
    pass


d = D()
print(D.mro())
d.process()
```

## Class Mro Left First

```python
# Mro (method resolution order) - left first
# --------------------------------------------------------------------------------
# With multiple inheritance Python consults base classes from left to right. The
# hierarchy in this file highlights how that ordering affects method lookup.

class A(object):

    @staticmethod
    def process():
        print('A.process()')


class B(object):
    @staticmethod
    def process():
        print('B.process()')


class C(A, B):
    pass


class D(B, A):
    pass


# The method process is searched for until the first class having the method is found (here A)
test = C()
print(C.mro())
test.process()

# The method process is searched for until the first class having the method is found (here B)
test = D()
print(D.mro())
test.process()
```

## Class Mro Unresolved

```python
# Mro (method resolution order) - unresolved
# --------------------------------------------------------------------------------
# Some inheritance graphs produce conflicting search orders that Python cannot
# resolve. This file sets up such a conflict and triggers an error when the
# interpreter tries to build the method resolution order. Understanding this
# failure helps diagnose complex inheritance issues.

class Player(object):
    pass


class Enemy(Player):
    pass


class GameObject(Player, Enemy):
    pass


# Explanation (see MRO rules in the documentation):
#
# - MRO is GameObject -> Player -> Enemy -> Player (not monotonic as Player appears twice)
# - Rule 2 says Enemy should appear before Player
# - Rule 3 says Player should appear before Enemy
#
# Rules 2 and 3 are in conflict, so the MRO algorithm cannot be applied. This is called an
# "unresolvable inheritance graph" and Python will raise an exception in this case.

g = GameObject()
print(GameObject.mro())
```

## Class Multiple Inheritance

```python
# Multiple inheritance
# --------------------------------------------------------------------------------
# A single class may inherit behavior from several parents. Combining features
# this way can reduce duplication but requires careful design to avoid
# conflicts.

class A(object):

    @staticmethod
    def process():
        print("Class A is processing... ")


class B(object):

    @staticmethod
    def process():
        print("Class B is processing... ")


class C(A, B):
    pass


class D(B, A):
    pass


# The method process is searched for until the first class having the method is found (here A)
test = C()
test.process()

# The method process is searched for until the first class having the method is found (here B)
test = D()
test.process()
```

## Class Named Constructor Different Params

```python
# Named constructors as alternative constructors
# --------------------------------------------------------------------------------
# A class can offer several named constructors for convenience. Each one accepts
# parameters tailored for a specific situation and returns a configured
# instance.

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_diagonal(cls, x1, y1, x2, y2):
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return cls(width, height)


# Create a square using the default constructor
rect1 = Rectangle(1, 1)
print(rect1.width, rect1.height)

# Create the same square using the named constructor
rect2 = Rectangle.from_diagonal(1, 1, 2, 2)
print(rect2.width, rect2.height)
```

## Class Named Constructor Init Sources

```python
# Different sources to create and initialize objects
# --------------------------------------------------------------------------------
# Objects may be constructed from data stored in several locations such as
# files or environment variables. Named constructors gather that information and
# return fully initialized instances.
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
```

## Class Named Constructor Reduce Params

```python
# Reduce the number of parameters
# --------------------------------------------------------------------------------
# When an initializer requires many arguments, a named constructor can provide a
# simpler interface. It bundles related values together before delegating to
# __init__.

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size):
        return cls(size, size)


# Create a square using the default constructor
square1 = Rectangle(1, 1)
print(square1.width, square1.height)

# Create the same square using the named constructor
square2 = Rectangle.square(size=1)
print(square2.width, square2.height)
```

## Class Named Constructor Representation

```python
# Different internal representations of the same object
# --------------------------------------------------------------------------------
# A class may provide alternate constructors that store data in various formats.
# Each representation exposes the same behavior to callers. Selecting one or
# another depends on the needs of the application.

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    @staticmethod
    def from_csv(data):
        name = data[0]
        age = data[1]
        return Person(name=name, age=age)


# Mock data
json_data = {'name': 'mayank', 'age': 27}
csv_data = [('mayank', 27), ]

person = Person.from_json(json_data)
print(person.name, person.age)

person = Person.from_csv(csv_data[0])
print(person.name, person.age)
```

## Class Nested

```python
# Nested classes for constants, settings, etc.
# --------------------------------------------------------------------------------
# Classes can contain other classes that serve as containers for related
# constants or configuration. Nesting keeps these auxiliary definitions close to
# the code that uses them.

class Settings:

    LANG = "English"
    THEME = "Light"
    IP_ADDR = "192.168.210.10"
    PORT = 8080

    class AdvancedSettings:

        ENABLE_LOGGING = False
        MAX_CONNECTIONS = 10

    class ExperimentalSettings:

        ENABLE_NEW_FEATURE = False


# Access the basic settings
print(Settings.THEME)

# Access the b settings
print(Settings.AdvancedSettings.ENABLE_LOGGING)  # Output: False

# Access the experimental settings
print(Settings.ExperimentalSettings.ENABLE_NEW_FEATURE)  # Output: False
```

## Class Properties

```python
# Property used to encapsulate an instance variable
# --------------------------------------------------------------------------------
# The property decorator exposes getter and setter functions as attribute
# access. This allows validation or computation while keeping the public
# interface simple.

class Person(object):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self.__name = value


p = Person("John")
print(p.name)
```

## Class Single Inheritance

```python
# Multilevel inheritance
# --------------------------------------------------------------------------------
# Multilevel inheritance arranges classes in a linear hierarchy. Each
# subsequent class extends the one above it, accumulating behavior down the
# chain.

class A(object):

    @staticmethod
    def process():
        print("Root is processing... ")


class B(A):
    pass


class C(B):
    pass


# The method process is searched for until the first class having the method is found (here A)
test = C()
test.process()
```

## Class Static Methods

```python
# Static method are not bound to the class and can be used as utility functions
# --------------------------------------------------------------------------------
# Static methods operate without reference to a particular instance or class.
# They behave like regular functions that happen to live in the class's
# namespace and are often used for related utility tasks.

class Packet(object):

    def __init__(self, ip_addr='192.168.10.1', mask="255.255.255.0", payload=()):
        self.payload = payload
        self.ip_addr = ip_addr
        self.mask = mask

    @staticmethod
    def dot_to_bytes(val):
        return bytes(map(int, val.split('.')))

    @staticmethod
    def bytes_to_dot(val):
        return '.'.join(map(str, val))


# Convert IP address in dot notation to bytes
addr_bytes = Packet.dot_to_bytes('192.168.1.1')
print(addr_bytes)

# Convert bytes to IP address in dot notation
addr_dot = Packet.bytes_to_dot(addr_bytes)
print(addr_dot)
```

## Class Structure

```python
# Class structure
# --------------------------------------------------------------------------------
# This file outlines common elements found in many classes such as attributes,
# static methods and constructors. Organizing these pieces consistently makes
# new classes easier to understand and maintain.

class ClassStructure(object):

    CLASS_VARIABLE = "Hi, I am "

    def __new__(cls, *args, **kwargs):
        print("This is the constructor method")
        return object.__new__(cls)

    def __init__(self):
        print("This is the initialization method")
        self.instance_variable = "John"

    @classmethod
    def class_method(cls):
        print("This is a class method, the class prefix is: {}".format(cls.class_variable))

    @staticmethod
    def static_method():
        print("This is a static method, the class prefix is: {}".format(ClassStructure.class_variable))

    def instance_method(self):
        print("This is an instance method, `{} {}`".format(self.class_variable, self.instance_variable))
```

## Class Superclass Attributes

```python
# Call super class method and access super class attributes
# --------------------------------------------------------------------------------
# Subclasses can call methods defined on their parent and access inherited
# attributes. Using ``super`` keeps the code maintainable when the hierarchy
# changes.

class Person(object):

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, id_number):
        super(Employee, self).__init__(name)
        self.id_number = id_number


e = Employee("John", 1234)
print(e.name)
print(e.id_number)
```

## Class Superclass Constructor

```python
# Call __new__ method of super class
# --------------------------------------------------------------------------------
# A subclass can override __new__ while still delegating part of the creation
# process to its parent. Calling the superclass method ensures base attributes
# are initialized correctly.

class Person(object):

    def __new__(cls, name):
        return super(Person, cls).__new__(cls)

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __new__(cls, name, id_number):
        return super(Employee, cls).__new__(cls, name)

    def __init__(self, name, id_number):
        super(Employee, self).__init__(name)
        self.id_number = id_number


e = Employee("John", 1234)
print(e.name)
print(e.id_number)
```

## Class Superclass Methods

```python
# Call super class methods
# --------------------------------------------------------------------------------
# Methods in a subclass can extend behavior defined in a parent. By calling the
# superclass implementation first, the subclass adds functionality without
# rewriting the original logic.

class Person(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Employee(Person):

    def __init__(self, name, id_number):
        super(Employee, self).__init__(name)
        self.id_number = id_number

    def get_id_number(self):
        return self.id_number


e = Employee("John", 1234)
print(e.get_name())
print(e.get_id_number())
```

## Class Variables

```python
# Working with class attributes
# --------------------------------------------------------------------------------
# Class attributes are shared across all instances of a class. They store values
# that should remain consistent, such as prefixes used by each Person object.

class Person(object):

    # Class attributes are defined outside of any method and are shared by all instances
    MALE_PREFIX = "Mr."
    FEMALE_PREFIX = "Ms."

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def get_prefix(self):
        """Return the appropriate prefix using class attributes."""

        # The person is male
        if self.sex == "male":
            prefix = self.MALE_PREFIX

        # The person is female
        elif self.sex == "female":
            prefix = self.FEMALE_PREFIX

        # Others
        else:
            prefix = ""

        return prefix

    def get_name(self):
        """ Return the name with the appropriate prefix """
        return "{} {}".format(self.get_prefix(), self.name)


# Create the instances
males = [Person(name="Branimir", sex="male"), Person("Dimitar", sex="male")]

# Class attributes are accessible from the instance methods
print("Default prefix...")
for male in males:
    print(male.get_name())

# Class attributes are accessible from the class itself and a change will affect all instances
print("Prefix changed...")
Person.MALE_PREFIX = "Sir"
for male in males:
    print(male.get_name())
```

## Class Variables Pitfalls

```python
# Class Variables Pitfalls
# --------------------------------------------------------------------------------
# Sharing state at the class level can introduce subtle bugs when instances
# modify that state. This section discusses common mistakes and how to avoid
# them.
"""Class vs. Instance Variables
--------------------------------
Class variables are shared by all instances, while instance variables belong
to each object. Assigning to ``self.variable`` creates an instance attribute.
If a class attribute with the same name exists, the instance attribute hides it
and later reads through ``self`` return the instance value. Mixing them can be
confusing because updates seem to apply only to some objects.

When you read ``self.value`` and ``value`` is not defined on the instance,
Python falls back to the class attribute:

    class A:
        value = 1

    obj = A()
    print(obj.value)  # 1 from the class

Any assignment using ``self`` stores a value on the instance:

    obj.value = 2
    print(A.value)   # 1
    print(obj.value) # 2

Here ``obj.value`` now shadows ``A.value``. To access the class attribute
explicitly you must use ``A.value``.
"""


class TestOp(object):

    immutable = 1
    mutable = [1, ]


class Test(TestOp):

    def __init__(self):
        super(Test, self).__init__()

    def test_immutable(self):

        print("#" * 80)
        print("Testing immutable class variable")
        print("#" * 80)

        # self references to the class variable
        print("")
        print("Read value through class name and then self...")

        print("CLS  => {0}:{1}".format(id(TestOp.immutable), TestOp.immutable))
        print("SELF => {0}:{1}".format(id(self.immutable), self.immutable))

        # self creates and references an instance variable (shadows the class variable)
        print("")
        print("Change immutable type using self...")

        self.immutable = 2
        print("CLS  => {0}:{1}".format(id(TestOp.immutable), TestOp.immutable))
        print("SELF => {0}:{1}".format(id(self.immutable), self.immutable))

        # Changing the value of immutable class variable will create a new object
        print("")
        print("Change the value of the class immutable variable...")

        TestOp.immutable = 3
        print("CLS  => {0}:{1}".format(id(TestOp.immutable), TestOp.immutable))
        print("SELF => {0}:{1}".format(id(self.immutable), self.immutable))

        print("")

    def test_mutable(self):
        print("#" * 80)
        print("Testing mutable class variable")
        print("#" * 80)

        # self references to the class variable
        print("")
        print("Read value through class name and then self...")

        print("CLS  => {0}:{1}".format(id(TestOp.mutable), TestOp.mutable))
        print("SELF => {0}:{1}".format(id(self.mutable), self.mutable))

        # self creates and references an instance variable (shadows the class variable)
        print("")
        print("Change mutable type using self...")

        self.mutable.append(2)
        print("CLS  => {0}:{1}".format(id(TestOp.mutable), TestOp.mutable))
        print("SELF => {0}:{1}".format(id(self.mutable), self.mutable))

        # self
        print("")
        print("Change the value of the class mutable variable...")

        TestOp.mutable.append(3)
        print("CLS  => {0}:{1}".format(id(TestOp.mutable), TestOp.mutable))
        print("SELF => {0}:{1}".format(id(self.mutable), self.mutable))

        print("")


if __name__ == "__main__":

    test = Test()

    test.test_mutable()
    print("Final value of immutable class variable is {0}:{1}\n".format(id(Test.immutable), Test.immutable))

    test.test_immutable()
    print("Final value of mutable class variable is {0}:{1}\n".format(id(Test.mutable), Test.mutable))
```
