# encoding: utf-8
import socket
import struct
import time


def run_server(ip_addr='127.0.0.1', port=503):
    """
    Simple echo server that will wait for a new client to send a connect request, wait for data from the client and
    send the data received back to the client.
    """

    print('Server started on port {0}...'.format(port))

    # 1. Create the server socket object (AF_INET -> IPv4, SOCK_STREAM -> TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind the server socket to a specific address and service port
    server.bind((ip_addr, port))

    # 3. Start listening on socket
    server.listen(5)

    # 4. Optionally configure the server port (linger option)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))

    while True:

        # 5. The server waits until the remote client tries to connect to the server. This step represents the TCP
        # 3-way handshake. If the handshake is successful a local copy of the client socket is returned.
        client, addr_info = server.accept()

        # 6. Wait for data from the client
        message = client.recv(1024)

        # 7. Send data back to the client
        response = message[::-1]
        client.send(response)

        # 8. Close the client connection
        client.close()

        # Poll frequence
        time.sleep(1)

        # Print some debug info
        print('.')


if __name__ == '__main__':
    run_server()