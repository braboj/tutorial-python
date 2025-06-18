# Operators

## Operators Arithmetic

```python
# Arithmetic Operators in Python
# --------------------------------------------------------------------------------
# Arithmetic operators are used to perform mathematical operations on
# numeric values. In Python, these operators include addition, subtraction,
# multiplication, division, floor division, modulus, and exponentiation.

a, b = 3, 2

# Addition
print(a+b)
# Output: 6

# Subtraction
print(a-b)
# Output: 1

# Multiplication
print(a*b)
# Output: 6

# Division (floating point division)
print(a/b)
# Output: 1.5

# Floor Division (integer division)
print(a//b)
# Output: 1

# Modulus (remainder)
print(a % b)
# Output: 1

# Exponentiation (a to the power of b)
print(a**b)
# Output: 9
```

## Operators Assignment

```python
# Assignment Operators
# --------------------------------------------------------------------------------
# Assignment operators are used to assign values to variables and can also
# perform operations on those values.
#
# For example, the `+=` operator adds a value to a variable and assigns the
# result back to that variable. The same applies to each of the other
# arithmetic and bitwise operators (e.g., `-=`, `*=`, `/=`, `&=`, `|=`, etc.).

a = 10
b = 15

# Assign
test = a
print(test)
# Output: 10

# Add and Assign
test += b
print(test)
# Output: 25 (same as test = test + b)
```

## Operators Bitwise

```python
# Bitwise Operators in Python
# --------------------------------------------------------------------------------
# Bitwise operators are used to perform bit-level operations on integers. These
# operators directly manipulate the binary representations of numbers. Each bit
# is calculated independently, based on the truth table of the operation.
#
# Truth table: & (AND)
# | A | B | A & B |
# |---|---|-------|
# | 0 | 0 |   0   |
# | 0 | 1 |   0   |
# | 1 | 0 |   0   |
# | 1 | 1 |   1   |

# Example:
#   0xAA  = 10101010 (binary)
#   0x55  = 01010101 (binary)
#   0xAA & 0x55 = 00000000 (binary)

# Initialize variables
a, b = 0xAA, 0x55

# Performs a binary AND operation between corresponding bits of a and b
print(hex(a & b))
# 0x00

# Performs a binary OR operation between corresponding bits of a and b
print(hex(a | b))
# 0xFF

# Performs a binary XOR operation between corresponding bits of a and b
print(hex(a ^ b))
# 0xFF

# Inverts all the bits of a (1's complement)
print(hex(~a))
# -0xAB

# Shifts the bits the left by 1 position, filling with 0 on the right
print(hex(a << 1))
# 0x154

# Shifts the bits the right by 1 position, discarding bits on the right
print(hex(a >> 1))
# 0x55
```

## Operators Comparison

```python
# Comparison Operators in Python
# --------------------------------------------------------------------------------
# Comparison operators are used to compare two values. They return a boolean
# value (True or False) based on the comparison.

# Initialize variables
a, b = 10, 20

# Equal
print(a == b)
# Output: False

# Not equal
print(a != b)
# Output: True

# Greater than
print(a > b)
# Output: False

# Less than
print(a < b)
# Output: True

# Greater than or equal to
print(a >= b)
# Output: False

# Less than or equal to
print(a <= b)
# Output: True
```

## Operators Conditional

```python
# Conditional Expressions in Python
# --------------------------------------------------------------------------------
# Conditional expressions allow you to evaluate a condition and return one
# of two values based on the result of the condition.
#
# Syntax: [value_if_true] if [condition] else [value_if_false]



a, b = 10, 20

# Find the minimum of two numbers using a conditional expression
result = a if a < b else b
print(result)
# Output: 10
```

## Operators Dict

```python
# Merging and updating dictionaries
# --------------------------------------------------------------------------------
# Python 3.9 introduced the | and |= operators to combine dictionaries. The | 
# operator creates a new dictionary containing keys from both operands, while
# |= updates the dictionary on the left in place. This provides a concise
# alternative to using the update() method or ** unpacking for merging.

a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5}

# Merging two dictionaries using the | operator
c = a | b
print(c)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Updating a dictionary with another using the |= operator
a |= b
print(a)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

## Operators Identity

```python
# Identity Operators in Python
# --------------------------------------------------------------------------------
# Identity operators are used to compare the memory locations of two objects.
# If two variables point to the same object in memory, they are considered
# identical.

a, b, c = 10, 20, 10

print(a is b)
# Output: False

print(a is not b)
# Output: True

print(a is c)
# Output: True
```

## Operators List

```python
# Common list operators in Python
# --------------------------------------------------------------------------------
# This file contains .examples of the most commonly used operators on lists,
# including indexing, slicing, concatenation, repetition, and membership tests.

my_list = [1, 2, 3, 4, 5]

# Indexing
print(my_list[0])   # Access the first element
print(my_list[-1])  # Access the last element

# Slicing
print(my_list[1:4]) # Get a sublist from index 1 to 3
print(my_list[:3])  # Get the first three elements

# Concatenation
new_list = my_list + [6, 7, 8]
print(new_list)  # Combine two lists

# Repetition
repeated_list = my_list * 2
print(repeated_list)  # Repeat the list twice

# Membership test
print(3 in my_list)  # Check if 3 is in the list
print(10 not in my_list)  # Check if 10 is not in the list
```

## Operators Logical

```python
# Logical Operators in Python
# --------------------------------------------------------------------------------
# Logical operators are used to combine conditional statements. They allow you
# to evaluate multiple conditions and return a boolean value (True or False)
# based on the evaluation.

a, b = 10, 20

# AND
print(a < 100 and b > 15)
# Output: True

# OR
print(a < 100 or b > 100)
# Output: True

# NOT
print(not(a < 100 and b > 15))
# Output: False
```

## Operators Membership

```python
# Membership Operators in Python
# --------------------------------------------------------------------------------
# Membership operators are used to test whether a value is a member of a
# sequence (e.g., a list, tuple, or string).

a, b = 1, 5
test_list = [1, 2, 3]

# in
print(a in test_list)

# not in
print(b not in test_list)
```

## Operators Precedence Boolean

```python
# Explore the precedence of boolean operators
# --------------------------------------------------------------------------------
# Boolean operators include `not`, `and`, and `or`, and their precedence
# determines the order in which they are evaluated. The precedence order is:
#
# 1. `not`
# 2. `and`
# 3. `or`
#
# !!! WARNING !!!
# Please always use parentheses to make the code more readable and
# to avoid confusion with operator precedence. The .examples below
# are for educational purposes only and should not be used in production
# code.


a = not False and True or False     # a = ((not False) and True) or False
# 1      True and True or False
# 2               True or False
# 3               True
print(a)
# Output: True
```

## Operators Precedence Math

```python
# Mathematical Operator Precedence in Python
# --------------------------------------------------------------------------------
# Mathematical operators include addition, subtraction, multiplication, and
# division, and their precedence determines the order in which they are e
# valuated.
#
# The precedence of mathematical operators in Python is as follows:
# 1. Parentheses
# 2. Exponentiation (**)
# 3. Multiplication (*), Division (/), and Modulus (%)
# 4. Addition (+) and Subtraction (-)
#
# !!! WARNING !!!
# The precedence of operators can lead to unexpected results if not
# understood correctly. Avoid using complex expressions without parentheses
# to ensure clarity and correctness, especially in production code.

a = 2 + 3 - 4/5  # a = 2 + 3 - (4/5)
print(a)
# Output: 4.2
```

## Operators Precedence Parantheses

```python
# Parentheses to control operator precedence
# --------------------------------------------------------------------------------
# The parentheses in Python can be used to control the precedence of
# operators in expressions.

a = 2 + 2**3
b = (2 + 2)**3

print(a)
# Output: 10

print(b)
# Output: 64
```

## Operators Set

```python
# Set Operators in Python
# --------------------------------------------------------------------------------
# Demonstrates fundamental set operations including union, intersection,
# difference, symmetric difference, and subset/superset checks.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_union = set1 | set2
print("Union:", set_union)  # Output: {1, 2, 3, 4, 5}

# Intersection
set_intersection = set1 & set2
print("Intersection:", set_intersection)  # Output: {3}

# Difference
set_difference = set1 - set2
print("Difference:", set_difference)  # Output: {1, 2}

# Symmetric Difference
set_symmetric_difference = set1 ^ set2
print("Symmetric Difference:", set_symmetric_difference)  # Output: {1, 2, 4, 5}

# Subset
set3 = {1, 2}
set4 = {1, 2, 3, 4, 5}
is_subset = set3 <= set4
print("Is set3 a subset of set4?", is_subset)  # Output: True

# Superset
is_superset = set4 >= set3
print("Is set4 a superset of set3?", is_superset)  # Output: True

# Proper subset
is_proper_subset = set3 < set4
print("Is set3 a proper subset of set4?", is_proper_subset)  # Output: True

# Proper superset
is_proper_superset = set4 > set3
print("Is set4 a proper superset of set3?", is_proper_superset)  # Output: True

# Disjoint
set5 = {6, 7}
is_disjoint = set1.isdisjoint(set5)
print("Are set1 and set5 disjoint?", is_disjoint)  # Output: True
```

## Operators Tuples

```python
# Tuple Operators in Python
# --------------------------------------------------------------------------------
# This example demonstrates common tuple operations including indexing,
# slicing, concatenation, repetition, and membership tests.

my_tuple = (1, 2, 3, 4, 5)

# Indexing
print(my_tuple[0])   # Output: 1
print(my_tuple[-1])  # Output: 5

# Slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Concatenation
print(my_tuple + (6, 7))  # Output: (1, 2, 3, 4, 5, 6, 7)

# Repetition
print(my_tuple * 2)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Membership
print(3 in my_tuple)  # Output: True
print(9 in my_tuple)  # Output: False
```
