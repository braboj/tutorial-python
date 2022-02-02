from collections import namedtuple

"""
def namedtuple(typename, field_names, verbose=False, rename=False)
"""

# Normal usecase
Point = namedtuple(
    typename="Point",
    field_names=["x", "y", "z"],
)

p = Point(1, 2, 3)
print(p)

# Use rename to rename fields which are reserved by Python
Point = namedtuple(
    typename="Point",
    field_names=["and", "or", "not"],
    verbose=False,
    rename=True
)

p = Point(1, 2, 3)
print(p)

# Print the created class
Point = namedtuple(
    typename="Point",
    field_names=["x", "y", "z"],
    verbose=True,
)

# p = Point(1, 2, 3)
# print(p)
