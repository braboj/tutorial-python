import threading
import time


##############################################################################
# Case 1 : Using function object as stop flag
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

        # Worker running
        time.sleep(10)

        # Stop worker using function object
        stop_threads = True
        t.join()

        print("Main thread stopped")


##############################################################################
# Case 2 :
##############################################################################

class ExitThreadCase2(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(ExitThreadCase2, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    def run(self):
        while True:
            print(".")
            time.sleep(1)

            if self._stop.is_set():
                print("Worker stopped.")
                break

    def stop(self):
        self._stop.set()

    @staticmethod
    def test():

        # Configure and start
        t = ExitThreadCase2()
        t.start()
        time.sleep(10)
        t.stop()
        t.join()
        print("Main thread stopped")


if __name__ == "__main__":
    ExitThreadCase2.test()