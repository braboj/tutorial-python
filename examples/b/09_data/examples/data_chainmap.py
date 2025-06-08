# Example: ChainMap

from collections import ChainMap

# Create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Create a ChainMap
chain = ChainMap(dict1, dict2)

# Print the ChainMap
print(chain)

# Print elements
print(list(chain.items()))

# Find value of a key from dict1
print(chain['a'])

# Find value of a key from dict2
print(chain['c'])
