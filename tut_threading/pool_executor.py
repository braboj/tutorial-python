import time
import threading
import logging
import concurrent.futures


def my_func(id):

    logging.info(f"func : Starting {id}")
    time.sleep(10)
    logging.info(f'func : Finishing {id}')


if __name__ == "__main__":
    """
    """

    f = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=f,
        level=logging.INFO,
        datefmt="%H:%M:%S"
    )

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(my_func, range(3))
