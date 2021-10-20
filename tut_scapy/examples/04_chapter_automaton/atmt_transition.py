from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import ARP


class Example(Automaton):

    @ATMT.state(initial=1)
    def WAITING(self):
        print("WAITING")

    @ATMT.receive_condition(WAITING, prio=1)
    def it_is_ICMP(self, pkt):
        if ICMP in pkt:
            raise self.RECEIVED_ICMP(pkt)

    @ATMT.receive_condition(WAITING, prio=2)
    def it_is_IP(self, pkt):
        if ARP in pkt:
            raise self.RECEIVED_IP(pkt)

    @ATMT.timeout(WAITING, 60.0)
    def waiting_timeout(self):
        raise self.ERROR_TIMEOUT()

    @ATMT.state()
    def RECEIVED_ICMP(self, pkt):
        print(pkt.summary())
        raise self.END()

    @ATMT.state()
    def RECEIVED_IP(self, pkt):
        print(pkt.summary())
        raise self.END()

    @ATMT.state(final=1)
    def END(self):
        raise self.WAITING()


if __name__ == "__main__":
    atmt = Example(iface='Technical Network')
    atmt.run()