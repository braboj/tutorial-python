# state

```python
# State interface
class State(object):

    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def send_data(self, data):
        raise NotImplementedError


# Concrete State: Disconnected
class DisconnectedState(State):

    def connect(self):

        # Action
        print("Connecting to the server...")

        # Transition to the Connected state
        return ConnectedState()

    def disconnect(self):
        print("Already disconnected.")
        return self

    def send_data(self, data):

        print("Cannot send data while disconnected.")
        return self


# Concrete State: Connected
class ConnectedState(State):

    def connect(self):

        # Action
        print("Already connected.")

        # Transition
        return self

    def disconnect(self):
        # Action
        print("Disconnecting from the server...")

        # Transition
        return DisconnectedState()

    def send_data(self, data):
        # Action
        print(f"Sending data to the server: {data}")

        # Transition
        return self


# Context class
class Client(object):

    def __init__(self):
        # Initial state
        self.state = DisconnectedState()

    def connect(self):
        self.state = self.state.connect()

    def disconnect(self):
        self.state = self.state.disconnect()

    def send_data(self, data):
        self.state.send_data(data)


# Client code
if __name__ == "__main__":

    client = Client()

    client.send_data("Hello, server!")  # Try sending data while disconnected

    client.connect()
    client.send_data("Hello, server!")  # Send data after connecting

    client.connect()  # Try connecting again

    client.disconnect()
    client.send_data("Goodbye, server!")  # Send data after disconnecting
```
