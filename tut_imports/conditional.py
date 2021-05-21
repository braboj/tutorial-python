import sys

# Option 1
try:
    import Queue as test1
except ImportError:
    import queue as test1

q = test1.Queue()
print(q)

# Option 2
is_py2 = sys.version[0] == '2'
if is_py2:
    import Queue as test2
else:
    import queue as test2

q = test2.Queue()
print(q)
