import socket

HOST = "172.20.10.114"
PORT = 10023

# Later to be used to simulate error in certificate validation
HOST = socket.getaddrinfo(HOST, PORT)[0][4][0]
print(HOST)