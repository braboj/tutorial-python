from scapy.all import *

ERROR = 0


class AutomatonStates(Automaton):

    @ATMT.state(initial=1)
    def BEGIN(self):
        print("BEGIN")
        raise self.SOME_STATE()

    @ATMT.state()
    def SOME_STATE(self):
        print("SOME_STATE")
        raise self.END()

    @ATMT.state(final=1)
    def END(self):
        print("END")
        if ERROR:
            raise self.ERROR()
        else:
            return "Result of the automaton: 42"

    @ATMT.state(error=1)
    def ERROR(self):
        return "Partial result, or explanation"


if __name__ == "__main__":
    t = AutomatonStates(iface='Technical Network')
    t.run()