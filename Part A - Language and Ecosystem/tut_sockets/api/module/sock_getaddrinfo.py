import socket
from collections import namedtuple

# Define named tuple
AddressInfo = namedtuple('AddrInfo', 'family socktype proto canonname sockaddr')

# Get address info
result = socket.getaddrinfo("google.bg", 80)

# Unpack first element of address info into the named tuple
info = AddressInfo(*result[0])

print(info)
