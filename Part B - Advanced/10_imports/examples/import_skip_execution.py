# Example: Main program


def func1():
    return 1


def func2():
    return 2


def func3():
    return 3


def test_module():
    assert func1() == 1
    assert func2() == 2
    assert func3() == 3


# The following code prevents the module to be executed when imported as a
# module. It will be executed only when run as a script directly by the Python
# interpreter. If omitted the module will be executed on each import.

if __name__ == '__main__':
    test_module()

