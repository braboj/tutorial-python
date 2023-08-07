def fibonacci(n):
    cache = {}

    def memoized_fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
        cache[n] = result
        return result

    return memoized_fibonacci(n)

print(fibonacci(5))
print(fibonacci(10))