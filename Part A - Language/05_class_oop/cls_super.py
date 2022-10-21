class Animal:
    def __init__(self, animal):
        print(animal, 'is an animal.')


class Mammal(Animal):
    def __init__(self, animal):
        print(animal, 'is a warm-blooded animal.')
        super(Mammal, self).__init__(animal)


class NonWingedMammal(Mammal):
    def __init__(self, animal):
        print(animal, "can't fly.")
        super(NonWingedMammal, self).__init__(animal)


class NonMarineMammal(Mammal):
    def __init__(self, animal):
        print(animal, "can't swim.")
        super(NonMarineMammal, self).__init__(animal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super(NonMarineMammal, self).__init__('Dog')


dog = Dog()
bat = NonMarineMammal('Bat')