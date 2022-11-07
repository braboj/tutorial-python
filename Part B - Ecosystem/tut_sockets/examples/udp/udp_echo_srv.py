# encoding: utf-8
import socket

dgramSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dgramSock.bind(('', 23000))

while True:
    msg, (addr, port) = dgramSock.recvfrom(100)
    dgramSock.sendto(msg, (addr, port))
