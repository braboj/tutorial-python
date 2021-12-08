from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)
for key, value in s:
    d[key].append(value)

print(sorted(d.items()))