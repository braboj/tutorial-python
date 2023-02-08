# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.client import HvlpClient
from components.errors import *
from six.moves import input

import sys
import threading


class HvlpClientApp(HvlpClient):

    PROMPT = "> "

    def __init__(self, srv_addr, port):
        super(HvlpClientApp, self).__init__(srv_addr=srv_addr, port=port)

        self.packets_in = []
        self.lock = threading.Lock()
        self.terminate = threading.Event()
        self.listener = None

    ###############################################################################################

    def config(self, ip, port):
        """ Configure the server address and port """

        try:
            self.srv_addr = ip
            self.port = int(port)

        except Exception:
            raise HvlpArgumentsError

    ###############################################################################################

    def stop(self):
        """ Stop all the threads """
        self.terminate.set()

    ###############################################################################################

    def quit(self):
        """ Terminate all threads and quit the program """

        self.terminate.set()
        self.listener.join()

    ###############################################################################################

    def wait(self):
        """ Wait for user input """

        # Split the command line into tokens
        try:
            self.show(self.PROMPT, end='')
            line = input()
            tokens = line.split()
            command = tokens[0]
            args = tokens[1:]

        except BaseException:
            raise HvlpCommandError

        return command, args

    ###############################################################################################

    def show(self, *args, **kwargs):
        """ Thread safe print """

        with self.lock:
            print(*args, **kwargs)

    ###############################################################################################

    def help(self, command=""):
        """ Display a help message """

        help_string = """

        -------------------------------------------------------------------------------------------
        | Command         | Description                               | Example
        -------------------------------------------------------------------------------------------
        | connect         | Connect the client to the server          | connect
        | subscribe       | Subscribe to a topic                      | subscribe test
        | unsubscribe     | Unsubscribe from a topic                  | unsubscribe test
        | publish         | Publish to a topic with data as bytes     | publish test 1 255
        | disconnect      | Disconnect from the server and exit       | disconnect
        | config          | Configure the connection to the broker    | config 127.0.0.1 65432
        | open            | Open a new TCP connection                 | open
        | send            | Send a raw TCP packet                     | send 1 0
        | close           | Close the TCP connection                  | close
        | sniffer         | Start or stop the sniffer manually        | sniffer start | stop
        | help            | Display the current help screen           | help or help <cmd>
        | quit            | Stop all threads and quit the program     | quit
        """

        if command:
            help_string = getattr(self, command).__doc__

        self.show(help_string)

    ###############################################################################################

    def sniffer(self, state=""):
        """ Start a sniiffer thread to capture packets from the broker """

        try:
            if state == "start":

                # Stop the active listener
                if self.listener:
                    self.terminate.set()
                    self.listener.join()

                # Activate the new listener
                self.listener = threading.Thread(target=self.listen)
                self.listener.start()

            elif state == "stop":

                # Stop the active listener
                self.terminate.set()
                self.listener.join()

            else:
                if self.listener:
                    self.show("Listener is {0}".format(self.listener.is_alive()))
                else:
                    self.show("Listener not started yet")

        except BaseException as e:
            self.show(e)

    ###############################################################################################

    def on_publish(self, packet):
        """ Event handler for PUBLISH packets """

        self.show("[@EVENT]: {0}:{1} sent {2}".format(self.srv_addr, self.port, packet))

    ###############################################################################################

    def run(self):
        """" Run the client application """

        print("HVLP Client started ...")

        try:

            while True:
                try:
                    # Parse the command line
                    command, args = self.wait()

                    # Execute the desired action
                    if command == 'connect':
                        self.connect(*args)

                    elif command == 'subscribe':
                        self.subscribe(*args)

                    elif command == 'unsubscribe':
                        self.unsubscribe(*args)

                    elif command == 'publish':
                        self.publish(*args)

                    elif command == 'disconnect':
                        self.disconnect(*args)

                    elif command == 'config':
                        self.config(*args)

                    elif command == 'open':
                        self.open()

                    elif command == 'close':
                        self.close()

                    elif command == 'sniffer':
                        self.sniffer(*args)

                    elif command == 'send':
                        self.send(*args)

                    elif command == 'help':
                        self.help(*args)

                    elif command == 'quit':
                        self.quit()
                        break

                    else:
                        raise HvlpCommandError

                # Expected errors
                except HvlpError as e:
                    self.show(e)

        # User interrupt
        except KeyboardInterrupt:
            self.stop()

        # Unknown exceptions
        except Exception as e:
            self.show(e)

        # Cleanup
        finally:
            self.stop()
            self.show("Client exit...")


def main(server_addr='localhost', port=65432):

    # TODO: Enhance broker to allow configuration form the command line or configuration file

    client = HvlpClientApp(srv_addr=server_addr, port=int(port))
    client.run()


if __name__ == "__main__":
    main(*sys.argv[1:])
