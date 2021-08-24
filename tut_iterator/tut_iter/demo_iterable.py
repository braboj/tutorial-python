"""
* An iterable is an object that implements the __iter__ method which returns an iterator.
* An iterator is an object that implements the __iter__ method which returns itself and the __next__ method which
returns the next element.

https://www.pythontutorial.net/advanced-python/python-iterator-vs-iterable/

"""


##################################################################################################
# ITERABLE CLASS
##################################################################################################

class Colors(object):
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __iter__(self):
        return ColorIterator(self)


##################################################################################################
# ITERATOR CLASS
##################################################################################################

class ColorIterator(object):
    def __init__(self, colors):
        self.__colors = colors
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.next()

    def next(self):
        try:
            color = self.__colors.rgb[self.__index]
            self.__index += 1
        except IndexError:
            raise StopIteration

        return color


##################################################################################################
# DEMO
##################################################################################################

c = Colors()
print(c)

c_iter = iter(c)
print(c_iter)

for element in c_iter:
    print(element)