import threading
import logging
import time


def worker():
    logging.info("{0} {1}".format(threading.current_thread().name, 'Starting'))
    time.sleep(2)
    logging.info("{0} {1}".format(threading.current_thread().name, 'Exiting'))


if __name__ == "__main__":

    # Configure logger
    f = "%(asctime)s: %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt=b"%H:%M:%S")

    # Start worker A
    w1 = threading.Thread(name="WORKER A", target=worker)
    w1.start()

    # Start worker B
    w2 = threading.Thread(name="WORKER B", target=worker)
    w2.start()
