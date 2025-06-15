# 2_memory_footprint

```python
import sys

# Create list comprehension and print size
l = [i for i in range(10)]
print("List size is {0}".format(sys.getsizeof(l)))

# Print items
for x in l:
    print(x)

# Create generator expression and print size
g = (k for k in range(10))
print("")
print("Generator expression size is {0}".format(sys.getsizeof(g)))

# Print items
for x in g:
    print(x)
```
