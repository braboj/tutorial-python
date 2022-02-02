"""
https://en.wikipedia.org/wiki/Transmission_Control_Protocol
"""

from scapy.sendrecv import sr1, send
from scapy.layers.inet import IP, TCP
from scapy.utils import hexdump

# Prepare IP packet
ip = IP(dst='192.168.210.254')

# Prepare TCP SYN Request
tcp_options = [
     ("MSS", 1460),
     ("NOP", None),
     ("WScale", 8),
     ("NOP", None),
     ("NOP", None),
     ("SAckOK", ''),
]

tcp = TCP(
    sport=1033,             # 16: Source port
    dport=80,               # 16: Destination port
    seq=0x253283A5,         # 32: Stream-ID in handshake process or byte offset
    ack=0,                  # 32: Next byte offset expected by the receiver
    dataofs=8,              # 04: Data offset or header length in 32-bit words
    reserved=0,             # 03: Reserved bits
    flags=2,                # 09: Control flags
    window=64240,           # 16: The size of the receive window in bytes
    chksum=None,            # 16: Checksum over header, payload and IP pseudo-header
    urgptr=0,               # 16: Offset from sequence number indicating the urgent byte
    options=tcp_options,    # ..: TCP options
)

# Build datagram
datagram = ip / tcp

# Print raw bytes
hexdump(datagram)

# Send the datagram
send(datagram, iface='Technical Network')
