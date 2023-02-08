# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.packets import *
from components.defines import *

import threading
import socket
import logging


class HvlpSession(threading.Thread):
    """ Hilscher Variable Protocol Length Session Class

    The session is a thread that works with a specific protocol version and handles the incoming
    packets from the client. The session is also responsible to forward incoming publish packets
    to all the subscribers of the topic in the publish packet.

    Args:
          broker        : Broker instance that created the session
          client        : Client connection
          name          : Thread name

    Attributes:
        self.broker     : Broker instance that created the session
        self.client     : Client connection
        self.register   : Reference to the broker register
        self.state      : Session state
        self.terminate  : Stop signal for all threads in the session
        self.log        : Logger instance
        self.lock       : Lock instance for shared resources
        self.stream_in  : Input byte stream

    """

    WAIT_CONNECT = 0
    CONNECTED = 1
    ERROR_NO_DATA = 10035

    def __init__(self, broker, client, name=""):
        super(HvlpSession, self).__init__(name=name)

        # Logging configuration
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

        # Connection
        self.broker = broker
        self.client = client

        # Session state management
        self.state = self.WAIT_CONNECT
        self.register = self.broker.register
        self.terminate = threading.Event()

        # Shared resources
        self.lock = threading.Lock()
        self.stream_in = b""

    ###############################################################################################

    def __on_subscribe(self, topics):
        """ Subscribe the client on subscribe request """

        self.register.append(topics=topics, client=self.client)
        self.log.debug(self.register)

    ###############################################################################################

    def __on_unsubscribe(self, topics):
        """ Unsubscribe the client on subscribe request """

        self.register.remove(topics=topics, client=self.client)
        self.log.debug(self.register)

    ###############################################################################################

    def __on_publish(self, packet):
        """ Forward publosh packets to the topic subscribers """

        # Get all subscribers and remove the publisher
        subscribers = self.register.get_subscribers(packet.topic)

        # Publish to all subscribers
        for subscriber in subscribers:

            # Skip the sender of the message
            if self.client == subscriber:
                continue

            # Send the message to the rest of the subscribers
            try:
                self.log.debug("PUBLISH to {0} with topic='{1}', data={2}".format(
                                subscriber.getpeername(),
                                packet.topic,
                                tuple(packet.data)
                            ))
                subscriber.sendall(packet.to_bytes())

            except socket.error:
                self.log.debug("Client not accessible, deleting fromt the register")
                self.register[packet.topic].remove(subscriber)

    ###############################################################################################

    def __handle_packet(self, packet):
        """ Handle the packet by calling the corresponding event handlers """

        self.log.debug("{0} from {1}".format(packet, self.client.getpeername()))

        # Handle subscribe packets
        if packet.id == SubscribePacket.ID:
            self.__on_subscribe(packet.topics)

        # Handle unsubscribe packets
        elif packet.id == UnsubscribePacket.ID:
            self.__on_unsubscribe(packet.topics)

        # Handle publish packets
        elif packet.id == PublishPacket.ID:
            self.__on_publish(packet)

        # Handle unknown packets
        else:
            self.log.debug("UNEXPECTED PACKET: {0}".format(packet))

    ###############################################################################################

    def __update_state(self, packet):
        """ Update the session state """

        # STATE: WAIT_CONNECT
        if self.state == self.WAIT_CONNECT:

            # Request to connect to the broker
            if packet.id == ConnectPacket.ID:
                self.log.debug('CONNECT from {0}'.format(self.client.getpeername()))
                self.state = self.CONNECTED

            # Ignore packets until the connect packet is detected
            else:
                self.log.debug("UNEXPECTED PACKET: {0}".format(packet))

        # STATE: CONNECTED
        elif self.state == self.CONNECTED:

            # Request to disconnect from the broker
            if packet.id == DisconnectPacket.ID:
                self.log.debug('DISCONNECT from {0}'.format(self.client.getpeername()))
                self.terminate.set()

            # Perform the required operations on other packets
            else:
                self.__handle_packet(packet)

    ###############################################################################################

    def __listen(self):
        """ Wait for new data and write it to the input stream """

        while not self.terminate.is_set():

            try:
                if len(self.stream_in) < STREAM_SIZE:
                    data = self.client.recv(BUFFER_SIZE)
                    with self.lock:
                        self.stream_in += data

            # Ingore errors when the recv call did not return data on time
            except socket.error as e:
                if e.errno != self.ERROR_NO_DATA:
                    self.stop()

    ###############################################################################################

    def run(self):
        """ Session activity required by threading.Thread on start()

         1. Register the current session
         2. Start the message sniffer
         3. While stop signal not active
             3.1. Copy the input buffer
             3.2. Parse a packet from the buffer
             3.3. Update the session state

        """

        self.log.debug("SESSION START")
        self.register.subscribe(self)

        # Start the data capture thread
        listener = threading.Thread(target=self.__listen)
        listener.start()

        while not self.terminate.is_set():
            try:
                with self.lock:
                    # Parse a packet from the stream
                    packet = Packet.from_bytes(self.stream_in)

                    # Remove the packet bytes from the stream
                    self.stream_in = self.stream_in[len(packet):]

                # Update the session state
                self.__update_state(packet)

            except HvlpParsingError:
                pass

        self.cleanup()
        self.log.debug("SESSION END")

    ###############################################################################################

    def stop(self):
        """ Stop the current thread """
        self.terminate.set()

    ###############################################################################################

    def cleanup(self):
        """ Close the client connection and remove the session from the register """

        try:
            # Close the client connection
            self.client.shutdown(socket.SHUT_RDWR)
            self.client.close()

            # Remove session from the register
            self.register.unsubscribe(self)

            # Show the register before
            self.log.debug("Register before : {0}".format(self.register.get_sessions()))

            # Remove the client connection from the registry
            for topic in self.register.keys():
                if self.client in self.register[topic]:
                    self.register[topic].remove(self.client)

            # Show the register after
            self.log.debug("Register after : {0}".format(self.register.get_sessions()))

        except socket.error:
            pass
