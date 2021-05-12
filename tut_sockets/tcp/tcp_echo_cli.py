# encoding: utf-8
import socket

clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clisock.connect(('192.168.43.235', 23000))

clisock.send(b"Hello World\n")
print(clisock.recv(100))

clisock.close()