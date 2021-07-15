from __future__ import print_function

import socket
import ssl
import time

CLIENT_CIPHERS = (
    'ECDHE-RSA-AES256-GCM-SHA384'
)

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create SSL context
# context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Configure client certificate
context.load_cert_chain(certfile="m2mqtt_client.crt", keyfile="m2mqtt_client.key")
# context.load_default_certs(purpose=ssl.Purpose.SERVER_AUTH)
context.load_verify_locations("m2mqtt_ca.crt")
context.set_ciphers(CLIENT_CIPHERS)

# Configure client side options
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED
context.options |= ssl.OP_NO_TLSv1_1

# Encrypt socket
ssl_sock = context.wrap_socket(sock, do_handshake_on_connect=False)

# Connect using TLS socket and manual handshake
ssl_sock.connect(("172.20.10.114", 10023))
ssl_sock.do_handshake()

print(ssl_sock.cipher())
print(ssl_sock.getpeercert())

# Exchange encrypted data
for i in range(10):
    ssl_sock.send(b".")
    print(ssl_sock.recv(1))
    time.sleep(1)

sock = ssl_sock.unwrap()
sock.shutdown(socket.SHUT_RDWR)
sock.close()