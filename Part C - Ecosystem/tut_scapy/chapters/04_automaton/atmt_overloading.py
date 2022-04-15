from scapy.all import *
from atmt_state import AutomatonStates

# TODO: Demonstrate state, action and transition overloading

class ATMT1(AutomatonStates):

    @ATMT.state(initial=1)
    def BEGIN(self):
        print("BEGIN")
        raise self.END()

    @ATMT.state(final=1)
    def END(self):
        print("END")


class ATMT2(ATMT1):

    @ATMT.state(initial=1)
    def BEGIN(self):
        print("Overloaded state BEGIN")
        raise self.END()


a = ATMT2()
a.run()