import random
import math
import threading
import time
import os


class MonteCarloPi(object):

    def __init__(self, iterations=1000000):
        self.iterations = iterations
        self.i = 0
        self.n = 0

    def calc_pi(self):

        i = 0
        n = 0
        for n in range(1, self.iterations + 1):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            r = math.sqrt(x ** 2 + y ** 2)
            if r <= 1:
                i += 1

        self.i, self.n = i, n


def main():

    print("Number of CPUs", os.cpu_count())

    threads = []
    sim_objects = []
    for _ in range(6):

        sim = MonteCarloPi()
        t = threading.Thread(target=sim.calc_pi)

        threads.append(t)
        sim_objects.append(sim)

    start_time = time.time()
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    delay = end_time - start_time

    i = 0
    n = 0
    pi = 0
    for o in sim_objects:
        i += o.i
        n += o.n
        pi = 4 * float(i) / float(n)

    print("PI = {0:5f} | I = {1} / {2} | TIME = {3}".format(
        pi,
        i,
        n,
        delay
    ))


if __name__ == "__main__":
    main()