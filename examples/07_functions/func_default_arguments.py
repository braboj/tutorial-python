# Default arguments in functions
# -----------------------------------------------------------------------------
# Each function can have default arguments, which are used if the caller does
# not provide a value for that argument.

def greet(name='Nemo', age=42):
    print("Hello, {0}! You are {1} years old.".format(name, age))


greet()
# Output: Hello, Nemo! You are 42 years old.
