# data_counter_class

```python
# Counting with Counter
# -----------------------------------------------------------------------------
# A Counter is a dictionary subclass for tallying hashable objects quickly.

from collections import Counter

# Create a Counter object
a = Counter('abcdeabcdabcaba')
b = Counter(reversed("abcdeabcdabcaba"))

# Print the Counter object
print(a)
print(b)

# Print the three most common element
print(a.most_common(3))
print(b.most_common(3))

# Add two Counter objects
c = a + b
print(c)

# Subtract two Counter objects
d = a - b
print(d)
```
