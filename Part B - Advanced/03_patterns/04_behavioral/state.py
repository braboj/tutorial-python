from abc import ABCMeta, abstractmethod
from six import with_metaclass


class State(with_metaclass(ABCMeta)):

    def __init__(self):
        self._state = None

    def goto(self, state):
        print("Transition to {0}".format(type(state).__name__))
        self._state = state

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass


# STATE: WAIT_CONNECTED
class WaitConnect(State):

    def on_connect(self):
        print("WAIT_CONNECTED handles CONNECT.")
        self.goto(Connected())

# STATE: CONNECTED
class Connected(State):
    def on_connect(self):
        print("CONNECTED handles CONNECT.")

    def on_disconnect(self):
        print("CONNECTED handles DISCONNECT.")


class Broker(object):

    def __init__(self):
        self.state = State()
        self.state.goto(WaitConnect())

    def on_connect(self):
        self.state.on_connect()

    def on_disconnect(self):
        self.state.on_disconnect()


if __name__ == "__main__":
    # The client code.

    context = Broker()
    context.on_connect()
    context.on_disconnect()