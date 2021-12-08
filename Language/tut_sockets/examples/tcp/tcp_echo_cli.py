# encoding: utf-8
import socket

"""
Simple echo client which will connect to the echo server, send data and wait for the data sent back. After the echo 
is received the socket will be closed.
"""

# 1. Create client socket
clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. In case the adapter has more than one address we can bind to a specific IP
clisock.bind(('localhost', 0))

# 3. Connect to the server port
clisock.connect(('localhost', 2525))

# 4. Send some data
for _ in range(2):
    clisock.send(bytearray([0xFF] * 8))

# 5. Receive some data
print(clisock.recv(1024))

# 6. Close the connection
clisock.close()