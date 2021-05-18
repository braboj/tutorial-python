import time
import threading
import logging


def my_func(id):

    logging.info("func : Starting {id}".format(id=id))
    time.sleep(10)
    logging.info('func : Finishing {id}'.format(id=id))


if __name__ == "__main__":
    """
    Threads that are daemons, however, are just killed wherever they are when 
    the program is exiting. With join the daemon thread will not be killed 
    and the main program will wait for the thread termination.
    
    Output:
    18:46:54: main : Create thread
    18:46:54: main : Starting thread
    18:46:54: func : Starting 1
    18:46:54: main : End
    """

    f = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=f,
        level=logging.INFO,
        datefmt="%H:%M:%S"
    )

    logging.info('main : Create thread')
    t = threading.Thread(target=my_func, args=[1], daemon=True)

    logging.info('main : Starting thread')
    t.start()

    logging.info('main : End')
    t.join()