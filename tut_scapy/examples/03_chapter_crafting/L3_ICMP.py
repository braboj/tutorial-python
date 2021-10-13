"""
Support protocol for internet management and troubleshooting
--------------------------------------------------------------------------------------------------
Attacks:
    Ping of death, Smurf attack, Fraggle Attack, ping flood, DoS, ICMP tunnels

Protection:
    Deep packet inspection, block ICMP traffic, fix size of ICMP packets
--------------------------------------------------------------------------------------------------
References:
    https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
    https://en.wikipedia.org/wiki/Ping_of_death
    https://en.wikipedia.org/wiki/Smurf_attack
    https://www.hackepedia.org/?title=Tfreak
    https://tools.cisco.com/security/center/resources/guide_ddos_defense.html
"""

from scapy.sendrecv import sr1
from scapy.layers.inet import IP, ICMP
from scapy.utils import hexdump

ip = IP(dst='192.168.210.254', ttl=20)
icmp = ICMP(
    type=8,         # 08: Type of ICMP
    code=0,         # 08: Subtype of ICMP
    # chksum=0      # 16: Checksum for header and data
)

data = '\xFF' * (1500 - len(ip / icmp))

# Send layer 2 datagram
packet = ip / icmp / data
packet.show2()
hexdump(packet)
reply = sr1(packet, iface='Technical Network', timeout=2)
print(reply)

