import threading
import time


class BankAccount(object):

    def __init__(self):
        self.balance = 0

    def earn(self, delay=0):

        # Use local copy and time sleep to de-synchronize the threads
        # and simulate a racing condition.

        local_copy = self.balance                   # READ
        local_copy += 1                             # MODIFY
        time.sleep(delay)
        self.balance = local_copy                   # WRITE

    def spend(self, delay=0):

        # Use local copy and time sleep to de-synchronize the threads
        # and simulate a racing condition.

        local_copy = self.balance                   # READ
        local_copy -= 1                             # MODIFY
        time.sleep(delay)
        self.balance = local_copy                   # WRITE

    def get_balance(self):
        return self.balance


def main(iterations):

    account = BankAccount()
    threads = []

    for _ in range(iterations):
        for _ in range(10):
            t1 = threading.Thread(target=account.earn, args=(0, ))
            t2 = threading.Thread(target=account.spend, args=(0.1,))
            t1.start()
            t2.start()
            threads.append(t1)
            threads.append(t2)

        for t in threads:
            threads.remove(t)
            t.join()

        print("Expected = {0}, Obtained = {1}".format(0, account.get_balance()))


if __name__ == "__main__":
    main(10)
