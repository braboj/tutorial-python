from scapy.layers.dhcp import DHCP_am
from scapy.base_classes import Net
import threading

# Define a pool as generator
# pool = Net(b'192.168.0.128/25')
# for x in pool:
#     print(x)

# Define pool as tuple
pool = (
    b'192.168.210.101',
    b'192.168.210.102',
    b'192.168.210.103',
    b'192.168.210.104',
)

if __name__ == "__main__":

    stop = False

    srv = DHCP_am(iface='Embedded', domain='',
                  pool=pool,
                  network='192.168.210.0/24',
                  gw='',
                  renewal_time=40,
                  lease_time=90,
                  stop_filter=stop
                  )

    srv.sniff_options_list.append('timeout')
    srv(stop_filter=stop, timeout=5)
    server = threading.Thread(target=srv)
    server.start()