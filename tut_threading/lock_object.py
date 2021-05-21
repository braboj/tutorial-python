"""
Once a thread has acquired a lock, subsequent attempts to acquire it block, until it is released. Any thread may
release the acquired lock.
"""

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
    print("@test_01")
    lock = threading.Lock()
    result = lock.acquire()
    print(result)

    test = threading.Thread(target=test_01, args=(lock, ))
    test.start()
    test.join()

    ##############################################################################################
    # Test 02 : Another thread tries to acquire with timeout (only Python 3+)
    ##############################################################################################
    print("@test_02")
    lock = threading.Lock()
    result = lock.acquire()
    print(result)

    test = threading.Thread(target=test_02, args=(lock, ))
    test.start()
    test.join()


if __name__ == "__main__":
    main()