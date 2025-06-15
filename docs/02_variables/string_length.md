# string_length

```python
# Calculate the length of a string
# --------------------------------------------------------------------------------
# This snippet calculates the number of characters in a string. The
# result differs from the byte length when the string contains UTF-8
# characters that use multiple bytes.

text = "0123456789"
print(len(text))
# Output:
# 10

text = 'Здравей!'
print(len(text))
# Output:
# 8
```
