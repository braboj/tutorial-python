"""
IEEE 802.1Q     :
IEEE 802.1ad    : QinQ

https://en.wikipedia.org/wiki/IEEE_802.1Q
https://en.wikipedia.org/wiki/IEEE_P802.1p

"""

from scapy.sendrecv import sendp
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether, Dot1Q
from scapy.utils import hexdump

# Prepare Ethernet II frame
eth = Ether(
    src='00:aa:bb:cc:dd:ee',  # 48: Source hardware address
    dst='FF:FF:FF:FF:FF:FF',    # 48: Target hardware address
    type=0x8100,                # 16: Protocol identifier
)

# Prepare IEEE 802.1Q fields
dot1q = Dot1Q(
    prio=0,         # 03: PCP   (Priority code point)
    id=0,           # 01: CFI   (Cannonical Format Indicator) or DEI (Drop Eligible Indicator)
    vlan=0,         # 12: VID   (VLAN identifier)
    type=0x0800,    # 16: TPID  (Tag protocol identifier)
)

# Build resulting frame
frame = eth / dot1q / IP(dst='192.168.210.254') / ICMP()
hexdump(frame)

# Send the frame
sendp(frame, iface='Technical Network')
