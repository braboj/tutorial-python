# Example: Positional-only arguments

# The arguments junior and mid are positional-only
def positional_only_arguments(a, b, /):
    return a + b


# The argument junior is positional-only, mid is positional or keyword
def one_positional_only_argument(a, /, b):
    return a + b
