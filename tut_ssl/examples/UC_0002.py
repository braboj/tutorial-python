import socket, ssl, pprint


# ----------------------------------------------------------------------------
# USECASE 0002 : Client verifies mosquitto certificate
# ----------------------------------------------------------------------------

# TODO: Start mosquitto server here

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# require a certificate from the server
# ssl_sock = s
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="..\\cert\\m2mqtt_ca.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('172.20.10.69', 8884))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())

while True:
    pass

# note that closing the SSLSocket will also close the underlying socket
# ssl_sock.close()