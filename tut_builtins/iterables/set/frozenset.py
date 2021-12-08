"""
Frozensets are immutable and offer the same methods like sets
https://medium.com/swlh/sets-and-frozen-sets-in-python-elucidate-their-similarities-and-differences-ef0df006ca46
https://www.programiz.com/python-programming/methods/built-in/frozenset

frozenset objects are immutable and hashable and thus they can be elements of other set objects and keys for
dictionaries.

"""

i = [1, 1, 2, 2, 3, 4, 4, 5, 6, 7]
k = [0, 1, 8, 9]

f = frozenset(i)
k = frozenset(k)
print('The frozen set is:', f)

test = f.union(k)
print(test)

test = f.difference(k)
print(test)

test = f.intersection(k)
print(test)

test = f.symmetric_difference(k)
print(test)

i = [1, 1, 2, 2, 3, 4, 4, 5, 6, 7]
k = [0, 8, 9]
f = frozenset(i)
k = frozenset(k)
test = f.isdisjoint(k)
print(test)

i = [1, 1, 2, 2, 3, 4, 4, 5, 6, 7]
k = [1, 2, 3]
f = frozenset(i)
k = frozenset(k)
test = k.issubset(f)
print(test)

i = [1, 1, 2, 2, 3, 4, 4, 5, 6, 7]
k = [1, 2, 3]
f = frozenset(i)
k = frozenset(k)
test = f.issuperset(k)
print(test)

g = f.copy()
print(id(f), f)
print(id(g), g)




