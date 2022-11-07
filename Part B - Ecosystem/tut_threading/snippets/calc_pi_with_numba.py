import random
import math
import threading
import time
import os
from numba import jit


class CalcObject(object):

    def __init__(self, iterations=1000000):
        self.iterations = iterations

        self.i = 0
        self.n = 0
        self.pi = 0
        self.delay = 0

    def generate_points(self):
        self.i, self.n, self.pi = self.generate_points_static(self.iterations)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def generate_points_static(iterations):

        i = 0
        n = 0
        for n in range(1, iterations + 1):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            r = math.sqrt(x ** 2 + y ** 2)
            if r <= 1:
                i += 1

        pi = 4 * (i / n)
        return i, n, pi


def main():

    print("Number of CPUs", os.cpu_count())

    threads = []
    calc_objects = []
    for _ in range(os.cpu_count()):

        calc = CalcObject()
        t = threading.Thread(target=calc.generate_points)

        threads.append(t)
        calc_objects.append(calc)

    time_start = time.time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    time_end = time.time()
    delay = time_end - time_start

    i = 0
    n = 0
    pi = 0
    for o in calc_objects:
        i += o.i
        n += o.n
        pi = 4 * float(i) / float(n)

    print("PI = {0:5f} | I = {1} / {2} | TIME = {3}".format
        (pi, i, n, delay)
    )


if __name__ == "__main__":
    main()
