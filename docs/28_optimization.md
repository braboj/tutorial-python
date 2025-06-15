# Optimization

## Function Caching

```python

```

## Loop Fusion

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

## Loop With Invariant Code

```python
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
```

## Loop With List Comprehension

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

## Loop With Unrolling

```python
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
```

## Peephole Constant Folding

```python
# Example: Peephole Optimization - Constant Folding

def unoptimized_const():

    # Simulates the creation of unoptimized constants

    # Short strings
    a = "Hello"
    a = a + a + a

    # Tuples
    b = (1, 2)
    b = b * 3

    # Expressions
    c = 60
    c = c * 5

    return a, b, c


def peephole_const():

    # Python optimizes strings up to 4096 characters and tuples of length up to 256 elements
    # Varite the length of the string and tuple to see the difference.

    # Short strings
    a = "Hello" * 3

    # Tuples
    b = (1, 2) * 3

    # Expressions
    c = 60 * 60

    return a, b, c


print(unoptimized_const.__code__.co_consts)
# (None, 'Hello', 1, 2, 5, (10, 20, 30), 7)

print(peephole_const.__code__.co_consts)
# (None, 604800, 'HelloHelloHello', (1, 2, 1, 2, 1, 2))
```

## Peephole Constant Propagation

```python
""" Example: Peephole Optimization - Constant Propagation

Replace variables with their values if they are constant. This is done at compile time. It seems
that this 08-optimization is not implemented.

"""

def unoptimized():

    a = 1
    b = 2 * a

    return b


def peepholed():
    return 2


print(unoptimized.__code__.co_consts)
# (None, 1, 2)

print(peepholed.__code__.co_consts)
# (None, 2)
```

## Peephole Membership

```python
# Example: Peephole Optimization - Membership Test

def unoptimized_membership(name):

    # Simulates the creation an unoptimized membership test

    names = list()
    names.append("John")
    names.append("Doe")
    names.append("Jane")
    names.append("Smith")

    if name in names:
        pass


def peephole_membership(name):

    # Membership tests are optimized for lists and sets
    if name in ["John", "Doe", "Jane", "Smith"]:
        pass


print(unoptimized_membership.__code__.co_consts)
# (None, 'John', 'Doe', 'Jane', 'Smith')

print(peephole_membership.__code__.co_consts)
# (None, ('John', 'Doe', 'Jane', 'Smith'), 'Is junior member')
```

## String Interning

```python
# Example: String Interning

import sys

# Create two string literals with the same content
str1 = "hello"
str2 = "hello"

# Check if str1 and str2 reference the same object (identity check)
print("> Creating two string literals with the same content")
print("# {} is {}: {}\n".format(str1, str2, str1 is str2))

# Create junior non-literal strings with the same content
str3 = ""
str3 += "h"
str3 += "e"
str3 += "l"
str3 += "l"
str3 += "o"

# Check if str1 and str2 reference the same object (identity check)
print("> Create junior non-literal string with the same content")
print("# {} is {}: {}\n".format(str1, str3, str1 is str3))

# Intern the string referenced by str3
str3 = sys.intern(str3)

# Check if str1 and str3 reference the same object (identity check)
print("> Intern the non-literal string")
print("# {} is {}: {}\n".format(str1, str3, str1 is str3))
```

## Use Arrays

```python

```

## Use Comprehension

```python

```

## Use Jit Compilers

```python

```
