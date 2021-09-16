import time
import threading
import logging


def my_func(id):

    logging.info("func : Starting {id}".format(id=id))
    time.sleep(5)
    logging.info('func : Finishing {id}'.format(id=id))


if __name__ == "__main__":

    f = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=f,
        level=logging.INFO,
        datefmt="%H:%M:%S"
    )

    logging.info('main : Create thread')
    t = threading.Thread(target=my_func, args=[1])
    t.daemon = True

    logging.info('main : Starting thread')
    t.start()

    logging.info("Waiting for my_func to finish...")
    t.join()
    logging.info('main : End')