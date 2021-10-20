from scapy.all import *
from scapy.layers.http import *


# ATMT: Simple Automaton
class ATMT1(Automaton):
    def parse_args(self, init, *args, **kargs):
        Automaton.parse_args(self, *args, **kargs)
        self.init = init

    @ATMT.state(initial=1)
    def BEGIN(self):
        raise self.MAIN(self.init)

    @ATMT.state()
    def MAIN(self, s):
        return s

    @ATMT.condition(MAIN, prio=-1)
    def go_to_END(self, s):
        if len(s) > 20:
            raise self.END(s).action_parameters(s)

    @ATMT.condition(MAIN)
    def trA(self, s):
        if s.endswith("b"):
            raise self.MAIN(s + "a")

    @ATMT.condition(MAIN)
    def trB(self, s):
        if s.endswith("a"):
            raise self.MAIN(s * 2 + "b")

    @ATMT.state(final=1)
    def END(self, s):
        return s

    @ATMT.action(go_to_END)
    def action_test(self, s):
        self.result = s


a = ATMT1(init="a", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'aabaaababaaabaaababab')
r = a.result

assert (r == 'aabaaababaaabaaababab')
a = ATMT1(init="b", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'babababababababababababababab')
r = a.result
assert (r == 'babababababababababababababab')

try:
    ATMT1(init="", ll=lambda: None, recvsock=lambda: None).run()
except Automaton.Stuck:
    assert True
else:
    assert False


# ATMT: State overloading
class ATMT2(ATMT1):
    @ATMT.state()
    def MAIN(self, s):
        return "c" + ATMT1.MAIN(self, s).run()


a = ATMT2(init="a", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'ccccccacabacccacababacccccacabacccacababab')

r = a.result

assert (r == 'ccccccacabacccacababacccccacabacccacababab')
a = ATMT2(init="b", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'cccccbaccbabaccccbaccbabab')
r = a.result

assert (r == 'cccccbaccbabaccccbaccbabab')


# ATMT: Condition overloading
class ATMT3(ATMT2):
    @ATMT.condition(ATMT1.MAIN)
    def trA(self, s):
        if s.endswith("b"):
            raise self.MAIN(s + "da")


a = ATMT3(init="a", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'cccccacabdacccacabdabda')
r = a.result

assert (r == 'cccccacabdacccacabdabda')
a = ATMT3(init="b", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'cccccbdaccbdabdaccccbdaccbdabdab')
r = a.result
assert (r == 'cccccbdaccbdabdaccccbdaccbdabdab')


# ATMT: Action overloading
class ATMT4(ATMT3):
    @ATMT.action(ATMT1.go_to_END)
    def action_test(self, s):
        self.result = "e" + s + "e"


a = ATMT4(init="a", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'cccccacabdacccacabdabda')
r = a.result

assert (r == 'ecccccacabdacccacabdabdae')
a = ATMT4(init="b", ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'cccccbdaccbdabdaccccbdaccbdabdab')
r = a.result

assert (r == 'ecccccbdaccbdabdaccccbdaccbdabdabe')


# ATMT: Priorities
class ATMT5(Automaton):
    @ATMT.state(initial=1)
    def BEGIN(self):
        self.res = "J"

    @ATMT.condition(BEGIN, prio=1)
    def tr1(self):
        self.res += "i"
        raise self.END()

    @ATMT.condition(BEGIN)
    def tr2(self):
        self.res += "p"

    @ATMT.condition(BEGIN, prio=-1)
    def tr3(self):
        self.res += "u"

    @ATMT.action(tr1)
    def ac1(self):
        self.res += "e"

    @ATMT.action(tr1, prio=-1)
    def ac2(self):
        self.res += "t"

    @ATMT.action(tr1, prio=1)
    def ac3(self):
        self.res += "r"

    @ATMT.state(final=1)
    def END(self):
        return self.res


a = ATMT5(ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == 'Jupiter')


# ATMT: Same action for many conditions
class ATMT6(Automaton):
    @ATMT.state(initial=1)
    def BEGIN(self):
        self.res = "M"

    @ATMT.condition(BEGIN)
    def tr1(self):
        raise self.MIDDLE()

    @ATMT.action(tr1)  # default prio=0
    def add_e(self):
        self.res += "e"

    @ATMT.action(tr1, prio=2)
    def add_c(self):
        self.res += "c"

    @ATMT.state()
    def MIDDLE(self):
        self.res += "u"

    @ATMT.condition(MIDDLE)
    def tr2(self):
        raise self.END()

    @ATMT.action(tr2, prio=2)
    def add_y(self):
        self.res += "y"

    @ATMT.action(tr1, prio=1)
    @ATMT.action(tr2)
    def add_r(self):
        self.res += "r"

    @ATMT.state(final=1)
    def END(self):
        return self.res


a = ATMT6(ll=lambda: None, recvsock=lambda: None)
r = a.run()
assert (r == 'Mercury')

a.restart()
r = a.run()

assert (r == 'Mercury')


# ATMT: IO event
class ATMT7(Automaton):
    @ATMT.state(initial=1)
    def BEGIN(self):
        self.res = "S"

    @ATMT.ioevent(BEGIN, name="tst")
    def tr1(self, fd):
        self.res += fd.recv()
        raise self.NEXT_STATE()

    @ATMT.state()
    def NEXT_STATE(self):
        self.oi.tst.send("ur")

    @ATMT.ioevent(NEXT_STATE, name="tst")
    def tr2(self, fd):
        self.res += fd.recv()
        raise self.END()

    @ATMT.state(final=1)
    def END(self):
        self.res += "n"
        return self.res


a = ATMT7(ll=lambda: None, recvsock=lambda: None)
a.run(wait=False)
a.io.tst.send("at")
r = a.io.tst.recv()

a.io.tst.send(r)
r = a.run()

assert (r == "Saturn")

a.restart()
a.run(wait=False)
a.io.tst.send("at")
r = a.io.tst.recv()

a.io.tst.send(r)
r = a.run()

assert (r == "Saturn")

import os


# ATMT: IO event from external file descriptor
class ATMT8(Automaton):
    @ATMT.state(initial=1)
    def BEGIN(self):
        self.res = b"U"

    @ATMT.ioevent(BEGIN, name="extfd")
    def tr1(self, fd):
        self.res += fd.read(2)
        raise self.NEXT_STATE()

    @ATMT.state()
    def NEXT_STATE(self):
        pass

    @ATMT.ioevent(NEXT_STATE, name="extfd")
    def tr2(self, fd):
        self.res += fd.read(2)
        raise self.END()

    @ATMT.state(final=1)
    def END(self):
        self.res += b"s"
        return self.res


if WINDOWS:
    r = w = ObjectPipe()
else:
    r, w = os.pipe()


def writeOn(w, msg):
    if WINDOWS:
        w.write(msg)
    else:
        os.write(w, msg)


a = ATMT8(external_fd={"extfd": r}, ll=lambda: None, recvsock=lambda: None)
a.run(wait=False)
writeOn(w, b"ra")
writeOn(w, b"nu")

r = a.run()

assert (r == b"Uranus")

a.restart()
a.run(wait=False)
writeOn(w, b"ra")
writeOn(w, b"nu")
r = a.run()

assert (r == b"Uranus")


class ATMT9(Automaton):
    def my_send(self, x):
        self.io.loop.send(x)

    @ATMT.state(initial=1)
    def BEGIN(self):
        self.res = "V"
        self.send(Raw("ENU"))

    @ATMT.ioevent(BEGIN, name="loop")
    def received_sth(self, fd):
        self.res += plain_str(fd.recv().load)
        raise self.END()

    @ATMT.state(final=1)
    def END(self):
        self.res += "s"
        return self.res


a = ATMT9(debug=5, ll=lambda: None, recvsock=lambda: None)
r = a.run()

assert (r == "VENUs")

a.restart()
r = a.run()

assert (r == "VENUs")

a.restart()
a.BEGIN.intercepts()
while True:
    try:
        x = a.run()
    except Automaton.InterceptionPoint as p:
        a.accept_packet(Raw(p.packet.load.lower()), wait=False)
    else:
        break

r = x

assert (r == "Venus")