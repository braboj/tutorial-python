# Handling a variable number of arguments in Python 2
# -----------------------------------------------------------------------------
# Demonstrates capturing extra positional arguments with `*args` and
# extra keyword arguments with `**kwargs` when keyword-only parameters are
# unavailable.  In Python 3 you can declare keyword-only parameters using
# the `*` separator instead of relying on `**kwargs`.  See
# `func_variable_arguments_python3.py` for comparison.

def variable_number_of_arguments(a, b, *args, **kwargs):
    print("a: {a}".format(a=a))
    print("b: {b}".format(b=b))
    print("args: {args}".format(args=args))
    print("kwargs: {kwargs}".format(kwargs=kwargs))


variable_number_of_arguments(1, 2, 3, c=4)
