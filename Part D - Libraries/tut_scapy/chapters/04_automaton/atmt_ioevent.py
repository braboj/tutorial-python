from scapy.automaton import *


# ATMT: Several actions to a condition / Several conditions trigger action
class Example(Automaton):

    def __init__(self, *args, **kargs):
        self.res = None
        super(Example, self).__init__(*args, **kargs)

    # BEGIN
    @ATMT.state(initial=1)
    def BEGIN(self):
        self.res = "M"

    # Wait for BEGIN and go to MIDDLE
    @ATMT.condition(BEGIN)
    def tr1(self):
        raise self.MIDDLE()

    # First action on transition 1
    @ATMT.action(tr1)  # default prio=0
    def add_e(self):
        self.res += "e"

    # Second action on transition 1
    @ATMT.action(tr1, prio=2)
    def add_c(self):
        self.res += "c"

    # MIDDLE
    @ATMT.state()
    def MIDDLE(self):
        self.res += "u"

    # Condition: Go to END if MIDDLE reached
    @ATMT.condition(MIDDLE)
    def tr2(self):
        raise self.END()

    # Fisrt action on transition 2
    @ATMT.action(tr2, prio=2)
    def add_y(self):
        self.res += "y"

    # Both transition 1 and transition 2 trigger the action
    @ATMT.action(tr1, prio=1)
    @ATMT.action(tr2)
    def add_r(self):
        self.res += "r"

    @ATMT.state(final=1)
    def END(self):
        return self.res


if __name__ == "__main__":

    a = Example(ll=lambda: None, recvsock=lambda: None)
    r = a.run()
    print(r)

    a.restart()
    r = a.run()
    print(r)
