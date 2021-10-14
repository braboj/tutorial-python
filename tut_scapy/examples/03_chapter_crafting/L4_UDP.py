"""
https://en.wikipedia.org/wiki/User_Datagram_Protocol
"""

from scapy.sendrecv import send
from scapy.layers.inet import IP, UDP
from scapy.utils import hexdump

# Combine raw ethernet frame with the payload bytes
ip_header = IP(dst='192.168.210.254')
udp_header = UDP(
    sport=0,        # 16: Source port
    dport=10000,    # 16: Destination port
    len=10,         # 16: Length of header and data in bytes
    chksum=None     # 16: Checksum of header and data
)

# Add some data to the data
data = '\xAA' * 2

# Build the datagram
datagram = ip_header / udp_header / data

# Print raw bytes
hexdump(datagram)

# Send L3 datagram
send(datagram, iface='Technical Network')
