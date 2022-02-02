# https://www.includehelp.com/python/threading-setprofile-method-with-example.aspx
# Python program to explain the use of
# setprofile()  method in Threading Module

import time
import threading


def trace_profile():
    print("Current thread's profile")
    print("Name:", str(threading.current_thread().getName()))
    print("Thread id:", threading.current_thread().ident)


def thread_1(i):
    time.sleep(5)
    threading.setprofile(trace_profile())
    print("Value by Thread-1:", i)
    print()


def thread_2(i):
    threading.setprofile(trace_profile())
    print("Value by Thread-2:", i)
    print()


def thread_3(i):
    time.sleep(4)
    threading.setprofile(trace_profile())
    print("Value by Thread-3:", i)
    print()


def thread_4(i):
    time.sleep(1)
    threading.setprofile(trace_profile())
    print("Value by Thread-4:", i)
    print()


# Creating sample threads
threading.setprofile(trace_profile())
print()

thread1 = threading.Thread(target=thread_1, args=(1,))
thread2 = threading.Thread(target=thread_2, args=(2,))
thread3 = threading.Thread(target=thread_3, args=(3,))
thread4 = threading.Thread(target=thread_4, args=(4,))

# Starting the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()