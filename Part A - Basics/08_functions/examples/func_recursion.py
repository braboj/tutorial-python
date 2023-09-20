def factorial(n):

    # Base case
    if n == 0:
        return 1

    # Recursive case
    else:
        return n * factorial(n - 1)


test_function = factorial(5)
print(test_function)