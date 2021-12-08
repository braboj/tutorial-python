"""
set(iterable)
"""

# empty set
print(set())

# from string
print(set('Python'))

# from tuple
test = ('a', 'e', 'i', 'o', 'u')
print(set(test))

# from list
test = ['a', 'e', 'i', 'o', 'u']
print(set(test))

# from range
print(set(range(5)))

# from set
test = {'a', 'e', 'i', 'o', 'u'}
print(set(test))

# from dictionary
test = {'a':1, 'e': 2, 'i':3, 'o':4, 'u':5}
print(set(test))

# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print(set(frozen_set))


class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num


# print_num is an iterable
print_num = PrintNumber(5)

# creating a set
print(set(print_num))