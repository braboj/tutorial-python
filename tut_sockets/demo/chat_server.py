import socket
import select


class ChatServer(object):

    def __init__(self, port):

        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", port))
        self.sock.listen(5)

        self.descriptors = [self.sock]
        print('ChatServer started on port %s' % port)

    def run(self):

        while True:

            # Await an event on a readable socket descriptor
            (sread, swrite, sexc) = select.select(self.descriptors, [], [])

            # Iterate through the tagged read descriptors
            for sock in sread:

                # Received a connect to the server (listening) socket
                if sock == self.sock:
                    self.accept_new_connection()

                else:

                    # Received something on a client socket
                    data = sock.recv(100)

                    # Check to see if the peer socket closed
                    if data == '':
                        host, port = sock.getpeername()
                        data = 'Client left %s:%s' % (host, port)
                        self.broadcast_string(data, sock)
                        sock.close()
                        self.descriptors.remove(sock)

                    else:
                        host, port = sock.getpeername()
                        newstr = '[%s:%s] %s' % (host, port, data)
                        self.broadcast_string(newstr, sock)

    def accept_new_connection(self):
        newsock, (remhost, remport) = self.sock.accept()
        self.descriptors.append(newsock)

        newsock.send(b"You're connected to the Python chatserver\r\n")
        data = 'Client joined %s:%s' % (remhost, remport)
        self.broadcast_string(data, newsock)

    def broadcast_string(self, data, omit_sock):

        print(data)
        data = bytearray(data.encode('utf-8'))
        for sock in self.descriptors:
            if sock != self.sock and sock != omit_sock:
                sock.send(data)


if __name__ == "__main__":
    myServer = ChatServer(2626)
    myServer.run()
