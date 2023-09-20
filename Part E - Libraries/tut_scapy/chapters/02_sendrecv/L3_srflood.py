from scapy.sendrecv import srflood
from scapy.layers.inet import IP, ICMP
from scapy.config import conf

conf.verb = 2
p = IP(dst='www.google.bg') / ICMP()
srflood(p, iface='Business Network', filter='icmp')
