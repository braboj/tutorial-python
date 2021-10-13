"""
https://en.wikipedia.org/wiki/Bootstrap_Protocol
https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol
http://wiki.cas.mcmaster.ca/index.php?title=File:DHCP_state_Diagram.jpg&limit=20
https://www.dummies.com/programming/networking/cisco/dynamic-host-configuration-protocol-dhcp-services/
"""

from scapy.sendrecv import send
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.utils import hexdump

# Combine raw ethernet frame with the payload bytes
ip = IP(src='0.0.0.0', dst='255.255.255.255')
udp = UDP(sport=68, dport=67)
bootp = BOOTP(
    op=1,                           # Message type (1=Request, 2=Reply)
    htype=1,                        # Hardware type (1=Ethernet)
    hlen=6,                         # Hardware address length (6 for MAC)
    hops=0,                         # Routing hops
    xid=1,                          # Transaction ID
    secs=0,                         # Seconds elapsed
    flags=0x8000,                   # BOOTP flags
    ciaddr='0.0.0.0',               # Client IP address
    yiaddr='0.0.0.0',               # Your IP address
    siaddr='0.0.0.0',               # Server IP address
    giaddr='0.0.0.0',               # Gateway IP address
    # chaddr='00:aa:bb:cc:dd:ee',     # Client hardware address
    # sname='',                       # Server host name
    # file='',                        # Boot file name
    # options=''                      # Options
)

# DHCP Options and padding
dhcp_options = [
    ("message-type", 1),
    ("max_dhcp_size", 1152),
    ("client_id", "cisco-cc00.0ac4.0000-Fa0/0"),
    ("hostname", "R0"),
    ("param_req_list", [1, 6, 15, 44, 3, 33, 150, 43]),
    "end",
]
dhcp = DHCP(options=dhcp_options)

# Calculate padding in DHCP options (define max DHCP size to 576 bytes)
padding = ["pad" for x in range(576 - len(bootp / dhcp))]
dhcp.options.extend(padding)

# Build the datagram
datagram = ip / udp / bootp / dhcp

# Print raw bytes
hexdump(datagram)

# Send L3 datagram
send(datagram, iface='Technical Network')
