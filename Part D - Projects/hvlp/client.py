# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from six.moves import input
from components.packets import *
from components.errors import *

import socket
import threading
import time

PROMPT = "> "

class HVLPClient(object):

    def __init__(self, srv_addr='localhost', port=65432):

        # Connection related attributes
        self.srv_addr = srv_addr
        self.port = port
        self.sock = None

        # Thread related attributes
        self.stop = threading.Event()
        self.stop.set()

    def on_open(self, args):
        """ Actions on a tcp open command """

        if len(args) == 1:
            raise HvlpArgumentsError

        elif len(args) == 2:
            self.srv_addr = args[0]
            self.port = int(args[1])

        try:
            self.sock = socket.socket()
            self.sock.connect((self.srv_addr, self.port))

            self.stop.clear()
            listener = threading.Thread(target=self.listen)
            listener.start()

        except socket.error:
            raise HvlpConnectionError

    def on_connect(self, args):
        """ Actions on a connect command """

        try:
            request = ConnectPacket(payload=args).to_bytes()
            self.sock.sendall(request)

        except socket.error:
            raise HvlpConnectionError


    def on_subscribe(self, args):
        """ Actions on a subscribe command """

        if not args:
            raise HvlpArgumentsError

        try:
            request = SubscribePacket(topics=args).to_bytes()
            self.sock.sendall(request)

        # Socket not initialized
        except AttributeError:
            raise HvlpConnectionError

        # Socket initialized but cannot send to the broker
        except socket.error:
            raise HvlpConnectionError

    def on_unsubscribe(self, args):
        """ Actions on a unsubscribe command """

        if not args:
            raise HvlpArgumentsError

        try:
            request = UnsubscribePacket(topics=args).to_bytes()
            self.sock.sendall(request)

        # Socket not initialized
        except AttributeError:
            raise HvlpConnectionError

        # Socket initialized but cannot send to the broker
        except socket.error:
            raise HvlpConnectionError

    def on_publish(self, args):
        """ Actions on a publish command """

        if not args:
            raise HvlpArgumentsError

        try:
            topic = args[0]
            data = [int(x) for x in args[1:]]

            request = PublishPacket(topic=topic, data=data).to_bytes()
            self.sock.sendall(request)

        # Socket not initialized
        except AttributeError:
            raise HvlpConnectionError

        # Socket initialized but cannot send to the broker
        except socket.error:
            raise HvlpConnectionError

    def on_disconnect(self, args):
        """ Actions on a disconnect command """

        try:
            request = DisconnectPacket(payload=args).to_bytes()
            self.sock.sendall(request)
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()

        # Socket not initialized
        except (socket.error, AttributeError):
            pass

        finally:
            self.stop.set()
            time.sleep(1)

    def on_quit(self, args):
        """ Actions on a quit command """

        self.stop.set()


    def listen(self):
        """ Wait for publish packets from the broker """

        self.sock.settimeout(1)
        while not self.stop.is_set():
            try:
                response = self.sock.recv(1024)
                print(Packet.from_bytes(response))
                print(PROMPT, end='')

            except socket.error:
                pass

        print("\nListener stopped")
        print(PROMPT, end='')

    def run(self):
        """" Run the client application """

        while True:
            try:
                # Get the user command and split it into tokens
                tokens = input(PROMPT).split()

                # Name the tokens
                command = tokens[0]
                args = tokens[1:]

                # Command actions
                if command == 'open':
                    self.on_open(args)

                elif command == 'connect':
                    self.on_connect(args)

                elif command == 'subscribe':
                    self.on_subscribe(args)

                elif command == 'unsubscribe':
                    self.on_unsubscribe(args)

                elif command == 'publish':
                    self.on_publish(args)

                elif command == 'disconnect':
                    self.on_disconnect(args)

                elif command == 'quit':
                   self.on_quit(args)
                   break

                else:
                    raise HvlpCommandError

            # Expected errors
            except HvlpError as e:
                print(e)

            # Unexpected errors
            except Exception as e:
                raise e

if __name__ == "__main__":
    client = HVLPClient()
    client.run()