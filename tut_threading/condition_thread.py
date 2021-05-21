"""
This class implements condition variable objects. A condition variable allows one or more threads to wait until
they are notified by another thread.

Methods:
    acquire()
    release()
    wait()
    wait_for()
    notify()
    notify_all()

"""

import threading
import logging
import time


def consumer(condition):
    condition.acquire()
    logging.info("Waiting for notification")
    condition.wait()
    logging.info('Resource is available to consumer')
    condition.release()


def producer(condition):
    condition.acquire()
    logging.info('Send notification and release resource')
    condition.notify_all()
    condition.release()


def test():

    condition = threading.Condition()
    c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
    c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
    p = threading.Thread(name='p', target=producer, args=(condition,))

    c1.start()
    time.sleep(2)

    c2.start()
    time.sleep(2)

    p.start()


if __name__ == "__main__":

    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
    test()