# Mixing positional arguments with keyword-only arguments
# --------------------------------------------------------------------------------
# Python 3 lets you combine regular positional parameters with ``*args`` and
# keyword-only parameters that have default values. The `*` separator defines
# that the positional parameters until a key-value pair is encountered.

def variable_number_of_arguments(a, *args, b=1, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


variable_number_of_arguments(1, 2, 3, c=4)
