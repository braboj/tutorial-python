# Lambda function with recursion
# --------------------------------------------------------------------------------
# Demonstrates lambda function with recursion.

x = lambda a: a * x(a - 1) if a > 1 else 1
print(x(5))
