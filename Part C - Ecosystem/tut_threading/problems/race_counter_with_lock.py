import threading
import time

"""
Solution 01: Use critical section primitives to access the shared state

Lock the access to the shared state by using synchronization primitives such 
as mutex or semaphore. It is critical to apply it on ALL read and write 
operations.

The local variables of a function are unique to each thread that runs the 
function.

"""


class BankAccount(object):

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def earn(self, delay=0):

        # Use local copy and time sleep to split the read-modify-write
        # process and delay to desynchronize the threads.

        with self.lock:
            local_copy = self.balance
            local_copy += 1
            time.sleep(delay)
            self.balance = local_copy

    def spend(self, delay=0):

        # Use local copy and time sleep to split the read-modify-write
        # process and delay to desynchronize the threads.

        with self.lock:
            local_copy = self.balance
            local_copy -= 1
            time.sleep(delay)
            self.balance = local_copy

    def get_balance(self):
        with self.lock:
            local_copy = self.balance

        return local_copy


def main(iterations):
    account = BankAccount()
    threads = []

    for _ in range(iterations):
        for _ in range(10):
            t1 = threading.Thread(target=account.earn, args=(0, ))
            t2 = threading.Thread(target=account.spend, args=(0.1, ))
            t1.start()
            t2.start()
            threads.append(t1)
            threads.append(t2)

        for t in threads:
            t.join()
            threads.remove(t)

        print("Expected = {0}, Obtained = {1}".format(0, account.get_balance()))


if __name__ == "__main__":
    main(5)
