vowels = 'aeiou'
test = reversed(vowels)
print(test)
print(list(test))

vowels = ['a', 'e', 'i', 'o', 'u']
test = reversed(vowels)
print(test)
print(list(test))

vowels = ('a', 'e', 'i', 'o', 'u')
test = reversed(vowels)
print(test)
print(list(test))


class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)


v = Vowels()
test = reversed(v)
print(test)
print(list(test))