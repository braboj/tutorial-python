import socket, ssl
import pprint

def deal_with_client(connstream):

    data = connstream.read()
    # null data means the client is finished with us
    while data:
        if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            break
        data = connstream.read()
    # finished with client


def do_something(connstream, data):
    print(data)


def run():

    bindsocket = socket.socket()
    bindsocket.bind(('172.20.11.24', 10023))
    bindsocket.listen(5)

    while True:
        client, fromaddr = bindsocket.accept()
        client = ssl.wrap_socket(client,
                                 server_side=True,
                                 cert_reqs=ssl.CERT_REQUIRED,
                                 ca_certs="..\\cert\\m2mqtt_ca.crt",
                                 certfile="..\\cert\\m2mqtt_srv.crt",
                                 keyfile="..\\cert\\m2mqtt_srv.key")
        try:
            print repr(client.getpeername())
            print client.cipher()
            print pprint.pformat(client.getpeercert())

        finally:
            client.shutdown(socket.SHUT_RDWR)
            client.close()


if __name__ == "__main__":
    run()
