# encoding: utf-8
import socket

# ----------------------------------------------------------------------------
# UDP Server
# ----------------------------------------------------------------------------

sock_udp = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
print(sock_udp)

sock_udp.bind(('192.168.43.235', 2525))
print(sock_udp)

# ----------------------------------------------------------------------------
# TCP Server
# ----------------------------------------------------------------------------

sock_tcp = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
print(sock_tcp)

# For this server, the address ('', 2525) is used which means that the
# wildcard is used for the interface address (''), allowing incoming
# connections from any interface on the host. You also bind to port number
# 2525.

sock_tcp.bind(('192.168.43.235', 2525))
print(sock_tcp)

sock_tcp.listen()
print(sock_tcp)

newsock, (remhost, remport) = sock_tcp.accept()

print(newsock)
print(remhost)
print(remport)

print(newsock.getpeername())

while True:
    pass


