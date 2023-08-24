"""
Your example works, if there is a packet. As the documentation says stop_filter is a
"Python function applied to each packet". If there is no packet (e.g. if you use a very restrictive filter
and/or there is very little traffic) the process/thread will wait and exit only after
the next captured packet when stop_filter is applied.
"""

import time
import threading
from scapy.all import sniff


e = threading.Event()


def _sniff(x):
    packets = sniff(
        # iface=None,
        filter="tcp port 80",
        stop_filter=lambda p: x.is_set(),
        # timeout=10
    )
    print("Stopped after {0} packets".format(len(packets)))


# Start sniffer
print("Start capturing thread")
t = threading.Thread(target=_sniff, args=(e,))
t.start()

# Wait some time to capture traffic
time.sleep(3)
print("Try to shutdown capturing...")
e.set()

# This will run until you send a HTTP request somewhere
# There is no way to exit clean if no package is received
while True:
    t.join(2)
    if t.is_alive():
        print("Thread is still running...")
    else:
        break

print("Shutdown complete!")
