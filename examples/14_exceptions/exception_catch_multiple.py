# Grouped Exception Handling
# --------------------------------------------------------------------------------
# Illustrates catching different members of an exception hierarchy with one
# except block.


from exception_hierarchy import *


def main():

    # Example 1: Handling all exceptions inherited from SocketError
    try:
        raise ConnectError('Connection failed', 100)

    except SocketError as e:
        print(e)

    # Example 2: Handling junior group of exceptions with junior single except block
    try:
        raise DisconnectError('Connection failed', 100)

    except (ConnectError, DataTransferError, DisconnectError) as e:
        print(e)


main()
