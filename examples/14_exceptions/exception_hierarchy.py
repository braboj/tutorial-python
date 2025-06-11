# Custom Exception Hierarchy
# --------------------------------------------------------------------------------
# Defines a family of related custom exceptions and demonstrates raising each
# member of the hierarchy.

class SocketError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ConnectError(SocketError):

    def __init__(self, message, status):
        super(ConnectError, self).__init__(message)
        self.status = status

    def __str__(self):
        return '{}: {}'.format(self.status, self.message)


class DataTransferError(SocketError):

    def __init__(self, message, status, source, destination):
        super(DataTransferError, self).__init__(message)
        self.status = status
        self.source = source
        self.destination = destination

    def __str__(self):
        return '{}: {} from {} to {}'.format(self.status, self.message, self.source,
                                             self.destination)


class DisconnectError(SocketError):

    def __init__(self, message, status):
        super(DisconnectError, self).__init__(message)
        self.status = status

    def __str__(self):
        return '{}: {}'.format(self.status, self.message)


if __name__ == "__main__":

    try:
        raise ConnectError('Connection failed', 100)

    except ConnectError as e:
        print(e)

    try:
        raise DataTransferError(
            message='Data transfer failed',
            status=200,
            source='myhost',
            destination='remotehost',
        )

    except DataTransferError as e:
        print(e)

    try:
        raise DisconnectError('Connection failed', 300)

    except DisconnectError as e:
        print(e)
