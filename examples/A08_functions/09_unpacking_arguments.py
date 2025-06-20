# Argument unpacking with `*args`
# ------------------------------------------------------------------------------
# When calling a function, the star operator can expand an iterable into
# positional arguments. This allows you to store the arguments in a list or
# other iterable and pass them all at once.

def my_function(a, b, c):
    print(a, b, c)


args = [1, 2, 3]
my_function(*args)
