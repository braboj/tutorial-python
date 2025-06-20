# Lambda functions
# ------------------------------------------------------------------------------
# Lambda expressions provide a compact way to create anonymous functions.
# They consist of a parameter list, a colon and a single expression that becomes
# the return value. Because they are limited to one expression, lambdas are best
# suited for small operations.

"""
lambda [param1, param2, ..]: expression

Lambda functions are one-line functions which return an expression using
the pre-defined parameters param1, param2, ... paramN.

Lambda functions are normally used for quick operations on data,
most notably in combination with map, filter, reduce.

"""

# Define a list to iterate over
data_in = [1, 2, 3]

# Use a lambda function to square the input and then map the result to a list `data_out`
data_out = list(map(lambda x: x * x, data_in))

# Print the result
print(data_in, data_out)
