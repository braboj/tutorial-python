from scapy.sendrecv import srp1
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.config import conf

conf.verb = 0
p = Ether() / IP(dst='www.google.bg') / ICMP()
answered = srp1(p, iface='Business Network', filter='icmp')
print(answered.summary())
