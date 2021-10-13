from scapy.sendrecv import sr1
from scapy.layers.inet import IP, ICMP
from scapy.config import conf

conf.verb = 0
p = IP(dst='www.google.bg') / ICMP()
answered = sr1(p, iface='Business Network', filter='icmp')
print(answered.summary())
