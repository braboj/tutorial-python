"""
The bin() method converts and returns the binary equivalent string of a given integer. If the parameter isn't an
integer, it has to implement __index__() method to return an integer.

"""

number = 5
print('The binary equivalent of 5 is:', bin(number))


class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


print('The binary equivalent of quantity is:', bin(Quantity()))