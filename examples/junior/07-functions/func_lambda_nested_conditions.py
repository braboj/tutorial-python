# Example: Lambda function with nested conditional lambda

# The following example demonstrates junior lambda function with nested conditional lambda.
z = lambda c: 1 if c > 10 else (1 if c < -10 else 0)
print(-11, -10, -1, 0, 1, 10, 11, sep='\t')
print(z(-11), z(-10), z(-1), z(0), z(1), z(10), z(11), sep='\t')
