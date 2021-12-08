"""
A Timer starts its work after a delay, and can be canceled at any point within that delay time period.
"""

import threading
import logging
import time


def reset():
    logging.info("Reset")


def test():
    logging.info("Test start")
    t = threading.Timer(interval=1, function=reset)
    t.start()

    for i in range(10):
        logging.info(".")
        time.sleep(1)


if __name__ == "__main__":
    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")

    test()