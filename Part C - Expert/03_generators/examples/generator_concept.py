# Subroutine returning a collection object
def sub_even_numbers(stream):
    them = []
    for n in stream:
        if n % 2 == 0:
            them.append(n)
    return them


# Generator function which generates a sequence of values
def gen_even_numbers(stream):
    for n in stream:
        if n % 2 == 0:
            yield n


if __name__ == "__main__":

    # Get the even numbers using the subroutine
    result = sub_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(result)

    # Get the even numbers using the generator function
    result = gen_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for x in result:
        print(x, end=" ")
