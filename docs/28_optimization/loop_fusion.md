# loop_fusion

```python
# Original code with two separate loops

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

    array_a = [i for i in range(iterations)]
    array_b = [i * 2 for i in range(iterations)]

    sum_a = 0
    i = 0
    while i < iterations:
        sum_a += array_a[i]
        i += 1

    sum_b = 0
    j = 0
    while j < iterations:
        sum_b += array_b[j]
        j += 1

    return sum_a, sum_b


@stats(num_samples=SAMPLES)
def optimized_loop(iterations):

    array_a = [i for i in range(iterations)]
    array_b = [i * 2 for i in range(iterations)]

    sum_a = 0
    sum_b = 0
    i = 0
    while i < iterations:
        sum_a += array_a[i]
        sum_b += array_b[i]
        i += 1

    return sum_a, sum_b


t1 = unoptimized_loop(ITERATIONS)
print('Output of unoptimized loop: ', t1, '\n')

t2 = optimized_loop(ITERATIONS)
print('Output of optimized loop: ', t2, '\n')
```
