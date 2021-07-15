from __future__ import print_function

import socket
import ssl

print(ssl.OP_NO_TICKET)

SERVER_CIPHERS = (
    'TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:'
    'TLS13-AES-128-GCM-SHA256:'
    'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:'
    'ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:'
    '!aNULL:!eNULL:!MD5:!DSS:!RC4:!3DES'
)


def notify(ssl_sock, server_name, context):
    print("Hello from client")


def run():

    # context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH, cafile="m2mqtt_ca.crt")
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)

    # Configure certificates
    context.load_cert_chain(certfile="m2mqtt_srv.crt", keyfile="m2mqtt_srv.key")
    # context.load_default_certs(purpose=ssl.Purpose.CLIENT_AUTH)
    context.load_verify_locations(cafile="m2mqtt_ca.crt")
    context.set_ciphers(SERVER_CIPHERS)
    context.set_servername_callback(notify)

    # Print some context info
    print(context.cert_store_stats())
    print(context.get_ca_certs())

    # Configure server side options
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED
    context.verify_flags = ssl.VERIFY_DEFAULT
    context.options |= ssl.OP_NO_TLSv1_1

    # Print some useful information
    print(ssl.get_protocol_name(context.protocol))
    print(ssl.OPENSSL_VERSION)
    print(ssl.HAS_TLSv1_3)

    # Create and bind server socket
    server_socket = socket.socket()
    server_socket.bind(('172.20.10.114', 10023))
    server_socket.listen(5)

    # Server loop
    while True:

        # Wait for new sockets
        connection, fromaddr = server_socket.accept()

        # Encrypt socket
        encrypted_connection = context.wrap_socket(connection, server_side=True)

        try:

            # Wait for data and send it back to the client
            while True:
                data = encrypted_connection.recv(1)
                encrypted_connection.sendall(data)

        finally:
            encrypted_connection.shutdown(socket.SHUT_RDWR)
            encrypted_connection.close()


if __name__ == "__main__":
    run()
