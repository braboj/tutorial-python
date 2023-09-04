# Example: Association Relationships

class Math(object):

    @staticmethod
    def add(a, b):
        return a + b


class Battery(object):

    def __init__(self, model):
        self.model = model

    def charge(self):
        print("Battery {} charging".format(self.model))

    def discharge(self):
        print("Battery {} discharging".format(self.model))


class FourLineDisplay(object):

    def __init__(self, model):
        self.model = model

    def display(self):
        print("Display {} displaying".format(self.model))

    def turn_off(self):
        print("Display {} turning off".format(self.model))

    def turn_on(self):
        print("Display {} turning on".format(self.model))


class Calculator(object):

    def __init__(self, display):
        self.display = display
        self.battery = Battery("default")

    def add(self, a, b):
        # Association relationship
        result = Math.add(a, b)
        return result

    def replace_battery(self, battery):
        self.battery = battery


calc = Calculator(display=FourLineDisplay(model="EL-W506T"))
calc.add(1, 1)
