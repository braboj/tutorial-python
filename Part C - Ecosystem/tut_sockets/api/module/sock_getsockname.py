import socket

# Connect to the device
s = socket.socket()
s.connect(('www.google.bg', 80))

# Return the address of the socket owner
print(s.getsockname())
