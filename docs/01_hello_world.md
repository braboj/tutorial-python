# Hello World

## Expressions

```python
# Use expressions to evaluate values in Python.
# --------------------------------------------------------------------------------
# An expression is anything that evaluates to a value. The following is true
# for all expressions:
#
#  - An expression always returns a value.
#  - Expressions can be used in statements (e.g. if, while, for).
#  - Expressions can be part of other expressions.

1                       # Simple expression
1 + 2 + 3               # Arithmetic expression
```

## Hello World

```python
# Hello World
# --------------------------------------------------------------------------------
# This simple program prints "Hello world!" and performs a basic
# addition (1 + 1) to highlight Python's core syntax.

print("Hello world!")
print(1 + 1)
```

## Modules

```python
# Use import to access python modules
# --------------------------------------------------------------------------------
# A module is a file containing Python code. It can define functions,
# classes, and variables that you can use in your code. You can import a
# module using the `import` statement.

import math
from math import pi

print(math.pi)
print(pi)
```

## Print Statement

```python
# Use the print() function to output text to the console.
# --------------------------------------------------------------------------------
# The print() function is used to output data to the screen. It can take
# multiple arguments and will convert them to strings before printing them.

# By default, print() ends with a newline character.
print("Hello")
print("World")
# Output:
#   Hello
#   World

# You can change this behavior by specifying the end parameter.
print("Hello", end="")
print("World", end="")
# Output:
#   HelloWorld

# A print statement with no arguments prints a newline character.
print("Hello", end="")
print()
print("World", end="")
# Output:
#   Hello
#   World

# You can also specify the separator symbol
print("Hello", "World", sep="")
print("Hello", "World", sep=" ")
print("Hello", "World", sep=", ")
# Output:
#   HelloWorld
#   Hello World
#   Hello, World
```

## Statements

```python
# Use statements to perform actions in Python.
# --------------------------------------------------------------------------------
# A statement is a piece of code that performs an action. It can be as simple
# as a single line or a more complex block of code. The following is true
# for all statements:
#
#  - A statement does not return a value.
#  - Statements cannot be used in expressions (e.g. if, while, for).
#  - It is a standalone operation.

# Valid statements
x = 5
print(x)

# Invalid statements
# if (x = 5):  # SyntaxError (statement cannot be used in an expression)
```

## Zen Of Python

```python
# Import the `this` module to print the Zen of Python
# --------------------------------------------------------------------------------
# This is a fun Easter egg in Python that prints the Zen of Python, the
# guiding principles for writing computer programs in Python. It emphasizes
# simplicity, readability, and the importance of explicitness in code design.

import this

# Output:
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
```
