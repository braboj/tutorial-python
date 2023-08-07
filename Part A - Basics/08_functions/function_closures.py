def greet():
    # Message variable
    text = "Welcome my dear!"

    def inner_function():
        # The text variable is captured
        return text

    # Returns the inner function
    return inner_function


# Execute greet to return the reference to the inner function
message = greet()

# Greet is no longer active, but the inner function has access to `text`
print(message())