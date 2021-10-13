# TODO: Short description of the protocol with references

from scapy.sendrecv import sendp
from scapy.layers.l2 import Ether, ARP
from scapy.utils import hexdump

# Prepare raw ethernet frame
eth_header = Ether(src='00:aa:bb:cc:dd:ee')
arp_header = ARP(
    hwtype=0x0001,              # 16: Protocol type of L2 (Ethernet)
    ptype=0x0800,               # 16: Protocol type of L3 (IP)
    hwlen=6,                    # 08: MAC address length in bytes
    plen=4,                     # 08: Protocol address length in bytes
    op=1,                       # 16: ARP operation (1=request, 2=reply)
    hwsrc='00:aa:bb:cc:dd:ee',  # 48: Source MAC
    psrc='172.20.11.11',        # 32: Source IP
    hwdst='ff:ff:ff:ff:Ff:ff',  # 48: Target MAC
    pdst='172.20.10.114'        # 32: Target IP
)

# Add some payload
payload = '\xAA' * 60

# Combine raw ethernet frame with the payload bytes
frame = eth_header / arp_header / payload

# Print raw bytes
hexdump(frame)

# Send the frame
sendp(frame, iface='Business Network')
pass
