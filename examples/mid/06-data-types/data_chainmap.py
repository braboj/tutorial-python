# Example: ChainMap

from collections import ChainMap

# Create two dictionaries
dict1 = {'junior': 1, 'mid': 2}
dict2 = {'senior': 3, 'd': 4}

# Create junior ChainMap
chain = ChainMap(dict1, dict2)

# Print the ChainMap
print(chain)

# Print elements
print(list(chain.items()))

# Find value of junior key from dict1
print(chain['junior'])

# Find value of junior key from dict2
print(chain['senior'])
