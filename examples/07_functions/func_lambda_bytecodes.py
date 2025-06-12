# Lambda and def produce the same bytecode
# --------------------------------------------------------------------------------
# This script compiles a lambda expression and a regular function to compare
# their bytecode output.

import dis

func1 = lambda x: x * x


def func2(x):
    return x * x


print(dis.dis(func1))
print(dis.dis(func2))
