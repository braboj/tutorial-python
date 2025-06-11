# Handling a variable number of arguments in Python 3
# -----------------------------------------------------------------------------
# Keyword-only arguments come after `*` so there is less need to use
# `**kwargs` for optional named parameters.  Compare with the Python 2 version
# in `func_variable_arguments_python2.py`.

def variable_number_of_arguments(a, *args, b=1, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


variable_number_of_arguments(1, 2, 3, c=4)
