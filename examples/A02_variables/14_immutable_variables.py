# Immutable variables in Python
# ------------------------------------------------------------------------------
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
