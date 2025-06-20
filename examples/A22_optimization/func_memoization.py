# Memoization with an inner function that caches results
# ------------------------------------------------------------------------------
# The inner ``memoized_fibonacci`` function stores each computed Fibonacci
# number in the ``cache`` dictionary. On subsequent calls with the same
# argument, the cached value is returned instead of recalculating it. This
# avoids redundant work and illustrates the principle of memoization.

# Explicit memoization using a dictionary
def fibonacci(n):
    cache = {}

    def memoized_fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
        cache[n] = result
        return result

    return memoized_fibonacci(n)


print(fibonacci(5))
print(fibonacci(10))


# Memoization using a decorator (the internal cache is a dictionary)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(10))
