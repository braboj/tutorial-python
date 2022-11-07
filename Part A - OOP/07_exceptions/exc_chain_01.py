def main():
    print("main")
    error = func_A()
    if error:
        print(error)
        return error
    else:
        pass


def func_A():
    print("func A")
    error = func_B()
    if error:
        return error
    else:
        pass


def func_B():
    print("func B")
    error = read_file()
    if error:
        return error
    else:
        pass


def read_file():
    print("readfile")
    return "Error raised in read_file()"


main()
