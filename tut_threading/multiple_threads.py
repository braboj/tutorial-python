import time
import threading
import logging


def my_func(id):

    logging.info(f"func : Starting {id}")
    time.sleep(10)
    logging.info(f'func : Finishing {id}')


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