class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __len__(self):
        return len(self.rgb)

    def __iter__(self):
        return ColorIterator(self)

class ColorIterator:
    def __init__(self, colors):
        self.__colors = colors
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__colors):
            raise StopIteration

        # return the next color
        color = self.__colors.rgb[self.__index]
        self.__index += 1
        return color


colors = Colors()

for color in colors:
    print(color)
