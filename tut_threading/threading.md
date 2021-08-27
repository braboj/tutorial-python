# THREADING TUTORIAL

## Table of Contents
* [Thread](#thread)
* [Queue](#queue)
* [Event](#event)
* [Lock](#lock)
* [RLock](#rlock)
* [Semaphore](#semaphore)
* [Condition](#resources)
* [Barrier](#barrier)


## Thread
__________________________________________________________________________________________________

### daemon
__________________________________________________________________________________________________

If non-daemon threads are used, the main thread has to wait for all its children threads to finish. However, using 
daemon all children threads will either completed or killed by the operating system when main thread exits.

Usecases:

1. Collecting statistics and performing the status monitoring tasks - Sending and receiving network heartbeats,
supplying the services to monitoring tools, and so on.

2. Performing asynchronous I/O tasks - You can create a queue of I/O requests, and set up a group of daemon threads
servicing these requests asynchronously.

3. Listening for incoming connections - daemon threads are very convenient in situations like this, because they let
you program a simple "forever" loop, rather than creating a setup that pays attention to exit requests from the main
thread.


    import threading
    import time
    import logging
    
    
    def daemon():
        logging.info('Starting')
        for i in range(10):
            logging.info(".")
            time.sleep(1)
        logging.info('Exiting')
    
    
    def non_daemon():
        logging.info('Starting')
        time.sleep(2)
        logging.info('Exiting')
    
    
    def main():
    
        logging.info('Starting')
    
        # Daemon task which will be killed before finishing execution (non-critical)
        d = threading.Thread(name='daemon', target=daemon)
        d.daemon = True
        d.start()
    
        # Main thread waiting for non-daemon task to finish (critical)
        t = threading.Thread(name="non-daemon", target=non_daemon)
        t.daemon = False
        t.start()
    
        logging.info('Exiting')
    
    
    # Configure logger
    log_format = '(%(threadName)-10s) %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    
    
    if __name__ == "__main__":
        main()
    
    # At this point the main program finishes. The daemon will be terminated too.


### start()
__________________________________________________________________________________________________

    import time
    import threading
    
    
    def my_func():
    
        print("func : Starting {id}".format(id=id))
        time.sleep(5)
        print('func : Finishing {id}'.format(id=id))
    
    
    if __name__ == "__main__":
    
        t = threading.Thread(target=my_func)
        t.start()

### join()
__________________________________________________________________________________________________

Waits for the target thread to finish its execution before the next statement of the inquiring thread.

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
    
        logging.info('main : End')
        t.join()


### currentThread()
__________________________________________________________________________________________________

Get the current thread running by the operating system. 

    import threading
    import logging
    import time
    
    
    def worker():
        logging.info("{0} {1}".format(threading.currentThread().getName(), 'Starting'))
        time.sleep(2)
        logging.info("{0} {1}".format(threading.currentThread().getName(), 'Exiting'))
    
    
    def my_service():
        logging.info("{0} {1}".format(threading.currentThread().getName(), 'Starting'))
        time.sleep(3)
        logging.info("{0} {1}".format(threading.currentThread().getName(), 'Exiting'))
    
    
    if __name__ == "__main__":
    
        f = "%(asctime)s: %(message)s"
        logging.basicConfig(format=f, level=logging.INFO, datefmt=b"%H:%M:%S")
    
        # Named service thread
        s = threading.Thread(name='my_service', target=my_service)
    
        # Named worker thread
        w1 = threading.Thread(name='worker', target=worker)
    
        # Start thread with default name
        w2 = threading.Thread(target=worker)
    
        w1.start()
        w2.start()
        s.start()


### enumerate()
__________________________________________________________________________________________________

Returns a list of all the threads started by the current program. 

    def worker():
        pause = random.randint(1,5)
        logging.info('sleeping %s', pause)
        time.sleep(pause)
        logging.info('ending')
        return
    
    
    def main():
        for i in range(3):
            t = threading.Thread(target=worker)
            t.setDaemon(True)
            t.start()
    
        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is main_thread:
                continue
            logging.info('joining %s', t.getName())
            t.join()
    
    
    if __name__ == "__main__":
    
        logging.basicConfig(level=logging.INFO, format='(%(threadName)-10s) %(message)s')
        main()


### local()
__________________________________________________________________________________________________

Defines a variable as local for the target thread.

    import random
    import threading
    import logging
    
    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-10s) %(message)s',
                        )
    
    
    def show_value(data):
        try:
            val = data.value
        except AttributeError:
            logging.debug('No value yet')
        else:
            logging.debug('value=%s', val)
    
    
    def worker(data):
        # Show local data for this thread before and after change
        show_value(data)
        data.value = random.randint(1, 100)
        show_value(data)
    
    
    # Define local data for each thread
    local_data = threading.local()
    
    # Show value in main thread before and after change
    show_value(local_data)
    local_data.value = 1000
    show_value(local_data)
    
    for i in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()


## Queue
__________________________________________________________________________________________________

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


## Timer
__________________________________________________________________________________________________
A Timer starts its work after a delay, and can be canceled at any point within that delay time period.

    import threading
    import logging
    import time
    
    
    def reset():
        logging.info("Reset")
    
    
    def test():
        logging.info("Test start")
        t = threading.Timer(interval=1, function=reset)
        t.start()
    
        for i in range(10):
            logging.info(".")
            time.sleep(1)
    
    
    if __name__ == "__main__":
        f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
        logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
    
        test()

## Event
__________________________________________________________________________________________________
    def worker(start):
        if start.wait(timeout=None):
            logging.info("Start")
            while start.is_set():
                logging.info("Working...")
                time.sleep(1)
            logging.info("End")
    
    
    def test():
        start = threading.Event()
        t = threading.Thread(target=worker, args=(start, ))
        t.start()
    
        for i in range(3):
            logging.info(".")
            time.sleep(1)
    
        start.set()
        time.sleep(3)
        start.clear()
    
    
    if __name__ == "__main__":
    
        f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
        logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
        test()

## Lock
__________________________________________________________________________________________________
Once a thread has acquired a lock, subsequent attempts to acquire it block, until it is released. Any thread may
release the acquired lock.

    import threading
    
    
    def test_01(lock):
        lock.release()
        print(lock.locked())
    
    
    def test_02(lock):
        result = lock.acquire(0)
        print(result)
    
    
    def main():
    
        ##############################################################################################
        # Test 01 : Another thread releases lock
        ##############################################################################################
        print("@test_01 : Another thread releases the lock")
        lock = threading.Lock()
        result = lock.acquire()
        print(result)
    
        test = threading.Thread(target=test_01, args=(lock, ))
        test.start()
        test.join()
    
        ##############################################################################################
        # Test 02 : Another thread tries to acquire with timeout (only Python 3+)
        ##############################################################################################
        print("@test_02 : Another thread tries to acquire the lock")
        lock = threading.Lock()
        result = lock.acquire()
        print(result)
    
        test = threading.Thread(target=test_02, args=(lock, ))
        test.start()
        test.join()
    
    
    if __name__ == "__main__":
        main()

## RLock
__________________________________________________________________________________________________
A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread. Internally,
it uses the concepts of “owning thread” and “recursion level” in addition to the locked/unlocked state used by
primitive locks. In the locked state, some thread owns the lock; in the unlocked state, no thread owns it.

The acquiring can be nested so that only the final release changes the lock's state to unlocked.


    import threading
    
    
    def test_01(lock):
        try:
            lock.release()
        except RuntimeError:
            print("RLock can be released only by the owner!")
    
    
    def test_02(lock):
        result = lock.acquire(blocking=False)
        if result:
            print("Locked by me")
        else:
            print("Already locked by another thread")
    
    
    def main():
    
        ##############################################################################################
        # Test 01 : Another thread releases lock (not allowed for RLock as it has an owner)
        ##############################################################################################
        print("@test_01")
        lock = threading.RLock()
        lock.acquire()
    
        test = threading.Thread(target=test_01, args=(lock, ))
        test.start()
        test.join()
    
        ##############################################################################################
        # Test 02 : Another thread allocates the lock (will block until it is released)
        ##############################################################################################
        print("@test_02")
        lock = threading.RLock()
        lock.acquire()
    
        test = threading.Thread(target=test_02, args=(lock, ))
        test.start()
        test.join()
    
        ##############################################################################################
        # Test 03 : The owner acquires the lock several times
        ##############################################################################################
        print("@test_03")
        lock = threading.RLock()
    
        # Lock several times
        lock.acquire()
        lock.acquire()
        lock.acquire()
    
        # First release (should still be locked)
        lock.release()
        test = threading.Thread(target=test_02, args=(lock, ))
        test.start()
        test.join()
    
        # Second release (should still be locked)
        lock.release()
        test = threading.Thread(target=test_02, args=(lock,))
        test.start()
        test.join()
    
        # Third release (should be free)
        lock.release()
        test = threading.Thread(target=test_02, args=(lock,))
        test.start()
        test.join()
    
    
    if __name__ == "__main__":
        main()


## Semaphore
__________________________________________________________________________________________________

Semaphore:
A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each
release() call. The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until
some other thread calls release().

BoundedSemaphore:
BoundedSemaphore works exactly like a semaphore except the number of release() operations cannot exceed
the number of acquire() operations.

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


## Condition
__________________________________________________________________________________________________

This class implements condition variable objects. A condition variable allows one or more threads to wait until
they are notified by another thread.

Example

    import threading
    import logging
    import time
    
    
    def consumer(condition):
        condition.acquire()
        logging.info("Waiting for notification")
        condition.wait()
        logging.info('Resource is available to consumer')
        condition.release()
    
    
    def producer(condition):
        condition.acquire()
        logging.info('Send notification and release resource')
        condition.notify_all()
        condition.release()
    
    
    def test():
    
        condition = threading.Condition()
        c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
        c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
        p = threading.Thread(name='p', target=producer, args=(condition,))
    
        c1.start()
        time.sleep(2)
    
        c2.start()
        time.sleep(2)
    
        p.start()
    
    
    if __name__ == "__main__":
    
        f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
        logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
        test()

Methods:

* acquire()
* release()
* wait()
* wait_for()
* notify()
* notify_all()

## Barrier
__________________________________________________________________________________________________
