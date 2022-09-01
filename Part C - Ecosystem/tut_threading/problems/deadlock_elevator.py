import threading
import logging
import time

up = threading.Lock()
down = threading.Lock()
stop = threading.Lock()


def p1(name):

    up.acquire()
    time.sleep(0.3)
    logging.info('{name} pressed up'.format(name=name))

    stop.acquire()
    time.sleep(0.3)
    logging.info('{name} pressed stop'.format(name=name))

    stop.release()
    up.release()

    logging.info('Destination reached')


def p2(name):

    stop.acquire()
    time.sleep(0.3)
    logging.info('{name} pressed stop'.format(name=name))

    up.acquire()
    time.sleep(0.3)
    logging.info('{name} pressed up'.format(name=name))

    stop.release()
    up.release()

    logging.info('Destination reached')


if __name__ == "__main__":

    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")

    t1 = threading.Thread(target=p1, args=['Branko', ])
    t2 = threading.Thread(target=p2, args=['Mitko', ])

    t1.start()
    t2.start()

    t1.join()
    t2.join()