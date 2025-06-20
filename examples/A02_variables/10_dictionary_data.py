# Dictionary data
# ------------------------------------------------------------------------------
# This code creates and manipulates dictionaries in Python. A dictionary is
# a collection of key–value pairs where each key is unique. If a key
# appears more than once, the last assigned value is retained. The
# dictionary variable has the following properties:
#
# - Passed by reference: Changes to one variable affect all references
# - Key access: You can access values using their keys
# - Unique keys: Each key must be unique within the dictionary
# - Mutable: Can be modified after creation
# - Ordered: The order of inserted items is maintained (as of Python 3.7)
# - Heterogeneous: Can contain keys and values of different types

# Passed by reference (changes to one variable affect all references)
d1 = {'junior': 1, 'mid': 2, 'senior': 3}
d2 = d1
d2['junior'] = 4
print(d1, d2)
# Output: {'junior': 4, 'mid': 2, 'senior': 3} {'junior': 4, 'mid': 2, 'senior': 3}

# Key access
a = {'junior': 1, 'mid': 2, 'senior': 3}
print(a['mid'])
# Output: 2

# Only unique keys (last one wins)
b = {'junior': 1, 'mid': 2, 'senior': 3, 'senior': 4}
print(b)
# Output: {'junior': 1, 'mid': 2, 'senior': 4}

# Mutable
c = {'junior':1, 'mid': 2}
c.update({'senior': 3})
print(c)
# Output: {'junior': 1, 'mid': 2, 'senior': 3}

# Ordered (as of Python 3.7)
d = {'mid': 2, 'senior': 3, 'junior': 1}
print(d)
# Output: {'mid': 2, 'junior': 1, 'senior': 3}

# Heterogeneous
e = {'junior': 1, 'mid': 2.5, 'senior': 'three'}
print(e)
# Output: {'junior': 1, 'mid': 2.5, 'senior': 'three'}
