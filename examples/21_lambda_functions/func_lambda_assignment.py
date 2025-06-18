# Assigning a lambda expression to a variable
# --------------------------------------------------------------------------------
# Lambda expressions can be assigned to variables to create small, unnamed
# functions on the fly. Doing so lets you reuse the lambda just like a regular
# function object. This pattern is handy for callbacks or short computations.

nop = lambda: None
print(nop())
