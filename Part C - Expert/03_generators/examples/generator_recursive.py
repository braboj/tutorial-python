# Example: Recursive generator for Fibonacci numbers

def fibonacci(n):
    if n <= 0:
        return
    a, b = 0, 1
    yield a  # Yield the first Fibonacci number
    for _ in range(n - 1):
        a, b = b, a + b
        yield a


# Usage
n = 10  # Generate the first 10 Fibonacci numbers
for number in fibonacci(n):
    print(number)
