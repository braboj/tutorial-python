# encoding: utf-8
import socket

"""
Simple echo client which will connect to the echo server, send data and wait for the data sent back. After the echo 
is received the socket will be closed.
"""

# 1. Create client socket
clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. In case the adapter has more than one address we can bind to a specific IP
clisock.bind(('192.168.210.2', 0))

# 3. Connect to the server port
clisock.connect(('192.168.210.1', 23000))

# 4. Send some data
clisock.send(b"Hello World\n")

# 5. Receive some data
print(clisock.recv(1024))

# 6. Close the connection
clisock.close()