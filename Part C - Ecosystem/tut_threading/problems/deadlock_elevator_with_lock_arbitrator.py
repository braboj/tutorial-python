import random
import threading
import logging
import time

operate = threading.Lock()


def operator():

    time.sleep(0.3)
    logging.info('Operator pressed up')

    time.sleep(0.3)
    logging.info('Operator pressed stop')

    logging.info('Destination reached')


def p(name):
    with operate:
        logging.info('{name} wants the elevator'.format(name=name))
        wait_time = random.uniform(0, 1)
        time.sleep(wait_time)
        operator()


def main(n=10):

    persons = []

    # Add a person
    for i in range(1, n + 1):
        t = threading.Thread(target=p, args=[i])
        persons.append(t)

    # Fill the elevator
    for t in persons:
        t.start()

    # Remove a person
    for t in persons:
        t.join()


if __name__ == "__main__":

    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
    main(10)