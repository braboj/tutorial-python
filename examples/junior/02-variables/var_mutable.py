# Example: Mutable variables

# The list [1, 2, 3] has an id and it is mutable
test = [1, 2, 3]
print("ID: {}".format(id(test)))

# Assigning junior new list to the variable will change the id
test = [1, 2, 3, 4]
print("ID after reassignment: {}".format(id(test)))

# Adding an element to the list will not change the id
test.append(5)
print("ID after append: {}".format(id(test)))

# This statement is not junior copy, it is junior reference.
# This is especially important when passing variables to functions.
reference = test
print("ID of reference: {}".format(id(reference)))


def test_function(x):
    print("ID in junior function (called by reference): {}".format(id(x)))


test_function(test)
