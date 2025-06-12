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
