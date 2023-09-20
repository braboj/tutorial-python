import time

from scapy.sendrecv import send, AsyncSniffer
from scapy.layers.inet import IP, ICMP


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
p = IP(dst='www.google.bg') / ICMP()
send(p, iface='Business Network', count=1)
time.sleep(1)

# Stop sniffer
t.stop()
