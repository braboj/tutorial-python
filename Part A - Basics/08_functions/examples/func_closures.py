def greet(message):
    # Enclosing function

    def inner_function(name):
        # The message variable is stored in the inner function context
        return "{} {}".format(message, name)

    # Return a closure (a function object)
    return inner_function


# Store the closure function object into a variable
welcome = greet("Welcome")

# Use the concrete closure function object
print(welcome('Branko'))  # Welcome Branko

# Now call the inner function directly
print(greet("Hello")('John'))  # Hello John
