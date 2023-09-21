import threading
import time
import random
import logging


N = 10
produce_time = 0.1
consume_time = 0.2

items = threading.Semaphore(value=0)
buffer_lock = threading.Lock()
buffer = []


def produce_next_item():
    return random.randint(0, 100)


def add_to_buffer(portion):
    buffer.append(portion)


def remove_from_buffer():
    item = buffer[0]
    buffer.remove(item)
    return item


def producer():

    while True:

        # Produce the next item
        item = produce_next_item()
        time.sleep(produce_time)

        # Lock the buffer and add as a last item
        with buffer_lock:
            add_to_buffer(item)

        items.release()
        logging.info(items._value)


def consumer():

    while True:

        # Wait until the next item is produced
        items.acquire()

        # Lock the buffer and remove the last item
        with buffer_lock:
            item = remove_from_buffer()

        # logging.info(item)
        logging.info(items._value)
        time.sleep(consume_time)


def main():

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":

    # Configure logger
    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")

    # Start the program
    main()