i = ("a", "b", "c")

e = enumerate(iterable=i, start=1)
print(e, list(e))

for count, item in enumerate(i):
  print(count, item)