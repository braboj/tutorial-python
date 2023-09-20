# encoding: utf-8
import socket

def run_client(message='Hello World!'):
    """
    Simple echo client which will connect to the echo server, send data and wait for the data to be sent back. After the
    echo is received the socket will be closed.
    """

    print("Client -> Server: '{0}'".format(message))


    # 1. Create socket object (AF_NET -> IPv4, SOCK_STREAM -> TCP)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Optionally the client can be bound to a specific adapter and port. If ommitted the operating system will take the
    # adapter with the highest priority and assign a port automatically
    client.bind(('127.0.0.1', 6969))

    # 3. Connect to the server port
    client.connect(('127.0.0.1', 503))

    # 4. Send some data
    client.send(message)

    # 5. Receive the response from the server
    response = client.recv(1024)
    print("Server -> Client: '{0}'".format(response))

    # 6. Close the connection
    client.close()

if __name__ == '__main__':
    run_client()