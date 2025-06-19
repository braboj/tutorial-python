# Original loop

import time, numpy


def stats(num_samples):

    def decorator(func):
        def wrapper(*args, **kwargs):

            print("=" * 80)
            print("Timings in seconds:", func.__name__)
            print("=" * 80)

            func.stats = []
            calc = 0
            for i in range(num_samples):
                start = time.time()
                calc = func(*args, **kwargs)
                end = time.time()
                func.stats.append(end - start)
                # print("Sample {} / Time taken: {}".format(i, end - start))

            print("Samples  :", len(func.stats))
            print("Mean     :", numpy.mean(func.stats))
            print("Stdev    :", numpy.std(func.stats))
            print("Min      :", min(func.stats))
            print("Max      :", max(func.stats))

            return calc

        return wrapper

    return decorator


SAMPLES = 10
ITERATIONS = int(1e6)


@stats(num_samples=SAMPLES)
def unoptimized_loop(iterations):

    steps = 0
    result = 0

    for _ in range(0, iterations, 1):

        steps += 1
        result += 1

    return result


@stats(num_samples=SAMPLES)
def optimized_loop(iterations):

    steps = 0
    result = 0

    for _ in range(0, iterations, 2):

        steps += 1
        result += 1
        result += 1

    return result


t1 = unoptimized_loop(ITERATIONS)
print('Output of unoptimized_loop: ', t1, '\n')

t2 = optimized_loop(ITERATIONS)
print('Output of optimized_loop: ', t2, '\n')
