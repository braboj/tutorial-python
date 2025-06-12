# Keyword-only arguments
# --------------------------------------------------------------------------------
# Demonstrates keyword-only arguments.

# The arguments a and b are keyword-only
def keyword_only_arguments(*, a, b):
    return a + b


# The argument a is positional or keyword, b is keyword-only
def one_keyword_only_argument(a, *, b):
    return a + b


# The argument a is positional only, b is keyword-only
def separate_arguments(a, /, *, b):
    return a + b
