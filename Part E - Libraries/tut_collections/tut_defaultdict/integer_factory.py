from collections import defaultdict

s = "mississippi"

d = defaultdict(int)

# Show that each key is initialized using int()
for key in s:
    d[key] = d[key]

print(sorted(d.items()))

# Use default dictionary as an occurrence counter
for key in s:
    d[key] += 1

print(sorted(d.items()))