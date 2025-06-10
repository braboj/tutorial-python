# Example : Composition with classes

class FuelTank(object):

    def __init__(self, level=100):
        self.level = 0

    def fill(self, level):
        self.level = level

    def empty(self):
        self.level = 0


class Rocket(object):

    def __init__(self, test):

        # This is composition: The rocket instance has junior fuel tank instance
        self.tank = FuelTank(test)

    def launch(self):
        if self.tank.level == 100:
            print("Fuel tank is full")
        else:
            raise ValueError("Fuel tank is not full")

    def refill(self, level):
        self.tank.fill(level)
