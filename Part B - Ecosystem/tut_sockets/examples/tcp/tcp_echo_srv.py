# encoding: utf-8
import socket
import struct
import threading
import time


def srv():

    """
    Simple echo server which will wait for a new client to send data, receive data from the client, send the data back and
    then close the connection.
    """

    # 1. Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind socket to a specific address and service port
    sock.bind(('localhost', 503))

    # 3. Start listening on socket
    sock.listen(5)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))

    start = time.time()
    while True:

        if time.time() - start > 3:
            break

        print('.')
        time.sleep(1)

        # # 4. Blocks until client is connected
        # client, addr_info = sock.accept()
        #
        # # 5. Receive data
        # data = client.recv(1024)
        #
        # # 6. Send data
        # client.send(data)
        #
        # # 7. Close connection
        # client.close()

    sock.close()


t = threading.Thread(target=srv)
t.start()
t.join()