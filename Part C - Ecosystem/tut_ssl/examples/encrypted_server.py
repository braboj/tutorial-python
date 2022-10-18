from __future__ import print_function

import socket
import ssl

SERVER_CIPHERS = (
    # 'TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:'
    # 'TLS13-AES-128-GCM-SHA256:'
    # 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:'
    # 'ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:'
    # '!aNULL:!eNULL:!MD5:!DSS:!RC4:!3DES:'
    'ALL:'
    'COMPLEMENTOFALL:'
    # 'ADH-AES128-GCM-SHA256'
)


def run():

    # context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH, cafile="ca.crt")
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)

    # Configure certificates
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    context.load_default_certs(purpose=ssl.Purpose.CLIENT_AUTH)
    context.load_verify_locations(cafile="ca.crt")
    context.set_ciphers(SERVER_CIPHERS)

    # Configure server side options
    context.options |= ssl.OP_NO_TLSv1_1
    context.verify_mode = ssl.CERT_REQUIRED
    context.verify_flags = ssl.VERIFY_DEFAULT
    context.check_hostname = False

    # Create and bind server socket
    server_socket = socket.socket()
    server_socket.bind(('192.168.210.122', 4433))
    server_socket.listen(5)

    # Print info
    print(context.cert_store_stats())
    print(context.get_ca_certs())
    print(ssl.get_protocol_name(context.protocol))
    print(ssl.OPENSSL_VERSION)

    # Server loop
    while True:

        try:

            # Wait for new sockets
            connection, fromaddr = server_socket.accept()

            # Encrypt connection
            encrypted = context.wrap_socket(connection, server_side=True)

            # Wait for data and send it back to the client
            request = encrypted.recv(1024)
            encrypted.sendall(request)
            print(request)

            # Close encrypted connection
            sock = encrypted.unwrap()
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()

        except ssl.SSLError as e:
            print(e)


if __name__ == "__main__":
    run()
