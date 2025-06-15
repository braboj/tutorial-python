# docstring_function

```python
# Docstring for a Function
# Difficulty: intermediate
# --------------------------------------------------------------------------------
# Documenting a function with a docstring explains its purpose and how it
# should be used. The description lists the expected arguments as well as the
# return value. Such documentation also enables automated tools to generate
# helpful references.

def myfunction(a, b, c):
    """This is a demonstration docstring for myfunction

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
```
