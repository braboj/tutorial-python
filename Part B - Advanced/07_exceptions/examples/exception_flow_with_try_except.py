# Example: Exception Flow with try-except statements
def func_A(x):
    # Function uses and returns only positive values
    if x < 0:
        # Simulate error condition
        raise ValueError("STEP A: ERROR")
    else:
        return 1


def func_B(x):
    # Functions uses and returns only negative values
    if x > 0:
        # Simulate error condition
        raise ValueError("STEP B: ERROR")
    else:
        return -1


def app(value):

    # Try to execute STEP B
    try:
        func_A(value)
        func_B(value)

    # On error print something
    except ValueError as e:
        print(e)

    # Try to execute STEP B
    try:
        func_B(value)
        print("STEP B: OK")

    # On error print something
    except ValueError as e:
        print(e)


app(1)
app(0)
app(-1)
