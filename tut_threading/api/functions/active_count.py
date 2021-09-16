import random
import threading
import time
import logging


def worker():
    pause = random.randint(1, 5)
    logging.info('sleeping %s', pause)
    time.sleep(pause)
    logging.info('ending')
    return


def main():

    COUNT = 5

    for i in range(COUNT):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    active = threading.active_count()
    logging.info("Active count {0}, expected {1} ".format(active, COUNT + 1))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='(%(threadName)-10s) %(message)s')
    main()
