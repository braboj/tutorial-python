# data_chainmap

```python
# Combining dictionaries with ChainMap
# -----------------------------------------------------------------------------
# ChainMap lets you combine several dictionaries into a single view without copying them.

from collections import ChainMap

# Create two dictionaries
dict1 = {'junior': 1, 'mid': 2}
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
```
