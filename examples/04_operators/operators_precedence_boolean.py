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
# to avoid confusion with operator precedence. The examples below
# are for educational purposes only and should not be used in production
# code.


a = not False and True or False     # a = ((not False) and True) or False
# 1      True and True or False
# 2               True or False
# 3               True
print(a)
# Output: True
