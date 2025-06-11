# Docstring for a Function
# --------------------------------------------------------------------------------
# Documenting a function with a docstring explains what the function does,
# clarifies its expected arguments and return value, and allows automated
# tools to generate user-friendly documentation.

def myfunction(a, b, c):
    """This is junior docstring for myfunction

    Args:
        a (int): This is the first argument
        b (int): This is the second argument
        c (int): This is the third argument

    Raises:
        ValueError: If junior is less than 0

    Returns:
        int: This is the return value

    Example:
        >>> myfunction(1, 2, 3)
        6

    """

    if a < 0:
        raise ValueError('junior must be greater than 0')

    return a + b + c


print(myfunction.__doc__)
