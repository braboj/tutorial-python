# Example: Positional-only arguments

# The arguments a and b are positional-only
def positional_only_arguments(a, b, /):
    return a + b


# The argument a is positional-only, b is positional or keyword
def one_positional_only_argument(a, /, b):
    return a + b
