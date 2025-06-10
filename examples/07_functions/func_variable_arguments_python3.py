def variable_number_of_arguments(a, *args, b=1, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


variable_number_of_arguments(1, 2, 3, c=4)
