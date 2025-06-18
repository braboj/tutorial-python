# Boolean Operators in Python
# --------------------------------------------------------------------------------
# Boolean operators evaluate expressions to produce a boolean value, meaning
# either `True` or `False`.
#
# oolean operators include `not`, `and`, and `or`, and their precedence
# determines the order in which they are evaluated. The precedence order is:
#
# 1. `not`
# 2. `and`
# 3. `or`
#
# !!! WARNING !!!
# Please always use parentheses to make the code more readable and
# to avoid confusion with operator precedence. The examples below
# are for educational purposes only and should not be used in production
# code.

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

# Precedence of operators
a = not False and True or False     # a = ((not False) and True) or False
# 1      True and True or False
# 2               True or False
# 3               True
print(a)
# Output: True
