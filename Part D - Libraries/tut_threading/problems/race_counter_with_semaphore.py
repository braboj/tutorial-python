import threading
import time


class BankAccount(object):

    def __init__(self):
        self.balance = 0
        self.critical = threading.Semaphore(value=1)

    def earn(self, delay=0):

        # Use local copy and time sleep to split the read-modify-write
        # process and delay to desynchronize the threads.

        with self.critical:
            local_copy = self.balance
            local_copy += 1
            time.sleep(delay)
            self.balance = local_copy

    def spend(self, delay=0):

        # Use local copy and time sleep to split the read-modify-write
        # process and delay to desynchronize the threads.

        with self.critical:
            local_copy = self.balance
            local_copy -= 1
            time.sleep(delay)
            self.balance = local_copy

    def get_balance(self):
        with self.critical:
            local_copy = self.balance

        return local_copy


def main(iterations=1, workers_per_iteration=10):

    account = BankAccount()
    threads = []

    for _ in range(iterations):
        for _ in range(workers_per_iteration):
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
    main(iterations=5, workers_per_iteration=10)
