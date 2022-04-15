# from scapy.layers.l2 import ARP
# from scapy.sendrecv import sniff
# from scapy.layers.inet import IP, TCP

from scapy.all import *
from scapy.layers.tls.record import TLS
from scapy.layers.tls.session import TLSSession
load_layer('tls')


def started():
    print("STARTED")


packets = sniff(

    # Network interface name
    iface='Embedded',

    # How many packets to capture
    count=0,

    # Callback on captured packet
    prn=lambda x: x.summary,

    # Store or discard sniffed packets
    store=False,

    # TCP or TLS sessions
    session=TLSSession,

    # Barkley Packet Fitler string
    # filter='tcp and port 502',

    # Filter as python function
    lfilter=lambda x: x.haslayer(TLS),

    # Stop condition
    # stop_filter=lambda x: x.haslayer(TCP),

    # Read from PCAP file
    offline=None,

    #
    quiet=False,

    #
    timeout=None,

    # Custom socket to listen to
    L2socket=None,

    # ???
    opened_socket=None,

    # Called as soon the sniffer is started
    started_callback=started,
)
