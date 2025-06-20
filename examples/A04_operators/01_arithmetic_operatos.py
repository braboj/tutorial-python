# Arithmetic Operators in Python
# ------------------------------------------------------------------------------
# Arithmetic operators are used to perform mathematical operations on
# numeric values. In Python, these operators include addition, subtraction,
# multiplication, division, floor division, modulus, and exponentiation.
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

# Operator Precedence
a = 2 + 3 - 4/5  # a = 2 + 3 - (4/5)
print(a)
# Output: 4.2
