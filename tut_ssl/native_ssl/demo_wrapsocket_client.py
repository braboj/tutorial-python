from __future__ import print_function

import socket
import ssl
import time
# from cryptography import x509

HOST = "172.20.10.114"
PORT = 10023

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)

# Create TLS socket
ssl_sock = ssl.wrap_socket(
    sock,
    cert_reqs=ssl.CERT_REQUIRED,
    do_handshake_on_connect=False,
    ca_certs="..\\..\\cert\\m2mqtt_ca.crt",
    certfile="..\\..\\cert\\m2mqtt_client.crt",
    keyfile="..\\..\\cert\\m2mqtt_client.key",
)
print(ssl_sock)

# Connect using TLS socket and manual handshake
ssl_sock.connect((HOST, PORT))
ssl_sock.do_handshake()

# Get cryptographic information
print(ssl_sock.getpeercert())
print(ssl_sock.cipher())
print(ssl_sock.compression())
print(ssl_sock.get_channel_binding())
print(ssl_sock.version())

# Exchange encrypted data
for i in range(10):
    ssl_sock.send(b".")
    print(ssl_sock.recv(1))
    time.sleep(1)

print(ssl_sock.unwrap())

# print(ssl_sock.context)
# Closing the SSLSocket will also close the underlying socket
# ssl_sock.close()
