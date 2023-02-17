# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.packets import *
from components.errors import *
from components.defines import *

import socket
import threading
import logging


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

        # Logging configuration
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

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

    def connect(self, payload=""):
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
            payload = payload.encode('utf-8')
            request = ConnectPacket(payload=payload).to_bytes()
            self.sock.sendall(request)

        except AttributeError:
            raise HvlpConnectionError

        # Socket related errors
        except socket.error:
            raise HvlpAlreadyConnected

    ###############################################################################################

    def disconnect(self, payload=""):
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
            payload = payload.encode('utf-8')
            request = DisconnectPacket(payload).to_bytes()
            self.sock.sendall(request)

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
        """ Save raw messages from the borker into the input buffer

        Args:
            stop     : Threading event to stop the listener loop

        Example:

            # Create the client object
            client = HvlpClient()

            # Create the stop event
            stop = threading.Event()

            # Start the listener thread
            listener = threading.Thread(target=client.listen, args=[stop, ])

        """

        while not stop.is_set():
            try:
                data = self.sock.recv(BUFFER_SIZE)
                while data:
                    packet = Packet.from_bytes(data)
                    self.on_packet(packet)
                    data = data[len(packet):]

            # Protocol related errors
            except HvlpError as e:
                self.log.error(e)

            # Connection related errors
            except (socket.error, AttributeError) as e:
                self.log.error(e)

            # Socket timed out in case it is non-blocking
            except socket.timeout:
                pass

    ###############################################################################################

    def on_packet(self, packet):
        """ Default packet handler that can be overriden by a custom application

        Args:
            packet     : Packet object

        Example:

            class MyHvlpClient(HvlpClient):

                def on_packet(self, packet):

                    if packet.id == PublishPacket.ID:
                        self.on_publish(packet)

                    elif packet.id == SomeCustomPacket.ID:
                        self.on_custom_packet(packet)

                    ...

        """

        self.log.info("{0} from {1}:{2}".format(packet, self.srv_addr, self.port))
