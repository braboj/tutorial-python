"""
If non-daemon threads are used, the main thread has to keep track of them manually. However, using daemon thread the
main thread can completely forget about this task and this task will either complete or killed when main thread exits.

Usecases:

. Collecting statistics and performing the status monitoring tasks - Sending and receiving network heartbeats,
supplying the services to monitoring tools, and so on.

. Performing asynchronous I/O tasks - You can create a queue of I/O requests, and set up a group of daemon threads
servicing these requests asynchronously.

. Listening for incoming connections - daemon threads are very convenient in situations like this, because they let
you program a simple "forever" loop, rather than creating a setup that pays attention to exit requests from the main
thread.

"""

import threading
import time
import logging


def daemon():
    logging.info('Starting')
    for i in range(10):
        logging.info(".")
        time.sleep(1)
    logging.info('Exiting')


def non_daemon():
    logging.info('Starting')
    time.sleep(2)
    logging.info('Exiting')


def main():

    logging.info('Starting')

    # Daemon task which will be killed before finishing execution (non-critical)
    d = threading.Thread(name='daemon', target=daemon)
    d.daemon = True
    d.start()

    # Main thread waiting for non-daemon task to finish (critical)
    t = threading.Thread(name="non-daemon", target=non_daemon)
    t.daemon = False
    t.start()

    logging.info('Exiting')


# Configure logger
log_format = '(%(threadName)-10s) %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)


if __name__ == "__main__":
    main()

# At this point the main program finishes. The daemon will be terminated too.
