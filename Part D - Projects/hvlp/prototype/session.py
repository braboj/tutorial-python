class EchoSession(object):

    def __init__(self, connection, addr_info):
         self.connection = connection
         self.addr_info = addr_info

    def run(self, connection, addr_info):
        print('Connection from {0}'.format(addr_info))
        while True:
            data = connection.recv(1024)
            if data == 'stop':
                break
            connection.send(data)

        print('Connection closed')
        connection.close()

class ReverseEchoSession(object):

    def __init__(self, connection, addr_info):
        self.connection = connection
        self.addr_info = addr_info

    def run(self, connection, addr_info):
        print('Connection from {0}'.format(addr_info))
        while True:
            data = connection.recv(1024)
            reversed = data[::-1]
            if data:
                print(data)
            connection.send(reversed)