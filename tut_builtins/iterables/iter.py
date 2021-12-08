"""
https://www.programiz.com/python-programming/methods/built-in/iter

iter(iterable) -> iterator
iter(callable, sentinel) -> iterator

Get an iterator from an object.  In the first form, the argument must supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel.

The iter() function returns an iterator object for the given object.

If the user-defined object doesn't implement __iter__(), and __next__() or __getitem()__,
the TypeError exception is raised. If the sentinel parameter is also provided, iter() returns an iterator until the
sentinel character isn't found.


"""


##############################################################################
# ITER : FIRST FORM (iterable)
##############################################################################

class PrintNumber:
    def __init__(self, maximum):
        self.maximum = maximum
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.maximum:
            raise StopIteration
        self.num += 1
        return self.num


# Usecase iter with iterable as argument
my_iter = iter(PrintNumber(3))
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break

# Equivalent code
a = iter(PrintNumber(3))
while True:
    try:
        b = a.__next__()
    except StopIteration:
        break


##############################################################################
# ITER : SECOND FORM (callable with sentinel)
##############################################################################

class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        if self.start >= pow(2, 20):
            raise StopIteration
        return self.start

    def __call__(self):
        return self.__next__()


# Usecase with callable and sentinel as arguments
my_iter = iter(DoubleIt(), 16)
for x in my_iter:
    print(x)

# Equivalent code when iter used with sentinel
a = DoubleIt()
while True:
    b = a.__call__()    # or also a()
    if b >= 16:
        break
    print(b)


##############################################################################
# EXAMPLE A : NESTED ITERATOR
##############################################################################

class NestedIterator(object):

    class MyIter(object):

        def __init__(self):
            pass

        def __iter__(self):

            # Initialized with each iter call
            self.start = 1
            return self

        def __next__(self):
            self.start *= 2
            if self.start >= pow(2, 20):
                raise StopIteration
            return self.start

    def __init__(self):

        self.a = 1
        self.b = 2

    def __iter__(self):
        self.my_iter = self.MyIter()
        return self.my_iter


a = iter(NestedIterator())
for x in a:
    print(x)
