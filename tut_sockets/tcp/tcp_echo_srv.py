# encoding: utf-8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ACCEPTCONN)
print(state)

sock.bind(('', 23000))
state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ACCEPTCONN)
print(state)

sock.listen(5)
state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ACCEPTCONN)
print(state)


while True:
    client, addr_info = sock.accept()
    data = client.recv(100)
    client.send(data)
    client.close()
