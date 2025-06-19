# Annotations for Python Functions
# --------------------------------------------------------------------------------
# Annotations in Python functions allow you to specify the expected types of
# parameters and the return type of the function. This can help with code
# readability and static type checking.
#
# There are no strict rules enforced by Python regarding these A13_type_hints,
# but they serve as a guide for developers and can be used by tools like
# type checkers, IDEs, and documentation 01_generators.

def add(x: int, y: int) -> int:
    return x + y
