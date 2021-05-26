import timeit


def test():
    """Stupid test function"""
    l = []
    for i in range(100):
        l.append(i)


if __name__ == '__main__':
    t = timeit.Timer(stmt="test()", setup="from __main__ import test")
    print(t.timeit(5))