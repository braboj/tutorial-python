from scapy.sendrecv import srp
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.config import conf

conf.verb = 0
p = Ether() / IP(dst='www.google.bg') / ICMP()
answered, unanswered = srp(p, iface='Business Network', filter='icmp')
for res in answered.res:
    print(res)
