from scapy.sendrecv import srploop
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.config import conf

conf.verb = 2
p = Ether() / IP(dst='www.google.bg') / ICMP()
srploop(p, iface='Business Network', filter='icmp', count=10)
