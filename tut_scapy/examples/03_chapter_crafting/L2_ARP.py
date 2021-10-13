from scapy.sendrecv import sendp
from scapy.layers.l2 import Ether, ARP
from scapy.utils import hexdump

# Prepare raw ethernet frame
eth_header = Ether(src='00:aa:bb:cc:dd:ee')
arp_header = ARP(
    hwtype=0x0001,              # Protocol type of L2 (Ethernet)
    ptype=0x0800,               # Protocol type of L3 (IP)
    hwlen=6,                    # MAC address length in bytes
    plen=4,                     # Protocol address length in bytes
    op=1,                       # ARP operation (1=request, 2=reply)
    hwsrc='00:aa:bb:cc:dd:ee',  # Source MAC
    psrc='172.20.11.11',        # Source IP
    hwdst='ff:ff:ff:ff:Ff:ff',  # Target MAC
    pdst='172.20.10.114'        # Target IP
)

# Add some payload
payload = '\xAA' * 60

# Combine raw ethernet frame with the payload bytes
arp_frame = eth_header / arp_header / payload

# Print raw bytes
hexdump(arp_frame)

# Send the frame
sendp(arp_frame, iface='Business Network')
pass
