"""
https://en.wikipedia.org/wiki/IPv4
https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers
https://en.wikipedia.org/wiki/Differentiated_services
https://en.wikipedia.org/wiki/Explicit_Congestion_Notification
"""

from scapy.sendrecv import sr1
from scapy.layers.inet import IP, ICMP
from scapy.utils import hexdump

# Combine raw ethernet frame with the payload bytes
datagram = IP(dst='192.168.210.240') / ICMP()

# Print raw bytes
hexdump(datagram)

# Send the frame
sr1(datagram, iface='Business Network')
