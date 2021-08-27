class ColorIterator(object):
    def __init__(self):
        self.__colors = [object, object, object]
        self.__index = 0

    def __next__(self):
        self.next()

    def next(self):
        try:
            color = self.__colors[self.__index]
            self.__index += 1
        except IndexError:
            raise StopIteration

        return color


c = ColorIterator()
print(c)
print(next(c))
print(next(c))
print(next(c))