# Recursive functions in Python
# ------------------------------------------------------------------------------
# A recursive function repeatedly calls itself with a simpler version of the
# original problem. Each call works toward a base case that stops the recursion.
# This technique is often used for tasks that can be defined in terms of similar
# subproblems.

def factorial(n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    else:
        return n * factorial(n - 1)


test_function = factorial(5)
print(test_function)
