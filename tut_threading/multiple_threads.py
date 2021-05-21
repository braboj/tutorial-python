import time
import threading
import logging


def my_func(id):

    logging.info("func : Starting {id}".format(id=id))
    time.sleep(10)
    logging.info('func : Finishing {id}'.format(id=id))


if __name__ == "__main__":
    """
    """

    f = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=f,
        level=logging.INFO,
        datefmt="%H:%M:%S"
    )

    threads = list()
    for index in range(3):
        logging.info("Main : Create and start thread %d", index)
        x = threading.Thread(target=my_func, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main : Before joining thread %d", index)
        thread.join()
        logging.info("Main : Thread %d done", index)