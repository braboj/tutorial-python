"""
The atexit module defines a single function to register cleanup functions. Functions thus registered are automatically
executed upon normal interpreter termination.

atexit runs these functions in the reverse order in which they were registered; if you register A, B, and C,
at interpreter termination time they will be run in the order C, B, A.

"""

import atexit
import datetime
import time
import sys, signal


def start():
    print("Start")


# TODO: Not working in debug
def worker():

    t1 = datetime.datetime.now()
    while True:
        t2 = datetime.datetime.now()
        if (t2 - t1).total_seconds() > 30:
            sys.exit()
        print("Hello at {0}".format(t2))
        time.sleep(0.1)


def end():
    print("End")


# Register in reverse execution order
atexit.register(end)
atexit.register(worker)
atexit.register(start)