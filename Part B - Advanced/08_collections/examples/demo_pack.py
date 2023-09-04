numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))

unzipped = zip(*zipped)
print(unzipped)
