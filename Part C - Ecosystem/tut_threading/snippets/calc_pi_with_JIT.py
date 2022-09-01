import random
import math
import threading
import time
import os
from numba import jit


class MonteCarloSim(object):

    def __init__(self, iterations=1000000):
        self.iterations = iterations

        self.i = 0
        self.n = 0
        self.pi = 0
        self.delay = 0

    def calc_pi(self):
        self.i, self.n, self.pi = self.calc_pi_static(self.iterations)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def calc_pi_static(iterations):

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


def main(N=1e6):

    print("Number of CPUs", os.cpu_count())

    threads = []
    sim_objects = []
    for _ in range(os.cpu_count()):

        sim = MonteCarloSim(iterations=int(N))
        t = threading.Thread(target=sim.calc_pi)

        threads.append(t)
        sim_objects.append(sim)

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
    for o in sim_objects:
        i += o.i
        n += o.n
        pi = 4 * float(i) / float(n)

    print("PI = {0:5f} | I = {1} / {2} | TIME = {3}".format
        (pi, i, n, delay)
    )


if __name__ == "__main__":
    main(N=1e6)
