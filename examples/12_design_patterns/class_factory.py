# Class factory using the __new__ method
# --------------------------------------------------------------------------------
# Overriding __new__ allows a class to act as a factory. The method returns an
# instance of a specific subclass based on the provided parameters. This
# separates the decision about which object to create from the calling code.

class WindowsCalculator(object):

    @staticmethod
    def do():
        print("Do in Windows Calculator")


class LinuxCalculator(object):

    @staticmethod
    def do():
        print("Do in Linux Calculator")


class Calculator(object):

    def __new__(cls, os="windows"):

        # An instance of the WindowsCalculator class is returned
        if os == "windows":
            return object.__new__(WindowsCalculator)

        # An instance of the LinuxCalculator class is returned
        elif os == "linux":
            return object.__new__(LinuxCalculator)

        # Invalid operating system
        else:
            raise ValueError("Invalid operating system")


# Create a new instance of the Calculator class
calc = Calculator("windows")

# Check if the Calculator class is an instance of the WindowsCalculator class
test = isinstance(calc, WindowsCalculator)
print("Is instance of WindowsCalculator? [{}]".format(test))

# Call the do method
calc.do()
