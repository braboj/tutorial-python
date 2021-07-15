# encoding: utf-8
import socket

clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clisock.connect(('172.20.10.114', 23000))

clisock.send(b"Hello World\n")
print(clisock.recv(100))
clisock.close()