import threading
import logging
import time


def worker():
    logging.info('Starting')
    time.sleep(2)
    logging.info('Exiting')


def service():
    logging.info('Starting')
    time.sleep(3)
    logging.info('Exiting')


if __name__ == "__main__":

    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")

    w = threading.Thread(name='worker', target=worker)
    s = threading.Thread(name='service', target=service)

    w.start()
    s.start()
