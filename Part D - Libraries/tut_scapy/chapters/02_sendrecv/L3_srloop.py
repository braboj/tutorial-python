from scapy.sendrecv import srloop
from scapy.layers.inet import IP, ICMP
from scapy.config import conf

conf.verb = 2
p = IP(dst='www.google.bg') / ICMP()
srloop(p, iface='Business Network', filter='icmp', count=10)
