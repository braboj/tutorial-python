class Fruits:
    def __init__(self):
        self.names = ['apple', 'banana', 'cherry']

    def __len__(self):
        return len(self.names)

    def __iter__(self):
        return FruitIterator(self)


class FruitIterator:
    def __init__(self, fruits):
        self.__fruits = fruits
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__fruits):
            raise StopIteration

        # return the next fruit
        fruit = self.__fruits.names[self.__index]
        self.__index += 1
        return fruit


fruits = Fruits()

for fruit in fruits:
    print(fruit)
