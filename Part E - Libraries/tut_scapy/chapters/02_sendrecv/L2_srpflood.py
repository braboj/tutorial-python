from scapy.sendrecv import srpflood
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.config import conf

conf.verb = 2
p = Ether() / IP(dst='www.google.bg') / ICMP()
srpflood(p, iface='Business Network', filter='icmp')
