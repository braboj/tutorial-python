# Example: Nested generator

def inner_generator(n):
    for j in range(n):
        yield "Inner Value {}".format(j)


def outer_generator(n):
    for i in range(n):
        yield "Outer Value {}".format(i)
        for inner_value in inner_generator(i):
            yield inner_value


# Usage
n = 3
for value in outer_generator(n):
    print(value)
