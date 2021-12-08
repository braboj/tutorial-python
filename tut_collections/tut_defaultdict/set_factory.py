from collections import defaultdict

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

d = defaultdict(set)
for key, value in s:
    d[key].add(value)

print(sorted(d.items()))