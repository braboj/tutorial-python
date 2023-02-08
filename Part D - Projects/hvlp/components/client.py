# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.packets import *
from components.errors import *
from components.defines import *

import socket
import threading


class HvlpClient(threading.Thread):
    """Hilscher Variable Length Protocol Client

    The client sends requests to the broker and listens for publish packets.

    Args:
        srv_addr        : Broker IP address
        port            : Broker port

    Attributes:
        srv_addr        : Broker address
        port            : Broker port
        sock            : Client socket

    Examples:

        # Create a default client
        client = HvlpClient()

        # Open a TCP connection to the broker
        client.open()

        # Send a connect request
        client.connect()

        # Subscribe to topics 'a', 'b' and 'c'
        client.subscribe('a', 'b', 'c')

        # Unsubscribe from topic 'c'
        client.unsubscribe('c')

        # Publish to topic 'a'
        client.publish(topic='a', 1, 2, 3)

        # Disconnect from the broker
        client.disconnect()

        # CLose the TCP connection
        client.close()

    """

    def __init__(self, srv_addr='localhost', port=DEFAULT_PORT):
        super(HvlpClient, self).__init__()

        # Connection related attributes
        self.srv_addr = srv_addr
        self.port = port
        self.sock = None

        # Message queue
        self.lock = threading.Lock()
        self.stream_in = b""

    ###############################################################################################

    def open(self):
        """ Open a TCP socket connection"""

        try:

            # Open the TCP connection
            self.sock = socket.socket()
            self.sock.connect((self.srv_addr, self.port))

            # Configure the socket to be non-blocking
            self.sock.settimeout(1)

        # The broker is not up
        except socket.error:
            raise HvlpConnectionError

    ###############################################################################################

    def send(self, *data):
        """ Send raw data over the TCP connection

        Args:
            data    : Bytes as arguments

        Example:

            # Send a raw connect packet
            client.send(1, 0)

            # Send a raw subscribe packet with topic 'a'
            client.send(3, 2, 1, 0x61)

        """

        stream = []
        try:

            # Convert to bytes
            for element in data:
                stream.append(int(element))

            # Open the TCP connection
            self.sock.sendall(bytearray(stream))

        # Socket attribute missing or connection error
        except (AttributeError, socket.error):
            raise HvlpConnectionError

    ###############################################################################################

    def close(self):
        """ Close the TCP connection """

        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            self.sock = None

        # Socket attribute missing or connection error
        except (AttributeError, socket.error):
            raise HvlpConnectionError

    ###############################################################################################

    def connect(self, payload=b""):
        """ Send a connect request packet to the broker

        Args:
            payload    : Bytes as arguments

        Example:

            # Send a default connect request with no payload
            client.connect()

            # Send a connect packet with optional data in the payload section
            clint.connect('Branko')

        """

        try:

            # Send the connect packet to the broker
            request = ConnectPacket(payload=payload).to_bytes()
            self.sock.sendall(request)

        # Payload related errors
        except (LookupError, ValueError):
            raise HvlpPayloadFormatError

        # Socket related errors
        except socket.error:
            raise HvlpAlreadyConnected

    ###############################################################################################

    def disconnect(self, payload=b""):
        """ Send a connect request packet to the broker

        Args:
            payload    : Bytes as arguments

        Example:

            # Send a default connect request with no payload
            client.disconnect()

            # Send a connect packet with optional data in the payload section
            clint.disconnect('Branko')

         """

        try:

            # Send the packet
            request = DisconnectPacket(payload).to_bytes()
            self.sock.sendall(request)

        # Payload related errors
        except (LookupError, ValueError):
            raise HvlpPayloadFormatError

        # Socket related errors
        except (AttributeError, socket.error):
            raise HvlpConnectionError

    ###############################################################################################

    def subscribe(self, *topics):
        """ Send a subscribe request to the broker

        Args:
            topics    : Comma-separated topic names

        Example:

            # Send a subscribe packet for topics 'a', 'b' and 'c'
            client.subsribe('a', 'b', 'c')

        """

        if not topics:
            raise HvlpArgumentsError

        try:
            request = SubscribePacket(topics=topics).to_bytes()
            self.sock.sendall(request)

        # Payload related errors
        except (LookupError, ValueError):
            raise HvlpPayloadFormatError

        # Socket related errors
        except (AttributeError, socket.error):
            raise HvlpConnectionError

    ###############################################################################################

    def unsubscribe(self, *topics):
        """ Send a unsubscribe request to the broker

        Args:
            topics    : Comma-separated topic names

        Example:

            # Send a unsubscribe packet for topics 'a', 'b', 'c'
            client.unsubsribe('a', 'b', 'c')

        """

        if not topics:
            raise HvlpArgumentsError

        try:
            request = UnsubscribePacket(topics=topics).to_bytes()
            self.sock.sendall(request)

        # Socket related errors
        except (AttributeError, socket.error):
            raise HvlpConnectionError

    ###############################################################################################

    def publish(self, topic, *data):
        """ Send a publish request to the broker

        Args:
            topic    : The topic name
            data     : Comma-separated list of bytes (range 0..255)

        Example:

            # Send a publish packet with topic 'a' and the bytes 1 and 2
            client.publish('a', 1, 2)

        """

        if not (topic and data):
            raise HvlpArgumentsError

        try:

            # Convert to bytes
            data = [int(x) for x in data]

            request = PublishPacket(topic=topic, data=data).to_bytes()
            self.sock.sendall(request)

        # Bad payload format
        except ValueError:
            raise HvlpPayloadFormatError

        # Socket related errors
        except (AttributeError, socket.error):
            raise HvlpConnectionError

    ###############################################################################################

    def listen(self, stop):
        """ Save raw messages from the borker into the input buffer  """

        while not stop.is_set():
            try:

                if len(self.stream_in) < STREAM_SIZE:
                    data = self.sock.recv(BUFFER_SIZE)
                    with self.lock:
                        self.stream_in += data

            except socket.timeout:
                pass

            # Connection related errors
            except (socket.error, AttributeError):
                raise HvlpConnectionError


# ####################################################################################################
# #
# ####################################################################################################
#
# def producer():
#
#     test_client = HvlpClient()
#     test_client.open()
#     test_client.connect()
#     test_client.subscribe('a')
#
#     i = 0
#     while True:
#         test_client.publish('a', (i % 256))
#         time.sleep(1)
#         i += 1
#
#
# def consumer():
#
#     test_client = HvlpClient()
#
#     test_client.open()
#     test_client.connect()
#     test_client.subscribe('a')
#
#     stop = threading.Event()
#     t = threading.Thread(target=test_client.listen, args=(stop,))
#     t.start()
#
#     while True:
#         try:
#             packet = Packet.from_bytes(test_client.stream_in)
#             test_client.stream_in = test_client.stream_in[len(packet):]
#             print(packet)
#         except HvlpParsingError:
#             pass
#
#
# if __name__ == "__main__":
#
#     p = threading.Thread(target=producer)
#     p.start()
#
#     c = threading.Thread(target=consumer)
#     c.start()
