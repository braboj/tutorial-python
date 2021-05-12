# encoding: utf-8
import socket

sock = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)

print("TCP SOCKET = {0}".format(sock))

sock.close()
print(sock)

del sock

# print(tcp_socket.fileno())
# print(tcp_socket.family)
# print(tcp_socket.type)
# print(tcp_socket.proto)





