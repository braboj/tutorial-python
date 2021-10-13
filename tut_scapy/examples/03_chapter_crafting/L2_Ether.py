# TODO: Short description of the protocol with references

from scapy.sendrecv import sendp
from scapy.layers.l2 import Ether
from scapy.utils import hexdump

# Prepare raw ethernet frame
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

