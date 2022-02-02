from __future__ import print_function

import socket
import ssl


def run():

    server_socket = socket.socket()
    server_socket.bind(('172.20.10.114', 10023))
    server_socket.listen(5)

    while True:
        client, fromaddr = server_socket.accept()
        encrypted_socket = ssl.wrap_socket(
            client,
            server_side=True,
            cert_reqs=ssl.CERT_REQUIRED,
            ca_certs="..\\..\\cert\\ca.crt",
            certfile="..\\..\\cert\\server.crt",
            keyfile="..\\..\\cert\\server.key"
        )

        try:

            while True:
                data = encrypted_socket.recv(1)
                encrypted_socket.sendall(data)
                print(data)

        finally:
            encrypted_socket.close()


if __name__ == "__main__":
    run()
