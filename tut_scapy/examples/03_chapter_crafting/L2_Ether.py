"""
LAN protocol based on hardware addresses
--------------------------------------------------------------------------------------------------

Attacks:
    Loop                    : More than one path between 2 nodes
    Broadcast storm         : In case of loops broadcasts/multicasts will flood the network
    MAC flooding            :
    VLAN hopping            :
    Double Encapsulation    :
    Jabber                  : Frame transmission time is too long (oversized frames)
    Runt                    : Frame transmission time is too short (undersized frames

Protection:
    Port security
    MAC lockdown
    Broadcast filtering
    Virtual LAN
    Link aggregation

References:
    https://en.wikipedia.org/wiki/Ethernet
    https://en.wikipedia.org/wiki/Ethernet_frame
    https://en.wikipedia.org/wiki/Autonegotiation
    https://en.wikipedia.org/wiki/Switching_loop
    https://en.wikipedia.org/wiki/Broadcast_storm
    https://en.wikipedia.org/wiki/Ethernet_frame#Runt_frames
    https://www.sanog.org/resources/sanog7/yusuf-L2-attack-mitigation.pdf
    \
"""

from scapy.sendrecv import sendp
from scapy.layers.l2 import Ether
from scapy.utils import hexdump

# Prepare Ethernet II frame
eth_header = Ether(
    src='00:aa:bb:cc:dd:ee',    # 48: Source hardware address
    dst='FF:FF:FF:FF:FF:FF',    # 48: Target hardware address
    type=0x9000                 # 16: Internet protocol type in payload
)

# Add some payload
payload = '\xAA' * 60

# Combine raw ethernet frame with the payload bytes
frame = eth_header / payload

# Print raw bytes
hexdump(frame)

# Send the frame
sendp(frame, iface='Business Network')

