# encoding: utf-8
import socket

dgramSock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

dgramSock.sendto(b"Hello World\n", ('192.168.43.235', 23000))
print(dgramSock.recv(100))
dgramSock.close()