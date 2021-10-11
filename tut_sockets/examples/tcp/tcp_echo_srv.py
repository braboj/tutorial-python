# encoding: utf-8
import socket

"""
Simple echo server which will wait for a new client to send data, receive data from the client, send the data back and 
then close the connection.
"""

# 1. Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind socket to a specific address and service port
sock.bind(('localhost', 2525))

# 3. Start listening on socket
sock.listen(5)

while True:

    # 4. Blocks until client is connected
    client, addr_info = sock.accept()

    # 5. Receive data
    data = client.recv(1024)

    # 6. Send data
    # client.send(data)

    # 7. Close connection
    client.close()
