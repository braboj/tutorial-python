"""
* Unpacks tuples, lists
** Unpacks dictionaries

https://codingfordata.com/6-essential-python-tuple-unpacking-techniques-you-can-use/
https://stackoverflow.com/questions/40676085/why-cant-i-use-a-starred-expression
https://geekflare.com/python-unpacking-operators/
"""


# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)


# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
# a-> 1, b->2, c->3, d->4
fun(*my_list)

# Error when len(args) != no of actual arguments
# required by the funcntion

my_list = [0, 1, 4, 9]


def func(a, b, c, *args):
    print(a + b + c + sum(args))


# calling function with unpacking args
func(*my_list)
