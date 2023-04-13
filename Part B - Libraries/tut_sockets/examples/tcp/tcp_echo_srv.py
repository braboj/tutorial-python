# encoding: utf-8
import socket
import struct
import time


def run_server(ip_addr='127.0.0.1', port=503):
    """
    Simple echo server that will wait for a new client to send a connect request, wait for data from the client and
    send the reversed data back to the client.
    """

    print('Server started on port {0}...'.format(port))

    # 1. Create the server socket object (AF_INET -> IPv4, SOCK_STREAM -> TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind the server socket to a specific address:port
    server.bind((ip_addr, port))

    # 3. Start listening (SYN packet from the client)
    server.listen(5)

    # 4. Optionally configure the server port (linger option)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))

    while True:

        # 5. Wait for client connections (Wait for SYN and perform handshake)
        session, addr_info = server.accept()

        # 6. Handshake successful, wait for data from the client
        message = session.recv(1024)

        # 7. Send data back to the client
        response = message[::-1]
        session.send(response)

        # 8. Close the connection (send FIN to the client)
        session.close()

        time.sleep(1)
        print('.')


if __name__ == '__main__':
    run_server()