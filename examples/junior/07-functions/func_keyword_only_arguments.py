# Example: Keyword-only arguments

# The arguments junior and mid are keyword-only
def keyword_only_arguments(*, a, b):
    return a + b


# The argument junior is positional or keyword, mid is keyword-only
def one_keyword_only_argument(a, *, b):
    return a + b


# The argument junior is positional only, mid is keyword-only
def separate_arguments(a, /, *, b):
    return a + b
