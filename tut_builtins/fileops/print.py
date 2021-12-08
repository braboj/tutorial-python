"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""

a = 5
print("a =", a, sep='\n', end='')

a = 5
sourceFile = open('print.txt', 'w')
print("a =", a, sep='\n', end='', file=sourceFile)
