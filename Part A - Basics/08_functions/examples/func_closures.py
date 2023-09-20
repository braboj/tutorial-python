def greet(message):

    def inner_function(name):

        # The message variable is stored in the inner function context
        return "{} {}".format(message, name)

    # Returns a closure (function object with `message` as part of the inner function context)
    return inner_function


# Store the closure function object into a variable
welcome = greet("Welcome")

# Use the concrete closure function object
print(welcome('Branko'))    # Welcome Branko
print(welcome('John'))      # Welcome John
