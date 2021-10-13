"""
https://en.wikipedia.org/wiki/IPv4
https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers
https://en.wikipedia.org/wiki/Differentiated_services
https://en.wikipedia.org/wiki/Explicit_Congestion_Notification
"""

import socket
from scapy.sendrecv import sendp
from scapy.packet import Raw
from scapy.layers.inet import IP, in4_chksum
from scapy.layers.l2 import Ether
from scapy.utils import hexdump

# Prepare frame
eth_header = Ether(src='00:aa:bb:cc:dd:ee')

# Prepare datagram
ip_header = IP(
    version=4,              # Protocol version
    ihl=5,                  # Header length in 32-bit words
    tos=0,                  # Type of service (Now Differentiated Service Code Point + Explicit Congestion Notification)
    len=80,                 # Total length of the datagram in bytes (header + payload)
    id=26231,               # Datagram identifier
    flags=0,                # Fragmentation flags
    frag=0,                 # Fragmentation offset
    ttl=20,                 # Time-to-live in seconds (prevent routing loops, hops counter)
    proto=0xFF,             # Higher level protocol in payload
    chksum=None,            # Header checksum (must be calculated anew in the router due to changes in TTL)
    src='172.20.10.114',    # Source IP address
    dst='172.20.11.114',    # Destination IP address
    options=[]              # IP options (rarely used)
)

# Calculate checksum (sum of 16-bit words in header)
result = ip_header.__class__(Raw(ip_header).load).chksum
ip_header.chksum = result

# Add some random payload
data = '\xAA' * 60

# Combine raw ethernet frame with the payload bytes
datagram = eth_header / ip_header / data

# Print raw bytes
hexdump(datagram)

# Send the frame
sendp(datagram, iface='Business Network')
