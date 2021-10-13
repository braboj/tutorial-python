from scapy.sendrecv import sr
from scapy.layers.inet import IP, ICMP
from scapy.config import conf

conf.verb = 0
p = IP(dst='www.google.bg') / ICMP()
answered, unanswered = sr(p, iface='Business Network', filter='icmp')
for res in answered.res:
    print(res)
