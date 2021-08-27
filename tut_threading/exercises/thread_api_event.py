import threading
import logging
import time


def worker(start):
    if start.wait(timeout=None):
        logging.info("Start")
        while start.is_set():
            logging.info("Working...")
            time.sleep(1)
        logging.info("End")


def test():
    start = threading.Event()
    t = threading.Thread(target=worker, args=(start, ))
    t.start()

    for i in range(3):
        logging.info(".")
        time.sleep(1)

    start.set()
    time.sleep(3)
    start.clear()


if __name__ == "__main__":

    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
    test()