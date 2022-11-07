import random
import multiprocessing
from multiprocessing import Pool


def monte_carlo_pi_part(n):
    i = 0
    for i in range(n):
        x = random.random()
        y = random.random()

        # if it is within the unit circle
        if x * x + y * y <= 1:
            i = i + 1

    # return
    return i


if __name__ == '__main__':
    np = multiprocessing.cpu_count()
    n = 1000

    pool = Pool(processes=np)
    count = pool.map(monte_carlo_pi_part, range(n))
    print(count)

    print("Esitmated value of Pi:: ", 4 * sum(count) / n)