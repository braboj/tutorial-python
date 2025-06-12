# Composition: owned components live and die with the owner
# -----------------------------------------------------------------------------
# Composition means that an object is made up of other objects which it
# owns completely.  When the container is destroyed so are its parts.
# The `Rocket` creates and manages its own `FuelTank`, which does not exist
# independently.

class FuelTank(object):

    def __init__(self, level=100):
        # Start the tank with a given fuel level
        self.level = level

    def fill(self, level):
        self.level = level

    def empty(self):
        self.level = 0


class Rocket(object):

    def __init__(self, fuel_level):
        # This is composition: the Rocket creates and owns the FuelTank.
        # When the rocket is destroyed the tank goes with it.
        self.tank = FuelTank(fuel_level)

    def launch(self):
        if self.tank.level == 100:
            print("Fuel tank is full")
        else:
            raise ValueError("Fuel tank is not full")

    def refill(self, level):
        self.tank.fill(level)
