from __future__ import print_function

import pprint
import socket
import ssl


def run():

    server_socket = socket.socket()
    server_socket.bind(('172.20.10.114', 10023))
    server_socket.listen(5)

    while True:
        client_socket, fromaddr = server_socket.accept()
        client_socket = ssl.wrap_socket(
            client_socket,
            server_side=True,
            cert_reqs=ssl.CERT_NONE,
            ca_certs="..\\cert\\m2mqtt_ca.crt",
            certfile="..\\cert\\m2mqtt_srv.crt",
            keyfile="..\\cert\\m2mqtt_srv.key"
        )

        try:
            print(repr(client_socket.getpeername()))
            print(client_socket.cipher())
            print(pprint.pformat(client_socket.getpeercert()))

        finally:
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()


if __name__ == "__main__":
    run()
