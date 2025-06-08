# Example: Docstrings in a class

class TestClass(object):
    """ This is a docstring for the class


    Args:
        test (int): This is a docstring for the constructor argument

    Example:

        >>> test_class = TestClass(1)
        >>> test_class.test_function(1)
        'This is a test function with argument 1'

    """

    def __init__(self, test):
        """ This is a docstring for the constructor """
        self.test = test

    def test_function(self, test):
        """  This is a docstring for the function

        Args:
            test (int): This is a docstring for the function argument

        Raises:
            ValueError: If test is None

        Returns:
            str: A string with the argument

        """

        if test is None:
            raise ValueError("test cannot be None")

        return "This is a test function with argument {}".format(test)


print(TestClass.__doc__)
print(TestClass.test_function.__doc__)
