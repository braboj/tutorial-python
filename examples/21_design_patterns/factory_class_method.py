# Example: Factory Method as a class method

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

    @classmethod
    def from_json(cls, json):
        # Factory method

        # Get transport type
        token = json.get("transport_type")

        # Convert to lowercase and remove whitespace
        transport_type = token.lower().strip(" \t\n\r")

        # Factory logic
        if transport_type == "truck":
            return Truck()

        elif transport_type == "ship":
            return Ship()

        else:
            raise ValueError("Invalid transport type")


class App(object):

    @staticmethod
    def run():

        # Select transport
        json = {"transport_type": "truck"}
        transport = Logistic.from_json(json)

        # Deliver
        logistic = Logistic(transport)
        logistic.deliver()


if __name__ == "__main__":
    app = App()
    app.run()
