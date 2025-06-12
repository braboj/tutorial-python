# Calling functions with keyword arguments
# --------------------------------------------------------------------------------
# Describe how naming parameters improves readability and allows optional
# argument ordering.

def greet(name, age):
    print("Hello, {0}! You are {1} years old.".format(name, age))


# Calling the greet() function with named arguments
greet(name="Alice", age=25)
