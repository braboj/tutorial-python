# Dunder Methods

## Demo Iterator

```python
# Dunder methods and iteration
# ---------------------------------------------------------------------------
# Demonstrates how special methods customize iteration behavior.
# * An iterable implements __iter__ returning an iterator.
# * An iterator implements __iter__ returning itself and __next__ returning
#   the next element.
# https://www.pythontutorial.net/advanced-python/python-iterator-vs-iterable/


##################################################################################################
# ITERABLE CLASS
##################################################################################################

class Colors(object):
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __iter__(self):
        return ColorIterator(self)


##################################################################################################
# ITERATOR CLASS
##################################################################################################

class ColorIterator(object):
    def __init__(self, colors):
        self.__colors = colors
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.next()

    def next(self):
        try:
            color = self.__colors.rgb[self.__index]
            self.__index += 1
        except IndexError:
            raise StopIteration

        return color


##################################################################################################
# DEMO
##################################################################################################

c = Colors()
print(c)

c_iter = iter(c)
print(c_iter)

for element in c:
    print(element)
```

## Dunder Arithmetic Operators

```python
# Dunder methods for arithmetic operators
# ---------------------------------------------------------------------------
# By defining special arithmetic methods, objects can participate in Python's
# numeric operations. These dunder hooks let a class customize how instances
# respond to +, -, *, and other operators.

class Complex(object):

    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __add__(self, other):
        return Complex(
            real=self.real + other.real,
            imag=self.imag + other.imag
        )

    def __sub__(self, other):
        return Complex(
            real=self.real - other.real,
            imag=self.imag - other.imag
        )

    def __mul__(self, other):
        return Complex(
            real=self.real * other.real,
            imag=self.imag * other.imag
        )

    def __divmod__(self, other):
        return Complex(
            real=self.real % other.real,
            imag=self.imag % other.imag
        )

    def __truediv__(self, other):
        return Complex(
            real=self.real / other.real,
            imag=self.imag / other.imag
        )

    def __floordiv__(self, other):
        return Complex(
            real=self.real // other.real,
            imag=self.imag // other.imag
        )


a = Complex(1, 2)
b = Complex(3, 4)

z = a + b
print(z.real, z.imag)
```

## Dunder Attributes

```python
# Dunder methods for attribute access
# ---------------------------------------------------------------------------
# Attribute related dunder methods such as __getattr__, __setattr__ and
# __delattr__ give objects dynamic control over attribute access. They enable
# customized lookup, assignment and deletion behavior.

class Complex(object):

    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __setattr__(self, key, value):
        print("Setting attribute: {} = {}".format(key, value))

    def __delattr__(self, item):
        print("Deleting attribute: {}".format(item))

    def __getattr__(self, item):
        print("Getting attribute: {}".format(item))
        return item

z = Complex(1, 2)
setattr(z, "real", 3)
delattr(z, "real")
print(getattr(z, "real"))
```

## Dunder Builtin Types

```python
# Dunder methods for object representation
# ---------------------------------------------------------------------------
# Built-in type conversion functions like bool(), int() and bytes() call
# corresponding dunder methods on objects. Implementing these hooks lets a
# class define how it converts to fundamental Python types.

import struct
import math


class Point(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.__length = self._calc_length()

    def _calc_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return bool(self.x or self.y)

    def __int__(self):
        return int(self._calc_length())

    def __float__(self):
        return float(self._calc_length())

    def __complex__(self):
        return complex(self.x, self.y)

    def __bytes__(self):
        return bytes(int(self.__length))


c = Point(1, 2)
print("Point({}, {})".format(c.x, c.y))
print("bool(c)    : {}".format(bool(c)))
print("int(c)     : {}".format(int(c)))
print("float(c)   : {}".format(float(c)))
print("complex(c) : {}".format(complex(c)))
print("bytes(c)   : {}".format(bytes(c)))
```

## Dunder Context Manager

```python
# Dunder methods for context manager
# ---------------------------------------------------------------------------
# The __enter__ and __exit__ methods allow an object to define its own
# setup and teardown logic when used in a with-statement. This example shows
# how implementing these hooks customizes resource management behavior.

class Complex(object):

    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __enter__(self):
        print(">>> Inside __enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(">>> Inside __exit__")
        print(" Execution type:", exc_type)
        print(" Execution value:", exc_val)
        print(" Traceback:", exc_tb)

        if exc_type is not None:
            print("\nException occurred")
            return True
        else:
            print("\nNo exception occurred")
            return False


with Complex(1, 0) as c:
    print(">>> Inside with block")
    print(c.real, c.imag)
    print(c.real / 0)
```

## Dunder Customize Behavior

```python
# Dunder methods for customizing object behavior
# ---------------------------------------------------------------------------
# This script demonstrates several special methods that hook into object
# creation, calling and destruction. Implementing these dunder methods lets a
# class take control over how instances are created, invoked and cleaned up.

class TestClass(object):

    def __init__(self):
        print("I'm initialized!")
        self.name = "DunderClass"

    def __new__(cls, *args, **kwargs):
        print("I'm created!")
        return super(TestClass, cls).__new__(cls)

    def __call__(self, *args, **kwargs):
        print("I'm called! My name is {}".format(self.name))

    def __del__(self):
        print("I'm deleted!")


# Create and initialize an instance of DunderClass
test = TestClass()

# Call the instance
test()

# Delete the instance
del test
```

## Dunder Iterator Protocol

```python
# Dunder methods for the iterator protocol
# ---------------------------------------------------------------------------
# Special (dunder) methods allow objects to integrate with Python features.
# By implementing __iter__ and __next__, this class customizes iteration
# behavior so that instances work seamlessly in for-loops and other iterable
# contexts.

class Stack(object):

    def __init__(self):
        self._items = []
        self._index = -1

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("Pop from an empty stack")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_item = self._items[self._index]
            self._index -= 1
            return next_item

        except IndexError:
            raise StopIteration


s = Stack()
s.push(1)
s.push(2)
s.push(3)

for item in s:
    print(item)
```

## Dunder Object Representation

```python
# Dunder methods for object representation
# ---------------------------------------------------------------------------
# Special representation methods like __repr__ and __str__ let objects control
# how they are displayed. This example highlights how these hooks customize the
# string and byte output of a class.

import struct


class Point(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __format__(self, format_spec):
        fmt = "({:" + format_spec + "} + {:" + format_spec + "})"
        fmt = fmt.format(self.x, self.y)
        return fmt

    def __hash__(self):
        return hash((self.x, self.y))

    def __bytes__(self):
        result = []
        for item in (self.x, self.y):
            result.extend(struct.pack("!f", item))

        return bytes(result)


p = Point(1, 2)
print(hash(p))
print(repr(p))
print(str(p))
print("{:.3f}".format(p))
print(bytes(p))
```

## Dunder Operator Overloading

```python
# Dunder methods for operator overloading
# ---------------------------------------------------------------------------
# Overloading arithmetic operators with dunder methods allows custom classes
# to behave like built-in numeric types. The following Point class defines
# how instances react to +, -, * and other operations.

class Point(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Point(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Point(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        return Point(
            x=self.x * other.x,
            y=self.y * other.y
        )

    def __divmod__(self, other):
        return Point(
            x=self.x % other.x,
            y=self.y % other.y
        )

    def __truediv__(self, other):
        return Point(
            x=self.x / other.x,
            y=self.y / other.y
        )

    def __floordiv__(self, other):
        return Point(
            x=self.x // other.x,
            y=self.y // other.y
        )


a = Point(1, 2)
b = Point(3, 4)

z = a + b
print(z.x, z.y)
```

## Snippets

```python
# Demonstration of special methods
# ---------------------------------------------------------------------------
# Various dunder methods show how objects integrate with Python features

class DunderClass(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        pass
    # ---------------------------------------------------------------------------------------------
    # - Context manager
    # ---------------------------------------------------------------------------------------------

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Iterator protocol
    # ---------------------------------------------------------------------------------------------

    def __iter__(self):
        pass

    def __next__(self):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Class decorators
    # ---------------------------------------------------------------------------------------------

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        pass

    def __getattr__(self, item):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Class representation
    # ---------------------------------------------------------------------------------------------

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __bytes__(self):
        pass

    def __sizeof__(self):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Overload comparison operators
    # ---------------------------------------------------------------------------------------------

    def __eq__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Overload arithmetic operators
    # ---------------------------------------------------------------------------------------------
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass
```
