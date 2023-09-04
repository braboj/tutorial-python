# Example: Factory Method as a Static Method

class Transport(object):
    def __init__(self):
        pass

    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        print("Delivering by land in a box")


class Ship(Transport):
    def deliver(self):
        print("Delivering by sea in a container")


class Logistic(object):
    def __init__(self, transport):
        self.transport = transport

    def deliver(self):
        self.transport.deliver()


class App(object):

    @staticmethod
    def select_transport():
        # Factory method

        # Get transport type
        token = input("Select transport type: ")

        # Convert to lowercase and remove whitespace
        transport_type = token.lower().strip(" \t\n\r")

        # Factory logic
        if transport_type == "truck":
            return Truck()

        elif transport_type == "ship":
            return Ship()

        else:
            raise ValueError("Invalid transport type")

    def run(self):

        # Select transport
        transport = self.select_transport()

        # Deliver
        logistic = Logistic(transport)
        logistic.deliver()


if __name__ == "__main__":
    app = App()
    app.run()