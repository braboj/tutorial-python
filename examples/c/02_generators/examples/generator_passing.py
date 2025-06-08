# Example: Generator Passing

def generator():
    yield 1
    yield 2
    yield 3


def wrapper(g):
    yield from g


for x in wrapper(generator()):
    print(x, end=", ")
