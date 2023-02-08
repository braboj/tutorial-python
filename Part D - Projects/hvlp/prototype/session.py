class EchoSession(object):

    def __init__(self, connection, addr_info):
        self.connection = connection
        self.addr_info = addr_info

    @staticmethod
    def run(connection, addr_info):
        print('Connection from {0}'.format(addr_info))
        while True:
            data = connection.recv(1024)
            connection.send(data)
            print(data, len(data))


class ReverseEchoSession(object):

    def __init__(self, connection, addr_info):
        self.connection = connection
        self.addr_info = addr_info

    @staticmethod
    def run(connection, addr_info):
        print('Connection from {0}'.format(addr_info))
        while True:
            data = connection.recv(1024)
            reverse = data[::-1]
            if data:
                print(data)
            connection.send(reverse)
