# Example: Loop Optimization with by moving invariant code out of the loop


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

    # Sums and multiplies by 2

    num = 1
    result = 0
    while num < iterations:
        num += 1
        result = num * 2

    return result


@stats(num_samples=SAMPLES)
def optimized_loop(iterations):

    # Uses the fact that (1*2 + 2*2 + 3*2 + ... + n*2) = 2 * (1 + 2 + 3 + ... + n)

    num = 1
    factor = 2
    while num < iterations:
        num += 1

    return num * factor


t1 = unoptimized_loop(ITERATIONS)
print('-> Output:', t1)

t2 = optimized_loop(ITERATIONS)
print('-> Output:', t2)