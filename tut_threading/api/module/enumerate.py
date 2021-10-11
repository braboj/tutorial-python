import random
import threading
import time
import logging


def worker():
    pause = random.randint(1,5)
    logging.info('sleeping %s', pause)
    time.sleep(pause)
    logging.info('ending')
    return


def main():
    for i in range(3):
        t = threading.Thread(target=worker)
        t.setDaemon(True)
        t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        logging.info('joining %s', t.getName())
        t.join()


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, format='(%(threadName)-10s) %(message)s')
    main()