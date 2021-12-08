import time
import threading
import logging


class Database(object):
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self):
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

        logging.info(self.value)


if __name__ == "__main__":

    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=fmt,
        level=logging.INFO,
        datefmt="%H:%M:%S"
    )

    database = Database()
    logging.info("Testing update. Starting value is %d.", database.value)

    for i in range(2):
        t = threading.Thread(target=database.locked_update)
        t.start()

    logging.info("Testing update. Ending value is %d.", database.value)
