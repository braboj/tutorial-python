def fibonacci_number(f0=0, f1=1, limit=1):

    # Initialize
    a, b = f0, f1

    # Loop
    while True:
        yield a

        # Solution 01
        # a, b = b, a + b

        # Solution 02
        b = a + b
        a = b - a


test = fibonacci_number(f0=2, f1=3)

for i in range(10):
    print(next(test))
