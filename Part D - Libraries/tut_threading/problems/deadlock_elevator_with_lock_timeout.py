import threading
import logging
import time

up = threading.Lock()
down = threading.Lock()
stop = threading.Lock()


def p1(name):

    up_check = up.acquire(timeout=1)
    time.sleep(0.3)
    logging.info('{name} pressed up'.format(name=name))

    stop_check = stop.acquire(timeout=1)
    time.sleep(0.3)
    logging.info('{name} pressed stop'.format(name=name))

    if stop_check:
        stop.release()

    if up_check:
        up.release()

    logging.info('Destination reached')


def p2(name):

    stop_check = stop.acquire(timeout=1)
    time.sleep(0.3)
    logging.info('{name} pressed stop'.format(name=name))

    up_check = up.acquire(timeout=2)
    time.sleep(0.3)
    logging.info('{name} pressed up'.format(name=name))

    if up_check:
        up.release()

    if stop_check:
        stop.release()

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