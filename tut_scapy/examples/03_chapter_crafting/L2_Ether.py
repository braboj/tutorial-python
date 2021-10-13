from scapy.sendrecv import sendp
from scapy.layers.l2 import Ether
from scapy.utils import hexdump

# Prepare raw ethernet frame
eth_header = Ether(src='00:aa:bb:cc:dd:ee', dst='FF:FF:FF:FF:FF:FF', type=0x9000)

# Add some payload
payload = '\xAA' * 60

# Combine raw ethernet frame with the payload bytes
frame = eth_header / payload

# Print raw bytes
hexdump(frame)

# Send the frame
sendp(frame, iface='Business Network')

