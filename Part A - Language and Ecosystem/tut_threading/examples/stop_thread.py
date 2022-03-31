import threading
import time
import ctypes


##############################################################################
# Case 1 : Function object as a stop flag
##############################################################################

class ExitThreadCase1(object):

    @staticmethod
    def worker(stop):
        while True:
            print(".")
            time.sleep(1)

            if stop():
                print("Worker stopped.")
                break

    @staticmethod
    def test():

        # Create worker object
        t = ExitThreadCase1()

        # Configure and start thread
        stop_threads = False
        t = threading.Thread(target=t.worker, args=(lambda: stop_threads,))
        t.start()

        # Worker is running
        time.sleep(3)

        # Stop worker using function object
        stop_threads = True

        # Wait for operating system to terminate worker
        t.join()

        # All test steps are done
        print("Main thread stopped")


##############################################################################
# Case 2 :  Polling of an event to stop the thread
##############################################################################

class ExitThreadCase2(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(ExitThreadCase2, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    def run(self):
        while not self._stop.is_set():
            print(".")
            time.sleep(1)

        print("Worker stopped.")

    def stop(self):
        self._stop.set()

    @staticmethod
    def test():
        # Create worker object and start worker
        t = ExitThreadCase2()
        t.start()

        # Worker is running
        time.sleep(3)

        # Stop worker
        t.stop()

        # Wait for operating system to terminate worker
        t.join()

        # All test steps are done
        print("Main thread stopped")


##############################################################################
# Case 3 : Polling of internal property to terminate the thread
##############################################################################

class ExitThreadCase3(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(ExitThreadCase3, self).__init__(*args, **kwargs)
        self._running = True

    def run(self):
        while self._running:
            print(".")
            time.sleep(1)

        print("Worker stopped.")

    def stop(self):
        self._running = False

    @staticmethod
    def test():

        # Create worker object and start worker
        t = ExitThreadCase3()
        t.start()

        # Worker is running
        time.sleep(3)

        # Stop worker
        t.stop()

        # Wait for operating system to terminate worker
        t.join()

        # All test steps are done
        print("Main thread stopped")


if __name__ == "__main__":
    ExitThreadCase1.test()
    ExitThreadCase2.test()
    ExitThreadCase3.test()
