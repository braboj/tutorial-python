"""
Used to troubleshoot network problems

Attacks     : Ping of death, Smurf attack, Fraggle Attack, ping flood, DoS, ICMP tunnels
Prevention  : Deep packet inspection, block ICMP traffic, fix size of ICMP packets

References:
https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
https://en.wikipedia.org/wiki/Ping_of_death
https://en.wikipedia.org/wiki/Smurf_attack
https://www.hackepedia.org/?title=Tfreak
https://tools.cisco.com/security/center/resources/guide_ddos_defense.html
"""

from scapy.sendrecv import sr1
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, ICMP
from scapy.utils import hexdump

eth_header = Ether()
ip_header = IP(dst='192.168.210.15', ttl=20)
icmp_header = ICMP(
    type=13,        # Type of ICMP
    code=0          # Subtype of ICMP
)

data = '\xFF' * (1500 - len(ip_header / icmp_header))

# Send layer 2 datagram
packet = ip_header / icmp_header / data
packet.show2()
hexdump(packet)
reply = sr1(packet, iface='Technical Network', timeout=2)
print(reply)

