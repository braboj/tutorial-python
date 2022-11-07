def func_A(x):
    # Function uses and returns only positive values
    if x < 0:
        # Simulate error condition
        return -1
    else:
        return 1


def func_B(x):
    # Functions uses and returns only negative values
    if x > 0:
        # Simulate error condition
        return 1
    else:
        return -1


def main(value):

    # Each function must have a check of the error condition
    # as there is no standard definition of an error

    # Check A
    error = func_A(value)
    if error < 0:
        print("STEP A: ERROR")
    else:
        print("STEP A: OK")

    # Check B
    error = func_B(value)
    if error > 0:
        print("STEP B: ERROR")
    else:
        print("STEP B: OK")


main(1)
main(0)
main(-1)
