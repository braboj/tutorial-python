# Exception Chaining
# ------------------------------------------------------------------------------
# Demonstrates explicit and implicit chaining of exceptions to preserve the
# original error context.

class MyException(Exception):
    pass


def main():
    try:
        print("main")
        func_a()
    except Exception as e:
        print(e)


def func_a():
    # Explicit chaining using `raise`
    try:
        print("func_a")
        func_b()
    except Exception as e:
        # Convert to another exception type
        raise MyException(e)


def func_b():
    # Unhandled exceptions sent to the caller by default
    print("func_b")
    read_file()


def read_file():
    print("read_file")
    raise Exception("Error raised in read_file()")


main()
