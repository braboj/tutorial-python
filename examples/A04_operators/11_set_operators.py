# Set Operators in Python
# ------------------------------------------------------------------------------
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
