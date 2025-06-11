# Demonstrates how functions receive arguments by their position
# -----------------------------------------------------------------------------
# Each value is matched to a parameter based on where it appears,
# so the order of the provided arguments matters.

def greet(name, age):
    print("Hello, {0}! You are {1} years old.".format(name, age))


# Calling the greet() function with positional arguments
greet("Alice", 25)
