# Variables

## String Cases

```python
# String case manipulation .examples
# --------------------------------------------------------------------------------
# This code applies various string case manipulation methods in Python.

# Store the string to be manipulated
text = "AAAA bbbb"

print(text.upper())
# Output:
# AAAA BBBB

print(text.lower())
# Output:
# aaaa bbbb

print(text.title())
# Output:
# Aaaa Bbbb

print(text.capitalize())
# Output:
# Aaaa bbbb

print(text.swapcase())
# Output:
# aaaa BBBB
```

## String Concatenation

```python
# String concatenation example
# --------------------------------------------------------------------------------
# This code concatenates (joins) strings using the `+` operator. This
# technique is common when constructing messages or combining text from
# different sources.


string1 = 'Hello'
string2 = "World"
string3 = "!"

result = string1 + " " + string2 + string3
print(result)
# Output:
# Hello World!
```

## String Escaping

```python
# Escape sequences in Python strings
# --------------------------------------------------------------------------------
# This example uses escape sequences in strings so you can include
# characters that would otherwise be difficult or impossible to type
# directly.
#
# Special characters:
# - `\n` for new line
# - `\t` for tab
# - `\\` for backslash
# - `\'` for single quote
# - `\"` for double quote

print("Hello\nWorld")           # Print new line inside string
print("He said, \"Goodbye\"")   # Print double quotes inside string
# Output:
# Hello
# World
# He said, "Goodbye"
```

## String Indexing

```python
# String indexing
# --------------------------------------------------------------------------------
# This code accesses individual characters in a string by index. Strings are
# sequences of characters, so index 0 refers to the first character, and
# negative indices let you read characters from the end of the string.

string = "Hello, world!"

print(string[0])    # Print first character
# Output:
# H

print(string[1])    # Print second character
# Output:
# e

print(string[-1])   # Print last character
# Output:
# !
```

## String Interpolation

```python
# String interpolation
# --------------------------------------------------------------------------------
# This code uses f-strings (formatted string literals) to create strings
# that include variables. Expressions inside curly braces `{}` are
# evaluated in place.

first_name = "Branimir"
last_name = "Georgiev"
age = 25

print(f"My name is {first_name} {last_name} and I am {age} years old")
# Output:
# My name is Branimir Georgiev and I am 25 years old
```

## String Joining

```python
# String joining
# --------------------------------------------------------------------------------
# The `join()` method is a string method that takes an iterable (like a list)
# and concatenates its elements into a single string, with a specified separator
# between each element. If no separator is provided, it defaults to an empty
# string, effectively concatenating the elements without any characters in
# between.

tokens = '1 2 3 4 5 6 7 8 9'.split()
print(tokens)
# Output:
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

text = ''.join(tokens)
print(text)
# Output:
# 123456789

text = ' '.join(tokens)
print(text)
# Output:
# 1 2 3 4 5 6 7 8 9

text = ','.join(tokens)
print(text)
# Output:
# 1,2,3,4,5,6,7,8,9
```

## String Length

```python
# Calculate the length of a string
# --------------------------------------------------------------------------------
# This snippet calculates the number of characters in a string. The
# result differs from the byte length when the string contains UTF-8
# characters that use multiple bytes.

text = "0123456789"
print(len(text))
# Output:
# 10

text = 'Здравей!'
print(len(text))
# Output:
# 8
```

## String Slicing

```python
# String slicing
# --------------------------------------------------------------------------------
# This code slices strings in Python. Slicing extracts a portion of a string
# by specifying a start index, an end index, and an optional step using
# the syntax `string[start:end:step]`.
#
# The `start` index is inclusive, the `end` index is exclusive, and the `step`
# determines the increment between each index in the slice. The default values
# for `start` is 0, for `end` is the length of the string, and for `step` is 1.

text = "0123456789ABCDEF"

print(text[0:5])
# Output: 01234

print(text[7:])
# Output: 789ABCDEF

print(text[:5])
# Output: 01234

print(text[::2])
# Output: 02468ACE

print(text[::-1])
# Output: FEDCBA9876543210

print(text[1:10:2])
# Output: 13579
```

## String Splitting

```python
# Splitting Strings
# --------------------------------------------------------------------------------
# The `split()` method is used to split a string into a list of tokens based
# on a specified separator. If no separator is provided, it defaults to
# whitespace. The `splitlines()` method is used to split a string into a
# list of lines.


text = "1 2 3 4 5 6 7 8 9 10"
print(text.split())
# Output:
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


text = "1, 2, 3 4 5 6 7 8 9 10"
print(text.split(', '))
# Output:
# ['1', '2', '3 4 5 6 7 8 9 10']

text = """ First line
Second line
Third line
"""
print(text.splitlines())
# Output:
# [' First line', 'Second line', 'Third line']
```

## Var As Container

```python
# Variable as a container
# --------------------------------------------------------------------------------
# This code uses a variable as a container for data. The variable `text`
# stores a string value that can be reused multiple times, illustrating how
# variables allow you to store and manipulate data efficiently.

text = 'Hello world!'
print(text)
print(text)
print(text)
print(text)
print(text)
# Output:
# Hello world!
# Hello world!
# Hello world!
# Hello world!
# Hello world!
```

## Var Bool Type

```python
# Boolean variables
# --------------------------------------------------------------------------------
# This example uses boolean variables to represent truth values—either
# `True` or `False`. Such variables are often part of conditional
# statements and logical operations.

var = False
print(var)
# Output:
# False

var = True
print(var)
# Output:
# True
```

## Var Complex Sum

```python
# Complex numbers arithmetics
# --------------------------------------------------------------------------------
# The operator + can be used to add complex numbers in Python, similar to
# how it is used for integers and floats and is an example of operators
# overloading in Python. Complex numbers are represented as `a + bj`, where `a`
# is the real part and `b` is the imaginary part. The `j` suffix indicates
# the imaginary unit, which is equivalent to the square root of -1.

a = 1 + 1j
b = 1 + 1j
print(a + b)
# Output:
# (2+2j)
```

## Var Complex Type

```python
# Complex variables
# --------------------------------------------------------------------------------
# This code creates and manipulates complex numbers in Python. A complex
# number is written as `a + bj`, where `a` is the real part and `b` is the
# imaginary part.

z1 = 1 + 2j
z2 = 2 + 4j
print(z1, z2)
# Output:
# (1+2j) (2+4j)
```

## Var Dict Types

```python
# Dictionary types in Python
# --------------------------------------------------------------------------------
# This code creates and manipulates dictionaries in Python. A dictionary is
# a collection of key–value pairs where each key is unique. If a key
# appears more than once, the last assigned value is retained. The
# dictionary variable has the following properties:
#
# - Key access: You can access values using their keys
# - Unique keys: Each key must be unique within the dictionary
# - Mutable: Can be modified after creation
# - Ordered: The order of inserted items is maintained (as of Python 3.7)
# - Heterogeneous: Can contain keys and values of different types

# Key access
a = {'junior': 1, 'mid': 2, 'senior': 3}
print(a['mid'])
# Output: 2

# Unique keys
b = {'junior': 1, 'mid': 2, 'senior': 3, 'senior': 4}
print(b)
# Output: {'junior': 1, 'mid': 2, 'senior': 4}

# Mutable
c = {'junior':1, 'mid': 2}
c.update({'senior': 3})
print(c)
# Output: {'junior': 1, 'mid': 2, 'senior': 3}

# Ordered (as of Python 3.7)
d = {'mid': 2, 'senior': 3, 'junior': 1}
print(d)
# Output: {'mid': 2, 'junior': 1, 'senior': 3}

# Heterogeneous
e = {'junior': 1, 'mid': 2.5, 'senior': 'three'}
print(e)
# Output: {'junior': 1, 'mid': 2.5, 'senior': 'three'}
```

## Var Float Sum

```python
# Floating point numbers arithmetics
# --------------------------------------------------------------------------------
# The `+` operator can be used to add float numbers in Python, similar to how
# it is used for integers, strings and complex numbers (operators overloading).

# Standard format for float numbers
a = 1.0
b = 1.0
print(a + b)

# Scientific notation for float numbers
c = 1.0e1   # equivalent to 10.0 or 1* 10^1
d = 1.0e-1  # equivalent to 0.1 or 1* 10^-1
print(c + d)
```

## Var Float Type

```python
# Floating point numbers in Python
# --------------------------------------------------------------------------------
# Floating point numbers are used to represent real numbers and can be defined
# in standard decimal format or scientific notation.  Python's `float` type is
# based on the IEEE 754 double-precision floating-point format, which provides
# a wide range of values and precision.

float_1 = 1.0       # Standard format for float numbers
float_2 = 1.0e0     # Scientific notation for float numbers (equivalent to 1.0)

print(float_1)
# Output: 1.0

print(float_2)
# Output: 1.0
```

## Var Immutable

```python
# Immutable variables in Python
# --------------------------------------------------------------------------------
# Some variables in Python are immutable, meaning their value cannot be changed
# after they are created. This is in contrast to mutable variables, which can
# be modified after creation.
#
# For example, integer constants (also known as literals) are immutable in
# Python. When you create a constant, it has a unique identifier (id)
# that remains constant throughout the program's execution. Trying to reassign
# an immutable constant to a new value will result in a SyntaxError.

test = 1
print("Testing immutable constant 1 (int)")
print("ID of test   : {}".format(id(test)))
print("ID of 1      : {}".format(id(1)))
# Output:
# Testing immutable constant 1 (int)
# ID of test   : 140737488346112
# ID of 1      : 140737488346112

test = "A"
print("Testing immutable constant 'A' (str)")
print("ID of test   : {}".format(id(test)))
print("ID of 'A'    : {}".format(id("A")))
# Output:
# Testing immutable constant 'A' (str)
# ID of test   : 140737488346112
# ID of 'A'    : 140737488346112

# Trying to reassign an immutable constant will raise a SyntaxError
1 = 2
# Output:
# SyntaxError: cannot assign to literal ...
```

## Var Integer Type

```python
# Integer variable types in Python
# --------------------------------------------------------------------------------
# The integer type in Python is used to represent whole numbers, both
# positive and negative. Python supports various bases for integers,
# including decimal, binary, octal, and hexadecimal.

decimal_var = 10
print(decimal_var)
# Output: 10

binary_var = 0b1010
print(binary_var)
# Output: 10

octal_var = 0o12
print(octal_var)
# Output: 10

hexadecimal_var = 0x0A
print(hexadecimal_var)
# Output: 10
```

## Var List Type

```python
# List variables in Python
# --------------------------------------------------------------------------------
# The list type in Python is used to represent a collection of items. It is
# important to note that lists are passed by reference (see mutability in
# .examples). When you assign a list to another variable, both variables point
# to the same list in memory. This means that changes made to one variable
# will affect the other variable as well. To create a copy of a list, you can
# use the `copy()` method or the slicing (e.g. `a = b[:]`). The list has the
# following properties:
#
# - Indexed: Elements can be accessed by their index
# - Mutable: Can be modified after creation
# - Ordered: Order of elements is preserved
# - Heterogeneous: Can contain elements of different types

# Indexed
a = [1, 2, 3]
print(a[0])
# Output: 1

# Mutable
b = [1, 2, 3]
b[0] = 4
print(b)
# Output: [4, 2, 3]

# Ordered
c = [2, 1, 3]
print(c)
# Output: [2, 1, 3]

# Heterogeneous
d = [1, 'two', 3.0]
print(d)
# Output: [1, 'two', 3.0]

# (!) Passing by reference (!)
l1 = [1, 2, 3]
l2 = l1
l2[0] = 4
print(l1, l2)
# Output: [4, 2, 3]

# Copying a list
l3 = l1.copy()
l3[0] = 5
print(l1, l3)
# Output: [4, 2, 3] [5, 2, 3]
```

## Var Mutable

```python
# Mutable variables in Python
# --------------------------------------------------------------------------------
# Some variables in Python are mutable, meaning their value can be changed after
# they are created allowing you to dynamic modification of their contents. The
# most common mutable variable types in Python are lists, dictionaries, and
# sets.
#
# In Python mutable variables are passed by reference, meaning that if you
# assign a mutable variable to another variable, both variables will refer to
# the same object in memory. This is a source of confusion for many a
# Python developers, as it can lead to unexpected behavior.

# Create a mutable variable (list)
test = [1, 2, 3, 4]
print("ID: {}".format(id(test)))
# Output:
# ID: 140123456789456

# Modify the mutable variable and prove that it is still the same object
test.append(5)
print("ID: {}".format(id(test)))
# Output:
# ID: 140123456789456

# An assignment to another variable will create a reference to the same object
reference = test
print("ID: {}".format(id(reference)))
# Output:
# ID: 140123456789456
```

## Var None Type

```python
# None type in Python
# --------------------------------------------------------------------------------
# The None type in Python is used to show that the variable is not assigned
# any value. It is useful when you want to indicate that a variable is
# intentionally left empty or when a function does not return a value, e.g.
# the `print` function.

a = None
print(a)
# Output: None

# The print function returns None
print(print())
# Output: None
```

## Var Reason

```python
# Reason of having variables in Python
# --------------------------------------------------------------------------------
# This example explains why variables are useful. Without them we would
# repeat the same value throughout the code and update each occurrence
# manually. Imagine printing "Hello world" 1000 times and later wanting
# to change it to "Hello Python"—we would need to edit every place it was
# written.

print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
# Output: Hello world
```

## Var Set Type

```python
# Set type in Python
# --------------------------------------------------------------------------------
# The set type in Python is a collection of elements with unique values. It
# used to remove duplicates from a collection and to perform set operations like
# union, intersection, and difference. The set type has the following
# characteristics:
#
# - Unique: A set cannot contain duplicate elements.
# - Mutable: You can add or remove elements from a set.
# - Unordered: The elements in a set do not have a specific order.
# - Heterogeneous: A set can contain elements of different data types.
# - Unindexed: You cannot access elements in a set by index

# Passing by reference
s1 = {1, 2, 3}
s2 = s1
s2.add(4)
print(s1, s2)
# Output: {1, 2, 3, 4} {1, 2, 3, 4}

# Copying a set
s3 = s1.copy()
s3.add(5)
print(s1, s3)

# All elements are unique
a = {1, 1, 2, 2, 3, 3}
print(id(a), a, sep=": ")
# Output: {1, 2, 3}

# Mutable: You can add and remove elements
a.add(4)
print(id(a), a, sep=": ")
# Output: {1, 2, 3, 4}

# Unordered: The order of elements is not guaranteed
b = {3, 1, 2}
print(id(b), b, sep=": ")
# Output: {1, 2, 3}

# Heterogeneous: A set can contain elements of different data types
c = {1, "two", 3.0, (4, 5)}
print(id(c), c, sep=": ")
# Output: {1, 'two', 3.0, (4, 5)}

# Unindexed: You cannot access elements by index
d = {1, 2, 3}
print(d[0])
# Output: TypeError: 'set' object is not subscriptable
```

## Var String Type

```python
# String type in Python
# --------------------------------------------------------------------------------
# String variables in Python can be defined using single or double quotes.
# Both types of quotes are valid and can be used interchangeably. The string
# has the following characteristics:
#
# - Immutable: Once created, the string cannot be changed.
# - Ordered: The characters in the string maintain their order.
# - Indexed: Each character in the string can be accessed by its index.
# - Homogeneous: All characters in the string are of the same type.

# Immutable (a change creates a new object)
string1 = "Hello, world!"
string2 = string1.replace("world", "Python")
print(id(string1), id(string2))

# Ordered (characters maintain their order)
string3 = "Python"
print(list(string3))
# Output: ['P', 'y', 't', 'h', 'o', 'n']

# Indexed (characters can be accessed by index)
string4 = "Hello, world!"
print(string4[0])
# Output: 'H'

# Homogeneous (all characters are of the same type)
string5 = "Python" + 3
# Output: TypeError: can only concatenate str (not "int") to str
```

## Var Tuple Type

```python
# Tuple type in Python
# --------------------------------------------------------------------------------
# A tuple is very similar to a list that is immutable, meaning it cannot be
# changed after creation. Their main advantage is the memory efficiency
# and performance benefits they provide over lists, especially when dealing
# with large datasets. They also can be used as keys in dictionaries.
#
# - Immutable: Once created, the string cannot be changed.
# - Ordered: The characters in the string maintain their order.
# - Indexed: Each character in the string can be accessed by its index.
# - Heterogeneous: Strings can contain characters of different types

# Immutable (a change creates a new object)
tuple1 = (1, 2, 3)
tuple2 = tuple1 + (4, 5)
print(id(tuple1), id(tuple2))

# Ordered (characters maintain their order)
tuple3 = (1, 2, 3)
print(list(tuple3))
# Output: [1, 2, 3]

# Indexed (characters can be accessed by index)
tuple4 = (3, 2, 1)
print(tuple4[0])
# Output: 3

# Heterogeneous (can contain different types)
tuple5 = (1, "two", 3.0, True)
print(tuple5)
# Output: (1, 'two', 3.0, True)
```

## Var Types

```python
# Get the type of a variable
# --------------------------------------------------------------------------------
# Python offers a way to inspect the type of a variable using `type()`. Type
# is a special class in Python that servers many purposes, including
# determining the type of a variable. When invoked on a variable, it returns
# the type of that variable, which can be useful for troubleshooting or understanding
# the data being worked with.

var = 100
print(var, type(var))
# Output: 100 <class 'int'>

var = 100.0
print(var, type(var))
# Output: 100.0 <class 'float'>
```
