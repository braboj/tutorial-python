# Using positional arguments
# ------------------------------------------------------------------------------
# Each value is matched to a parameter based on where it appears, so the order
# of the provided arguments matters. Positional parameters correspond directly
# to the order defined in the function signature. Mixing up the order can lead
# to incorrect results or errors.

def greet(name, age):
    print("Hello, {0}! You are {1} years old.".format(name, age))


# Calling the greet() function with positional arguments in the correct order
greet("Alice", 25)
# Output: Hello, Alice! You are 25 years old.

# Calling the greet() function with positional arguments incorrectly
greet(30, "Bob")
# Output: Hello, 30! You are Bob years old.
