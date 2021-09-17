# import socket
# import struct
#
#
# def getTCPInfo(s):
#     fmt = "B" * 7 + "I" * 21
#     x = struct.unpack(fmt,
#                       s.getsockopt(socket.IPPROTO_TCP, socket.TCP_INFO, 92))
#     print(x)
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# getTCPInfo(s)
# s.connect(('www.google.com', 80))
# getTCPInfo(s)
# s.send(b"hi\n\n")
# getTCPInfo(s)
# s.recv(1024)
# getTCPInfo(s)
