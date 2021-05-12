# encoding: utf-8
import socket

# ----------------------------------------------------------------------------
# UDP Client
# ----------------------------------------------------------------------------

udp_sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.connect(('192.168.43.235', 2525))

while True:
    pass