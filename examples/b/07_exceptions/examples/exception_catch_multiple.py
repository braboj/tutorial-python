# Example: Catch Multiple Exceptions with a Single Except Block


from exception_hierarchy import *


def main():

    # Example 1: Handling all exceptions inherited from SocketError
    try:
        raise ConnectError('Connection failed', 100)

    except SocketError as e:
        print(e)

    # Example 2: Handling a group of exceptions with a single except block
    try:
        raise DisconnectError('Connection failed', 100)

    except (ConnectError, DataTransferError, DisconnectError) as e:
        print(e)


main()
