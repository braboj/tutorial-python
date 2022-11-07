class MyException(Exception):
    pass


def main():
    try:
        print("main")
        func_A()
    except Exception as e:
        print(e)


def func_A():
    # Explicit chaining using `raise`
    try:
        print("func A")
        func_B()
    except Exception as e:
        # Convert to another exception type
        raise MyException(e)


def func_B():
    # Unhandled exceptions sent to the caller by default
    print("func B")
    read_file()


def read_file():
    print("read_file")
    raise Exception("Error raised in readFile()")


main()