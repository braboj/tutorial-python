# Example: Unpacking Arguments using the * operator and ** operator

# A list of arguments
pos_args = [1, 2, 3, 4]
keyword_args = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# A sample function that takes 4 arguments
# and prints the,
def func1(a, b, c, d):
    print(a, b, c, d)


# Variable number of arguments
def func2(a, b, c, d, *args):
    print(a + b + c + d + sum(args))


# Variable number of keyword arguments
def func3(**kwargs):
    print(kwargs['a'] + kwargs['b'] + kwargs['c'] + kwargs['d'])


func1(*pos_args)
func2(*pos_args)
func3(**keyword_args)

# test = "PYTHON"
# unpacked = [*test]
# print(unpacked)
