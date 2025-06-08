def log(message):
    # This is the outer function with the decorator parameters

    # Place a breakpoint here
    print("> Call to log")

    def decorator(func):
        # The standard decorator function with the function as parameter

        # Place a breakpoint here
        print("> Call to decorator")

        def wrapper(*args, **kwargs):
            # This is the wrapper function

            # Place a breakpoint here
            print("> First call to wrapper")

            # This is the wrapper function
            print(message)

            # Return the function
            return func(*args, **kwargs)

        # Return the wrapper function
        return wrapper

    return decorator


def add(a, b):
    return a + b


@log(message="Hello World")
def sub(a, b):
    return a - b


# Decorate function withtout the "@" operator
add = log("Hello World")(add)
print(sub(1, 2))

# Let Python do the work for us
print(sub(1, 2))
