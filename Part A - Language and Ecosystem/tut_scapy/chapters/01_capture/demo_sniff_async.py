import time
from scapy.sendrecv import AsyncSniffer
from scapy.layers.inet import TCP


def started():
    print("SNIFFER STARTED")


t = AsyncSniffer(
    iface='Business Network',
    count=0,
    prn=lambda x: x.summary,
    store=False,
    session=None,
    filter='',
    lfilter=lambda x: x.haslayer(TCP),
    # stop_filter=lambda x: x.haslayer(TCP),
    offline=None,
    quiet=False,
    timeout=10,
    L2socket=None,
    opened_socket=None,
    started_callback=started,
)

t.start()
time.sleep(1)
print("STOP SNIFFER")
t.stop()

