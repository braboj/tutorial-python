import threading
import logging
import time

try:
    import Queue as queue
except ImportError:
    import queue


def worker(stream):
    while True:
        item = stream.get()
        logging.info(item)
        time.sleep(0.2)
        stream.task_done()


def process(data):

    stream = queue.Queue()

    # Start parallel workers to work on stream (increase workers to speed-up)
    for i in range(10):
         t = threading.Thread(target=worker, args=(stream, ))
         t.daemon = True
         t.start()

    # Read data (for example a file object)
    for item in data:
        stream.put(item)

    # Wait until all items in stream processed
    stream.join()


if __name__ == "__main__":

    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")

    data = range(100)
    process(data)