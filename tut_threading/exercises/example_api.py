from __future__ import print_function

import threading
import time


##############################################################################################

def process(period, lock, stop):

    while True:

        if stop.is_set():
            break

        time.sleep(period)

        # Context manager for lock
        # It will activate the lock, perform the operation and then deactivate it
        with lock:
            print(period, end=", ")


##############################################################################################

def main():

    # Pool for thread management
    pool = []

    # Event to stop all the worker threads
    stop_event = threading.Event()

    # Lock for the standart output
    print_lock = threading.Lock()

    # Start workers
    for i in range(1, 4):

        worker = threading.Thread(
            target=process,
            args=(i, print_lock, stop_event),
            # kwargs={'period': i, 'lock': print_lock, 'stop': stop_event}
        )
        worker.daemon = True
        worker.start()
        pool.append(worker)

    # Run program for a specific amount of time and then stop everything
    time_start = time.clock()
    while True:
        time_now = time.clock()
        delta = time_now - time_start
        if delta > 5:
            print("Sending STOP to all threads.")
            stop_event.set()
            break

    # Wait for workers to finish (relevant for daemon threads)
    for worker in pool:
        worker.join()

    # Check if threads are alive
    status = [x.is_alive() for x in pool]
    if True not in status:
        print("All threads terminated")


if __name__ == "__main__":
    main()