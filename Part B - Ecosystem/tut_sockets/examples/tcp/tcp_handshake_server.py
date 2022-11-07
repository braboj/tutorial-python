# encoding: utf-8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)

# For this server, the address ('', 2525) is used, which means that the
# wildcard is used for the interface address (''), allowing incoming
# connections from any interface on the host.

# Bind all interfaces for incoming connections on port 2525 (equivalent to 0.0.0.0)
sock.bind(('', 2525))
print(sock)

sock.listen(5)
print(sock)

newsock, (remhost, remport) = sock.accept()

print(newsock)
print(remhost)
print(remport)

print(newsock.getpeername())

while True:
    pass
