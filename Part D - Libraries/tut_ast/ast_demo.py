from __future__ import print_function

import ast, pprint

a = [0xfor x in (1, 2, 3)]
b = [0xf or x in (1, 2, 3)]
c = [0xf or (x in (1, 2, 3))]

"""
Explanation
1. Get token reads 0xf
2. Or is lazy and stops when the left operand is true
3. Value is 0xF
"""

print(a, b, c)

try:
    [x in (1, 2, 3) or 0xf]
except NameError:
    print("Now x is evaluated and the expected NameError is raised")


parsed = ast.parse('0xfor x in (1, 2, 3)', mode='eval')
print(ast.dump(parsed))