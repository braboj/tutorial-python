import time
import threading
import logging


def my_func(name):

    logging.info("func : Starting {0}".format(name))
    time.sleep(10)
    logging.info('func : Finishing {0}'.format(name))


if __name__ == "__main__":
    """
    If a program is running Threads that are not daemons, then the program 
    will wait for those threads to complete before it terminates. 
    
    18:33:04: main : Create thread
    18:33:04: main : Execute thread
    18:33:04: func : Starting myfunc
    18:33:04: main : End
    18:33:14: func : Finishing myfunc
    """

    f = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=f,
        level=logging.INFO,
        datefmt="%H:%M:%S"
    )

    logging.info('main : Create thread')
    t = threading.Thread(target=my_func, args=['myfunc'])

    logging.info('main : Starting thread')
    t.start()

    logging.info('main : End')