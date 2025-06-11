# Lambda function with nested conditionals
# -----------------------------------------------------------------------------
# This example defines a lambda expression that returns `1` when the input
# is greater than 10 or less than -10 and `0` otherwise.
z = lambda c: 1 if c > 10 else (1 if c < -10 else 0)
print(-11, -10, -1, 0, 1, 10, 11, sep='\t')
print(z(-11), z(-10), z(-1), z(0), z(1), z(10), z(11), sep='\t')
