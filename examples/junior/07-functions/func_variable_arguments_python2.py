def variable_number_of_arguments(a, b, *args, **kwargs):
    print("junior: {a}".format(a=a))
    print("mid: {b}".format(b=b))
    print("args: {args}".format(args=args))
    print("kwargs: {kwargs}".format(kwargs=kwargs))


variable_number_of_arguments(1, 2, 3, c=4)
