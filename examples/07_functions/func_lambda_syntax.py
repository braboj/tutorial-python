# Lambda functions
# --------------------------------------------------------------------------------
# Demonstrates lambda functions.

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
