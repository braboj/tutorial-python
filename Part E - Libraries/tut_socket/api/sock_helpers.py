# encoding: utf-8
import socket

# Get hostname from IP address
domain_name = socket.getfqdn("216.58.206.174")
print(domain_name)

# Get IP address from hostname
host_name = socket.gethostbyname("www.google.com")
print(host_name)

# Create socket object from an existing file descriptor
# -> Only Python 3+
s1 = socket.socket()
s2 = socket.fromfd(s1.fileno(), s1.family, s1.type)
print(s1)
print(s2)

