import threading
import logging
import time


def worker():
    logging.info("{0} {1}".format(threading.currentThread().getName(), 'Starting'))
    time.sleep(2)
    logging.info("{0} {1}".format(threading.currentThread().getName(), 'Exiting'))


def my_service():
    logging.info("{0} {1}".format(threading.currentThread().getName(), 'Starting'))
    time.sleep(3)
    logging.info("{0} {1}".format(threading.currentThread().getName(), 'Exiting'))


if __name__ == "__main__":

    f = "%(asctime)s: %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt=b"%H:%M:%S")

    # Named service thread
    s = threading.Thread(name='my_service', target=my_service)

    # Named worker thread
    w1 = threading.Thread(name='worker', target=worker)

    # Start thread with default name
    w2 = threading.Thread(target=worker)

    w1.start()
    w2.start()
    s.start()
