import logging
import threading

SENTINEL = None


class Pipeline(object):
    """
    Class to allow a single element pipeline between producer and consumer.
    """

    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self):
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release()
        return message

    def set_message(self, message):
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()


def producer(pipeline):
    for index in range(10):
        message = index
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message)

    # Send a sentinel message to the consumer to signal end of production
    pipeline.set_message(SENTINEL)


def consumer(pipeline):
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message()
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


if __name__ == "__main__":

    # Configure logger
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    # Create pipeline
    p = Pipeline()

    # Create producer and consumer threads
    t1 = threading.Thread(target=producer, args=(p,))
    t2 = threading.Thread(target=consumer, args=(p,))

    # Start the producer and consumer threads
    t1.start()
    t2.start()
