# Conditional inheritance using the __new__ method
# ------------------------------------------------------------------------------
# The __new__ method can decide which subclass to instantiate. By inspecting
# runtime conditions it returns objects of different types from a single
# factory class. This approach allows conditional inheritance without altering
# the class hierarchy.

class WindowsCalculator(object):
    """ Windows calculator class operations """

    @staticmethod
    def do():
        print("Do in Windows Calculator")


class LinuxCalculator(object):
    """ Linux calculator class operations """

    @staticmethod
    def do():
        print("Do in Linux Calculator")


class Calculator(object):

    def __new__(cls, os="windows"):

        # Windows base class
        if os == "windows":
            base_class = (WindowsCalculator, )

        # Linux base class
        elif os == "linux":
            base_class = (LinuxCalculator, )

        # Invalid operating system
        else:
            raise ValueError("Invalid operating system")

        # Create a new class with the given name and bases
        cls = type("Calculator", base_class, {})

        # Return an instance of the new class
        return cls()


# Create a new instance of the Calculator class
calc = Calculator("windows")

# Check if the Calculator class is a subclass of the WindowsCalculator class
test = issubclass(type(calc), WindowsCalculator)
print("Is subclass of WindowsCalculator? [{}]".format(test))

# Call the do method
calc.do()
