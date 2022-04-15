"""
http://p-nand-q.com/python/lambda.html
"""

###############################################################################
# Syntax

"""
lambda [param1, param2, ..]: expression

Lambda functions are one-line functions which return an expression using the
pre-defined parameters param1, param2, ... paramN.

Lambda functions are normally used for quick data operations on data, most
notably in combination with map, filter, reduce.
 
"""

data_in = [1, 2, 3]
data_out = map(lambda x: x*x, data_in)
print(data_in, data_out)

###############################################################################
# Demonstrate that both lamda and def return the same result

print("#" * 80)
print("")


func1 = lambda x: x*x


def func2(x):
    return x*x


print('Using lambda: ', func1(5))
print(map(func1, [1, 2, 3]))

print('Using def: ', func2(5))
print(map(func2, [1, 2, 3]))

###############################################################################
# Demostrate that the assembly code is the same

import dis

print("#" * 80)
print("")

print(dis.dis(func1))
print(dis.dis(func2))

###############################################################################
# Some examples

# Multi-parameter lambda
x = lambda a, b, c, d, e: (a + b) * (c + d) / e
print(x(1, 2, 3, 4, 5))

# Conditional lambda
y = lambda b: 1 if b > 0 else 0
print(y(-1), y(0), y(1))

# Nested conditional lambda
z = lambda c: 1 if c > 0 else (0 if c == 0 else -1)
print(z(-1), y(0), y(1))