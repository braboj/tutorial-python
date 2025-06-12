# Lambda functions with multiple arguments
# --------------------------------------------------------------------------------
# Demonstrates lambda functions with multiple arguments.

# Multi-parameter lambda
x = lambda a, b, c, d, e: (a + b) * (c + d) / e
print(x(1, 2, 3, 4, 5))
