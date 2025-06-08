# Example: Zipping Data using the zip() function

# Sample data
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# Zip two lists
zipped = zip(numbers, letters)
zipped_list = list(zipped)
print(zipped_list)

# Unzip into two lists
unzipped = zip(*zipped_list)
numbers, letters = map(list, unzipped)
print(numbers)
print(letters)
