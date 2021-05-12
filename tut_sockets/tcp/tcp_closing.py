# encoding: utf-8
import socket

# Socket factory
sock = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)
print(sock)

sock.close()
print(sock)

del sock
