"""
Semaphore:
A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each
release() call. The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until
some other thread calls release().

BoundedSemaphore:
BoundedSemaphore works exactly like a semaphore except the number of release() operations cannot exceed
the number of acquire() operations.

"""

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )


class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()

        # Shared list for each worker to register
        self.active_workers = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active_workers.append(name)
            logging.debug('Running: %s', self.active_workers)

    def makeInactive(self, name):
        with self.lock:
            self.active_workers.remove(name)
            logging.debug('Running: %s', self.active_workers)


def worker(semaphore, pool):
    logging.debug('Waiting to join the pool')
    semaphore.acquire()
    name = threading.currentThread().getName()
    pool.makeActive(name)
    time.sleep(0.1)
    pool.makeInactive(name)
    semaphore.release()


# Maximum 2 workers allowed at a time
p = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(target=worker, name=str(i), args=(s, p))
    t.start()
