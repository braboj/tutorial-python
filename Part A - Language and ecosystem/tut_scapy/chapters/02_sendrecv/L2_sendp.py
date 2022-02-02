import time

from scapy.sendrecv import sendp, AsyncSniffer
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether


def handle_icmp(packet):
    print(packet.summary())
    pass


t = AsyncSniffer(
    iface='Business Network',
    filter='icmp',
    prn=handle_icmp,
)

# Start sniffer
t.start()

# Send packet and wait
p = Ether() / IP(dst='www.google.bg') / ICMP()
sendp(p, iface='Business Network', count=1)
time.sleep(1)

# Stop sniffer
t.stop()
