import socket
import ssl
import sys

# ----------------------------------------------------------------------------
# USECASE 0001 : Client verifies server certificate
# ----------------------------------------------------------------------------

print(sys.path[0])
HOST = "172.20.11.13"
PORT = 443

# Later to be used to simulate error in certificate validation
HOST = socket.getaddrinfo(HOST, PORT)[0][4][0]
print(HOST)

# wrap socket to add SSL support
sock = socket.socket()

# create socket and connect to server
sock.connect((HOST, PORT))

# Should report error with CERT_REQUIRED, but ssl in Python 2.x doesn't verify the server certificate
sock = ssl.wrap_socket(sock,
                       cert_reqs=ssl.CERT_REQUIRED,
                       # file with root certificates
                       ca_certs="..\\cert\\cacert.pem"
                       )
