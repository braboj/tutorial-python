def outer_function():
    # This is the outer function scope

    def inner_function():
        # This is the inner function scope

        print('This is the inner function')

    return inner_function


# Call the inner function directly
outer_function()()

# Store the inner function object into a variable
func = outer_function()

# Now call the inner function using the variable
func()
print()
