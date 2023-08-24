# Abstraction demo using composition

# Mixin class for logging functionality
class LoggingMixin(object):
    def log_info(self, message):
        print("[INFO] {}".format(message))

    def log_warning(self, message):
        print("[WARNING] {}".format(message))

    def log_error(self, message):
        print("[ERROR] {}".format(message))


# Sample classes using the LoggingMixin
class Vehicle(object):
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle, LoggingMixin):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)
        self.model = model

    def drive(self):
        self.log_info("{} {} is driving.".format(self.brand, self.model))


class Motorcycle(Vehicle, LoggingMixin):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)
        self.model = model

    def drive(self):
        self.log_info("{} {} is driving.".format(self.brand, self.model))


# Create instances and use the classes
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR500R")

car.drive()
motorcycle.drive()
