# Lambda function with recursion
# ------------------------------------------------------------------------------
# Although lambdas are typically simple, they can also be used recursively.
# The expression here computes factorial by calling itself for successive
# decrements. Assigning the lambda to a variable is required so it can
# reference itself.

x = lambda a: a * x(a - 1) if a > 1 else 1
print(x(5))
