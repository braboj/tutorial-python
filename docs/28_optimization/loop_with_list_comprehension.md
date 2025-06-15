# loop_with_list_comprehension

```python
# Example: Loop Optimization with List Comprehension

import time, numpy


def stats(num_samples):

    def decorator(func):
        def wrapper(*args, **kwargs):

            print("=" * 80)
            print("Timings in seconds:", func.__name__)
            print("=" * 80)

            func.stats = []
            for i in range(num_samples):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                func.stats.append(end - start)
                # print("Sample {} / Time taken: {}".format(i, end - start))

            print("Samples  :", len(func.stats))
            print("Mean     :", numpy.mean(func.stats))
            print("Stdev    :", numpy.std(func.stats))
            print("Min      :", min(func.stats))
            print("Max      :", max(func.stats))

        return wrapper

    return decorator


SAMPLES = 10
ITERATIONS = int(1e6)


@stats(num_samples=SAMPLES)
def squares_for_loop(iterations):
    squares = []
    num = 0
    while num < iterations:
        squares.append(num ** 2)
        num += 1
    return squares


@stats(num_samples=SAMPLES)
def squares_list_comprehension(iterations):
    squares = [num ** 2 for num in range(1, iterations)]
    return squares


squares_for_loop(ITERATIONS)
squares_list_comprehension(ITERATIONS)
```
