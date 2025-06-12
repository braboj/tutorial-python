# Function annotations for parameters and return values
# --------------------------------------------------------------------------------
# Annotations in Python functions allow you to specify the expected types of
# parameters and the return type of the function. This can help with code
# readability and static type checking.
#
# There are no strict rules enforced by Python regarding these annotations,
# but they serve as a guide for developers and can be used by tools like
# type checkers, IDEs, and documentation generators.

def add(x: int, y: int) -> int:
    return x + y
