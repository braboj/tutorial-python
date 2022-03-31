# encoding: utf-8
import socket

# TCP socket
tcp_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)

# UDP socket
udp_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_DGRAM
)

print("TCP SOCKET = {0}".format(tcp_socket))
print("UDP SOCKET = {0}".format(udp_socket))

tcp_socket.close()
print(tcp_socket)

del tcp_socket

# print(tcp_socket.fileno())
# print(tcp_socket.family)
# print(tcp_socket.type)
# print(tcp_socket.proto)





