import random
import os
import math
import threading

inside = 0
total = 0


def generate_points(iterations):

    i = 0
    n = 1
    for n in range(1, iterations + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        r = math.sqrt(x ** 2 + y ** 2)
        if r <= 1:
            i += 1

    global inside
    inside = i

    global total
    total = n


def calc_pi():
    pi = 4 * float(inside) / float(total)
    print(pi)


threads = []
for _ in range(os.cpu_count()):
    t = threading.Thread(target=generate_points, args=[10000, ])
    t.start()
calc_pi()