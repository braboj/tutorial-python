def myfunction(a, b, c):
    """This is a docstring for myfunction

    Args:
        a (int): This is the first argument
        b (int): This is the second argument
        c (int): This is the third argument

    Raises:
        ValueError: If a is less than 0

    Returns:
        int: This is the return value

    Example:
        >>> myfunction(1, 2, 3)
        6

    """

    if a < 0:
        raise ValueError('a must be greater than 0')

    return a + b + c


print(myfunction.__doc__)
