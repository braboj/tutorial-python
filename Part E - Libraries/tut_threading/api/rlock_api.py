# coding: utf-8
"""
A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread. Internally,
it uses the concepts of “owning thread” and “recursion level” in addition to the locked/unlocked state used by
primitive locks. In the locked state, some thread owns the lock; in the unlocked state, no thread owns it.

The acquiring can be nested so that only the final release changes the lock's state to unlocked.

"""

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
