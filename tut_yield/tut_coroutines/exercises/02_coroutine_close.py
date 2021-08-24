def print_name():

    print("Activated.")

    try:
        while True:
            name = yield
            print(name)

    except GeneratorExit:
        print("Terminated.")


# Get generator object
coroutine = print_name()

# Start coroutine
next(coroutine)

# Sending inputs
coroutine.send("A")
coroutine.send("B")
coroutine.close()
